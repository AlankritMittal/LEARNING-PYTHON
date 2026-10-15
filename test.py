x = 0.00 ;
while True:
    print("This is test case");
    x = x+1 ;
    if x > 3:
        break; 
subjects = [None]*5;
print("Enter your 5 most favourite subjects")
for i in range(len(subjects)):
    subj = input()
    subjects[i] =subj
subjects.sort()
for i in range(len(subjects)):
    print(subjects[i])

target = "maths"
def search (subjects, target):
    for i in range (len(subjects)):
        if subjects[i] == target:
            return i+1
    return -1 
result = search(subjects, target)
print("The result of linear search is ",result)

   
   
   
