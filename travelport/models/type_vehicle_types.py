from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


class TypeVehicleTypes(Enum):
    """
    Properties
    ----------
    ANY_VEHICLE
        Any vehicle - GDS Pseudo Code ACAR
    ANY2_3_DOOR_VEHICLE
        Any 2-3 door vehicle - GDS Pseudo Code ALLB
    ANY2_3_DOOR_PASSENGER_CAR
        Any 2-3 door passenger cars - GDS Pseudo Code ALBC
    ANY2_4_DOOR_VEHICLE
        Any 2-4 door vehicle - GDS Pseudo Code ALLC
    ANY2_4_DOOR_PASSENGER_CAR
        Any 2-4 door passenger cars - GDS Pseudo Code ALCC
    ANY4_5_DOOR_VEHICLE
        Any 4-5 door vehicle - GDS Pseudo Code ALLD
    ANY4_DOOR_PASSENGER_CAR
        Any 4 door passenger cars - GDS Pseudo Code ALDC
    ANY_ELITE
        Any elite - GDS Pseudo Code AELT
    ANY_COUPE_ROADSTER
        Any Coupe and/or Roadster - GDS Pseudo Code ACPR
    ANY_SPECIAL
        Any Special - GDS Pseudo Code ASPC
    ANY_PICK_UP
        Any PickUp - GDS Pseudo Code APUP
    ANY_WAGON
        Any Wagon - GDS Pseudo Code AWGN
    ANY_RECREATIONAL_VEHICLE
        Any Recreational Vehicle - GDS Pseudo Code AREC
    ANY_SUV
        Any SUV - GDS Pseudo Code ASUV
    ANY_PASSENGER_VAN
        Any Passenger Van - GDS Pseudo Code AVAN
    ANY6_PASSENGER_VAN_OR_SUV
        Any 6 Passenger Van or SUV - GDS Pseudo Code ASIX
    ANY7_PASSENGER_VAN_OR_SUV
        Any 7 Passenger Van or SUV - GDS Pseudo Code ASEV
    ANY8_PASSENGER_VAN_OR_SUV
        Any 8 Passenger Van or SUV - GDS Pseudo Code AEIG
    ANY4_OR_ALL_WHEEL_DRIVE
        Any 4 or all wheel drive- GDS Pseudo Code AFWD
    ANY_ALL_TERRAIN_VEHICLE
        Any all Terrain Vehicle- GDS Pseudo Code ATRV
    ANY_COMMERCIAL_TRUCK
        Any commercial truck- GDS Pseudo Code ACGO
    ANY_LIMOUSINE
        Any Limousine- GDS Pseudo Code ALMO
    ANY_SPORT
        Any Sport- GDS Pseudo Code ASPT
    ANY_CONVERTIBLE
        Any Convertible- GDS Pseudo Code ACNV
    ANY_SPECIAL_OFFER_VEHICLE
        Any Special Offer Vehicle- GDS Pseudo Code AOFR
    ANY_MONOSPACE
        Any Monospace- GDS Pseudo Code AMNO
    ANY_MOTOR_HOME
        Any Motor Home- GDS Pseudo Code AMTO
    ANY2_WHEEL_VEHICLE
        Any 2-Wheel Vehicle- GDS Pseudo Code AMCY
    ANY_CROSSOVER
        Any Crossover- GDS Pseudo Code ACRS
    ALL_MANUAL_TRANSMISSION_VEHICLES
        All Manual Transmission Vehicles- GDS Pseudo Code AMAN
    ALL_AUTOMATIC_TRANSMISSION_VEHICLES
        All Automatic Transmission Vehicles- GDS Pseudo Code AUTO
    ALL_GASOLINE_VEHICLES
        All Gasoline Powered Vehicles- GDS Pseudo Code AGAS
    ALL_PETROL_VEHICLES
        All Petrol Powered Vehicles- GDS Pseudo Code APET
    ALL_DIESEL_VEHICLES
        All Diesel Powered Vehicles- GDS Pseudo Code ADSL
    ANY_GREEN_VEHICLE
        Any Green vehicle (hybrid, electric, LPG, hydrogen, multi-fuel)- GDS
        Pseudo Code AGRN
    ALL_HYBRID_VEHICLES
        All Hybrid Vehicles- GDS Pseudo Code AHYB
    ALL_ELECTRIC_VEHICLES
        All Electric powered vehicles- GDS Pseudo Code AELC
    ALL_HYDROGEN_VEHICLES
        All Hydrogen powered vehicles- GDS Pseudo Code AHYD
    ALL_MULTI_FUEL_VEHICLES
        All Multi-Fuel powered vehicles- GDS Pseudo Code AMFP
    ALL_LPGVEHICLES
        All LPG/Compressed Gas powered vehicles- GDS Pseudo Code ACPG
    ALL_ETHANOL_VEHICLES
        All Ethanol powered vehicles   - GDS Pseudo Code AETH
    """

    ANY_VEHICLE = "AnyVehicle"
    ANY2_3_DOOR_VEHICLE = "Any2-3DoorVehicle"
    ANY2_3_DOOR_PASSENGER_CAR = "Any2-3DoorPassengerCar"
    ANY2_4_DOOR_VEHICLE = "Any2-4DoorVehicle"
    ANY2_4_DOOR_PASSENGER_CAR = "Any2-4DoorPassengerCar"
    ANY4_5_DOOR_VEHICLE = "Any4-5DoorVehicle"
    ANY4_DOOR_PASSENGER_CAR = "Any4DoorPassengerCar"
    ANY_ELITE = "AnyElite"
    ANY_COUPE_ROADSTER = "AnyCoupe-Roadster"
    ANY_SPECIAL = "AnySpecial"
    ANY_PICK_UP = "AnyPickUp"
    ANY_WAGON = "AnyWagon"
    ANY_RECREATIONAL_VEHICLE = "AnyRecreationalVehicle"
    ANY_SUV = "AnySUV"
    ANY_PASSENGER_VAN = "AnyPassengerVan"
    ANY6_PASSENGER_VAN_OR_SUV = "Any6PassengerVanOrSUV"
    ANY7_PASSENGER_VAN_OR_SUV = "Any7PassengerVanOrSUV"
    ANY8_PASSENGER_VAN_OR_SUV = "Any8PassengerVanOrSUV"
    ANY4_OR_ALL_WHEEL_DRIVE = "Any4OrAllWheelDrive"
    ANY_ALL_TERRAIN_VEHICLE = "AnyAllTerrainVehicle"
    ANY_COMMERCIAL_TRUCK = "AnyCommercialTruck"
    ANY_LIMOUSINE = "AnyLimousine"
    ANY_SPORT = "AnySport"
    ANY_CONVERTIBLE = "AnyConvertible"
    ANY_SPECIAL_OFFER_VEHICLE = "AnySpecialOfferVehicle"
    ANY_MONOSPACE = "AnyMonospace"
    ANY_MOTOR_HOME = "AnyMotorHome"
    ANY2_WHEEL_VEHICLE = "Any2WheelVehicle"
    ANY_CROSSOVER = "AnyCrossover"
    ALL_MANUAL_TRANSMISSION_VEHICLES = "AllManualTransmissionVehicles"
    ALL_AUTOMATIC_TRANSMISSION_VEHICLES = "AllAutomaticTransmissionVehicles"
    ALL_GASOLINE_VEHICLES = "AllGasolineVehicles"
    ALL_PETROL_VEHICLES = "AllPetrolVehicles"
    ALL_DIESEL_VEHICLES = "AllDieselVehicles"
    ANY_GREEN_VEHICLE = "AnyGreenVehicle"
    ALL_HYBRID_VEHICLES = "AllHybridVehicles"
    ALL_ELECTRIC_VEHICLES = "AllElectricVehicles"
    ALL_HYDROGEN_VEHICLES = "AllHydrogenVehicles"
    ALL_MULTI_FUEL_VEHICLES = "AllMultiFuelVehicles"
    ALL_LPGVEHICLES = "AllLPGVehicles"
    ALL_ETHANOL_VEHICLES = "AllEthanolVehicles"
