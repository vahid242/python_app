# import Flask class object from flask library
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

# instantiating Flask object of (create variable to store flask object instance)
app=Flask(__name__)
# confige what database to connect
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'# create a sqlalchemy object for flask application
# create a SQLALCHEMY object
db=SQLAlchemy(app)


# create a model with class for database(table, columns..)
class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    # to sure when use post method in request not get...
    if request.method == 'POST':
        # capture values
        email=request.form["email_name"]
        height=request.form["height_name"]

        # check email not submit before
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            # create an object of Data class to map these strings to dtaabase model
            data=Data(email,height)
            # to add rows shoid point to sqlalchemy object
            db.session.add(data)
            # commit changes to databse
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
    return render_template('index.html',
    text="This email adress has been submitted already!")

if __name__ == '__main__':
    app.debug=True
    app.run()
