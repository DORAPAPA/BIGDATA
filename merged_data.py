import pandas as pd

# 建立一個空的 DataFrame，稍後用於存儲合併的數據
merged_data = pd.DataFrame()

# 合併 22 個 CSV 檔案
for i in range(1, 23):
    file_path = f'final_no_dot_final_modified_group_4_{i}.csv'
    data = pd.read_csv(file_path)
    merged_data = pd.concat([merged_data, data], ignore_index=True)

# 存儲合併的數據到一個新的 CSV 檔案
merged_data.to_csv('merged_data4.csv', index=False)
