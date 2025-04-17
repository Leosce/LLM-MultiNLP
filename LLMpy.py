#!/usr/bin/env python
# coding: utf-8

# # Text-classification

# In[16]:


# ! pip install  transformers
# ! pip install sentencepiece

from transformers import pipeline
import pandas as pd


# In[17]:


classifier = pipeline("text-classification" , model = 'distilbert-base-uncased-finetuned-sst-2-english' )
# Pipeline(name_of_task  , name of the model from hugging face)
# https://huggingface.co/models


# In[18]:


def classify(text):
    outputs = classifier(text)
    return outputs

