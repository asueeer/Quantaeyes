from datetime import datetime

from MVC import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_date = db.Column(db.DateTime)
    url = db.Column(db.String(512))
    course_name = db.Column(db.String(80))
    teacher = db.Column(db.String(80))
    open_date = db.Column(db.String(80))
    course_url = db.Column(db.String(80))
    university = db.Column(db.String(80))
    details = db.Column(db.String(10000))
    status = db.Column(db.String(10))
    brief_detail = db.Column(db.String(200))
    type = db.Column(db.String(10))

    def __init__(self, course_name, url, open_date, details, teacher, course_url, university, type):
        self.created_date = datetime.now()
        self.url = url
        self.course_name = course_name
        self.open_date = open_date
        self.details = details
        self.teacher = teacher
        self.status = "待审核"
        self.course_url = course_url
        self.university = university
        if len(details)<=200:
            self.brief_detail = details
        else:
            self.brief_detail = details[0:200]
        self.type = type


    def __repr__(self):
        return '<Course %d %s>' % (self.id, self.url)