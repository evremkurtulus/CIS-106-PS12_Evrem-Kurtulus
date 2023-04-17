lname = ["Albert","Barth","Charlie","Dean","Effren","Facks","Greg","Hector","Isabel","Jackson"]
def forward(lname):
  for i in range (0,10,1):
    print(lname[i])
def reverse(lname):
  for x in range (9,-1,-1):
    print(lname[x])
forward(lname)
print("\n")
reverse(lname)