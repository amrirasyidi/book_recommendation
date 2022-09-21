import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

search_result = pickle.load(open('search_result.pkl', 'rb'))
search_define = pickle.load(open('search_define.pkl', 'rb'))
search_fit_transform = pickle.load(open('search_fit_transform.pkl', 'rb'))

# the starting point from where the app will run
app=Flask(__name__)

# Load the data set

# Load the search algorithm

# Load the collaborative algorithm


# define the url address. '/' indicates homepage
# landing page
@app.route('/')
def home():
    return render_template('home.html')
    # return "Hello World"

@app.route('/search_api', methods=['POST'])
def search_api():
    user_input = request.form.get('user_input')
    book_rec = search_result("harry potter",search_define)

    print(book_rec)

    return render_template('home.html',data=book_rec)
    

if __name__ == '__main__':
    app.run(debug = True)