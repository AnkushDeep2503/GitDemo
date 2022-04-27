dictionary = {
        "Spielberb": "Jurrasic Park",
        "Tarantino": "Pulp Fiction",
        "Coen": "No Country For Old Man",
        "Box Office": "1 Billion",
        234567: 87980000,
        "myFavdictionary": {"The Shawshank Redemption": "Interstellar", "Departed": "The Raging Bull"}
}
#Dictionary Methods
print(dictionary.values())
print(type(dictionary.values()))
print(list(dictionary.keys())) #prints the keys of the dictionary
print(list(dictionary.values())) #prints the values of the dictionary
print(list(dictionary.items())) #prints the (keys, values) for all the contents of the dictionary
newdictionary = {"Tom Cruise": "Top Gun",
            "Brad Pitt": "Seven",
            "Coen": "True Grit"
}
dictionary.update(newdictionary) #updating new keys and values in the existing dictionary by using update
#Even the existing values can be updated
print(dictionary)
# print(dictionary.update(newdictionary))
print(dictionary.get("Tarantino")) #prints value associated with key Tarantino.
print(dictionary["Tarantino"]) #prints value associated with key Tarantino.
print(dictionary.get("Scorsese")) #return None as the Scorsese is not present in the dictionary
# print(dictionary["Scorsese"]) #throws an error as Scorsese is not present in the dictionary
