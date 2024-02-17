#coding:utf-8
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score

# 1. 数据读取和预处理
df = pd.read_csv('D:\\SchoolWork\\行业大数据\\mysite\\web\\algorithm\\data\\jobs_score.csv', encoding='utf-8')
df = df.dropna()  # 去除缺失值
df['能力要求'] = df['能力要求'].apply(lambda x: ' '.join(x.split()))  # 清洗文本数据

# 2. 特征提取和转换
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['能力要求'])

# 3. 聚类模型选择和训练
k = 3  # 聚类的簇数
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(X)

# 4. 聚类结果分析和展示
df['label'] = kmeans.labels_
cluster_size = df['label'].value_counts()
for i in range(len(cluster_size)):
    print(f"Cluster {i}: {cluster_size[i]} samples")

# 计算轮廓系数和DBI指数
silhouette_avg = silhouette_score(X, kmeans.labels_)
db_index = davies_bouldin_score(X.toarray(), kmeans.labels_)
print(f"Average Silhouette Score: {silhouette_avg}")
print(f"Davies-Bouldin Index: {db_index}")

# 可视化聚类结果
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD

svd = TruncatedSVD(n_components=2)
X_2d = svd.fit_transform(X)

plt.scatter(X_2d[:, 0], X_2d[:, 1], c=df['label'])
plt.show()
