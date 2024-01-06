import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

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

plt.scatter(Y, model.predict(X), c='red', label='Predicted Values')
plt.scatter(Y, Y, c='blue', label='Actual Values') 
plt.title('Actual vs. Predicted Values')
plt.xlabel('Actual Y')
plt.ylabel('Predicted Y')

# 顯示回歸線
plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], linestyle='--', color='green', linewidth=2, label='Regression Line')

plt.legend()
plt.show()
