from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xcbl.models.sourcing_result_response import (
    Purpose,
    SourcingCreateReference,
)
from xcbl.models.time_series_response import (
    Contact,
    ListOfDimension,
    ListOfPartyCoded,
    Location,
    MaximumValue,
    MinimumValue,
    Party,
    UnitOfMeasurement,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import (
    Agency,
    Country,
    Identifier,
    Language,
    ValidityDates,
)


@dataclass(kw_only=True)
class CatalogReference:
    catalog_url: str = field(
        metadata={
            "name": "CatalogURL",
            "type": "Element",
            "required": True,
        }
    )
    catalog_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CatalogID",
            "type": "Element",
        }
    )
    catalog_item_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CatalogItemID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ContractType:
    contract_type_coded: str = field(
        metadata={
            "name": "ContractTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    contract_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContractTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class DateQualifier:
    date_qualifier_coded: str = field(
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


@dataclass(kw_only=True)
class HazardousIdentifiers:
    hazardous_regulations_coded: str = field(
        metadata={
            "name": "HazardousRegulationsCoded",
            "type": "Element",
            "required": True,
        }
    )
    hazardous_regulations_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousRegulationsCodedOther",
            "type": "Element",
        }
    )
    hazard_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardCode",
            "type": "Element",
        }
    )
    code_extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeExtension",
            "type": "Element",
        }
    )
    code_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeVersion",
            "type": "Element",
        }
    )
    hazard_official_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardOfficialText",
            "type": "Element",
        }
    )
    trem_card_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "TremCardNum",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class HazardousPlacardInformation:
    hazardous_placard_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousPlacardIdentification",
            "type": "Element",
        }
    )
    hazardous_placard_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousPlacardText",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class HazardousShipmentInformation:
    hazard_packing_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardPackingCoded",
            "type": "Element",
        }
    )
    hazard_packing_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardPackingCodedOther",
            "type": "Element",
        }
    )
    hazardous_shipment_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousShipmentCoded",
            "type": "Element",
        }
    )
    hazardous_shipment_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousShipmentCodedOther",
            "type": "Element",
        }
    )
    hazardous_shipment_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousShipmentNote",
            "type": "Element",
        }
    )
    hazardous_zone_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousZoneCoded",
            "type": "Element",
        }
    )
    hazardous_zone_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousZoneCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class LineItemNum:
    buyer_line_item_num: str = field(
        metadata={
            "name": "BuyerLineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    seller_line_item_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerLineItemNum",
            "type": "Element",
        }
    )


class LineItemNumberReferenceLineItemNumTypeCoded(Enum):
    BUYER = "Buyer"
    SELLER = "Seller"


@dataclass(kw_only=True)
class LineItemType:
    line_item_type_coded: str = field(
        metadata={
            "name": "LineItemTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    line_item_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemTypeCodedOther",
            "type": "Element",
        }
    )


class MonetaryLimitSignificanceCoded(Enum):
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
class NameValuePair:
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    value: str = field(
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


@dataclass(kw_only=True)
class PartNum:
    part_id: str = field(
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


@dataclass(kw_only=True)
class PercentQualifier:
    percent_qualifier_coded: str = field(
        metadata={
            "name": "PercentQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    percent_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PercentQualifierCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PriceMultiplier:
    price_multiplier_coded: str = field(
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
    multiplier: str = field(
        metadata={
            "name": "Multiplier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PricingType:
    price_type_coded: str = field(
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


@dataclass(kw_only=True)
class ProductIdentifierCoded:
    product_identifier_qualifier_coded: str = field(
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
    product_identifier: str = field(
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


@dataclass(kw_only=True)
class QuoteAwardDetails:
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    number_of_line_items_awarded: str = field(
        metadata={
            "name": "NumberOfLineItemsAwarded",
            "type": "Element",
            "required": True,
        }
    )
    total_award_value: str = field(
        metadata={
            "name": "TotalAwardValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RoundTripInformation:
    round_trip_order: str = field(
        init=False,
        default="true",
        metadata={
            "name": "RoundTripOrder",
            "type": "Attribute",
            "required": True,
        }
    )
    immutable: Optional[str] = field(
        default=None,
        metadata={
            "name": "Immutable",
            "type": "Element",
        }
    )
    re_link: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReLink",
            "type": "Element",
        }
    )
    supplier_shopping_cart_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierShoppingCartID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class SalesRequirement:
    sales_requirement_coded: str = field(
        metadata={
            "name": "SalesRequirementCoded",
            "type": "Element",
            "required": True,
        }
    )
    sales_requirement_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SalesRequirementCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class SealIssuer:
    seal_issuer_coded: str = field(
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


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class StandardCategoryId:
    class Meta:
        name = "StandardCategoryID"

    standard_category_type: str = field(
        metadata={
            "name": "StandardCategoryType",
            "type": "Element",
            "required": True,
        }
    )
    classification_id: str = field(
        metadata={
            "name": "ClassificationID",
            "type": "Element",
            "required": True,
        }
    )
    technical_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechnicalID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class StatusReason:
    status_reason_coded: str = field(
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


@dataclass(kw_only=True)
class TransitDirection:
    transit_direction_coded: str = field(
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


@dataclass(kw_only=True)
class TransportMeans:
    transport_means_coded: str = field(
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


@dataclass(kw_only=True)
class TransportMode:
    transport_mode_coded: str = field(
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


@dataclass(kw_only=True)
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
    attachment_purpose: str = field(
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
    attachment_location: str = field(
        metadata={
            "name": "AttachmentLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BillToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BuyerPartNumber:
    part_num: PartNum = field(
        metadata={
            "name": "PartNum",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BuyerParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CarrierId:
    class Meta:
        name = "CarrierID"

    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Category:
    category_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CategoryID",
            "type": "Element",
        }
    )
    standard_category_id: Optional[StandardCategoryId] = field(
        default=None,
        metadata={
            "name": "StandardCategoryID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CommodityCode:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ConditionsOfSale:
    sales_requirement: List[SalesRequirement] = field(
        default_factory=list,
        metadata={
            "name": "SalesRequirement",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    sales_action_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SalesActionCoded",
            "type": "Element",
        }
    )
    sales_action_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SalesActionCodedOther",
            "type": "Element",
        }
    )
    sales_action_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "SalesActionValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ContractId:
    class Meta:
        name = "ContractID"

    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CountryOfDestination:
    country: Country = field(
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CountryOfOrigin:
    country: Country = field(
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DateCoded:
    date: str = field(
        metadata={
            "name": "Date",
            "type": "Element",
            "required": True,
        }
    )
    date_qualifier: DateQualifier = field(
        metadata={
            "name": "DateQualifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Description:
    description_text: str = field(
        metadata={
            "name": "DescriptionText",
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


@dataclass(kw_only=True)
class FinalRecipient:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class HazardousContact:
    contact: Contact = field(
        metadata={
            "name": "Contact",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InitiatingParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ItemCharacteristic:
    item_characteristic_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemCharacteristicCoded",
            "type": "Element",
        }
    )
    item_characteristic_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemCharacteristicCodedOther",
            "type": "Element",
        }
    )
    surface_layer_position_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SurfaceLayerPositionCoded",
            "type": "Element",
        }
    )
    surface_layer_position_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SurfaceLayerPositionCodedOther",
            "type": "Element",
        }
    )
    item_characteristic_value: str = field(
        metadata={
            "name": "ItemCharacteristicValue",
            "type": "Element",
            "required": True,
        }
    )
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
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
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class LineItemNumberReference:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    line_item_num_type_coded: LineItemNumberReferenceLineItemNumTypeCoded = field(
        default=LineItemNumberReferenceLineItemNumTypeCoded.BUYER,
        metadata={
            "name": "LineItemNumTypeCoded",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfConditions:
    list_of_dimension: ListOfDimension = field(
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfEquipmentMeasurements:
    list_of_dimension: ListOfDimension = field(
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfHazardousIdentifiers:
    hazardous_identifiers: List[HazardousIdentifiers] = field(
        default_factory=list,
        metadata={
            "name": "HazardousIdentifiers",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfNameValuePair:
    name_value_pair: List[NameValuePair] = field(
        default_factory=list,
        metadata={
            "name": "NameValuePair",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfProductIdentifierCoded:
    product_identifier_coded: List[ProductIdentifierCoded] = field(
        default_factory=list,
        metadata={
            "name": "ProductIdentifierCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfReference:
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfStatusReason:
    status_reason: List[StatusReason] = field(
        default_factory=list,
        metadata={
            "name": "StatusReason",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfTemperatureCoded:
    list_of_dimension: ListOfDimension = field(
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ManufacturerId:
    class Meta:
        name = "ManufacturerID"

    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ManufacturingToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MaterialIssuer:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MonetaryLimit:
    significance_coded: Optional[MonetaryLimitSignificanceCoded] = field(
        default=None,
        metadata={
            "name": "SignificanceCoded",
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
    monetary_limit_value: str = field(
        metadata={
            "name": "MonetaryLimitValue",
            "type": "Element",
            "required": True,
        }
    )
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MonetaryRange:
    minimum_monetary_value: str = field(
        metadata={
            "name": "MinimumMonetaryValue",
            "type": "Element",
            "required": True,
        }
    )
    maximum_monetary_value: str = field(
        metadata={
            "name": "MaximumMonetaryValue",
            "type": "Element",
            "required": True,
        }
    )
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class NatureOfGoods:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PrimaryReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuantityRange:
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


@dataclass(kw_only=True)
class ReferenceCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RemitToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SealInfo:
    seal_number: str = field(
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


@dataclass(kw_only=True)
class SellerPartNumber:
    part_num: PartNum = field(
        metadata={
            "name": "PartNum",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SellerParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShipFromLocation:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShipFromParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShipToLocation:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShipToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShipToSubLocation:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SoldToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultId:
    class Meta:
        name = "SourcingResultID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultItemId:
    class Meta:
        name = "SourcingResultItemID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultPurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultSummary:
    total_num_sourcing_results: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumSourcingResults",
            "type": "Element",
        }
    )
    total_num_winning_quotes: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumWinningQuotes",
            "type": "Element",
        }
    )
    quote_award_details: List[QuoteAwardDetails] = field(
        default_factory=list,
        metadata={
            "name": "QuoteAwardDetails",
            "type": "Element",
        }
    )
    total_num_participants: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumParticipants",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class StandardPartNumber:
    product_identifier_coded: ProductIdentifierCoded = field(
        metadata={
            "name": "ProductIdentifierCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class StructuredNote:
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )
    note_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoteID",
            "type": "Element",
        }
    )
    agency: Optional[Agency] = field(
        default=None,
        metadata={
            "name": "Agency",
            "type": "Element",
        }
    )
    note_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoteURL",
            "type": "Element",
        }
    )
    text_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextTypeCoded",
            "type": "Element",
        }
    )
    text_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class SupportingReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SupportingSubReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxIdentifier:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxLocation:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxTypeCodedOther:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TermsOfDelivery:
    terms_of_delivery_function_coded: str = field(
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
    shipment_method_of_payment_coded: str = field(
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


@dataclass(kw_only=True)
class UnitPrice:
    unit_price_value: str = field(
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


@dataclass(kw_only=True)
class WarehouseParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BasisMonetaryRange:
    monetary_range: Optional[MonetaryRange] = field(
        default=None,
        metadata={
            "name": "MonetaryRange",
            "type": "Element",
        }
    )
    monetary_limit: Optional[MonetaryLimit] = field(
        default=None,
        metadata={
            "name": "MonetaryLimit",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class Contract:
    contract_id: ContractId = field(
        metadata={
            "name": "ContractID",
            "type": "Element",
            "required": True,
        }
    )
    contract_type: Optional[ContractType] = field(
        default=None,
        metadata={
            "name": "ContractType",
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
    system_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfAttachment:
    attachment: List[Attachment] = field(
        default_factory=list,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfDateCoded:
    date_coded: List[DateCoded] = field(
        default_factory=list,
        metadata={
            "name": "DateCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfDescription:
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfItemCharacteristic:
    item_characteristic: List[ItemCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "ItemCharacteristic",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfRateOfExchangeReference:
    list_of_reference: ListOfReference = field(
        metadata={
            "name": "ListOfReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfSealInfo:
    seal_info: List[SealInfo] = field(
        default_factory=list,
        metadata={
            "name": "SealInfo",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfStructuredNote:
    structured_note: List[StructuredNote] = field(
        default_factory=list,
        metadata={
            "name": "StructuredNote",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ManufacturerPartNumber:
    part_id: str = field(
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


@dataclass(kw_only=True)
class NameValueSet:
    set_name: str = field(
        metadata={
            "name": "SetName",
            "type": "Element",
            "required": True,
        }
    )
    set_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SetID",
            "type": "Element",
        }
    )
    list_of_name_value_pair: ListOfNameValuePair = field(
        metadata={
            "name": "ListOfNameValuePair",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherItemIdentifiers:
    list_of_product_identifier_coded: ListOfProductIdentifierCoded = field(
        metadata={
            "name": "ListOfProductIdentifierCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ParentItemNumber:
    line_item_number_reference: LineItemNumberReference = field(
        metadata={
            "name": "LineItemNumberReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PartyTaxInformation:
    tax_identifier: Optional[TaxIdentifier] = field(
        default=None,
        metadata={
            "name": "TaxIdentifier",
            "type": "Element",
        }
    )
    registered_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegisteredName",
            "type": "Element",
        }
    )
    registered_office: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegisteredOffice",
            "type": "Element",
        }
    )
    tax_location: Optional[TaxLocation] = field(
        default=None,
        metadata={
            "name": "TaxLocation",
            "type": "Element",
        }
    )
    company_registration_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyRegistrationNumber",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Quantity:
    quantity_value: Optional[QuantityValue] = field(
        default=None,
        metadata={
            "name": "QuantityValue",
            "type": "Element",
        }
    )
    quantity_range: Optional[QuantityRange] = field(
        default=None,
        metadata={
            "name": "QuantityRange",
            "type": "Element",
        }
    )
    unit_of_measurement: UnitOfMeasurement = field(
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuantityCoded:
    quantity_value: Optional[QuantityValue] = field(
        default=None,
        metadata={
            "name": "QuantityValue",
            "type": "Element",
        }
    )
    quantity_range: Optional[QuantityRange] = field(
        default=None,
        metadata={
            "name": "QuantityRange",
            "type": "Element",
        }
    )
    unit_of_measurement: UnitOfMeasurement = field(
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
            "required": True,
        }
    )
    quantity_qualifier_coded: str = field(
        metadata={
            "name": "QuantityQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    quantity_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuantityQualifierCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class RatePerUnit:
    unit_price: UnitPrice = field(
        metadata={
            "name": "UnitPrice",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ReferenceCoded:
    reference_type_coded: str = field(
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
    primary_reference: PrimaryReference = field(
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


@dataclass(kw_only=True)
class ShipmentStatusReasons:
    list_of_status_reason: ListOfStatusReason = field(
        metadata={
            "name": "ListOfStatusReason",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SubstitutePartNumbers:
    list_of_product_identifier_coded: ListOfProductIdentifierCoded = field(
        metadata={
            "name": "ListOfProductIdentifierCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Tax:
    tax_function_qualifier_coded: str = field(
        metadata={
            "name": "TaxFunctionQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_function_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxFunctionQualifierCodedOther",
            "type": "Element",
        }
    )
    tax_category_coded: str = field(
        metadata={
            "name": "TaxCategoryCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_category_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxCategoryCodedOther",
            "type": "Element",
        }
    )
    reason_tax_exempt_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonTaxExemptCoded",
            "type": "Element",
        }
    )
    reason_tax_exempt_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonTaxExemptCodedOther",
            "type": "Element",
        }
    )
    tax_type_coded: str = field(
        metadata={
            "name": "TaxTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_type_coded_other: Optional[TaxTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "TaxTypeCodedOther",
            "type": "Element",
        }
    )
    tax_percent: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPercent",
            "type": "Element",
        }
    )
    tax_payment_method_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPaymentMethodCoded",
            "type": "Element",
        }
    )
    tax_payment_method_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPaymentMethodCodedOther",
            "type": "Element",
        }
    )
    taxable_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxableAmount",
            "type": "Element",
        }
    )
    taxable_amount_in_tax_accounting_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxableAmountInTaxAccountingCurrency",
            "type": "Element",
        }
    )
    tax_amount: str = field(
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "required": True,
        }
    )
    tax_amount_in_tax_accounting_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxAmountInTaxAccountingCurrency",
            "type": "Element",
        }
    )
    tax_location: Optional[TaxLocation] = field(
        default=None,
        metadata={
            "name": "TaxLocation",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AllowOrChgDesc:
    ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefID",
            "type": "Element",
        }
    )
    list_of_description: Optional[ListOfDescription] = field(
        default=None,
        metadata={
            "name": "ListOfDescription",
            "type": "Element",
        }
    )
    service_coded: str = field(
        metadata={
            "name": "ServiceCoded",
            "type": "Element",
            "required": True,
        }
    )
    service_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class BasisQuantityRange:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BuyerTaxInformation:
    party_tax_information: PartyTaxInformation = field(
        metadata={
            "name": "PartyTaxInformation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CalculatedPriceBasisQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ContractItem:
    contract: Contract = field(
        metadata={
            "name": "Contract",
            "type": "Element",
            "required": True,
        }
    )
    contract_item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContractItemNumber",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Control:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Emergency:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Flashpoint:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LineItemAttachments:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfNameValueSet:
    name_value_set: List[NameValueSet] = field(
        default_factory=list,
        metadata={
            "name": "NameValueSet",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfOtherDeliveryDate:
    list_of_date_coded: ListOfDateCoded = field(
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfQuantityCoded:
    quantity_coded: List[QuantityCoded] = field(
        default_factory=list,
        metadata={
            "name": "QuantityCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfReferenceCoded:
    reference_coded: List[ReferenceCoded] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfSourcingResultDetailAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MaxBackOrderQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class PackageReference:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
        }
    )
    package_idreference: str = field(
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


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class PriceBasisQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceQuantityRange:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Rate:
    rate_per_unit: RatePerUnit = field(
        metadata={
            "name": "RatePerUnit",
            "type": "Element",
            "required": True,
        }
    )
    unit_price_basis: str = field(
        metadata={
            "name": "UnitPriceBasis",
            "type": "Element",
            "required": True,
        }
    )
    unit_of_measurement: Optional[UnitOfMeasurement] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class RateOfExchangeDetail:
    reference_currency: ReferenceCurrency = field(
        metadata={
            "name": "ReferenceCurrency",
            "type": "Element",
            "required": True,
        }
    )
    target_currency: TargetCurrency = field(
        metadata={
            "name": "TargetCurrency",
            "type": "Element",
            "required": True,
        }
    )
    rate_of_exchange: str = field(
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


@dataclass(kw_only=True)
class SellerTaxInformation:
    party_tax_information: PartyTaxInformation = field(
        metadata={
            "name": "PartyTaxInformation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShipToSubQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
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
    equipment_id: str = field(
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


@dataclass(kw_only=True)
class AllowanceOrChargeDescription:
    allow_or_chg_desc: AllowOrChgDesc = field(
        metadata={
            "name": "AllowOrChgDesc",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class HazardousReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class HazardousTemperatures:
    flashpoint: Optional[Flashpoint] = field(
        default=None,
        metadata={
            "name": "Flashpoint",
            "type": "Element",
        }
    )
    emergency: Optional[Emergency] = field(
        default=None,
        metadata={
            "name": "Emergency",
            "type": "Element",
        }
    )
    control: Optional[Control] = field(
        default=None,
        metadata={
            "name": "Control",
            "type": "Element",
        }
    )
    list_of_temperature_coded: Optional[ListOfTemperatureCoded] = field(
        default=None,
        metadata={
            "name": "ListOfTemperatureCoded",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ItemIdentifiers:
    part_numbers: Optional[PartNumbers] = field(
        default=None,
        metadata={
            "name": "PartNumbers",
            "type": "Element",
        }
    )
    service: Optional[str] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
        }
    )
    item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemDescription",
            "type": "Element",
        }
    )
    list_of_item_characteristic: Optional[ListOfItemCharacteristic] = field(
        default=None,
        metadata={
            "name": "ListOfItemCharacteristic",
            "type": "Element",
        }
    )
    commodity_code: Optional[CommodityCode] = field(
        default=None,
        metadata={
            "name": "CommodityCode",
            "type": "Element",
        }
    )
    category: Optional[Category] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ItemPackagingReference:
    package_reference: List[PackageReference] = field(
        default_factory=list,
        metadata={
            "name": "PackageReference",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfContractItem:
    contract_item: List[ContractItem] = field(
        default_factory=list,
        metadata={
            "name": "ContractItem",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfItemReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfTransportEquipment:
    transport_equipment: List[TransportEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TransportEquipment",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class MonetaryValue:
    monetary_amount: str = field(
        metadata={
            "name": "MonetaryAmount",
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
    rate_of_exchange_detail: Optional[RateOfExchangeDetail] = field(
        default=None,
        metadata={
            "name": "RateOfExchangeDetail",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class OrderParty:
    buyer_party: BuyerParty = field(
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_tax_information: Optional[BuyerTaxInformation] = field(
        default=None,
        metadata={
            "name": "BuyerTaxInformation",
            "type": "Element",
        }
    )
    seller_party: SellerParty = field(
        metadata={
            "name": "SellerParty",
            "type": "Element",
            "required": True,
        }
    )
    seller_tax_information: Optional[SellerTaxInformation] = field(
        default=None,
        metadata={
            "name": "SellerTaxInformation",
            "type": "Element",
        }
    )
    ship_to_party: Optional[ShipToParty] = field(
        default=None,
        metadata={
            "name": "ShipToParty",
            "type": "Element",
        }
    )
    bill_to_party: Optional[BillToParty] = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        }
    )
    remit_to_party: Optional[RemitToParty] = field(
        default=None,
        metadata={
            "name": "RemitToParty",
            "type": "Element",
        }
    )
    ship_from_party: Optional[ShipFromParty] = field(
        default=None,
        metadata={
            "name": "ShipFromParty",
            "type": "Element",
        }
    )
    warehouse_party: Optional[WarehouseParty] = field(
        default=None,
        metadata={
            "name": "WarehouseParty",
            "type": "Element",
        }
    )
    sold_to_party: Optional[SoldToParty] = field(
        default=None,
        metadata={
            "name": "SoldToParty",
            "type": "Element",
        }
    )
    manufacturing_to_party: Optional[ManufacturingToParty] = field(
        default=None,
        metadata={
            "name": "ManufacturingToParty",
            "type": "Element",
        }
    )
    material_issuer: Optional[MaterialIssuer] = field(
        default=None,
        metadata={
            "name": "MaterialIssuer",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Price:
    pricing_type: Optional[PricingType] = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Element",
        }
    )
    unit_price: UnitPrice = field(
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


@dataclass(kw_only=True)
class SourcingResultDates:
    order_dates: OrderDates = field(
        metadata={
            "name": "OrderDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultHeader:
    sourcing_result_purpose: SourcingResultPurpose = field(
        metadata={
            "name": "SourcingResultPurpose",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_issue_date: str = field(
        metadata={
            "name": "SourcingResultIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_id: SourcingResultId = field(
        metadata={
            "name": "SourcingResultID",
            "type": "Element",
            "required": True,
        }
    )
    tracking_id: str = field(
        metadata={
            "name": "TrackingID",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_reference: SourcingCreateReference = field(
        metadata={
            "name": "SourcingCreateReference",
            "type": "Element",
            "required": True,
        }
    )
    initiating_party: Optional[InitiatingParty] = field(
        default=None,
        metadata={
            "name": "InitiatingParty",
            "type": "Element",
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
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
    sourcing_result_list_of_attachment: Optional[SourcingResultListOfAttachment] = field(
        default=None,
        metadata={
            "name": "SourcingResultListOfAttachment",
            "type": "Element",
        }
    )
    sourcing_result_general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingResultGeneralNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Hazardous:
    list_of_hazardous_identifiers: Optional[ListOfHazardousIdentifiers] = field(
        default=None,
        metadata={
            "name": "ListOfHazardousIdentifiers",
            "type": "Element",
        }
    )
    hazard_class_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardClassCoded",
            "type": "Element",
        }
    )
    hazard_class_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardClassCodedOther",
            "type": "Element",
        }
    )
    hazardous_placard_information: Optional[HazardousPlacardInformation] = field(
        default=None,
        metadata={
            "name": "HazardousPlacardInformation",
            "type": "Element",
        }
    )
    hazardous_references: Optional[HazardousReferences] = field(
        default=None,
        metadata={
            "name": "HazardousReferences",
            "type": "Element",
        }
    )
    hazardous_contact: Optional[HazardousContact] = field(
        default=None,
        metadata={
            "name": "HazardousContact",
            "type": "Element",
        }
    )
    hazard_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardNote",
            "type": "Element",
        }
    )
    undgnum: Optional[str] = field(
        default=None,
        metadata={
            "name": "UNDGNum",
            "type": "Element",
        }
    )
    hazardous_temperatures: Optional[HazardousTemperatures] = field(
        default=None,
        metadata={
            "name": "HazardousTemperatures",
            "type": "Element",
        }
    )
    hazardous_shipment_information: Optional[HazardousShipmentInformation] = field(
        default=None,
        metadata={
            "name": "HazardousShipmentInformation",
            "type": "Element",
        }
    )
    emsnum: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMSNum",
            "type": "Element",
        }
    )
    mfag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mfag",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ItemContractReferences:
    list_of_contract_item: ListOfContractItem = field(
        metadata={
            "name": "ListOfContractItem",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfPrice:
    price: List[Price] = field(
        default_factory=list,
        metadata={
            "name": "Price",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class PercentageMonetaryValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuantityMonetaryValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultParty:
    order_party: OrderParty = field(
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SubLocationItemPackagingReference:
    item_packaging_reference: ItemPackagingReference = field(
        metadata={
            "name": "ItemPackagingReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Transport:
    transport_id: str = field(
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


@dataclass(kw_only=True)
class HazardousMaterials:
    hazardous: Hazardous = field(
        metadata={
            "name": "Hazardous",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PercentageAllowanceOrCharge:
    percent_qualifier: PercentQualifier = field(
        metadata={
            "name": "PercentQualifier",
            "type": "Element",
            "required": True,
        }
    )
    percent: str = field(
        metadata={
            "name": "Percent",
            "type": "Element",
            "required": True,
        }
    )
    percentage_monetary_value: Optional[PercentageMonetaryValue] = field(
        default=None,
        metadata={
            "name": "PercentageMonetaryValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class QuantityAllowanceOrCharge:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )
    rate: Rate = field(
        metadata={
            "name": "Rate",
            "type": "Element",
            "required": True,
        }
    )
    quantity_monetary_value: Optional[QuantityMonetaryValue] = field(
        default=None,
        metadata={
            "name": "QuantityMonetaryValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ShipToSubInformation:
    ship_to_sub_location: ShipToSubLocation = field(
        metadata={
            "name": "ShipToSubLocation",
            "type": "Element",
            "required": True,
        }
    )
    ship_to_sub_quantity: ShipToSubQuantity = field(
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


@dataclass(kw_only=True)
class BaseItemDetail:
    line_item_num: LineItemNum = field(
        metadata={
            "name": "LineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    line_item_type: Optional[LineItemType] = field(
        default=None,
        metadata={
            "name": "LineItemType",
            "type": "Element",
        }
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        }
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        }
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        }
    )
    total_quantity: Optional[TotalQuantity] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        }
    )
    max_back_order_quantity: Optional[MaxBackOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        }
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        }
    )
    off_catalog_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        }
    )
    item_contract_references: Optional[ItemContractReferences] = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        }
    )
    list_of_item_references: Optional[ListOfItemReferences] = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        }
    )
    country_of_origin: Optional[CountryOfOrigin] = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        }
    )
    country_of_destination: Optional[CountryOfDestination] = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        }
    )
    final_recipient: Optional[FinalRecipient] = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )
    conditions_of_sale: Optional[ConditionsOfSale] = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        }
    )
    hazardous_materials: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfShipToSubInformation:
    ship_to_sub_information: List[ShipToSubInformation] = field(
        default_factory=list,
        metadata={
            "name": "ShipToSubInformation",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class TypeOfAllowanceOrCharge:
    quantity_allowance_or_charge: Optional[QuantityAllowanceOrCharge] = field(
        default=None,
        metadata={
            "name": "QuantityAllowanceOrCharge",
            "type": "Element",
        }
    )
    percentage_allowance_or_charge: Optional[PercentageAllowanceOrCharge] = field(
        default=None,
        metadata={
            "name": "PercentageAllowanceOrCharge",
            "type": "Element",
        }
    )
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AllowOrCharge:
    seq_no: str = field(
        default="1",
        metadata={
            "name": "SeqNo",
            "type": "Attribute",
            "required": True,
        }
    )
    indicator_coded: str = field(
        metadata={
            "name": "IndicatorCoded",
            "type": "Element",
            "required": True,
        }
    )
    indicator_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndicatorCodedOther",
            "type": "Element",
        }
    )
    basis_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasisCoded",
            "type": "Element",
        }
    )
    basis_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasisCodedOther",
            "type": "Element",
        }
    )
    method_of_handling_coded: str = field(
        metadata={
            "name": "MethodOfHandlingCoded",
            "type": "Element",
            "required": True,
        }
    )
    method_of_handling_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodOfHandlingCodedOther",
            "type": "Element",
        }
    )
    allowance_or_charge_description: AllowanceOrChargeDescription = field(
        metadata={
            "name": "AllowanceOrChargeDescription",
            "type": "Element",
            "required": True,
        }
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )
    basis_quantity_range: Optional[BasisQuantityRange] = field(
        default=None,
        metadata={
            "name": "BasisQuantityRange",
            "type": "Element",
        }
    )
    basis_monetary_range: Optional[BasisMonetaryRange] = field(
        default=None,
        metadata={
            "name": "BasisMonetaryRange",
            "type": "Element",
        }
    )
    type_of_allowance_or_charge: TypeOfAllowanceOrCharge = field(
        metadata={
            "name": "TypeOfAllowanceOrCharge",
            "type": "Element",
            "required": True,
        }
    )
    tax: List[Tax] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
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
    quantity: Quantity = field(
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
        }
    )
    transport_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportReference",
            "type": "Element",
        }
    )
    list_of_ship_to_sub_information: Optional[ListOfShipToSubInformation] = field(
        default=None,
        metadata={
            "name": "ListOfShipToSubInformation",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfAllowOrCharge:
    allow_or_charge: List[AllowOrCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowOrCharge",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfScheduleLine:
    schedule_line: List[ScheduleLine] = field(
        default_factory=list,
        metadata={
            "name": "ScheduleLine",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class ItemAllowancesOrCharges:
    list_of_allow_or_charge: ListOfAllowOrCharge = field(
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PricingDetail:
    list_of_price: ListOfPrice = field(
        metadata={
            "name": "ListOfPrice",
            "type": "Element",
            "required": True,
        }
    )
    tax: List[Tax] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
        }
    )
    item_allowances_or_charges: Optional[ItemAllowancesOrCharges] = field(
        default=None,
        metadata={
            "name": "ItemAllowancesOrCharges",
            "type": "Element",
        }
    )
    total_value: Optional[TotalValue] = field(
        default=None,
        metadata={
            "name": "TotalValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ItemDetail:
    base_item_detail: BaseItemDetail = field(
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    pricing_detail: Optional[PricingDetail] = field(
        default=None,
        metadata={
            "name": "PricingDetail",
            "type": "Element",
        }
    )
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
        }
    )
    round_trip_information: Optional[RoundTripInformation] = field(
        default=None,
        metadata={
            "name": "RoundTripInformation",
            "type": "Element",
        }
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        }
    )
    line_item_attachments: Optional[LineItemAttachments] = field(
        default=None,
        metadata={
            "name": "LineItemAttachments",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class SourcingResultItem:
    item_detail: ItemDetail = field(
        metadata={
            "name": "ItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfSourcingResultItem:
    sourcing_result_item: List[SourcingResultItem] = field(
        default_factory=list,
        metadata={
            "name": "SourcingResultItem",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class SourcingResultDetail:
    sourcing_result_item_id: SourcingResultItemId = field(
        metadata={
            "name": "SourcingResultItemID",
            "type": "Element",
            "required": True,
        }
    )
    winning_quote_indicator: str = field(
        metadata={
            "name": "WinningQuoteIndicator",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_party: SourcingResultParty = field(
        metadata={
            "name": "SourcingResultParty",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_dates: Optional[SourcingResultDates] = field(
        default=None,
        metadata={
            "name": "SourcingResultDates",
            "type": "Element",
        }
    )
    sourcing_result_currency: Optional[SourcingResultCurrency] = field(
        default=None,
        metadata={
            "name": "SourcingResultCurrency",
            "type": "Element",
        }
    )
    list_of_sourcing_result_item: ListOfSourcingResultItem = field(
        metadata={
            "name": "ListOfSourcingResultItem",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_detail_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingResultDetailNotes",
            "type": "Element",
        }
    )
    list_of_sourcing_result_detail_attachment: Optional[ListOfSourcingResultDetailAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingResultDetailAttachment",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfSourcingResultDetail:
    sourcing_result_detail: List[SourcingResultDetail] = field(
        default_factory=list,
        metadata={
            "name": "SourcingResultDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class SourcingResult:
    sourcing_result_header: SourcingResultHeader = field(
        metadata={
            "name": "SourcingResultHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_sourcing_result_detail: ListOfSourcingResultDetail = field(
        metadata={
            "name": "ListOfSourcingResultDetail",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_summary: SourcingResultSummary = field(
        metadata={
            "name": "SourcingResultSummary",
            "type": "Element",
            "required": True,
        }
    )
