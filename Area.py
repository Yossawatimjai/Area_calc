
def triangle():
    height=float(input("Input height:"))
    base=float(input("Input Base:"))
    area=0.5*height*base
    print(area)

def circle():
    r=float(input("Input radius:"))
    print("22/7 input 1 3.14 Input 0")
    pi=int(input("Input 1 or 0:"))
    if(pi==1):
        area=22/7*(r**2)
    else:
        area=3.14*(r**2)
    print(area)

print("******************Calc******************")
print("triangle : 1")
print("circle : 2")
mode= int(input("Select area formula: "))

if (mode==1):
    triangle()
elif(mode==2):
    circle()