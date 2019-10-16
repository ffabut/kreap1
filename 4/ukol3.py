def dualHello(user1, user2=None):
    if user2 != None:
        print("Hello " + user1 + " and " + user2 + "!")
    else:
        print("Hello " + user1 + "!")

# test zda to jede:
dualHello("Jan", "Leona")
dualHello("Leona")
