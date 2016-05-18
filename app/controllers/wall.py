
from system.core.controller import *
from time import mktime
from datetime import datetime
from time import strftime


class Wall(Controller):
    def __init__(self, action):
        super(Wall, self).__init__(action)

        self.load_model('Wallmodel')

    def show(self, id):

        info={
            'id':id
        }
        msgs=self.models['Wallmodel'].msgshow()
        cmts=self.models['Wallmodel'].cmtshow()
        user=self.models['Wallmodel'].usershow(info)
        return self.load_view('wall.html', user=user[0], msgs=msgs, cmts=cmts)

    def msg(self):
        id=session['userid']
        msg=request.form['msg']
        friend_id=request.form['friend_id']
        info={
            'id':id,
            'msg':msg,
            'friend_id':friend_id
        }
        self.models['Wallmodel'].msgpost(info)
        url="/wall/"+str(friend_id)
        return redirect (url)

    def comment(self):
        msg_id = request.form['cmt_id']
        cmt = request.form['cmt']
        user_id = session['userid']
        friend_id = request.form['friend_id']
        info={
            'message_id': msg_id,
            'comment':cmt,
            'user_id': user_id
        }
        self.models['Wallmodel'].cmtpost(info)
        url="/wall/"+str(friend_id)
        return redirect (url)

    def msgdel(self):
        msg_id=request.form['msg_id']
        user_id=request.form['walluser']
        info={'message_id':msg_id, 'user_id':user_id}
        self.models['Wallmodel'].msgdel(info)
        url="/wall/"+str(user_id)
        return redirect (url)

    def cmtdel(self):
        id=request.form['cmt_id']
        info={
            'id':id
        }
        self.models['Wallmodel'].cmtdel(info)

        url="/wall/"+str(session['userid'])
        return redirect (url)
