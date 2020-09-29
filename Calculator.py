#GIven Below is My Code TO the Calculator. It shows you All the three arithmetic operations together.




print("Enter The First Number")
inpnum = input()

print("Enter The Second Number")
inpnum2 = input()

print("Sum of These Two Numbers Is- \n",float(inpnum) + float(inpnum2))
print("Quotient of These Two Numbers Is- \n", float(inpnum) / float(inpnum2))
print("Differe1nce of These Two Numbers Is- \n", float(inpnum) - float(inpnum2))
print("Product of These Two Numbers Is- \n", float(inpnum) * float(inpnum2))


print("If their any number left, Enter The Third Number-")
inpnum3 = input()

print("Warning: The Third Number will be added to the answers of These Answers Above.")

print(float(inpnum) + float(inpnum2) + float(inpnum3))
print(float(inpnum) / float(inpnum2) + float(inpnum3))
print(float(inpnum) - float(inpnum2) + float(inpnum3))
print(float(inpnum) * float(inpnum2) + float(inpnum3))