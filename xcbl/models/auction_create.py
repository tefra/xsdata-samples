from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


@dataclass
class Agency:
    agency_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyCoded",
            "type": "Element",
            "required": True,
        }
    )
    agency_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyCodedOther",
            "type": "Element",
        }
    )
    agency_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyDescription",
            "type": "Element",
        }
    )
    code_list_identifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeListIdentifierCoded",
            "type": "Element",
        }
    )
    code_list_identifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeListIdentifierCodedOther",
            "type": "Element",
        }
    )


@dataclass
class AuctionCategory:
    auction_category_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCategoryName",
            "type": "Element",
            "required": True,
        }
    )
    auction_category_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCategoryLevel",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionCreateSummary:
    total_number_of_auction_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfAuctionItems",
            "type": "Element",
        }
    )
    total_number_of_participants: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfParticipants",
            "type": "Element",
        }
    )


@dataclass
class AuctionItemComponent:
    auction_create_detail: Optional["AuctionCreateDetail"] = field(
        default=None,
        metadata={
            "name": "AuctionCreateDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionSpecifications:
    auction_create_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCreateName",
            "type": "Element",
        }
    )
    auction_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionType",
            "type": "Element",
        }
    )
    auction_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionStatus",
            "type": "Element",
        }
    )
    partial_bid_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialBidIndicator",
            "type": "Element",
        }
    )


@dataclass
class ContactFunction:
    contact_function_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactFunctionCoded",
            "type": "Element",
            "required": True,
        }
    )
    contact_function_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactFunctionCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ContactNumber:
    contact_number_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactNumberValue",
            "type": "Element",
            "required": True,
        }
    )
    contact_number_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactNumberTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    contact_number_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactNumberTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class Country:
    country_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCoded",
            "type": "Element",
            "required": True,
        }
    )
    country_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCodedOther",
            "type": "Element",
        }
    )


@dataclass
class Currency:
    currency_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCoded",
            "type": "Element",
            "required": True,
        }
    )
    currency_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCodedOther",
            "type": "Element",
        }
    )


@dataclass
class DateQualifier:
    date_qualifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    date_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateQualifierCodedOther",
            "type": "Element",
        }
    )


@dataclass
class Gpscooridinates:
    class Meta:
        name = "GPSCooridinates"

    gpssystem: Optional[str] = field(
        default=None,
        metadata={
            "name": "GPSSystem",
            "type": "Element",
            "required": True,
        }
    )
    latitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "required": True,
        }
    )
    longitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Language:
    language_dependent: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageDependent",
            "type": "Attribute",
        }
    )
    language_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageCoded",
            "type": "Element",
            "required": True,
        }
    )
    language_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageCodedOther",
            "type": "Element",
        }
    )
    locale_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocaleCoded",
            "type": "Element",
        }
    )
    locale_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocaleCodedOther",
            "type": "Element",
        }
    )


class MaximumValueConditionsCoded(Enum):
    OTHER = "Other"
    WHERE_AIR_EQUALS1 = "WhereAirEquals1"
    WHERE_BUTYL_ACETATE_EQUALS1 = "WhereButylAcetateEquals1"
    WHERE_H2_OEQUALS1_OR_WATER_EQUALS1 = "WhereH2OEquals1OrWaterEquals1"
    CORRECTED_TO60_DEGREES_FAHRENHEIT = "CorrectedTo60DegreesFahrenheit"
    WHERE_TOLUENE_EQUALS1 = "WhereTolueneEquals1"
    VAPOR_IN_AIR = "VaporInAir"
    VAPOR_IN_OTHER_THAN_AIR = "VaporInOtherThanAir"
    STANDARD_TEMPERATURE_AND_PRESSURE = "StandardTemperatureAndPressure"
    CONDITIONS_OTHER_THAN_STANDARD_TEMPERATURE_AND_PRESSURE = "ConditionsOtherThanStandardTemperatureAndPressure"
    IN_ETHYL_ALCOHOL = "InEthylAlcohol"
    IN_ETHYL_ETHER = "InEthylEther"
    IN_WATER = "InWater"
    AT1_ATMOSPHERE_PRESSURE = "At1AtmospherePressure"
    WHERE_ETHER_EQUALS1 = "WhereEtherEquals1"
    ACTUAL = "Actual"
    PREDICTED = "Predicted"
    AIR_DRIED_BASIS = "Air-DriedBasis"
    AS_RECEIVED_BASIS = "As-ReceivedBasis"
    DRY_BASIS = "DryBasis"
    EQUILIBRIUM_BASIS = "EquilibriumBasis"
    MOISTURE_AND_ASH_FREE_BASIS = "MoistureAndAsh-FreeBasis"
    OXIDIZING_ATMOSPHERE = "OxidizingAtmosphere"
    REDUCING_ATMOSPHERE = "ReducingAtmosphere"
    CALCULATED = "Calculated"
    SCALED_WEIGHT = "ScaledWeight"
    RATCHET = "Ratchet"
    SATURATED_VAPOR = "SaturatedVapor"
    UNCONDITIONAL = "Unconditional"
    SHORT_TERM = "Short-Term"
    TIME_WEIGHTED = "Time-Weighted"
    CORRECTED = "Corrected"
    UNCORRECTED = "Uncorrected"
    OFF_PEAK = "OffPeak"
    ON_PEAK = "OnPeak"
    INTERMEDIATE = "Intermediate"
    AVERAGE = "Average"
    PER_GALLON = "PerGallon"
    ESTIMATED = "Estimated"
    MINIMUM = "Minimum"
    MIST = "Mist"
    PREDOMINANT = "Predominant"
    TOTAL = "Total"
    COST = "Cost"
    TENANT = "Tenant"
    OWNER = "Owner"
    FOR_SALE = "ForSale"
    REAL_ESTATE_OWNED_OR_CORPORATE_OWNED = "RealEstateOwnedOrCorporateOwned"
    BOARDED_OR_BLOCKED_UP = "BoardedOrBlockedUp"
    PLANNED = "Planned"
    COMPLETED = "Completed"
    SOLD = "Sold"
    RENTED = "Rented"
    CURRENT = "Current"
    CURRENT_LIST = "CurrentList"
    EFFECTIVE = "Effective"
    LIST_WHEN_SOLD = "ListWhenSold"
    SALES = "Sales"
    FINAL_LIST = "FinalList"
    AS_IS = "AsIs"
    AS_REPAIRED_OR_IMPROVED = "AsRepairedOrImproved"
    INSTANTANEOUS = "Instantaneous"
    LOW = "Low"
    LOW_TO_GOOD = "LowToGood"
    LOW_TO_HIGH = "LowToHigh"
    LOW_TO_MEDIUM = "LowToMedium"
    LOW_TO_MODERATE = "LowToModerate"
    MEDIUM = "Medium"
    MEDIUM_TO_GOOD = "MediumToGood"
    MEDIUM_TO_HIGH = "MediumToHigh"
    MODERATE = "Moderate"
    MODERATE_TO_GOOD = "ModerateToGood"
    MODERATE_TO_HIGH = "ModerateToHigh"
    MODERATE_TO_MEDIUM = "ModerateToMedium"
    GOOD = "Good"
    GOOD_TO_HIGH = "GoodToHigh"
    HIGH = "High"
    BUDGETED = "Budgeted"
    FORECAST = "Forecast"
    ADJUSTED = "Adjusted"
    ALLOCATED = "Allocated"
    INCREASING = "Increasing"
    STABLE = "Stable"
    DECLINING = "Declining"
    PREVIOUS = "Previous"
    POTENTIAL = "Potential"
    MODELED = "Modeled"
    MEASURED = "Measured"
    MAXIMUM = "Maximum"
    SUMMER_ON_PEAK = "SummerOn-Peak"
    SUMMER_MID_PEAK = "SummerMid-Peak"
    SUMMER_OFF_PEAK = "SummerOff-Peak"
    SUMMER_SUPER_ON_PEAK = "SummerSuperOn-Peak"
    SUMMER_SUPER_OFF_PEAK = "SummerSuperOff-Peak"
    WINTER_ON_PEAK = "WinterOn-Peak"
    WINTER_MID_PEAK = "WinterMid-Peak"
    WINTER_OFF_PEAK = "WinterOff-Peak"
    WINTER_SUPER_ON_PEAK = "WinterSuperOn-Peak"
    WINTER_SUPER_OFF_PEAK = "WinterSuperOff-Peak"
    SUMMER_DAY = "SummerDay"
    SUMMER_NIGHT = "SummerNight"
    WINTER_DAY = "WinterDay"
    WINTER_NIGHT = "WinterNight"
    SUMMER = "Summer"
    WINTER = "Winter"
    DAY = "Day"
    NIGHT = "Night"
    PEAK_2 = "Peak-2"
    PEAK_3 = "Peak-3"
    PEAK_4 = "Peak-4"
    SHOULDER = "Shoulder"
    NON_TIME_RELATED_DEMAND = "NonTimeRelatedDemand"


class MaximumValueSignificanceCoded(Enum):
    OTHER = "Other"
    APPROXIMATELY = "Approximately"
    EQUAL_TO = "EqualTo"
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"
    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL_TO = "LessThanOrEqualTo"
    NOT_EQUAL_TO = "NotEqualTo"
    TRACE = "Trace"
    TRUE_VALUE = "TrueValue"
    OBSERVED_VALUE = "ObservedValue"
    OUT_OF_RANGE = "OutOfRange"


class MeasurementValueConditionsCoded(Enum):
    OTHER = "Other"
    WHERE_AIR_EQUALS1 = "WhereAirEquals1"
    WHERE_BUTYL_ACETATE_EQUALS1 = "WhereButylAcetateEquals1"
    WHERE_H2_OEQUALS1_OR_WATER_EQUALS1 = "WhereH2OEquals1OrWaterEquals1"
    CORRECTED_TO60_DEGREES_FAHRENHEIT = "CorrectedTo60DegreesFahrenheit"
    WHERE_TOLUENE_EQUALS1 = "WhereTolueneEquals1"
    VAPOR_IN_AIR = "VaporInAir"
    VAPOR_IN_OTHER_THAN_AIR = "VaporInOtherThanAir"
    STANDARD_TEMPERATURE_AND_PRESSURE = "StandardTemperatureAndPressure"
    CONDITIONS_OTHER_THAN_STANDARD_TEMPERATURE_AND_PRESSURE = "ConditionsOtherThanStandardTemperatureAndPressure"
    IN_ETHYL_ALCOHOL = "InEthylAlcohol"
    IN_ETHYL_ETHER = "InEthylEther"
    IN_WATER = "InWater"
    AT1_ATMOSPHERE_PRESSURE = "At1AtmospherePressure"
    WHERE_ETHER_EQUALS1 = "WhereEtherEquals1"
    ACTUAL = "Actual"
    PREDICTED = "Predicted"
    AIR_DRIED_BASIS = "Air-DriedBasis"
    AS_RECEIVED_BASIS = "As-ReceivedBasis"
    DRY_BASIS = "DryBasis"
    EQUILIBRIUM_BASIS = "EquilibriumBasis"
    MOISTURE_AND_ASH_FREE_BASIS = "MoistureAndAsh-FreeBasis"
    OXIDIZING_ATMOSPHERE = "OxidizingAtmosphere"
    REDUCING_ATMOSPHERE = "ReducingAtmosphere"
    CALCULATED = "Calculated"
    SCALED_WEIGHT = "ScaledWeight"
    RATCHET = "Ratchet"
    SATURATED_VAPOR = "SaturatedVapor"
    UNCONDITIONAL = "Unconditional"
    SHORT_TERM = "Short-Term"
    TIME_WEIGHTED = "Time-Weighted"
    CORRECTED = "Corrected"
    UNCORRECTED = "Uncorrected"
    OFF_PEAK = "OffPeak"
    ON_PEAK = "OnPeak"
    INTERMEDIATE = "Intermediate"
    AVERAGE = "Average"
    PER_GALLON = "PerGallon"
    ESTIMATED = "Estimated"
    MINIMUM = "Minimum"
    MIST = "Mist"
    PREDOMINANT = "Predominant"
    TOTAL = "Total"
    COST = "Cost"
    TENANT = "Tenant"
    OWNER = "Owner"
    FOR_SALE = "ForSale"
    REAL_ESTATE_OWNED_OR_CORPORATE_OWNED = "RealEstateOwnedOrCorporateOwned"
    BOARDED_OR_BLOCKED_UP = "BoardedOrBlockedUp"
    PLANNED = "Planned"
    COMPLETED = "Completed"
    SOLD = "Sold"
    RENTED = "Rented"
    CURRENT = "Current"
    CURRENT_LIST = "CurrentList"
    EFFECTIVE = "Effective"
    LIST_WHEN_SOLD = "ListWhenSold"
    SALES = "Sales"
    FINAL_LIST = "FinalList"
    AS_IS = "AsIs"
    AS_REPAIRED_OR_IMPROVED = "AsRepairedOrImproved"
    INSTANTANEOUS = "Instantaneous"
    LOW = "Low"
    LOW_TO_GOOD = "LowToGood"
    LOW_TO_HIGH = "LowToHigh"
    LOW_TO_MEDIUM = "LowToMedium"
    LOW_TO_MODERATE = "LowToModerate"
    MEDIUM = "Medium"
    MEDIUM_TO_GOOD = "MediumToGood"
    MEDIUM_TO_HIGH = "MediumToHigh"
    MODERATE = "Moderate"
    MODERATE_TO_GOOD = "ModerateToGood"
    MODERATE_TO_HIGH = "ModerateToHigh"
    MODERATE_TO_MEDIUM = "ModerateToMedium"
    GOOD = "Good"
    GOOD_TO_HIGH = "GoodToHigh"
    HIGH = "High"
    BUDGETED = "Budgeted"
    FORECAST = "Forecast"
    ADJUSTED = "Adjusted"
    ALLOCATED = "Allocated"
    INCREASING = "Increasing"
    STABLE = "Stable"
    DECLINING = "Declining"
    PREVIOUS = "Previous"
    POTENTIAL = "Potential"
    MODELED = "Modeled"
    MEASURED = "Measured"
    MAXIMUM = "Maximum"
    SUMMER_ON_PEAK = "SummerOn-Peak"
    SUMMER_MID_PEAK = "SummerMid-Peak"
    SUMMER_OFF_PEAK = "SummerOff-Peak"
    SUMMER_SUPER_ON_PEAK = "SummerSuperOn-Peak"
    SUMMER_SUPER_OFF_PEAK = "SummerSuperOff-Peak"
    WINTER_ON_PEAK = "WinterOn-Peak"
    WINTER_MID_PEAK = "WinterMid-Peak"
    WINTER_OFF_PEAK = "WinterOff-Peak"
    WINTER_SUPER_ON_PEAK = "WinterSuperOn-Peak"
    WINTER_SUPER_OFF_PEAK = "WinterSuperOff-Peak"
    SUMMER_DAY = "SummerDay"
    SUMMER_NIGHT = "SummerNight"
    WINTER_DAY = "WinterDay"
    WINTER_NIGHT = "WinterNight"
    SUMMER = "Summer"
    WINTER = "Winter"
    DAY = "Day"
    NIGHT = "Night"
    PEAK_2 = "Peak-2"
    PEAK_3 = "Peak-3"
    PEAK_4 = "Peak-4"
    SHOULDER = "Shoulder"
    NON_TIME_RELATED_DEMAND = "NonTimeRelatedDemand"


class MeasurementValueSignificanceCoded(Enum):
    OTHER = "Other"
    APPROXIMATELY = "Approximately"
    EQUAL_TO = "EqualTo"
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"
    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL_TO = "LessThanOrEqualTo"
    NOT_EQUAL_TO = "NotEqualTo"
    TRACE = "Trace"
    TRUE_VALUE = "TrueValue"
    OBSERVED_VALUE = "ObservedValue"
    OUT_OF_RANGE = "OutOfRange"


class MinimumValueConditionsCoded(Enum):
    OTHER = "Other"
    WHERE_AIR_EQUALS1 = "WhereAirEquals1"
    WHERE_BUTYL_ACETATE_EQUALS1 = "WhereButylAcetateEquals1"
    WHERE_H2_OEQUALS1_OR_WATER_EQUALS1 = "WhereH2OEquals1OrWaterEquals1"
    CORRECTED_TO60_DEGREES_FAHRENHEIT = "CorrectedTo60DegreesFahrenheit"
    WHERE_TOLUENE_EQUALS1 = "WhereTolueneEquals1"
    VAPOR_IN_AIR = "VaporInAir"
    VAPOR_IN_OTHER_THAN_AIR = "VaporInOtherThanAir"
    STANDARD_TEMPERATURE_AND_PRESSURE = "StandardTemperatureAndPressure"
    CONDITIONS_OTHER_THAN_STANDARD_TEMPERATURE_AND_PRESSURE = "ConditionsOtherThanStandardTemperatureAndPressure"
    IN_ETHYL_ALCOHOL = "InEthylAlcohol"
    IN_ETHYL_ETHER = "InEthylEther"
    IN_WATER = "InWater"
    AT1_ATMOSPHERE_PRESSURE = "At1AtmospherePressure"
    WHERE_ETHER_EQUALS1 = "WhereEtherEquals1"
    ACTUAL = "Actual"
    PREDICTED = "Predicted"
    AIR_DRIED_BASIS = "Air-DriedBasis"
    AS_RECEIVED_BASIS = "As-ReceivedBasis"
    DRY_BASIS = "DryBasis"
    EQUILIBRIUM_BASIS = "EquilibriumBasis"
    MOISTURE_AND_ASH_FREE_BASIS = "MoistureAndAsh-FreeBasis"
    OXIDIZING_ATMOSPHERE = "OxidizingAtmosphere"
    REDUCING_ATMOSPHERE = "ReducingAtmosphere"
    CALCULATED = "Calculated"
    SCALED_WEIGHT = "ScaledWeight"
    RATCHET = "Ratchet"
    SATURATED_VAPOR = "SaturatedVapor"
    UNCONDITIONAL = "Unconditional"
    SHORT_TERM = "Short-Term"
    TIME_WEIGHTED = "Time-Weighted"
    CORRECTED = "Corrected"
    UNCORRECTED = "Uncorrected"
    OFF_PEAK = "OffPeak"
    ON_PEAK = "OnPeak"
    INTERMEDIATE = "Intermediate"
    AVERAGE = "Average"
    PER_GALLON = "PerGallon"
    ESTIMATED = "Estimated"
    MINIMUM = "Minimum"
    MIST = "Mist"
    PREDOMINANT = "Predominant"
    TOTAL = "Total"
    COST = "Cost"
    TENANT = "Tenant"
    OWNER = "Owner"
    FOR_SALE = "ForSale"
    REAL_ESTATE_OWNED_OR_CORPORATE_OWNED = "RealEstateOwnedOrCorporateOwned"
    BOARDED_OR_BLOCKED_UP = "BoardedOrBlockedUp"
    PLANNED = "Planned"
    COMPLETED = "Completed"
    SOLD = "Sold"
    RENTED = "Rented"
    CURRENT = "Current"
    CURRENT_LIST = "CurrentList"
    EFFECTIVE = "Effective"
    LIST_WHEN_SOLD = "ListWhenSold"
    SALES = "Sales"
    FINAL_LIST = "FinalList"
    AS_IS = "AsIs"
    AS_REPAIRED_OR_IMPROVED = "AsRepairedOrImproved"
    INSTANTANEOUS = "Instantaneous"
    LOW = "Low"
    LOW_TO_GOOD = "LowToGood"
    LOW_TO_HIGH = "LowToHigh"
    LOW_TO_MEDIUM = "LowToMedium"
    LOW_TO_MODERATE = "LowToModerate"
    MEDIUM = "Medium"
    MEDIUM_TO_GOOD = "MediumToGood"
    MEDIUM_TO_HIGH = "MediumToHigh"
    MODERATE = "Moderate"
    MODERATE_TO_GOOD = "ModerateToGood"
    MODERATE_TO_HIGH = "ModerateToHigh"
    MODERATE_TO_MEDIUM = "ModerateToMedium"
    GOOD = "Good"
    GOOD_TO_HIGH = "GoodToHigh"
    HIGH = "High"
    BUDGETED = "Budgeted"
    FORECAST = "Forecast"
    ADJUSTED = "Adjusted"
    ALLOCATED = "Allocated"
    INCREASING = "Increasing"
    STABLE = "Stable"
    DECLINING = "Declining"
    PREVIOUS = "Previous"
    POTENTIAL = "Potential"
    MODELED = "Modeled"
    MEASURED = "Measured"
    MAXIMUM = "Maximum"
    SUMMER_ON_PEAK = "SummerOn-Peak"
    SUMMER_MID_PEAK = "SummerMid-Peak"
    SUMMER_OFF_PEAK = "SummerOff-Peak"
    SUMMER_SUPER_ON_PEAK = "SummerSuperOn-Peak"
    SUMMER_SUPER_OFF_PEAK = "SummerSuperOff-Peak"
    WINTER_ON_PEAK = "WinterOn-Peak"
    WINTER_MID_PEAK = "WinterMid-Peak"
    WINTER_OFF_PEAK = "WinterOff-Peak"
    WINTER_SUPER_ON_PEAK = "WinterSuperOn-Peak"
    WINTER_SUPER_OFF_PEAK = "WinterSuperOff-Peak"
    SUMMER_DAY = "SummerDay"
    SUMMER_NIGHT = "SummerNight"
    WINTER_DAY = "WinterDay"
    WINTER_NIGHT = "WinterNight"
    SUMMER = "Summer"
    WINTER = "Winter"
    DAY = "Day"
    NIGHT = "Night"
    PEAK_2 = "Peak-2"
    PEAK_3 = "Peak-3"
    PEAK_4 = "Peak-4"
    SHOULDER = "Shoulder"
    NON_TIME_RELATED_DEMAND = "NonTimeRelatedDemand"


class MinimumValueSignificanceCoded(Enum):
    OTHER = "Other"
    APPROXIMATELY = "Approximately"
    EQUAL_TO = "EqualTo"
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"
    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL_TO = "LessThanOrEqualTo"
    NOT_EQUAL_TO = "NotEqualTo"
    TRACE = "Trace"
    TRUE_VALUE = "TrueValue"
    OBSERVED_VALUE = "ObservedValue"
    OUT_OF_RANGE = "OutOfRange"


class NameAddressAddressTypeCoded(Enum):
    OTHER = "Other"
    ACCEPTANCE_LOCATION = "AcceptanceLocation"
    ACCOUNTS_PAYABLE_OFFICE = "AccountsPayableOffice"
    ACKNOWLEDGEMENT_RECIPIENT = "AcknowledgementRecipient"
    ADDITIONAL_ADDRESS = "AdditionalAddress"
    ADDITIONAL_DELIVERY_ADDRESS = "AdditionalDeliveryAddress"
    ADDITIONAL_PICK_UP_ADDRESS = "AdditionalPickUpAddress"
    ALCOHOL_BEVERAGE_DEPARTMENT = "AlcoholBeverageDepartment"
    ALTERNATE_RETURN_ADDRESS = "AlternateReturnAddress"
    ALTERNATIVE_ADDRESSEE = "AlternativeAddressee"
    AUDIT_OFFICE = "AuditOffice"
    BAILMENT_WAREHOUSE = "BailmentWarehouse"
    BID_OPENING_LOCATION = "BidOpeningLocation"
    BILL_AND_SHIP_TO = "BillAndShipTo"
    BILLED_FROM = "BilledFrom"
    BILL_OF_LADING_RECIPIENT = "BillOfLadingRecipient"
    BILL_TO = "BillTo"
    BOOKING_OFFICE = "BookingOffice"
    CANDY_AND_CONFECTIONS_DEPARTMENT = "CandyAndConfectionsDepartment"
    CHANGED_ADDRESS = "ChangedAddress"
    COMPANY_ASSIGNED_WELL = "CompanyAssignedWell"
    COMPANY_OWNED_OIL_FIELD = "Company-OwnedOilField"
    CONSIGNEE_COURIER_TRANSFER_STATION = "ConsigneeCourierTransferStation"
    CONSIGNOR_COURIER_TRANSFER_STATION = "ConsignorCourierTransferStation"
    CONSULTANTS_OFFICE = "ConsultantsOffice"
    CONTACT_OFFICE = "ContactOffice"
    CONTAINER_LOCATION = "ContainerLocation"
    COPY_MESSAGE_TO = "CopyMessageTo"
    CORPORATE_OFFICE = "CorporateOffice"
    CORRECTED_ADDRESS = "CorrectedAddress"
    DELIVERY_ADDRESS = "DeliveryAddress"
    DESTINATION_MAIL_FACILITY = "DestinationMailFacility"
    DIFFERENT_PREMISE_ADDRESS = "DifferentPremiseAddress"
    DISTRIBUTION_RECIPIENT = "DistributionRecipient"
    DOCUMENT_OR_MESSAGE_ISSUER_OR_SENDER = "DocumentOrMessageIssuerOrSender"
    DOCUMENT_RECIPIENT = "DocumentRecipient"
    DOMESTIC_FINANCIAL_INSTITUTION = "DomesticFinancialInstitution"
    DOWNSTREAM_METER_LOCATION = "DownstreamMeterLocation"
    DROP_OFF_LOCATION = "Drop-OffLocation"
    EMERGENCY_DEPARTMENT = "EmergencyDepartment"
    ESTABLISHED_LOCATION = "EstablishedLocation"
    EVENT_LOCATION = "EventLocation"
    FILING_ADDRESS = "FilingAddress"
    FILING_LOCATION = "FilingLocation"
    FILING_OFFICE = "FilingOffice"
    FINAL_MESSAGE_RECIPIENT = "FinalMessageRecipient"
    FINAL_RECIPIENT = "FinalRecipient"
    FINAL_SCHEDULED_DESTINATION = "FinalScheduledDestination"
    FINANCIAL_INSTITUTION = "FinancialInstitution"
    FIRST_CONTACT = "FirstContact"
    FLORAL_DEPARTMENT = "FloralDepartment"
    FOREIGN_DISCLOSURE_INFORMATION_OFFICE = "ForeignDisclosureInformationOffice"
    FOREIGN_OFFICE = "ForeignOffice"
    FOREIGN_REGISTRATION_LOCATION = "ForeignRegistrationLocation"
    FORMER_ADDRESS = "FormerAddress"
    FREEON_BOARD_POINT = "FreeonBoardPoint"
    FROZEN_DEPARTMENT = "FrozenDepartment"
    GARAGED_LOCATION = "GaragedLocation"
    GAS_PLANT = "GasPlant"
    GAS_TRANSACTION_ENDING_POINT = "GasTransactionEndingPoint"
    GAS_TRANSACTION_POINT1 = "GasTransactionPoint1"
    GAS_TRANSACTION_POINT2 = "GasTransactionPoint2"
    GAS_TRANSACTION_STARTING_POINT = "GasTransactionStartingPoint"
    HAZARDOUS_MATERIAL_OFFICE = "HazardousMaterialOffice"
    HEAD_OFFICE = "HeadOffice"
    HOME_OFFICE = "HomeOffice"
    IMPORTED_FROM_LOCATION = "ImportedFromLocation"
    INCORPORATED_LOCATION = "IncorporatedLocation"
    INCORPORATION_STATE_PLACE_OF_BUSINESS = "IncorporationStatePlaceOfBusiness"
    INCORPORATION_STATE_PRINCIPAL_OFFICE = "IncorporationStatePrincipalOffice"
    INQUIRY_ADDRESS = "InquiryAddress"
    INSPECTION_ADDRESS = "InspectionAddress"
    INSPECTION_AND_ACCEPTANCE_LOCATION = "InspectionAndAcceptanceLocation"
    INSPECTION_LOCATION = "InspectionLocation"
    INSTALLED_AT = "InstalledAt"
    IN_STORE_BAKERY_DEPARTMENT = "In-StoreBakeryDepartment"
    INSURED_LOCATION = "InsuredLocation"
    LABORATORY = "Laboratory"
    LAST_BREAK_TERMINAL = "LastBreakTerminal"
    LEASE_LOCATION = "LeaseLocation"
    LISTING_OFFICE = "ListingOffice"
    LOCAL_CHAIN = "LocalChain"
    LOCATION_OF_GOODS = "LocationOfGoods"
    LOCATION_OF_GOODS_FOR_CUSTOMS_EXAMINATION_BEFORE_CLEARANCE = "LocationOfGoodsForCustomsExaminationBeforeClearance"
    LOCATION_OF_LOAD_EXCHANGE = "LocationOfLoadExchange"
    LOCATION_OF_SPOT_FOR_STORAGE = "LocationOfSpotForStorage"
    LOT = "Lot"
    MAIL_ADDRESS = "MailAddress"
    MAIL_TO = "MailTo"
    MANUFACTURING_PLANT = "ManufacturingPlant"
    MASTER_PROPERTY = "MasterProperty"
    MATERIAL_CHANGE_NOTICE_ADDRESS = "MaterialChangeNoticeAddress"
    MATERIAL_DISPOSITION_AUTHORIZATION_LOCATION = "MaterialDispositionAuthorizationLocation"
    MEAT_DEPARTMENT = "MeatDepartment"
    MEETING_LOCATION = "MeetingLocation"
    MESSAGE_FROM = "MessageFrom"
    MESSAGE_RECIPIENT = "MessageRecipient"
    MESSAGE_TO = "MessageTo"
    NEIGHBORHOOD = "Neighborhood"
    NEW_ADDRESS = "NewAddress"
    NEW_SUPPLY_SOURCE = "NewSupplySource"
    NEXT_DESTINATION = "NextDestination"
    NEXT_SCHEDULED_DESTINATION = "NextScheduledDestination"
    NON_TEMPORARY_STORAGE_FACILITY = "Non-TemporaryStorageFacility"
    NOT_APPLICABLE = "NotApplicable"
    OPERATOR_OF_THE_TRANSFER_POINT = "OperatorOfTheTransferPoint"
    ORIGINAL_LOCATION = "OriginalLocation"
    ORIGIN_MAIL_FACILITY = "OriginMailFacility"
    ORIGIN_SUBLOCATION = "OriginSublocation"
    ORIGIN_TERMINAL = "OriginTerminal"
    OTHER_DEPARTMENTS = "OtherDepartments"
    OUTER_CONTINENTAL_SHELF_AREA_LOCATION = "OuterContinentalShelfAreaLocation"
    OUT_OF_STATE_PRINCIPAL_OFFICE = "Out-Of-StatePrincipalOffice"
    OWNING_INVENTORY_CONTROL_POINT = "OwningInventoryControlPoint"
    PART_SOURCE = "PartSource"
    PAYMENT_ADDRESS = "PaymentAddress"
    PERSONNEL_OFFICE = "PersonnelOffice"
    PHARMACY_DEPARTMENT = "PharmacyDepartment"
    PHYSICAL_ADDRESS = "PhysicalAddress"
    PICK_UP_ADDRESS = "PickUpAddress"
    PIPELINE = "Pipeline"
    PIPELINE_SEGMENT = "PipelineSegment"
    PIPELINE_SEGMENT_BOUNDARY = "PipelineSegmentBoundary"
    PLACE_OF_BOTTLING = "PlaceOfBottling"
    PLACE_OF_BUSINESS = "PlaceOfBusiness"
    POSTAL_MAILING_ADDRESS = "PostalMailingAddress"
    PRELIMINARY_INSPECTION_LOCATION = "PreliminaryInspectionLocation"
    PREMISES = "Premises"
    PRESENT_ADDRESS = "PresentAddress"
    PRIMARY_CONTROL_POINT_LOCATION = "PrimaryControlPointLocation"
    PRODUCE_DEPARTMENT = "ProduceDepartment"
    PRODUCT_SERVICES_AND_REPAIRS_CENTRE = "ProductServicesAndRepairsCentre"
    PROJECT_COORDINATION_OFFICE = "ProjectCoordinationOffice"
    PROJECT_MANAGEMENT_OFFICE = "ProjectManagementOffice"
    PROJECT_PROPERTY = "ProjectProperty"
    PROPERTY = "Property"
    QUALITY_CONTROL = "QualityControl"
    RADIO_CONTROL_STATION_LOCATION = "RadioControlStationLocation"
    RAILROAD = "Railroad"
    RECEIPT_METER_LOCATION = "ReceiptMeterLocation"
    RECEIPT_ZONE = "ReceiptZone"
    RECEIVED_FROM = "ReceivedFrom"
    RECEIVER_SITE = "ReceiverSite"
    RECEIVING_LOCATION = "ReceivingLocation"
    RECEIVING_POINT_FOR_CUSTOMER_SAMPLES = "ReceivingPointForCustomerSamples"
    RECEIVING_SUB_LOCATION = "ReceivingSub-Location"
    RECLAMATION_CENTER = "ReclamationCenter"
    RECORD_KEEPING_ADDRESS = "Record-KeepingAddress"
    REFINERY = "Refinery"
    REGIONAL_OFFICE = "RegionalOffice"
    REGISTERED_OFFICE = "RegisteredOffice"
    RELEASE_TO = "ReleaseTo"
    REMIT_TO = "RemitTo"
    REPAIRING_OUTLET = "RepairingOutlet"
    REPAIR_OR_REFURBISH_LOCATION = "RepairOrRefurbishLocation"
    REPORTING_LOCATION = "ReportingLocation"
    RESEARCH_INSTITUTE = "ResearchInstitute"
    RESIDENCE_OR_DOMICILE = "ResidenceOrDomicile"
    RETURNED_TO = "ReturnedTo"
    ROUTING_POINT = "RoutingPoint"
    SALES_OFFICE = "SalesOffice"
    SAMPLES_TO_BE_RETURNED_TO = "SamplesToBeReturnedTo"
    SAMPLING_LOCATION = "SamplingLocation"
    SECONDARY_LOCATION_ADDRESS = "SecondaryLocationAddress"
    SECOND_HOME = "SecondHome"
    SELLING_OFFICE = "SellingOffice"
    SERVICE_BUREAU = "ServiceBureau"
    SERVICE_LOCATION = "ServiceLocation"
    SHELTERED_WORKSHOP = "ShelteredWorkshop"
    SHIP_FROM = "ShipFrom"
    SHIP_TO = "ShipTo"
    SMALL_BASE_STATION_LOCATION = "SmallBaseStationLocation"
    SMALL_CONTROL_STATION_LOCATION = "SmallControlStationLocation"
    SOLD_TO_AND_SHIP_TO = "SoldToAndShipTo"
    SOLD_TO_IF_DIFFERENT_FROM_BILL_TO = "SoldToIfDifferentFromBillTo"
    STORAGE_AREA = "StorageArea"
    STORAGE_FACILITYAT_DESTINATION = "StorageFacilityatDestination"
    STORAGE_FACILITY_AT_ORIGIN = "StorageFacilityAtOrigin"
    STORE = "Store"
    SOLD_TO = "SoldTo"
    SUBCONTRACT_OR_COGNIZANT_SECURITY_OFFICE = "SubcontractOrCognizantSecurityOffice"
    SUBJECT_PROPERTY = "SubjectProperty"
    SUB_OFFICE = "Sub-Office"
    SUBSIDIARY = "Subsidiary"
    SUBSIDIARY_DIVISION = "SubsidiaryDivision"
    SUPPLIER_OR_MANUFACTURER = "SupplierOrManufacturer"
    SUPPLIERS_CORPORATE_OFFICE = "SuppliersCorporateOffice"
    SUPPLY_SOURCE = "SupplySource"
    TANK_FARM = "TankFarm"
    TAX_ADDRESS = "TaxAddress"
    TAX_COLLECTORS_OFFICE = "TaxCollectorsOffice"
    TECHNICAL_OFFICE = "TechnicalOffice"
    TERMINAL = "Terminal"
    TERMINAL_LOCATION = "TerminalLocation"
    TESTING_LABORATORY = "TestingLaboratory"
    TOOL_SOURCE = "ToolSource"
    TRANSFER_POINT = "TransferPoint"
    TRANSFER_TO = "TransferTo"
    TRANSPORTATION_OFFICE = "TransportationOffice"
    ULTIMATE_CONSIGNEE = "UltimateConsignee"
    ULTIMATE_CUSTOMER = "UltimateCustomer"
    ULTIMATE_PARENT_COMPANY = "UltimateParentCompany"
    UNIT_PROPERTY = "UnitProperty"
    UPSTREAM_METER_LOCATION = "UpstreamMeterLocation"
    VACATION_HOME = "VacationHome"
    VENDOR = "Vendor"
    VIDEO_DEPARTMENT = "VideoDepartment"
    WAREHOUSE = "Warehouse"
    WHOLESALER = "Wholesaler"


@dataclass
class NameValuePair:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        }
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "name": "Datatype",
            "type": "Element",
        }
    )


@dataclass
class Pobox:
    class Meta:
        name = "POBox"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    pobox_postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "POBoxPostalCode",
            "type": "Attribute",
        }
    )


@dataclass
class PartNum:
    part_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartID",
            "type": "Element",
            "required": True,
        }
    )
    part_idext: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartIDExt",
            "type": "Element",
        }
    )
    revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RevisionNumber",
            "type": "Element",
        }
    )


@dataclass
class PriceMultiplier:
    price_multiplier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PriceMultiplierCoded",
            "type": "Element",
            "required": True,
        }
    )
    price_multiplier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PriceMultiplierCodedOther",
            "type": "Element",
        }
    )
    multiplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Multiplier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PricingType:
    price_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PriceTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    price_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PriceTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ProductIdentifierCoded:
    product_identifier_qualifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductIdentifierQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    product_identifier_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductIdentifierQualifierCodedOther",
            "type": "Element",
        }
    )
    product_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    product_identifier_ext: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductIdentifierExt",
            "type": "Element",
        }
    )


@dataclass
class Purpose:
    purpose_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurposeCodedOther",
            "type": "Element",
        }
    )


class QuantityValueConditionsCoded(Enum):
    OTHER = "Other"
    WHERE_AIR_EQUALS1 = "WhereAirEquals1"
    WHERE_BUTYL_ACETATE_EQUALS1 = "WhereButylAcetateEquals1"
    WHERE_H2_OEQUALS1_OR_WATER_EQUALS1 = "WhereH2OEquals1OrWaterEquals1"
    CORRECTED_TO60_DEGREES_FAHRENHEIT = "CorrectedTo60DegreesFahrenheit"
    WHERE_TOLUENE_EQUALS1 = "WhereTolueneEquals1"
    VAPOR_IN_AIR = "VaporInAir"
    VAPOR_IN_OTHER_THAN_AIR = "VaporInOtherThanAir"
    STANDARD_TEMPERATURE_AND_PRESSURE = "StandardTemperatureAndPressure"
    CONDITIONS_OTHER_THAN_STANDARD_TEMPERATURE_AND_PRESSURE = "ConditionsOtherThanStandardTemperatureAndPressure"
    IN_ETHYL_ALCOHOL = "InEthylAlcohol"
    IN_ETHYL_ETHER = "InEthylEther"
    IN_WATER = "InWater"
    AT1_ATMOSPHERE_PRESSURE = "At1AtmospherePressure"
    WHERE_ETHER_EQUALS1 = "WhereEtherEquals1"
    ACTUAL = "Actual"
    PREDICTED = "Predicted"
    AIR_DRIED_BASIS = "Air-DriedBasis"
    AS_RECEIVED_BASIS = "As-ReceivedBasis"
    DRY_BASIS = "DryBasis"
    EQUILIBRIUM_BASIS = "EquilibriumBasis"
    MOISTURE_AND_ASH_FREE_BASIS = "MoistureAndAsh-FreeBasis"
    OXIDIZING_ATMOSPHERE = "OxidizingAtmosphere"
    REDUCING_ATMOSPHERE = "ReducingAtmosphere"
    CALCULATED = "Calculated"
    SCALED_WEIGHT = "ScaledWeight"
    RATCHET = "Ratchet"
    SATURATED_VAPOR = "SaturatedVapor"
    UNCONDITIONAL = "Unconditional"
    SHORT_TERM = "Short-Term"
    TIME_WEIGHTED = "Time-Weighted"
    CORRECTED = "Corrected"
    UNCORRECTED = "Uncorrected"
    OFF_PEAK = "OffPeak"
    ON_PEAK = "OnPeak"
    INTERMEDIATE = "Intermediate"
    AVERAGE = "Average"
    PER_GALLON = "PerGallon"
    ESTIMATED = "Estimated"
    MINIMUM = "Minimum"
    MIST = "Mist"
    PREDOMINANT = "Predominant"
    TOTAL = "Total"
    COST = "Cost"
    TENANT = "Tenant"
    OWNER = "Owner"
    FOR_SALE = "ForSale"
    REAL_ESTATE_OWNED_OR_CORPORATE_OWNED = "RealEstateOwnedOrCorporateOwned"
    BOARDED_OR_BLOCKED_UP = "BoardedOrBlockedUp"
    PLANNED = "Planned"
    COMPLETED = "Completed"
    SOLD = "Sold"
    RENTED = "Rented"
    CURRENT = "Current"
    CURRENT_LIST = "CurrentList"
    EFFECTIVE = "Effective"
    LIST_WHEN_SOLD = "ListWhenSold"
    SALES = "Sales"
    FINAL_LIST = "FinalList"
    AS_IS = "AsIs"
    AS_REPAIRED_OR_IMPROVED = "AsRepairedOrImproved"
    INSTANTANEOUS = "Instantaneous"
    LOW = "Low"
    LOW_TO_GOOD = "LowToGood"
    LOW_TO_HIGH = "LowToHigh"
    LOW_TO_MEDIUM = "LowToMedium"
    LOW_TO_MODERATE = "LowToModerate"
    MEDIUM = "Medium"
    MEDIUM_TO_GOOD = "MediumToGood"
    MEDIUM_TO_HIGH = "MediumToHigh"
    MODERATE = "Moderate"
    MODERATE_TO_GOOD = "ModerateToGood"
    MODERATE_TO_HIGH = "ModerateToHigh"
    MODERATE_TO_MEDIUM = "ModerateToMedium"
    GOOD = "Good"
    GOOD_TO_HIGH = "GoodToHigh"
    HIGH = "High"
    BUDGETED = "Budgeted"
    FORECAST = "Forecast"
    ADJUSTED = "Adjusted"
    ALLOCATED = "Allocated"
    INCREASING = "Increasing"
    STABLE = "Stable"
    DECLINING = "Declining"
    PREVIOUS = "Previous"
    POTENTIAL = "Potential"
    MODELED = "Modeled"
    MEASURED = "Measured"
    MAXIMUM = "Maximum"
    SUMMER_ON_PEAK = "SummerOn-Peak"
    SUMMER_MID_PEAK = "SummerMid-Peak"
    SUMMER_OFF_PEAK = "SummerOff-Peak"
    SUMMER_SUPER_ON_PEAK = "SummerSuperOn-Peak"
    SUMMER_SUPER_OFF_PEAK = "SummerSuperOff-Peak"
    WINTER_ON_PEAK = "WinterOn-Peak"
    WINTER_MID_PEAK = "WinterMid-Peak"
    WINTER_OFF_PEAK = "WinterOff-Peak"
    WINTER_SUPER_ON_PEAK = "WinterSuperOn-Peak"
    WINTER_SUPER_OFF_PEAK = "WinterSuperOff-Peak"
    SUMMER_DAY = "SummerDay"
    SUMMER_NIGHT = "SummerNight"
    WINTER_DAY = "WinterDay"
    WINTER_NIGHT = "WinterNight"
    SUMMER = "Summer"
    WINTER = "Winter"
    DAY = "Day"
    NIGHT = "Night"
    PEAK_2 = "Peak-2"
    PEAK_3 = "Peak-3"
    PEAK_4 = "Peak-4"
    SHOULDER = "Shoulder"
    NON_TIME_RELATED_DEMAND = "NonTimeRelatedDemand"


class QuantityValueSignificanceCoded(Enum):
    OTHER = "Other"
    APPROXIMATELY = "Approximately"
    EQUAL_TO = "EqualTo"
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"
    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL_TO = "LessThanOrEqualTo"
    NOT_EQUAL_TO = "NotEqualTo"
    TRACE = "Trace"
    TRUE_VALUE = "TrueValue"
    OBSERVED_VALUE = "ObservedValue"
    OUT_OF_RANGE = "OutOfRange"


@dataclass
class Reference:
    ref_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNum",
            "type": "Element",
            "required": True,
        }
    )
    ref_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefDate",
            "type": "Element",
        }
    )


@dataclass
class Region:
    region_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegionCoded",
            "type": "Element",
            "required": True,
        }
    )
    region_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegionCodedOther",
            "type": "Element",
        }
    )


@dataclass
class Rule:
    rule_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleName",
            "type": "Element",
            "required": True,
        }
    )
    rule_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleDescription",
            "type": "Element",
        }
    )
    rule_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleValue",
            "type": "Element",
            "required": True,
        }
    )
    rule_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleFormula",
            "type": "Element",
        }
    )


@dataclass
class SealIssuer:
    seal_issuer_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SealIssuerCoded",
            "type": "Element",
            "required": True,
        }
    )
    seal_issuer_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SealIssuerCodedOther",
            "type": "Element",
        }
    )


@dataclass
class SealStatusDescription:
    seal_status_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SealStatusCoded",
            "type": "Element",
        }
    )
    seal_status_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SealStatusCodedOther",
            "type": "Element",
        }
    )
    seal_status_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "SealStatusInfo",
            "type": "Element",
        }
    )


@dataclass
class StatusReason:
    status_reason_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusReasonCoded",
            "type": "Element",
            "required": True,
        }
    )
    status_reason_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusReasonCodedOther",
            "type": "Element",
        }
    )


@dataclass
class Timezone:
    timezone_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimezoneCoded",
            "type": "Element",
            "required": True,
        }
    )
    timezone_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimezoneCodedOther",
            "type": "Element",
        }
    )


@dataclass
class TransitDirection:
    transit_direction_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransitDirectionCoded",
            "type": "Element",
            "required": True,
        }
    )
    transit_direction_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransitDirectionCodedOther",
            "type": "Element",
        }
    )
    transit_time_qualifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransitTimeQualifierCoded",
            "type": "Element",
        }
    )
    transit_time_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransitTimeQualifierCodedOther",
            "type": "Element",
        }
    )
    transit_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransitTime",
            "type": "Element",
        }
    )


@dataclass
class TransportMeans:
    transport_means_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportMeansCoded",
            "type": "Element",
            "required": True,
        }
    )
    transport_means_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportMeansCodedOther",
            "type": "Element",
        }
    )


@dataclass
class TransportMode:
    transport_mode_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportModeCoded",
            "type": "Element",
            "required": True,
        }
    )
    transport_mode_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportModeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class UnitOfMeasurement:
    uomcoded: Optional[str] = field(
        default=None,
        metadata={
            "name": "UOMCoded",
            "type": "Element",
            "required": True,
        }
    )
    uomcoded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "UOMCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ValidityDates:
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "required": True,
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class VisibilityRules:
    visibility_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "VisibilityIndicator",
            "type": "Element",
        }
    )
    visibility_of_comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "VisibilityOfComments",
            "type": "Element",
        }
    )
    visibility_of_amounts: Optional[str] = field(
        default=None,
        metadata={
            "name": "VisibilityOfAmounts",
            "type": "Element",
        }
    )
    visibility_of_quantities: Optional[str] = field(
        default=None,
        metadata={
            "name": "VisibilityOfQuantities",
            "type": "Element",
        }
    )
    visibility_of_participants: Optional[str] = field(
        default=None,
        metadata={
            "name": "VisibilityOfParticipants",
            "type": "Element",
        }
    )


@dataclass
class Attachment:
    attachment_action_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachmentActionCoded",
            "type": "Element",
        }
    )
    attachment_action_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachmentActionCodedOther",
            "type": "Element",
        }
    )
    attachment_purpose: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachmentPurpose",
            "type": "Element",
            "required": True,
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Element",
        }
    )
    attachment_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachmentTitle",
            "type": "Element",
        }
    )
    attachment_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachmentDescription",
            "type": "Element",
        }
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
        }
    )
    mimetype: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIMEType",
            "type": "Element",
        }
    )
    replacement_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReplacementFile",
            "type": "Element",
        }
    )
    attachment_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachmentLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionCreatePurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionValidityDates:
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class BaseCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class BidCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class BuyerPartNumber:
    part_num: Optional[PartNum] = field(
        default=None,
        metadata={
            "name": "PartNum",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CorrespondenceLanguage:
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class DateCoded:
    date: Optional[str] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "required": True,
        }
    )
    date_qualifier: Optional[DateQualifier] = field(
        default=None,
        metadata={
            "name": "DateQualifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Identifier:
    agency: Optional[Agency] = field(
        default=None,
        metadata={
            "name": "Agency",
            "type": "Element",
            "required": True,
        }
    )
    ident: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ident",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class KeyVal:
    key_val_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyValString",
            "type": "Element",
            "required": True,
        }
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    keyword: Optional[str] = field(
        default=None,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfAuctionCategory:
    auction_category: List[AuctionCategory] = field(
        default_factory=list,
        metadata={
            "name": "AuctionCategory",
            "type": "Element",
        }
    )


@dataclass
class ListOfAuctionItemComponents:
    auction_item_component: List[AuctionItemComponent] = field(
        default_factory=list,
        metadata={
            "name": "AuctionItemComponent",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfContactNumber:
    contact_number: List[ContactNumber] = field(
        default_factory=list,
        metadata={
            "name": "ContactNumber",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfProductIdentifierCoded:
    product_identifier_coded: List[ProductIdentifierCoded] = field(
        default_factory=list,
        metadata={
            "name": "ProductIdentifierCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfReference:
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfRules:
    rule: List[Rule] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfStatusReason:
    status_reason: List[StatusReason] = field(
        default_factory=list,
        metadata={
            "name": "StatusReason",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfValues:
    name_value_pair: List[NameValuePair] = field(
        default_factory=list,
        metadata={
            "name": "NameValuePair",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class MaximumValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    significance_coded: Optional[MaximumValueSignificanceCoded] = field(
        default=None,
        metadata={
            "name": "SignificanceCoded",
            "type": "Attribute",
        }
    )
    conditions_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConditionsCodedOther",
            "type": "Attribute",
        }
    )
    conditions_coded: Optional[MaximumValueConditionsCoded] = field(
        default=None,
        metadata={
            "name": "ConditionsCoded",
            "type": "Attribute",
        }
    )
    significance_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignificanceCodedOther",
            "type": "Attribute",
        }
    )


@dataclass
class MeasurementValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    significance_coded: Optional[MeasurementValueSignificanceCoded] = field(
        default=None,
        metadata={
            "name": "SignificanceCoded",
            "type": "Attribute",
        }
    )
    conditions_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConditionsCodedOther",
            "type": "Attribute",
        }
    )
    conditions_coded: Optional[MeasurementValueConditionsCoded] = field(
        default=None,
        metadata={
            "name": "ConditionsCoded",
            "type": "Attribute",
        }
    )
    significance_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignificanceCodedOther",
            "type": "Attribute",
        }
    )


@dataclass
class MinimumValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    significance_coded: Optional[MinimumValueSignificanceCoded] = field(
        default=None,
        metadata={
            "name": "SignificanceCoded",
            "type": "Attribute",
        }
    )
    conditions_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConditionsCodedOther",
            "type": "Attribute",
        }
    )
    conditions_coded: Optional[MinimumValueConditionsCoded] = field(
        default=None,
        metadata={
            "name": "ConditionsCoded",
            "type": "Attribute",
        }
    )
    significance_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignificanceCodedOther",
            "type": "Attribute",
        }
    )


@dataclass
class PrimaryReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuantityValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    significance_coded: Optional[QuantityValueSignificanceCoded] = field(
        default=None,
        metadata={
            "name": "SignificanceCoded",
            "type": "Attribute",
        }
    )
    conditions_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConditionsCodedOther",
            "type": "Attribute",
        }
    )
    conditions_coded: Optional[QuantityValueConditionsCoded] = field(
        default=None,
        metadata={
            "name": "ConditionsCoded",
            "type": "Attribute",
        }
    )
    significance_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignificanceCodedOther",
            "type": "Attribute",
        }
    )


@dataclass
class ReferenceCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SealInfo:
    seal_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SealNumber",
            "type": "Element",
            "required": True,
        }
    )
    seal_issuer: Optional[SealIssuer] = field(
        default=None,
        metadata={
            "name": "SealIssuer",
            "type": "Element",
        }
    )
    seal_status_description: Optional[SealStatusDescription] = field(
        default=None,
        metadata={
            "name": "SealStatusDescription",
            "type": "Element",
        }
    )


@dataclass
class SellerPartNumber:
    part_num: Optional[PartNum] = field(
        default=None,
        metadata={
            "name": "PartNum",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class StandardPartNumber:
    product_identifier_coded: Optional[ProductIdentifierCoded] = field(
        default=None,
        metadata={
            "name": "ProductIdentifierCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SupportingReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SupportingSubReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TargetCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class UnitPrice:
    unit_price_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitPriceValue",
            "type": "Element",
            "required": True,
        }
    )
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
        }
    )
    unit_of_measurement: Optional[UnitOfMeasurement] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
        }
    )


@dataclass
class AuctionItemAttribute:
    auction_attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionAttributeName",
            "type": "Element",
            "required": True,
        }
    )
    auction_attribute_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionAttributeDescription",
            "type": "Element",
        }
    )
    auction_attribute_data_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionAttributeDataTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    auction_attribute_data_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionAttributeDataTypeCodedOther",
            "type": "Element",
        }
    )
    list_of_values: Optional[ListOfValues] = field(
        default=None,
        metadata={
            "name": "ListOfValues",
            "type": "Element",
        }
    )
    auction_attribute_field_size: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionAttributeFieldSize",
            "type": "Element",
        }
    )
    required_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequiredIndicator",
            "type": "Element",
            "required": True,
        }
    )
    auction_attribute_default_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionAttributeDefaultValue",
            "type": "Element",
        }
    )


@dataclass
class CarrierId:
    class Meta:
        name = "CarrierID"

    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ContactId:
    class Meta:
        name = "ContactID"

    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfAttachment:
    attachment: List[Attachment] = field(
        default_factory=list,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfDateCoded:
    date_coded: List[DateCoded] = field(
        default_factory=list,
        metadata={
            "name": "DateCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfIdentifier:
    identifier: List[Identifier] = field(
        default_factory=list,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfKeyVal:
    key_val: List[KeyVal] = field(
        default_factory=list,
        metadata={
            "name": "KeyVal",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfRateOfExchangeReference:
    list_of_reference: Optional[ListOfReference] = field(
        default=None,
        metadata={
            "name": "ListOfReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfSealInfo:
    seal_info: List[SealInfo] = field(
        default_factory=list,
        metadata={
            "name": "SealInfo",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class LocId:
    class Meta:
        name = "LocID"

    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ManufacturerId:
    class Meta:
        name = "ManufacturerID"

    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class MeasurementRange:
    minimum_value: Optional[MinimumValue] = field(
        default=None,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "required": True,
        }
    )
    maximum_value: Optional[MaximumValue] = field(
        default=None,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class NameAddress:
    address_type_coded: NameAddressAddressTypeCoded = field(
        default=NameAddressAddressTypeCoded.NOT_APPLICABLE,
        metadata={
            "name": "AddressTypeCoded",
            "type": "Attribute",
            "required": True,
        }
    )
    address_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddressTypeCodedOther",
            "type": "Attribute",
        }
    )
    external_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalAddressID",
            "type": "Element",
        }
    )
    name1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name1",
            "type": "Element",
            "required": True,
        }
    )
    name2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name2",
            "type": "Element",
        }
    )
    name3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name3",
            "type": "Element",
        }
    )
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
        }
    )
    pobox: Optional[Pobox] = field(
        default=None,
        metadata={
            "name": "POBox",
            "type": "Element",
        }
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
        }
    )
    house_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "HouseNumber",
            "type": "Element",
        }
    )
    street_supplement1: Optional[str] = field(
        default=None,
        metadata={
            "name": "StreetSupplement1",
            "type": "Element",
        }
    )
    street_supplement2: Optional[str] = field(
        default=None,
        metadata={
            "name": "StreetSupplement2",
            "type": "Element",
        }
    )
    building: Optional[str] = field(
        default=None,
        metadata={
            "name": "Building",
            "type": "Element",
        }
    )
    floor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Floor",
            "type": "Element",
        }
    )
    room_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoomNumber",
            "type": "Element",
        }
    )
    inhouse_mail: Optional[str] = field(
        default=None,
        metadata={
            "name": "InhouseMail",
            "type": "Element",
        }
    )
    department: Optional[str] = field(
        default=None,
        metadata={
            "name": "Department",
            "type": "Element",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
        }
    )
    county: Optional[str] = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
        }
    )
    region: Optional[Region] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
        }
    )
    district: Optional[str] = field(
        default=None,
        metadata={
            "name": "District",
            "type": "Element",
        }
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
        }
    )
    timezone: Optional[Timezone] = field(
        default=None,
        metadata={
            "name": "Timezone",
            "type": "Element",
        }
    )


@dataclass
class NatureOfGoods:
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OtherItemIdentifiers:
    list_of_product_identifier_coded: Optional[ListOfProductIdentifierCoded] = field(
        default=None,
        metadata={
            "name": "ListOfProductIdentifierCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PartyId:
    class Meta:
        name = "PartyID"

    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuantityRange:
    minimum_value: Optional[MinimumValue] = field(
        default=None,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "required": True,
        }
    )
    maximum_value: Optional[MaximumValue] = field(
        default=None,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Range:
    minimum_value: Optional[MinimumValue] = field(
        default=None,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "required": True,
        }
    )
    maximum_value: Optional[MaximumValue] = field(
        default=None,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ReferenceCoded:
    reference_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    reference_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceTypeCodedOther",
            "type": "Element",
        }
    )
    primary_reference: Optional[PrimaryReference] = field(
        default=None,
        metadata={
            "name": "PrimaryReference",
            "type": "Element",
            "required": True,
        }
    )
    supporting_reference: Optional[SupportingReference] = field(
        default=None,
        metadata={
            "name": "SupportingReference",
            "type": "Element",
        }
    )
    supporting_sub_reference: Optional[SupportingSubReference] = field(
        default=None,
        metadata={
            "name": "SupportingSubReference",
            "type": "Element",
        }
    )
    reference_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceDescription",
            "type": "Element",
        }
    )


@dataclass
class RulesProfile:
    bid_rule_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "BidRuleCoded",
            "type": "Element",
            "required": True,
        }
    )
    bid_rule_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "BidRuleCodedOther",
            "type": "Element",
        }
    )
    mvbtemplate: Optional[str] = field(
        default=None,
        metadata={
            "name": "MVBTemplate",
            "type": "Element",
        }
    )
    win_rule_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "WinRuleCoded",
            "type": "Element",
            "required": True,
        }
    )
    win_rule_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "WinRuleCodedOther",
            "type": "Element",
        }
    )
    visibility_rules: Optional[VisibilityRules] = field(
        default=None,
        metadata={
            "name": "VisibilityRules",
            "type": "Element",
        }
    )
    list_of_rules: Optional[ListOfRules] = field(
        default=None,
        metadata={
            "name": "ListOfRules",
            "type": "Element",
        }
    )


@dataclass
class ShipmentStatusReasons:
    list_of_status_reason: Optional[ListOfStatusReason] = field(
        default=None,
        metadata={
            "name": "ListOfStatusReason",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SubstitutePartNumbers:
    list_of_product_identifier_coded: Optional[ListOfProductIdentifierCoded] = field(
        default=None,
        metadata={
            "name": "ListOfProductIdentifierCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionCreatListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CargoTypeification:
    class Meta:
        name = "CargoClassification"

    nature_of_goods: Optional[NatureOfGoods] = field(
        default=None,
        metadata={
            "name": "NatureOfGoods",
            "type": "Element",
        }
    )
    operational_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationalTypeCoded",
            "type": "Element",
        }
    )
    operational_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationalTypeCodedOther",
            "type": "Element",
        }
    )
    type_of_cargo: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfCargo",
            "type": "Element",
        }
    )


@dataclass
class Contact:
    contact_id: Optional[ContactId] = field(
        default=None,
        metadata={
            "name": "ContactID",
            "type": "Element",
        }
    )
    contact_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactName",
            "type": "Element",
            "required": True,
        }
    )
    contact_function: Optional[ContactFunction] = field(
        default=None,
        metadata={
            "name": "ContactFunction",
            "type": "Element",
        }
    )
    contact_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactDescription",
            "type": "Element",
        }
    )
    list_of_contact_number: Optional[ListOfContactNumber] = field(
        default=None,
        metadata={
            "name": "ListOfContactNumber",
            "type": "Element",
        }
    )


@dataclass
class ListOfAuctionItemAttribute:
    auction_item_attribute: List[AuctionItemAttribute] = field(
        default_factory=list,
        metadata={
            "name": "AuctionItemAttribute",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfOtherDeliveryDate:
    list_of_date_coded: Optional[ListOfDateCoded] = field(
        default=None,
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfReferenceCoded:
    reference_coded: List[ReferenceCoded] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class LocationIdentifier:
    loc_id: Optional[LocId] = field(
        default=None,
        metadata={
            "name": "LocID",
            "type": "Element",
            "required": True,
        }
    )
    location_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationDescription",
            "type": "Element",
        }
    )


@dataclass
class Mvbrange:
    class Meta:
        name = "MVBRange"

    range: Optional[Range] = field(
        default=None,
        metadata={
            "name": "Range",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ManufacturerPartNumber:
    part_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartID",
            "type": "Element",
            "required": True,
        }
    )
    part_idext: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartIDExt",
            "type": "Element",
        }
    )
    revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RevisionNumber",
            "type": "Element",
        }
    )
    manufacturer_id: Optional[ManufacturerId] = field(
        default=None,
        metadata={
            "name": "ManufacturerID",
            "type": "Element",
        }
    )
    manufacturer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ManufacturerName",
            "type": "Element",
        }
    )


@dataclass
class Measurement:
    measurement_value: Optional[MeasurementValue] = field(
        default=None,
        metadata={
            "name": "MeasurementValue",
            "type": "Element",
            "required": True,
        }
    )
    measurement_range: Optional[MeasurementRange] = field(
        default=None,
        metadata={
            "name": "MeasurementRange",
            "type": "Element",
            "required": True,
        }
    )
    unit_of_measurement: Optional[UnitOfMeasurement] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderDates:
    requested_ship_by_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestedShipByDate",
            "type": "Element",
        }
    )
    requested_deliver_by_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestedDeliverByDate",
            "type": "Element",
        }
    )
    promise_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PromiseDate",
            "type": "Element",
        }
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )
    cancel_by_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CancelByDate",
            "type": "Element",
        }
    )
    list_of_date_coded: Optional[ListOfDateCoded] = field(
        default=None,
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
        }
    )


@dataclass
class Quantity:
    quantity_value: Optional[QuantityValue] = field(
        default=None,
        metadata={
            "name": "QuantityValue",
            "type": "Element",
            "required": True,
        }
    )
    quantity_range: Optional[QuantityRange] = field(
        default=None,
        metadata={
            "name": "QuantityRange",
            "type": "Element",
            "required": True,
        }
    )
    unit_of_measurement: Optional[UnitOfMeasurement] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RateOfExchangeDetail:
    reference_currency: Optional[ReferenceCurrency] = field(
        default=None,
        metadata={
            "name": "ReferenceCurrency",
            "type": "Element",
            "required": True,
        }
    )
    target_currency: Optional[TargetCurrency] = field(
        default=None,
        metadata={
            "name": "TargetCurrency",
            "type": "Element",
            "required": True,
        }
    )
    rate_of_exchange: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateOfExchange",
            "type": "Element",
            "required": True,
        }
    )
    inverse_rate_of_exchange: Optional[str] = field(
        default=None,
        metadata={
            "name": "InverseRateOfExchange",
            "type": "Element",
        }
    )
    date_of_rate_of_exchange: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateOfRateOfExchange",
            "type": "Element",
        }
    )
    list_of_rate_of_exchange_reference: Optional[ListOfRateOfExchangeReference] = field(
        default=None,
        metadata={
            "name": "ListOfRateOfExchangeReference",
            "type": "Element",
        }
    )


@dataclass
class AuctionItemDates:
    order_dates: Optional[OrderDates] = field(
        default=None,
        metadata={
            "name": "OrderDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionQuantity:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CalculatedPriceBasisQuantity:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Dimension:
    measurement: Optional[Measurement] = field(
        default=None,
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )
    dimension_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DimensionCoded",
            "type": "Element",
            "required": True,
        }
    )
    dimension_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DimensionCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ListOfContact:
    contact: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Location:
    location_qualifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationQualifierCoded",
            "type": "Element",
        }
    )
    location_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationQualifierCodedOther",
            "type": "Element",
        }
    )
    location_identifier: Optional[LocationIdentifier] = field(
        default=None,
        metadata={
            "name": "LocationIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    external_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalAddressID",
            "type": "Element",
            "required": True,
        }
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
            "required": True,
        }
    )
    gpscooridinates: Optional[Gpscooridinates] = field(
        default=None,
        metadata={
            "name": "GPSCooridinates",
            "type": "Element",
        }
    )


@dataclass
class Mvbvariable:
    class Meta:
        name = "MVBVariable"

    mvbvariable_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MVBVariableName",
            "type": "Element",
            "required": True,
        }
    )
    mvbvariable_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "MVBVariableValue",
            "type": "Element",
            "required": True,
        }
    )
    mvbrange: Optional[Mvbrange] = field(
        default=None,
        metadata={
            "name": "MVBRange",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderContact:
    contact: Optional[Contact] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PackageReference:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
        }
    )
    package_idreference: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageIDReference",
            "type": "Element",
            "required": True,
        }
    )
    package_reference: Optional["PackageReference"] = field(
        default=None,
        metadata={
            "name": "PackageReference",
            "type": "Element",
        }
    )


@dataclass
class PartNumbers:
    seller_part_number: Optional[SellerPartNumber] = field(
        default=None,
        metadata={
            "name": "SellerPartNumber",
            "type": "Element",
        }
    )
    buyer_part_number: Optional[BuyerPartNumber] = field(
        default=None,
        metadata={
            "name": "BuyerPartNumber",
            "type": "Element",
        }
    )
    manufacturer_part_number: Optional[ManufacturerPartNumber] = field(
        default=None,
        metadata={
            "name": "ManufacturerPartNumber",
            "type": "Element",
        }
    )
    standard_part_number: Optional[StandardPartNumber] = field(
        default=None,
        metadata={
            "name": "StandardPartNumber",
            "type": "Element",
        }
    )
    substitute_part_numbers: Optional[SubstitutePartNumbers] = field(
        default=None,
        metadata={
            "name": "SubstitutePartNumbers",
            "type": "Element",
        }
    )
    other_item_identifiers: Optional[OtherItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "OtherItemIdentifiers",
            "type": "Element",
        }
    )


@dataclass
class PriceBasisQuantity:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PriceQuantityRange:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ReceivingContact:
    contact: Optional[Contact] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ShipToSubQuantity:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ShippingContact:
    contact: Optional[Contact] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ValidBidCurrency:
    bid_currency: Optional[BidCurrency] = field(
        default=None,
        metadata={
            "name": "BidCurrency",
            "type": "Element",
            "required": True,
        }
    )
    rate_of_exchange_detail: Optional[RateOfExchangeDetail] = field(
        default=None,
        metadata={
            "name": "RateOfExchangeDetail",
            "type": "Element",
        }
    )


@dataclass
class AuctionItem:
    auction_item_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionItemID",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionItemName",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionItemDescription",
            "type": "Element",
        }
    )
    list_of_auction_category: Optional[ListOfAuctionCategory] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionCategory",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_item_attribute: Optional[ListOfAuctionItemAttribute] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionItemAttribute",
            "type": "Element",
        }
    )
    auction_item_hierarchy_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionItemHierarchyLevel",
            "type": "Element",
            "required": True,
        }
    )
    auction_line_item_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionLineItemNum",
            "type": "Element",
        }
    )
    auction_quantity: Optional[AuctionQuantity] = field(
        default=None,
        metadata={
            "name": "AuctionQuantity",
            "type": "Element",
            "required": True,
        }
    )
    partial_bid_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialBidIndicator",
            "type": "Element",
        }
    )
    part_numbers: Optional[PartNumbers] = field(
        default=None,
        metadata={
            "name": "PartNumbers",
            "type": "Element",
        }
    )


@dataclass
class ItemPackagingReference:
    package_reference: List[PackageReference] = field(
        default_factory=list,
        metadata={
            "name": "PackageReference",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfDimension:
    dimension: List[Dimension] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfMvbvariables:
    class Meta:
        name = "ListOfMVBVariables"

    mvbvariable: List[Mvbvariable] = field(
        default_factory=list,
        metadata={
            "name": "MVBVariable",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfValidBidCurrency:
    valid_bid_currency: List[ValidBidCurrency] = field(
        default_factory=list,
        metadata={
            "name": "ValidBidCurrency",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OtherContacts:
    list_of_contact: Optional[ListOfContact] = field(
        default=None,
        metadata={
            "name": "ListOfContact",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Price:
    pricing_type: Optional[PricingType] = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Element",
        }
    )
    unit_price: Optional[UnitPrice] = field(
        default=None,
        metadata={
            "name": "UnitPrice",
            "type": "Element",
            "required": True,
        }
    )
    price_basis_quantity: Optional[PriceBasisQuantity] = field(
        default=None,
        metadata={
            "name": "PriceBasisQuantity",
            "type": "Element",
        }
    )
    calculated_price_basis_quantity: Optional[CalculatedPriceBasisQuantity] = field(
        default=None,
        metadata={
            "name": "CalculatedPriceBasisQuantity",
            "type": "Element",
        }
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )
    price_quantity_range: Optional[PriceQuantityRange] = field(
        default=None,
        metadata={
            "name": "PriceQuantityRange",
            "type": "Element",
        }
    )
    price_multiplier: Optional[PriceMultiplier] = field(
        default=None,
        metadata={
            "name": "PriceMultiplier",
            "type": "Element",
        }
    )


@dataclass
class ShipFromLocation:
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ShipToLocation:
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ShipToSubLocation:
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TermsOfDelivery:
    terms_of_delivery_function_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TermsOfDeliveryFunctionCoded",
            "type": "Element",
            "required": True,
        }
    )
    terms_of_delivery_function_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TermsOfDeliveryFunctionCodedOther",
            "type": "Element",
        }
    )
    transport_terms_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportTermsCoded",
            "type": "Element",
        }
    )
    transport_terms_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportTermsCodedOther",
            "type": "Element",
        }
    )
    shipment_method_of_payment_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShipmentMethodOfPaymentCoded",
            "type": "Element",
            "required": True,
        }
    )
    shipment_method_of_payment_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShipmentMethodOfPaymentCodedOther",
            "type": "Element",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
        }
    )
    terms_of_delivery_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "TermsOfDeliveryDescription",
            "type": "Element",
        }
    )
    transport_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportDescription",
            "type": "Element",
        }
    )
    risk_of_loss_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "RiskOfLossCoded",
            "type": "Element",
        }
    )
    risk_of_loss_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "RiskOfLossCodedOther",
            "type": "Element",
        }
    )
    risk_of_loss_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "RiskOfLossDescription",
            "type": "Element",
        }
    )


@dataclass
class AuctionCurrency:
    base_currency: Optional[BaseCurrency] = field(
        default=None,
        metadata={
            "name": "BaseCurrency",
            "type": "Element",
            "required": True,
        }
    )
    list_of_valid_bid_currency: Optional[ListOfValidBidCurrency] = field(
        default=None,
        metadata={
            "name": "ListOfValidBidCurrency",
            "type": "Element",
        }
    )


@dataclass
class AuctionPartners:
    party_id: Optional[PartyId] = field(
        default=None,
        metadata={
            "name": "PartyID",
            "type": "Element",
            "required": True,
        }
    )
    list_of_identifier: Optional[ListOfIdentifier] = field(
        default=None,
        metadata={
            "name": "ListOfIdentifier",
            "type": "Element",
        }
    )
    mdfbusiness: Optional[str] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        }
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        }
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        }
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        }
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        }
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        }
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        }
    )
    group_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "GroupIndicator",
            "type": "Element",
            "required": True,
        }
    )
    list_of_key_val: Optional[ListOfKeyVal] = field(
        default=None,
        metadata={
            "name": "ListOfKeyVal",
            "type": "Element",
        }
    )


@dataclass
class ListOfConditions:
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfEquipmentMeasurements:
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfPrice:
    price: List[Price] = field(
        default_factory=list,
        metadata={
            "name": "Price",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Party:
    party_id: Optional[PartyId] = field(
        default=None,
        metadata={
            "name": "PartyID",
            "type": "Element",
            "required": True,
        }
    )
    list_of_identifier: Optional[ListOfIdentifier] = field(
        default=None,
        metadata={
            "name": "ListOfIdentifier",
            "type": "Element",
        }
    )
    mdfbusiness: Optional[str] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        }
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        }
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        }
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        }
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        }
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        }
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        }
    )


@dataclass
class SubLocationItemPackagingReference:
    item_packaging_reference: Optional[ItemPackagingReference] = field(
        default=None,
        metadata={
            "name": "ItemPackagingReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionPricingDetail:
    open_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "OpenPrice",
            "type": "Element",
            "required": True,
        }
    )
    reserve_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservePrice",
            "type": "Element",
        }
    )
    bid_increment: Optional[str] = field(
        default=None,
        metadata={
            "name": "BidIncrement",
            "type": "Element",
        }
    )
    list_of_price: Optional[ListOfPrice] = field(
        default=None,
        metadata={
            "name": "ListOfPrice",
            "type": "Element",
        }
    )


@dataclass
class Conditions:
    refrigeration_on: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefrigerationOn",
            "type": "Element",
        }
    )
    residue: Optional[str] = field(
        default=None,
        metadata={
            "name": "Residue",
            "type": "Element",
        }
    )
    list_of_conditions: Optional[ListOfConditions] = field(
        default=None,
        metadata={
            "name": "ListOfConditions",
            "type": "Element",
        }
    )


@dataclass
class InitiatingParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfAuctionPartners:
    auction_partners: List[AuctionPartners] = field(
        default_factory=list,
        metadata={
            "name": "AuctionPartners",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfParty:
    party: List[Party] = field(
        default_factory=list,
        metadata={
            "name": "Party",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ShipToSubInformation:
    ship_to_sub_location: Optional[ShipToSubLocation] = field(
        default=None,
        metadata={
            "name": "ShipToSubLocation",
            "type": "Element",
            "required": True,
        }
    )
    ship_to_sub_quantity: Optional[ShipToSubQuantity] = field(
        default=None,
        metadata={
            "name": "ShipToSubQuantity",
            "type": "Element",
            "required": True,
        }
    )
    sub_location_item_packaging_reference: Optional[SubLocationItemPackagingReference] = field(
        default=None,
        metadata={
            "name": "SubLocationItemPackagingReference",
            "type": "Element",
        }
    )


@dataclass
class ListOfShipToSubInformation:
    ship_to_sub_information: List[ShipToSubInformation] = field(
        default_factory=list,
        metadata={
            "name": "ShipToSubInformation",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListToInform:
    list_of_party: Optional[ListOfParty] = field(
        default=None,
        metadata={
            "name": "ListOfParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TransportEquipment:
    equipment_provider_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentProviderCoded",
            "type": "Element",
        }
    )
    equipment_provider_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentProviderCodedOther",
            "type": "Element",
        }
    )
    equipment_owner_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentOwnerCoded",
            "type": "Element",
        }
    )
    equipment_owner_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentOwnerCodedOther",
            "type": "Element",
        }
    )
    equipment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentID",
            "type": "Element",
            "required": True,
        }
    )
    equipment_size_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentSizeTypeCoded",
            "type": "Element",
        }
    )
    equipement_size_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipementSizeTypeCodedOther",
            "type": "Element",
        }
    )
    equipment_status_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentStatusCoded",
            "type": "Element",
        }
    )
    equipment_status_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentStatusCodedOther",
            "type": "Element",
        }
    )
    full_indicator_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullIndicatorCoded",
            "type": "Element",
        }
    )
    full_indicator_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullIndicatorCodedOther",
            "type": "Element",
        }
    )
    conditions: Optional[Conditions] = field(
        default=None,
        metadata={
            "name": "Conditions",
            "type": "Element",
        }
    )
    equipment_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentNote",
            "type": "Element",
        }
    )
    list_of_seal_info: Optional[ListOfSealInfo] = field(
        default=None,
        metadata={
            "name": "ListOfSealInfo",
            "type": "Element",
        }
    )
    list_of_equipment_measurements: Optional[ListOfEquipmentMeasurements] = field(
        default=None,
        metadata={
            "name": "ListOfEquipmentMeasurements",
            "type": "Element",
        }
    )


@dataclass
class AuctionParticipants:
    initiating_party: Optional[InitiatingParty] = field(
        default=None,
        metadata={
            "name": "InitiatingParty",
            "type": "Element",
            "required": True,
        }
    )
    community_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommunityID",
            "type": "Element",
        }
    )
    list_to_inform: Optional[ListToInform] = field(
        default=None,
        metadata={
            "name": "ListToInform",
            "type": "Element",
        }
    )
    list_of_auction_partners: Optional[ListOfAuctionPartners] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionPartners",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfTransportEquipment:
    transport_equipment: List[TransportEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TransportEquipment",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AuctionCreateHeader:
    auction_create_purpose: Optional[AuctionCreatePurpose] = field(
        default=None,
        metadata={
            "name": "AuctionCreatePurpose",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCreateIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCreateID",
            "type": "Element",
            "required": True,
        }
    )
    foward_auction_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "FowardAuctionIndicator",
            "type": "Element",
            "required": True,
        }
    )
    auction_validity_dates: Optional[AuctionValidityDates] = field(
        default=None,
        metadata={
            "name": "AuctionValidityDates",
            "type": "Element",
            "required": True,
        }
    )
    decision_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DecisionDate",
            "type": "Element",
        }
    )
    rules_profile: Optional[RulesProfile] = field(
        default=None,
        metadata={
            "name": "RulesProfile",
            "type": "Element",
            "required": True,
        }
    )
    auction_currency: Optional[AuctionCurrency] = field(
        default=None,
        metadata={
            "name": "AuctionCurrency",
            "type": "Element",
        }
    )
    auction_participants: Optional[AuctionParticipants] = field(
        default=None,
        metadata={
            "name": "AuctionParticipants",
            "type": "Element",
            "required": True,
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCreateGeneralNotes",
            "type": "Element",
        }
    )
    auction_creat_list_of_attachment: Optional[AuctionCreatListOfAttachment] = field(
        default=None,
        metadata={
            "name": "AuctionCreatListOfAttachment",
            "type": "Element",
        }
    )
    auction_specifications: Optional[AuctionSpecifications] = field(
        default=None,
        metadata={
            "name": "AuctionSpecifications",
            "type": "Element",
        }
    )


@dataclass
class Transport:
    transport_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportID",
            "type": "Element",
            "required": True,
        }
    )
    transport_mode: Optional[TransportMode] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
        }
    )
    transport_means: Optional[TransportMeans] = field(
        default=None,
        metadata={
            "name": "TransportMeans",
            "type": "Element",
        }
    )
    carrier_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarrierName",
            "type": "Element",
        }
    )
    carrier_id: Optional[CarrierId] = field(
        default=None,
        metadata={
            "name": "CarrierID",
            "type": "Element",
        }
    )
    cust_shipping_contract_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustShippingContractNum",
            "type": "Element",
        }
    )
    service_level_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelCoded",
            "type": "Element",
        }
    )
    service_level_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelCodedOther",
            "type": "Element",
        }
    )
    shipping_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShippingInstructions",
            "type": "Element",
        }
    )
    transport_leg_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportLegCoded",
            "type": "Element",
        }
    )
    transport_leg_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportLegCodedOther",
            "type": "Element",
        }
    )
    list_of_transport_equipment: Optional[ListOfTransportEquipment] = field(
        default=None,
        metadata={
            "name": "ListOfTransportEquipment",
            "type": "Element",
        }
    )
    transit_direction: Optional[TransitDirection] = field(
        default=None,
        metadata={
            "name": "TransitDirection",
            "type": "Element",
        }
    )
    transport_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportNote",
            "type": "Element",
        }
    )


@dataclass
class ScheduleLine:
    schedule_line_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleLineID",
            "type": "Element",
        }
    )
    shipment_status_event_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShipmentStatusEventCoded",
            "type": "Element",
        }
    )
    shipment_status_event_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShipmentStatusEventCodedOther",
            "type": "Element",
        }
    )
    shipment_status_reasons: Optional[ShipmentStatusReasons] = field(
        default=None,
        metadata={
            "name": "ShipmentStatusReasons",
            "type": "Element",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )
    requested_delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryDate",
            "type": "Element",
        }
    )
    list_of_other_delivery_date: Optional[ListOfOtherDeliveryDate] = field(
        default=None,
        metadata={
            "name": "ListOfOtherDeliveryDate",
            "type": "Element",
        }
    )
    schedule_line_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleLineNote",
            "type": "Element",
        }
    )
    transport: Optional[Transport] = field(
        default=None,
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )
    transport_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportReference",
            "type": "Element",
            "required": True,
        }
    )
    list_of_ship_to_sub_information: Optional[ListOfShipToSubInformation] = field(
        default=None,
        metadata={
            "name": "ListOfShipToSubInformation",
            "type": "Element",
        }
    )


@dataclass
class ListOfScheduleLine:
    schedule_line: List[ScheduleLine] = field(
        default_factory=list,
        metadata={
            "name": "ScheduleLine",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class DeliveryDetail:
    ship_to_location: Optional[ShipToLocation] = field(
        default=None,
        metadata={
            "name": "ShipToLocation",
            "type": "Element",
        }
    )
    ship_from_location: Optional[ShipFromLocation] = field(
        default=None,
        metadata={
            "name": "ShipFromLocation",
            "type": "Element",
        }
    )
    list_of_schedule_line: Optional[ListOfScheduleLine] = field(
        default=None,
        metadata={
            "name": "ListOfScheduleLine",
            "type": "Element",
        }
    )
    item_packaging_reference: Optional[ItemPackagingReference] = field(
        default=None,
        metadata={
            "name": "ItemPackagingReference",
            "type": "Element",
        }
    )
    simple_package_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "SimplePackageNote",
            "type": "Element",
        }
    )
    terms_of_delivery: List[TermsOfDelivery] = field(
        default_factory=list,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
        }
    )
    cargo_classification: Optional[CargoTypeification] = field(
        default=None,
        metadata={
            "name": "CargoClassification",
            "type": "Element",
        }
    )


@dataclass
class AuctionDeliveryDetail:
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionCreateDetail:
    auction_item: Optional[AuctionItem] = field(
        default=None,
        metadata={
            "name": "AuctionItem",
            "type": "Element",
            "required": True,
        }
    )
    list_of_mvbvariables: Optional[ListOfMvbvariables] = field(
        default=None,
        metadata={
            "name": "ListOfMVBVariables",
            "type": "Element",
        }
    )
    auction_pricing_detail: Optional[AuctionPricingDetail] = field(
        default=None,
        metadata={
            "name": "AuctionPricingDetail",
            "type": "Element",
        }
    )
    auction_item_dates: Optional[AuctionItemDates] = field(
        default=None,
        metadata={
            "name": "AuctionItemDates",
            "type": "Element",
        }
    )
    auction_delivery_detail: Optional[AuctionDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "AuctionDeliveryDetail",
            "type": "Element",
        }
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )
    component_auction_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComponentAuctionIndicator",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_item_components: Optional[ListOfAuctionItemComponents] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionItemComponents",
            "type": "Element",
        }
    )


@dataclass
class AuctionDetail:
    auction_item: Optional[AuctionItem] = field(
        default=None,
        metadata={
            "name": "AuctionItem",
            "type": "Element",
            "required": True,
        }
    )
    list_of_mvbvariables: Optional[ListOfMvbvariables] = field(
        default=None,
        metadata={
            "name": "ListOfMVBVariables",
            "type": "Element",
        }
    )
    auction_pricing_detail: Optional[AuctionPricingDetail] = field(
        default=None,
        metadata={
            "name": "AuctionPricingDetail",
            "type": "Element",
        }
    )
    auction_item_dates: Optional[AuctionItemDates] = field(
        default=None,
        metadata={
            "name": "AuctionItemDates",
            "type": "Element",
        }
    )
    auction_delivery_detail: Optional[AuctionDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "AuctionDeliveryDetail",
            "type": "Element",
        }
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )
    component_auction_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComponentAuctionIndicator",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfAuctionCreateDetail:
    auction_create_detail: List[AuctionCreateDetail] = field(
        default_factory=list,
        metadata={
            "name": "AuctionCreateDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AuctionCreate:
    auction_create_header: Optional[AuctionCreateHeader] = field(
        default=None,
        metadata={
            "name": "AuctionCreateHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_create_detail: Optional[ListOfAuctionCreateDetail] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionCreateDetail",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_summary: Optional[AuctionCreateSummary] = field(
        default=None,
        metadata={
            "name": "AuctionCreateSummary",
            "type": "Element",
            "required": True,
        }
    )
