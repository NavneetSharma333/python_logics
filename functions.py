def login(username, password):
    if username == "admin" and password == "123":
        return True
    else:
        return False
    
print(login("user1", "pass1"))
print(login("user2", "pass2"))
print(login("usr3", "pass3"))
print(login("admin","123"))