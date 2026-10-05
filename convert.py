import json,os,sqlite3


with open('biblejson.json', 'r') as file:
    bible= json.load(file)
    

    

for book in bible["books"]:
        if book["englishName"]=="Genesis":
            print(book["chapters"][0]["verses"][1]["text"])
        
        

    
    
        
    
    
    
   