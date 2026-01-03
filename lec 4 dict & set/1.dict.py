# info={
#     "name":"imran",
#     "age":23,
#     "li":[1,2,3,40],
#     "tup":(1,2,3,4,5)
# }
# print(info)
# print(info['li'])
dict={
    "key":"value",#string
    "name":"imran",
    "learning":"coding",
    "marks":94.5
}
print(dict)
new_dict={
    "key":"value",#string
    "name":"imran",
    "age":23, #int
    "learning":["coding","python","c","c++"],#list
    "number":(1,2,3,4),#tuple
    "marks":94.5#float
}
print(new_dict)
print(new_dict["age"])
print(new_dict["learning"][0])
print(new_dict["number"][3])
new_dict["learning"]="java"
print(new_dict)