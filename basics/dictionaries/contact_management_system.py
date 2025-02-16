users = {
    "contact_1":{
        "name":{
        "first_name" :"Ibad",
        "last_name" : "Uddin"
        },
    "age":"18",
    "email":"ibaduddinsiddiqui418@gmail.com",
    "phone":"03353948636"
    },
    "contact_2":{
        "name":{
        "first_name" :"Ammad",
        "last_name" : "Uddin"
        },
    "age":"16",
    "email":"ammaduddinsiddiqui418@gmail.com",
    "phone":"03353948637"
    },
    "contact_3":{
        "name":{
        "first_name" :"Aquib",
        "last_name" : "Uddin"
        },
    "age":"20",
    "email":"aquibuddinsiddiqui418@gmail.com",
    "phone":"03353948648"
    }
}

print(users["contact_1"]["name"]["first_name"])

users["contact_1"]["name"] = {
    "first_name" : "Rabia",
    "last_name" : "Hamid"
}

print(users["contact_1"])


#genral syntax for for loop
#for key,value in dictionary.items()
for contact, info in users.items():
    print(f'Your name is {info["name"]["first_name"]} age is {info["age"]}')