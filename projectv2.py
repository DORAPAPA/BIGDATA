import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import numpy as np

# 讀取CSV檔
file_path = 'D:/CCC/HHH.csv'
data = pd.read_csv(file_path)

# 提取X和Y的數據
X = data[['縣市', '統計期', '業者名稱']]
Y = data['基地臺']

# 添加截距項
X = sm.add_constant(X)

# 擬合線性回歸模型
model = sm.OLS(Y, X).fit()

# 打印回歸結果
print(model.summary())

# 繪製實際值 vs. 預測值的散點圖，將實際值的點顏色改成藍色，預測值的點顏色改成紅色
plt.scatter(Y, model.predict(X), c='red', label='Predicted Values')
plt.scatter(Y, Y, c='blue', label='Actual Values')  # 這裡使用兩次scatter，分別繪製實際值和預測值

plt.title('Actual vs. Predicted Values')
plt.xlabel('Actual Y')
plt.ylabel('Predicted Y')

# 顯示回歸線
plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], linestyle='--', color='green', linewidth=2, label='Regression Line')

# 計算均方根誤差（Root Mean Squared Error）
rmse = np.sqrt(mean_squared_error(Y, model.predict(X)))

# 顯示預測正確率
plt.text(Y.max(), Y.min(), f'RMSE: {rmse:.2f}', ha='right', va='bottom')

plt.legend()
plt.show()
