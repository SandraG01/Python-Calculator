# number1= int(input("insert number:\n "))
# for i in range(number1):
    # print(f"hello student {i+1}")

menu = []
start = "start"
while start != "checkout":
    start = input(" What would you like to order? ")
    if start == "checkout":
        print("Going to checkout")
    else:
        menu.append(start)
        print(menu)

print(menu)