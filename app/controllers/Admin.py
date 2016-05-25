
from system.core.controller import *

class Admin(Controller):
    def __init__(self, action):
        super(Admin, self).__init__(action)

        self.load_model('Adminmodel')
        # self.db = self._app.db


    def admin_dash(self):
        users=self.models['Adminmodel'].showall()
        return self.load_view('admindash.html', users=users)

    def admin_add_page(self):
        return self.load_view('adminadd.html')

    def admin_add(self):
        return

    def admin_editpage(self, id):
        user=self.models['Adminmodel'].showone(id)
        print user
        return self.load_view('adminedit.html', user=user[0])

    def edituser(self):
        info={
            'id': request.form['id'],
            'first':request.form['first'],
            'last':request.form['last'],
            'email':request.form['email'],
            'level': request.form['level']
            }
        print info
        user=self.models['Adminmodel'].userupdate(info)
        return redirect('/admin/dash')

    def pwupdate(self, id):
        pw=request.form['pw']
        cpw=request.form['cpw']
        id=request.form['id']
        if pw != cpw:
            flash('password invalid')
            url="/admin/editpage/"+str(id)
            return redirect (url)
        info={
        'pw':pw,
        'id':id
        }
        user=self.models['Adminmodel'].pwupdate(info)
        return redirect('/admin/dash', user=user)



    def kick(self, id):
        self.models['Adminmodel'].kick(id)
        return redirect ('/admin/dash')

    def addanoun(self):
        info={
            'user_id':request.form['user_id'],
            'content':request.form['anoun'],
            'apt':request.form['apt']
        }
        self.models['Adminmodel'].addanoun(info)
        apt=session['apt']
        url="/wall/"+str(apt)
        return redirect (url)
