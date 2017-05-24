def CelsiusToFahrenheit(value):

    if (value < -273.15):
         return ""

    return str((value * 1.8) + 32) + "\n"

temperatures=[10,-20,-289,100]
file = open("file.txt", "w")

for i in temperatures:
    file.write(CelsiusToFahrenheit(i))

file.close()
