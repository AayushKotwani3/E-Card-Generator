from flask import Flask,render_template,redirect,request
from flask import current_app as app
from .models import * #inheriting models module to make indirect connection with app.py
from key_generator import aadhar_key,pan_key,driving_key,voter_key

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        this_user=User.query.filter_by(username=username).first() #Lhs is attribite from db table and rhs is form submission value
        if this_user:
            if this_user.password==password: #lhs is from db table and rhs is form submission value
                 if this_user.type=='admin':
                    return redirect('/admin')
                 else:
                    return redirect(f'/home/{this_user.id}')
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

@app.route('/admin')
def admin_dash():
    this_user=User.query.filter_by(type='admin').first()
    all_info=Info.query.all()
    users=len(User.query.all())
    requests=len(Info.query.filter_by(attribute_value='requested').all())
    generated=len(Info.query.filter_by(attribute_value='generated').all())
    return render_template('admin_dashboard.html',this_user=this_user,all_info=all_info,users=users,requests=requests,generated=generated)

@app.route('/home/<int:user_id>')
def user_dashboard(user_id):
    this_user=User.query.filter_by(id=user_id).first()
    return render_template('user_dashboard.html',this_user=this_user)


@app.route('/request_card/<int:user_id>',methods=["GET","POST"])
def request_cards(user_id):
    if request.method=='POST':
        card=request.form.get('selectedcard')
        return redirect(f'/request/{card}/{user_id}')
    return render_template('select.html',user_id=user_id)

@app.route('/request/<card>/<int:user_id>',methods=["GET","POST"])
def card_details(card,user_id):
    this_user=User.query.filter_by(id=user_id).first()
    if card=='aadhar':
        if request.method=='POST':
            Aadhar_name=request.form.get('Aadhar_name')
            father_name=request.form.get('father_name')
            gender=request.form.get('gender')
            dob=request.form.get('dob')
            Address=request.form.get('Address')
            image_file = request.files.get('image')
            if image_file:
                # You might want to save the file or process it differently
                # For now, we'll just get the filename
                image_filename = image_file.filename
            else:
                image_filename = None  # or provide a default
            info1=Info(attribute_name='Fullname',attribute_value=Aadhar_name,card_name=card,user_id=user_id)
            info2=Info(attribute_name='Fathers_name',attribute_value=father_name,card_name=card,user_id=user_id)
            info3=Info(attribute_name='Gender',attribute_value=gender,card_name=card,user_id=user_id)
            info4=Info(attribute_name='dob',attribute_value=dob,card_name=card,user_id=user_id)
            info5=Info(attribute_name='Address',attribute_value=Address,card_name=card,user_id=user_id)
            info6=Info(attribute_name='image',attribute_value=image_filename,card_name=card,user_id=user_id)
            info7=Info(attribute_name='Status',attribute_value='requested',card_name=card,user_id=user_id)
            db.session.add_all([info1,info2,info3,info4,info5,info6,info7])
            db.session.commit()
            return render_template('user_dashboard.html',this_user=this_user)
        return render_template('Aadhar.html',user_id=user_id)
    elif card=='pan':
        if request.method=='POST':
            pan_name=request.form.get('pan_name')
            father_name=request.form.get('father_name')
            dob=request.form.get('dob')
            image_file = request.files.get('image')
            if image_file:
                # You might want to save the file or process it differently
                # For now, we'll just get the filename
                image_filename = image_file.filename
            else:
                image_filename = None  # or provide a default
            info1=Info(attribute_name='Fullname',attribute_value=pan_name,card_name=card,user_id=user_id)
            info2=Info(attribute_name='Fathers_name',attribute_value=father_name,card_name=card,user_id=user_id)
            info3=Info(attribute_name='dob',attribute_value=dob,card_name=card,user_id=user_id)
            info4=Info(attribute_name='image',attribute_value=image_filename,card_name=card,user_id=user_id)
            info5=Info(attribute_name='Status',attribute_value='requested',card_name=card,user_id=user_id)
            db.session.add_all([info1,info2,info3,info4,info5])
            db.session.commit()
            return render_template('user_dashboard.html',this_user=this_user)    
        return render_template('pan-card.html',user_id=user_id)    
    elif card=='driving':
        if request.method=='POST':
            driving_license_name=request.form.get('driving_license_name')
            father_name=request.form.get('father_name')
            dob=request.form.get('dob')
            Address=request.form.get('Address')
            pincode=request.form.get('pincode')
            image_file = request.files.get('image')
            if image_file:
                # You might want to save the file or process it differently
                # For now, we'll just get the filename
                image_filename = image_file.filename
            else:
                image_filename = None  # or provide a default
            info1=Info(attribute_name='Fullname',attribute_value=driving_license_name,card_name=card,user_id=user_id)
            info2=Info(attribute_name='Fathers_name',attribute_value=father_name,card_name=card,user_id=user_id)
            info3=Info(attribute_name='dob',attribute_value=dob,card_name=card,user_id=user_id)
            info4=Info(attribute_name='Address',attribute_value=Address,card_name=card,user_id=user_id)
            info5=Info(attribute_name='pincode',attribute_value=pincode,card_name=card,user_id=user_id)
            info6=Info(attribute_name='image',attribute_value=image_filename,card_name=card,user_id=user_id)
            info7=Info(attribute_name='Status',attribute_value='requested',card_name=card,user_id=user_id)
            db.session.add_all([info1,info2,info3,info4,info5,info6,info7])
            db.session.commit()
            return render_template('user_dashboard.html',this_user=this_user)
        return render_template('driving-license.html',user_id=user_id)
    elif card=='voterid':
        if request.method=='POST':
            voter_id_name=request.form.get('voter_id_name')
            ward_name=request.form.get('ward_name')
            gender=request.form.get('gender')
            dob=request.form.get('dob')
            image_file = request.files.get('image')
            if image_file:
                # You might want to save the file or process it differently
                # For now, we'll just get the filename
                image_filename = image_file.filename
            else:
                image_filename = None  # or provide a default
            info1=Info(attribute_name='Fullname',attribute_value=voter_id_name,card_name=card,user_id=user_id)
            info2=Info(attribute_name='ward_name',attribute_value=ward_name,card_name=card,user_id=user_id)
            info3=Info(attribute_name='Gender',attribute_value=gender,card_name=card,user_id=user_id)
            info4=Info(attribute_name='dob',attribute_value=dob,card_name=card,user_id=user_id)
            info5=Info(attribute_name='image',attribute_value=image_filename,card_name=card,user_id=user_id)
            info6=Info(attribute_name='Status',attribute_value='requested',card_name=card,user_id=user_id)
            db.session.add_all([info1,info2,info3,info4,info5,info6])
            db.session.commit()
            return render_template('user_dashboard.html',this_user=this_user)
        return render_template('voter-id.html',user_id=user_id)

@app.route('/update_status/<card>/<int:user_id>',methods=['GET','POST'])
def update_status(card,user_id):
    details=Info.query.filter_by(user_id=user_id,card_name=card).all()
    detail=Info.query.filter_by(user_id=user_id,card_name=card,attribute_name='Status').first()
    if request.method=='POST':
        status=request.form.get('status')
        detail.attribute_value=status
        db.session.commit()
        return redirect('/admin')
    return render_template('update_status.html',user_id=user_id,card=card,details=details)

@app.route('/generate/<card>/<user_id>')
def generate(card,user_id):
    detail=Info.query.filter_by(card_name=card,user_id=user_id,attribute_name='Status').first()
    detail.attribute_value='generated'
    db.session.commit()
    if card=='aadhar':
        key=aadhar_key()
    if card=='pan':
        key=pan_key()
    if card=='driving':
        key=driving_key()
    if card=='voterid':
        key=voter_key()            
    info=Info(card_name=card,user_id=user_id,attribute_name='key',attribute_value=key)
    db.session.add(info)
    db.session.commit()
    return redirect('/admin')

@app.route('/view/<card>/<user_id>')
def view_card(card,user_id):
     details=Info.query.filter_by(user_id=user_id,card_name=card).all()
     if card=='aadhar':
         return render_template('view_aadhar.html',details=details)
     if card=='pan':
         return render_template('view_pan.html',details=details)
     if card=='voterid':
         return render_template('view_voterid.html',details=details)
     if card=='driving':
         return render_template('view_driving.html',details=details)

@app.route('/results')
def search():
    search_word=request.args.get('search')
    key=request.args.get('key')
    if key=='user':
        results=User.query.filter_by(username=search_word).all()
    else:
        results=Info.query.filter_by(attribute_name='Status',card_name=search_word.lower()).all()
    return render_template('results.html',results=results,key=key)        

@app.route('/summary')
def summary():
    ra=len(Info.query.filter_by(attribute_value='requested',card_name='aadhar').all())
    rp=len(Info.query.filter_by(attribute_value='requested',card_name='pan').all())
    rd=len(Info.query.filter_by(attribute_value='requested',card_name='driving').all())
    rv=len(Info.query.filter_by(attribute_value='requested',card_name='voterid').all())
    #underverification
    uva=len(Info.query.filter_by(attribute_value='under_verification',card_name='aadhar').all())
    uvp=len(Info.query.filter_by(attribute_value='under_verification',card_name='pan').all())
    uvd=len(Info.query.filter_by(attribute_value='under_verification',card_name='driving').all())
    uvv=len(Info.query.filter_by(attribute_value='under_verification',card_name='voterid').all())
    #verified
    va=len(Info.query.filter_by(attribute_value='verified',card_name='aadhar').all())
    vp=len(Info.query.filter_by(attribute_value='verified',card_name='pan').all())
    vd=len(Info.query.filter_by(attribute_value='verified',card_name='driving').all())
    vv=len(Info.query.filter_by(attribute_value='verified',card_name='voterid').all())
    #Generated
    ga=len(Info.query.filter_by(attribute_value='generated',card_name='aadhar').all())
    gp=len(Info.query.filter_by(attribute_value='generated',card_name='pan').all())
    gd=len(Info.query.filter_by(attribute_value='generated',card_name='driving').all())
    gv=len(Info.query.filter_by(attribute_value='generated',card_name='voterid').all())
    return render_template('summary.html',ra=ra,rp=rp,rd=rd,rv=rv,
                                          uva=uva,uvp=uvp,uvd=uvd,uvv=uvv,
                                          va=va,vp=vp,vd=vd,vv=vv,
                                          ga=ga,gp=gp,gd=gd,gv=gv)