
#tuple
#იგივე list მაგრამ ელემენტებს ვერ შევცვლით და წონა(mb) უფრო პატარა აქვს

data = (3, 5, 13, 4, 3, True, "str", 6.5) 

#data[4] = 6 #ერორი
print(data[6])
print(data[2:7:2])

print(" ")

print(data.count(3))
print(len(data))
print(data)

print(" ")

#tuple ვარიანტი 2

data2 = 3, 4, 1, 2, 4, True, 4.5,
print(data2)

print(" ")

data3 = (5)# ეს არ ითველბა როგორც tuple
print(data3)

data4 = (5,) #ასე ჩაითვლება როგორც tuple
print(data4)

data5 = 5,
print(data5)

#მაგალითები


for i in data:
    print(i)


#როგორ გადავაქციოთ list-ი tuple-ში

list = [4, 3, 5, 1]

new_data = tuple(list)
print(new_data)

#როგორ გადავაქციოთ str-ი tuple-ში

word = tuple("hello world")
print(word)

