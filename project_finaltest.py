import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

# 讀取CSV檔
file_path = 'D:/CCC/combined_data.csv'  # 請替換為實際的檔案路徑
data = pd.read_csv(file_path)

# 提取X和Y的數據
X = data.iloc[:, [0, 1, 4]]  # 根據實際的索引值進行調整
Y_actual = data.iloc[:, 3]    # 根據實際的索引值進行調整

# 添加截距項
X = sm.add_constant(X)

# 擬合線性回歸模型
model = sm.OLS(Y_actual, X).fit()

# 預測
Y_pred = model.predict(X)

# 計算MSE、R-squared和MAPE
mse = mean_squared_error(Y_actual, Y_pred)
r2 = r2_score(Y_actual, Y_pred)
mape = (abs((Y_actual - Y_pred) / Y_actual)).mean() * 100

# 打印回歸結果
print(model.summary())

# 繪製預測值 vs. 實際值的散點圖
plt.scatter(Y_actual, Y_pred, color='red', label='Predicted')
plt.scatter(Y_actual, Y_actual, color='blue', label='Actual')

# 顯示回歸線
plt.plot([Y_actual.min(), Y_actual.max()], [Y_actual.min(), Y_actual.max()], linestyle='--', color='green', linewidth=2, label='Regression Line')

# 添加MSE、R-squared和MAPE的數值標籤
text = f'MSE: {mse:.2f}\nR-squared: {r2:.2f}\nMAPE: {mape:.2f}%'
plt.text(Y_actual.min(), Y_actual.max(), text, verticalalignment='bottom', horizontalalignment='left', color='black', fontsize=10)

plt.legend()
plt.title('Actual vs. Predicted Values')
plt.xlabel('Actual Y')
plt.ylabel('Predicted Y')
plt.show()

# 顯示MSE、R-squared和MAPE
print(f'Mean Squared Error (MSE): {mse}')
print(f'R-squared: {r2}')
print(f'MAPE: {mape:.2f}%')
