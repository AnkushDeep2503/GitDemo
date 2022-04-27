myDict = {
        "Ankush" : "Smart boy", 
        "Surbhi" : "Wise girl"
}
print(myDict['Ankush'])
print(myDict['Surbhi']) # Dictionary stores values in relation to keys as "Key": "Values"

# Nested Dictionary

myDict = {
        "Ankush" : "Smart boy", 
        "Surbhi" : "Wise girl",
        "newDict": {'New Words': 'Old Words', 'Vocab': 'Lexical Resources' }#Nested Dictionary
}
print(myDict['newDict']['New Words'])
print(myDict['newDict']['Vocab'])


