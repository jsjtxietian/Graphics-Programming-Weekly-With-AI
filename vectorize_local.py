import os
import json
import glob
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

# git clone https://www.modelscope.cn/sentence-transformers/all-MiniLM-L6-v2.git
# 配置
INPUT_DIR = "gpw_clean_notes"
OUTPUT_FILE = "gpw_index.json"

# ModelScope 上的模型 ID (通常和 HF 一致)
# all-MiniLM-L6-v2 在魔搭上的 ID 也是这个
MODEL_ID = 'sentence-transformers/all-MiniLM-L6-v2'

def main():
    # 2. 加载模型
    # SentenceTransformer 支持直接加载本地文件夹
    print("Loading model into memory...")
    model = SentenceTransformer('../Models/all-MiniLM-L6-v2')

    # 3. 读取所有 Markdown 文件
    files = glob.glob(os.path.join(INPUT_DIR, "*.md"))
    if not files:
        print(f"Error: No markdown files found in {INPUT_DIR}")
        return

    print(f"Found {len(files)} notes. Reading content...")
    
    documents = []
    texts_to_embed = []

    for filepath in files:
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        documents.append({
            "id": filename,
            "content": content
        })
        texts_to_embed.append(content)

    # 4. 批量计算向量
    print("Calculating embeddings locally...")
    # normalize_embeddings=True 确保后续点积计算就是余弦相似度
    embeddings = model.encode(texts_to_embed, batch_size=64, show_progress_bar=True, normalize_embeddings=True)

    # 5. 构建并保存索引
    print("Building index...")
    index_data = []
    
    for i, doc in enumerate(documents):
        # 转为 list 并保留 4 位小数
        vec = [round(float(x), 4) for x in embeddings[i]]
        
        index_data.append({
            "id": doc['id'],
            "content": doc['content'],
            "vector": vec
        })

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False)

    print(f"Done! Saved index to {OUTPUT_FILE}")
    print(f"Total size: {os.path.getsize(OUTPUT_FILE) / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    main()