# [WIP]Book Recommendation Machine Learning Web App

## Author's Note
What I've learn from this project
1. VS code
1. Git
1. Collaborative filtering
    1. Making the content-user matrix
    1. Calculate similarity using cosine similarity
1. Create a "search engine" using TfidfVectorizer
---
## Goals
By the end of this project, we will create a web app with the following features:
1. Book search feature
1. "People also like" feature (collaborative filtering)
1. "Similar book" feature (clustering)
    1. Similarity by rating
    1. Similarity by content(?) (fiction with fiction etc)

## Steps
This project will go through
1. Preparing the GitHub repository
1. Data preparation
    1. Data Cleaning
    1. Exploratory Data Analysis (EDA)
    1. Feature engineering
    1. ~~Feature selection~~
1. Creating the model <-- 🔥 **Currently in this stage** 🔥
    1. Model training
    1. ~~Model assessment~~
    1. Model serialization (to make the model reusable in the web app)
1. Setting up the web app
    1. Flask
    1. Streamlit
    1. Running and testing the web app (postman)
1. Web app deployment
    1. Heroku
    1. Dockers
    
## Tools

---
## Sources
1. [Krish Naik's End To End Machine Learning Project Implementation With Dockers,Github Actions And Deployment](https://www.youtube.com/watch?v=MJ1vWb1rGwM)
1. [Dataquest's Build A Book Recommendation System With Machine Learning](https://www.youtube.com/watch?v=x-alwfgQ-cY)
1. [CampusX-Official Book Recommender System](https://github.com/campusx-official/book-recommender-system)
1. Kaggle
    1. [[Data]Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset?datasetId=1004280)
    1. [[Notebook]Book_Item-Based Collaborative Filtering](https://www.kaggle.com/code/sebnemgurek/book-item-based-collaborative-filtering)
    1. [[Notebook]Book Recommendation System](https://www.kaggle.com/code/fahadmehfoooz/book-recommendation-system)
1. Additional
    1. [Additional: How to Build a Book Recommendation System](https://www.analyticsvidhya.com/blog/2021/06/build-book-recommendation-system-unsupervised-learning-project/)
    1. [Rpubs: PCA and Linear Regression](https://rpubs.com/esobolewska/pcr-step-by-step#:~:text=PCA%20in%20linear%20regression%20has,with%20Partial%20Least%20Squares%20Regression.)
    1. [Stat SE: PCA vs Linear Regression](https://stats.stackexchange.com/questions/410516/using-pca-vs-linear-regression)
    1. [Statology: PCRegression](https://www.statology.org/principal-components-regression-in-python/)
