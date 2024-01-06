import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 讀取三個CSV檔案
file_paths = ['subset_1_4.csv', 'subset_2_4.csv', 'subset_3_4.csv']

for file_path in file_paths:
    # 讀取 CSV 檔案
    data = pd.read_csv(file_path)

    # 提取X和Y的數據
    X = data.iloc[:, 0]  # 第一欄
    Y = data.iloc[:, 1]  # 第二欄

    # 添加截距項
    X = sm.add_constant(X)

    # 擬合線性回歸模型
    model = sm.OLS(Y, X).fit()

    # 預測值
    predictions = model.predict(X)

    # 計算MSE和R-squared
    mse = mean_squared_error(Y, predictions)
    r_squared = r2_score(Y, predictions)

    # 繪製預測值 vs. 實際值的散點圖
    plt.scatter(X.iloc[:, 1], Y, label='實際值', color='blue')
    plt.scatter(X.iloc[:, 1], predictions, label='預測值', color='red')

    # 顯示回歸線
    plt.plot(X.iloc[:, 1], predictions, linestyle='--', color='red', linewidth=2, label='回歸線')

    plt.title(f'線性回歸 - {file_path}\nMSE: {mse:.2f}, R-squared: {r_squared:.2f}')
    plt.xlabel('第一欄')
    plt.ylabel('第二欄')
    plt.legend()
    plt.show()

    print(f'MSE: {mse:.2f}')
    print(f'R-squared: {r_squared:.2f}')
    print('-----------------------------------')
