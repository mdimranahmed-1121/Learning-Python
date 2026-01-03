dict={
 "name":"imran",
 "age" :26,
 "roll no.":1814037,
 "reg. num.":1121
}

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("age"))
new_dict={
    "city":"dhaka",
    "region":"savar",
    "religion":"islam"
}
dict.update(new_dict)
print(dict)
dict.update({"area":"arapara"})
print(dict)