import pandas as pd

# 讀取 CSV 檔案
file_path = 'D:/CCC/111.csv'
data = pd.read_csv(file_path)

# 定義縣市與數字的映射字典，將 '台' 換成 '臺'
city_mapping = {
    '臺北市': 1,
    '新北市': 2,
    '桃園市': 3,
    '臺中市': 4,
    '臺南市': 5,
    '高雄市': 6,
    '基隆市': 7,
    '新竹市': 8,
    '嘉義市': 9,
    '新竹縣': 10,
    '苗栗縣': 11,
    '彰化縣': 12,
    '南投縣': 13,
    '雲林縣': 14,
    '嘉義縣': 15,
    '屏東縣': 16,
    '宜蘭縣': 17,
    '花蓮縣': 18,
    '臺東縣': 19,
    '澎湖縣': 20,
    '金門縣': 21,
    '連江縣': 22
}

# 將縣市列轉換為數字
data['縣市'] = data['縣市'].map(city_mapping)

# 保存轉換後的數據到新的 CSV 檔案
output_file_path = 'your_output_file.csv'
data.to_csv(output_file_path, index=False)

print(f"轉換完成，結果保存到 {output_file_path}")
