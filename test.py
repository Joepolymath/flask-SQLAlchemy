class Student(db.Model):
    title = db.Column(db.String(80), unique = True, nullable = False, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    phone = db.Column(db.String(80), unique = True, nullable = False)
    def __repr__(self):
        return "<Title: {}>".format(self.title)



john = Student()
book = Student(title=?, name=?, phone=?)
================================================
<form action="/sub" method="POST">
        <input type="text" name="ftitle">
        <input type="text" name="fname">
        <input type="text" name="fphone">
        <input type="submit" value="Add">
    </form>
if request.form:
    a = request.form.get('ftitle')
    b = request.form.get('fname')
    c = request.form.get('fphone')
=================================================
book = Student(title=a, name=b, phone=c)