
# coding: utf-8

# In[14]:


import sqlite3
from flask_restful import Resource,reqparse
from models.Logging_user import UserModel


# In[ ]:


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type = str, required = True, help = 'not blank')
    parser.add_argument('password',type = str, required = True, help = 'not blank')
    
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message":"user alredy exists"}
        user = UserModel(data['username'],data['password'])
        user.save_to_db()
        return {'message':'user created'}

