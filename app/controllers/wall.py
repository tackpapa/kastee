
from system.core.controller import *

class Wall(Controller):
    def __init__(self, action):
        super(Wall, self).__init__(action)

        self.load_model('Wallmodel')
        self.db = self._app.db

    def show(self, id):
        info={
            'id':id
        }
        msgs=self.models['Wallmodel'].msgshow()
        cmts=self.models['Wallmodel'].cmtshow()
        user=self.models['Wallmodel'].usershow(info)
        return self.load_view('wall.html', user=user, msgs=msgs, cmts=cmts)

    def msg(self,id):
        id=session['id']
        msg=request.form['msg']
        info={
            'id':id,
            'msg':msg
        }
        self.models['Wallmodel'].msgpost(info)
        url="/wall/"+str(id)
        return redirect (url)

    def comment(self):
        msg_id = request.form['msg_id']
        cmt = request.form['cmt']
        user_id = session['userid']

        info={
            'message_id': msg_id,
            'comment':cmt,
            'user_id': user_id
        }
        self.models['Wallmodel'].cmtpost(info)
        url="/wall/"+str(info['user_id'])
        return redirect (url)

    def msgdel(self):
        msg_id=request.form['msg_id']
        info={
            'message_id'=:msg_id
        }
        self.models['Wallmodel'].msgdel(info)
        url="/wall/"+str(session['userid'])
        return redirect (url)

    def cmtdel(self):
        id=request.form['cmt_id']
        info={
            'id'=:id
        }
        self.models['Wallmodel'].cmtdel(info)

        url="/wall/"+str(session['userid'])
        return redirect (url)
