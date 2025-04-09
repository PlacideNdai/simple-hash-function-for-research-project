
# user login database 
#for demo salt is manually made, but its usually randomly generated. 

user_db = {
    "userA":{
        "username" : "usera",
        "salt": "userAsalt",
        "password": "copiedpassword"
        },
    
    
    "userB":{
        "username" : "userb",
        "salt": "userBsalt",
        "password": "copiedpassword"
        }
}


#hash function
def simple_hash(string, salt):
    #after the salt generation (which we did not)
    
    addedString = string + salt
    hash_value = 0
    
    for char in addedString:
        hash_value = (hash_value * 31 + ord(char)) % 1000
    return hash_value


userApass_hashing = user_db["userA"]["password"]
userASalt = user_db["userA"]["salt"]

print(simple_hash(userApass_hashing, userASalt))


userBpass_hashing = user_db["userB"]["password"]
userBSalt = user_db["userB"]["salt"]

print(simple_hash(userBpass_hashing, userBSalt))