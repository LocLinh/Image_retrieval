from flask import Flask
import pickle
import numpy as np
import faiss


app = Flask(__name__)

@app.route("/")
def hello_world():
    with open("./vectors/paths_total.pkl", "rb") as f:
        paths = pickle.load(f)

    with open("./vectors/paths_total.pkl", "rb") as vector_f:
        vectors = pickle.load(vector_f)
    
    vector_dim = len(vectors[0])
    vectors = np.array(vectors)

    # faiss create index
    index = faiss.IndexFlatL2(vector_dim)
    index.add(vectors)

    # faiss search

    return f"<p>{paths[0]}</p>"

@app.route("/user")
def user():
    return "<p>user</p>"
