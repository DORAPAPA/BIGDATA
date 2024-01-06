import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 讀取CSV檔
file_path = 'D:/CCC/merged_data1.csv'  # 請替換為實際的檔案路徑
data = pd.read_csv(file_path)

# 提取X和Y的數據
X = data.iloc[:, [0, 1, 4]]  # 根據實際的索引值進行調整
Y = data.iloc[:, 3]            # 根據實際的索引值進行調整

# 切分訓練和測試集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 添加截距項
X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)

# 擬合線性回歸模型
model = sm.OLS(Y_train, X_train).fit()

# 預測
Y_pred = model.predict(X_test)

# 計算MSE和R-squared
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

# 打印回歸結果
print(model.summary())

# 繪製預測值 vs. 實際值的散點圖
plt.scatter(Y_test, Y_pred, color='red', label='Predicted')
plt.scatter(Y_test, Y_test, color='blue', label='Actual')

# 顯示回歸線
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], linestyle='--', color='green', linewidth=2, label='Regression Line')

plt.legend()
plt.title('Actual vs. Predicted Values')
plt.xlabel('Actual Y')
plt.ylabel('Predicted Y')
plt.show()

# 顯示MSE和R-squared
print(f'Mean Squared Error (MSE): {mse}')
print(f'R-squared: {r2}')
