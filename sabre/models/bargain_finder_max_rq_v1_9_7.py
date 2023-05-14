from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDuration
from sabre.models.bargain_finder_max_common_types_v1_9_7 import (
    AdvResTicketingType,
    AirTripType,
    CompanyNameType,
    DepartureOrArrival,
    EquipmentType,
    OtaAirLowFareSearchRqTarget,
    OtaAirLowFareSearchRqTransactionStatusCode,
    OutboundOrInbound,
    PassengerTypeQuantityType,
    StayRestrictionsType,
    VoluntaryChangesType,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class AddressTypeShareMarketInd(Enum):
    """
    Value="Inherit" Permission for sharing data for marketing purposes.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


class AddressTypeShareSynchInd(Enum):
    """
    Value="Inherit" Permission for sharing data for synchronization of information
    held by other travel service providers.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


class AirTravelerTypeGender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    UNKNOWN = "Unknown"


class AirTravelerTypeShareMarketInd(Enum):
    """
    Value="Inherit" Permission for sharing data for marketing purposes.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


class AirTravelerTypeShareSynchInd(Enum):
    """
    Value="Inherit" Permission for sharing data for synchronization of information
    held by other travel service providers.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


@dataclass
class AirlineType:
    """
    Attributes
        operating: Operating airline code
        marketing: Marketing airline code
    """
    operating: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operating",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
    marketing: Optional[str] = field(
        default=None,
        metadata={
            "name": "Marketing",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )


@dataclass
class AllianceType:
    """
    Attributes
        code: Identifies an alliance by the alliance code.
    """
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )


class AltCitiesCombinationsLocationsType(Enum):
    ALL = "All"
    MAIN = "Main"


@dataclass
class ApplyResidentDiscountType:
    """
    Apply resident discount in CLFE.
    """
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AwardShoppingType:
    """
    Attributes
        enable: Enable award shopping.
        use_ras: Use Redemption Availability Service
    """
    enable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Enable",
            "type": "Attribute",
        }
    )
    use_ras: bool = field(
        default=False,
        metadata={
            "name": "UseRAS",
            "type": "Attribute",
        }
    )


@dataclass
class BillingInformationType:
    user_station: int = field(
        default=0,
        metadata={
            "name": "UserStation",
            "type": "Attribute",
        }
    )
    user_branch: int = field(
        default=0,
        metadata={
            "name": "UserBranch",
            "type": "Attribute",
        }
    )
    partition_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartitionID",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,4}",
        }
    )
    user_set_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserSetAddress",
            "type": "Attribute",
            "pattern": r"[0-9A-F]{6}",
        }
    )
    aaacity: Optional[str] = field(
        default=None,
        metadata={
            "name": "AAACity",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    agent_sine_in: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentSineIn",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceName",
            "type": "Attribute",
            "pattern": r"[0-9a-zA-Z,]{1,8}",
        }
    )
    action_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActionCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )


@dataclass
class BookingChannelType:
    """
    Specifies the booking channel types and whether it is the primary means of
    connectivity of the source.

    Attributes
        type: The type of booking channel (e.g. Global Distribution
            System (GDS), Alternative Distribution System (ADS), Sales
            and Catering System (SCS), Property Management System (PMS),
            Central Reservation System (CRS), Tour Operator System
            (TOS), Internet and ALL). Refer to OTA Code List Booking
            Channel Type (BCT).
        primary: Indicates whether the enumerated booking channel is the
            primary means of connectivity used by the source.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    primary: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Primary",
            "type": "Attribute",
        }
    )


@dataclass
class BrandType:
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )


class CabinType(Enum):
    """
    A cabin is either Premium First (P), First (F), Premium Business (J), Business
    (C), Premium Economy (S) or Economy (Y)
    """
    PREMIUM_FIRST = "PremiumFirst"
    FIRST = "First"
    PREMIUM_BUSINESS = "PremiumBusiness"
    BUSINESS = "Business"
    PREMIUM_ECONOMY = "PremiumEconomy"
    ECONOMY = "Economy"
    Y = "Y"
    S = "S"
    C = "C"
    J = "J"
    F = "F"
    P = "P"


@dataclass
class CachePartitionType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z0-9_]{1,}",
        }
    )


class CarrierType(Enum):
    """
    Used to specify if carrier type is  marketing or operating.
    """
    MARKETING = "Marketing"
    OPERATING = "Operating"


class ConnectionLocationConnectionInfo(Enum):
    """
    Attributes
        VIA: Location without stopping or changing.
        STOP: Location is for stopping.
        CHANGE: Location is for changing.
    """
    VIA = "Via"
    STOP = "Stop"
    CHANGE = "Change"


class ContentTypeType(Enum):
    AIR = "Air"
    RAIL = "Rail"


@dataclass
class CountryNameType:
    """
    The name or code of a country (e.g. as used in an address or to specify
    citizenship of a traveller).

    Attributes
        value:
        code: ISO 3166 code for a country.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 64,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{2}",
        }
    )


class CustLoyaltyTypeShareMarketInd(Enum):
    """
    Value="Inherit" Permission for sharing data for marketing purposes.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


class CustLoyaltyTypeShareSynchInd(Enum):
    """
    Value="Inherit" Permission for sharing data for synchronization of information
    held by other travel service providers.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


class CustLoyaltyTypeSingleVendorInd(Enum):
    SINGLE_VNDR = "SingleVndr"
    ALLIANCE = "Alliance"


class CustomerTypeValue(Enum):
    """
    Attributes
        REGULAR: Regular customer type.
        TVLYPREF: TVLY_PREFERRED customer type.
        PREFELITE: PREFERED_ELITE customer type.
        LOYALTY: LOYALTY customer type.
    """
    REGULAR = "REGULAR"
    TVLYPREF = "TVLYPREF"
    PREFELITE = "PREFELITE"
    LOYALTY = "LOYALTY"


@dataclass
class DateRangeType:
    """
    Attributes
        outbound_date: Outbound date
        date_range: Number of date range
    """
    outbound_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OutboundDate",
            "type": "Attribute",
        }
    )
    date_range: Optional[int] = field(
        default=None,
        metadata={
            "name": "DateRange",
            "type": "Attribute",
        }
    )


@dataclass
class DateTimeType:
    """
    Attributes
        time_window_start: Allowed amount of time before specified time.
        time_window_end: Allowed amount of time after specified time.
        time_tolerance: Maximum time difference between actual and
            desired time.
        date_flexibility: The number of alternate days around the travel
            date to search.
        max_options_per_date: Number of options for requested date.
        connection_time_min: Minimal amount of time between flights
        connection_time_max: Maximal amount of time between flights
    """
    time_window_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeWindowStart",
            "type": "Attribute",
            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
        }
    )
    time_window_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeWindowEnd",
            "type": "Attribute",
            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
        }
    )
    time_tolerance: Optional[int] = field(
        default=None,
        metadata={
            "name": "TimeTolerance",
            "type": "Attribute",
        }
    )
    date_flexibility: Optional[int] = field(
        default=None,
        metadata={
            "name": "DateFlexibility",
            "type": "Attribute",
        }
    )
    max_options_per_date: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOptionsPerDate",
            "type": "Attribute",
        }
    )
    connection_time_min: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConnectionTimeMin",
            "type": "Attribute",
        }
    )
    connection_time_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConnectionTimeMax",
            "type": "Attribute",
        }
    )


@dataclass
class DepartureDaysType:
    """
    Specify which days of week  to consider for departure.

    Attributes
        value: Value format: First letter of the name of the day or '_',
            eg. 'SMT___S' means we are interested in departing at
            Saturday, Sunday, Monday or Tuesday. Even if there are
            schedules for Wednesday, Thursday or Friday, they won't be
            returned in ISell response.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "length": 7,
        }
    )


class DocumentTypeGender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    UNKNOWN = "Unknown"


class DocumentTypeShareMarketInd(Enum):
    """
    Value="Inherit" Permission for sharing data for marketing purposes.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


class DocumentTypeShareSynchInd(Enum):
    """
    Value="Inherit" Permission for sharing data for synchronization of information
    held by other travel service providers.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


class EmailTypeShareMarketInd(Enum):
    """
    Value="Inherit" Permission for sharing data for marketing purposes.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


class EmailTypeShareSynchInd(Enum):
    """
    Value="Inherit" Permission for sharing data for synchronization of information
    held by other travel service providers.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


@dataclass
class ExchangeFareType:
    """
    Attributes
        base_fare_amount: Base fare amount
        non_refundable_amount: Non-refundable Base Fare Amount. Currency
            is defined by @BaseFareCurrency.
        base_fare_currency: Base fare currency
        fare_calc_currency: Fare calc currency
        validating_carrier: Validating carrier
        roe: Rate of Exchange override (note: doesn't need to be
            specified if FareCalc currency and BaseFare currency is the
            same).
    """
    base_fare_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BaseFareAmount",
            "type": "Attribute",
            "required": True,
            "fraction_digits": 3,
        }
    )
    non_refundable_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NonRefundableAmount",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )
    base_fare_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseFareCurrency",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    fare_calc_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareCalcCurrency",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    validating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidatingCarrier",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
    roe: Optional[float] = field(
        default=None,
        metadata={
            "name": "ROE",
            "type": "Attribute",
        }
    )


class ExchangeSettingsTypeReissueExchange(Enum):
    A = "A"


class ExchangeSettingsTypeRequestType(Enum):
    BASIC = "basic"
    CONTEXT = "context"


@dataclass
class FareDetailsType:
    """You don't need to specify all of these attributes for a given flight.

    For some of them it is sufficient to be specified in the last flight
    of a given fare component. For details, see notes below --- the
    attributes are annotated with ,,last Flight in Fare Component''.

    Attributes
        component_no: Fare component number
        basis_code: Fare basis code
        amount: Fare amount (note: last Flight in Fare Component)
        vendor: Vendor (note: last Flight in Fare Component)
        source_vendor: Fare Source Vendor (note: last Flight in Fare
            Component)
        tariff: Tariff (note: last Flight in Fare Component)
        rule_number: Rule Number (note: last Flight in Fare Component)
        brand_id: Used to indicate brand code
        program_id:
    """
    component_no: Optional[int] = field(
        default=None,
        metadata={
            "name": "ComponentNo",
            "type": "Attribute",
            "required": True,
        }
    )
    basis_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasisCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "pattern": r"[A-Z0-9]+(/[A-Z0-9]+)?",
        }
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )
    vendor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Attribute",
        }
    )
    source_vendor: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceVendor",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
    tariff: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tariff",
            "type": "Attribute",
        }
    )
    rule_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleNumber",
            "type": "Attribute",
        }
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    program_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProgramID",
            "type": "Attribute",
        }
    )


@dataclass
class FareOptionalDetailsType:
    """You don't need to specify all of these attributes for a given flight.

    For some of them it is sufficient to be specified in the last flight
    of a given fare component. For details, see notes below --- the
    attributes are annotated with ,,last Flight in Fare Component''.

    Attributes
        component_no: Fare component number
        basis_code: Fare basis code
        amount: Fare amount (note: last Flight in Fare Component)
        vendor: Vendor (note: last Flight in Fare Component)
        source_vendor: Fare Source Vendor (note: last Flight in Fare
            Component)
        tariff: Tariff (note: last Flight in Fare Component)
        rule_number: Rule Number (note: last Flight in Fare Component)
        brand_id: Used to indicate brand code
        program_id:
    """
    component_no: Optional[int] = field(
        default=None,
        metadata={
            "name": "ComponentNo",
            "type": "Attribute",
        }
    )
    basis_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasisCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 15,
            "pattern": r"[A-Z0-9]+(/[A-Z0-9]+)?",
        }
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )
    vendor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Attribute",
        }
    )
    source_vendor: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceVendor",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
    tariff: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tariff",
            "type": "Attribute",
        }
    )
    rule_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleNumber",
            "type": "Attribute",
        }
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    program_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProgramID",
            "type": "Attribute",
        }
    )


@dataclass
class FlightStopsAsConnectionsType:
    """
    Treat all stops as connections.
    """
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Attribute",
            "required": True,
        }
    )


class FlightTypeType(Enum):
    """Identifies a particular type of flight - Direct, Stopover etc.

    Attributes
        NONSTOP: Flight without plane change and without intermediate
            landing.
        DIRECT: Flight without plane change and possible intermediate
            landing.
        CONNECTION: Flight with plane changes, allowing maximum of 24
            hours for each change
    """
    NONSTOP = "Nonstop"
    DIRECT = "Direct"
    CONNECTION = "Connection"


@dataclass
class GoverningCarrierOverrideType:
    """
    Attributes
        airline_code: Airline Carrier Code - override the GOVERNING
            CARRIER to get the fare filed by that carrier.
    """
    airline_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirlineCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )


@dataclass
class IncludeVendorPrefType:
    """
    Consider only these carriers for this leg.

    Attributes
        code: Identifies a company by the company code.
    """
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )


@dataclass
class JumpCabinLogicType:
    """
    Attributes
        disabled: Controls if response could contain options with cabin
            class different than requested.
    """
    disabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Disabled",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class KeepSameCabinType:
    """
    Attributes
        enabled: Set to "true" guarantees that all segments within
            single shopping option belong to the requested cabin.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Enabled",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MileageDisplayType:
    """
    Attributes
        type: Mileage display type
        city: Mileage display city
        surcharge: Mileage surcharge percentage
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    surcharge: Optional[int] = field(
        default=None,
        metadata={
            "name": "Surcharge",
            "type": "Attribute",
        }
    )


class MultiTicketDisplayPolicy(Enum):
    SOW = "SOW"
    GOW2_RT = "GOW2RT"
    SCHS = "SCHS"


@dataclass
class NumTripsType:
    """
    This element allows a user to specify the number of itineraries returned.

    Attributes
        number:
        per_date_min: Minimum number of options to be retrieved for each
            combination of outbound/inbound dates.
        per_date_max: Maximum number of options to be retrieved for each
            combination of outbound/inbound dates.
        per_market: Number of itineraries per market for alternate
            cities request. It allows to control market diversity only.
        per_month: In Advanced Calendar API: Maximum number of
            itineraries to be retrieved for each departure month and
            departure/arrival combination.
    """
    number: int = field(
        default=9,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
    per_date_min: Optional[int] = field(
        default=None,
        metadata={
            "name": "PerDateMin",
            "type": "Attribute",
        }
    )
    per_date_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "PerDateMax",
            "type": "Attribute",
        }
    )
    per_market: Optional[int] = field(
        default=None,
        metadata={
            "name": "PerMarket",
            "type": "Attribute",
        }
    )
    per_month: Optional[int] = field(
        default=None,
        metadata={
            "name": "PerMonth",
            "type": "Attribute",
        }
    )


@dataclass
class OptionsPerDatePairType:
    """
    Attributes
        departure: Departure date
        return_value: Return date
        min: Minimum number of options per date/date pair
        max: Maximum number of options per date/date pair
    """
    departure: Optional[str] = field(
        default=None,
        metadata={
            "name": "Departure",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
        }
    )
    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Return",
            "type": "Attribute",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
        }
    )
    min: Optional[int] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Attribute",
            "required": True,
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Attribute",
            "required": True,
        }
    )


class PassengerStatusType(Enum):
    """
    Attributes
        R: Residency.
        E: Employment.
        N: Nationality.
    """
    R = "R"
    E = "E"
    N = "N"


class PersonNameTypeShareMarketInd(Enum):
    """
    Value="Inherit" Permission for sharing data for marketing purposes.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


class PersonNameTypeShareSynchInd(Enum):
    """
    Value="Inherit" Permission for sharing data for synchronization of information
    held by other travel service providers.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


@dataclass
class PlusUpType:
    """
    Attributes
        amount: Amount
        origin_city: Origin City
        destination_city: Destination City
        fare_origin_city: Fare Origin City
        fare_destination_city: Fare Destination City
        via_city: Via City
        message: Message
        country_of_payment: Country of payment
    """
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
            "fraction_digits": 3,
        }
    )
    origin_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginCity",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    destination_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationCity",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    fare_origin_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareOriginCity",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    fare_destination_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareDestinationCity",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    via_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "ViaCity",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
        }
    )
    country_of_payment: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryOfPayment",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{2}",
        }
    )


@dataclass
class PointOfSaleOverrideType:
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )


@dataclass
class PointOfTicketingOverrideType:
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )


@dataclass
class PositionType:
    """
    Used to identify geospatial postion of the requesting entity.
    """
    latitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    longitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    altitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "Altitude",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )


class PreferLevelType(Enum):
    """
    Used to specify a preference level for something that is or will be requested
    (e.g. a supplier of a service, a type of service, a form of payment, etc.).
    """
    ONLY = "Only"
    UNACCEPTABLE = "Unacceptable"
    PREFERRED = "Preferred"


@dataclass
class RequestLocationType:
    """
    Code and optional string to describe a location point.

    Attributes
        value:
        location_code: Location identifying code. Required unless
            AirportsGroup or AllAirports is specified. Cannot appear
            with AirportsGroup nor AllAirports.
        airports_group: Name of the airports group
        code_context: Identifies the context of the identifying code,
            such as IATA, ARC, or internal code, etc.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationCode",
            "type": "Attribute",
            "pattern": r"[A-Z]{1,8}",
        }
    )
    airports_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirportsGroup",
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9]{1,40}",
        }
    )
    code_context: str = field(
        default="IATA",
        metadata={
            "name": "CodeContext",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )


class RequestPricingSourceType(Enum):
    """
    It can be used to indicate whether the fare is public or private.
    """
    PUBLISHED = "Published"
    PRIVATE = "Private"
    BOTH = "Both"


@dataclass
class ReservationType:
    """
    Attributes
        status: Reservation status
        real_status: Real reservation status
    """
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "pattern": r"[A-Z]{1,2}",
        }
    )
    real_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "RealStatus",
            "type": "Attribute",
            "pattern": r"[A-Z]{1,2}",
        }
    )


@dataclass
class RetailerRulesType:
    """
    Attributes
        retailer_rule:
        force: If set to true, only fares with a matched Business Rule
            containing the specified Retailer Rule Qualifier will be
            returned
    """
    retailer_rule: List["RetailerRulesType.RetailerRule"] = field(
        default_factory=list,
        metadata={
            "name": "RetailerRule",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 4,
        }
    )
    force: bool = field(
        default=False,
        metadata={
            "name": "Force",
            "type": "Attribute",
        }
    )

    @dataclass
    class RetailerRule:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9a-zA-Z]{2,20}",
            }
        )


@dataclass
class RoutingLegType:
    """
    Definition of individual routing legs, at least one leg must be present.
    """
    inbound_outbound_carrier: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InboundOutboundCarrier",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"\*|[A-Z][A-Z0-9]{1}|[A-Z0-9][A-Z][A-Z0-9]?",
        }
    )
    inbound_carrier: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InboundCarrier",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"\*|[A-Z][A-Z0-9]{1}|[A-Z0-9][A-Z][A-Z0-9]?",
        }
    )
    outbound_carrier: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OutboundCarrier",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"\*|[A-Z][A-Z0-9]{1}|[A-Z0-9][A-Z][A-Z0-9]?",
        }
    )
    connect_point: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ConnectPoint",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"\*|\?|\+|\.|[A-Z]{3,5}",
        }
    )


@dataclass
class SeatStatusSimType:
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    command: Optional[str] = field(
        default=None,
        metadata={
            "name": "Command",
            "type": "Attribute",
        }
    )


class SegmentTypeCode(Enum):
    """
    Attributes
        ARUNK: Arrival unknown
        O: Normal
        X: Connection. Collapses this and subsequent
            OriginDestinationInformation so that they are treated as
            single leg.
    """
    ARUNK = "ARUNK"
    O = "O"
    X = "X"


@dataclass
class SideTripType:
    """
    Attributes
        number: Side trip number
        start: Side trip start
        end: Side trip end
    """
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        }
    )
    start: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Attribute",
        }
    )
    end: Optional[bool] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Attribute",
        }
    )


class SpanishFamilyDiscountLevel(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class StateProvType:
    """
    State, province, or region name or code needed to identify location.

    Attributes
        value:
        state_code: The postal service standard code or abbreviation for
            the state, province, or region.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 64,
        }
    )
    state_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "StateCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 8,
        }
    )


@dataclass
class StreetNmbrType:
    """
    Street name; number on street.

    Attributes
        value:
        po_box: Defines a Post Office Box number.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 64,
        }
    )
    po_box: Optional[str] = field(
        default=None,
        metadata={
            "name": "PO_Box",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )


@dataclass
class TaxCodeType:
    """
    Defines the data fields available for tax code.

    Attributes
        tax_code: Identifies the code for the tax.
    """
    tax_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z0-9]{2}[A-Z0-9]{0,1}",
        }
    )


class TelephoneTypeShareMarketInd(Enum):
    """
    Value="Inherit" Permission for sharing data for marketing purposes.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


class TelephoneTypeShareSynchInd(Enum):
    """
    Value="Inherit" Permission for sharing data for synchronization of information
    held by other travel service providers.
    """
    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"


@dataclass
class TravelDateTimeType:
    """
    Date and time of trip, that allows specifying a time window before and after
    the given date.

    Attributes
        departure_date_time: This date should be of the form YYYY-MM-
            DDTHH:MM:SS
        arrival_date_time: This date should be of the form YYYY-MM-
            DDTHH:MM:SS
        departure_dates:
        arrival_dates: Allowed only for Advanced Calendar API.
        departure_window: This should be of the form HHMMHHMM.
        arrival_window: This should be of the form HHMMHHMM.
    """
    departure_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureDateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}",
        }
    )
    arrival_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalDateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}",
        }
    )
    departure_dates: Optional["TravelDateTimeType.DepartureDates"] = field(
        default=None,
        metadata={
            "name": "DepartureDates",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    arrival_dates: Optional["TravelDateTimeType.ArrivalDates"] = field(
        default=None,
        metadata={
            "name": "ArrivalDates",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    departure_window: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureWindow",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"([0-2][0-9][0-5][0-9]){2}",
        }
    )
    arrival_window: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalWindow",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"([0-2][0-9][0-5][0-9]){2}",
        }
    )

    @dataclass
    class DepartureDates:
        """
        Attributes
            day:
            days_range:
            length_of_stay: Amount of days between previous leg's
                DEPARTURE date and current leg's DEPARTURE date. NOTE:
                Allowed only in 2nd or further
                "OriginDestinationInformation". Example: for outbound
                departing on Jan 20, LengthOfStay/@Days="2" means
                inbound departing on Jan 22.
            length_of_stay_range: See comment on "LengthOfStay" element.
        """
        day: List["TravelDateTimeType.DepartureDates.Day"] = field(
            default_factory=list,
            metadata={
                "name": "Day",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "sequence": 1,
            }
        )
        days_range: List["TravelDateTimeType.DepartureDates.DaysRange"] = field(
            default_factory=list,
            metadata={
                "name": "DaysRange",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "sequence": 1,
            }
        )
        length_of_stay: List["TravelDateTimeType.DepartureDates.LengthOfStay"] = field(
            default_factory=list,
            metadata={
                "name": "LengthOfStay",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        length_of_stay_range: List["TravelDateTimeType.DepartureDates.LengthOfStayRange"] = field(
            default_factory=list,
            metadata={
                "name": "LengthOfStayRange",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class LengthOfStay:
            days: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Days",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class LengthOfStayRange:
            """
            Attributes
                min_days: (inclusive)
                max_days: (inclusive)
            """
            min_days: Optional[int] = field(
                default=None,
                metadata={
                    "name": "MinDays",
                    "type": "Attribute",
                    "required": True,
                }
            )
            max_days: Optional[int] = field(
                default=None,
                metadata={
                    "name": "MaxDays",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class Day:
            date: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Date",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )

        @dataclass
        class DaysRange:
            from_date: Optional[str] = field(
                default=None,
                metadata={
                    "name": "FromDate",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )
            to_date: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ToDate",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )
            week_days: Optional[str] = field(
                default=None,
                metadata={
                    "name": "WeekDays",
                    "type": "Attribute",
                    "pattern": r"[S_][M_][T_][W_][T_][F_][S_]",
                }
            )

    @dataclass
    class ArrivalDates:
        day: List["TravelDateTimeType.ArrivalDates.Day"] = field(
            default_factory=list,
            metadata={
                "name": "Day",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        days_range: List["TravelDateTimeType.ArrivalDates.DaysRange"] = field(
            default_factory=list,
            metadata={
                "name": "DaysRange",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class Day:
            date: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Date",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )

        @dataclass
        class DaysRange:
            from_date: Optional[str] = field(
                default=None,
                metadata={
                    "name": "FromDate",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )
            to_date: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ToDate",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )
            week_days: Optional[str] = field(
                default=None,
                metadata={
                    "name": "WeekDays",
                    "type": "Attribute",
                    "pattern": r"[S_][M_][T_][W_][T_][F_][S_]",
                }
            )


@dataclass
class TravelerInfoSummaryTpaExtensionsType:
    """
    Attributes
        traveler_rating: Customer Value Scores and Frequent Flyer Tiers
            for one traveler. It can influence Availability results when
            provided.
    """
    class Meta:
        name = "TravelerInfoSummary_TPA_ExtensionsType"

    traveler_rating: List["TravelerInfoSummaryTpaExtensionsType.TravelerRating"] = field(
        default_factory=list,
        metadata={
            "name": "TravelerRating",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )

    @dataclass
    class TravelerRating:
        score: List["TravelerInfoSummaryTpaExtensionsType.TravelerRating.Score"] = field(
            default_factory=list,
            metadata={
                "name": "Score",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        frequent_flyer: List["TravelerInfoSummaryTpaExtensionsType.TravelerRating.FrequentFlyer"] = field(
            default_factory=list,
            metadata={
                "name": "FrequentFlyer",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class Score:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )
            carrier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Carrier",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class FrequentFlyer:
            tier: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Tier",
                    "type": "Attribute",
                    "required": True,
                }
            )
            carrier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Carrier",
                    "type": "Attribute",
                    "required": True,
                }
            )


@dataclass
class TravelerRefNumberType:
    """
    A reference place holder used as a pointer to link back to the traveler.

    Attributes
        rph: Reference place holder.
    """
    rph: Optional[str] = field(
        default=None,
        metadata={
            "name": "RPH",
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}",
        }
    )


class ValidatingCarrierPreferLevelType(Enum):
    """Used to specify a preference level for ValidatingCarrier.

    For adding new enums see PreferLevelType.
    """
    UNACCEPTABLE = "Unacceptable"
    PREFERRED = "Preferred"


@dataclass
class XofaresType:
    """
    XOFares indicator.
    """
    class Meta:
        name = "XOFaresType"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AddressType:
    """
    Attributes
        street_nmbr: Street Name and Number within the address
        bldg_room: Building name, room, apartment, or suite number.
        address_line:
        city_name: City name eg. Dublin
        postal_code: Post Office Code number.
        county: County Name eg. Fairfax
        state_prov: State name eg. Texas
        country_name: Country name eg. Ireland
        formatted_ind: Specifies if the associated data is formatted or
            not. If true, then it is formatted, if false, then not
            formatted.
        share_synch_ind:
        share_market_ind:
        type: Defines the type of address (e.g. home, business, other).
            Refer to OTA Code List Communication Location Type (CLT).
    """
    street_nmbr: Optional[StreetNmbrType] = field(
        default=None,
        metadata={
            "name": "StreetNmbr",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    bldg_room: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgRoom",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 0,
            "max_length": 64,
        }
    )
    address_line: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 64,
        }
    )
    city_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 64,
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 16,
        }
    )
    county: Optional[str] = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 32,
        }
    )
    state_prov: Optional[StateProvType] = field(
        default=None,
        metadata={
            "name": "StateProv",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    country_name: Optional[CountryNameType] = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    formatted_ind: bool = field(
        default=False,
        metadata={
            "name": "FormattedInd",
            "type": "Attribute",
        }
    )
    share_synch_ind: Optional[AddressTypeShareSynchInd] = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        }
    )
    share_market_ind: Optional[AddressTypeShareMarketInd] = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class AltCitiesCombinationsType:
    """
    Which (if any) alt cities locations should be handled in a special way (i.e.
    Validate instead of precomputed path).

    Attributes
        origins: Which origins to process in live path (All or Main
            only)
        destinations: Which destinations to process in live path (All or
            Main only)
    """
    origins: AltCitiesCombinationsLocationsType = field(
        default=AltCitiesCombinationsLocationsType.MAIN,
        metadata={
            "name": "Origins",
            "type": "Attribute",
        }
    )
    destinations: AltCitiesCombinationsLocationsType = field(
        default=AltCitiesCombinationsLocationsType.MAIN,
        metadata={
            "name": "Destinations",
            "type": "Attribute",
        }
    )


@dataclass
class ArunkType:
    """
    Attributes
        origin_location: Origin code
        destination_location: Destination code
        side_trip: Side trip information
    """
    origin_location: Optional[RequestLocationType] = field(
        default=None,
        metadata={
            "name": "OriginLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    destination_location: Optional[RequestLocationType] = field(
        default=None,
        metadata={
            "name": "DestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    side_trip: Optional[SideTripType] = field(
        default=None,
        metadata={
            "name": "SideTrip",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )


@dataclass
class BookingClassPrefType:
    """
    Booking class code and preference level for specifying booking classes
    preferred/not preferred in a request.

    Attributes
        res_book_desig_code: Booking class code
        prefer_level:
    """
    res_book_desig_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResBookDesigCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{1,2}",
        }
    )
    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        }
    )


@dataclass
class CabinPrefType:
    """
    Indicates preferences for choice of airline cabin for a given travel situation.

    Attributes
        prefer_level:
        cabin: Specify cabin type.
    """
    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        }
    )
    cabin: Optional[CabinType] = field(
        default=None,
        metadata={
            "name": "Cabin",
            "type": "Attribute",
        }
    )


@dataclass
class CachePartitionGroupType:
    partition: List[CachePartitionType] = field(
        default_factory=list,
        metadata={
            "name": "Partition",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 2,
        }
    )


@dataclass
class CompanyNamePrefType(CompanyNameType):
    """
    Identifies a preferred company by name.

    Attributes
        prefer_level:
        type: Specify what type  of carrier it comes to.
    """
    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        }
    )
    type: Optional[CarrierType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class ConnectionType:
    """
    To specify connection locations, preference level for each, min connection
    time, and whether location is specified for stopping or changing.
    """
    connection_location: List["ConnectionType.ConnectionLocation"] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 9,
        }
    )

    @dataclass
    class ConnectionLocation(RequestLocationType):
        """
        Attributes
            inclusive:
            prefer_level:
            min_change_time: Number of minutes between connections.
            connection_info:
        """
        inclusive: bool = field(
            default=True,
            metadata={
                "name": "Inclusive",
                "type": "Attribute",
            }
        )
        prefer_level: PreferLevelType = field(
            default=PreferLevelType.PREFERRED,
            metadata={
                "name": "PreferLevel",
                "type": "Attribute",
            }
        )
        min_change_time: Optional[int] = field(
            default=None,
            metadata={
                "name": "MinChangeTime",
                "type": "Attribute",
            }
        )
        connection_info: Optional[ConnectionLocationConnectionInfo] = field(
            default=None,
            metadata={
                "name": "ConnectionInfo",
                "type": "Attribute",
            }
        )


@dataclass
class CustLoyaltyType:
    """
    Program rewarding frequent use by accumulating credits for services provided by
    vendors.

    Attributes
        share_synch_ind:
        share_market_ind:
        program_id: Identifier to indicate the company owner of the
            loyalty program.
        membership_id: Unique identifier of the member in the program
            (membership number, account number, etc.).
        travel_sector: Identifies the travel sector. Refer to OTA Code
            List Travel Sector (TVS).
        loyal_level: Indicates special privileges in program assigned to
            individual.
        single_vendor_ind: Indicates if program is affiliated with a
            group of related offers accumulating credits.
        signup_date: Indicates when the member signed up for the loyalty
            program.
        effective_date: Indicates the starting date.
        expire_date: Indicates the ending date.
        rph: Reference place holder, to reference it back in the
            response.
    """
    share_synch_ind: Optional[CustLoyaltyTypeShareSynchInd] = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        }
    )
    share_market_ind: Optional[CustLoyaltyTypeShareMarketInd] = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        }
    )
    program_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProgramID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    membership_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MembershipID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    travel_sector: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelSector",
            "type": "Attribute",
        }
    )
    loyal_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "LoyalLevel",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    single_vendor_ind: Optional[CustLoyaltyTypeSingleVendorInd] = field(
        default=None,
        metadata={
            "name": "SingleVendorInd",
            "type": "Attribute",
        }
    )
    signup_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SignupDate",
            "type": "Attribute",
        }
    )
    effective_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        }
    )
    expire_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExpireDate",
            "type": "Attribute",
        }
    )
    rph: Optional[str] = field(
        default=None,
        metadata={
            "name": "RPH",
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}",
        }
    )


@dataclass
class DiversityControlType:
    """
    These parameters control how IntellSell should select itineraries based not
    necessarily on cheapest price, but also on other criteria that guarantee a
    diverse response.
    """
    low_fare_bucket: Optional["DiversityControlType.LowFareBucket"] = field(
        default=None,
        metadata={
            "name": "LowFareBucket",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    dimensions: Optional["DiversityControlType.Dimensions"] = field(
        default=None,
        metadata={
            "name": "Dimensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )

    @dataclass
    class LowFareBucket:
        options: Optional[str] = field(
            default=None,
            metadata={
                "name": "Options",
                "type": "Attribute",
                "pattern": r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%",
            }
        )
        fare_cut_off: Optional[str] = field(
            default=None,
            metadata={
                "name": "FareCutOff",
                "type": "Attribute",
                "pattern": r"(0|100|[1-9][0-9]?)%",
            }
        )

    @dataclass
    class Dimensions:
        travel_time: Optional["DiversityControlType.Dimensions.TravelTime"] = field(
            default=None,
            metadata={
                "name": "TravelTime",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        carrier: Optional["DiversityControlType.Dimensions.Carrier"] = field(
            default=None,
            metadata={
                "name": "Carrier",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        operating_duplicate: Optional["DiversityControlType.Dimensions.OperatingDuplicate"] = field(
            default=None,
            metadata={
                "name": "OperatingDuplicate",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        inbound_outbound_pairing: Optional["DiversityControlType.Dimensions.InboundOutboundPairing"] = field(
            default=None,
            metadata={
                "name": "InboundOutboundPairing",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        time_of_day: Optional["DiversityControlType.Dimensions.TimeOfDay"] = field(
            default=None,
            metadata={
                "name": "TimeOfDay",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        stops_number: Optional["DiversityControlType.Dimensions.StopsNumber"] = field(
            default=None,
            metadata={
                "name": "StopsNumber",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        price_weight: int = field(
            default=10,
            metadata={
                "name": "PriceWeight",
                "type": "Attribute",
                "min_inclusive": 0,
                "max_inclusive": 10,
            }
        )

        @dataclass
        class TravelTime:
            weight: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )

        @dataclass
        class Carrier:
            default: Optional["DiversityControlType.Dimensions.Carrier.Default"] = field(
                default=None,
                metadata={
                    "name": "Default",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            override: List["DiversityControlType.Dimensions.Carrier.Override"] = field(
                default_factory=list,
                metadata={
                    "name": "Override",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            weight: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )
            online_indicator: bool = field(
                default=False,
                metadata={
                    "name": "OnlineIndicator",
                    "type": "Attribute",
                }
            )

            @dataclass
            class Default:
                options: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Options",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%",
                    }
                )

            @dataclass
            class Override:
                code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9A-Z]{2,3}",
                    }
                )
                options: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Options",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%",
                    }
                )

        @dataclass
        class OperatingDuplicate:
            preferred_carrier: List["DiversityControlType.Dimensions.OperatingDuplicate.PreferredCarrier"] = field(
                default_factory=list,
                metadata={
                    "name": "PreferredCarrier",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            weight: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )

            @dataclass
            class PreferredCarrier:
                code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9A-Z]{2,3}",
                    }
                )

        @dataclass
        class InboundOutboundPairing:
            weight: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )
            duplicates: int = field(
                default=1,
                metadata={
                    "name": "Duplicates",
                    "type": "Attribute",
                }
            )

        @dataclass
        class TimeOfDay:
            """
            Attributes
                distribution: Exactly one attribute: either Direction or
                    Leg must be provided
                weight:
            """
            distribution: List["DiversityControlType.Dimensions.TimeOfDay.Distribution"] = field(
                default_factory=list,
                metadata={
                    "name": "Distribution",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            weight: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )

            @dataclass
            class Distribution:
                range: List["DiversityControlType.Dimensions.TimeOfDay.Distribution.Range"] = field(
                    default_factory=list,
                    metadata={
                        "name": "Range",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "max_occurs": 4,
                    }
                )
                direction: Optional[OutboundOrInbound] = field(
                    default=None,
                    metadata={
                        "name": "Direction",
                        "type": "Attribute",
                    }
                )
                leg: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Leg",
                        "type": "Attribute",
                    }
                )
                endpoint: DepartureOrArrival = field(
                    default=DepartureOrArrival.DEPARTURE,
                    metadata={
                        "name": "Endpoint",
                        "type": "Attribute",
                    }
                )

                @dataclass
                class Range:
                    """Either all Range elements shall contain attribute Options or none.

                    Ranges shall not overlap.
                    """
                    begin: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Begin",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"([0-1]?[0-9]|2[0-3]):[0-5][0-9]",
                        }
                    )
                    end: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "End",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"([0-1]?[0-9]|2[0-3]):[0-5][0-9]",
                        }
                    )
                    options: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Options",
                            "type": "Attribute",
                            "pattern": r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%",
                        }
                    )

        @dataclass
        class StopsNumber:
            weight: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )


@dataclass
class DocumentType:
    """
    Provides information on a specific documents.

    Attributes
        doc_holder_name: Specify document holder name.
        doc_limitations: Used to indicate any limitations on the
            document (e.g. as a person may only be allowed to spend a
            max of 30 days in country on a visitor's visa).
        share_synch_ind:
        share_market_ind:
        doc_issue_authority: Indicates the group or association that
            granted the document.
        doc_issue_location: Indicates the location where the document
            was issued.
        doc_id: Unique number assigned by authorities to document.
        doc_type: Indicates the type of document (e.g. Passport,
            Military ID, Drivers License, national ID, Vaccination
            Certificate). Refer to OTA Code List Document Type (DOC).
        gender:
        birth_date: Indicates the date of birth as indicated in the
            document, in ISO 8601 prescribed format.
        effective_date: Indicates the starting date.
        expire_date: Indicates the ending date.
    """
    doc_holder_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocHolderName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 64,
        }
    )
    doc_limitations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DocLimitations",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 9,
            "min_length": 1,
            "max_length": 64,
        }
    )
    share_synch_ind: Optional[DocumentTypeShareSynchInd] = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        }
    )
    share_market_ind: Optional[DocumentTypeShareMarketInd] = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        }
    )
    doc_issue_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocIssueAuthority",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    doc_issue_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocIssueLocation",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    doc_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocType",
            "type": "Attribute",
        }
    )
    gender: Optional[DocumentTypeGender] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
        }
    )
    birth_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Attribute",
        }
    )
    effective_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        }
    )
    expire_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExpireDate",
            "type": "Attribute",
        }
    )


@dataclass
class EmailType:
    """
    Electronic email addresses, in IETF specified format.

    Attributes
        value:
        share_synch_ind:
        share_market_ind:
        default_ind:
        email_type: Defines the purpose of the e-mail address (e.g.
            personal, business, listserve). Refer to OTA Code List Email
            Address Type (EAT).
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    share_synch_ind: Optional[EmailTypeShareSynchInd] = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        }
    )
    share_market_ind: Optional[EmailTypeShareMarketInd] = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        }
    )
    default_ind: bool = field(
        default=False,
        metadata={
            "name": "DefaultInd",
            "type": "Attribute",
        }
    )
    email_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailType",
            "type": "Attribute",
        }
    )


@dataclass
class EquipmentTypePref(EquipmentType):
    """
    Attributes
        prefer_level:
        wide_body: Specify if equipment should have a wide body or not.
    """
    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        }
    )
    wide_body: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WideBody",
            "type": "Attribute",
        }
    )


@dataclass
class ExchangeOriginDestinationFlightType:
    """
    Attributes
        origin_location: Flight origin code
        destination_location: Flight destination code
        airline: Airline information
        side_trip: Side trip information
        reservation: Reservation information
        mileage_display: Mileage information
        booking_date_time: Booking date and time
        fare:
        plus_up:
        number: Flight number
        departure_date_time: Departure date and time
        arrival_date_time: Arrival date and time
        marriage_status: Marriage status
        type: Flight type (A: Air Segment, K: ARUNK, O: Open Segment)
        flown: Specify whether the flight is flown.
        class_of_service: Class of service
    """
    origin_location: Optional[RequestLocationType] = field(
        default=None,
        metadata={
            "name": "OriginLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    destination_location: Optional[RequestLocationType] = field(
        default=None,
        metadata={
            "name": "DestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    airline: Optional[AirlineType] = field(
        default=None,
        metadata={
            "name": "Airline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    side_trip: Optional[SideTripType] = field(
        default=None,
        metadata={
            "name": "SideTrip",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    reservation: Optional[ReservationType] = field(
        default=None,
        metadata={
            "name": "Reservation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    mileage_display: List[MileageDisplayType] = field(
        default_factory=list,
        metadata={
            "name": "MileageDisplay",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    booking_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingDateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?",
        }
    )
    fare: Optional["ExchangeOriginDestinationFlightType.Fare"] = field(
        default=None,
        metadata={
            "name": "Fare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    plus_up: List[PlusUpType] = field(
        default_factory=list,
        metadata={
            "name": "PlusUp",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    departure_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureDateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?",
        }
    )
    arrival_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalDateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?",
        }
    )
    marriage_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarriageStatus",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "pattern": r"[AKO]",
        }
    )
    flown: bool = field(
        default=False,
        metadata={
            "name": "Flown",
            "type": "Attribute",
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{1,2}",
        }
    )

    @dataclass
    class Fare(FareDetailsType):
        adjustment: Optional["ExchangeOriginDestinationFlightType.Fare.Adjustment"] = field(
            default=None,
            metadata={
                "name": "Adjustment",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class Adjustment:
            """
            Attributes
                value: Adjustment Value, can be positive or negative,
                    number or percentage
                currency: Currency of Adjustment's Value
                group: Markup/Discount Group
            """
            value: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"(\+|-)?([0-9]+(\.[0-9]*)?|\.[0-9]+)%?",
                }
            )
            currency: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Currency",
                    "type": "Attribute",
                    "pattern": r"[a-zA-Z]{3}",
                }
            )
            group: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Group",
                    "type": "Attribute",
                }
            )


@dataclass
class ExchangeSettingsType:
    """
    Attributes
        reprice_current_itin: If set to ''false'', disables processing
            of Current Itin path.
        attach_exchange_info: If set to ''true'', adds exchange-specific
            information to the response. The information includes richer
            Tax elements, ReissueVsExchange attribute and currency
            conversion rates.
        reissue_exchange: Process Type Indicator for Primary Request
            Type
        branded_results: Enables branded results (if brands are
            available for returned options)
        miptimeout_threshold: Hints MIP that it should return options
            within this amount of time (in seconds)
        request_type: Used to specify if the request is an usual
            Exchange request (basic) or an Exchange Context Shopping
            request (context). When not specified, basic is assumed.
    """
    reprice_current_itin: bool = field(
        default=True,
        metadata={
            "name": "RepriceCurrentItin",
            "type": "Attribute",
        }
    )
    attach_exchange_info: bool = field(
        default=False,
        metadata={
            "name": "AttachExchangeInfo",
            "type": "Attribute",
        }
    )
    reissue_exchange: Optional[ExchangeSettingsTypeReissueExchange] = field(
        default=None,
        metadata={
            "name": "ReissueExchange",
            "type": "Attribute",
        }
    )
    branded_results: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BrandedResults",
            "type": "Attribute",
        }
    )
    miptimeout_threshold: Optional[int] = field(
        default=None,
        metadata={
            "name": "MIPTimeoutThreshold",
            "type": "Attribute",
        }
    )
    request_type: Optional[ExchangeSettingsTypeRequestType] = field(
        default=None,
        metadata={
            "name": "RequestType",
            "type": "Attribute",
        }
    )


@dataclass
class ExchangeTpaExtensionsType:
    class Meta:
        name = "ExchangeTPA_ExtensionsType"

    award_shopping: Optional[AwardShoppingType] = field(
        default=None,
        metadata={
            "name": "AwardShopping",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )


@dataclass
class FareRestrictPrefType:
    """
    Identifies preferences for airfare restrictions acceptable or not acceptable
    for a given travel situation.

    Attributes
        prefer_level:
        fare_restriction: Refer to OTA Code List Fare Restriction (FAR).
    """
    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        }
    )
    fare_restriction: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareRestriction",
            "type": "Attribute",
        }
    )


@dataclass
class FlexibleFaresType:
    """
    Attributes
        fare_parameters: This element specifies parameters for desired
            fare.
    """
    fare_parameters: List["FlexibleFaresType.FareParameters"] = field(
        default_factory=list,
        metadata={
            "name": "FareParameters",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 10,
        }
    )

    @dataclass
    class FareParameters:
        """
        Attributes
            exclude_restricted: Setting this to true means the same as
                setting ResTicketing, MinMaxStay and RefundPenalty to
                false.
            res_ticketing: If set to true, fares that have a
                reservation/ticketing can be included in the responses.
                If set to false, then no fares that include
                reservation/ticketing requirement will be included in
                the response. This is negation of XA qualifier.
            min_max_stay: If set to true, fares that have a min/max stay
                can be included in the responses. If set to false, then
                no fares that include a min/max stay requirement will be
                included in the response. This is negation of XS
                qualifier.
            refund_penalty: If set to true, fares that have a refund
                penalty can be included in the responses. If set to
                false, then no fares that include a refund penalty
                requirement will be included in the response. This is
                negation of XP qualifier.
            public_fare: This element finds only public fares.
            private_fare: This element finds only private fares.
            cabin: This element specifies preffered cabin type.
            passenger_type: This element specifies PTC used to find this
                fare.
            negotiated_fares_only: If set to true then returned fares
                need to match AcccountCode/CorpID specified in Fare
                Group definition on all fare components.
            xofares: If set to true only fares matching PTC specified in
                the Flex Fare Group will be returned on all fare
                components.
            passenger_type_quantity: Define information on the number of
                passengers of a specific type.
            jump_cabin_logic:
            keep_same_cabin:
            corporate_id:
            account_code:
        """
        exclude_restricted: Optional["FlexibleFaresType.FareParameters.ExcludeRestricted"] = field(
            default=None,
            metadata={
                "name": "ExcludeRestricted",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        res_ticketing: Optional["FlexibleFaresType.FareParameters.ResTicketing"] = field(
            default=None,
            metadata={
                "name": "ResTicketing",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        min_max_stay: Optional["FlexibleFaresType.FareParameters.MinMaxStay"] = field(
            default=None,
            metadata={
                "name": "MinMaxStay",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        refund_penalty: Optional["FlexibleFaresType.FareParameters.RefundPenalty"] = field(
            default=None,
            metadata={
                "name": "RefundPenalty",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        public_fare: Optional["FlexibleFaresType.FareParameters.PublicFare"] = field(
            default=None,
            metadata={
                "name": "PublicFare",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        private_fare: Optional["FlexibleFaresType.FareParameters.PrivateFare"] = field(
            default=None,
            metadata={
                "name": "PrivateFare",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        cabin: Optional["FlexibleFaresType.FareParameters.Cabin"] = field(
            default=None,
            metadata={
                "name": "Cabin",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        passenger_type: Optional["FlexibleFaresType.FareParameters.PassengerType"] = field(
            default=None,
            metadata={
                "name": "PassengerType",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        negotiated_fares_only: Optional["FlexibleFaresType.FareParameters.NegotiatedFaresOnly"] = field(
            default=None,
            metadata={
                "name": "NegotiatedFaresOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        xofares: Optional["FlexibleFaresType.FareParameters.Xofares"] = field(
            default=None,
            metadata={
                "name": "XOFares",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        passenger_type_quantity: List[PassengerTypeQuantityType] = field(
            default_factory=list,
            metadata={
                "name": "PassengerTypeQuantity",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "max_occurs": 4,
            }
        )
        jump_cabin_logic: Optional[JumpCabinLogicType] = field(
            default=None,
            metadata={
                "name": "JumpCabinLogic",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        keep_same_cabin: Optional[KeepSameCabinType] = field(
            default=None,
            metadata={
                "name": "KeepSameCabin",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        corporate_id: List["FlexibleFaresType.FareParameters.CorporateId"] = field(
            default_factory=list,
            metadata={
                "name": "CorporateID",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        account_code: List["FlexibleFaresType.FareParameters.AccountCode"] = field(
            default_factory=list,
            metadata={
                "name": "AccountCode",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class ExcludeRestricted:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class ResTicketing:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MinMaxStay:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class RefundPenalty:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class PublicFare:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class PrivateFare:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class Cabin:
            type: Optional[CabinType] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class PassengerType:
            """
            Attributes
                code: Specify traveler type code.
            """
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 8,
                }
            )

        @dataclass
        class NegotiatedFaresOnly:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class Xofares:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class CorporateId:
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[A-Za-z]{3}[0-9]{2}",
                }
            )

        @dataclass
        class AccountCode:
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                }
            )


@dataclass
class FlightTypePrefType:
    """
    Indicates preferences for certain types of flights, such as connections or
    stopovers, when used for a specific travel situation.

    Attributes
        prefer_level:
        flight_type:
        max_connections: Indicates that if connection is chosen, then
            this attribute defines the maximum number of connections
            preferred.
    """
    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        }
    )
    flight_type: Optional[FlightTypeType] = field(
        default=None,
        metadata={
            "name": "FlightType",
            "type": "Attribute",
        }
    )
    max_connections: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "name": "MaxConnections",
            "type": "Attribute",
        }
    )


@dataclass
class GlobalDateTimeType(DateTimeType):
    """
    Attributes
        date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS.
    """
    date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}",
        }
    )


@dataclass
class InterlineBrandsType:
    """
    Attributes
        brand: Brand list to be returned
        change_brand_for_soldout: If specific XX brand is not available
            for requested date/flight, another cheapest brand will be
            returned combined with available XX brand.
    """
    brand: List[BrandType] = field(
        default_factory=list,
        metadata={
            "name": "Brand",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    change_brand_for_soldout: bool = field(
        default=False,
        metadata={
            "name": "ChangeBrandForSoldout",
            "type": "Attribute",
        }
    )


@dataclass
class OriginDestinationFlightType:
    """
    Attributes
        origin_location: Flight origin code
        destination_location: Flight destination code
        airline: Airline information
        side_trip: Side trip information
        reservation: Reservation information
        mileage_display: Mileage information
        booking_date_time: Booking date and time
        fare:
        plus_up:
        number: Flight number
        departure_date_time: Departure date and time
        arrival_date_time: Arrival date and time
        marriage_status: Marriage status
        type: Flight type (A: Air Segment, K: ARUNK, O: Open Segment)
        flown: Specify whether the flight is flown.
        class_of_service: Class of service
        shopped: Specify whether the flight is shopped.
    """
    origin_location: Optional[RequestLocationType] = field(
        default=None,
        metadata={
            "name": "OriginLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    destination_location: Optional[RequestLocationType] = field(
        default=None,
        metadata={
            "name": "DestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    airline: Optional[AirlineType] = field(
        default=None,
        metadata={
            "name": "Airline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    side_trip: Optional[SideTripType] = field(
        default=None,
        metadata={
            "name": "SideTrip",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    reservation: Optional[ReservationType] = field(
        default=None,
        metadata={
            "name": "Reservation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    mileage_display: List[MileageDisplayType] = field(
        default_factory=list,
        metadata={
            "name": "MileageDisplay",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    booking_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingDateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?",
        }
    )
    fare: Optional[FareOptionalDetailsType] = field(
        default=None,
        metadata={
            "name": "Fare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    plus_up: List[PlusUpType] = field(
        default_factory=list,
        metadata={
            "name": "PlusUp",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    departure_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureDateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?",
        }
    )
    arrival_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalDateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?",
        }
    )
    marriage_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarriageStatus",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "pattern": r"[AKO]",
        }
    )
    flown: bool = field(
        default=False,
        metadata={
            "name": "Flown",
            "type": "Attribute",
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "pattern": r"[A-Z]{1,2}",
        }
    )
    shopped: bool = field(
        default=False,
        metadata={
            "name": "Shopped",
            "type": "Attribute",
        }
    )


@dataclass
class OverrideDateTimeType(DateTimeType):
    """
    Attributes
        date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS.
    """
    date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Attribute",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}",
        }
    )


@dataclass
class PersonNameType:
    """
    This is an XML Schema representing the OTA Person Name object.

    Attributes
        name_prefix: Salutation of honorific. (e.g., Mr. Mrs., Ms.,
            Miss, Dr.)
        given_name: Given name, first name or names
        middle_name: Person's middle name
        surname_prefix: e.g "van der", "von", "de"
        surname: Family name, last name.
        name_suffix: Hold various name suffixes and letters (e.g. Jr.,
            Sr., III, Ret., Esq.).
        name_title: Degree or honors (e.g., Ph.D., M.D.)
        share_synch_ind:
        share_market_ind:
        name_type: Type of name of the individual, such as former,
            nickname, alternate or alias name. Refer to OTA Code List
            Name Type (NAM).
    """
    name_prefix: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NamePrefix",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 16,
        }
    )
    given_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GivenName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 64,
        }
    )
    middle_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MiddleName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 64,
        }
    )
    surname_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "SurnamePrefix",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 16,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )
    name_suffix: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 16,
        }
    )
    name_title: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NameTitle",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 16,
        }
    )
    share_synch_ind: Optional[PersonNameTypeShareSynchInd] = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        }
    )
    share_market_ind: Optional[PersonNameTypeShareMarketInd] = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        }
    )
    name_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameType",
            "type": "Attribute",
        }
    )


@dataclass
class PriceRequestInformationType:
    """
    Identify pricing source, if negotiated fares are requested and if it is a
    reprice request.

    Attributes
        negotiated_fare_code:
        account_code:
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        fare_qualifier: Fare Type is specific to a specific fare and
            this is a request for a set of fares based on these
            qualifiers.
        negotiated_fares_only: If set to true then returned fares need
            to match requested AcccountCode/CorpID on all fare
            components
        currency_code: Type of funds preferred for reviewing monetary
            values, in ISO 4217 codes.
        pricing_source: It can be used to indicate whether the fare is
            public or private.
        reprice:
        process_thru_fares_only: Activates processing of thru fares
            only.
        purchase_date: Specify purchase date. Fares returned will be
            based on the purchase date.
        purchase_time: Specify purchase time. Fares returned will be
            based on the purchase time.
        net_fares_used: Set to true when exchange ticket uses net fare.
    """
    negotiated_fare_code: List["PriceRequestInformationType.NegotiatedFareCode"] = field(
        default_factory=list,
        metadata={
            "name": "NegotiatedFareCode",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    account_code: List["PriceRequestInformationType.AccountCode"] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    tpa_extensions: Optional["PriceRequestInformationType.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    fare_qualifier: Optional[Union[str, bool]] = field(
        default=None,
        metadata={
            "name": "FareQualifier",
            "type": "Attribute",
        }
    )
    negotiated_fares_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NegotiatedFaresOnly",
            "type": "Attribute",
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    pricing_source: Optional[RequestPricingSourceType] = field(
        default=None,
        metadata={
            "name": "PricingSource",
            "type": "Attribute",
        }
    )
    reprice: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reprice",
            "type": "Attribute",
        }
    )
    process_thru_fares_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProcessThruFaresOnly",
            "type": "Attribute",
        }
    )
    purchase_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PurchaseDate",
            "type": "Attribute",
        }
    )
    purchase_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchaseTime",
            "type": "Attribute",
        }
    )
    net_fares_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NetFaresUsed",
            "type": "Attribute",
        }
    )

    @dataclass
    class TpaExtensions:
        """
        Attributes
            public_fare: This element finds only public fares.
            private_fare: This element finds only private fares.
            iatafare: This element finds only IATA fares.
            web_fare:
            priority: This element governs how flights are returned. A
                user can uses a priority of 1-4 to make this
                determination.
            indicators: This element restricts fares which can be
                returned in response. If a customer passes this element,
                all its children should be specified.
            promo_id: Promotional Identifier - a string which identifies
                a promotion, possibly giving a discount prices etc.
            customer_type:
            multiple_traveler_groups: This element governs how flights
                are returned when multiple passenger groups are
                requested.
            branded_fare_indicators:
            passenger_status:
            point_of_sale_override: Will return the fares available for
                specified point of sale and priced in this point of sale
                currency. Currency is overriden by
                PriceRequestInformation@CurrencyCode.
            point_of_ticketing_override:
            apply_resident_discount: Apply resident discount in CLFE
            eticketable_override:
            currency:
            use_reduced_constructions: Use reduced constructions (simple
                fare paths with restrictions on the number of fare
                components).
            obfees:
            fare_breaks_at_legs: Force fare breaks at leg points if
                split taxes by leg requested. By default set to true.
            fare_adjustment: Capability to specify Plus-Up and Discount
                Amount and Percentage.
        """
        public_fare: Optional["PriceRequestInformationType.TpaExtensions.PublicFare"] = field(
            default=None,
            metadata={
                "name": "PublicFare",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        private_fare: Optional["PriceRequestInformationType.TpaExtensions.PrivateFare"] = field(
            default=None,
            metadata={
                "name": "PrivateFare",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        iatafare: Optional["PriceRequestInformationType.TpaExtensions.Iatafare"] = field(
            default=None,
            metadata={
                "name": "IATAFare",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        web_fare: Optional["PriceRequestInformationType.TpaExtensions.WebFare"] = field(
            default=None,
            metadata={
                "name": "WebFare",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        priority: Optional["PriceRequestInformationType.TpaExtensions.Priority"] = field(
            default=None,
            metadata={
                "name": "Priority",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        indicators: Optional["PriceRequestInformationType.TpaExtensions.Indicators"] = field(
            default=None,
            metadata={
                "name": "Indicators",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        promo_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "PromoID",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        customer_type: Optional["PriceRequestInformationType.TpaExtensions.CustomerType"] = field(
            default=None,
            metadata={
                "name": "CustomerType",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        multiple_traveler_groups: Optional["PriceRequestInformationType.TpaExtensions.MultipleTravelerGroups"] = field(
            default=None,
            metadata={
                "name": "MultipleTravelerGroups",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        branded_fare_indicators: Optional["PriceRequestInformationType.TpaExtensions.BrandedFareIndicators"] = field(
            default=None,
            metadata={
                "name": "BrandedFareIndicators",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        passenger_status: Optional["PriceRequestInformationType.TpaExtensions.PassengerStatus"] = field(
            default=None,
            metadata={
                "name": "PassengerStatus",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        point_of_sale_override: Optional[PointOfSaleOverrideType] = field(
            default=None,
            metadata={
                "name": "PointOfSaleOverride",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        point_of_ticketing_override: Optional[PointOfTicketingOverrideType] = field(
            default=None,
            metadata={
                "name": "PointOfTicketingOverride",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        apply_resident_discount: Optional[ApplyResidentDiscountType] = field(
            default=None,
            metadata={
                "name": "ApplyResidentDiscount",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        eticketable_override: Optional["PriceRequestInformationType.TpaExtensions.EticketableOverride"] = field(
            default=None,
            metadata={
                "name": "ETicketableOverride",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        currency: Optional["PriceRequestInformationType.TpaExtensions.Currency"] = field(
            default=None,
            metadata={
                "name": "Currency",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        use_reduced_constructions: Optional["PriceRequestInformationType.TpaExtensions.UseReducedConstructions"] = field(
            default=None,
            metadata={
                "name": "UseReducedConstructions",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        obfees: Optional["PriceRequestInformationType.TpaExtensions.Obfees"] = field(
            default=None,
            metadata={
                "name": "OBFees",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        fare_breaks_at_legs: Optional["PriceRequestInformationType.TpaExtensions.FareBreaksAtLegs"] = field(
            default=None,
            metadata={
                "name": "FareBreaksAtLegs",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        fare_adjustment: Optional["PriceRequestInformationType.TpaExtensions.FareAdjustment"] = field(
            default=None,
            metadata={
                "name": "FareAdjustment",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class PublicFare:
            ind: bool = field(
                default=False,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                }
            )

        @dataclass
        class PrivateFare:
            ind: bool = field(
                default=False,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                }
            )

        @dataclass
        class Iatafare:
            ind: bool = field(
                default=False,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                }
            )

        @dataclass
        class WebFare:
            """
            Attributes
                ind: Web fare
            """
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                }
            )

        @dataclass
        class Priority:
            price: Optional["PriceRequestInformationType.TpaExtensions.Priority.Price"] = field(
                default=None,
                metadata={
                    "name": "Price",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                }
            )
            direct_flights: Optional["PriceRequestInformationType.TpaExtensions.Priority.DirectFlights"] = field(
                default=None,
                metadata={
                    "name": "DirectFlights",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                }
            )
            time: Optional["PriceRequestInformationType.TpaExtensions.Priority.Time"] = field(
                default=None,
                metadata={
                    "name": "Time",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                }
            )
            vendor: Optional["PriceRequestInformationType.TpaExtensions.Priority.Vendor"] = field(
                default=None,
                metadata={
                    "name": "Vendor",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                }
            )

            @dataclass
            class Price:
                priority: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Priority",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 4,
                    }
                )

            @dataclass
            class DirectFlights:
                priority: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Priority",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 4,
                    }
                )

            @dataclass
            class Time:
                priority: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Priority",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 4,
                    }
                )

            @dataclass
            class Vendor:
                priority: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Priority",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 4,
                    }
                )

        @dataclass
        class Indicators:
            """
            Attributes
                retain_fare: Currently must be set to true.
                min_max_stay: If set to true, fares that have a min/max
                    stay can be included in the responses. If set to
                    false, then no fares that include a min/max stay
                    requirement will be included in the response.
                refund_penalty: If set to true, fares that have a refund
                    penalty can be included in the responses. If set to
                    false, then no fares that include a refund penalty
                    requirement will be included in the response.
                res_ticketing: If set to true, fares that have a
                    reservation/ticketing can be included in the
                    responses. If set to false, then no fares that
                    include reservation/ticketing requirement will be
                    included in the response.
                travel_policy: This element is currently ignored whether
                    it is true or false.
            """
            retain_fare: Optional["PriceRequestInformationType.TpaExtensions.Indicators.RetainFare"] = field(
                default=None,
                metadata={
                    "name": "RetainFare",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            min_max_stay: Optional["PriceRequestInformationType.TpaExtensions.Indicators.MinMaxStay"] = field(
                default=None,
                metadata={
                    "name": "MinMaxStay",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            refund_penalty: Optional["PriceRequestInformationType.TpaExtensions.Indicators.RefundPenalty"] = field(
                default=None,
                metadata={
                    "name": "RefundPenalty",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            res_ticketing: Optional["PriceRequestInformationType.TpaExtensions.Indicators.ResTicketing"] = field(
                default=None,
                metadata={
                    "name": "ResTicketing",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            travel_policy: Optional["PriceRequestInformationType.TpaExtensions.Indicators.TravelPolicy"] = field(
                default=None,
                metadata={
                    "name": "TravelPolicy",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )

            @dataclass
            class RetainFare:
                ind: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class MinMaxStay:
                ind: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class RefundPenalty:
                ind: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class ResTicketing:
                ind: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class TravelPolicy:
                ind: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    }
                )

        @dataclass
        class CustomerType:
            value: Optional[CustomerTypeValue] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MultipleTravelerGroups:
            """
            Attributes
                itineraries_per_group: Indicates desired number of
                    itineraries to be returned in each passenger group
                    at beggining of response.
            """
            itineraries_per_group: Optional[int] = field(
                default=None,
                metadata={
                    "name": "ItinerariesPerGroup",
                    "type": "Attribute",
                    "min_inclusive": 1,
                    "max_inclusive": 99,
                }
            )

        @dataclass
        class BrandedFareIndicators:
            """
            Attributes
                return_cheapest_unbranded_fare:
                single_branded_fare: Return single brand option per itin
                multiple_branded_fares: Return multiple brand options
                    per itin
            """
            return_cheapest_unbranded_fare: Optional["PriceRequestInformationType.TpaExtensions.BrandedFareIndicators.ReturnCheapestUnbrandedFare"] = field(
                default=None,
                metadata={
                    "name": "ReturnCheapestUnbrandedFare",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            single_branded_fare: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "SingleBrandedFare",
                    "type": "Attribute",
                }
            )
            multiple_branded_fares: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "MultipleBrandedFares",
                    "type": "Attribute",
                }
            )

            @dataclass
            class ReturnCheapestUnbrandedFare:
                """
                Attributes
                    ind: Indicator to turn on or off return of cheapest
                        unbranded fare referred as "catch all" fare for
                        the branded carriers from the branded fares
                        service.
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    }
                )

        @dataclass
        class PassengerStatus:
            state_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "StateCode",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_length": 2,
                    "max_length": 8,
                }
            )
            country_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CountryCode",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "pattern": r"[a-zA-Z]{2}",
                }
            )
            city_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CityCode",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "pattern": r"[a-zA-Z]{3}",
                }
            )
            type: Optional[PassengerStatusType] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class EticketableOverride:
            """
            Attributes
                value: ETicketable override
            """
            value: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                }
            )

        @dataclass
        class Currency:
            """
            Attributes
                dual: Dual currency
                moverride: M override
            """
            dual: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Dual",
                    "type": "Attribute",
                    "pattern": r"[a-zA-Z]{3}",
                }
            )
            moverride: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "MOverride",
                    "type": "Attribute",
                }
            )

        @dataclass
        class UseReducedConstructions:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                }
            )

        @dataclass
        class Obfees:
            """
            Attributes
                rtype: Indicator Returning R-Type OB Fees
                ttype: Indicator Returning T-Type OB Fees
            """
            rtype: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "RType",
                    "type": "Attribute",
                }
            )
            ttype: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "TType",
                    "type": "Attribute",
                }
            )

        @dataclass
        class FareBreaksAtLegs:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                }
            )

        @dataclass
        class FareAdjustment:
            """
            Attributes
                value: Adjustment Value, can be positive or negative,
                    number or percentage
                currency: Currency of Adjustment's Value
            """
            value: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"(\+|-)?([0-9]+(\.[0-9]*)?|\.[0-9]+)%?",
                }
            )
            currency: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Currency",
                    "type": "Attribute",
                    "pattern": r"[a-zA-Z]{3}",
                }
            )

    @dataclass
    class NegotiatedFareCode:
        """
        Attributes
            code: Any code used to specify an item, for example, type of
                traveler, service code, room amenity, etc.
            code_context: Identifies the source authority for the code.
            uri: Identifies the location of the code table
            quantity: Used to define a quantity of an associated element
                or attribute.
            secondary_code: An additional attribute to allow flexibility
                for particular organizations who require an additional
                code.
            supplier_code: An additional attribute to allow flexibility
                for particular organizations who require an additional
                supplier code.
            content:
        """
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "pattern": r"[A-Za-z]{3}[0-9]{2}",
            }
        )
        code_context: Optional[str] = field(
            default=None,
            metadata={
                "name": "CodeContext",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 32,
            }
        )
        uri: Optional[str] = field(
            default=None,
            metadata={
                "name": "URI",
                "type": "Attribute",
            }
        )
        quantity: Optional[int] = field(
            default=None,
            metadata={
                "name": "Quantity",
                "type": "Attribute",
                "min_inclusive": 1,
                "max_inclusive": 999,
            }
        )
        secondary_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "SecondaryCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 16,
            }
        )
        supplier_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "SupplierCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 16,
            }
        )
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
                "choices": (
                    {
                        "name": "Supplier",
                        "type": CompanyNameType,
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                    {
                        "name": "TPA_Extensions",
                        "type": str,
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                ),
            }
        )

    @dataclass
    class AccountCode:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 20,
            }
        )


@dataclass
class RoutingDefinitionType:
    """
    Definition of a routing.

    Attributes
        routing_leg:
        add_wildcards: If true, wildcards will be automatically inserted
            between each two leg (RoutingLeg) elements. Will be set to
            'false' if not present.
    """
    routing_leg: List[RoutingLegType] = field(
        default_factory=list,
        metadata={
            "name": "RoutingLeg",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )
    add_wildcards: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AddWildcards",
            "type": "Attribute",
        }
    )


@dataclass
class SourceBookingChannelType(BookingChannelType):
    """
    Specifies the booking channel type and whether it is the primary means of
    connectivity of the source.

    Attributes
        company_name: Identifies the company that is associated with the
            booking channel.
    """
    company_name: Optional[CompanyNameType] = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )


@dataclass
class TaxCodeAmountType(TaxCodeType):
    """
    Defines the data fields available for tax code and amount.
    """
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )


@dataclass
class TelephoneType:
    """
    Construct for holding a telephone number.

    Attributes
        share_synch_ind:
        share_market_ind:
        phone_location_type: Refer to OTA Code List Phone Location Type
            (PLT).
        phone_tech_type: Indicates type of technology associated with
            this telephone number, such as Voice, Data, Fax, Pager,
            Mobile, TTY, etc. Refer to OTA Code List Phone Technology
            Type (PTT).
        country_access_code: Code assigned by telecommunications
            authorities for international country access identifier.
        area_city_code: Code assigned for telephones in a specific
            region, city, or area.
        phone_number: Telephone number assigned to a single location.
        extension: Extension to reach a specific party at the phone
            number.
        pin: Additional codes used for pager or telephone access rights.
        formatted_ind: Specifies if the associated data is formatted or
            not. If true, then it is formatted, if false, then not
            formatted.
    """
    share_synch_ind: Optional[TelephoneTypeShareSynchInd] = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        }
    )
    share_market_ind: Optional[TelephoneTypeShareMarketInd] = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        }
    )
    phone_location_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneLocationType",
            "type": "Attribute",
        }
    )
    phone_tech_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneTechType",
            "type": "Attribute",
        }
    )
    country_access_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryAccessCode",
            "type": "Attribute",
            "pattern": r"[0-9]{1,3}",
        }
    )
    area_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AreaCityCode",
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}",
        }
    )
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "pattern": r"[0-9]{1,5}",
        }
    )
    pin: Optional[str] = field(
        default=None,
        metadata={
            "name": "PIN",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    formatted_ind: bool = field(
        default=False,
        metadata={
            "name": "FormattedInd",
            "type": "Attribute",
        }
    )


@dataclass
class TicketDistribPrefType:
    """
    Type of ticket distribution to be used with this collection of preferences.

    Attributes
        value:
        prefer_level:
        distrib_type: Ticket distribution method; such as Fax, Email,
            Courier, Mail, Airport_Pickup, City_Office, Hotel_Desk,
            WillCall, etc.
        ticket_time: Ticket turnaround time desired, amount of time
            requested to deliver tickets.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 64,
        }
    )
    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        }
    )
    distrib_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistribType",
            "type": "Attribute",
        }
    )
    ticket_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TicketTime",
            "type": "Attribute",
        }
    )


@dataclass
class UniqueIdType:
    """
    An identifier used to uniquely reference an object in a system (e.g. an airline
    reservation reference, customer profile reference, booking confirmation number,
    or a reference to a previous availability quote).

    Attributes
        company_name: Identifies the company that is associated with the
            UniqueID.
        url: URL that identifies the location associated with the record
            identified by the UniqueID.
        type: A reference to the type of object defined by the UniqueID
            element. Refer to OTA Code List Unique ID Type (UIT).
        instance: The identification of a record as it exists at a point
            in time. An instance is used in update messages where the
            sender must assure the server that the update sent refers to
            the most recent modification level of the object being
            updated.
        id: A unique identifying value assigned by the creating system.
            The ID attribute may be used to reference a primary-key
            value within a database or in a particular implementation.
        id_context: Used to identify the source of the identifier (e.g.
            IATA, ABTA, etc.).
    """
    class Meta:
        name = "UniqueID_Type"

    company_name: Optional[CompanyNameType] = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    instance: Optional[str] = field(
        default=None,
        metadata={
            "name": "Instance",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        }
    )
    id_context: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID_Context",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )


@dataclass
class ValidatingCarrierType:
    """
    Attributes
        preference:
        code: Validating Carrier code
    """
    preference: List["ValidatingCarrierType.Preference"] = field(
        default_factory=list,
        metadata={
            "name": "Preference",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )

    @dataclass
    class Preference:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9A-Z]{2,3}",
            }
        )
        level: Optional[ValidatingCarrierPreferLevelType] = field(
            default=None,
            metadata={
                "name": "Level",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class AirSearchPrefsType:
    """
    Defines user preferences to be used in conducting a search.

    Attributes
        vendor_pref: Specify vendors to include and exclude from the
            response.
        flight_type_pref: Defines preferred flight characteristics to be
            used in a search.
        fare_restrict_pref: Constrains a fare search to those with
            restrictions that satisfy user-imposed limitations.
        equip_pref: Defines preferred equipment profile(s) to be used in
            a search.
        cabin_pref: Defines preferred cabin(s) to be used in a search.
            The Cabin type specified in a
            OriginDestinationInformation/TPA_Extensions overrides this
            Cabin type for that specific segment/leg. If a Cabin type is
            not specified in a
            OriginDestinationInformation/TPA_Extensions the cabin type
            in this element will be used as default cabin type for that
            segment/leg.
        ticket_distrib_pref: Defines Distribution prefernces.
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        ancillary_fees:
        frequent_flyer: Frequent Flyer Status Information
        spanish_family_discount:
        interline_brands:
        smoking_allowed:
        on_time_rate: Request for flights in response that meet the
            given Department of Transport on-time rate. This is a number
            between 0 and 100.
        eticket_desired: Request flights that are e-ticketable in the
            response.
        valid_interline_ticket: Request options that are validated on
            base of interline ticketing aggrement.
        max_stops_quantity: Request flights that have no more than the
            requested number of stops.
        use_all_flights: Each flight should appear at least once.
        all_flights_data: Return flights not combinable into roundtrips
            as one ways is a separate section.
        hybrid: If false no solutions priced outside of ATSE systems
            will be returned in response for carriers operating in
            hybrid content distribution model.
    """
    vendor_pref: List[CompanyNamePrefType] = field(
        default_factory=list,
        metadata={
            "name": "VendorPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    flight_type_pref: Optional[FlightTypePrefType] = field(
        default=None,
        metadata={
            "name": "FlightTypePref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    fare_restrict_pref: List["AirSearchPrefsType.FareRestrictPref"] = field(
        default_factory=list,
        metadata={
            "name": "FareRestrictPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 4,
        }
    )
    equip_pref: List[EquipmentTypePref] = field(
        default_factory=list,
        metadata={
            "name": "EquipPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 9,
        }
    )
    cabin_pref: List[CabinPrefType] = field(
        default_factory=list,
        metadata={
            "name": "CabinPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
        }
    )
    ticket_distrib_pref: List[TicketDistribPrefType] = field(
        default_factory=list,
        metadata={
            "name": "TicketDistribPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
        }
    )
    tpa_extensions: Optional["AirSearchPrefsType.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    ancillary_fees: Optional["AirSearchPrefsType.AncillaryFees"] = field(
        default=None,
        metadata={
            "name": "AncillaryFees",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    frequent_flyer: List["AirSearchPrefsType.FrequentFlyer"] = field(
        default_factory=list,
        metadata={
            "name": "FrequentFlyer",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    spanish_family_discount: Optional["AirSearchPrefsType.SpanishFamilyDiscount"] = field(
        default=None,
        metadata={
            "name": "SpanishFamilyDiscount",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    interline_brands: Optional[InterlineBrandsType] = field(
        default=None,
        metadata={
            "name": "InterlineBrands",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    smoking_allowed: bool = field(
        default=False,
        metadata={
            "name": "SmokingAllowed",
            "type": "Attribute",
        }
    )
    on_time_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OnTimeRate",
            "type": "Attribute",
            "min_inclusive": Decimal("0.01"),
            "max_inclusive": Decimal("100.00"),
        }
    )
    eticket_desired: bool = field(
        default=False,
        metadata={
            "name": "ETicketDesired",
            "type": "Attribute",
        }
    )
    valid_interline_ticket: bool = field(
        default=False,
        metadata={
            "name": "ValidInterlineTicket",
            "type": "Attribute",
        }
    )
    max_stops_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxStopsQuantity",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        }
    )
    use_all_flights: bool = field(
        default=False,
        metadata={
            "name": "UseAllFlights",
            "type": "Attribute",
        }
    )
    all_flights_data: bool = field(
        default=False,
        metadata={
            "name": "AllFlightsData",
            "type": "Attribute",
        }
    )
    hybrid: bool = field(
        default=True,
        metadata={
            "name": "Hybrid",
            "type": "Attribute",
        }
    )

    @dataclass
    class FareRestrictPref(FareRestrictPrefType):
        """
        Attributes
            adv_res_ticketing: Identifies whether advance reservation or
                ticketing restrictions are acceptable in the search
                results.
            stay_restrictions: Identifies whether restrictions on
                minimum or maximum stays should be included in the
                search results.
            voluntary_changes: Identifies whether penalties associated
                with voluntary changes should be included in the search
                results.
        """
        adv_res_ticketing: Optional[AdvResTicketingType] = field(
            default=None,
            metadata={
                "name": "AdvResTicketing",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        stay_restrictions: Optional[StayRestrictionsType] = field(
            default=None,
            metadata={
                "name": "StayRestrictions",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        voluntary_changes: Optional[VoluntaryChangesType] = field(
            default=None,
            metadata={
                "name": "VoluntaryChanges",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

    @dataclass
    class TpaExtensions:
        """
        Attributes
            departure_window: This should be of the form HHMMHHMM.
            arrival_window: This should be of the form HHMMHHMM.
            exclude_vendor_pref: This element allows a user to exclude
                certain carriers from the search.
            include_alliance_pref: Consider only these alliances.
            exclude_alliance_pref: Do not consider these alliances.
            num_trips:
            alt_cities_combinations:
            num_trips_with_routing: This element allows a user to
                specify the number of itineraries with special routing
                returned.
            online_indicator:
            interline_indicator:
            trip_type: Specify air trip type.
            max_price: Maximum price returned from LFE service.
            content_type: Restrict content type returned by LFE service.
            domestic_layover_time: Domestic maximum connecting hours.
            long_connect_time: Change minimum and maximum connect time
                per connection in long connection schedules if Long
                Connect Time logic is enabled. Specified values should
                be less than 1440 minutes (24 hours).
            long_connect_points: Minimum and maximum number of
                connection points (not necessarily long) for Long
                Connections.
            air_service_only: Return air service only.
            jet_service_only: Return jet service only.
            same_connection_airport_only: Same airport at connection
                point restriction
            same_origin_airport_only: Same airport at origin point
                restriction
            same_turnaround_airport_only: Same airport at turnaround
                point restriction
            aircraft_type_penalty: Aircraft type penalty (in dollars).
                Used to penalize propeller aircraft type in the
                response.
            alternate_airport_penalty: Alternate airport penalty (in
                dollars). Used to penalize options with alternate
                airports.
            fare_amount_threshold: % ESV value above the lowest
                itinerary
            num_of_low_fare_sol: Number of low fare solutions for ESV2
            num_of_must_price_onl_sol: Number of must price online
                solutions for ESV2
            num_of_must_price_inrl_sol: Number of must price interline
                solutions for ESV2
            num_of_must_price_nstp_onl_sol: Number of must price non-
                stop online solutions for ESV2
            num_of_must_price_nstp_inrl_sol: Number of must price non-
                stop interline solutions for ESV2
            num_of_must_price_sstop_onl_sol: Number of must price single
                stop online solutions for ESV2
            stp_penalty_in_usd: Stop penalty in dollars for ESV2
            dur_penalty_in_usd: Duration penalty in dollars for ESV2
            dep_penalty_in_usd: Departure penalty in dollars for ESV2
            max_allowed_must_price_overage_per_crr: Max allowed must
                price overage per carrier for ESV2
            flt_opt_must_price_reuse_limit: Flight option reuse limit
                (must price) for ESV2
            upper_bound_must_price_factor_for_not_non_stp: Upper bound
                factor for not non-stops (must price) for ESV2
            upper_bound_lfsfactor: Low fare search upper bound factor
                for ESV2
            num_of_must_price_nstp1_stp_onl_sol: Number of must price
                non-stop/one-stop online solutions for ESV2
            num_of_must_price_nstp1_stp_inrl_sol: Number of must price
                non-stop/one-stop interline solutions for ESV2
            upper_bound_must_price_factor_for_non_stp: Upper bound
                factor for non-stops (must price) for ESV2
            max_allowed_lfsoverage_per_crr_percent: Low fare search max
                allowed overage per carrier % for ESV2
            target_min_num_of_lfsonl_sol_per_crr: Low fare search target
                minimum number of online solutions per carrier for ESV2
            target_min_num_of_lfstot_onl_sol_percent: Low fare search
                target minimum number of total online solutions % for
                ESV2
            flt_opt_lfsreuse_limit_for_non_avs: Low fare search flight
                option reuse limit for non AVS for ESV2
            flt_opt_lfsreuse_limit_for_avs: Low fare search flight
                option reuse limit for AVS for ESV2
            avs_penalty_crrs: AVS penalty carrier list (| delimited) for
                ESV2
            max_num_of_non_stp_onl_sol: Max number of nonstop online
                solutions for ESV2
            max_num_of_non_stp_inrl_sol: Max number of nonstop interline
                solutions for ESV2
            max_num_of_single_stp_onl_sol: Max number of single stop
                online solutions for ESV2
            max_num_of2_plus_stp_sol: Max number of 2+ stops solutions
                for ESV2
            min_allowed_overage_per_crr_percent: Min allowed overage per
                carrier % for ESV2
            min_allowed_overage_per_crr: Min allowed overage per carrier
                for ESV2
            max_rel_fare_lvl_ofx_for_non_stp: Max relative fare level of
                x for nonstops for ESV2
            max_rel_fare_lvl_ofx_for_cnx: Max relative fare level of x
                for carrier for ESV2
            num_of_must_price2_plus_stp_sol: Number of must price 2+
                stops solutions for ESV2
            itinerary_number_threshold: Number of preffered/good itins
                to price
            xofares:
            exempt_all_taxes: Exempt all taxes (/TE)
            exempt_all_taxes_and_fees: Exempt all taxes and fees (/TN)
            taxes: Specify Taxes (/TX)
            exempt_tax: Exempt Tax (/TE)
            flight_stops_as_connections:
            ticketing_sum_of_locals: Settings specific to Ticketing Sum
                of Locals processing
            multi_airport_codes: Settings specific to Multi Airport
                Codes processing
            jump_cabin_logic:
            keep_same_cabin:
            governing_carrier_override:
            exclude_call_direct_carriers:
            validating_carrier:
            validating_carrier_check:
            settlement_method:
            flight_repeat_limit:
            flexible_fares:
            diversity_parameters:
            additional_fare_limit:
            fare_focus_rules:
            selling_levels:
            budget: Budget Shopping settings
            options_per_date_pair_list: List of dates/date pairs with
                different requested number of options
            country_pref: List of countries to be excluded from
                processing
            retailer_rules:
        """
        departure_window: Optional[str] = field(
            default=None,
            metadata={
                "name": "DepartureWindow",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "pattern": r"([0-2][0-9][0-5][0-9]){2}",
            }
        )
        arrival_window: Optional[str] = field(
            default=None,
            metadata={
                "name": "ArrivalWindow",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "pattern": r"([0-2][0-9][0-5][0-9]){2}",
            }
        )
        exclude_vendor_pref: List["AirSearchPrefsType.TpaExtensions.ExcludeVendorPref"] = field(
            default_factory=list,
            metadata={
                "name": "ExcludeVendorPref",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        include_alliance_pref: List[AllianceType] = field(
            default_factory=list,
            metadata={
                "name": "IncludeAlliancePref",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        exclude_alliance_pref: List[AllianceType] = field(
            default_factory=list,
            metadata={
                "name": "ExcludeAlliancePref",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_trips: Optional[NumTripsType] = field(
            default=None,
            metadata={
                "name": "NumTrips",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        alt_cities_combinations: Optional[AltCitiesCombinationsType] = field(
            default=None,
            metadata={
                "name": "AltCitiesCombinations",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_trips_with_routing: Optional["AirSearchPrefsType.TpaExtensions.NumTripsWithRouting"] = field(
            default=None,
            metadata={
                "name": "NumTripsWithRouting",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        online_indicator: Optional["AirSearchPrefsType.TpaExtensions.OnlineIndicator"] = field(
            default=None,
            metadata={
                "name": "OnlineIndicator",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        interline_indicator: Optional["AirSearchPrefsType.TpaExtensions.InterlineIndicator"] = field(
            default=None,
            metadata={
                "name": "InterlineIndicator",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        trip_type: Optional["AirSearchPrefsType.TpaExtensions.TripType"] = field(
            default=None,
            metadata={
                "name": "TripType",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        max_price: Optional["AirSearchPrefsType.TpaExtensions.MaxPrice"] = field(
            default=None,
            metadata={
                "name": "MaxPrice",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        content_type: Optional["AirSearchPrefsType.TpaExtensions.ContentType"] = field(
            default=None,
            metadata={
                "name": "ContentType",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        domestic_layover_time: Optional["AirSearchPrefsType.TpaExtensions.DomesticLayoverTime"] = field(
            default=None,
            metadata={
                "name": "DomesticLayoverTime",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        long_connect_time: Optional["AirSearchPrefsType.TpaExtensions.LongConnectTime"] = field(
            default=None,
            metadata={
                "name": "LongConnectTime",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        long_connect_points: Optional["AirSearchPrefsType.TpaExtensions.LongConnectPoints"] = field(
            default=None,
            metadata={
                "name": "LongConnectPoints",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        air_service_only: Optional["AirSearchPrefsType.TpaExtensions.AirServiceOnly"] = field(
            default=None,
            metadata={
                "name": "AirServiceOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        jet_service_only: Optional["AirSearchPrefsType.TpaExtensions.JetServiceOnly"] = field(
            default=None,
            metadata={
                "name": "JetServiceOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        same_connection_airport_only: Optional["AirSearchPrefsType.TpaExtensions.SameConnectionAirportOnly"] = field(
            default=None,
            metadata={
                "name": "SameConnectionAirportOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        same_origin_airport_only: Optional["AirSearchPrefsType.TpaExtensions.SameOriginAirportOnly"] = field(
            default=None,
            metadata={
                "name": "SameOriginAirportOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        same_turnaround_airport_only: Optional["AirSearchPrefsType.TpaExtensions.SameTurnaroundAirportOnly"] = field(
            default=None,
            metadata={
                "name": "SameTurnaroundAirportOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        aircraft_type_penalty: Optional["AirSearchPrefsType.TpaExtensions.AircraftTypePenalty"] = field(
            default=None,
            metadata={
                "name": "AircraftTypePenalty",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        alternate_airport_penalty: Optional["AirSearchPrefsType.TpaExtensions.AlternateAirportPenalty"] = field(
            default=None,
            metadata={
                "name": "AlternateAirportPenalty",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        fare_amount_threshold: Optional["AirSearchPrefsType.TpaExtensions.FareAmountThreshold"] = field(
            default=None,
            metadata={
                "name": "FareAmountThreshold",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_of_low_fare_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfLowFareSol"] = field(
            default=None,
            metadata={
                "name": "numOfLowFareSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_of_must_price_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceOnlSol"] = field(
            default=None,
            metadata={
                "name": "numOfMustPriceOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_of_must_price_inrl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceInrlSol"] = field(
            default=None,
            metadata={
                "name": "numOfMustPriceInrlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_of_must_price_nstp_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstpOnlSol"] = field(
            default=None,
            metadata={
                "name": "numOfMustPriceNStpOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_of_must_price_nstp_inrl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstpInrlSol"] = field(
            default=None,
            metadata={
                "name": "numOfMustPriceNStpInrlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_of_must_price_sstop_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceSstopOnlSol"] = field(
            default=None,
            metadata={
                "name": "numOfMustPriceSStopOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        stp_penalty_in_usd: Optional["AirSearchPrefsType.TpaExtensions.StpPenaltyInUsd"] = field(
            default=None,
            metadata={
                "name": "stpPenaltyInUSD",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        dur_penalty_in_usd: Optional["AirSearchPrefsType.TpaExtensions.DurPenaltyInUsd"] = field(
            default=None,
            metadata={
                "name": "durPenaltyInUSD",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        dep_penalty_in_usd: Optional["AirSearchPrefsType.TpaExtensions.DepPenaltyInUsd"] = field(
            default=None,
            metadata={
                "name": "depPenaltyInUSD",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        max_allowed_must_price_overage_per_crr: Optional["AirSearchPrefsType.TpaExtensions.MaxAllowedMustPriceOveragePerCrr"] = field(
            default=None,
            metadata={
                "name": "maxAllowedMustPriceOveragePerCrr",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        flt_opt_must_price_reuse_limit: Optional["AirSearchPrefsType.TpaExtensions.FltOptMustPriceReuseLimit"] = field(
            default=None,
            metadata={
                "name": "fltOptMustPriceReuseLimit",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        upper_bound_must_price_factor_for_not_non_stp: Optional["AirSearchPrefsType.TpaExtensions.UpperBoundMustPriceFactorForNotNonStp"] = field(
            default=None,
            metadata={
                "name": "upperBoundMustPriceFactorForNotNonStp",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        upper_bound_lfsfactor: Optional["AirSearchPrefsType.TpaExtensions.UpperBoundLfsfactor"] = field(
            default=None,
            metadata={
                "name": "upperBoundLFSFactor",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_of_must_price_nstp1_stp_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstp1StpOnlSol"] = field(
            default=None,
            metadata={
                "name": "numOfMustPriceNStp1StpOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_of_must_price_nstp1_stp_inrl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstp1StpInrlSol"] = field(
            default=None,
            metadata={
                "name": "numOfMustPriceNStp1StpInrlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        upper_bound_must_price_factor_for_non_stp: Optional["AirSearchPrefsType.TpaExtensions.UpperBoundMustPriceFactorForNonStp"] = field(
            default=None,
            metadata={
                "name": "upperBoundMustPriceFactorForNonStp",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        max_allowed_lfsoverage_per_crr_percent: Optional["AirSearchPrefsType.TpaExtensions.MaxAllowedLfsoveragePerCrrPercent"] = field(
            default=None,
            metadata={
                "name": "maxAllowedLFSOveragePerCrrPercent",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        target_min_num_of_lfsonl_sol_per_crr: Optional["AirSearchPrefsType.TpaExtensions.TargetMinNumOfLfsonlSolPerCrr"] = field(
            default=None,
            metadata={
                "name": "targetMinNumOfLFSOnlSolPerCrr",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        target_min_num_of_lfstot_onl_sol_percent: Optional["AirSearchPrefsType.TpaExtensions.TargetMinNumOfLfstotOnlSolPercent"] = field(
            default=None,
            metadata={
                "name": "targetMinNumOfLFSTotOnlSolPercent",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        flt_opt_lfsreuse_limit_for_non_avs: Optional["AirSearchPrefsType.TpaExtensions.FltOptLfsreuseLimitForNonAvs"] = field(
            default=None,
            metadata={
                "name": "fltOptLFSReuseLimitForNonAVS",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        flt_opt_lfsreuse_limit_for_avs: Optional["AirSearchPrefsType.TpaExtensions.FltOptLfsreuseLimitForAvs"] = field(
            default=None,
            metadata={
                "name": "fltOptLFSReuseLimitForAVS",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        avs_penalty_crrs: Optional["AirSearchPrefsType.TpaExtensions.AvsPenaltyCrrs"] = field(
            default=None,
            metadata={
                "name": "avsPenaltyCrrs",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        max_num_of_non_stp_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.MaxNumOfNonStpOnlSol"] = field(
            default=None,
            metadata={
                "name": "maxNumOfNonStpOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        max_num_of_non_stp_inrl_sol: Optional["AirSearchPrefsType.TpaExtensions.MaxNumOfNonStpInrlSol"] = field(
            default=None,
            metadata={
                "name": "maxNumOfNonStpInrlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        max_num_of_single_stp_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.MaxNumOfSingleStpOnlSol"] = field(
            default=None,
            metadata={
                "name": "maxNumOfSingleStpOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        max_num_of2_plus_stp_sol: Optional["AirSearchPrefsType.TpaExtensions.MaxNumOf2PlusStpSol"] = field(
            default=None,
            metadata={
                "name": "maxNumOf2PlusStpSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        min_allowed_overage_per_crr_percent: Optional["AirSearchPrefsType.TpaExtensions.MinAllowedOveragePerCrrPercent"] = field(
            default=None,
            metadata={
                "name": "minAllowedOveragePerCrrPercent",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        min_allowed_overage_per_crr: Optional["AirSearchPrefsType.TpaExtensions.MinAllowedOveragePerCrr"] = field(
            default=None,
            metadata={
                "name": "minAllowedOveragePerCrr",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        max_rel_fare_lvl_ofx_for_non_stp: Optional["AirSearchPrefsType.TpaExtensions.MaxRelFareLvlOfxForNonStp"] = field(
            default=None,
            metadata={
                "name": "maxRelFareLvlOfxForNonStp",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        max_rel_fare_lvl_ofx_for_cnx: Optional["AirSearchPrefsType.TpaExtensions.MaxRelFareLvlOfxForCnx"] = field(
            default=None,
            metadata={
                "name": "maxRelFareLvlOfxForCnx",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        num_of_must_price2_plus_stp_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPrice2PlusStpSol"] = field(
            default=None,
            metadata={
                "name": "numOfMustPrice2PlusStpSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        itinerary_number_threshold: Optional["AirSearchPrefsType.TpaExtensions.ItineraryNumberThreshold"] = field(
            default=None,
            metadata={
                "name": "ItineraryNumberThreshold",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        xofares: Optional[XofaresType] = field(
            default=None,
            metadata={
                "name": "XOFares",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        exempt_all_taxes: Optional["AirSearchPrefsType.TpaExtensions.ExemptAllTaxes"] = field(
            default=None,
            metadata={
                "name": "ExemptAllTaxes",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        exempt_all_taxes_and_fees: Optional["AirSearchPrefsType.TpaExtensions.ExemptAllTaxesAndFees"] = field(
            default=None,
            metadata={
                "name": "ExemptAllTaxesAndFees",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        taxes: Optional["AirSearchPrefsType.TpaExtensions.Taxes"] = field(
            default=None,
            metadata={
                "name": "Taxes",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        exempt_tax: List[TaxCodeType] = field(
            default_factory=list,
            metadata={
                "name": "ExemptTax",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        flight_stops_as_connections: Optional[FlightStopsAsConnectionsType] = field(
            default=None,
            metadata={
                "name": "FlightStopsAsConnections",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        ticketing_sum_of_locals: Optional["AirSearchPrefsType.TpaExtensions.TicketingSumOfLocals"] = field(
            default=None,
            metadata={
                "name": "TicketingSumOfLocals",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        multi_airport_codes: Optional["AirSearchPrefsType.TpaExtensions.MultiAirportCodes"] = field(
            default=None,
            metadata={
                "name": "MultiAirportCodes",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        jump_cabin_logic: Optional[JumpCabinLogicType] = field(
            default=None,
            metadata={
                "name": "JumpCabinLogic",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        keep_same_cabin: Optional[KeepSameCabinType] = field(
            default=None,
            metadata={
                "name": "KeepSameCabin",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        governing_carrier_override: Optional[GoverningCarrierOverrideType] = field(
            default=None,
            metadata={
                "name": "GoverningCarrierOverride",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        exclude_call_direct_carriers: Optional["AirSearchPrefsType.TpaExtensions.ExcludeCallDirectCarriers"] = field(
            default=None,
            metadata={
                "name": "ExcludeCallDirectCarriers",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        validating_carrier: Optional[ValidatingCarrierType] = field(
            default=None,
            metadata={
                "name": "ValidatingCarrier",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        validating_carrier_check: Optional["AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck"] = field(
            default=None,
            metadata={
                "name": "ValidatingCarrierCheck",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        settlement_method: Optional[str] = field(
            default=None,
            metadata={
                "name": "SettlementMethod",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "pattern": r"[a-zA-Z0-9]{3}",
            }
        )
        flight_repeat_limit: Optional["AirSearchPrefsType.TpaExtensions.FlightRepeatLimit"] = field(
            default=None,
            metadata={
                "name": "FlightRepeatLimit",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        flexible_fares: Optional[FlexibleFaresType] = field(
            default=None,
            metadata={
                "name": "FlexibleFares",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        diversity_parameters: Optional["AirSearchPrefsType.TpaExtensions.DiversityParameters"] = field(
            default=None,
            metadata={
                "name": "DiversityParameters",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        additional_fare_limit: Optional["AirSearchPrefsType.TpaExtensions.AdditionalFareLimit"] = field(
            default=None,
            metadata={
                "name": "AdditionalFareLimit",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        fare_focus_rules: Optional["AirSearchPrefsType.TpaExtensions.FareFocusRules"] = field(
            default=None,
            metadata={
                "name": "FareFocusRules",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        selling_levels: Optional["AirSearchPrefsType.TpaExtensions.SellingLevels"] = field(
            default=None,
            metadata={
                "name": "SellingLevels",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        budget: Optional["AirSearchPrefsType.TpaExtensions.Budget"] = field(
            default=None,
            metadata={
                "name": "Budget",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        options_per_date_pair_list: Optional["AirSearchPrefsType.TpaExtensions.OptionsPerDatePairList"] = field(
            default=None,
            metadata={
                "name": "OptionsPerDatePairList",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        country_pref: List["AirSearchPrefsType.TpaExtensions.CountryPref"] = field(
            default_factory=list,
            metadata={
                "name": "CountryPref",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        retailer_rules: Optional[RetailerRulesType] = field(
            default=None,
            metadata={
                "name": "RetailerRules",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class ExcludeVendorPref:
            """
            Attributes
                code: Identifies a company by the company code.
            """
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "min_length": 1,
                    "max_length": 8,
                }
            )

        @dataclass
        class NumTripsWithRouting:
            number: int = field(
                default=5,
                metadata={
                    "name": "Number",
                    "type": "Attribute",
                    "min_inclusive": 1,
                }
            )

        @dataclass
        class TripType:
            value: Optional[AirTripType] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                }
            )

        @dataclass
        class MaxPrice:
            value: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "fraction_digits": 3,
                }
            )

        @dataclass
        class ContentType:
            type: Optional[ContentTypeType] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )

        @dataclass
        class DomesticLayoverTime:
            hours: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Hours",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class LongConnectTime:
            min: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Min",
                    "type": "Attribute",
                }
            )
            max: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Max",
                    "type": "Attribute",
                }
            )
            enable: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Enable",
                    "type": "Attribute",
                }
            )

        @dataclass
        class LongConnectPoints:
            min: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Min",
                    "type": "Attribute",
                }
            )
            max: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Max",
                    "type": "Attribute",
                }
            )

        @dataclass
        class AirServiceOnly:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class JetServiceOnly:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class SameConnectionAirportOnly:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class SameOriginAirportOnly:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class SameTurnaroundAirportOnly:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class AircraftTypePenalty:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class AlternateAirportPenalty:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class FareAmountThreshold:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class NumOfLowFareSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class NumOfMustPriceOnlSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class NumOfMustPriceInrlSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class NumOfMustPriceNstpOnlSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class NumOfMustPriceNstpInrlSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class NumOfMustPriceSstopOnlSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class StpPenaltyInUsd:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class DurPenaltyInUsd:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class DepPenaltyInUsd:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MaxAllowedMustPriceOveragePerCrr:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class FltOptMustPriceReuseLimit:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class UpperBoundMustPriceFactorForNotNonStp:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class UpperBoundLfsfactor:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class NumOfMustPriceNstp1StpOnlSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class NumOfMustPriceNstp1StpInrlSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class UpperBoundMustPriceFactorForNonStp:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MaxAllowedLfsoveragePerCrrPercent:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class TargetMinNumOfLfsonlSolPerCrr:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class TargetMinNumOfLfstotOnlSolPercent:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class FltOptLfsreuseLimitForNonAvs:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class FltOptLfsreuseLimitForAvs:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class AvsPenaltyCrrs:
            value: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MaxNumOfNonStpOnlSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MaxNumOfNonStpInrlSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MaxNumOfSingleStpOnlSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MaxNumOf2PlusStpSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MinAllowedOveragePerCrrPercent:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MinAllowedOveragePerCrr:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MaxRelFareLvlOfxForNonStp:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class MaxRelFareLvlOfxForCnx:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class NumOfMustPrice2PlusStpSol:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class ItineraryNumberThreshold:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class TicketingSumOfLocals:
            """
            Attributes
                enable: Enable Ticketing Sum of Locals processing.
            """
            enable: bool = field(
                default=False,
                metadata={
                    "name": "Enable",
                    "type": "Attribute",
                }
            )

        @dataclass
        class MultiAirportCodes:
            """
            Attributes
                enable_open_jaw: Enable open jaw leg combinations.
            """
            enable_open_jaw: bool = field(
                default=False,
                metadata={
                    "name": "EnableOpenJaw",
                    "type": "Attribute",
                }
            )

        @dataclass
        class ExcludeCallDirectCarriers:
            """
            Attributes
                enabled: Force DSF to return schedules only for carriers
                    bookable by Sabre.
            """
            enabled: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Enabled",
                    "type": "Attribute",
                }
            )

        @dataclass
        class ValidatingCarrierCheck:
            settlement_validation: Optional["AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.SettlementValidation"] = field(
                default=None,
                metadata={
                    "name": "SettlementValidation",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                }
            )
            ietvalidation: Optional["AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.Ietvalidation"] = field(
                default=None,
                metadata={
                    "name": "IETValidation",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                }
            )
            carrier: List["AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.Carrier"] = field(
                default_factory=list,
                metadata={
                    "name": "Carrier",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            country: List["AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.Country"] = field(
                default_factory=list,
                metadata={
                    "name": "Country",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )

            @dataclass
            class SettlementValidation:
                """
                If set to true validate BSP agreement for given carriers.
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class Ietvalidation:
                """
                If set to true validate IET agreement for listed countries.
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class Carrier:
                code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9A-Z]{2,3}",
                    }
                )

            @dataclass
            class Country:
                code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[a-zA-Z]{2}",
                    }
                )

        @dataclass
        class FlightRepeatLimit:
            """
            Attributes
                value: Flight Repeat Limit for DSF. Expected value
                    1-100.
            """
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class DiversityParameters:
            """
            Attributes
                weightings: Defines how important various parameter
                    options are in the response. Sum of all weightings
                    needs to equal 10.
                time_of_day_distribution: Defines how the options in the
                    response should be distributed between certain
                    departure time of day ranges. All defined
                    TimeOfDayRanges need to cover the whole day and the
                    sum of all Percentages needs to equal 100.
                inbound_outbound_pairing: Defines the requested ratio of
                    inbounds to outbounds in the response.
                additional_non_stops_number: Defines how many additional
                    non-stop options should be added to the response.
                    Overrides @Percentage.
                additional_non_stops_percentage: Defines how many
                    additional non-stop options should be added to the
                    response as a percentage of the requested number of
                    options.
            """
            weightings: Optional["AirSearchPrefsType.TpaExtensions.DiversityParameters.Weightings"] = field(
                default=None,
                metadata={
                    "name": "Weightings",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            time_of_day_distribution: Optional["AirSearchPrefsType.TpaExtensions.DiversityParameters.TimeOfDayDistribution"] = field(
                default=None,
                metadata={
                    "name": "TimeOfDayDistribution",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            inbound_outbound_pairing: Optional[int] = field(
                default=None,
                metadata={
                    "name": "InboundOutboundPairing",
                    "type": "Attribute",
                    "min_inclusive": 1,
                    "max_inclusive": 1000,
                }
            )
            additional_non_stops_number: Optional[int] = field(
                default=None,
                metadata={
                    "name": "AdditionalNonStopsNumber",
                    "type": "Attribute",
                    "min_inclusive": 1,
                }
            )
            additional_non_stops_percentage: Optional[int] = field(
                default=None,
                metadata={
                    "name": "AdditionalNonStopsPercentage",
                    "type": "Attribute",
                    "min_inclusive": 0,
                    "max_inclusive": 100,
                }
            )

            @dataclass
            class Weightings:
                """
                Attributes
                    price_weight: Defines how important price options
                        are on a scale from 0 to 10.
                    travel_time_weight: Defines how important travel
                        time options are on a scale from 0 to 10.
                """
                price_weight: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "PriceWeight",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0,
                        "max_inclusive": 10,
                    }
                )
                travel_time_weight: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "TravelTimeWeight",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0,
                        "max_inclusive": 10,
                    }
                )

            @dataclass
            class TimeOfDayDistribution:
                time_of_day_range: List["AirSearchPrefsType.TpaExtensions.DiversityParameters.TimeOfDayDistribution.TimeOfDayRange"] = field(
                    default_factory=list,
                    metadata={
                        "name": "TimeOfDayRange",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "min_occurs": 2,
                        "max_occurs": 4,
                    }
                )

                @dataclass
                class TimeOfDayRange:
                    """
                    Attributes
                        begin: Beginning of the TimeOfDayRange in HHMM
                            format.
                        end: End of the TimeOfDayRange in HHMM format.
                        percentage: Defines how many percent options
                            should be in the TimeOfDayRange.
                    """
                    begin: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Begin",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
                        }
                    )
                    end: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "End",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
                        }
                    )
                    percentage: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "Percentage",
                            "type": "Attribute",
                            "required": True,
                            "min_inclusive": 0,
                            "max_inclusive": 100,
                        }
                    )

        @dataclass
        class AdditionalFareLimit:
            """
            Attributes
                value: Additional fare limit.
            """
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class FareFocusRules:
            """
            Attributes
                exclude: Exclude fare focus rules.
            """
            exclude: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Exclude",
                    "type": "Attribute",
                }
            )

        @dataclass
        class SellingLevels:
            selling_level_rules: Optional["AirSearchPrefsType.TpaExtensions.SellingLevels.SellingLevelRules"] = field(
                default=None,
                metadata={
                    "name": "SellingLevelRules",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            show_fare_amounts: Optional["AirSearchPrefsType.TpaExtensions.SellingLevels.ShowFareAmounts"] = field(
                default=None,
                metadata={
                    "name": "ShowFareAmounts",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )

            @dataclass
            class SellingLevelRules:
                """
                Attributes
                    ignore: Force ignore adjustment selling level rules
                """
                ignore: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Ignore",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class ShowFareAmounts:
                """
                Attributes
                    original: Show original selling fare level amounts
                        and total adjusted amount in Fare Calc line
                    adjusted: Show selling level amounts and total
                        adjusted amount in Fare Calc line
                """
                original: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Original",
                        "type": "Attribute",
                    }
                )
                adjusted: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Adjusted",
                        "type": "Attribute",
                    }
                )

        @dataclass
        class Budget:
            """
            Attributes
                minimum_price: Minimum price to include in response
                maximum_price: Maximum price to include in response
                relative_price_threshold: Relative price difference
                    threshold to be respected while choosing alternative
                    options
            """
            minimum_price: Optional[object] = field(
                default=None,
                metadata={
                    "name": "MinimumPrice",
                    "type": "Attribute",
                }
            )
            maximum_price: Optional[object] = field(
                default=None,
                metadata={
                    "name": "MaximumPrice",
                    "type": "Attribute",
                }
            )
            relative_price_threshold: Optional[str] = field(
                default=None,
                metadata={
                    "name": "RelativePriceThreshold",
                    "type": "Attribute",
                    "pattern": r"0|-?[1-9][0-9]*%?",
                }
            )

        @dataclass
        class OptionsPerDatePairList:
            options_per_date_pair: List[OptionsPerDatePairType] = field(
                default_factory=list,
                metadata={
                    "name": "OptionsPerDatePair",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                }
            )

        @dataclass
        class CountryPref:
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[a-zA-Z]{2}",
                }
            )
            prefer_level: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PreferLevel",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"Unacceptable",
                }
            )

        @dataclass
        class OnlineIndicator:
            """
            Attributes
                ind: Specifies if the associated data is formatted or
                    not. If true, then it is formatted, if false, then
                    not formatted.
            """
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                }
            )

        @dataclass
        class InterlineIndicator:
            """
            Attributes
                ind: Specifies if the associated data is formatted or
                    not. If true, then it is formatted, if false, then
                    not formatted.
            """
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                }
            )

        @dataclass
        class ExemptAllTaxes:
            value: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class ExemptAllTaxesAndFees:
            value: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class Taxes:
            """
            Attributes
                tax: Specify tax amount and code.
            """
            tax: List[TaxCodeAmountType] = field(
                default_factory=list,
                metadata={
                    "name": "Tax",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )

    @dataclass
    class AncillaryFees:
        """
        Attributes
            ancillary_fee_group: List of requested groups
            enable: Enable Ancillary Fees processing path.
            summary: Flag whether this is a summary request.
        """
        ancillary_fee_group: List["AirSearchPrefsType.AncillaryFees.AncillaryFeeGroup"] = field(
            default_factory=list,
            metadata={
                "name": "AncillaryFeeGroup",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        enable: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Enable",
                "type": "Attribute",
                "required": True,
            }
        )
        summary: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Summary",
                "type": "Attribute",
            }
        )

        @dataclass
        class AncillaryFeeGroup:
            """
            Attributes
                code: Group code
                count: Number of items
            """
            code: Optional[object] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                }
            )
            count: Optional[object] = field(
                default=None,
                metadata={
                    "name": "Count",
                    "type": "Attribute",
                }
            )

    @dataclass
    class FrequentFlyer:
        """
        Attributes
            status: Frequent Flyer Status
            airline_code: Airline Carrier Code
        """
        status: Optional[int] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Attribute",
                "required": True,
            }
        )
        airline_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "AirlineCode",
                "type": "Attribute",
            }
        )

    @dataclass
    class SpanishFamilyDiscount:
        """
        Attributes
            level: Spanish Large Family Discount Level. Valid values are
                1 or 2.
        """
        level: Optional[SpanishFamilyDiscountLevel] = field(
            default=None,
            metadata={
                "name": "Level",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class AirTravelerType:
    """Information about the person traveling.

    Gender - the gender of the customer, if needed. BirthDate - Date of Birth. Currency - the preferred currency in which monetary amounts should be returned.

    Attributes
        profile_ref: Stored information about a customer. May contain
            readily available information relevant to the booking.
        person_name:
        telephone:
        email:
        address:
        cust_loyalty: Specify a customer loyalty program.
        document:
        passenger_type_quantity: Define information on the number of
            passengers of a specific type.
        traveler_ref_number: Direct reference of traveler assigned by
            requesting system. Used as a cross reference between data
            segments.
        flight_segment_rphs: Reference pointers to flight segments
        gender:
        share_synch_ind:
        share_market_ind:
        birth_date: Date of Birth.
        currency_code: The preferred currency in which monetary amounts
            should be returned.
        passenger_type_code: A three-letter code representing passenger
            type (e.g. .ADT. for adult, .CNN. for child)
        accompanied_by_infant: Indicates if an infant accompanying a
            traveler is with or without a seat.
    """
    profile_ref: Optional["AirTravelerType.ProfileRef"] = field(
        default=None,
        metadata={
            "name": "ProfileRef",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    person_name: Optional[PersonNameType] = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    telephone: List[TelephoneType] = field(
        default_factory=list,
        metadata={
            "name": "Telephone",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
        }
    )
    email: List[EmailType] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
        }
    )
    address: List[AddressType] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
        }
    )
    cust_loyalty: List[CustLoyaltyType] = field(
        default_factory=list,
        metadata={
            "name": "CustLoyalty",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
        }
    )
    document: List[DocumentType] = field(
        default_factory=list,
        metadata={
            "name": "Document",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 10,
        }
    )
    passenger_type_quantity: Optional[PassengerTypeQuantityType] = field(
        default=None,
        metadata={
            "name": "PassengerTypeQuantity",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    traveler_ref_number: Optional[TravelerRefNumberType] = field(
        default=None,
        metadata={
            "name": "TravelerRefNumber",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    flight_segment_rphs: Optional["AirTravelerType.FlightSegmentRphs"] = field(
        default=None,
        metadata={
            "name": "FlightSegmentRPHs",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    gender: Optional[AirTravelerTypeGender] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
        }
    )
    share_synch_ind: Optional[AirTravelerTypeShareSynchInd] = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        }
    )
    share_market_ind: Optional[AirTravelerTypeShareMarketInd] = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        }
    )
    birth_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Attribute",
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    passenger_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    accompanied_by_infant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccompaniedByInfant",
            "type": "Attribute",
        }
    )

    @dataclass
    class ProfileRef:
        unique_id: Optional[UniqueIdType] = field(
            default=None,
            metadata={
                "name": "UniqueID",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "required": True,
            }
        )

    @dataclass
    class FlightSegmentRphs:
        """
        Attributes
            flight_segment_rph: Reference to the flight segments for
                this traveler
        """
        flight_segment_rph: List[str] = field(
            default_factory=list,
            metadata={
                "name": "FlightSegmentRPH",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 99,
                "pattern": r"[0-9]{1,8}",
            }
        )


@dataclass
class ExchangeSourceType:
    """
    Attributes
        booking_channel:
        agent_sine: Identifies the party within the requesting entity.
        pseudo_city_code: An identification code assigned to an
            office/agency by a reservation system.
        isocountry: The country code of the requesting party.
        isocurrency: The currency code in which the reservation will be
            ticketed.
        agent_duty_code: An authority code assigned to a requestor.
        airline_vendor_id: The IATA assigned airline code.
        airport_code: The IATA assigned airport code.
        first_depart_point: The point of first departure in a trip.
        ersp_user_id: Electronic Reservation Service Provider (ERSP)
            assigned identifier used to identify the individual using
            the ERSP system.
        personal_city_code: City code part of Office Accounting Code
        accounting_code: Accounting Code part of Office Accounting Code
        office_code: Office Code part of Office Accounting Code
        default_ticketing_carrier: Default Ticketing Carrier for Office
            Accounting Code
        airline_channel_code: Airline Channel Code
        agent_department_code: Agent department code
        agent_function: Agent function
        travel_agency_iata: Travel agency IATA
        home_agency_iata: Home agency IATA
        agent_iata: Agent IATA
        vendor_crscode: Vendor CRS code
        agent_duty: Agent duty
        abacus_user: Abacus user
        agent_city: Agent city
        main_travel_agency_pcc: Main travel agency PCC
        carrier: Carrier
        host_carrier: PCC Host Carrier
        eticket_capable: Agency is Eticket capable
        co_host_id: CoHostID
    """
    booking_channel: Optional[SourceBookingChannelType] = field(
        default=None,
        metadata={
            "name": "BookingChannel",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    agent_sine: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentSine",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    isocountry: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISOCountry",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{2}",
        }
    )
    isocurrency: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISOCurrency",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    agent_duty_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentDutyCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    airline_vendor_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirlineVendorID",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2,3}",
        }
    )
    airport_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirportCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{3,5}",
        }
    )
    first_depart_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstDepartPoint",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 3,
        }
    )
    ersp_user_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ERSP_UserID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    personal_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PersonalCityCode",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{3,4}",
        }
    )
    accounting_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountingCode",
            "type": "Attribute",
            "pattern": r"[0-9a-zA-Z]{2,3}",
        }
    )
    office_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "OfficeCode",
            "type": "Attribute",
            "pattern": r"[0-9]{7}",
        }
    )
    default_ticketing_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultTicketingCarrier",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2}[A-Z]?",
        }
    )
    airline_channel_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirlineChannelCode",
            "type": "Attribute",
            "pattern": r"[A-Z]{3}",
        }
    )
    agent_department_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentDepartmentCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    agent_function: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentFunction",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    travel_agency_iata: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelAgencyIATA",
            "type": "Attribute",
            "pattern": r"[0-9]{1,14}",
        }
    )
    home_agency_iata: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomeAgencyIATA",
            "type": "Attribute",
            "pattern": r"[0-9]{1,14}",
        }
    )
    agent_iata: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentIATA",
            "type": "Attribute",
            "pattern": r"[0-9]{1,14}",
        }
    )
    vendor_crscode: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorCRSCode",
            "type": "Attribute",
        }
    )
    agent_duty: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentDuty",
            "type": "Attribute",
            "length": 1,
        }
    )
    abacus_user: bool = field(
        default=False,
        metadata={
            "name": "AbacusUser",
            "type": "Attribute",
        }
    )
    agent_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentCity",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    main_travel_agency_pcc: Optional[str] = field(
        default=None,
        metadata={
            "name": "MainTravelAgencyPCC",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
    host_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "HostCarrier",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
    eticket_capable: bool = field(
        default=False,
        metadata={
            "name": "ETicketCapable",
            "type": "Attribute",
        }
    )
    co_host_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CoHostID",
            "type": "Attribute",
        }
    )


@dataclass
class ExchangeTravelPreferencesTpaExtensionsType:
    """
    Attributes
        exempt_all_taxes: Exempt all taxes (/TE)
        exempt_all_taxes_and_fees: Exempt all taxes and fees (/TN)
        taxes: Specify Taxes (/TX)
        exempt_tax: Exempt Tax (/TE)
        settlement_method:
    """
    class Meta:
        name = "ExchangeTravelPreferencesTPA_ExtensionsType"

    exempt_all_taxes: Optional["ExchangeTravelPreferencesTpaExtensionsType.ExemptAllTaxes"] = field(
        default=None,
        metadata={
            "name": "ExemptAllTaxes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    exempt_all_taxes_and_fees: Optional["ExchangeTravelPreferencesTpaExtensionsType.ExemptAllTaxesAndFees"] = field(
        default=None,
        metadata={
            "name": "ExemptAllTaxesAndFees",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    taxes: Optional["ExchangeTravelPreferencesTpaExtensionsType.Taxes"] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    exempt_tax: List[TaxCodeType] = field(
        default_factory=list,
        metadata={
            "name": "ExemptTax",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    settlement_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "SettlementMethod",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"[a-zA-Z0-9]{3}",
        }
    )

    @dataclass
    class ExemptAllTaxes:
        value: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ExemptAllTaxesAndFees:
        value: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Taxes:
        """
        Attributes
            tax: Specify tax amount and code.
        """
        tax: List[TaxCodeAmountType] = field(
            default_factory=list,
            metadata={
                "name": "Tax",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )


@dataclass
class OriginDestinationInformationType(TravelDateTimeType):
    """Origin and Destination location, and time information for the request.

    Also includes the ability to specify a connection location for the
    search.

    Attributes
        origin_location: Travel Origin Location - for example, air uses
            the IATA 3 letter code.
        destination_location: Travel Destination Location - for example,
            air uses the IATA 3 letter code.
        connection_locations: Travel Connection Location - for example,
            air uses the IATA 3 letter code.
    """
    origin_location: Optional["OriginDestinationInformationType.OriginLocation"] = field(
        default=None,
        metadata={
            "name": "OriginLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    destination_location: Optional["OriginDestinationInformationType.DestinationLocation"] = field(
        default=None,
        metadata={
            "name": "DestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    connection_locations: Optional[ConnectionType] = field(
        default=None,
        metadata={
            "name": "ConnectionLocations",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )

    @dataclass
    class OriginLocation(RequestLocationType):
        """
        Attributes
            all_airports: Flag indicating if all cached origin cities
                are to be processed as origin airports.
        """
        all_airports: Optional[bool] = field(
            default=None,
            metadata={
                "name": "AllAirports",
                "type": "Attribute",
            }
        )

    @dataclass
    class DestinationLocation(RequestLocationType):
        """
        Attributes
            all_airports: Flag indicating if all cached destination
                cities are to be processed as destination airports.
        """
        all_airports: Optional[bool] = field(
            default=None,
            metadata={
                "name": "AllAirports",
                "type": "Attribute",
            }
        )


@dataclass
class SourceType:
    """
    Attributes
        requestor_id: An identifier of the entity making the request
            (e.g. ATA/IATA/ID number, Electronic Reservation Service
            Provider (ERSP), Association of British Travel Agents
            (ABTA)).
        position:
        booking_channel:
        agent_sine: Identifies the party within the requesting entity.
        pseudo_city_code: An identification code assigned to an
            office/agency by a reservation system.
        isocountry: The country code of the requesting party.
        isocurrency: The currency code in which the reservation will be
            ticketed.
        agent_duty_code: An authority code assigned to a requestor.
        airline_vendor_id: The IATA assigned airline code.
        airport_code: The IATA assigned airport code.
        first_depart_point: The point of first departure in a trip.
        ersp_user_id: Electronic Reservation Service Provider (ERSP)
            assigned identifier used to identify the individual using
            the ERSP system.
        personal_city_code: City code part of Office Accounting Code
        accounting_code: Accounting Code part of Office Accounting Code
        office_code: Office Code part of Office Accounting Code
        default_ticketing_carrier: Default Ticketing Carrier for Office
            Accounting Code
        airline_channel_code: Airline Channel Code
        agent_department_code: Agent department code
        agent_function: Agent function
        travel_agency_iata: Travel agency IATA
        home_agency_iata: Home agency IATA
        agent_iata: Agent IATA
        vendor_crscode: Vendor CRS code
        agent_duty: Agent duty
        abacus_user: Abacus user
        agent_city: Agent city
        carrier: Carrier
        main_travel_agency_pcc: Main travel agency PCC
        home_pcc: Home PCC
    """
    requestor_id: Optional[UniqueIdType] = field(
        default=None,
        metadata={
            "name": "RequestorID",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    position: Optional[PositionType] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    booking_channel: Optional[SourceBookingChannelType] = field(
        default=None,
        metadata={
            "name": "BookingChannel",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    agent_sine: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentSine",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    isocountry: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISOCountry",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{2}",
        }
    )
    isocurrency: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISOCurrency",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    agent_duty_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentDutyCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    airline_vendor_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirlineVendorID",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2,3}",
        }
    )
    airport_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirportCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{3,5}",
        }
    )
    first_depart_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstDepartPoint",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 3,
        }
    )
    ersp_user_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ERSP_UserID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    personal_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PersonalCityCode",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{3,4}",
        }
    )
    accounting_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountingCode",
            "type": "Attribute",
            "pattern": r"[0-9a-zA-Z]{2,3}",
        }
    )
    office_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "OfficeCode",
            "type": "Attribute",
            "pattern": r"[0-9]{7}",
        }
    )
    default_ticketing_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultTicketingCarrier",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2}[A-Z]?",
        }
    )
    airline_channel_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirlineChannelCode",
            "type": "Attribute",
            "pattern": r"[A-Z]{3}",
        }
    )
    agent_department_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentDepartmentCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    agent_function: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentFunction",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    travel_agency_iata: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelAgencyIATA",
            "type": "Attribute",
            "pattern": r"[0-9]{1,14}",
        }
    )
    home_agency_iata: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomeAgencyIATA",
            "type": "Attribute",
            "pattern": r"[0-9]{1,14}",
        }
    )
    agent_iata: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentIATA",
            "type": "Attribute",
            "pattern": r"[0-9]{1,14}",
        }
    )
    vendor_crscode: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorCRSCode",
            "type": "Attribute",
        }
    )
    agent_duty: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentDuty",
            "type": "Attribute",
            "length": 1,
        }
    )
    abacus_user: bool = field(
        default=False,
        metadata={
            "name": "AbacusUser",
            "type": "Attribute",
        }
    )
    agent_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentCity",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
    main_travel_agency_pcc: Optional[str] = field(
        default=None,
        metadata={
            "name": "MainTravelAgencyPCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    home_pcc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomePCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )


@dataclass
class TransactionType:
    """
    IntelliSell Type.

    Attributes
        request_type: Identifier of the type of request.
        service_tag: Identifier of the transaction path.
        purchase_type: A target available for user, that can be used to
            create specific rules. For example, if the client wants to
            target preferred customer request, we can use this element
            to achieve this.
        sabre_ath: Sabre authentication ID (ATH) - passed into the
            request to keep session information when communicating with
            TPF. The use of this element had been deprecated and is
            achieved by session pooling mechanism in Intellisell.
        tran_id: Transaction ID.
        client_session_id: A unique identifier to relate all
            transactions within a single session. Used by AirShop/LFE
            transactions.
        branch: Attribute of the Rule that can be passed in to
            selectively target a rule. This has been deprecated.
        compress_response: Decides if the response should be compressed.
        fare_overrides: Contains a sequence of fare overrides.
        diagnostics: For internal use
        subagent_data: Subagent data for LFE transactions.
        response_sorting: Settings for IntelliSell merchandising
        seat_status_sim:
        available_level:
        atsetest: Allows ATSE Team to test new features. This element
            and its content is meant to never be published.
        debug: Turns on or off debug mode.
        debug_key: Key unlocking disabled debug mode.
        config_set: Alternative configuration selector.
        disable_cache: Disables itinerary cache for this request (if it
            is enabled in this service).
        chunk_number: Helps Forwarder in keeping track of response parts
            generated as a result of request processing (AB only).
        show_itin_source: If enabled, Intellisell will return source for
            each itinerary.
    """
    request_type: Optional["TransactionType.RequestType"] = field(
        default=None,
        metadata={
            "name": "RequestType",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    service_tag: Optional["TransactionType.ServiceTag"] = field(
        default=None,
        metadata={
            "name": "ServiceTag",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    purchase_type: Optional["TransactionType.PurchaseType"] = field(
        default=None,
        metadata={
            "name": "PurchaseType",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    sabre_ath: Optional["TransactionType.SabreAth"] = field(
        default=None,
        metadata={
            "name": "SabreAth",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    tran_id: Optional["TransactionType.TranId"] = field(
        default=None,
        metadata={
            "name": "TranID",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    client_session_id: Optional["TransactionType.ClientSessionId"] = field(
        default=None,
        metadata={
            "name": "ClientSessionID",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    branch: Optional["TransactionType.Branch"] = field(
        default=None,
        metadata={
            "name": "Branch",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    compress_response: Optional["TransactionType.CompressResponse"] = field(
        default=None,
        metadata={
            "name": "CompressResponse",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    fare_overrides: Optional["TransactionType.FareOverrides"] = field(
        default=None,
        metadata={
            "name": "FareOverrides",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    diagnostics: Optional["TransactionType.Diagnostics"] = field(
        default=None,
        metadata={
            "name": "Diagnostics",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    subagent_data: Optional["TransactionType.SubagentData"] = field(
        default=None,
        metadata={
            "name": "SubagentData",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    response_sorting: Optional["TransactionType.ResponseSorting"] = field(
        default=None,
        metadata={
            "name": "ResponseSorting",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    seat_status_sim: Optional[SeatStatusSimType] = field(
        default=None,
        metadata={
            "name": "SeatStatusSim",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    available_level: Optional["TransactionType.AvailableLevel"] = field(
        default=None,
        metadata={
            "name": "AvailableLevel",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    atsetest: Optional["TransactionType.Atsetest"] = field(
        default=None,
        metadata={
            "name": "ATSETest",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    debug: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Debug",
            "type": "Attribute",
        }
    )
    debug_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "DebugKey",
            "type": "Attribute",
        }
    )
    config_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfigSet",
            "type": "Attribute",
        }
    )
    disable_cache: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisableCache",
            "type": "Attribute",
        }
    )
    chunk_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChunkNumber",
            "type": "Attribute",
        }
    )
    show_itin_source: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowItinSource",
            "type": "Attribute",
        }
    )

    @dataclass
    class RequestType:
        value: str = field(
            default="",
            metadata={
                "required": True,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )

    @dataclass
    class ServiceTag:
        value: str = field(
            default="",
            metadata={
                "required": True,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )

    @dataclass
    class PurchaseType:
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )

    @dataclass
    class SabreAth:
        value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
            }
        )
        binary_sec_token: Optional[str] = field(
            default=None,
            metadata={
                "name": "BinarySecToken",
                "type": "Attribute",
            }
        )
        conversation_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "ConversationID",
                "type": "Attribute",
            }
        )

    @dataclass
    class TranId:
        value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
            }
        )

    @dataclass
    class ClientSessionId:
        value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
            }
        )

    @dataclass
    class Branch:
        name: str = field(
            default="Main",
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )

    @dataclass
    class CompressResponse:
        value: bool = field(
            default=False,
            metadata={
                "name": "Value",
                "type": "Attribute",
            }
        )

    @dataclass
    class FareOverrides:
        """
        Attributes
            fare_override: Contains attributes of the FareGroup
                functionality used during shopping and pricing. If
                passed in this request, it will override setting in the
                rule.
        """
        fare_override: List["TransactionType.FareOverrides.FareOverride"] = field(
            default_factory=list,
            metadata={
                "name": "FareOverride",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 4,
            }
        )

        @dataclass
        class FareOverride:
            """
            Attributes
                vendor_pref: Specify vendors to include and exclude from
                    the response.
                tpa_extensions: This is a place holder for additional
                    elements.
                fare_type: Attribute of FareGroup functionality, used in
                    search of fares during shopping.
                pseudo_city_code:
                corporate_id: Attribute of FareGroup functionality, used
                    in search of fares during shopping.
                callable: Indicator to enable/disable this FareOverride.
            """
            vendor_pref: List[CompanyNamePrefType] = field(
                default_factory=list,
                metadata={
                    "name": "VendorPref",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            tpa_extensions: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            fare_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "FareType",
                    "type": "Attribute",
                    "required": True,
                }
            )
            pseudo_city_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PseudoCityCode",
                    "type": "Attribute",
                }
            )
            corporate_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CorporateID",
                    "type": "Attribute",
                }
            )
            callable: str = field(
                default="true",
                metadata={
                    "name": "Callable",
                    "type": "Attribute",
                }
            )

    @dataclass
    class Diagnostics:
        """
        Attributes
            diagnostic: Specify diagnostic code and which service to
                sent it to.
        """
        diagnostic: List["TransactionType.Diagnostics.Diagnostic"] = field(
            default_factory=list,
            metadata={
                "name": "Diagnostic",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Diagnostic:
            """
            Attributes
                diagnostic_argument: Name-value pairs to be used as
                    arguments for the diagnostic.
                tpa_extensions: This is a place holder for additional
                    elements.
                target:
                code:
            """
            diagnostic_argument: List["TransactionType.Diagnostics.Diagnostic.DiagnosticArgument"] = field(
                default_factory=list,
                metadata={
                    "name": "DiagnosticArgument",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            tpa_extensions: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            target: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Target",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[A-Za-z0-9_]+(/[A-Za-z0-9_]+)*",
                }
            )

            @dataclass
            class DiagnosticArgument:
                name: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Name",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                value: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Value",
                        "type": "Attribute",
                    }
                )

    @dataclass
    class SubagentData:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )

    @dataclass
    class ResponseSorting:
        enable_chronological_sorting: Optional[bool] = field(
            default=None,
            metadata={
                "name": "EnableChronologicalSorting",
                "type": "Attribute",
            }
        )

    @dataclass
    class AvailableLevel:
        value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Atsetest:
        """
        Attributes
            feature: Meaning of that attribute is dependent on MIP Team,
                ISell sends it in all ShoppingRequests when specified.
        """
        feature: Optional[str] = field(
            default=None,
            metadata={
                "name": "Feature",
                "type": "Attribute",
            }
        )


@dataclass
class ExchangeAirSearchPrefsType:
    """
    Attributes
        tpa_extensions:
        valid_interline_ticket: Request itins that are validated on base
            of interline ticketing aggrement.
    """
    tpa_extensions: Optional[ExchangeTravelPreferencesTpaExtensionsType] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    valid_interline_ticket: bool = field(
        default=False,
        metadata={
            "name": "ValidInterlineTicket",
            "type": "Attribute",
        }
    )


@dataclass
class ExchangeOriginDestinationInformationType(OriginDestinationInformationType):
    """
    Attributes
        flight:
        date_flexibility: The number of alternate days around the travel
            date to search.
        sister_destination_location: List of alternate destination
            cities to search
        sister_destination_mileage:
        sister_origin_location: List of alternate origin cities to
            search
        sister_origin_mileage:
        segment_type:
        alternate_time: Maximum time difference/deviation allowed.
        max_one_way_options: Maximum number of options to return.
        num_one_way_options: Number of options for requested date.
        cabin_pref: Defines preferred cabin to be used in a search for
            this leg level (if SegmentType is "O") or segment (if
            SegmentType is "X"). The cabin type specified in this
            element will override the cabin type specified at the
            request level for this leg/segment. If a cabin type is not
            specified for this element the cabin type at request level
            will be used as default for this leg or segment. If the
            cabin type is not specified at both the leg/segment level
            and request level a default cabin of "Economy" will be used?
        connection_time: Connection time between segments.
        total_travel_time: Total travel time settings
    """
    flight: List[ExchangeOriginDestinationFlightType] = field(
        default_factory=list,
        metadata={
            "name": "Flight",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )
    date_flexibility: List["ExchangeOriginDestinationInformationType.DateFlexibility"] = field(
        default_factory=list,
        metadata={
            "name": "DateFlexibility",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 2,
        }
    )
    sister_destination_location: List[RequestLocationType] = field(
        default_factory=list,
        metadata={
            "name": "SisterDestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    sister_destination_mileage: Optional["ExchangeOriginDestinationInformationType.SisterDestinationMileage"] = field(
        default=None,
        metadata={
            "name": "SisterDestinationMileage",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    sister_origin_location: List[RequestLocationType] = field(
        default_factory=list,
        metadata={
            "name": "SisterOriginLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    sister_origin_mileage: Optional["ExchangeOriginDestinationInformationType.SisterOriginMileage"] = field(
        default=None,
        metadata={
            "name": "SisterOriginMileage",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    segment_type: Optional["ExchangeOriginDestinationInformationType.SegmentType"] = field(
        default=None,
        metadata={
            "name": "SegmentType",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    alternate_time: Optional["ExchangeOriginDestinationInformationType.AlternateTime"] = field(
        default=None,
        metadata={
            "name": "AlternateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    max_one_way_options: Optional["ExchangeOriginDestinationInformationType.MaxOneWayOptions"] = field(
        default=None,
        metadata={
            "name": "MaxOneWayOptions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    num_one_way_options: Optional["ExchangeOriginDestinationInformationType.NumOneWayOptions"] = field(
        default=None,
        metadata={
            "name": "NumOneWayOptions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    cabin_pref: Optional[CabinPrefType] = field(
        default=None,
        metadata={
            "name": "CabinPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    connection_time: Optional["ExchangeOriginDestinationInformationType.ConnectionTime"] = field(
        default=None,
        metadata={
            "name": "ConnectionTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    total_travel_time: Optional["ExchangeOriginDestinationInformationType.TotalTravelTime"] = field(
        default=None,
        metadata={
            "name": "TotalTravelTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )

    @dataclass
    class DateFlexibility:
        """
        Attributes
            nbr_of_days: Number of alternate dates before and after
                requested travel date.
            plus: Number of alternate dates before requested travel
                date.
            minus: Number of alternate dates after requested travel
                date.
            validate: Flag telling if dates within the specified range
                should be processed in the validate path.
        """
        nbr_of_days: Optional[int] = field(
            default=None,
            metadata={
                "name": "NbrOfDays",
                "type": "Attribute",
            }
        )
        plus: Optional[int] = field(
            default=None,
            metadata={
                "name": "Plus",
                "type": "Attribute",
            }
        )
        minus: Optional[int] = field(
            default=None,
            metadata={
                "name": "Minus",
                "type": "Attribute",
            }
        )
        validate: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Validate",
                "type": "Attribute",
            }
        )

    @dataclass
    class SisterDestinationMileage:
        number: Optional[int] = field(
            default=None,
            metadata={
                "name": "Number",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SisterOriginMileage:
        number: Optional[int] = field(
            default=None,
            metadata={
                "name": "Number",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SegmentType:
        """
        Attributes
            code: "Code" can be "ARUNK", "O" for normal, or "X" for
                connection.
        """
        code: Optional[SegmentTypeCode] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )

    @dataclass
    class AlternateTime:
        """
        Attributes
            plus_minus: Maximum time difference between actual and
                desired time.
            plus: Maximum number of hours after desired time.
            minus: Maximum number of hours before desired time.
        """
        plus_minus: Optional[int] = field(
            default=None,
            metadata={
                "name": "PlusMinus",
                "type": "Attribute",
                "min_inclusive": 0,
                "max_inclusive": 9,
            }
        )
        plus: Optional[int] = field(
            default=None,
            metadata={
                "name": "Plus",
                "type": "Attribute",
                "min_inclusive": 0,
                "max_inclusive": 9,
            }
        )
        minus: Optional[int] = field(
            default=None,
            metadata={
                "name": "Minus",
                "type": "Attribute",
                "min_inclusive": 0,
                "max_inclusive": 72,
            }
        )

    @dataclass
    class MaxOneWayOptions:
        value: Optional[int] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class NumOneWayOptions:
        number: Optional[int] = field(
            default=None,
            metadata={
                "name": "Number",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ConnectionTime:
        """
        Attributes
            min:
            max:
            excluded_connection_begin: Excluded connection time begin in
                format HHMM
            excluded_connection_end: Excluded connection time end in
                format HHMM
            enable_excluded_connection: Enable excluded connection time
                (default: true)
        """
        min: Optional[int] = field(
            default=None,
            metadata={
                "name": "Min",
                "type": "Attribute",
            }
        )
        max: Optional[int] = field(
            default=None,
            metadata={
                "name": "Max",
                "type": "Attribute",
            }
        )
        excluded_connection_begin: Optional[str] = field(
            default=None,
            metadata={
                "name": "ExcludedConnectionBegin",
                "type": "Attribute",
                "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
            }
        )
        excluded_connection_end: Optional[str] = field(
            default=None,
            metadata={
                "name": "ExcludedConnectionEnd",
                "type": "Attribute",
                "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
            }
        )
        enable_excluded_connection: Optional[bool] = field(
            default=None,
            metadata={
                "name": "EnableExcludedConnection",
                "type": "Attribute",
            }
        )

    @dataclass
    class TotalTravelTime:
        min: Optional[int] = field(
            default=None,
            metadata={
                "name": "Min",
                "type": "Attribute",
            }
        )
        max: Optional[int] = field(
            default=None,
            metadata={
                "name": "Max",
                "type": "Attribute",
            }
        )


@dataclass
class ExchangePostype:
    class Meta:
        name = "ExchangePOSType"

    source: Optional[ExchangeSourceType] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )


@dataclass
class PosType:
    """
    Point of Sale (POS) is the details identifying the party or connection channel
    making the request.

    Attributes
        source: This holds details regarding the requestor. It may be
            repeated to also accommodate the delivery systems.
    """
    class Meta:
        name = "POS_Type"

    source: List[SourceType] = field(
        default_factory=list,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )


@dataclass
class TravelerInformationType:
    """
    Specifies passenger numbers and types.

    Attributes
        passenger_type_quantity: Specifies number of passengers using
            Passenger Type Codes.
        air_traveler: Information profiling the person traveling Gender
            - the gender of the customer, if needed BirthDate - Date of
            Birth Currency - the preferred currency in which monetary
            amounts should be returned.
    """
    passenger_type_quantity: List[PassengerTypeQuantityType] = field(
        default_factory=list,
        metadata={
            "name": "PassengerTypeQuantity",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 9,
        }
    )
    air_traveler: Optional[AirTravelerType] = field(
        default=None,
        metadata={
            "name": "AirTraveler",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )


@dataclass
class TravelerInfoSummaryType:
    """
    Specifies passenger numbers and types.

    Attributes
        seats_requested: The sum of all seats required by all passenger
            groups.
        air_traveler_avail: Specifies passenger numbers and types.
        price_request_information: Identify pricing source, if
            negotiated fares are requested and if it is a reprice
            request.
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        specific_ptc_indicator: If true, this request is for a specific
            PTC and only fares applicable to that PTC will be checked
            and returned. It is the same as XOFares flag in Intellisell
            request.
    """
    seats_requested: List[int] = field(
        default_factory=list,
        metadata={
            "name": "SeatsRequested",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 4,
        }
    )
    air_traveler_avail: List[TravelerInformationType] = field(
        default_factory=list,
        metadata={
            "name": "AirTravelerAvail",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 4,
        }
    )
    price_request_information: Optional[PriceRequestInformationType] = field(
        default=None,
        metadata={
            "name": "PriceRequestInformation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    tpa_extensions: Optional[TravelerInfoSummaryTpaExtensionsType] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    specific_ptc_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpecificPTC_Indicator",
            "type": "Attribute",
        }
    )


@dataclass
class ExchangeType:
    """
    Attributes
        fare:
        pos:
        origin_destination_information:
        arunk:
        travel_preferences:
        traveler_info_summary:
        tpa_extensions:
        original_tkt_issue_date_time: Original ticket issue date and
            time
        exchanged_tkt_issue_date_time: Exchanged ticket issue date and
            time
        previous_exchange_date_time: Previous exchange date and time
        number_of_tax_boxes: Number of tax boxes
        bypass_advance_purchase_option: Bypass Advance Purchase Option
    """
    fare: Optional[ExchangeFareType] = field(
        default=None,
        metadata={
            "name": "Fare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    pos: Optional[ExchangePostype] = field(
        default=None,
        metadata={
            "name": "POS",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    origin_destination_information: List[ExchangeOriginDestinationInformationType] = field(
        default_factory=list,
        metadata={
            "name": "OriginDestinationInformation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )
    arunk: List[ArunkType] = field(
        default_factory=list,
        metadata={
            "name": "Arunk",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    travel_preferences: Optional[ExchangeAirSearchPrefsType] = field(
        default=None,
        metadata={
            "name": "TravelPreferences",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    traveler_info_summary: Optional[TravelerInfoSummaryType] = field(
        default=None,
        metadata={
            "name": "TravelerInfoSummary",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    tpa_extensions: Optional[ExchangeTpaExtensionsType] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    original_tkt_issue_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalTktIssueDateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}(T[0-9]{2}:[0-9]{2}:[0-9]{2})?",
        }
    )
    exchanged_tkt_issue_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExchangedTktIssueDateTime",
            "type": "Attribute",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}(T[0-9]{2}:[0-9]{2}:[0-9]{2})?",
        }
    )
    previous_exchange_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreviousExchangeDateTime",
            "type": "Attribute",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}(T[0-9]{2}:[0-9]{2}:[0-9]{2})?",
        }
    )
    number_of_tax_boxes: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfTaxBoxes",
            "type": "Attribute",
        }
    )
    bypass_advance_purchase_option: Optional[str] = field(
        default=None,
        metadata={
            "name": "BypassAdvancePurchaseOption",
            "type": "Attribute",
            "length": 1,
        }
    )


@dataclass
class OtaAirLowFareSearchRq:
    """The Low Fare Search Request message requests priced itinerary options for
    flights between specific city pairs on specific dates for specific numbers and
    types of passengers.

    Optional request information can include: - Time / Time Window - Connecting cities. - Client Preferences (airlines, cabin, flight types etc.) The Low Fare Search request contains similar information to a Low Fare Search entry on an airline CRS or GDS.

    Attributes
        pos: Point of sale object.
        origin_destination_information: Origin and Destination location,
            and time information for the Air Low Fare Search request.
        leg: Single leg specification
        travel_preferences: Air Low Fare Search Request preference
            information.
        traveler_info_summary: Specifies the number of passengers and
            types for Air Low Fare Search.
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        echo_token: A sequence number for additional message
            identification, assigned by the requesting host system. When
            a request message includes an echo token the corresponding
            response message MUST include an echo token with an
            identical value.
        time_stamp: Indicates the creation date and time of the message
            in UTC using the following format specified by ISO 8601;
            YYYY-MM-DDThh:mm:ssZ with time values using the 24 hour
            clock (e.g. 20 November 2003, 1:59:38 pm UTC becomes
            2003-11-20T13:59:38Z).
        target: Used to indicate whether the request is for the Test or
            Production system.
        version: For all OTA versioned messages, the version of the
            message is indicated by a decimal value.
        transaction_identifier: A unique identifier to relate all
            messages within a transaction (e.g. this would be sent in
            all request and response messages that are part of an on-
            going transaction).
        sequence_nmbr: Used to identify the sequence number of the
            transaction as assigned by the sending system; allows for an
            application to process messages in a certain order or to
            request a resynchronization of messages in the event that a
            system has been off-line and needs to retrieve messages that
            were missed.
        transaction_status_code: This indicates where this message falls
            within a sequence of messages.
        primary_lang_id: Identifes the primary language preference for
            the form of travel represented in a collection. The human
            language is identified by ISO 639 codes.
        alt_lang_id:
        max_responses: A positive integer value that indicates the
            maximum number of responses desired in the return.
        direct_flights_only: Request direct flights between given
            locations. This defaults to false.
        available_flights_only: Include only flights with available
            booking codes (when True or when attribute not present).
        response_type:
        response_version:
        separate_messages: Whether all messages should be printed in
            separate MTP element or not. Works only with PSS response
            serializers.
        truncate_messages: Whether each MTP content should be truncated
            to specified length or not. Works only with PSS response
            serializers.
    """
    class Meta:
        name = "OTA_AirLowFareSearchRQ"
        namespace = "http://www.opentravel.org/OTA/2003/05"

    pos: Optional[PosType] = field(
        default=None,
        metadata={
            "name": "POS",
            "type": "Element",
            "required": True,
        }
    )
    origin_destination_information: List["OtaAirLowFareSearchRq.OriginDestinationInformation"] = field(
        default_factory=list,
        metadata={
            "name": "OriginDestinationInformation",
            "type": "Element",
            "max_occurs": 10,
        }
    )
    leg: List["OtaAirLowFareSearchRq.Leg"] = field(
        default_factory=list,
        metadata={
            "name": "Leg",
            "type": "Element",
        }
    )
    travel_preferences: Optional[AirSearchPrefsType] = field(
        default=None,
        metadata={
            "name": "TravelPreferences",
            "type": "Element",
        }
    )
    traveler_info_summary: Optional[TravelerInfoSummaryType] = field(
        default=None,
        metadata={
            "name": "TravelerInfoSummary",
            "type": "Element",
            "required": True,
        }
    )
    tpa_extensions: Optional["OtaAirLowFareSearchRq.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
        }
    )
    echo_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "EchoToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    time_stamp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeStamp",
            "type": "Attribute",
        }
    )
    target: OtaAirLowFareSearchRqTarget = field(
        default=OtaAirLowFareSearchRqTarget.PRODUCTION,
        metadata={
            "name": "Target",
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
    transaction_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    sequence_nmbr: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "name": "SequenceNmbr",
            "type": "Attribute",
        }
    )
    transaction_status_code: Optional[OtaAirLowFareSearchRqTransactionStatusCode] = field(
        default=None,
        metadata={
            "name": "TransactionStatusCode",
            "type": "Attribute",
        }
    )
    primary_lang_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrimaryLangID",
            "type": "Attribute",
        }
    )
    alt_lang_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltLangID",
            "type": "Attribute",
        }
    )
    max_responses: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxResponses",
            "type": "Attribute",
        }
    )
    direct_flights_only: bool = field(
        default=False,
        metadata={
            "name": "DirectFlightsOnly",
            "type": "Attribute",
        }
    )
    available_flights_only: bool = field(
        default=True,
        metadata={
            "name": "AvailableFlightsOnly",
            "type": "Attribute",
        }
    )
    response_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponseType",
            "type": "Attribute",
        }
    )
    response_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponseVersion",
            "type": "Attribute",
        }
    )
    separate_messages: bool = field(
        default=False,
        metadata={
            "name": "SeparateMessages",
            "type": "Attribute",
        }
    )
    truncate_messages: bool = field(
        default=True,
        metadata={
            "name": "TruncateMessages",
            "type": "Attribute",
        }
    )

    @dataclass
    class TpaExtensions:
        """
        Attributes
            intelli_sell_transaction:
            diversity_control:
            messaging_details:
            alternate_airport_cities: For each specified location
                provide an alternate location.
            alternate_airport_mileage: Specify maximum allowed distance
                from specified airport.
            award_shopping:
            billing:
            exchange_settings:
            exchange:
            split_taxes:
            alternate_dates_processing:
            itinerary_cache:
            multi_ticket:
            partitions:
            reservation_data:
            alternate_pcc:
        """
        intelli_sell_transaction: Optional[TransactionType] = field(
            default=None,
            metadata={
                "name": "IntelliSellTransaction",
                "type": "Element",
            }
        )
        diversity_control: Optional[DiversityControlType] = field(
            default=None,
            metadata={
                "name": "DiversityControl",
                "type": "Element",
            }
        )
        messaging_details: Optional["OtaAirLowFareSearchRq.TpaExtensions.MessagingDetails"] = field(
            default=None,
            metadata={
                "name": "MessagingDetails",
                "type": "Element",
            }
        )
        alternate_airport_cities: List["OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportCities"] = field(
            default_factory=list,
            metadata={
                "name": "AlternateAirportCities",
                "type": "Element",
            }
        )
        alternate_airport_mileage: Optional["OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportMileage"] = field(
            default=None,
            metadata={
                "name": "AlternateAirportMileage",
                "type": "Element",
            }
        )
        award_shopping: Optional[AwardShoppingType] = field(
            default=None,
            metadata={
                "name": "AwardShopping",
                "type": "Element",
            }
        )
        billing: Optional[BillingInformationType] = field(
            default=None,
            metadata={
                "name": "Billing",
                "type": "Element",
            }
        )
        exchange_settings: Optional[ExchangeSettingsType] = field(
            default=None,
            metadata={
                "name": "ExchangeSettings",
                "type": "Element",
            }
        )
        exchange: List[ExchangeType] = field(
            default_factory=list,
            metadata={
                "name": "Exchange",
                "type": "Element",
            }
        )
        split_taxes: Optional["OtaAirLowFareSearchRq.TpaExtensions.SplitTaxes"] = field(
            default=None,
            metadata={
                "name": "SplitTaxes",
                "type": "Element",
            }
        )
        alternate_dates_processing: Optional["OtaAirLowFareSearchRq.TpaExtensions.AlternateDatesProcessing"] = field(
            default=None,
            metadata={
                "name": "AlternateDatesProcessing",
                "type": "Element",
            }
        )
        itinerary_cache: Optional["OtaAirLowFareSearchRq.TpaExtensions.ItineraryCache"] = field(
            default=None,
            metadata={
                "name": "ItineraryCache",
                "type": "Element",
            }
        )
        multi_ticket: Optional["OtaAirLowFareSearchRq.TpaExtensions.MultiTicket"] = field(
            default=None,
            metadata={
                "name": "MultiTicket",
                "type": "Element",
            }
        )
        partitions: Optional["OtaAirLowFareSearchRq.TpaExtensions.Partitions"] = field(
            default=None,
            metadata={
                "name": "Partitions",
                "type": "Element",
            }
        )
        reservation_data: Optional["OtaAirLowFareSearchRq.TpaExtensions.ReservationData"] = field(
            default=None,
            metadata={
                "name": "ReservationData",
                "type": "Element",
            }
        )
        alternate_pcc: List["OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc"] = field(
            default_factory=list,
            metadata={
                "name": "AlternatePCC",
                "type": "Element",
            }
        )

        @dataclass
        class MessagingDetails:
            mdrsubset: Optional["OtaAirLowFareSearchRq.TpaExtensions.MessagingDetails.Mdrsubset"] = field(
                default=None,
                metadata={
                    "name": "MDRSubset",
                    "type": "Element",
                }
            )

            @dataclass
            class Mdrsubset:
                code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                    }
                )

        @dataclass
        class SplitTaxes:
            by_leg: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "ByLeg",
                    "type": "Attribute",
                }
            )
            by_fare_component: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "ByFareComponent",
                    "type": "Attribute",
                }
            )

        @dataclass
        class AlternateDatesProcessing:
            calendar_mode: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "CalendarMode",
                    "type": "Attribute",
                }
            )
            num_options_per_alternate_date: int = field(
                default=9,
                metadata={
                    "name": "NumOptionsPerAlternateDate",
                    "type": "Attribute",
                }
            )

        @dataclass
        class ItineraryCache:
            public_time_to_live: Optional[int] = field(
                default=None,
                metadata={
                    "name": "PublicTimeToLive",
                    "type": "Attribute",
                }
            )
            remove_previous_on_update: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "RemovePreviousOnUpdate",
                    "type": "Attribute",
                }
            )

        @dataclass
        class MultiTicket:
            """
            Attributes
                display_policy: Display Option Policy, takes values: -
                    SOW - Show OneWays separately - GOW2RT - Group
                    OneWays and match to RoundTrip - SCHS - Group
                    OneWays, match to RoundTrip and show cheaper
                    solution
            """
            display_policy: Optional[MultiTicketDisplayPolicy] = field(
                default=None,
                metadata={
                    "name": "DisplayPolicy",
                    "type": "Attribute",
                }
            )

        @dataclass
        class Partitions:
            partition: List[CachePartitionType] = field(
                default_factory=list,
                metadata={
                    "name": "Partition",
                    "type": "Element",
                }
            )
            group: List[CachePartitionGroupType] = field(
                default_factory=list,
                metadata={
                    "name": "Group",
                    "type": "Element",
                }
            )

        @dataclass
        class ReservationData:
            """
            Attributes
                dknumber: DK number
            """
            dknumber: Optional[str] = field(
                default=None,
                metadata={
                    "name": "DKNumber",
                    "type": "Attribute",
                }
            )

        @dataclass
        class AlternatePcc:
            """
            Attributes
                travel_preferences:
                pseudo_city_code: An identification code assigned to an
                    office/agency by a reservation system.
            """
            travel_preferences: Optional["OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc.TravelPreferences"] = field(
                default=None,
                metadata={
                    "name": "TravelPreferences",
                    "type": "Element",
                }
            )
            pseudo_city_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PseudoCityCode",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 16,
                }
            )

            @dataclass
            class TravelPreferences:
                vendor_pref: List["OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc.TravelPreferences.VendorPref"] = field(
                    default_factory=list,
                    metadata={
                        "name": "VendorPref",
                        "type": "Element",
                    }
                )
                tpa_extensions: Optional["OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc.TravelPreferences.TpaExtensions"] = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    }
                )

                @dataclass
                class VendorPref:
                    """
                    Attributes
                        code: Identifies a company by the company code.
                        prefer_level:
                    """
                    code: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Code",
                            "type": "Attribute",
                            "required": True,
                            "min_length": 1,
                            "max_length": 8,
                        }
                    )
                    prefer_level: PreferLevelType = field(
                        default=PreferLevelType.PREFERRED,
                        metadata={
                            "name": "PreferLevel",
                            "type": "Attribute",
                        }
                    )

                @dataclass
                class TpaExtensions:
                    """
                    Attributes
                        include_alliance_pref: Consider only these
                            alliances.
                        exclude_alliance_pref: Do not consider these
                            alliances.
                    """
                    include_alliance_pref: List[AllianceType] = field(
                        default_factory=list,
                        metadata={
                            "name": "IncludeAlliancePref",
                            "type": "Element",
                        }
                    )
                    exclude_alliance_pref: List[AllianceType] = field(
                        default_factory=list,
                        metadata={
                            "name": "ExcludeAlliancePref",
                            "type": "Element",
                        }
                    )

        @dataclass
        class AlternateAirportCities:
            """
            Attributes
                specified_location: A desired location (airport city).
                alternate_location: An alternate location (airport
                    city).
            """
            specified_location: Optional["OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportCities.SpecifiedLocation"] = field(
                default=None,
                metadata={
                    "name": "SpecifiedLocation",
                    "type": "Element",
                    "required": True,
                }
            )
            alternate_location: List["OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportCities.AlternateLocation"] = field(
                default_factory=list,
                metadata={
                    "name": "AlternateLocation",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 5,
                }
            )

            @dataclass
            class SpecifiedLocation:
                location_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "LocationCode",
                        "type": "Attribute",
                        "pattern": r"[A-Z]*",
                    }
                )

            @dataclass
            class AlternateLocation:
                location_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "LocationCode",
                        "type": "Attribute",
                        "pattern": r"[A-Z]*",
                    }
                )

        @dataclass
        class AlternateAirportMileage:
            """
            Attributes
                number: Maximum allowed number of miles from desired
                    airport.
            """
            number: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Number",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class OriginDestinationInformation(OriginDestinationInformationType):
        """
        Attributes
            tpa_extensions: Additional elements and attributes to be
                included if required, per Trading Partner Agreement
                (TPA).
            rph: A placeholder for OriginDestinationInformation to be
                referenced wihin the OTA_AirLowFareSearchRS message.
                PricedItineraryType carries the reference to this RPH.
            fixed: OriginDestination node with flight and fare
                information fixed. Used in context shopping
            full_diversity: Request for full diversity of flights for
                the particular OriginDestination node. Used in Exchange
                Context Shopping
        """
        tpa_extensions: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions"] = field(
            default=None,
            metadata={
                "name": "TPA_Extensions",
                "type": "Element",
            }
        )
        rph: Optional[str] = field(
            default=None,
            metadata={
                "name": "RPH",
                "type": "Attribute",
                "pattern": r"[0-9]{1,8}",
            }
        )
        fixed: bool = field(
            default=False,
            metadata={
                "name": "Fixed",
                "type": "Attribute",
            }
        )
        full_diversity: bool = field(
            default=False,
            metadata={
                "name": "FullDiversity",
                "type": "Attribute",
            }
        )

        @dataclass
        class TpaExtensions:
            """
            Attributes
                flight:
                routing:
                date_flexibility: The number of alternate days around
                    the travel date to search.
                sister_destination_location: List of alternate
                    destination cities to search
                sister_destination_mileage:
                sister_origin_location: List of alternate origin cities
                    to search
                sister_origin_mileage:
                segment_type:
                alternate_time: Maximum time difference/deviation
                    allowed.
                max_one_way_options: Maximum number of options to
                    return.
                num_one_way_options: Number of options for requested
                    date.
                cabin_pref: Defines preferred cabin to be used in a
                    search for this leg level (if SegmentType is "O") or
                    segment (if SegmentType is "X"). The cabin type
                    specified in this element will override the cabin
                    type specified at the request level for this
                    leg/segment. If a cabin type is not specified for
                    this element the cabin type at request level will be
                    used as default for this leg or segment. If the
                    cabin type is not specified at both the leg/segment
                    level and request level a default cabin of "Economy"
                    will be used?
                connection_time: Connection time between segments.
                total_travel_time: Total travel time settings
                include_vendor_pref:
                include_alliance_pref: Consider only these alliances.
                departure_days:
            """
            flight: List[OriginDestinationFlightType] = field(
                default_factory=list,
                metadata={
                    "name": "Flight",
                    "type": "Element",
                }
            )
            routing: List[RoutingDefinitionType] = field(
                default_factory=list,
                metadata={
                    "name": "Routing",
                    "type": "Element",
                }
            )
            date_flexibility: List["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.DateFlexibility"] = field(
                default_factory=list,
                metadata={
                    "name": "DateFlexibility",
                    "type": "Element",
                    "max_occurs": 2,
                }
            )
            sister_destination_location: List[RequestLocationType] = field(
                default_factory=list,
                metadata={
                    "name": "SisterDestinationLocation",
                    "type": "Element",
                }
            )
            sister_destination_mileage: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.SisterDestinationMileage"] = field(
                default=None,
                metadata={
                    "name": "SisterDestinationMileage",
                    "type": "Element",
                }
            )
            sister_origin_location: List[RequestLocationType] = field(
                default_factory=list,
                metadata={
                    "name": "SisterOriginLocation",
                    "type": "Element",
                }
            )
            sister_origin_mileage: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.SisterOriginMileage"] = field(
                default=None,
                metadata={
                    "name": "SisterOriginMileage",
                    "type": "Element",
                }
            )
            segment_type: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.SegmentType"] = field(
                default=None,
                metadata={
                    "name": "SegmentType",
                    "type": "Element",
                }
            )
            alternate_time: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.AlternateTime"] = field(
                default=None,
                metadata={
                    "name": "AlternateTime",
                    "type": "Element",
                }
            )
            max_one_way_options: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.MaxOneWayOptions"] = field(
                default=None,
                metadata={
                    "name": "MaxOneWayOptions",
                    "type": "Element",
                }
            )
            num_one_way_options: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.NumOneWayOptions"] = field(
                default=None,
                metadata={
                    "name": "NumOneWayOptions",
                    "type": "Element",
                }
            )
            cabin_pref: Optional[CabinPrefType] = field(
                default=None,
                metadata={
                    "name": "CabinPref",
                    "type": "Element",
                }
            )
            connection_time: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.ConnectionTime"] = field(
                default=None,
                metadata={
                    "name": "ConnectionTime",
                    "type": "Element",
                }
            )
            total_travel_time: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.TotalTravelTime"] = field(
                default=None,
                metadata={
                    "name": "TotalTravelTime",
                    "type": "Element",
                }
            )
            include_vendor_pref: List[IncludeVendorPrefType] = field(
                default_factory=list,
                metadata={
                    "name": "IncludeVendorPref",
                    "type": "Element",
                }
            )
            include_alliance_pref: List[AllianceType] = field(
                default_factory=list,
                metadata={
                    "name": "IncludeAlliancePref",
                    "type": "Element",
                }
            )
            departure_days: Optional[DepartureDaysType] = field(
                default=None,
                metadata={
                    "name": "DepartureDays",
                    "type": "Element",
                }
            )

            @dataclass
            class DateFlexibility:
                """
                Attributes
                    nbr_of_days: Number of alternate dates before and
                        after requested travel date.
                    plus: Number of alternate dates before requested
                        travel date.
                    minus: Number of alternate dates after requested
                        travel date.
                    validate: Flag telling if dates within the specified
                        range should be processed in the validate path.
                """
                nbr_of_days: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "NbrOfDays",
                        "type": "Attribute",
                    }
                )
                plus: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Plus",
                        "type": "Attribute",
                    }
                )
                minus: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Minus",
                        "type": "Attribute",
                    }
                )
                validate: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Validate",
                        "type": "Attribute",
                    }
                )

            @dataclass
            class SisterDestinationMileage:
                number: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class SisterOriginMileage:
                number: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class SegmentType:
                """
                Attributes
                    code: "Code" can be "ARUNK", "O" for normal, or "X"
                        for connection.
                """
                code: Optional[SegmentTypeCode] = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                    }
                )

            @dataclass
            class AlternateTime:
                """
                Attributes
                    plus_minus: Maximum time difference between actual
                        and desired time.
                    plus: Maximum number of hours after desired time.
                    minus: Maximum number of hours before desired time.
                """
                plus_minus: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "PlusMinus",
                        "type": "Attribute",
                        "min_inclusive": 0,
                        "max_inclusive": 9,
                    }
                )
                plus: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Plus",
                        "type": "Attribute",
                        "min_inclusive": 0,
                        "max_inclusive": 9,
                    }
                )
                minus: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Minus",
                        "type": "Attribute",
                        "min_inclusive": 0,
                        "max_inclusive": 72,
                    }
                )

            @dataclass
            class MaxOneWayOptions:
                value: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Value",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class NumOneWayOptions:
                number: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class ConnectionTime:
                """
                Attributes
                    min:
                    max:
                    excluded_connection_begin: Excluded connection time
                        begin in format HHMM
                    excluded_connection_end: Excluded connection time
                        end in format HHMM
                    enable_excluded_connection: Enable excluded
                        connection time (default: true)
                """
                min: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Min",
                        "type": "Attribute",
                    }
                )
                max: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Max",
                        "type": "Attribute",
                    }
                )
                excluded_connection_begin: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ExcludedConnectionBegin",
                        "type": "Attribute",
                        "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
                    }
                )
                excluded_connection_end: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ExcludedConnectionEnd",
                        "type": "Attribute",
                        "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
                    }
                )
                enable_excluded_connection: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "EnableExcludedConnection",
                        "type": "Attribute",
                    }
                )

            @dataclass
            class TotalTravelTime:
                min: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Min",
                        "type": "Attribute",
                    }
                )
                max: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Max",
                        "type": "Attribute",
                    }
                )

    @dataclass
    class Leg:
        """
        Attributes
            departure_date_time:
            arrival_date_time:
            origins:
            destinations:
            connection_locations: Travel Connection Location - for
                example, air uses the IATA 3 letter code.
            carriers: Carrier preferrence information
            cabin: Defines preferred cabin to be used in a search for
                this leg level.
            rph: A placeholder for OriginDestinationInformation to be
                referenced wihin the OTA_AirLowFareSearchRS message.
                PricedItineraryType carries the reference to this RPH.
            max_options: Maximum number of options to return.
        """
        departure_date_time: Optional["OtaAirLowFareSearchRq.Leg.DepartureDateTime"] = field(
            default=None,
            metadata={
                "name": "DepartureDateTime",
                "type": "Element",
            }
        )
        arrival_date_time: Optional[GlobalDateTimeType] = field(
            default=None,
            metadata={
                "name": "ArrivalDateTime",
                "type": "Element",
            }
        )
        origins: Optional["OtaAirLowFareSearchRq.Leg.Origins"] = field(
            default=None,
            metadata={
                "name": "Origins",
                "type": "Element",
                "required": True,
            }
        )
        destinations: Optional["OtaAirLowFareSearchRq.Leg.Destinations"] = field(
            default=None,
            metadata={
                "name": "Destinations",
                "type": "Element",
                "required": True,
            }
        )
        connection_locations: Optional[ConnectionType] = field(
            default=None,
            metadata={
                "name": "ConnectionLocations",
                "type": "Element",
            }
        )
        carriers: Optional["OtaAirLowFareSearchRq.Leg.Carriers"] = field(
            default=None,
            metadata={
                "name": "Carriers",
                "type": "Element",
            }
        )
        cabin: Optional["OtaAirLowFareSearchRq.Leg.Cabin"] = field(
            default=None,
            metadata={
                "name": "Cabin",
                "type": "Element",
            }
        )
        rph: Optional[str] = field(
            default=None,
            metadata={
                "name": "RPH",
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{1,8}",
            }
        )
        max_options: Optional[int] = field(
            default=None,
            metadata={
                "name": "MaxOptions",
                "type": "Attribute",
            }
        )

        @dataclass
        class Origins:
            origin: List["OtaAirLowFareSearchRq.Leg.Origins.Origin"] = field(
                default_factory=list,
                metadata={
                    "name": "Origin",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class Origin:
                """
                Attributes
                    airport_code: Required unless AirportsGroup is
                        specified. Cannot appear with AirportsGroup.
                    airports_group: Name of the airports group
                """
                airport_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "AirportCode",
                        "type": "Attribute",
                        "min_length": 1,
                        "max_length": 8,
                    }
                )
                airports_group: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "AirportsGroup",
                        "type": "Attribute",
                    }
                )

                @dataclass
                class Carriers:
                    """
                    Attributes
                        include_vendor_pref:
                        exclude_vendor_pref: Do not consider these
                            carriers for this leg.
                    """
                    include_vendor_pref: List[IncludeVendorPrefType] = field(
                        default_factory=list,
                        metadata={
                            "name": "IncludeVendorPref",
                            "type": "Element",
                        }
                    )
                    exclude_vendor_pref: List["OtaAirLowFareSearchRq.Leg.Origins.Origin.Carriers.ExcludeVendorPref"] = field(
                        default_factory=list,
                        metadata={
                            "name": "ExcludeVendorPref",
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class ExcludeVendorPref:
                        """
                        Attributes
                            code: Identifies a company by the company
                                code.
                        """
                        code: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "Code",
                                "type": "Attribute",
                                "required": True,
                                "min_length": 1,
                                "max_length": 8,
                            }
                        )

        @dataclass
        class Destinations:
            destination: List["OtaAirLowFareSearchRq.Leg.Destinations.Destination"] = field(
                default_factory=list,
                metadata={
                    "name": "Destination",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class Destination:
                """
                Attributes
                    airport_code: Required unless AirportsGroup is
                        specified. Cannot appear with AirportsGroup.
                    airports_group: Name of the airports group
                """
                airport_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "AirportCode",
                        "type": "Attribute",
                        "min_length": 1,
                        "max_length": 8,
                    }
                )
                airports_group: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "AirportsGroup",
                        "type": "Attribute",
                    }
                )

                @dataclass
                class Carriers:
                    """
                    Attributes
                        include_vendor_pref:
                        exclude_vendor_pref: Do not consider these
                            carriers for this leg.
                    """
                    include_vendor_pref: List[IncludeVendorPrefType] = field(
                        default_factory=list,
                        metadata={
                            "name": "IncludeVendorPref",
                            "type": "Element",
                        }
                    )
                    exclude_vendor_pref: List["OtaAirLowFareSearchRq.Leg.Destinations.Destination.Carriers.ExcludeVendorPref"] = field(
                        default_factory=list,
                        metadata={
                            "name": "ExcludeVendorPref",
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class ExcludeVendorPref:
                        """
                        Attributes
                            code: Identifies a company by the company
                                code.
                        """
                        code: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "Code",
                                "type": "Attribute",
                                "required": True,
                                "min_length": 1,
                                "max_length": 8,
                            }
                        )

        @dataclass
        class Carriers:
            """
            Attributes
                include_vendor_pref:
                exclude_vendor_pref: Do not consider these carriers for
                    this leg.
            """
            include_vendor_pref: List[IncludeVendorPrefType] = field(
                default_factory=list,
                metadata={
                    "name": "IncludeVendorPref",
                    "type": "Element",
                }
            )
            exclude_vendor_pref: List["OtaAirLowFareSearchRq.Leg.Carriers.ExcludeVendorPref"] = field(
                default_factory=list,
                metadata={
                    "name": "ExcludeVendorPref",
                    "type": "Element",
                }
            )

            @dataclass
            class ExcludeVendorPref:
                """
                Attributes
                    code: Identifies a company by the company code.
                """
                code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 8,
                    }
                )

        @dataclass
        class Cabin:
            """
            Attributes
                preference_level:
                type: Specifies cabin type.
            """
            preference_level: PreferLevelType = field(
                default=PreferLevelType.PREFERRED,
                metadata={
                    "name": "PreferenceLevel",
                    "type": "Attribute",
                }
            )
            type: Optional[CabinType] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )

        @dataclass
        class DepartureDateTime(GlobalDateTimeType):
            """
            Attributes
                week_days: Specify which days of week  to consider for
                    departure. Value format: First letter of the name of
                    the day or '_', eg. 'SMT___S' means we are
                    interested in departing at Saturday, Sunday, Monday
                    or Tuesday. Even if there are schedules for
                    Wednesday, Thursday or Friday, they won't be
                    returned in ISell response.
            """
            week_days: Optional[str] = field(
                default=None,
                metadata={
                    "name": "WeekDays",
                    "type": "Attribute",
                    "length": 7,
                }
            )
