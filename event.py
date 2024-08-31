from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

class profiles(db.Model):
    id = mapped_column(Integer,primary_key=True,autoincrement=True)
    name = mapped_column(String(20),nullable=False)
    age = mapped_column(Integer,nullable=False)
    gender = mapped_column(String(6),nullable=False)
    address = mapped_column(String(50),nullable=False)
    phone = mapped_column(Integer,nullable=False)
    email = mapped_column(Integer,nullable=False)
    license = mapped_column(String(20),unique=True,nullable=False)

with app.app_context():
    db.create_all()

@app.route('/',methods = ["GET"])
def event():
    return render_template("event.html")

@app.route('/nextpage', methods = ["GET"])
def nextpage():
    return render_template("register.html")

@app.route('/register',methods= ["POST"])
def register():
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    address = request.form["address"]
    phn = request.form["phn"]
    email = request.form["email"]
    license = request.form["lisence"]
    x = profiles(name = name, age=age ,gender=gender, address=address, phone=phn, email=email, license=license)
    db.session.add(x)
    db.session.commit()
    return render_template("details.html",id=x.id )
@app.route('/get/<int:id>',methods=["GET"])
def get_details(id):
    user = db.get_or_404(profiles,id)
    return render_template("users.html",user=user)

    
