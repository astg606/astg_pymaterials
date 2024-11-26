#!/usr/bin/env python

"""
   Module containing utility functions for converting temperatures
   from one unit to another. It has the following functions:

      - convert_celsius_to_kelvin
      - convert_celsius_to_fahrenheit
      - convert_kelvin_to_celsius
      - convert_kelvin_to_fahrenheit
      - convert_fahrenheit_to_celsius
      - convert_fahrenheit_to_kelvin
"""

# Local modules
# TODO: import the constants module here to use zeroCelsius

#--------------------------------------------------------------------------

def convert_celsius_to_kelvin(temperatureC: float) -> float:
    """
       Convert temperature from Celsius to Kelvin.
       
       Parameters
       ----------
       temperatureC : float
            Temperature in degree Celsius

       Returns
       -------
       temperatureK : float
            Temperature in degree Kelvin
    """
    return temperatureC + constants.zeroCelsius

#--------------------------------------------------------------------------

def convert_celsius_to_fahrenheit(temperatureC: float) -> float:
    """
       Convert temperature from Celsius to Fahrenheit.

       Parameters
       ----------
       temperatureC : float
            Temperature in degree Celsius

       Returns
       -------
       temperatureF : float
            Temperature in degree Fahrenheit
    """
    return (9.0/5.0)*temperatureC + 32.0

#--------------------------------------------------------------------------

def convert_kelvin_to_celsius(temperatureK: float) -> float:
    """
       Convert temperature from Kelvin to Celsius.
       
       Parameters
       ----------
       temperatureK : float
            Temperature in degree Kelvin

       Returns
       -------
       temperatureC : float
            Temperature in degree Celsius
    """
    return temperatureK - constants.zeroCelsius

#--------------------------------------------------------------------------

def convert_kelvin_to_fahrenheit(temperatureK: float) -> float:
    """
       Convert temperature from Kelvin to Fahrenheit.

       Parameters
       ----------
       temperatureK : float
            Temperature in degree Kelvin

       Returns
       -------
       temperatureF : float
            Temperature in degree Fahrenheit
    """
    return (9.0/5.0)*(temperatureK - constants.zeroCelsius) + 32.0

#--------------------------------------------------------------------------

def convert_fahrenheit_to_celsius(temperatureF: float) -> float:
    """
       Convert temperature from Fahrenheit to Celsius.

       Parameters
       ----------
       temperatureF : float
            Temperature in degree Fahrenheit

       Returns
       -------
       temperatureC : float
            Temperature in degree Celsius
    """
    return (5.0/9.0)*(temperatureF - 32.0)

#--------------------------------------------------------------------------

def convert_fahrenheit_to_kelvin(temperatureF: float) -> float:
    """
       Convert temperature from Fahrenheit to Kelvin

       Parameters
       ----------
       temperatureF : float
            Temperature in degree Fahrenheit

       Returns
       -------
       temperatureK : float
            Temperature in degree Kelvin
    """
    return (5.0/9.0)*(temperatureF - 32.0) +  constants.zeroCelsius


#--------------------------------------------------------------------------

if __name__ == '__main__':
   print (convert_celsius_to_kelvin(15.7))
   print (convert_kelvin_to_celsius(302.9))
