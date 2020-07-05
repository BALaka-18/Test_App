# -*- coding: utf-8 -*-


from google.colab import drive
drive.mount('/content/drive')

from flask import Flask,render_template,url_for,request
import requests
import pandas as pd
import threading
from flask_ngrok import run_with_ngrok
import matplotlib as ml
import matplotlib.pyplot as plt
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# %%html
# <h1><strong>PART 1 : </strong></h1>

data = pd.read_csv('/content/drive/My Drive/data - data.csv')
data.head(10)

data.info()

data.replace("\\N","Not Mentioned",inplace=True)
data.head(10)

data['request_received'] = pd.to_datetime(data['request_received'])
data['response_delivered'] = pd.to_datetime(data['response_delivered'])
data.info()

data.to_csv('data_new.csv')

"""## Visualization :"""

# Commented out IPython magic to ensure Python compatibility.

data = pd.read_csv('/content/drive/My Drive/dress - dress.csv')       # Code written after mounting my Drive.
data['category'].replace('polka dot','polka_dot',inplace=True)
dress_category = list(set(data.category.values))

app = Flask(__name__,template_folder='drive/My Drive/templates')      # Code written after mounting my Drive.
# run_with_ngrok(app)

@app.route("/")
def home():
  return render_template('index.html',dress_category=dress_category)

@app.route('/predict',methods=['POST'])
def predict():
  category = request.form.get('item')
  links = sorted(list(data[data.category == category].image_url.values))
  return render_template('predict.html',dress_category = dress_category,links = links)

app.run()

