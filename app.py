import dill as pickle
from flask import Flask, json, request, app, jsonify, url_for, render_template

import re

import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity




# the starting point from where the app will run
app=Flask(__name__, template_folder='pages')

# Load the data set
books_data = pickle.load(open('pickles/books_data.pkl', 'rb'))
images_data = pickle.load(open('pickles/images_data.pkl', 'rb'))

# Load the search algorithm
search_define = pickle.load(open('pickles/search_define.pkl', 'rb'))
search_fit_transform = pickle.load(open('pickles/search_fit_transform.pkl', 'rb'))
search_result = pickle.load(open('pickles/search_result.pkl', 'rb'))

# Load the collaborative algorithm


# Define the url address. '/' indicates homepage
# Landing page
@app.route('/')
def home():
    return render_template('home.html')

# For postman API
@app.route('/search_api', methods=['POST'])
def search_api():
    data=request.json["data"]
    print(data)

    book_rec = search_result(data,search_define)
    print(book_rec)

    return book_rec

# For web app
@app.route('/search', methods=['POST'])
def search():
    user_input = [str(i) for i in request.form.values()]
    book_rec = search_result(user_input[0],search_define)

    return render_template('home.html',data=book_rec)

@app.route('/rec')
def rec():
    user_input = [str(i) for i in request.form.values()]
    return render_template('test.html', forward_message = user_input)

if __name__ == '__main__':
    app.run(debug = True)