from flask import Flask,render_template,redirect,request
from flask import current_app as app
from .models import * #inheriting models module to make indirect connection with app.py

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        this_user=User.query.filter_by(username=username).first() #Lhs is attribite from db table and rhs is form submission value
        if this_user:
            if this_user.password==password: #lhs is from db table and rhs is form submission value
                 if this_user.type=='admin':
                    return 'Admindashboard'
                 else:
                    return render_template('user_dashboard.html',username=username)
            else:
                return 'Incorrect Password'
        else:
             return 'User doesnt exist'
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        this_user=User.query.filter_by(username=username).first() #Lhs is attribite from db table and rhs is form submission value
        if this_user:
            return 'User already registered'
        else:
            new_user=User(username=username,email=email,password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
    return render_template('Register.html')

