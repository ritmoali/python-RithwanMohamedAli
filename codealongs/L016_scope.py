#scope, life time of a viriable.
#Local scope: Only available locally in a function.
#Global scope: Available through execution of program

name = "Fredrik"

def main():
    global name
    name = "Kalle"
    print(name)

print (name)
main()
print(name) 


# # def main():
# #    name = "Fredrik"
# #    print(name) 
# # # Python doesn't  
# # if name == "Fredri":
# #    last_name = "Johansson"

#print(last_name)

# # for i in range(10):
