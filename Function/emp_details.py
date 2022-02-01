
details = {}
name = input("Enter the employee name : ")
details.setdefault('name', name)
address = input(f"Enter the address of {name} : ")
details.setdefault('address', address)
phone = int(input(f"Enter the phone number of {name} :"))
details.setdefault('phone', phone)
print(details)
print(f"Name : {details['name']}\nAddress : {details['address']}\nPhone No : {details['phone']}")
