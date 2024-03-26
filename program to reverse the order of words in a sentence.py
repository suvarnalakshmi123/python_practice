list = input("Input sep by space: ")
list = list.split()  
list.reverse()  
print("Exepected output:", end=" ")
for word in list:
    print(word, end=" ")