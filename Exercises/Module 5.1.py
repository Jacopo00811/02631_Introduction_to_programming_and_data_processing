def convertTemperature(T, unitFrom, unitTo):
    
    if unitFrom == "Celsius":
        if unitTo == "Fahrenheit":
            T = 1.8*T + 32
        elif unitTo == "Kelvin":
            T = T + 273.15
        else:
            T = T
    
    elif unitFrom == "Fahrenheit":
        if unitTo == "Celsius":
            T = (T-32)/1.8
        elif unitTo == "Kelvin":
            T = (T + 459.67)/1.8
        else:
            T = T
    
    else:
        if unitTo == "Fahrenheit":
            T = 1.8*T - 459.67
        elif unitTo == "Celsius":
            T = T - 273.15
        else:
            T = T
    
    
    return T

print(convertTemperature(50.0, "Fahrenheit", "Celsius"))