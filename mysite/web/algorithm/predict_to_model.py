# coding:gbk
from keras.losses import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
import pickle

data = pd.read_csv('D:\\SchoolWork\\行业大数据\\mysite\\web\\algorithm\\data\\jobs.csv', encoding='gbk')
# 提取特征和目标变量
features = data[['经验要求', '学历要求','城市','职位名称',"福利个数"]]
target = data['平均薪水']
city_mapping={'北京':1,'上海':2,'广州':3,'深圳':4,'杭州':5, '天津':6, '西安':7, '苏州':8, '武汉':9, '厦门':10, '长沙':11, '成都':12, '郑州':13, '重庆':14 }
degree_mapping = {'大专': 0, '本科': 2, '硕士': 4, '博士': 6}
experience_mapping = {'在校/应届': 0, '1年以内': 1, '1-3年': 2, '3-5': 3, '5-10年': 4, '10年以上': 5, '经验不限': 5, }
occupation_mapping = {'java':1, 'python':2, 'cto':3, '技术总监':3, '人工智能':4, 'AI':4, 'BI':5, 'ETL':6, '数据挖掘':7, '数据仓库':8, '数据分析':9 }
welfare_mapping = {1: 1, 2: 2, 3: 3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18, 19:19, 20:20}

features.loc[:, '城市'] = features['城市'].map(city_mapping)
features.loc[:, '学历要求'] = features['学历要求'].map(degree_mapping)
features.loc[:, '经验要求'] = features['经验要求'].map(experience_mapping)
features.loc[:, '职位名称'] = features['职位名称'].map(occupation_mapping)
features.loc[:, '福利个数'] = features['福利个数'].map(welfare_mapping)
# 处理缺失值
imputer = SimpleImputer(strategy='mean')
features = imputer.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 训练线性回归模型且保存模型 160.74
model = LinearRegression()
model.fit(X_train, y_train)
with open('D:\\SchoolWork\\行业大数据\\mysite\\web\\algorithm\\model_linear.pickle', 'wb') as f:
    pickle.dump(model, f)
# 训练决策树模型且保存模型 147.09
model = DecisionTreeRegressor(max_depth=5, random_state=42)
model.fit(X_train, y_train)
with open('D:\\SchoolWork\\行业大数据\\mysite\\web\\algorithm\\model_decision.pickle', 'wb') as f:
    pickle.dump(model, f)
# # 训练随机森林模型且保存模型 144.20
model = RandomForestRegressor(max_depth=5, random_state=42)
model.fit(X_train, y_train)
with open('D:\\SchoolWork\\行业大数据\\mysite\\web\\algorithm\\model_random.pickle', 'wb') as f:
    pickle.dump(model, f)
# # 训练KNN模型且保存模型 151.48
model = KNeighborsRegressor(n_neighbors=26)
model.fit(X_train, y_train)
with open('D:\\SchoolWork\\行业大数据\\mysite\\web\\algorithm\\model_knn.pickle', 'wb') as f:
    pickle.dump(model, f)
# # 训练SVR模型且保存模型 164.73
model = SVR(C = 2,kernel='rbf')
model.fit(X_train, y_train)
with open('D:\\SchoolWork\\行业大数据\\mysite\\web\\algorithm\\model_svr.pickle', 'wb') as f:
    pickle.dump(model, f)

# 预测单个数据
# single_data = np.array([2, 2, 1, 2]).reshape(1, -1)
# single_data = imputer.transform(single_data)
# prediction = model.predict(single_data)
# print("单个数据的预测值为：", prediction[0])

#模型评分
# y_pred = model.predict(X_test)
# # 计算预测结果的 MSE
# mse = mean_squared_error(y_test, y_pred)
# print("模型的均方误差（MSE）：", mse)

# print("over!")


# # 训练线性回归模型
# model = LinearRegression()
# model.fit(X_train, y_train)
# # 训练决策树模型
# model = DecisionTreeRegressor(max_depth=5, random_state=42)
# model.fit(X_train, y_train)
# # 训练随机森林模型
# model = RandomForestRegressor(n_estimators=10, random_state=42)
# model.fit(X_train, y_train)
# # 训练knn模型
# model = KNeighborsRegressor(n_neighbors=26)
# model.fit(X_train, y_train)
# # 训练SVR模型
# model = SVR(C = 2,kernel='rbf')
# model.fit(X_train, y_train)