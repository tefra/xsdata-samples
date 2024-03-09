from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeProfileDataElementType2(Enum):
    """
    Specify which fixed field type this field refers to.
    """

    TRAVEL_DOCUMENT = "TravelDocument"
    ACCOUNTING_REFERENCE = "AccountingReference"
    POLICY_REFERENCE = "PolicyReference"
    COMMISSION_REFERENCE = "CommissionReference"
    LOYALTY_PROGRAM_ENROLLMENT = "LoyaltyProgramEnrollment"
    COMMISSION = "Commission"
    CONTRACT = "Contract"
    SERVICE_FEE = "ServiceFee"
    REMARK = "Remark"
    FIELD_DATA = "FieldData"
    FIELD_GROUP_DATA = "FieldGroupData"
    ALTERNATE_CONTACT = "AlternateContact"
    AIR_PREFERENCE = "AirPreference"
    HOTEL_PREFERENCE = "HotelPreference"
    VEHICLE_PREFERENCE = "VehiclePreference"
    ADDRESS = "Address"
    PHONE = "Phone"
    ELECTRONIC_ADDRESS = "ElectronicAddress"
    TRAVELER_IDENTITY_INFORMATION = "TravelerIdentityInformation"
    EXTERNAL_IDENTIFIER = "ExternalIdentifier"
    ALTERNATE_CONTACT_ADDRESS = "AlternateContactAddress"
    ALTERNATE_CONTACT_PHONE = "AlternateContactPhone"
    ALTERNATE_CONTACT_ELECTRONIC_ADDRESS = "AlternateContactElectronicAddress"
    ADVISORY = "Advisory"
    RAIL_PREFERENCE = "RailPreference"
    PROVIDER_INFO = "ProviderInfo"
    OTHER_PREFERENCE = "OtherPreference"
    PROPRIETARY_DATA = "ProprietaryData"
    FORM_OF_PAYMENT = "FormOfPayment"
