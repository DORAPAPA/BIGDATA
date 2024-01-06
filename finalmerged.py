import pandas as pd

# 假設檔案名稱為 merged_data1.csv 到 merged_data5.csv
files = ['merged_data1.csv', 'merged_data2.csv', 'merged_data3.csv', 'merged_data4.csv', 'merged_data5.csv']

# 創建一個空的 DataFrame 用於存儲合併的數據
merged_data = pd.DataFrame()

# 逐一讀取檔案並合併
for file in files:
    data = pd.read_csv(file)
    merged_data = pd.concat([merged_data, data], ignore_index=True)

# 存儲合併後的數據到一個新的 CSV 檔案
merged_data.to_csv('combined_data.csv', index=False)
