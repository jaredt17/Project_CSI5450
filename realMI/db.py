from enum import Enum
from typing import List

from pymongo import MongoClient
import json
from bson import ObjectId

DB = "realmi"

class TABLES(str, Enum):

    HOMES = "HOMES"
    LOCATIONS = "LOCATIONS"
    APPLIANCES = "APPLIANCES"
    AGENTS = "AGENTS"
    OWNERS = "OWNERS"
    TRANSACTIONS = "TRANSACTIONS"
    COMPANIES = "COMPANIES"


class HomeType(str, Enum):

    house= "house"
    mansion = "mansion"
    apartment = "apartment"
    townhome = "townhome"
    condo = "condo"

    # I think this needs some work:
        # The user should select a home type, and then we just need to validate
        # If they select 2 floors it cant be an apartment etc.
        # Call HomeType.validate() returns true or false
    def validate(user_input: str, floor_space: int, floors: int, bed_rooms: int, land_size: int) -> str:
        print("entered validation step:  ")
        print(user_input)
        print(floors)
        
        # todo add more here as needed, we can also validate all other inputs in forms for other collections too
        
        if floor_space >= 6000 and land_size > 2 and user_input == 'mansion':
            return True
        
        if floors > 1 and user_input == 'apartment':
            print("Floors was greater than 1 and apartment set")
            return False
        
        # Should return True by default?
        return True

class HOME(str, Enum):

    floor_space = "floor_space"
    floors = "floors"
    bed_rooms = "bed_rooms"
    bath_rooms = "bath_rooms"
    land_size = "land_size"
    year_constructed = "year_constructed"
    home_type = "home_type"
    appliances = "appliances"
    owner_id = "owner_id"
    location_id = "location_id"


class LOCATION(str, Enum):

    street_number = "street_number"
    unit_number = "unit_number"
    street = "street"
    city = "city"
    zip = "zip"
    state = "state"
    county = "county"
    country = "country"


class APPLIANCE(str, Enum):

    name = "name"
    model = "model"
    year = "year"
    make = "make"
    price = "price"


class AGENT(str, Enum):

    first_name = "first_name"
    last_name = "last_name"
    companies = "companies"
    sales = "sales"
    

class OWNER(str, Enum):

    first_name = "first_name"
    last_name = "last_name"
    ssn = "ssn"
    no_dependents = "no_dependents"
    income = "income"
    age = "age"
    profession = "profession"


class TRANSACTION(str, Enum):

    owner_id = "owner_id"
    agent_id = "agent_id"
    company_id = "company_id"
    location_id = "location_id"
    home_id = "home_id"
    date = "date"
    price = "price"


class COMPANY(str, Enum):

    name = "name"
    commission = "commission"
    street_number = "street_number"
    unit_number = "unit_number"
    street = "street"
    city = "city"
    zip = "zip"
    state = "state"

def setup():

    cl = MongoClient()

    cl.drop_database(DB)

    realmi = cl[DB]
    
    for k in TABLES.__members__.keys():
        realmi.create_collection(k)

def main():
    setup()


if __name__ == "__main__":
    main()