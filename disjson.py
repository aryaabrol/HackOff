import json
import pandas as pd

dis = pd.read_csv('diseases.csv')

names = dis["Disease Name"]
info = dis["Information"]
syms = dis["Symptoms"]
causes = dis["Causes"]
digs = dis["Diagnosis"]
mgmt = dis["Management"]

print(len(info[0]))

# function to add to JSON 
def write_json(data, filename='dis.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

"""with open('dis.json') as json_file: 
    data = json.load(json_file) 
      
    temp = data['intents']

for i in range(len(names)):
    a = {"tag":names[i] + " info", 
         "patterns": ["What is " + names[i] + "?", "Tell me about " + names[i], "Explain about " + names[i], "Can you tell me about " + names[i] + "?"],
         "responses": [info[i]]
        }  
    temp.append(a)

    b = {"tag":names[i] + " symptoms", 
         "patterns": ["What are the symptoms of " + names[i] + "?", "Tell me the symptoms of " + names[i], "How do we know if we have "  + names[i] + "?", "How do I know if I have " + names[i] + "?",],
         "responses": [syms[i]]
        }  
    temp.append(b)

    c = {"tag":names[i] + " causes", 
         "patterns": ["What are the causes for " + names[i], "Tell me the causes for " + names[i], "How is " + names[i] + " caused?", "How does "  + names[i] + " start?"],
         "responses": [causes[i]]
        }  
    temp.append(c)

    d = {"tag":names[i] + " diagnosis", 
         "patterns": ["How to diagnose " + names[i] + "?", "Tell methods to diagnose " + names[i], "How can we diagnose " + names[i] + "?", "How can " + names[i] + " be cured?", "How to cure " + names[i] + "?"],
         "responses": [digs[i]]
        }  
    temp.append(d)

    e = {"tag":names[i] + " management", 
         "patterns": ["How can we manage " + names[i] + "?", "Methods to manage " + names[i], "How can I manage " + names[i] + "?", "How can one manage " + names[i] + "?", "Ways to manage " + names[i]],
         "responses": [mgmt[i]]
        }  
    temp.append(e)
      
write_json(data)
"""