import pandas as pd
import os

# 指定檔案所在資料夾
folder_path = 'D:/CCC/'  # 替換成實際的資料夾路徑

# 處理每個檔案
for i in range(1, 6):
    for j in range(1, 23):
        file_name = f'group_{i}_{j}.csv'
        file_path = os.path.join(folder_path, file_name)

        # 讀取 CSV 檔案
        data = pd.read_csv(file_path)

        # 複製第四列到第五列
        data['之前的基地台數量'] = data.iloc[:, 3]

        # 將第四列的數值上移一格
        data.iloc[1:, 3] = data.iloc[:-1, 3].values

        # 更換第四列的名稱
        data.rename(columns={data.columns[3]: '之前的基地台數量'}, inplace=True)

        # 保存修改後的數據到新的 CSV 檔案
        output_file_path = os.path.join(folder_path, f'modified_{file_name}')
        data.to_csv(output_file_path, index=False)

        print(f"檔案 {file_name} 修改完成，結果保存到 {output_file_path}")
