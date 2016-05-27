
from system.core.controller import *
from time import mktime
from datetime import datetime
from time import strftime


class Wall(Controller):
    def __init__(self, action):
        super(Wall, self).__init__(action)

        self.load_model('Wallmodel')

    def show(self, id):


        msgs=self.models['Wallmodel'].msgshow()
        cmts=self.models['Wallmodel'].cmtshow()

        all=self.models['Wallmodel'].all()
        anoun=self.models['Wallmodel'].anoun()
        return self.load_view('wall.html', msgs=msgs, cmts=cmts, all=all, anoun=anoun)

    def msg(self):
        id=session['userid']
        msg=request.form['msg']
        apt=request.form['apt']
        info={
            'id':id,
            'msg':msg,
            'apt':apt
        }
        self.models['Wallmodel'].msgpost(info)
        url="/wall/"+str(apt)
        return redirect (url)

    def comment(self):
        msg_id = request.form['cmt_id']
        cmt = request.form['cmt']
        user_id = session['userid']
        friend_id = request.form['friend_id']
        apt=session['apt']
        info={
            'message_id': msg_id,
            'comment':cmt,
            'user_id': user_id
        }
        self.models['Wallmodel'].cmtpost(info)
        url="/wall/"+str(apt)
        return redirect (url)

    def msgdel(self):
        msg_id=request.form['msg_id']
        user_id=request.form['walluser']
        info={'message_id':msg_id, 'user_id':user_id}
        self.models['Wallmodel'].msgdel(info)
        apt=session['apt']
        url="/wall/"+str(apt)
        return redirect (url)

    def cmtdel(self):
        id=request.form['cmt_id']
        info={
            'id':id
        }
        self.models['Wallmodel'].cmtdel(info)
        apt=session['apt']
        url="/wall/"+str(apt)
        return redirect (url)

    def dm(self):

        info={
            'user_id': request.form['user_id'],
            'friend_id':request.form['friend_id'],
            'dm': request.form['dm']
        }
        self.models['Wallmodel'].dm(info)
        apt=session['apt']
        url="/wall/"+str(apt)

        return redirect (url)

    def delanoun(self, id):

        self.models['Wallmodel'].delanoun(id)
        apt=session['apt']
        url="/wall/"+str(apt)
        return redirect (url)
