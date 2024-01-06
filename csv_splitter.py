import pandas as pd

# 讀取 CSV 檔案
file_path = 'D:/CCC/HHH.csv'  # 替換成實際的檔案路徑
data = pd.read_csv(file_path)

# 根據第一與第四欄分成檔案
subset_1_4 = data[['縣市', '基地臺']]
subset_1_4.to_csv('subset_1_4.csv', index=False)

# 根據第二與第四欄分成檔案
subset_2_4 = data[['統計期', '基地臺']]
subset_2_4.to_csv('subset_2_4.csv', index=False)

# 根據第三與第四欄分成檔案
subset_3_4 = data[['業者名稱', '基地臺']]
subset_3_4.to_csv('subset_3_4.csv', index=False)

print("檔案分割完成")
import pandas as pd

# 讀取 CSV 檔案
file_path = 'your_file.csv'  # 替換成實際的檔案路徑
data = pd.read_csv(file_path)

# 根據第一與第四欄分成檔案
subset_1_4 = data[['column1', 'column4']]
subset_1_4.to_csv('subset_1_4.csv', index=False)

# 根據第二與第四欄分成檔案
subset_2_4 = data[['column2', 'column4']]
subset_2_4.to_csv('subset_2_4.csv', index=False)

# 根據第三與第四欄分成檔案
subset_3_4 = data[['column3', 'column4']]
subset_3_4.to_csv('subset_3_4.csv', index=False)

print("檔案分割完成")
