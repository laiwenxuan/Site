# coding:gbk
import pickle
import pandas as pd

def predict_salary(city,degree, experience,occupation,welfare,modelselect):
# def predict_salary(city,degree, experience,occupation):
    city_mapping={'北京':1,'上海':2,'广州':3,'深圳':4,'杭州':5, '天津':6, '西安':7, '苏州':8, '武汉':9, '厦门':10, '长沙':11, '成都':12, '郑州':13, '重庆':14 }
    degree_mapping = {'大专': 0, '本科': 1, '硕士': 2, '博士': 5}
    experience_mapping = {'在校/应届': 0, '1年以内': 1, '1-3年': 2, '3-5年': 3, '5-10年': 4, '10年以上': 5,
                          '经验不限': 5, }
    occupation_mapping = {'java': 1, 'python': 2, 'cto': 3, '人工智能': 4, 'BI': 5, 'ETL': 6, '数据挖掘': 7, '数据仓库': 8,
                   '数据分析': 9}
    welfare_mapping = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14,
                       15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20}
    model_mapping = {
        "线性回归": "model_linear.pickle",
        "决策树": "model_decision.pickle",
        "随机森林": "model_random.pickle",
        "KNN": "model_knn.pickle",
        "SVD": "model_svr.pickle"
    }

    try:
        with open(f'D:\\SchoolWork\\行业大数据\\mysite\\web\\algorithm\\{model_mapping.get(modelselect)}', 'rb') as f:
        # with open(f'D:\\SchoolWork\\行业大数据\\mysite\\web\\algorithm\\model_linear.pickle', 'rb') as f:
            loaded_model = pickle.load(f)
        new_data = pd.DataFrame({
            '城市': [city_mapping.get(city, 0)],
            '学历要求': [degree_mapping.get(degree, 0)],
            '经验要求': [experience_mapping.get(experience, 0)],
            '职位': [occupation_mapping.get(occupation, 0)],
            '福利个数': [welfare_mapping.get(occupation, 0)]
        })

        predicted_salary = loaded_model.predict(new_data)
        return "{:.2f}".format(float(predicted_salary))

    except Exception as e:
        print("Error:", e)
