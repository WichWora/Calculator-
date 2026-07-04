print("=== Scientific Calculator ===")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        exit()
    result = num1 / num2
else:
    print("Invalid operator!")
    exit()

print(f"\nResult: {result}")

# Hidden Easter Eggs
if result == 520:
    print("\n❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️")
    print("      I LOVE YOU <3")
    print("Will you be my girlfriend? 🌹")
    print("❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️")
elif result == 521:
    print("\n🥰 I LOVE YOU TOO!")
elif result == 1314:
    print("\n💍 Together Forever ❤️")
elif result == 999:
    print("\n💕 Love Forever!")