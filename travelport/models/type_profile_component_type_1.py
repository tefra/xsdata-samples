from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeProfileComponentType1(Enum):
    """Specifies the component names.

    (i.e AccountInfo, AirPreference, TravelDocument etc)
    """

    ACCOUNT_INFO = "AccountInfo"
    TRAVELER_INFO = "TravelerInfo"
    TRAVELER_IDENTITY_INFORMATION = "TravelerIdentityInformation"
    TRAVEL_DOCUMENT = "TravelDocument"
    ACCOUNTING_REFERENCE = "AccountingReference"
    POLICY_REFERENCE = "PolicyReference"
    LOYALTY_PROGRAM_ENROLLMENT = "LoyaltyProgramEnrollment"
    CONTRACT = "Contract"
    COMMISSION = "Commission"
    SERVICE_FEE = "ServiceFee"
    REMARK = "Remark"
    ALTERNATE_CONTACT = "AlternateContact"
    ALTERNATE_CONTACT_ADDRESS = "AlternateContactAddress"
    ALTERNATE_CONTACT_PHONE = "AlternateContactPhone"
    ALTERNATE_CONTACT_ELECTRONIC_ADDRESS = "AlternateContactElectronicAddress"
    COMMISSION_REFERENCE = "CommissionReference"
    ADDRESS = "Address"
    PHONE = "Phone"
    ELECTRONIC_ADDRESS = "ElectronicAddress"
    AIR_PREFERENCE = "AirPreference"
    VEHICLE_PREFERENCE = "VehiclePreference"
    HOTEL_PREFERENCE = "HotelPreference"
    RAIL_PREFERENCE = "RailPreference"
    PROFILE_PARENT_HISTORY = "ProfileParentHistory"
    FIELD_DATA = "FieldData"
    FIELD_GROUP_DATA = "FieldGroupData"
    ADVISORY = "Advisory"
    AGENCY_GROUP_INFO = "AgencyGroupInfo"
    AGENCY_INFO = "AgencyInfo"
    BRANCH_GROUP_INFO = "BranchGroupInfo"
    BRANCH_INFO = "BranchInfo"
    AGENT_INFO = "AgentInfo"
    TRAVELER_GROUP_INFO = "TravelerGroupInfo"
    PROFILE_STATUS = "ProfileStatus"
    PROFILE_LINK = "ProfileLink"
    OTHER_PREFERENCE = "OtherPreference"
    FORM_OF_PAYMENT = "FormOfPayment"
    EXTERNAL_IDENTIFIER = "ExternalIdentifier"
