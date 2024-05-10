import requests
import json
import pprint 
nav_api =  "http://join.navgurukul.org/api/partners"
nav_url = requests.get(nav_api)                       
Data_1= nav_url.json()

with open ("navgurukul.json","w") as nav_data:
    json.dump(Data_1,nav_data,indent = 4)
# serial_no = 0
list_1=[]
dict_1={}
for i in Data_1["data"]:
    a=i["name"], i["id"]
    print(i["id"],i["name"])
    # serial_no=serial_no+1
    list_1.append((i["name"],i["id"]))
    dict_1.update(list_1)
    with open("data.json","w") as f:
        json.dump(dict_1,f,indent=4)
# print(list_1) 
user_input=input("In what order do you want assending(a) or desending(d)---------------------------------")
if user_input=="a":
    sorted_values=sorted(dict_1.values())
    sorted_dict={}
    for i in sorted_values:
        for k in dict_1.keys():
            if dict_1[k]==i:
                sorted_dict[k]=dict_1[k]
            
                break
    # for i in sorted_dict:
    #     c=sorted_dict[i]
    #     print(c,[i])       
    # pprint.pprint(sorted_dict)
    print(sorted_dict)        
    # x=sorted_dict
    # pprint.pprint(x)

    # d={}
    # for i in dict_1:
    #     d.update({i:dict_1[i]})
    # mini = 0
    # for i in d:
    #     if d[i] > mini:
    #         mini = d[i]
    #         print(d[i],i)
elif user_input=="d":     
    new={}
    length=len(dict_1)
    for i in range(length):
        max=0
        for val in dict_1:
            if max<dict_1[val]:
                max=dict_1 [val]
                key=val
        new.update({key:max})
        dict_1.pop(key)
    for j in new:
        print(new[j],j)
