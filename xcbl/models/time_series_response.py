from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xcbl.models.trading_partner_organization_information import (
    ExternalAddressId,
)
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import (
    Building,
    City,
    CorrespondenceLanguage,
    Country,
    County,
    Department,
    District,
    Floor,
    GeneralNotes,
    HouseNumber,
    Identifier,
    InhouseMail,
    Language,
    Pobox,
    PostalCode,
    Region,
    RoomNumber,
    Street,
    StreetSupplement1,
    StreetSupplement2,
    Timezone,
    ValidityDates,
)


@dataclass(kw_only=True)
class CharacteristicAttributeDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CharacteristicAttributeId:
    class Meta:
        name = "CharacteristicAttributeID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CharacteristicAttributeNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CharacteristicCombinationId:
    class Meta:
        name = "CharacteristicCombinationID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CharacteristicCombinationPurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CharacteristicCombinationPurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CharacteristicCombinationResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CharacteristicCombinationResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CharacteristicName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactFunctionCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactFunctionCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactNumberTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactNumberTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactNumberValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DimensionCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DimensionCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Gpssystem:
    class Meta:
        name = "GPSSystem"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class KeyFigureDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class KeyFigureId:
    class Meta:
        name = "KeyFigureID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class KeyFigureName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Latitude:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LocationAttributeDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LocationAttributeId:
    class Meta:
        name = "LocationAttributeID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LocationDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LocationNotes:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LocationQualifierCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LocationQualifierCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Longitude:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Mdfbusiness:
    class Meta:
        name = "MDFBusiness"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
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
    CONDITIONS_OTHER_THAN_STANDARD_TEMPERATURE_AND_PRESSURE = (
        "ConditionsOtherThanStandardTemperatureAndPressure"
    )
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
    CONDITIONS_OTHER_THAN_STANDARD_TEMPERATURE_AND_PRESSURE = (
        "ConditionsOtherThanStandardTemperatureAndPressure"
    )
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
    CONDITIONS_OTHER_THAN_STANDARD_TEMPERATURE_AND_PRESSURE = (
        "ConditionsOtherThanStandardTemperatureAndPressure"
    )
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


@dataclass(kw_only=True)
class Name11:
    class Meta:
        name = "Name1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Name21:
    class Meta:
        name = "Name2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Name31:
    class Meta:
        name = "Name3"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


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
    FOREIGN_DISCLOSURE_INFORMATION_OFFICE = (
        "ForeignDisclosureInformationOffice"
    )
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
    LOCATION_OF_GOODS_FOR_CUSTOMS_EXAMINATION_BEFORE_CLEARANCE = (
        "LocationOfGoodsForCustomsExaminationBeforeClearance"
    )
    LOCATION_OF_LOAD_EXCHANGE = "LocationOfLoadExchange"
    LOCATION_OF_SPOT_FOR_STORAGE = "LocationOfSpotForStorage"
    LOT = "Lot"
    MAIL_ADDRESS = "MailAddress"
    MAIL_TO = "MailTo"
    MANUFACTURING_PLANT = "ManufacturingPlant"
    MASTER_PROPERTY = "MasterProperty"
    MATERIAL_CHANGE_NOTICE_ADDRESS = "MaterialChangeNoticeAddress"
    MATERIAL_DISPOSITION_AUTHORIZATION_LOCATION = (
        "MaterialDispositionAuthorizationLocation"
    )
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
    SUBCONTRACT_OR_COGNIZANT_SECURITY_OFFICE = (
        "SubcontractOrCognizantSecurityOffice"
    )
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


@dataclass(kw_only=True)
class PartyRoleCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PartyRoleCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ProductAttributeDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ProductAttributeId:
    class Meta:
        name = "ProductAttributeID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ProductNotes:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourceId:
    class Meta:
        name = "SourceID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TargetId:
    class Meta:
        name = "TargetID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesDataNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesDetailResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesDetailResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesHeaderResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesHeaderResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesKeyFigurePurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesKeyFigurePurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesKeyFigureResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesKeyFigureResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesPurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesPurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesResponseIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalCharacteristicCombinations:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalKeyFigures:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalTimeSeriesData:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Uomcoded:
    class Meta:
        name = "UOMCoded"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class UomcodedOther:
    class Meta:
        name = "UOMCodedOther"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CharacteristicAttributeName:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ContactFunction:
    contact_function_coded: ContactFunctionCoded = field(
        metadata={
            "name": "ContactFunctionCoded",
            "type": "Element",
            "required": True,
        }
    )
    contact_function_coded_other: Optional[ContactFunctionCodedOther] = field(
        default=None,
        metadata={
            "name": "ContactFunctionCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ContactId:
    class Meta:
        name = "ContactID"

    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ContactNumber:
    contact_number_value: ContactNumberValue = field(
        metadata={
            "name": "ContactNumberValue",
            "type": "Element",
            "required": True,
        }
    )
    contact_number_type_coded: ContactNumberTypeCoded = field(
        metadata={
            "name": "ContactNumberTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    contact_number_type_coded_other: Optional[ContactNumberTypeCodedOther] = (
        field(
            default=None,
            metadata={
                "name": "ContactNumberTypeCodedOther",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class Gpscooridinates:
    class Meta:
        name = "GPSCooridinates"

    gpssystem: Gpssystem = field(
        metadata={
            "name": "GPSSystem",
            "type": "Element",
            "required": True,
        }
    )
    latitude: Latitude = field(
        metadata={
            "name": "Latitude",
            "type": "Element",
            "required": True,
        }
    )
    longitude: Longitude = field(
        metadata={
            "name": "Longitude",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class KeyFigure:
    key_figure_id: KeyFigureId = field(
        metadata={
            "name": "KeyFigureID",
            "type": "Element",
            "required": True,
        }
    )
    key_figure_name: Optional[KeyFigureName] = field(
        default=None,
        metadata={
            "name": "KeyFigureName",
            "type": "Element",
        },
    )
    key_figure_description: Optional[KeyFigureDescription] = field(
        default=None,
        metadata={
            "name": "KeyFigureDescription",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfIdentifier:
    identifier: List[Identifier] = field(
        default_factory=list,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class LocId:
    class Meta:
        name = "LocID"

    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LocationAttributeName:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MaximumValue:
    significance_coded: Optional[MaximumValueSignificanceCoded] = field(
        default=None,
        metadata={
            "name": "SignificanceCoded",
            "type": "Attribute",
        },
    )
    conditions_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConditionsCodedOther",
            "type": "Attribute",
        },
    )
    conditions_coded: Optional[MaximumValueConditionsCoded] = field(
        default=None,
        metadata={
            "name": "ConditionsCoded",
            "type": "Attribute",
        },
    )
    significance_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignificanceCodedOther",
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MeasurementValue:
    significance_coded: Optional[MeasurementValueSignificanceCoded] = field(
        default=None,
        metadata={
            "name": "SignificanceCoded",
            "type": "Attribute",
        },
    )
    conditions_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConditionsCodedOther",
            "type": "Attribute",
        },
    )
    conditions_coded: Optional[MeasurementValueConditionsCoded] = field(
        default=None,
        metadata={
            "name": "ConditionsCoded",
            "type": "Attribute",
        },
    )
    significance_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignificanceCodedOther",
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MinimumValue:
    significance_coded: Optional[MinimumValueSignificanceCoded] = field(
        default=None,
        metadata={
            "name": "SignificanceCoded",
            "type": "Attribute",
        },
    )
    conditions_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConditionsCodedOther",
            "type": "Attribute",
        },
    )
    conditions_coded: Optional[MinimumValueConditionsCoded] = field(
        default=None,
        metadata={
            "name": "ConditionsCoded",
            "type": "Attribute",
        },
    )
    significance_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignificanceCodedOther",
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NameAddress:
    address_type_coded: NameAddressAddressTypeCoded = field(
        default=NameAddressAddressTypeCoded.NOT_APPLICABLE,
        metadata={
            "name": "AddressTypeCoded",
            "type": "Attribute",
            "required": True,
        },
    )
    address_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddressTypeCodedOther",
            "type": "Attribute",
        },
    )
    external_address_id: Optional[ExternalAddressId] = field(
        default=None,
        metadata={
            "name": "ExternalAddressID",
            "type": "Element",
        },
    )
    name1: Name11 = field(
        metadata={
            "name": "Name1",
            "type": "Element",
            "required": True,
        }
    )
    name2: Optional[Name21] = field(
        default=None,
        metadata={
            "name": "Name2",
            "type": "Element",
        },
    )
    name3: Optional[Name31] = field(
        default=None,
        metadata={
            "name": "Name3",
            "type": "Element",
        },
    )
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
        },
    )
    pobox: Optional[Pobox] = field(
        default=None,
        metadata={
            "name": "POBox",
            "type": "Element",
        },
    )
    street: Optional[Street] = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
        },
    )
    house_number: Optional[HouseNumber] = field(
        default=None,
        metadata={
            "name": "HouseNumber",
            "type": "Element",
        },
    )
    street_supplement1: Optional[StreetSupplement1] = field(
        default=None,
        metadata={
            "name": "StreetSupplement1",
            "type": "Element",
        },
    )
    street_supplement2: Optional[StreetSupplement2] = field(
        default=None,
        metadata={
            "name": "StreetSupplement2",
            "type": "Element",
        },
    )
    building: Optional[Building] = field(
        default=None,
        metadata={
            "name": "Building",
            "type": "Element",
        },
    )
    floor: Optional[Floor] = field(
        default=None,
        metadata={
            "name": "Floor",
            "type": "Element",
        },
    )
    room_number: Optional[RoomNumber] = field(
        default=None,
        metadata={
            "name": "RoomNumber",
            "type": "Element",
        },
    )
    inhouse_mail: Optional[InhouseMail] = field(
        default=None,
        metadata={
            "name": "InhouseMail",
            "type": "Element",
        },
    )
    department: Optional[Department] = field(
        default=None,
        metadata={
            "name": "Department",
            "type": "Element",
        },
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        },
    )
    city: Optional[City] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
        },
    )
    county: Optional[County] = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
        },
    )
    region: Optional[Region] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    district: Optional[District] = field(
        default=None,
        metadata={
            "name": "District",
            "type": "Element",
        },
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
        },
    )
    timezone: Optional[Timezone] = field(
        default=None,
        metadata={
            "name": "Timezone",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PartyId:
    class Meta:
        name = "PartyID"

    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ProductAttributeName:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceTargetId:
    class Meta:
        name = "SourceTargetID"

    source_id: Optional[SourceId] = field(
        default=None,
        metadata={
            "name": "SourceID",
            "type": "Element",
        },
    )
    target_id: Optional[TargetId] = field(
        default=None,
        metadata={
            "name": "TargetID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TimeSeriesBucket:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesId:
    class Meta:
        name = "TimeSeriesID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesResponseId:
    class Meta:
        name = "TimeSeriesResponseID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesSummary:
    total_time_series_data: Optional[TotalTimeSeriesData] = field(
        default=None,
        metadata={
            "name": "TotalTimeSeriesData",
            "type": "Element",
        },
    )
    total_characteristic_combinations: Optional[
        TotalCharacteristicCombinations
    ] = field(
        default=None,
        metadata={
            "name": "TotalCharacteristicCombinations",
            "type": "Element",
        },
    )
    total_key_figures: Optional[TotalKeyFigures] = field(
        default=None,
        metadata={
            "name": "TotalKeyFigures",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TimeSeriesTimePeriod:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class UnitOfMeasurement:
    uomcoded: Uomcoded = field(
        metadata={
            "name": "UOMCoded",
            "type": "Element",
            "required": True,
        }
    )
    uomcoded_other: Optional[UomcodedOther] = field(
        default=None,
        metadata={
            "name": "UOMCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfContactNumber:
    contact_number: List[ContactNumber] = field(
        default_factory=list,
        metadata={
            "name": "ContactNumber",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class LocationIdentifier:
    loc_id: LocId = field(
        metadata={
            "name": "LocID",
            "type": "Element",
            "required": True,
        }
    )
    location_description: Optional[LocationDescription] = field(
        default=None,
        metadata={
            "name": "LocationDescription",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class MeasurementRange:
    minimum_value: MinimumValue = field(
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "required": True,
        }
    )
    maximum_value: MaximumValue = field(
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceKeyFigure:
    key_figure: KeyFigure = field(
        metadata={
            "name": "KeyFigure",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetKeyFigure:
    key_figure: KeyFigure = field(
        metadata={
            "name": "KeyFigure",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesData:
    time_series_bucket: TimeSeriesBucket = field(
        metadata={
            "name": "TimeSeriesBucket",
            "type": "Element",
            "required": True,
        }
    )
    time_series_value: TimeSeriesValue = field(
        metadata={
            "name": "TimeSeriesValue",
            "type": "Element",
            "required": True,
        }
    )
    time_series_data_note: Optional[TimeSeriesDataNote] = field(
        default=None,
        metadata={
            "name": "TimeSeriesDataNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TimeSeriesPlanningData:
    source_target_id: SourceTargetId = field(
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesPlanningStep:
    source_target_id: SourceTargetId = field(
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesResponseSummary:
    time_series_summary: TimeSeriesSummary = field(
        metadata={
            "name": "TimeSeriesSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesSelection:
    source_target_id: SourceTargetId = field(
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesSystemType:
    source_target_id: SourceTargetId = field(
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Contact:
    contact_id: Optional[ContactId] = field(
        default=None,
        metadata={
            "name": "ContactID",
            "type": "Element",
        },
    )
    contact_name: ContactName = field(
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
        },
    )
    contact_description: Optional[ContactDescription] = field(
        default=None,
        metadata={
            "name": "ContactDescription",
            "type": "Element",
        },
    )
    list_of_contact_number: Optional[ListOfContactNumber] = field(
        default=None,
        metadata={
            "name": "ListOfContactNumber",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class KeyFigureInformation:
    source_key_figure: Optional[SourceKeyFigure] = field(
        default=None,
        metadata={
            "name": "SourceKeyFigure",
            "type": "Element",
        },
    )
    target_key_figure: Optional[TargetKeyFigure] = field(
        default=None,
        metadata={
            "name": "TargetKeyFigure",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Location:
    location_qualifier_coded: Optional[LocationQualifierCoded] = field(
        default=None,
        metadata={
            "name": "LocationQualifierCoded",
            "type": "Element",
        },
    )
    location_qualifier_coded_other: Optional[LocationQualifierCodedOther] = (
        field(
            default=None,
            metadata={
                "name": "LocationQualifierCodedOther",
                "type": "Element",
            },
        )
    )
    location_identifier: Optional[LocationIdentifier] = field(
        default=None,
        metadata={
            "name": "LocationIdentifier",
            "type": "Element",
        },
    )
    external_address_id: Optional[ExternalAddressId] = field(
        default=None,
        metadata={
            "name": "ExternalAddressID",
            "type": "Element",
        },
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        },
    )
    gpscooridinates: Optional[Gpscooridinates] = field(
        default=None,
        metadata={
            "name": "GPSCooridinates",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Measurement:
    measurement_value: Optional[MeasurementValue] = field(
        default=None,
        metadata={
            "name": "MeasurementValue",
            "type": "Element",
        },
    )
    measurement_range: Optional[MeasurementRange] = field(
        default=None,
        metadata={
            "name": "MeasurementRange",
            "type": "Element",
        },
    )
    unit_of_measurement: UnitOfMeasurement = field(
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Dimension:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )
    dimension_coded: DimensionCoded = field(
        metadata={
            "name": "DimensionCoded",
            "type": "Element",
            "required": True,
        }
    )
    dimension_coded_other: Optional[DimensionCodedOther] = field(
        default=None,
        metadata={
            "name": "DimensionCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfContact:
    contact: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderContact:
    contact: Contact = field(
        metadata={
            "name": "Contact",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ReceivingContact:
    contact: Contact = field(
        metadata={
            "name": "Contact",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShippingContact:
    contact: Contact = field(
        metadata={
            "name": "Contact",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesKeyFigureData:
    time_series_key_figure_purpose_coded: Optional[
        TimeSeriesKeyFigurePurposeCoded
    ] = field(
        default=None,
        metadata={
            "name": "TimeSeriesKeyFigurePurposeCoded",
            "type": "Element",
        },
    )
    time_series_key_figure_purpose_coded_other: Optional[
        TimeSeriesKeyFigurePurposeCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "TimeSeriesKeyFigurePurposeCodedOther",
            "type": "Element",
        },
    )
    time_series_key_figure_response_coded: Optional[
        TimeSeriesKeyFigureResponseCoded
    ] = field(
        default=None,
        metadata={
            "name": "TimeSeriesKeyFigureResponseCoded",
            "type": "Element",
        },
    )
    time_series_key_figure_response_coded_other: Optional[
        TimeSeriesKeyFigureResponseCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "TimeSeriesKeyFigureResponseCodedOther",
            "type": "Element",
        },
    )
    characteristic_combination_id: CharacteristicCombinationId = field(
        metadata={
            "name": "CharacteristicCombinationID",
            "type": "Element",
            "required": True,
        }
    )
    key_figure_information: KeyFigureInformation = field(
        metadata={
            "name": "KeyFigureInformation",
            "type": "Element",
            "required": True,
        }
    )
    unit_of_measurement: UnitOfMeasurement = field(
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
            "required": True,
        }
    )
    time_series_data: List[TimeSeriesData] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeriesData",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfDimension:
    dimension: List[Dimension] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfTimeSeriesKeyFigureData:
    time_series_key_figure_data: List[TimeSeriesKeyFigureData] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeriesKeyFigureData",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OtherContacts:
    list_of_contact: ListOfContact = field(
        metadata={
            "name": "ListOfContact",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CharacteristicAttribute:
    characteristic_name: CharacteristicName = field(
        metadata={
            "name": "CharacteristicName",
            "type": "Element",
            "required": True,
        }
    )
    characteristic_attribute_id: CharacteristicAttributeId = field(
        metadata={
            "name": "CharacteristicAttributeID",
            "type": "Element",
            "required": True,
        }
    )
    characteristic_attribute_name: List[CharacteristicAttributeName] = field(
        default_factory=list,
        metadata={
            "name": "CharacteristicAttributeName",
            "type": "Element",
        },
    )
    characteristic_attribute_description: Optional[
        CharacteristicAttributeDescription
    ] = field(
        default=None,
        metadata={
            "name": "CharacteristicAttributeDescription",
            "type": "Element",
        },
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        },
    )
    characteristic_attribute_note: Optional[CharacteristicAttributeNote] = (
        field(
            default=None,
            metadata={
                "name": "CharacteristicAttributeNote",
                "type": "Element",
            },
        )
    )
    other_characteristic_attribute: List["OtherCharacteristicAttribute"] = (
        field(
            default_factory=list,
            metadata={
                "name": "OtherCharacteristicAttribute",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class ListOfChangedTimeSeriesKeyFigureData:
    list_of_time_series_key_figure_data: ListOfTimeSeriesKeyFigureData = field(
        metadata={
            "name": "ListOfTimeSeriesKeyFigureData",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Party:
    party_id: PartyId = field(
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
        },
    )
    mdfbusiness: Optional[Mdfbusiness] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        },
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        },
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        },
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        },
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        },
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        },
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PartyCoded:
    party_id: PartyId = field(
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
        },
    )
    mdfbusiness: Optional[Mdfbusiness] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        },
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        },
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        },
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        },
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        },
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        },
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        },
    )
    party_role_coded: PartyRoleCoded = field(
        metadata={
            "name": "PartyRoleCoded",
            "type": "Element",
            "required": True,
        }
    )
    party_role_coded_other: Optional[PartyRoleCodedOther] = field(
        default=None,
        metadata={
            "name": "PartyRoleCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfPartyCoded:
    party_coded: List[PartyCoded] = field(
        default_factory=list,
        metadata={
            "name": "PartyCoded",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OtherCharacteristicAttribute:
    characteristic_attribute: CharacteristicAttribute = field(
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherLocationAttribute:
    characteristic_attribute: CharacteristicAttribute = field(
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherProductAttribute:
    characteristic_attribute: CharacteristicAttribute = field(
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ReceiverParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceCharacteristicsOther:
    characteristic_attribute: CharacteristicAttribute = field(
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetCharacteristicsOther:
    characteristic_attribute: CharacteristicAttribute = field(
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BaseCharacteristicLocation:
    location_attribute_id: LocationAttributeId = field(
        metadata={
            "name": "LocationAttributeID",
            "type": "Element",
            "required": True,
        }
    )
    location_attribute_name: List[LocationAttributeName] = field(
        default_factory=list,
        metadata={
            "name": "LocationAttributeName",
            "type": "Element",
        },
    )
    location_attribute_description: Optional[LocationAttributeDescription] = (
        field(
            default=None,
            metadata={
                "name": "LocationAttributeDescription",
                "type": "Element",
            },
        )
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
        },
    )
    location_notes: Optional[LocationNotes] = field(
        default=None,
        metadata={
            "name": "LocationNotes",
            "type": "Element",
        },
    )
    other_location_attribute: Optional[OtherLocationAttribute] = field(
        default=None,
        metadata={
            "name": "OtherLocationAttribute",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class BaseCharacteristicProduct:
    product_attribute_id: ProductAttributeId = field(
        metadata={
            "name": "ProductAttributeID",
            "type": "Element",
            "required": True,
        }
    )
    product_attribute_name: List[ProductAttributeName] = field(
        default_factory=list,
        metadata={
            "name": "ProductAttributeName",
            "type": "Element",
        },
    )
    product_attribute_description: Optional[ProductAttributeDescription] = (
        field(
            default=None,
            metadata={
                "name": "ProductAttributeDescription",
                "type": "Element",
            },
        )
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        },
    )
    product_notes: Optional[ProductNotes] = field(
        default=None,
        metadata={
            "name": "ProductNotes",
            "type": "Element",
        },
    )
    other_product_attribute: Optional[OtherProductAttribute] = field(
        default=None,
        metadata={
            "name": "OtherProductAttribute",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CharacteristicOther:
    source_characteristics_other: Optional[SourceCharacteristicsOther] = field(
        default=None,
        metadata={
            "name": "SourceCharacteristicsOther",
            "type": "Element",
        },
    )
    target_characteristics_other: Optional[TargetCharacteristicsOther] = field(
        default=None,
        metadata={
            "name": "TargetCharacteristicsOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TimeSeriesParty:
    source_party: Optional[SourceParty] = field(
        default=None,
        metadata={
            "name": "SourceParty",
            "type": "Element",
        },
    )
    receiver_party: Optional[ReceiverParty] = field(
        default=None,
        metadata={
            "name": "ReceiverParty",
            "type": "Element",
        },
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SourceLocation:
    base_characteristic_location: BaseCharacteristicLocation = field(
        metadata={
            "name": "BaseCharacteristicLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceProduct:
    base_characteristic_product: BaseCharacteristicProduct = field(
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceProductGroup:
    base_characteristic_product: BaseCharacteristicProduct = field(
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetLocation:
    base_characteristic_location: BaseCharacteristicLocation = field(
        metadata={
            "name": "BaseCharacteristicLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetProduct:
    base_characteristic_product: BaseCharacteristicProduct = field(
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetProductGroup:
    base_characteristic_product: BaseCharacteristicProduct = field(
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesHeader:
    time_series_issue_date: TimeSeriesIssueDate = field(
        metadata={
            "name": "TimeSeriesIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    time_series_id: TimeSeriesId = field(
        metadata={
            "name": "TimeSeriesID",
            "type": "Element",
            "required": True,
        }
    )
    time_series_purpose_coded: TimeSeriesPurposeCoded = field(
        metadata={
            "name": "TimeSeriesPurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    time_series_purpose_coded_other: Optional[TimeSeriesPurposeCodedOther] = (
        field(
            default=None,
            metadata={
                "name": "TimeSeriesPurposeCodedOther",
                "type": "Element",
            },
        )
    )
    time_series_time_period: Optional[TimeSeriesTimePeriod] = field(
        default=None,
        metadata={
            "name": "TimeSeriesTimePeriod",
            "type": "Element",
        },
    )
    time_series_system_type: Optional[TimeSeriesSystemType] = field(
        default=None,
        metadata={
            "name": "TimeSeriesSystemType",
            "type": "Element",
        },
    )
    time_series_planning_data: TimeSeriesPlanningData = field(
        metadata={
            "name": "TimeSeriesPlanningData",
            "type": "Element",
            "required": True,
        }
    )
    time_series_selection: Optional[TimeSeriesSelection] = field(
        default=None,
        metadata={
            "name": "TimeSeriesSelection",
            "type": "Element",
        },
    )
    time_series_planning_step: Optional[TimeSeriesPlanningStep] = field(
        default=None,
        metadata={
            "name": "TimeSeriesPlanningStep",
            "type": "Element",
        },
    )
    time_series_party: TimeSeriesParty = field(
        metadata={
            "name": "TimeSeriesParty",
            "type": "Element",
            "required": True,
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    general_notes: Optional[GeneralNotes] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TimeSeriesResponseParty:
    time_series_party: TimeSeriesParty = field(
        metadata={
            "name": "TimeSeriesParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ChangedTimeSeriesHeader:
    time_series_header: TimeSeriesHeader = field(
        metadata={
            "name": "TimeSeriesHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CharacteristicLocation:
    source_location: Optional[SourceLocation] = field(
        default=None,
        metadata={
            "name": "SourceLocation",
            "type": "Element",
        },
    )
    target_location: Optional[TargetLocation] = field(
        default=None,
        metadata={
            "name": "TargetLocation",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CharacteristicProduct:
    source_product: Optional[SourceProduct] = field(
        default=None,
        metadata={
            "name": "SourceProduct",
            "type": "Element",
        },
    )
    target_product: Optional[TargetProduct] = field(
        default=None,
        metadata={
            "name": "TargetProduct",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CharacteristicProductGroup:
    source_product_group: Optional[SourceProductGroup] = field(
        default=None,
        metadata={
            "name": "SourceProductGroup",
            "type": "Element",
        },
    )
    target_product_group: Optional[TargetProductGroup] = field(
        default=None,
        metadata={
            "name": "TargetProductGroup",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CharacteristicCombination:
    characteristic_combination_purpose_coded: Optional[
        CharacteristicCombinationPurposeCoded
    ] = field(
        default=None,
        metadata={
            "name": "CharacteristicCombinationPurposeCoded",
            "type": "Element",
        },
    )
    characteristic_combination_purpose_coded_other: Optional[
        CharacteristicCombinationPurposeCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "CharacteristicCombinationPurposeCodedOther",
            "type": "Element",
        },
    )
    characteristic_combination_response_coded: Optional[
        CharacteristicCombinationResponseCoded
    ] = field(
        default=None,
        metadata={
            "name": "CharacteristicCombinationResponseCoded",
            "type": "Element",
        },
    )
    characteristic_combination_response_coded_other: Optional[
        CharacteristicCombinationResponseCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "CharacteristicCombinationResponseCodedOther",
            "type": "Element",
        },
    )
    characteristic_combination_id: CharacteristicCombinationId = field(
        metadata={
            "name": "CharacteristicCombinationID",
            "type": "Element",
            "required": True,
        }
    )
    characteristic_product: Optional[CharacteristicProduct] = field(
        default=None,
        metadata={
            "name": "CharacteristicProduct",
            "type": "Element",
        },
    )
    characteristic_location: Optional[CharacteristicLocation] = field(
        default=None,
        metadata={
            "name": "CharacteristicLocation",
            "type": "Element",
        },
    )
    characteristic_product_group: Optional[CharacteristicProductGroup] = field(
        default=None,
        metadata={
            "name": "CharacteristicProductGroup",
            "type": "Element",
        },
    )
    characteristic_other: List[CharacteristicOther] = field(
        default_factory=list,
        metadata={
            "name": "CharacteristicOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TimeSeriesResponseHeader:
    time_series_response_issue_date: TimeSeriesResponseIssueDate = field(
        metadata={
            "name": "TimeSeriesResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    time_series_response_id: TimeSeriesResponseId = field(
        metadata={
            "name": "TimeSeriesResponseID",
            "type": "Element",
            "required": True,
        }
    )
    time_series_reference: TimeSeriesReference = field(
        metadata={
            "name": "TimeSeriesReference",
            "type": "Element",
            "required": True,
        }
    )
    time_series_planning_data: Optional[TimeSeriesPlanningData] = field(
        default=None,
        metadata={
            "name": "TimeSeriesPlanningData",
            "type": "Element",
        },
    )
    time_series_response_party: TimeSeriesResponseParty = field(
        metadata={
            "name": "TimeSeriesResponseParty",
            "type": "Element",
            "required": True,
        }
    )
    time_series_header_response_coded: TimeSeriesHeaderResponseCoded = field(
        metadata={
            "name": "TimeSeriesHeaderResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    time_series_header_response_coded_other: Optional[
        TimeSeriesHeaderResponseCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "TimeSeriesHeaderResponseCodedOther",
            "type": "Element",
        },
    )
    changed_time_series_header: Optional[ChangedTimeSeriesHeader] = field(
        default=None,
        metadata={
            "name": "ChangedTimeSeriesHeader",
            "type": "Element",
        },
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    general_notes: Optional[GeneralNotes] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfCharacteristicCombinations:
    characteristic_combination: List[CharacteristicCombination] = field(
        default_factory=list,
        metadata={
            "name": "CharacteristicCombination",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfChangedCharacteristicCombinations:
    list_of_characteristic_combinations: ListOfCharacteristicCombinations = (
        field(
            metadata={
                "name": "ListOfCharacteristicCombinations",
                "type": "Element",
                "required": True,
            }
        )
    )


@dataclass(kw_only=True)
class TimeSeriesResponseDetail:
    time_series_detail_response_coded: TimeSeriesDetailResponseCoded = field(
        metadata={
            "name": "TimeSeriesDetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    time_series_detail_response_coded_other: TimeSeriesDetailResponseCodedOther = field(
        metadata={
            "name": "TimeSeriesDetailResponseCodedOther",
            "type": "Element",
            "required": True,
        }
    )
    list_of_changed_characteristic_combinations: Optional[
        ListOfChangedCharacteristicCombinations
    ] = field(
        default=None,
        metadata={
            "name": "ListOfChangedCharacteristicCombinations",
            "type": "Element",
        },
    )
    list_of_changed_time_series_key_figure_data: Optional[
        ListOfChangedTimeSeriesKeyFigureData
    ] = field(
        default=None,
        metadata={
            "name": "ListOfChangedTimeSeriesKeyFigureData",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TimeSeriesResponse:
    time_series_response_header: TimeSeriesResponseHeader = field(
        metadata={
            "name": "TimeSeriesResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    time_series_response_detail: TimeSeriesResponseDetail = field(
        metadata={
            "name": "TimeSeriesResponseDetail",
            "type": "Element",
            "required": True,
        }
    )
    time_series_response_summary: TimeSeriesResponseSummary = field(
        metadata={
            "name": "TimeSeriesResponseSummary",
            "type": "Element",
            "required": True,
        }
    )
