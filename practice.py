# import json 
# import os
# for i in range(1,4):
#     if os.path.isfile("Num"+str(i)+".json"):
#         with open("Num"+str(i)+".json","r") as fh:
#             a = json.load(fh)

#         print("Load")
#     else:
#         with open("Num"+str(i)+".json","w") as fh:
#             json.dump(i,fh)
#             a = i
#         print("Dump")
#     print(a)


# y={"a":12,"b":4,"c":6,"d":2,"e":10}
# dic={}
# dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# sorted_values=sorted(dict.values())
# sorted_dict={}
# for i in sorted_values:
#     for k in dict.keys():
#         if dict[k]==i:
#             sorted_dict[k]=dict[k]
#             break
# print(sorted_dict)


# dic=[{"a":12},{"b":4},{"c":6},{"d":2},{"e":10}]
# d={}
# for i in dic:
#     d.update(i)
# # print(d)
# a=d[0]
# for i in d:
#     # print(d[i])
#     if d[i]>a:
#         a=d[i]
#         # key=value[

# dict1={'bijender':45,'deepak':0,'param':20,'anjili':30,'roshini':50}
dict_1=[{"a":2,"b":"d"},{"b":4},{"c":6},{"d":18},{"e":0}]

# d={}
# for i in dict_1:
#     d.update(i)
# mini = 0
# list_ = []
# for i in d:
#     if d[i] > mini:
#         mini = d[i]
#         list_.append(mini)
# print(list_)

# a={}
# for i in dic1:
#     a.update(i)
# print(a)
# dic=a
# k={}
# for i in dic:
#     a=dic[i]
#     for j in dic:
#         b=dic[j]
#         if a>b:
#             k[j]=b
# for i in dic:
#     a=dic[i]
#     for j in dic:
#         b=dic[j]
#         if a<b:
#             k[j]=b
# print(k)

l=[]
for i in dict_1:
    l.append(i)
# print(l,"..")    

    # b = {}
    # for j in range(len(dict_1)):
    #     mini =
    #     for i in dict_1:
    #         if mini > dict_1[i]:
    #             mini = dict_1[i]
    #             key_1 = i
    #     b.update({key_1:mini})
    #     del dict_1[key_1]
    # pprint.pprint(b)
    

    # dict_2={}
    # for i in dict_1:
    #     s=dict_1[i]
    #     for j in dict_1:
    #         a=dict_1[j]
    #         if s>a:
    #             dict_2[j]=a
    # for i in dict_1:
    #     s=dict_1[i]
    #     for j in dict_1:
    #         a=dict_1[j]
    #         if s<a:
    #             dict_2[j]=a 
        # print(dict_2[i],i) 
