from system.core.controller import *
from time import strftime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from flask.ext.bcrypt import Bcrypt

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('Usersmodel')
######################################################################################################################

    def index(self):
        if 'login' not in session:
            session['login']=False;
        if 'userid' not in session:
            session['userid'] = [];
        return self.load_view('index.html')
######################################################################################################################
    def loginpage(self):
        return self.load_view('login.html')
######################################################################################################################
    def login(self):
        email=request.form['email']
        pw=request.form['pw']
        info={
        'email':email,
        'pw': pw
        }
        user=self.models['Usersmodel'].login(info)
        if user==False:
            flash('invalid email or password')
            return redirect('/users/dash')

        session['status']=True
        session['userid']=user[0]['id']
        session['first']=user[0]['first']
        session['last']=user[0]['last']
        session['email']=user[0]['email']
        session['level']=user[0]['level']


        if user:
            return redirect ('/users/dash')
######################################################################################################################
    def logout(self):
        session['user']=[]
        session['first']=[]
        session['last']=[]
        session['email']=[]
        session['userid']=[]
        session['status']=False
        return redirect('/users/loginpage')
######################################################################################################################
    def register_page(self):
        return self.load_view('register.html')
######################################################################################################################
    def register(self):
        error=False

        if len(request.form['first']) < 2:
            flash('name should be longer than 2 letters')
            error=True

        if len(request.form['last']) < 2:
            flash('name should be longer than 2 letters')
            error=True

        if not EMAIL_REGEX.match(request.form['email']):
            flash("email not valid!")
            error=True


        if len(request.form['pw']) < 2:
            flash("password should be longer than 2letters!")
            error=True

        pw = request.form['pw']
        cpw = request.form['cpw']
        if cpw != pw:
            flash("pw doesn't match you idiot!")
            error=True
        if error == True:
            flash(" whats wrong")
            return redirect('/users/registerpage')
        print 'AKJAKLSFDJKALJFD;KLFKLJ;AKJDF;KAJF;KLJA;LFKJA;KL'

        info={
        'first':request.form['first'],
        'last':request.form['last'],
        'email':request.form['email'],
        'pw': request.form['pw'],
        'level': 1
        }
        run=self.models['Usersmodel'].register(info)
        if run[0]['id']== 1:
            self.models['Usersmodel'].makeadmin()
        else:
            pass

        return redirect ('/users/loginpage')

######################################################################################################################
    def dash(self):
        users=self.models['Usersmodel'].showall()
        if session['level'] > 5:
            return redirect('/admin/dash')
        else:
            return self.load_view('userdash.html', users=users)
######################################################################################################################
    def editpage(self):
        return self.load_view('edit.html')
######################################################################################################################
    def edit(self):
        info={
            'first':request.form['first'],
            'last':request.form['last'],
            'email':request.form['email'],
            'id': session['userid']
        }
        users=self.models['Usersmodel'].update(info)
        return redirect('/users/dash')
######################################################################################################################

    def pw(self):
        pw=request.form['pw']
        cpw=request.form['cpw']
        email=session['email']
        if pw != cpw:
            flash('password invalid')
            return ('/users/editpage')
        info={
        'pw':pw,
        'email':email
        }
        self.models['Usersmodel'].pwupdate(info)
        return redirect('/users/dash')
######################################################################################################################
