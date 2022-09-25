import dill as pickle
from flask import Flask, json, request, app, jsonify, url_for, render_template

# import re

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
similarity_scores = pickle.load(open('pickles/similarity_scores.pkl', 'rb'))
sparse_to_df_map = pickle.load(open('pickles/sparse_to_df_map.pkl', 'rb'))
recommender = pickle.load(open('pickles/recommender.pkl', 'rb'))


# Define the url address. '/' indicates homepage
# Landing page
@app.route('/')
def home():
    return render_template('home.html')

# For postman API
# @app.route('/search_api', methods=['POST'])
# def search_api():
#     data=request.json["data"]
#     print(data)

#     book_rec = search_result(data,search_define)
#     print(book_rec)

#     return book_rec

# For web app search
@app.route('/search', methods=['POST'])
def search():
    user_input = [str(i) for i in request.form.values()]
    
    # manual search
    # book_search = books_data[books_data['mod_title'].str.contains(user_input[0].lower())]
    # book_search = book_search.merge(images_data,how = 'left', on = "isbn")[["isbn_index","isbn","book_title","book_author","year_of_publication","image_url_s"]].drop_duplicates().head(5)
    # book_search = book_search.set_index("isbn").T.to_dict()
    
    # search using tdifvectorizer
    book_search = search_result(user_input[0],search_define)
    return render_template('home.html', book_search = book_search)

# For web app recommendation
@app.route('/rec', methods=['POST'])
def rec():
    sim_input = [str(i) for i in request.form.values()]

    book_rec = books_data[books_data['isbn_index'].isin(recommender(int(sim_input[0])))]
    book_rec = book_rec.merge(images_data[["isbn","image_url_m"]], how = "left", on = "isbn").head(6)
    book_rec = book_rec[book_rec['isbn_index']!=int(sim_input[0])]
    book_rec = book_rec.set_index("isbn").T.to_dict()
    
    return render_template('rec.html', book_rec = book_rec)

if __name__ == '__main__':
    app.run(debug = True)