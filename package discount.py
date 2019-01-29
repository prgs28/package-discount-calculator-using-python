
qty_pck=int(input("enter no. of packages: "))
price=qty_pck*99
if(qty_pck>=10 and qty_pck<=19):
    dis=price*0.1
    print("CONGRATULATIONS!! you got a discount of 10%")
elif(qty_pck>=20 and qty_pck<=49):
    dis=price*0.2
    print("CONGRATULATIONS!! you got a discount of 20%")
elif(qty_pck>=50 and qty_pck<=99):
    dis=price*0.3
    print("CONGRATULATIONS!! you got a discount of 30%")
else:
    dis=price*0.4
    print("CONGRATULATIONS!! you got a discount of 40%")
print("you got a discount of: $",dis)
final_price=price-dis
print("the total amount is: ", final_price)
