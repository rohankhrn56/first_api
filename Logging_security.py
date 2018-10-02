
# coding: utf-8

# In[1]:


from models.Logging_user import UserModel
from werkzeug.security import safe_str_cmp


# In[2]:


def authenticate(username , password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user


# In[3]:


def identity(payload):
    print(payload)
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

