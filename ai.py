"""
    file: ai.py
    author: Orens Xhagolli
    description: EconSim logic
"""

from rit_object import *
from random import *


class FederalReserve(rit_object):
    #the three tools that the reserve can use to affect the interest rate
    __slots__ = ("primeR", "fedFundsR", "discountR")
    _types = (float, float, float)

    
class Country(rit_object):
    #All the data that will be modified/used/referred by the simulator
    __slots__ = ("name", "gdp", "gdppc", "population",
                 "pop_growth", "econ_growth", "currency",
                 "toUSD", "influence", "deficit", "debt")
    _types =    (str, float, int, int,
                 float, float, str,
                 float, int, float, float)


class GameTime(rit_object):
    #for simplicity purposes we only use weeks and years
    #1 year has 52 weeks
    __slots__ = ("week", "year")
    _types = (int, int)


class Expenditures(rit_object):
    #major spending categories. Can we have the user allocate them?
    __slots__ = ("total", "health", "military", "education", "infrastructure"
                 "research", "debtservice", "misc", "foreignaid")
    _types = (int, int, int, int, int, int, int, int)


class Income(rit_object):
    #major income categories. The user should be able to adjust tax rates
    #inside lag
    __slots__ = ("total", "taxes", "debtservice", "foreignaid", "ownerships")
    _types = (int, int, int, int, int)


class Leader(rit_object):
    #determines how easy it is for the leader to take action
    __slots__ = ("approval", "passed", "weeks")
    _types = (int, int, int)


def newCountry(name):
    """
    Creates a new country based on the provided name. The other values will be
    randomly generated within a range which will put this country among the
    poor nations, meaning that you will have to service some public debt, but
    also be able to receive foreign aid.
    """
    gdp = randint(100, 200) #gdp in millions of dollars
    population = randing(10, 20) #population in millions
    gdppc = gdp/population
    
    return Country(name, randint(100, 200)) 


