
# coding: utf-8

# In[1]:


from flask import Flask
import os
from flask_restful import Api
from Logging_security import authenticate , identity
from flask_jwt import JWT
from resources.Logging_user import UserRegister
from resources.item import Item , ItemList
from resources.store import Store, StoreList


# In[2]:


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app,authenticate,identity)


# In[3]:


api.add_resource(Item,'/item/<string:name>')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/store')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')


if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run()

