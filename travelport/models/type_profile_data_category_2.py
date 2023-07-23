from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeProfileDataCategory2(Enum):
    """
    The category of data that controls what data will be returned in the response.

    Properties
    ----------
    GENERAL_INFORMATION
        Basic information (AgencyInfo/BranchGroupInfo/etc) and
        AccountingReference for Traveler
    ALL_DETAILS
        All stored profile datac
    ALTERNATE_CONTACTS
        Basic information and all AlternateContact data for the retrieved
        profile including a. Address b. Phone c. ElectronicAddress
    CUSTOM_INFORMATION
        All data for all custom fields/field groups and basic information
    COMMISSIONS
        Commission data for the retrieved profile and basic information
    CONTRACTS
        Contract data for the retrieved profile and basic information
    FORMS_OF_PAYMENT
        Payment data for the retrieved profile and basic information
    LOYALTY_PROGRAMS_ALL
        All loyalty program enrollment data for each SupplierType and basic
        information
    LOYALTY_PROGRAMS_AIR
        All loyalty program enrollment for the Air supplier type (i.e.,
        LoyaltyProgramEnrollment.Supplier Type=Air) and basic information
    LOYALTY_PROGRAMS_VEHICLE
        All loyalty program enrollment for the Vehicle supplier type (i.e.,
        LoyaltyProgramEnrollment.Supplier Type=Vehicle) and basic
        information
    LOYALTY_PROGRAMS_HOTEL
        All loyalty program enrollment for the Hotel supplier type (i.e.,
        LoyaltyProgramEnrollment.Supplier Type=Hotel) and basic information
    LOYALTY_PROGRAMS_RAIL
        All loyalty program enrollment for the Rail supplier type (i.e.,
        LoyaltyProgramEnrollment.Supplier Type=Rail) and basic information
    LOYALTY_PROGRAMS_OTHER
        All loyalty program enrollment for the Other supplier type (i.e.,
        LoyaltyProgramEnrollment.Supplier Type=Other) and basic information
    POLICY_REFERENCE
    PREFERENCES_ALL
        All preference data for each preference type (i.e., Air, Vehicle,
        Hotel, Rail, Other) and basic information
    PREFERENCES_AIR
        All Air Preference data and basic information
    PREFERENCES_VEHICLE
        All Vehicle Preference data and basic information
    PREFERENCES_HOTEL
        All Hotel Preference data and basic information
    PREFERENCES_RAIL
        All Rail Preference data and basic information
    PREFERENCES_OTHER
        All Other Preference data and basic information
    SERVICE_FEES
        ServiceFee data for the retrieved profile and basic information
    TRAVEL_DOCUMENTS_ALL
        All related data for each Travel Document and basic information
    TRAVEL_DOCUMENTS_PASSPORTS
        All related data for Passport (i.e., TravelDocument.Type=Passport)
        and basic information
    TRAVEL_DOCUMENTS_VISAS
        All related data for Visa (i.e., TravelDocument.Type=Visa) and basic
        information
    TRAVEL_DOCUMENTS_OTHER
        All related data for any travel document other than Passport or Visa
        (i.e., TravelDocument.Type not equal to Passport or Visa) and basic
        information
    TRAVELER_LINKS
        All the links for all the profiles who are related to the requested
        Traveler profile and basic information
    TRAVELER_IDENTITY_INFORMATION
        All data for all traveler identity information
    """
    GENERAL_INFORMATION = "General Information"
    ALL_DETAILS = "All Details"
    ALTERNATE_CONTACTS = "Alternate Contacts"
    CUSTOM_INFORMATION = "Custom Information"
    COMMISSIONS = "Commissions"
    CONTRACTS = "Contracts"
    FORMS_OF_PAYMENT = "Forms of Payment"
    LOYALTY_PROGRAMS_ALL = "Loyalty Programs - All"
    LOYALTY_PROGRAMS_AIR = "Loyalty Programs - Air"
    LOYALTY_PROGRAMS_VEHICLE = "Loyalty Programs - Vehicle"
    LOYALTY_PROGRAMS_HOTEL = "Loyalty Programs - Hotel"
    LOYALTY_PROGRAMS_RAIL = "Loyalty Programs - Rail"
    LOYALTY_PROGRAMS_OTHER = "Loyalty Programs - Other"
    POLICY_REFERENCE = "PolicyReference"
    PREFERENCES_ALL = "Preferences - All"
    PREFERENCES_AIR = "Preferences - Air"
    PREFERENCES_VEHICLE = "Preferences - Vehicle"
    PREFERENCES_HOTEL = "Preferences - Hotel"
    PREFERENCES_RAIL = "Preferences - Rail"
    PREFERENCES_OTHER = "Preferences - Other"
    SERVICE_FEES = "Service Fees"
    TRAVEL_DOCUMENTS_ALL = "Travel Documents - All"
    TRAVEL_DOCUMENTS_PASSPORTS = "Travel Documents - Passports"
    TRAVEL_DOCUMENTS_VISAS = "Travel Documents - Visas"
    TRAVEL_DOCUMENTS_OTHER = "Travel Documents - Other"
    TRAVELER_LINKS = "Traveler Links"
    TRAVELER_IDENTITY_INFORMATION = "TravelerIdentityInformation"
