def CelsiusToFahrenheit(value):

    if (value < -273.15):
        return "That temperature doesn't make sense!"

    return (value * 1.8) + 32

temperatures=[10,-20,-289,100]
for i in temperatures:
    print CelsiusToFahrenheit(i)
