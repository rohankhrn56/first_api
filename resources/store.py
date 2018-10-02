
# coding: utf-8

# In[2]:


from flask_restful import Resource , reqparse
from models.store import StoreModel


# In[3]:


class StoreList(Resource):
    def get(self):
        return{'Stores':[store.json() for store in StoreModel.query.all()]}

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'not found'},404
    
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message':"store with name '{}' already exists.".format(name)},400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'error in inserting'},500
        return store.json(),201
    
    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message':"store deleted"}
