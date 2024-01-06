import pandas as pd

# 讀取 CSV 檔案
file_path = 'D:/CCC/isptonum.csv'
  # 替換成實際的檔案路徑
data = pd.read_csv(file_path)

# 根據第三列的值分組
grouped = data.groupby(data.iloc[:, 2])

# 將分組後的數據保存到不同的檔案
for group_name, group_data in grouped:
    output_file_path = f'group_{group_name}.csv'
    group_data.to_csv(output_file_path, index=False)
    print(f'檔案 {output_file_path} 保存成功')
