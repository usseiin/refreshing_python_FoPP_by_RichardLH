dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

msg = dividend / divisor if divisor != 0 else "Error, Cannot divide by zero"

print(msg)
