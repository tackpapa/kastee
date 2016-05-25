
from system.core.model import Model

class Adminmodel(Model):
    def __init__(self):
        super(Adminmodel, self).__init__()

    def kick(self, id):
        query = "DELETE from users where id=:id"
        data = {'id': id}
        return self.db.query_db(query, data)

    def showall(self):
        query = "Select * from users order by created_at desc"
        return self.db.query_db(query)

    def showone(self, id):
        id=id
        query = "SELECT * from users where id=:id limit 1"
        data = {'id': id}
        return self.db.query_db(query, data)

    def userupdate(self, info):
        query = "update users set email=:email, first=:first, last=:last, level=:level where id=:id"
        data = {
            'email':info['email'],
            'first':info['first'],
            'last': info['last'],
            'level': info['level'],
            'id': info['id']
        }
        return self.db.query_db(query, data)

    def pwupdate(self, info):
        pw = info['pw']
        id = info['id']
        hashed_pw = self.bcrypt.generate_password_hash(pw)
        query = "update users set pw=:pw where id=:id"
        data = {'pw':hashed_pw, 'id':info['id']}
        return self.db.query_db(query, data)

    def addanoun(self, info):
        query = " insert into announcements(created_at, content, user_id, apt) values (NOW(), :content, :user_id, :apt)"
        data={
            'content': info['content'],
            'user_id': info['user_id'],
            'apt':info['apt']
        }
        return self.db.query_db(query, data)
