data1 = input("Enter temperature: ")
data2 = float(data1)
unit1 = input("Enter unit (C/F/K): ")
unit2 = unit1.lower()
temp1 = 0
temp2 = 0
temp3 = 0
if unit2 == "c":
    temp1 = (data2 * 9/5) + 32
    temp2 = data2 + 273.15
    print("Fahrenheit:", temp1)
    print("Kelvin:", temp2)
if unit2 == "f":
    temp1 = (data2 - 32) * 5/9
    temp2 = temp1 + 273.15
    print("Celsius:", temp1)
    print("Kelvin:", temp2)
if unit2 == "k":
    temp1 = data2 - 273.15
    temp2 = (temp1 * 9/5) + 32
    print("Celsius:", temp1)
    print("Fahrenheit:", temp2)