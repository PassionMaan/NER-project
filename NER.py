#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy


# In[2]:


get_ipython().system('python -m spacy download en_core_web_lg')


# In[3]:


nlp = spacy.load("en_core_web_lg")
nlp


# In[5]:


doc = nlp("Dear Customer, your Amazon order containing 2 items of Rs. 1129  has been confirmed. Use the Amazon app to track your order.")


# In[6]:


doc


# In[7]:


type(doc)


# In[8]:


doc.ents


# In[9]:


from spacy import displacy
displacy.render(doc, style="ent", jupyter=True)


# In[38]:


import json
with open('/Customer Analysis/latest-anno_annotations.json', 'r') as f:
    data = json.load(f)


# In[40]:



data['examples'][0]


# In[41]:


data['examples'][0].keys()


# In[42]:


data['examples'][0]['content']


# In[43]:


data['examples'][0]['annotations'][0]


# In[46]:


training_data = []
for example in data['examples']:
  temp_dict = {}
  temp_dict['text'] = example['content']
  temp_dict['entities'] = []
  for annotation in example['annotations']:
    start = annotation['start']
    end = annotation['end']
    label = annotation['tag'].upper()
    temp_dict['entities'].append((start, end, label))
  training_data.append(temp_dict)
print(training_data[0])


# In[47]:


training_data[0]['entities']


# In[ ]:




