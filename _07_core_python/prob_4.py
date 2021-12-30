mp = int(input("enter the market price "))

if mp>10000:
    print(f"net amount = {mp-(mp*0.2)}")
elif 7000<mp<=10000:
    print(f"net amount = {mp-(mp*0.15)}")
elif mp<=7000:
    print(f"net amount = {mp-(mp*0.1)}")



