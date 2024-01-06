import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 讀取三個CSV檔案
file_paths = ['subset_1_4.csv', 'subset_2_4.csv', 'subset_3_4.csv']

for file_path in file_paths:
    # 讀取 CSV 檔案
    data = pd.read_csv(file_path)

    # 提取X和Y的數據
    X = data.iloc[:, :-1]  # 所有特徵欄位 (除了最後一欄)
    Y = data.iloc[:, -1]   # 最後一欄

    # 添加截距項
    X = sm.add_constant(X)

    # 擬合線性回歸模型
    model = sm.OLS(Y, X).fit()

    # 繪製預測值 vs. 實際值的散點圖
    plt.scatter(Y, model.predict(X), label='預測值', color='red')
    plt.scatter(Y, Y, label='實際值', color='blue')

    # 顯示回歸線
    plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], linestyle='--', color='red', linewidth=2, label='回歸線')

    plt.title(f'多變數線性回歸 - {file_path}')
    plt.xlabel('實際值')
    plt.ylabel('預測值')
    plt.legend()
    plt.show()
