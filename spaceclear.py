import pandas as pd

# 讀取 CSV 檔案
file_path = 'D:/CCC/ZZZ.csv'
data = pd.read_csv(file_path)

# 清除所有列中的空白鍵
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# 保存清除空白鍵後的數據到新的 CSV 檔案
output_file_path = 'your_output_file.csv'
data.to_csv(output_file_path, index=False)

print(f"清除空白鍵完成，結果保存到 {output_file_path}")
