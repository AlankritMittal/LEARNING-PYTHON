names = ["Alan" , "Mugil" , "Akshansh", "Larib" , "Vibhor"]
age = [27 , 29 , 24 , 33, 32]
for i in range (len(names)):
    print ("The age of ",names[i],"is",age[i],"\n")

while names:
    del names[0]
    del age[0]
print (names, age)
    
subjects = ["Math", "Science", "History", "Art", "Music"]
size = len(subjects)

# Loop backward: start at (size - 1), stop before -1, step by -1
for i in range(size - 1, -1, -1):
    # Remove and return the item at index i
    deleted_item = subjects.pop(i)
    print(f"Deleted: {deleted_item} | Remaining list: {subjects}")

print("\nFinal list state:", subjects)