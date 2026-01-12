import os
import re
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from tqdm import tqdm

# 配置
INPUT_FILE = "origin.html"
OUTPUT_DIR = "gpw_clean_notes"
# 锚点数据 (仅用于日期推算兜底)
ANCHOR_ISSUE = 422
ANCHOR_DATE = datetime(2025, 12, 28)

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def sanitize_filename(text):
    safe_text = re.sub(r'[\\/*?:"<>|]', "", text)
    safe_text = safe_text.replace(" ", "_").strip()
    return safe_text[:100]

def extract_issue_number(url):
    if not url: return 0
    match = re.search(r'issue-?(\d+)', url)
    return int(match.group(1)) if match else 0

def extract_date_from_url(url):
    if not url: return None
    # 模式: 2023/05/14
    match_full = re.search(r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', url)
    if match_full:
        y, m, d = match_full.groups()
        return f"{y}-{int(m):02d}-{int(d):02d}"
    
    # 模式: 2023/05
    match_ym = re.search(r'(\d{4})[-/](\d{1,2})', url)
    if match_ym:
        y, m = match_ym.groups()
        return f"{y}-{int(m):02d}-01"

    # 模式: 2023
    match_year = re.search(r'(\d{4})', url)
    if match_year:
        year = int(match_year.group(1))
        if 2000 < year < 2030:
            return f"{year}-01-01"
    return None

def extract_date_from_archive(url):
    if not url: return None
    match = re.search(r'web/(\d{4})(\d{2})(\d{2})', url)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return None

def estimate_date_from_issue(issue_num):
    if issue_num <= 0: return None
    weeks_diff = issue_num - ANCHOR_ISSUE
    estimated_date = ANCHOR_DATE + timedelta(weeks=weeks_diff)
    return estimated_date.strftime("%Y")

def save_clean_markdown(item):
    # 只有当 issue > 0 时才显示 Issue 号，否则显示 0 (Unknown)
    filename = f"Issue{item['issue']}_{sanitize_filename(item['title'])}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    content = f"{item['date']}: [{item['title']}]({item['link']})\n\n{item['summary_text']}\n"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print(f"Reading {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        return

    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_='card')
    print(f"Found {len(cards)} cards. Processing...")

    count = 0
    
    # === 核心逻辑：Issue 追踪器 ===
    # 用来记住“上一次看到的有效 Issue ID”
    current_tracker_issue = 0 
    
    for card in tqdm(cards):
        try:
            # 1. 提取基础信息
            header = card.find('h5', class_='accordion-header')
            if not header: continue
            link_tag = header.find('a')
            if not link_tag: continue
            title = link_tag.get_text(strip=True)
            link = link_tag['href']

            body = card.find('div', class_='accordion-body')
            if not body: continue
            
            summary_points = []
            ul = body.find('ul', class_='card-text')
            if ul:
                for li in ul.find_all('li'):
                    txt = li.get_text(strip=True)
                    if txt: summary_points.append(f"- {txt}")
            summary_text = "\n".join(summary_points)
            if not summary_text: continue

            # 2. 提取 Issue ID
            summary_link = body.find('a', href=re.compile(r'issue-?\d+'))
            explicit_issue = extract_issue_number(summary_link['href']) if summary_link else 0
            
            # === 状态机逻辑 ===
            if explicit_issue > 0:
                # 遇到了新的 Issue ID，更新追踪器
                current_tracker_issue = explicit_issue
                final_issue = explicit_issue
            else:
                # 没遇到 ID，就用上一次记住的
                # (如果开头第一篇就没有ID，那也没办法，只能是0，但这种情况极少)
                final_issue = current_tracker_issue

            # 3. 提取日期
            archive_link = body.find('a', href=re.compile(r'web\.archive\.org'))
            date_str = extract_date_from_archive(archive_link['href']) if archive_link else None
            
            if not date_str:
                date_str = extract_date_from_url(link)
            
            # 如果日期还是没找到，但我们现在有了推测出来的 Issue ID，就用它来反推日期
            if not date_str and final_issue > 0:
                date_str = estimate_date_from_issue(final_issue)
                
            if not date_str: date_str = "Unknown Date"

            # 4. 保存
            save_clean_markdown({
                "title": title,
                "link": link,
                "date": date_str,
                "issue": final_issue, # 使用推测出的 ID
                "summary_text": summary_text
            })
            count += 1

        except Exception as e:
            continue

    print(f"\nDone! Generated {count} clean markdown notes.")

if __name__ == "__main__":
    main()