
# breake და continue

# breake არის ციკლიდან გამოსვლა.

# continue არის ციკლის გაგრზლება

for i in range(15):
    if i == 10:
        break
        print("tu udris 10 es ar daiwereba")         

    if i % 2 == 0:
        continue 

    print(i)    


print("")

# ასოს პოვნა

found = None
for i in "hello":
    if i == "l":
        found = True
        break

else:
    found = False
        
print(found)

