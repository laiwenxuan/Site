# coding:gbk
import pickle
import pandas as pd

def predict_salary(city,degree, experience,occupation,welfare,modelselect):
# def predict_salary(city,degree, experience,occupation):
    city_mapping={'����':1,'�Ϻ�':2,'����':3,'����':4,'����':5, '���':6, '����':7, '����':8, '�人':9, '����':10, '��ɳ':11, '�ɶ�':12, '֣��':13, '����':14 }
    degree_mapping = {'��ר': 0, '����': 1, '˶ʿ': 2, '��ʿ': 5}
    experience_mapping = {'��У/Ӧ��': 0, '1������': 1, '1-3��': 2, '3-5��': 3, '5-10��': 4, '10������': 5,
                          '���鲻��': 5, }
    occupation_mapping = {'java': 1, 'python': 2, 'cto': 3, '�˹�����': 4, 'BI': 5, 'ETL': 6, '�����ھ�': 7, '���ݲֿ�': 8,
                   '���ݷ���': 9}
    welfare_mapping = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14,
                       15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20}
    model_mapping = {
        "���Իع�": "model_linear.pickle",
        "������": "model_decision.pickle",
        "���ɭ��": "model_random.pickle",
        "KNN": "model_knn.pickle",
        "SVD": "model_svr.pickle"
    }

    try:
        with open(f'D:\\SchoolWork\\��ҵ������\\mysite\\web\\algorithm\\{model_mapping.get(modelselect)}', 'rb') as f:
        # with open(f'D:\\SchoolWork\\��ҵ������\\mysite\\web\\algorithm\\model_linear.pickle', 'rb') as f:
            loaded_model = pickle.load(f)
        new_data = pd.DataFrame({
            '����': [city_mapping.get(city, 0)],
            'ѧ��Ҫ��': [degree_mapping.get(degree, 0)],
            '����Ҫ��': [experience_mapping.get(experience, 0)],
            'ְλ': [occupation_mapping.get(occupation, 0)],
            '��������': [welfare_mapping.get(occupation, 0)]
        })

        predicted_salary = loaded_model.predict(new_data)
        return "{:.2f}".format(float(predicted_salary))

    except Exception as e:
        print("Error:", e)
