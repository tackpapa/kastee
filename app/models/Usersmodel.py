
from system.core.model import Model

class Usersmodel(Model):
    def __init__(self):
        super(Usersmodel, self).__init__()

    def register(self, info):
        pw = info['pw']
        hashed_pw = self.bcrypt.generate_password_hash(pw)
        query = "INSERT into users (first, last, email, created_at, updated_at, pw, level) values(:first, :last, :email, NOW(), NOW(), :pw, :level)"
        data = {
        'first': info['first'],
        'last': info['last'],
        'email': info['email'],
        'pw':hashed_pw,
        'level':info['level']
        }
        self.db.query_db(query, data)
        runquery = "select * from users where id='1'"

        return self.db.query_db(runquery)

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
