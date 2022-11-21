from settings import db


class Students(db.Model):
    id_student = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    last_name = db.Column(db.String(40), unique=True)
    age = db.Column(db.Integer)
    number_class = db.Column(db.String(40))

    def __init__(self, name, last_name, age, number_class):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.number_class = number_class


class Teachers(db.Model):
    id_teachers = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    last_name = db.Column(db.String(40), unique=True)
    school_subject = db.Column(db.Text)

    def __init__(self, name, last_name, school_subject):
        self.name = name
        self.last_name = last_name
        self.academic_subject = school_subject

