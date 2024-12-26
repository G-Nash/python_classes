# break and continue

# pass
# is more like a placepholder
# used to manage syntax error 

# nested loops 

units=450
if (units<=200):
    if(units<=100):
        cBill=units*(-5)
    else:
        cBill=0
else:
    if(units>200 and units<350):
        cBill=units*10
    else:
        cBill=units*20

print(f"{units} units consumed and current bill is {cBill}")