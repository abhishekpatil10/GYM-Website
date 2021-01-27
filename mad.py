from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import *
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Contacts(db.Model):
    '''
    name,lastname,country,subject
    '''
    
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(20), nullable=False,primary_key=True)
    country = db.Column(db.String(12), nullable=False)
    subject = db.Column(db.String(52), nullable=False)
    def __init__(self,name,lastname, country,subject):
        self.name=name
        self.lastname=lastname
        self.country=country
       	self.subject=subject
        

#login page------
@app.route("/login", methods=['GET','POST'])
def login():
	if request.method == 'POST':
		if request.form['username']=='admin' and request.form['password']=='123':
			return redirect(url_for('suc'))
		else:
			flash('You enter Wrong details,Try again!!!!!', 'error') 
	return render_template('login.html')
#signup page------
@app.route("/")
def home():
	return render_template('home.html')

#register page------
@app.route("/register", methods=['GET','POST'])
def register():

	if (request.method=='POST'):
		print('eeeeeeeeeeeeeeeeeeeeeeee')
		if not request.form['name'] or not request.form['lastname'] or not request.form['country'] or not request.form['subject']:
			flash("enter details",'error')
		else:
			name = request.form['name']
			lastname = request.form['lastname']
			country = request.form['country']
			subject = request.form['subject']
			entry=Contacts(name=name,lastname=lastname,country=country,subject=subject)
			db.session.add(entry)
			db.session.commit()
			return redirect(url_for('thnk'))
	else:
		return render_template("register.html")
	return render_template('register.html')


#successful submit page------
@app.route("/db",methods=['GET','POST'])
def suc():
	return render_template('suc.html',Contacts=Contacts.query.all())

@app.route("/thnk")
def thnk():
	return render_template('thnk.html')
if __name__=="__main__":
	db.create_all()
	app.run(debug=True)