
from system.core.model import Model

class Usersmodel(Model):
    def __init__(self):
        super(Usersmodel, self).__init__()

    def register(self, info):
        pw = info['pw']
        hashed_pw = self.bcrypt.generate_password_hash(pw)
        query = "INSERT into users (first, last, email, created_at, updated_at, pw, level, apt, car) values(:first, :last, :email, NOW(), NOW(), :pw, :level, :apt, :car)"
        data = {
        'first': info['first'],
        'last': info['last'],
        'email': info['email'],
        'pw':hashed_pw,
        'level':info['level'],
        'apt':info['apt'],
        'car':info['car']
        }
        self.db.query_db(query, data)


        return

    def aptsearch(self, code):
        query="select * from users where apt=:apt limit 1"
        data={
        'apt' : code}

        apt=self.db.query_db(query, data)
        if len(apt) == 0:
            return False
        if apt:
            return apt[0]['apt']

    def makeadmin(self):
        query = "UPDATE users set level = '9' where id = '1'"
        return self.db.query_db(query)


    def login(self, info):
        pw = info['pw']
        email = info['email']
        userquery = "SELECT * FROM users WHERE email=:email limit 1"
        userdata = {'email': email}
        user = self.db.query_db(userquery, userdata)
        if len(user) == 0:
            return False
        if user:
            if self.bcrypt.check_password_hash(user[0]['pw'], pw):
                return user



    def showall(self):
        query = "Select * from users"
        return self.db.query_db(query)

    def update(self, info):
        query = "UPDATE users set email=:email, first=:first, last=:last where id=:id"
        data = {'email':info['email'], 'first':info['first'], 'last':info['last'], 'id':info['id']}
        print data
        return self.db.query_db(query, data)

    def pwupdate(self, info):
        pw = info['pw']
        cquery = "SELECT * FROM users WHERE email = :email LIMIT 1"
        cdata = {'pw': pw, 'email':info['email']}
        user = self.db.query_db(cquery, cdata)
        if len(user)== 0:
            return False
        if user:
            if self.bcrypt.check_password_hash(user[0]['pw'], pw):
                hashed_pw = self.bcrypt.generate_password_hash(pw)
                query = "update users set pw=:pw where email=:email"
                data = {'pw':hashed_pw, 'email':info['email']}
                return self.db.query_db(query, data)

    def dms(self, info):
        query="select dms.id, dms.dm, dms.user_id, dms.friend_id, dms.created_at, users.first, users.last from dms left join users on users.id=dms.user_id where dms.friend_id=:id order by created_at desc"
        data={
            'id':info['id']
        }
        return self.db.query_db(query, data)

    def dmcmts(self):
        query="SELECT dmcomments.id as dmcmt_id, dmcomments.created_at, dmcomments.dm_id, dmcomments.user_id, dmcomments.dmcomment, users.first, users.last from dmcomments left join users on dmcomments.user_id=users.id"
        return self.db.query_db(query)

    def dmcomment(self, info):
        query="INSERT INTO dmcomments (dmcomment, user_id, dm_id, created_at) values (:dmcomment, :user_id, :dm_id, NOW())"
        data={
            'dmcomment':info['dmcomment'],
            'user_id':info['user_id'],
            'dm_id' : info['dm_id']
        }
        return self.db.query_db (query, data)

    def dmcmtdel(self, info):
        query="delete from dmcomments where id=:id"
        data={
            'id':info['dmcmt_id']
        }
        return self.db.query_db (query, data)

    def dmdel(self, id):
        query="delete from dms where id=:id"
        return self.db.query_db (query)
