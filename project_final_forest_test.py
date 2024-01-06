import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# 讀取CSV檔
file_path = 'D:/CCC/combined_data.csv'  # 請替換為實際的檔案路徑
data = pd.read_csv(file_path)

# 提取X和Y的數據
X = data.iloc[:, [0, 1, 4]]  # 根據實際的索引值進行調整
Y = data.iloc[:, 3]    # 根據實際的索引值進行調整

# 切分訓練和測試集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 添加截距項
X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)

# 擬合線性回歸模型
model = sm.OLS(Y_train, X_train).fit()

# 預測線性回歸
Y_pred_linear = model.predict(X_test)

# 使用隨機森林模型
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, Y_train)

# 預測隨機森林
Y_pred_rf = rf_model.predict(X_test)

# 計算MSE和R-squared
mse_linear = mean_squared_error(Y_test, Y_pred_linear)
r2_linear = r2_score(Y_test, Y_pred_linear)
mape_linear = mean_absolute_error(Y_test, Y_pred_linear) / np.mean(Y_test) * 100

mse_rf = mean_squared_error(Y_test, Y_pred_rf)
r2_rf = r2_score(Y_test, Y_pred_rf)
mape_rf = mean_absolute_error(Y_test, Y_pred_rf) / np.mean(Y_test) * 100

# 顯示回歸結果
print("Linear Regression:")
print(f'Mean Squared Error (MSE): {mse_linear}')
print(f'R-squared: {r2_linear}')
print(f'MAPE: {mape_linear}%\n')

print("Random Forest:")
print(f'Mean Squared Error (MSE): {mse_rf}')
print(f'R-squared: {r2_rf}')
print(f'MAPE: {mape_rf}%')

# 繪製線性回歸預測值 vs. 實際值的散點圖
plt.scatter(Y_test, Y_pred_linear, color='red', label='Linear Regression Predicted')

# 繪製隨機森林預測值 vs. 實際值的散點圖
plt.scatter(Y_test, Y_pred_rf, color='green', label='Random Forest Predicted')

# 顯示回歸線
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], linestyle='--', color='blue', linewidth=2, label='Actual Values')

# 顯示MSE、MAPE、R-squared
plt.text(Y_test.min(), Y_test.max(), f'MSE (Linear): {mse_linear:.2f}\nMAPE (Linear): {mape_linear:.2f}%\nR-squared (Linear): {r2_linear:.2f}', verticalalignment='top', horizontalalignment='left', color='black')
plt.text(Y_test.min(), Y_test.max() - 500, f'MSE (Random Forest): {mse_rf:.2f}\nMAPE (Random Forest): {mape_rf:.2f}%\nR-squared (Random Forest): {r2_rf:.2f}', verticalalignment='top', horizontalalignment='left', color='black')

plt.legend()
plt.title('Actual vs. Predicted Values')
plt.xlabel('Actual Y')
plt.ylabel('Predicted Y')
plt.show()
