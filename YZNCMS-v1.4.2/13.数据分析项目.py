import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
df = pd.read_csv('data.csv')

# 数据清洗
# 假设我们删除所有包含缺失值的行
df.dropna(inplace=True)

# 探索性数据分析
# 计算基本的统计数据
print(df.describe())

# 数据可视化
# 创建一个简单的散点图来查看Age和Salary之间的关系
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Salary'])
plt.title('Age vs. Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# 创建一个直方图来查看Salary的分布
plt.figure(figsize=(10, 6))
plt.hist(df['Salary'], bins=20)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()