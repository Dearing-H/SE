#converts Farenheit -> Celcius


def Farenheit_to_celcius(temp_in_farenheit):
    temp_in_celcius = (temp_in_farenheit - 32) * (5 / 9)
    return temp_in_celcius


current_temp = Farenheit_to_celcius(81)
                                    
print(current_temp)
