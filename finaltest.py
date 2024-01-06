import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

# 讀取CSV檔案
file_path = 'D:/CCC/final_no_dot_final_modified_group_1_1.csv'
data = pd.read_csv(file_path)

# 提取X和Y的數據
# 假設第二列、第五列和第四列的索引分別為 1、4、3
X = data.iloc[:, [1, 4]]
Y_actual = data.iloc[:, 3]

# 添加截距項
X = sm.add_constant(X)

# 擬合多變數線性回歸模型
model = sm.OLS(Y_actual, X).fit()

# 獲取預測值
Y_pred = model.predict(X)

# 計算MSE和R-squared
mse = mean_squared_error(Y_actual, Y_pred)
r2 = r2_score(Y_actual, Y_pred)

# 打印回歸結果、MSE和R-squared
print(model.summary())
print(f'Mean Squared Error (MSE): {mse}')
print(f'R-squared: {r2}')

# 繪製預測值 vs. 實際值的散點圖
plt.scatter(Y_actual, Y_pred, color='red', label='Predicted Values')
plt.scatter(Y_actual, Y_actual, color='blue', label='Actual Values')

# 顯示回歸線
plt.plot(Y_actual, Y_pred, linestyle='--', color='red', linewidth=2, label='Regression Line')

plt.title('Actual vs. Predicted Values')
plt.xlabel('Actual Y')
plt.ylabel('Predicted Y')
plt.legend()
plt.show()
