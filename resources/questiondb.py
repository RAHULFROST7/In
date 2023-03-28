#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install pymongo')


# In[2]:


from pymongo import MongoClient


# In[3]:


client = MongoClient('mongodb+srv://webinterview:12345@cluster0.unj3vql.mongodb.net/main?retryWrites=true&w=majority');
print('connection successful');


# In[4]:


db = client['main']
col = db['questions']

dict = {'question':'what is deep learning','answer1':'Deep learning is a subset of machine learning that uses artificial neural networks with multiple layers to model and solve complex problems. It involves training these networks on large datasets to learn patterns and make predictions.','answer2':'In deep learning, the neural networks are designed to learn and represent data in multiple levels of abstraction, which enables them to perform tasks such as image and speech recognition, natural language processing, and decision making.','answer3':'Deep learning is a type of AI that relies on artificial neural networks with multiple layers to process and analyze large amounts of data. These networks are trained using algorithms that adjust the weights and biases of the connections between neurons to optimize performance on a specific task','answer4':'At its core, deep learning is a way of training artificial neural networks to learn from data and make predictions. This involves breaking down complex problems into smaller, more manageable sub-problems and using a combination of supervised and unsupervised learning techniques to train the network. The resulting model can then be used to make predictions on new data, such as recognizing objects in an image or translating text into another language'}

x = col.insert_one(dict)
print(x.inserted_id)


# In[5]:


myquery = {'question':'what is deep learning'}

data = col.find(myquery)

for x in data:
    collected = list(x.values())[1:]
    print(collected)


# In[ ]:




