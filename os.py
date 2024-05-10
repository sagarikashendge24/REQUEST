import requests
import json
import os

# from requests.models import ContentDecodingError
if  os.path.isfile("courses.json"):
    with open ("courses.json","r") as saral_data:
       data= json.load(saral_data)   
else:
    saral_api = " http://saral.navgurukul.org/api/courses"    
    saral_url = requests.get(saral_api)                       
    data = saral_url.json()
    with open ("courses.json","w") as saral_data:
        json.dump(data,saral_data,indent = 4)      
serial_no = 0
id_lst=[]
for i in data["availableCourses"]:
    print(serial_no+1 ,i["name"], i["id"])
    id_lst.append(i["id"])
    serial_no=serial_no+1
print("")
user_input =int(input("Enter your courses number that you want to learn:- "))
parent_id=data["availableCourses"][user_input-1]["id"]
print(data["availableCourses"][user_input-1]["name"])
parent_name = data["availableCourses"][user_input-1]["name"]
id = id_lst[user_input-1]
if os.path.isfile("parentes"+str(user_input)+".json"):
    with open ("parentes"+str(user_input)+".json","r") as saral_data:
        data_1=json.load(saral_data)   
else:
    parent_api = "http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][user_input-1]["id"])+"/exercises"
    parent_url = requests.get(parent_api)
    data_1 = parent_url.json()
    with open ("parentes"+str(user_input)+".json","w") as child_data:
        json.dump(data_1,child_data,indent=4)
        
serial_no_1=0
for i in data_1["data"]:
    print(serial_no_1+1,".",i["name"])
    if len(i["childExercises"])>0:
        s= 0
        for j in i['childExercises']:
            s = s+ 1
            print("",s,j['name'])
    else:
        print("",i["name"])
    serial_no_1+=1
topic_no = int(input("Enter topic number that you want to learn:- "))
if data_1["data"][topic_no-1]["childExercises"]==[]:
    print(" 1.",data_1["data"][topic_no-1]["slug"])
else:
    l = 0
    while l < len(data_1["data"][topic_no-1]["childExercises"]):
        print("    ",l+1,data_1["data"][topic_no-1]["childExercises"][l]["name"])
        l = l+1  
            
questions_no = int(input("choose the specific questions no :- "))
que=questions_no-1
slug = data_1["data"][topic_no-1]["childExercises"][que]["slug"]
Content_id = data_1["data"][topic_no-1]["childExercises"][que]["id"]
child_exercises_url = ("http://saral.navgurukul.org/api/courses/"+str(parent_id)+"/exercise/getBySlug?slug=" + slug )
Data_3 = requests.get(child_exercises_url)
convert_data = Data_3.json()
if os.path.isfile("Request/content/"+str(Content_id )+".json"):
   with open("Request/content/"+str(Content_id )+".json","r") as f:
    content = json.load(f)
    print(content) 
else:
    with open("Request/content/"+str(Content_id )+".json","w") as f:
        json.dump(convert_data["content"],f,indent=4)
        print(convert_data["content"])

# 