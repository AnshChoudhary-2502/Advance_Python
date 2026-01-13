import pickle

data = {"name": "Ansh", "Age": 22, "Skills": ["Python", "SQL"]}

with open("data.pkl", "wb") as file:
    pickle.dump(data, file)                   # Serialization :- dump object/data into .pkl file

with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)           # Deserialization :- load object/data from a file

print(loaded_data)




# Pickling without files
list = [1,3,2,7,4]
binary_data = pickle.dumps(list)
print(binary_data)
original_data = pickle.loads(binary_data)
print(original_data)
