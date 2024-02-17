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

data = pd.read_csv('D:\\SchoolWork\\��ҵ������\\mysite\\web\\algorithm\\data\\jobs.csv', encoding='gbk')
# ��ȡ������Ŀ�����
features = data[['����Ҫ��', 'ѧ��Ҫ��','����','ְλ����',"��������"]]
target = data['ƽ��нˮ']
city_mapping={'����':1,'�Ϻ�':2,'����':3,'����':4,'����':5, '���':6, '����':7, '����':8, '�人':9, '����':10, '��ɳ':11, '�ɶ�':12, '֣��':13, '����':14 }
degree_mapping = {'��ר': 0, '����': 2, '˶ʿ': 4, '��ʿ': 6}
experience_mapping = {'��У/Ӧ��': 0, '1������': 1, '1-3��': 2, '3-5': 3, '5-10��': 4, '10������': 5, '���鲻��': 5, }
occupation_mapping = {'java':1, 'python':2, 'cto':3, '�����ܼ�':3, '�˹�����':4, 'AI':4, 'BI':5, 'ETL':6, '�����ھ�':7, '���ݲֿ�':8, '���ݷ���':9 }
welfare_mapping = {1: 1, 2: 2, 3: 3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18, 19:19, 20:20}

features.loc[:, '����'] = features['����'].map(city_mapping)
features.loc[:, 'ѧ��Ҫ��'] = features['ѧ��Ҫ��'].map(degree_mapping)
features.loc[:, '����Ҫ��'] = features['����Ҫ��'].map(experience_mapping)
features.loc[:, 'ְλ����'] = features['ְλ����'].map(occupation_mapping)
features.loc[:, '��������'] = features['��������'].map(welfare_mapping)
# ����ȱʧֵ
imputer = SimpleImputer(strategy='mean')
features = imputer.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# ѵ�����Իع�ģ���ұ���ģ�� 160.74
model = LinearRegression()
model.fit(X_train, y_train)
with open('D:\\SchoolWork\\��ҵ������\\mysite\\web\\algorithm\\model_linear.pickle', 'wb') as f:
    pickle.dump(model, f)
# ѵ��������ģ���ұ���ģ�� 147.09
model = DecisionTreeRegressor(max_depth=5, random_state=42)
model.fit(X_train, y_train)
with open('D:\\SchoolWork\\��ҵ������\\mysite\\web\\algorithm\\model_decision.pickle', 'wb') as f:
    pickle.dump(model, f)
# # ѵ�����ɭ��ģ���ұ���ģ�� 144.20
model = RandomForestRegressor(max_depth=5, random_state=42)
model.fit(X_train, y_train)
with open('D:\\SchoolWork\\��ҵ������\\mysite\\web\\algorithm\\model_random.pickle', 'wb') as f:
    pickle.dump(model, f)
# # ѵ��KNNģ���ұ���ģ�� 151.48
model = KNeighborsRegressor(n_neighbors=26)
model.fit(X_train, y_train)
with open('D:\\SchoolWork\\��ҵ������\\mysite\\web\\algorithm\\model_knn.pickle', 'wb') as f:
    pickle.dump(model, f)
# # ѵ��SVRģ���ұ���ģ�� 164.73
model = SVR(C = 2,kernel='rbf')
model.fit(X_train, y_train)
with open('D:\\SchoolWork\\��ҵ������\\mysite\\web\\algorithm\\model_svr.pickle', 'wb') as f:
    pickle.dump(model, f)

# Ԥ�ⵥ������
# single_data = np.array([2, 2, 1, 2]).reshape(1, -1)
# single_data = imputer.transform(single_data)
# prediction = model.predict(single_data)
# print("�������ݵ�Ԥ��ֵΪ��", prediction[0])

#ģ������
# y_pred = model.predict(X_test)
# # ����Ԥ������ MSE
# mse = mean_squared_error(y_test, y_pred)
# print("ģ�͵ľ�����MSE����", mse)

# print("over!")


# # ѵ�����Իع�ģ��
# model = LinearRegression()
# model.fit(X_train, y_train)
# # ѵ��������ģ��
# model = DecisionTreeRegressor(max_depth=5, random_state=42)
# model.fit(X_train, y_train)
# # ѵ�����ɭ��ģ��
# model = RandomForestRegressor(n_estimators=10, random_state=42)
# model.fit(X_train, y_train)
# # ѵ��knnģ��
# model = KNeighborsRegressor(n_neighbors=26)
# model.fit(X_train, y_train)
# # ѵ��SVRģ��
# model = SVR(C = 2,kernel='rbf')
# model.fit(X_train, y_train)