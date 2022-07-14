from typing import Iterable, Tuple
import pandas
import math


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    celsius = ((fahrenheit_temp - 32) / 1.8000)

    return round(celsius, 2) # remove pass statement and implement me


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    fahrenheit = (celsius_temp * 1.8000) + 32
    return round(fahrenheit, 2)  # remove pass statement and implement me

def convert_to_kelvin(celsius_temp: float) -> int:

    kelvin = celsius_temp + 273.15

    return round(kelvin, 2)


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    conv_temp = []
    for temperature in temperatures:
        if input_unit_of_measurement == "f":
            new_temp = (temperature, convert_to_celsius(temperature))
            conv_temp.append(new_temp)
        elif input_unit_of_measurement == "c":
            new_temp = (temperature, convert_to_fahrenheit(temperature))
            conv_temp.append(new_temp)
        elif input_unit_of_measurement == "a":
            new_temp = (temperature, convert_to_kelvin(temperature))
            conv_temp.append(new_temp)
        #print(conv_temp)

    return tuple(conv_temp)



    #pass  # remove pass statement and implement me
