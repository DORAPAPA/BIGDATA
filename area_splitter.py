import pandas as pd

# 分割出的五個檔案
file_paths = ['group_1.csv', 'group_2.csv', 'group_3.csv', 'group_4.csv', 'group_5.csv']

for file_path in file_paths:
    # 讀取 CSV 檔案
    data = pd.read_csv(file_path)

    # 根據第一列的值分組
    grouped = data.groupby(data.iloc[:, 0])

    # 將分組後的數據保存到不同的檔案
    for group_name, group_data in grouped:
        output_file_path = f'{file_path.split(".")[0]}_{group_name}.csv'
        group_data.to_csv(output_file_path, index=False)
        print(f'檔案 {output_file_path} 保存成功')
