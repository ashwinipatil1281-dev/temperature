import sys

default_temp = 25.0

if len(sys.argv) == 2:
    temp = float(sys.argv[1])
    source = "User Input"
else:
    temp = default_temp
    source = "Self-assigned"

print(f"Temperature: {temp} ({source})")

if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")
