
from system.core.model import Model
from time import mktime
from datetime import datetime

class Wallmodel(Model):
    def __init__(self):
        super(Wallmodel, self).__init__()

    def msgpost(self, info):
        query = "INSERT INTO messages (user_id, message, created_at, updated_at, apt) values (:user_id, :message, NOW(), NOW(), :apt)"
        data={
            'user_id':info['id'],
            'message':info['msg'],
            'apt':info['apt']
        }
        return self.db.query_db(query, data)

    def cmtpost(self, info):
        query = "INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) values (:comment, NOW(), NOW(), :user_id, :message_id)"
        data = {
            'comment':info['comment'],
            'user_id':info['user_id'],
            'message_id':info['message_id']
        }
        return self.db.query_db(query, data)

    def msgshow(self):
        query = "select users.first, users.last, users.id, messages.apt, messages.message, messages.created_at, messages.id as msg_id from messages left join users on users.id=messages.user_id order by created_at Desc"
        return self.db.query_db(query)



    def cmtshow(self):
        query = "select comments.id as cmt_id, comments.created_at, comments.message_id, comments.user_id, comments.comment, users.first, users.last from comments left join users on comments.user_id=users.id"
        return self.db.query_db(query)

    def usershow(self, info):
        query = "SELECT * FROM users where id=:id limit 1"
        data={ 'id':info['id'] }
        return self.db.query_db(query, data)

    def msgdel(self, info):
        query = "DELETE from messages where id=:message_id"
        data={
            'message_id':info['message_id']
        }
        return self.db.query_db(query, data)

    def cmtdel(self, info):
        query = "DELETE from comments where id=:id"
        data={
            'id':info['id']
        }
        return self.db.query_db(query, data)

    def all(self):
        query="select * from users order by level desc"
        return self.db.query_db(query)

    def anoun(self):
        query="SELECT * from announcements"
        return self.db.query_db(query)

    def dm(self, info):
        query="insert into dms (dm, user_id, friend_id, created_at) values (:dm, :user_id, :friend_id, NOW())"
        data={
            'dm':info['dm'],
            'user_id':info['user_id'],
            'friend_id':info['friend_id']
        }
        return self.db.query_db(query, data)

    def delanoun(self, id):
        query="delete from announcements where id=:id"
        data={'id':id}
        return self.db.query_db(query, data)
