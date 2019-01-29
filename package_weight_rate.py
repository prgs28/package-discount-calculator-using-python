
pck_weight=int(input("enter package weight: "))
if(pck_weight<=2):
    rate=1.5*pck_weight
elif(pck_weight>2 and pck_weight<=6):
    rate=3*pck_weight
elif(pck_weight>6 and pck_weight<=10):
    rate=4*pck_weight
else:
    rate=4.75*pck_weight

print("shipping charges: ",rate)
