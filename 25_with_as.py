
# with და as
#იგივე არის რაც .close()    

try:
    with open("text2.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("file not founded")        
        