# -*- coding:utf-8 -*-
from flask import render_template, redirect, request
from MVC import app, db
from MVC.models import Course

@app.route('/upLoadNewCourse/', methods={"GET", "POST"})
def upLoadNewCourse():
    course_name = request.values.get('course_name').strip()
    url = request.values.get('url').strip()
    teacher = request.values.get('teacher').strip()
    details = request.values.get('details').strip()
    open_date = request.values.get('open_date').strip()
    course_url = request.values.get('course_url').strip()
    university = request.values.get('university').strip()
    print(course_name)
    course = Course(course_name=course_name, url=url, teacher=teacher, details=details, open_date=open_date,
                    course_url=course_url, university=university, type="course")
    db.session.add(course)
    db.session.commit()
    return "上传成功！！"


@app.route('/upLoadNewPaper/', methods={"GET", "POST"})
def upLoadNewPaper():
    course_name = request.values.get('course_name').strip()
    url = request.values.get('url').strip()
    teacher = request.values.get('teacher').strip()
    details = request.values.get('details').strip()
    open_date = request.values.get('open_date').strip()
    course_url = request.values.get('course_url').strip()
    university = request.values.get('university').strip()
    course = Course(course_name=course_name, url=url, teacher=teacher, details=details, open_date=open_date,
                    course_url=course_url, university=university, type="paper")
    db.session.add(course)
    db.session.commit()
    return "上传成功！！"


@app.route('/')
def course_detail():
    courses = Course.query.order_by(db.desc(Course.id)).limit(4).all()
    papers = courses[0:3]
    print(len(papers))
    return render_template('index.html', courses=courses, papers = papers)


@app.route('/post/')
def post():
    return render_template('post.html')


@app.route('/post_paper/')
def post_paper():
    return render_template('post_paper.html')


@app.route('/course_detail/<int:course_id>')
def index(course_id):
    course = Course.query.get(course_id)
    if course is None:
        return redirect('/')
    return render_template('course_detail.html', course=course)


@app.route('/course_recommend/<int:page>/')
def course_recommend(page):
    courses = Course.query.order_by(db.desc(Course.id)).all()
    # 每页20个
    print(page)
    courses = courses[page*20:page*20 + 19]
    return render_template('recommend.html', courses=courses, page = page, type="course")



@app.route('/paper_recommend/<int:page>/')
def paper_recommend(page):
    papers = Course.query.order_by(db.desc(Course.id)).all()
    # 每页20个
    print(page)
    paper = papers[page*20:page*20 + 19]
    return render_template('recommend.html', courses=paper, page = page, type="paper")
