import pandas as pd

# 讀取 CSV 檔案
file_path = 'D:/CCC/CCC.csv'
data = pd.read_csv(file_path)

# 定義業者與數字的映射字典
vendor_mapping = {
    '中華電信股份有限公司': 1,
    '台灣大哥大股份有限公司': 2,
    '台灣之星電信股份有限公司': 3,
    '亞太電信股份有限公司': 4,
    '遠傳電信股份有限公司': 5
    # 可根據實際情況繼續添加其他業者
}

# 將業者列轉換為數字
data['業者名稱'] = data['業者名稱'].map(vendor_mapping)

# 保存轉換後的數據到新的 CSV 檔案
output_file_path = 'your_output_file.csv'
data.to_csv(output_file_path, index=False)

print(f"轉換完成，結果保存到 {output_file_path}")
