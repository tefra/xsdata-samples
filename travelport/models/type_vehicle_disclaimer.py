from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


class TypeVehicleDisclaimer(Enum):
    VEHICLES = "Vehicles"
    SHUTTLE = "Shuttle"
    AGE_REQUIREMENTS = "AgeRequirements"
    ADDL_DRIVER_INFO = "AddlDriverInfo"
    ADDL_DRIVER_FEES = "AddlDriverFees"
    PAYMENT = "Payment"
    GUARANTEE = "Guarantee"
    DEPOSIT = "Deposit"
    VOUCHER = "Voucher"
    LICENSE = "License"
    PICKUP = "Pickup"
    DROP_OFF = "DropOff"
    FUEL = "Fuel"
    GEOGRAPHIC = "Geographic"
    LIABILITIES = "Liabilities"
    SPECIAL_EQUIPMENT = "SpecialEquipment"
    INSURANCE = "Insurance"
    ELIGIBILITY = "Eligibility"
    FEES = "Fees"
    OTHER = "Other"
