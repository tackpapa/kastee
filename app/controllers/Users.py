from system.core.controller import *
from time import strftime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from flask.ext.bcrypt import Bcrypt

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('Usersmodel')
        self.load_model('Wallmodel')
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
        session['apt'] = user[0]['apt']


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
        session['apt'] = []
        return redirect('/')
######################################################################################################################
    def register_page(self):
        return self.load_view('register.html')
######################################################################################################################
    def register(self):
        error=False

        if len(request.form['apt']) == 0:
            flash('You need a code to register!')
            error=True
        thecode=request.form['apt']
        code=self.models['Usersmodel'].aptsearch(thecode)

        if len(request.form['car']) == 0:
            request.form['car'] =1

        if code == False:
            flash('Your apartment has not registered yet, or invalid code')
            error=True

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
            return redirect('/users/registerpage')

        info={
        'first':request.form['first'],
        'last':request.form['last'],
        'email':request.form['email'],
        'pw': request.form['pw'],
        'level': 1,
        'apt':code,
        'car':request.form['car']
        }
        self.models['Usersmodel'].register(info)
        if session['level'] > 5:
            return redirect ('/admin/dash')
        return redirect ('/users/loginpage')

    def regimanager(self):
        error=False

        if len(request.form['car']) == 0:
            request.form['car'] =1

        if len(request.form['apt']) == 0:
            flash('You should make a code for your apt')

        if len(request.form['first']) < 2:
            flash('name should be longer than 2 letters')
            error=True

        if len(request.form['last']) < 2:
            flash('you must write your apt number')
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
            return redirect('/users/registerpage/manager')


        level = 6

        info={
        'first':request.form['first'],
        'last':request.form['last'],
        'email':request.form['email'],
        'pw': request.form['pw'],
        'level': level,
        'apt':request.form['apt'],
        'car':request.form['car']
        }
        self.models['Usersmodel'].register(info)

        return redirect ('/users/loginpage')

######################################################################################################################
    def dash(self):

        users=self.models['Usersmodel'].showall()

        url="/wall/"+str(session['apt'])
        return redirect(url)
######################################################################################################################
    def editpage(self):

        info={
            'id':session['userid']
        }

        dms=self.models['Usersmodel'].dms(info)
        dmcmts=self.models['Usersmodel'].dmcmts()
        all=self.models['Wallmodel'].all()


        return self.load_view('edit.html', dms=dms, dmcmts=dmcmts, all=all)
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

    def dmcomment(self):

        info={
            'dm_id':request.form['dm_id'],
            'user_id' : request.form['user_id'],
            'dmcomment' : request.form['dmcmt']
        }
        self.models['Usersmodel'].dmcomment(info)
        return redirect ('/users/editpage')

    def dmcmtdel(self):
        info={
            'dmcmt_id':request.form['dmcmt_id']
        }
        self.models['Usersmodel'].dmcmtdel(info)
        return redirect ('/users/editpage')

    def manager(self):
        session['mag']=True
        return self.load_view('manager.html')

    def profile(self):
        info={
            'id':session['userid']
        }

        all=self.models['Wallmodel'].all()


        return self.load_view('profile.html', all=all)

    def dmdel(self):
        id=request.form['dm_id']
        self.models['Usersmodel'].dmdel(id)
        return redirect ('/users/editpage')
