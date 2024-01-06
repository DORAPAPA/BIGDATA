import pandas as pd
import os

# 指定檔案所在資料夾
folder_path = 'D:/CCC/'  # 替換成實際的資料夾路徑

# 處理每個檔案
for i in range(1, 6):
    for j in range(1, 23):
        file_name = f'modified_group_{i}_{j}.csv'  # 修改過的檔案名稱
        file_path = os.path.join(folder_path, file_name)

        # 讀取 CSV 檔案
        data = pd.read_csv(file_path)

        # 更換第五列的標題
        data.rename(columns={data.columns[3]: '的基地台數量'}, inplace=True)

        # 保存修改後的數據到新的 CSV 檔案
        output_file_path = os.path.join(folder_path, f'final_{file_name}')
        data.to_csv(output_file_path, index=False)

        print(f"檔案 {file_name} 修改完成，結果保存到 {output_file_path}")
