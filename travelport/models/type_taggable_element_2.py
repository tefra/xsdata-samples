from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeTaggableElement2(Enum):
    """
    Specify which fixed field type this field refers to.
    """
    TRAVEL_DOCUMENT = "TravelDocument"
    LOYALTY_PROGRAM_ENROLLMENT = "LoyaltyProgramEnrollment"
    CONTRACT = "Contract"
    ALTERNATE_CONTACT = "AlternateContact"
    ADDRESS = "Address"
    PHONE = "Phone"
    ELECTRONIC_ADDRESS = "ElectronicAddress"
    ALTERNATE_CONTACT_ADDRESS = "AlternateContactAddress"
    ALTERNATE_CONTACT_PHONE = "AlternateContactPhone"
    ALTERNATE_CONTACT_ELECTRONIC_ADDRESS = "AlternateContactElectronicAddress"
    AIR_PREFERENCE = "AirPreference"
    HOTEL_PREFERENCE = "HotelPreference"
    VEHICLE_PREFERENCE = "VehiclePreference"
    RAIL_PREFERENCE = "RailPreference"
    OTHER_PREFERENCE = "OtherPreference"
    REMARK = "Remark"
    FIELD_DATA = "FieldData"
    FIELD_GROUP_DATA = "FieldGroupData"
    FORM_OF_PAYMENT = "FormOfPayment"
