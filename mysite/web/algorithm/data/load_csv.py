#coding:gbk
import csv
from web.models import Occupation

def import_data():
    with open('D:\\SchoolWork\\行业大数据\\mysite\\web\\algorithm\\data\\jobs_score.csv', 'r', encoding='gbk') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过标题行
        for row in reader:
            occupation = Occupation.objects.create(
                occupation=row[0],
                name=row[1],
                area=row[2],
                experience=row[3],
                degree=row[4],
                welfare=row[5],
                link=row[6],
                salary=row[7],
                score=int(row[8])
            )
            occupation.save()

if __name__ == '__main__':
    import_data()
