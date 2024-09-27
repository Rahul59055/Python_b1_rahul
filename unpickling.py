import pickle


#Open the file in binary read mode


with open("data.pickle", "rb") as file:
    # Unpickle the Python object from the file
    loaded_data = pickle.load(file)
print("Deserialized data:", loaded_data)

