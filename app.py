import dill as pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd




# the starting point from where the app will run
app=Flask(__name__)

# Load the data set


# Load the search algorithm
search_define = pickle.load(open('pickles/search_define.pkl', 'rb'))
search_fit_transform = pickle.load(open('pickles/search_fit_transform.pkl', 'rb'))
search_result = pickle.load(open('pickles/search_result.pkl', 'rb'))

# Load the collaborative algorithm


# define the url address. '/' indicates homepage
# landing page
@app.route('/')
def home():
    return render_template('home.html')
    # return "Hello World"

@app.route('/search_api', methods=['POST'])
def search_api():
    user_input = request.form.get("user_input")
    book_rec = search_result(user_input,search_define)

    print(book_rec)

    return render_template('home.html',data=book_rec)
    

if __name__ == '__main__':
    app.run(debug = True)