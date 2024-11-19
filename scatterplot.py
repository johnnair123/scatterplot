import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
iris_df=pd.read_csv("Iris.csv")
print(iris_df.head())
sns.scatterplot(data=iris_df,x='SepalLengthCm',y='SepalWidthCm',hue="Species")
plt.show()