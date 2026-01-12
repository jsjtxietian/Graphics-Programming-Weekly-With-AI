import os
import requests
from tqdm import tqdm

# 配置：Web端需要的模型文件清单
# 我们使用 Xenova 转换的量化版 (Quantized)，体积最小
BASE_URL = "https://hf-mirror.com/Xenova/all-MiniLM-L6-v2/resolve/main"
TARGET_DIR = "models/Xenova/all-MiniLM-L6-v2"

FILES_TO_DOWNLOAD = [
    "config.json",
    "tokenizer.json",
    "tokenizer_config.json",
    "special_tokens_map.json",
    "onnx/model_quantized.onnx" # 关键文件，约 23MB
]

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        print(f"❌ Failed to download {url}")
        return
    
    total_size = int(response.headers.get('content-length', 0))
    
    # 确保子文件夹存在 (比如 onnx/)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, 'wb') as f, tqdm(
        desc=os.path.basename(save_path),
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)

def main():
    print(f"Downloading ONNX model to '{TARGET_DIR}'...")
    
    for file_name in FILES_TO_DOWNLOAD:
        url = f"{BASE_URL}/{file_name}"
        save_path = os.path.join(TARGET_DIR, file_name)
        
        if os.path.exists(save_path):
            print(f"✅ Exists: {file_name}")
            continue
            
        print(f"📥 Downloading: {file_name}")
        download_file(url, save_path)

    print("\n🎉 Download complete! You can now run the web server.")

if __name__ == "__main__":
    main()