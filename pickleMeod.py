import pickle

# A Python object (dictionary in this case)
data = {"name": "Alice", "age": 30, "occupation": "Engineer"}

# Open a file in binary write mode
with open("data.pickle", "wb") as file:
    # Pickle the Python object and save it to file
    pickle.dump(data, file)

print("Data has been serialized and saved to data.pickle")

