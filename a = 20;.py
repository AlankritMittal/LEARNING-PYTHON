print ("Enter Fahreinheit Temperature : ");
fahreinheit = float(input());
celsius = (fahreinheit-32)* 5/9
print ("The value in celsius is: "+str(celsius));
if celsius > 25:
    print ("The weather is quite hot today");
elif celsius >0 and celsius < 25  :
    print("The weather is quite nice today");
else:
    print ("Its freezing outside");

string = "Alankrit"
print (string.find("a"))
text = "Hello"
print(text)
text += " World"
print(text)
for i in range(4):
    print (string[i])

print(string[0:5])