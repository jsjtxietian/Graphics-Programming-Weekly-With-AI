import os
import re
from bs4 import BeautifulSoup
from tqdm import tqdm

# 配置
INPUT_FILE = "origin.html"  # 确保你的 HTML 文件名叫这个
OUTPUT_DIR = "gpw_clean_notes"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def sanitize_filename(text):
    # 文件名只保留安全字符，防止系统报错
    safe_text = re.sub(r'[\\/*?:"<>|]', "", text)
    safe_text = safe_text.replace(" ", "_").strip()
    return safe_text[:100] # 稍微长一点也没事

def extract_date_from_archive(url):
    # 尝试从 archive.org 链接提取日期
    # 格式通常是: .../web/20180514123456/...
    if not url: return "Unknown Date"
    match = re.search(r'web/(\d{4})(\d{2})(\d{2})', url)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return "Unknown Date"

def extract_issue_number(url):
    # 从 summary 链接提取 Issue 号
    if not url: return "0"
    match = re.search(r'issue-(\d+)', url)
    if match:
        return match.group(1)
    return "0"

def save_clean_markdown(item):
    # 文件名: Issue422_Title.md (保持你想要的文件名区分)
    filename = f"Issue{item['issue']}_{sanitize_filename(item['title'])}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # 构造你想要的核心内容
    # 格式：YYYY-MM-DD: [Title](Link) \n\n - Summary...
    content = f"{item['date']}: [{item['title']}]({item['link']})\n\n{item['summary_text']}\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print(f"Reading {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print(f"Error: 找不到 {INPUT_FILE}，请确认文件就在当前目录下。")
        return

    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_='card')
    print(f"Found {len(cards)} cards. Processing...")

    count = 0
    for card in tqdm(cards):
        try:
            # --- 1. 提取 Header 信息 (Title & Link) ---
            header = card.find('h5', class_='accordion-header')
            if not header: continue
            
            link_tag = header.find('a')
            if not link_tag: continue
            
            title = link_tag.get_text(strip=True)
            link = link_tag['href']

            # --- 2. 提取 Body 信息 (Summary & Date & Issue) ---
            body = card.find('div', class_='accordion-body')
            if not body: continue
            
            # 提取 Summary 文本列表
            summary_points = []
            ul = body.find('ul', class_='card-text')
            if ul:
                for li in ul.find_all('li'):
                    txt = li.get_text(strip=True)
                    if txt:
                        summary_points.append(f"- {txt}")
            
            if not summary_points: continue # 如果没有简介，可能是空条目
            
            summary_text = "\n".join(summary_points)

            # 寻找 Archive 链接 (用于提取日期)
            archive_link = body.find('a', href=re.compile(r'web\.archive\.org'))
            date_str = extract_date_from_archive(archive_link['href']) if archive_link else "Unknown Date"
            
            # 寻找 Summary 链接 (用于提取 Issue 号)
            summary_link = body.find('a', href=re.compile(r'issue-\d+'))
            issue_str = extract_issue_number(summary_link['href']) if summary_link else "0"

            # --- 3. 保存 ---
            save_clean_markdown({
                "title": title,
                "link": link,
                "date": date_str,
                "issue": issue_str,
                "summary_text": summary_text
            })
            count += 1

        except Exception as e:
            # print(f"Skipped one card due to error: {e}")
            continue

    print(f"\nDone! Generated {count} clean markdown notes in '{OUTPUT_DIR}/'")

if __name__ == "__main__":
    main()