import pickle

data = {"a": 1, "b": 2}

with open("data.pkl", "wb+") as f:
    pickle.dump(data, f)
    f.seek(0)
    pickle.load(f)
