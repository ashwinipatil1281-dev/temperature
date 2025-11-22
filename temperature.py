import sys

if len(sys.argv) != 2:
    print("Usage: python temp.py <temperature>")
    sys.exit(1)

temp = float(sys.argv[1])

if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")
