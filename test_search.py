import json
import numpy as np
import os
from sentence_transformers import SentenceTransformer

# === 配置 ===
INDEX_FILE = "gpw_index.json"
MODEL_ID = 'sentence-transformers/all-MiniLM-L6-v2'

def load_data():
    print(f"Loading index from {INDEX_FILE}...")
    try:
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ 找不到索引文件，请检查路径！")
        return None, None

    # 预处理：将所有向量提取为一个巨大的 Numpy 矩阵 (N, 384)
    # 这样计算速度比循环快几百倍
    print("Building vector matrix...")
    corpus_ids = [item['id'] for item in data]
    corpus_content = [item['content'] for item in data]
    corpus_vectors = np.array([item['vector'] for item in data], dtype='float32')
    
    return {
        "ids": corpus_ids,
        "content": corpus_content,
        "vectors": corpus_vectors,
        "raw_data": data # 保留原始数据以备查看
    }

def load_model():
    print("Loading model from ModelScope...")
    model = SentenceTransformer('./all-MiniLM-L6-v2')
    return model

def search(query_vector, db, top_k=10, exclude_id=None):
    """
    核心搜索函数：计算余弦相似度并排序
    """
    # 1. 计算所有向量与 Query 的点积 (Dot Product)
    # 因为我们在生成时已经做了 normalize，所以点积 = 余弦相似度
    scores = np.dot(db['vectors'], query_vector)
    
    # 2. 排序 (argsort 返回的是从小到大的索引，所以要取反)
    # 取前 k+1 个，因为如果是文件搜索，第一名肯定是自己，需要排除
    top_indices = np.argsort(scores)[::-1][:top_k+1]
    
    results = []
    for idx in top_indices:
        file_id = db['ids'][idx]
        
        # 如果是搜相似文件，排除掉自己
        if exclude_id and file_id == exclude_id:
            continue
            
        score = scores[idx]
        # 提取标题 (content 的第一行)
        first_line = db['content'][idx].split('\n')[0][:100] 
        
        results.append({
            "score": score,
            "id": file_id,
            "preview": first_line
        })
        
        # 凑够 top_k 就停
        if len(results) >= top_k:
            break
            
    return results

def main():
    # 1. 初始化资源
    db = load_data()
    if not db: return
    model = load_model()
    
    print("\n✅ System Ready! (输入 'q' 退出)")
    print("------------------------------------------------")

    while True:
        mode = input("\n请选择模式 [1] 文字搜索  [2] 相似文件推荐 (输入文件名): ")
        
        if mode.lower() == 'q': break

        # --- 模式 1: 文字搜索 ---
        if mode == '1':
            query = input("🔎 输入搜索关键词 (支持中文/英文): ")
            if not query: continue
            
            # 把文字变成向量
            query_vec = model.encode([query], normalize_embeddings=True)[0]
            
            results = search(query_vec, db, top_k=10)
            
            print(f"\nResults for '{query}':")
            for i, res in enumerate(results):
                print(f"{i+1}. [{res['score']:.4f}] {res['preview']}")
                # print(f"   File: {res['id']}") # 如果想看文件名取消注释

        # --- 模式 2: 相似文件推荐 (More Like This) ---
        elif mode == '2':
            target_file = input("📄 输入要寻找相似的文件名 (例如 Issue422_....md): ")
            
            # 找到这个文件在数据库里的索引
            try:
                idx = db['ids'].index(target_file.strip())
            except ValueError:
                print("❌ 找不到这个文件，请检查文件名是否完全匹配（包含后缀 .md）")
                continue
                
            # 直接拿库里存好的向量，不用重新算
            target_vec = db['vectors'][idx]
            
            print(f"\n与 '{target_file}' 最相似的文章:")
            # 传入 exclude_id 防止搜出它自己
            results = search(target_vec, db, top_k=10, exclude_id=target_file)
            
            for i, res in enumerate(results):
                print(f"{i+1}. [{res['score']:.4f}] {res['preview']}")

if __name__ == "__main__":
    main()