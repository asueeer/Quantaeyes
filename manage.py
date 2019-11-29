# -*- encoding=UTF-8 -*-
import random

from MVC import app, db
from flask_script import Manager
from MVC.models import Course

manager = Manager(app)

@manager.command
def init_database():
    # 如果没有pymysql，需要在终端里输入pip install pymysql来安装
    # pip install mysql-python
    db.drop_all()
    db.create_all()

    for i in range(100):
        course_name = "高等数学（一）"
        url ="http://1.im.guokr.com/w4dTx9KUGsJH-v1pLjMkRAGD4vNg8ffjQRDQO4eTPOGqAQAA8AAAAEpQ.jpg?imageView2/1"
        teacher = "朱健民"
        details ="高等数学以微积分为主要内容。微积分是研究运动和变化的数学，它广泛应用于自然科学、社会科学、经济管理、工程技术等各个领域，其内容、思想与方法对培养各类人才全面综合素质具有不可替代的作用。高等数学课程着重培养学员的抽象思维能力、逻辑推理能力、空间想象能力、实验及观察能力以及综合运用所学知识分析问题解决问题的能力，也是开展数学素质教育、培养学习者创新精神和创新能力的重要课程。 "
        open_date = "2016/03/01"
        course_url = "https://www.icourse163.org/course/nudt-9004"
        university = "国防科技大学"
        course = Course(course_name=course_name, url=url, teacher=teacher, details=details, open_date=open_date, course_url=course_url, university=university, type="course")
        db.session.add(course)
    db.session.commit()


if __name__ == '__main__':
    init_database()