
# for

for i in range(1, 6, 2):
    print(i)
# 1 ნიშნავს რომ დათვლა დაიწყება 1 დან ანუ: 1, 2, 3, 4, 5, ... . 6 არის სანამდეც უნდა მივიდეს. 2 ნიშნავს რომ 2-ით გაიზრდება ანუ: 0, 2, 4, ...


#რამეს დათვლა for-ში

count = 0
word = "hello world!"
for i in word:
    if i == "l":
        count += 1  
print(count)   

