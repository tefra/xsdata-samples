from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union
from sabre.models.request.bargain_finder_max_common_types_v1_9_7 import (
    AdvResTicketingType,
    AirTripType,
    CompanyNameType,
    DepartureOrArrival,
    EquipmentType,
    OutboundOrInbound,
    PassengerTypeQuantityType,
    StayRestrictionsType,
    VoluntaryChangesType,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class AirlineType:
    """
    :ivar operating: Operating airline code
    :ivar marketing: Marketing airline code
    """
    operating: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Operating",
            type="Attribute",
            required=True,
            pattern=r"[0-9A-Z]{2,3}"
        )
    )
    marketing: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Marketing",
            type="Attribute",
            required=True,
            pattern=r"[0-9A-Z]{2,3}"
        )
    )


@dataclass
class AllianceType:
    """
    :ivar code: Identifies an alliance by the alliance code.
    """
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            length=2
        )
    )


class AltCitiesCombinationsLocationsType(Enum):
    """
    :cvar ALL:
    :cvar MAIN:
    """
    ALL = "All"
    MAIN = "Main"


@dataclass
class ApplyResidentDiscountType:
    """Apply resident discount in CLFE.

    :ivar ind:
    """
    ind: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Ind",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AwardShoppingType:
    """
    :ivar enable: Enable award shopping.
    :ivar use_ras: Use Redemption Availability Service
    """
    enable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Enable",
            type="Attribute"
        )
    )
    use_ras: bool = field(
        default=False,
        metadata=dict(
            name="UseRAS",
            type="Attribute"
        )
    )


@dataclass
class BillingInformationType:
    """
    :ivar user_station:
    :ivar user_branch:
    :ivar partition_id:
    :ivar user_set_address:
    :ivar aaacity:
    :ivar agent_sine_in:
    :ivar service_name:
    :ivar action_code:
    """
    user_station: int = field(
        default=0,
        metadata=dict(
            name="UserStation",
            type="Attribute"
        )
    )
    user_branch: int = field(
        default=0,
        metadata=dict(
            name="UserBranch",
            type="Attribute"
        )
    )
    partition_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PartitionID",
            type="Attribute",
            pattern=r"[0-9A-Z]{2,4}"
        )
    )
    user_set_address: Optional[str] = field(
        default=None,
        metadata=dict(
            name="UserSetAddress",
            type="Attribute",
            pattern=r"[0-9A-F]{6}"
        )
    )
    aaacity: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AAACity",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    agent_sine_in: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentSineIn",
            type="Attribute",
            max_length=3.0
        )
    )
    service_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ServiceName",
            type="Attribute",
            pattern=r"[0-9a-zA-Z,]{1,8}"
        )
    )
    action_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ActionCode",
            type="Attribute",
            min_length=1.0,
            max_length=5.0
        )
    )


@dataclass
class BookingChannelType:
    """Specifies the booking channel types and whether it is the primary means of
    connectivity of the source.

    :ivar type: The type of booking channel (e.g. Global Distribution System (GDS), Alternative Distribution System (ADS), Sales and Catering System (SCS), Property Management System (PMS), Central Reservation System (CRS), Tour Operator System (TOS), Internet and ALL). Refer to OTA Code List Booking Channel Type (BCT).
    :ivar primary: Indicates whether the enumerated booking channel is the primary means of connectivity used by the source.
    """
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )
    primary: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Primary",
            type="Attribute"
        )
    )


@dataclass
class BrandType:
    """
    :ivar code:
    """
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )


class CabinType(Enum):
    """A cabin is either Premium First (P), First (F), Premium Business (J),
    Business (C), Premium Economy (S) or Economy (Y)

    :cvar BUSINESS:
    :cvar C:
    :cvar ECONOMY:
    :cvar F:
    :cvar FIRST:
    :cvar J:
    :cvar P:
    :cvar PREMIUM_BUSINESS:
    :cvar PREMIUM_ECONOMY:
    :cvar PREMIUM_FIRST:
    :cvar S:
    :cvar Y:
    """
    BUSINESS = "Business"
    C = "C"
    ECONOMY = "Economy"
    F = "F"
    FIRST = "First"
    J = "J"
    P = "P"
    PREMIUM_BUSINESS = "PremiumBusiness"
    PREMIUM_ECONOMY = "PremiumEconomy"
    PREMIUM_FIRST = "PremiumFirst"
    S = "S"
    Y = "Y"


@dataclass
class CachePartitionType:
    """
    :ivar name:
    """
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            required=True,
            pattern=r"[A-Z0-9_]{1,}"
        )
    )


class CarrierType(Enum):
    """Used to specify if carrier type is  marketing or operating.

    :cvar MARKETING:
    :cvar OPERATING:
    """
    MARKETING = "Marketing"
    OPERATING = "Operating"


@dataclass
class CountryNameType:
    """The name or code of a country (e.g. as used in an address or to specify
    citizenship of a traveller).

    :ivar value:
    :ivar code: ISO 3166 code for a country.
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=0.0,
            max_length=64.0
        )
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            pattern=r"[a-zA-Z]{2}"
        )
    )


@dataclass
class CustLoyaltyType:
    """Program rewarding frequent use by accumulating credits for services provided
    by vendors.

    :ivar share_synch_ind:
    :ivar share_market_ind:
    :ivar program_id: Identifier to indicate the company owner of the loyalty program.
    :ivar membership_id: Unique identifier of the member in the program (membership number, account number, etc.).
    :ivar travel_sector: Identifies the travel sector. Refer to OTA Code List Travel Sector (TVS).
    :ivar loyal_level: Indicates special privileges in program assigned to individual.
    :ivar single_vendor_ind: Indicates if program is affiliated with a group of related offers accumulating credits.
    :ivar signup_date: Indicates when the member signed up for the loyalty program.
    :ivar effective_date: Indicates the starting date.
    :ivar expire_date: Indicates the ending date.
    :ivar rph: Reference place holder, to reference it back in the response.
    """
    share_synch_ind: Optional["CustLoyaltyType.ShareSynchInd"] = field(
        default=None,
        metadata=dict(
            name="ShareSynchInd",
            type="Attribute"
        )
    )
    share_market_ind: Optional["CustLoyaltyType.ShareMarketInd"] = field(
        default=None,
        metadata=dict(
            name="ShareMarketInd",
            type="Attribute"
        )
    )
    program_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProgramID",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    membership_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MembershipID",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    travel_sector: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelSector",
            type="Attribute"
        )
    )
    loyal_level: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LoyalLevel",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    single_vendor_ind: Optional["CustLoyaltyType.SingleVendorInd"] = field(
        default=None,
        metadata=dict(
            name="SingleVendorInd",
            type="Attribute"
        )
    )
    signup_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SignupDate",
            type="Attribute"
        )
    )
    effective_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EffectiveDate",
            type="Attribute"
        )
    )
    expire_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ExpireDate",
            type="Attribute"
        )
    )
    rph: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RPH",
            type="Attribute",
            pattern=r"[0-9]{1,8}"
        )
    )

    class ShareSynchInd(Enum):
        """value="Inherit" Permission for sharing data for synchronization of
        information held by other travel service providers.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"

    class ShareMarketInd(Enum):
        """value="Inherit" Permission for sharing data for marketing purposes.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"

    class SingleVendorInd(Enum):
        """
        :cvar ALLIANCE:
        :cvar SINGLE_VNDR:
        """
        ALLIANCE = "Alliance"
        SINGLE_VNDR = "SingleVndr"


@dataclass
class DateRangeType:
    """
    :ivar outbound_date: Outbound date
    :ivar date_range: Number of date range
    """
    outbound_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OutboundDate",
            type="Attribute"
        )
    )
    date_range: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DateRange",
            type="Attribute"
        )
    )


@dataclass
class DepartureDaysType:
    """Specify which days of week  to consider for departure.

    :ivar value: Value format: First letter of the name of the day or '_', eg. 'SMT___S' means we are interested in departing at Saturday, Sunday, Monday or Tuesday. Even if there are schedules for Wednesday, Thursday or Friday, they won't be returned in ISell response.
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True,
            length=7
        )
    )


@dataclass
class DocumentType:
    """Provides information on a specific documents.

    :ivar doc_holder_name: Specify document holder name.
    :ivar doc_limitations: Used to indicate any limitations on the document (e.g. as a person may only be allowed to spend a max of 30 days in country on a visitor's visa).
    :ivar share_synch_ind:
    :ivar share_market_ind:
    :ivar doc_issue_authority: Indicates the group or association that granted the document.
    :ivar doc_issue_location: Indicates the location where the document was issued.
    :ivar doc_id: Unique number assigned by authorities to document.
    :ivar doc_type: Indicates the type of document (e.g. Passport, Military ID, Drivers License, national ID, Vaccination Certificate). Refer to OTA Code List Document Type (DOC).
    :ivar gender:
    :ivar birth_date: Indicates the date of birth as indicated in the document, in ISO 8601 prescribed format.
    :ivar effective_date: Indicates the starting date.
    :ivar expire_date: Indicates the ending date.
    """
    doc_holder_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocHolderName",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_length=1.0,
            max_length=64.0
        )
    )
    doc_limitations: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="DocLimitations",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=64.0
        )
    )
    share_synch_ind: Optional["DocumentType.ShareSynchInd"] = field(
        default=None,
        metadata=dict(
            name="ShareSynchInd",
            type="Attribute"
        )
    )
    share_market_ind: Optional["DocumentType.ShareMarketInd"] = field(
        default=None,
        metadata=dict(
            name="ShareMarketInd",
            type="Attribute"
        )
    )
    doc_issue_authority: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocIssueAuthority",
            type="Attribute",
            min_length=1.0,
            max_length=64.0
        )
    )
    doc_issue_location: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocIssueLocation",
            type="Attribute",
            min_length=1.0,
            max_length=64.0
        )
    )
    doc_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocID",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    doc_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocType",
            type="Attribute"
        )
    )
    gender: Optional["DocumentType.Gender"] = field(
        default=None,
        metadata=dict(
            name="Gender",
            type="Attribute"
        )
    )
    birth_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BirthDate",
            type="Attribute"
        )
    )
    effective_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EffectiveDate",
            type="Attribute"
        )
    )
    expire_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ExpireDate",
            type="Attribute"
        )
    )

    class ShareSynchInd(Enum):
        """value="Inherit" Permission for sharing data for synchronization of
        information held by other travel service providers.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"

    class ShareMarketInd(Enum):
        """value="Inherit" Permission for sharing data for marketing purposes.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"

    class Gender(Enum):
        """
        :cvar FEMALE:
        :cvar MALE:
        :cvar UNKNOWN:
        """
        FEMALE = "Female"
        MALE = "Male"
        UNKNOWN = "Unknown"


@dataclass
class EmailType:
    """Electronic email addresses, in IETF specified format.

    :ivar value:
    :ivar share_synch_ind:
    :ivar share_market_ind:
    :ivar default_ind:
    :ivar email_type: Defines the purpose of the e-mail address (e.g. personal, business, listserve). Refer to OTA Code List Email Address Type (EAT).
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=1.0,
            max_length=128.0
        )
    )
    share_synch_ind: Optional["EmailType.ShareSynchInd"] = field(
        default=None,
        metadata=dict(
            name="ShareSynchInd",
            type="Attribute"
        )
    )
    share_market_ind: Optional["EmailType.ShareMarketInd"] = field(
        default=None,
        metadata=dict(
            name="ShareMarketInd",
            type="Attribute"
        )
    )
    default_ind: bool = field(
        default=False,
        metadata=dict(
            name="DefaultInd",
            type="Attribute"
        )
    )
    email_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EmailType",
            type="Attribute"
        )
    )

    class ShareSynchInd(Enum):
        """value="Inherit" Permission for sharing data for synchronization of
        information held by other travel service providers.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"

    class ShareMarketInd(Enum):
        """value="Inherit" Permission for sharing data for marketing purposes.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"


@dataclass
class ExchangeFareType:
    """
    :ivar base_fare_amount: Base fare amount
    :ivar non_refundable_amount: Non-refundable Base Fare Amount. Currency is defined by @BaseFareCurrency.
    :ivar base_fare_currency: Base fare currency
    :ivar fare_calc_currency: Fare calc currency
    :ivar validating_carrier: Validating carrier
    :ivar roe: Rate of Exchange override (note: doesn't need to be specified if FareCalc currency and BaseFare currency is the same).
    """
    base_fare_amount: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="BaseFareAmount",
            type="Attribute",
            required=True,
            fraction_digits=3
        )
    )
    non_refundable_amount: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="NonRefundableAmount",
            type="Attribute",
            fraction_digits=3
        )
    )
    base_fare_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BaseFareCurrency",
            type="Attribute",
            required=True,
            pattern=r"[a-zA-Z]{3}"
        )
    )
    fare_calc_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareCalcCurrency",
            type="Attribute",
            required=True,
            pattern=r"[a-zA-Z]{3}"
        )
    )
    validating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ValidatingCarrier",
            type="Attribute",
            pattern=r"[0-9A-Z]{2,3}"
        )
    )
    roe: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="ROE",
            type="Attribute"
        )
    )


@dataclass
class ExchangeSettingsType:
    """
    :ivar reprice_current_itin: If set to ''false'', disables processing of Current Itin path.
    :ivar attach_exchange_info: If set to ''true'', adds exchange-specific information to the response.
    					The information includes richer Tax elements, ReissueVsExchange attribute and currency conversion rates.
    :ivar reissue_exchange: Process Type Indicator for Primary Request Type
    :ivar branded_results: Enables branded results (if brands are available for returned options)
    :ivar miptimeout_threshold: Hints MIP that it should return options within this amount of time (in seconds)
    :ivar request_type: Used to specify if the request is an usual Exchange request (basic) or an Exchange Context Shopping request (context). When not specified, basic is assumed.
    """
    reprice_current_itin: bool = field(
        default=True,
        metadata=dict(
            name="RepriceCurrentItin",
            type="Attribute"
        )
    )
    attach_exchange_info: bool = field(
        default=False,
        metadata=dict(
            name="AttachExchangeInfo",
            type="Attribute"
        )
    )
    reissue_exchange: Optional["ExchangeSettingsType.ReissueExchange"] = field(
        default=None,
        metadata=dict(
            name="ReissueExchange",
            type="Attribute"
        )
    )
    branded_results: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="BrandedResults",
            type="Attribute"
        )
    )
    miptimeout_threshold: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MIPTimeoutThreshold",
            type="Attribute"
        )
    )
    request_type: Optional["ExchangeSettingsType.RequestType"] = field(
        default=None,
        metadata=dict(
            name="RequestType",
            type="Attribute"
        )
    )

    class ReissueExchange(Enum):
        """
        :cvar A:
        """
        A = "A"

    class RequestType(Enum):
        """
        :cvar BASIC:
        :cvar CONTEXT:
        """
        BASIC = "basic"
        CONTEXT = "context"


@dataclass
class FareDetailsType:
    """You don't need to specify all of these attributes for a given flight. For
    some of them it is sufficient to be specified in the last flight of a given
    fare component. For details, see notes below --- the attributes are annotated
    with ,,last Flight in Fare Component''.

    :ivar component_no: Fare component number
    :ivar basis_code: Fare basis code
    :ivar amount: Fare amount (note: last Flight in Fare Component)
    :ivar vendor: Vendor (note: last Flight in Fare Component)
    :ivar source_vendor: Fare Source Vendor (note: last Flight in Fare Component)
    :ivar tariff: Tariff (note: last Flight in Fare Component)
    :ivar rule_number: Rule Number (note: last Flight in Fare Component)
    :ivar brand_id: Used to indicate brand code
    :ivar program_id:
    """
    component_no: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ComponentNo",
            type="Attribute",
            required=True
        )
    )
    basis_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BasisCode",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=15.0,
            pattern=r"[A-Z0-9]+(/[A-Z0-9]+)?"
        )
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            fraction_digits=3
        )
    )
    vendor: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Vendor",
            type="Attribute"
        )
    )
    source_vendor: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SourceVendor",
            type="Attribute",
            pattern=r"[0-9A-Z]{2,3}"
        )
    )
    tariff: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Tariff",
            type="Attribute"
        )
    )
    rule_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RuleNumber",
            type="Attribute"
        )
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandID",
            type="Attribute",
            min_length=1.0
        )
    )
    program_id: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ProgramID",
            type="Attribute"
        )
    )


@dataclass
class FareOptionalDetailsType:
    """You don't need to specify all of these attributes for a given flight. For
    some of them it is sufficient to be specified in the last flight of a given
    fare component. For details, see notes below --- the attributes are annotated
    with ,,last Flight in Fare Component''.

    :ivar component_no: Fare component number
    :ivar basis_code: Fare basis code
    :ivar amount: Fare amount (note: last Flight in Fare Component)
    :ivar vendor: Vendor (note: last Flight in Fare Component)
    :ivar source_vendor: Fare Source Vendor (note: last Flight in Fare Component)
    :ivar tariff: Tariff (note: last Flight in Fare Component)
    :ivar rule_number: Rule Number (note: last Flight in Fare Component)
    :ivar brand_id: Used to indicate brand code
    :ivar program_id:
    """
    component_no: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ComponentNo",
            type="Attribute"
        )
    )
    basis_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BasisCode",
            type="Attribute",
            min_length=1.0,
            max_length=15.0,
            pattern=r"[A-Z0-9]+(/[A-Z0-9]+)?"
        )
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            fraction_digits=3
        )
    )
    vendor: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Vendor",
            type="Attribute"
        )
    )
    source_vendor: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SourceVendor",
            type="Attribute",
            pattern=r"[0-9A-Z]{2,3}"
        )
    )
    tariff: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Tariff",
            type="Attribute"
        )
    )
    rule_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RuleNumber",
            type="Attribute"
        )
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandID",
            type="Attribute",
            min_length=1.0
        )
    )
    program_id: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ProgramID",
            type="Attribute"
        )
    )


@dataclass
class FlightStopsAsConnectionsType:
    """Treat all stops as connections.

    :ivar ind:
    """
    ind: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Ind",
            type="Attribute",
            required=True
        )
    )


class FlightTypeType(Enum):
    """
    Identifies a particular type of flight - Direct, Stopover etc.
    :cvar CONNECTION: Flight with plane changes, allowing maximum of 24 hours for each change
    :cvar DIRECT: Flight without plane change and possible intermediate landing.
    :cvar NONSTOP: Flight without plane change and without intermediate landing.
    """
    CONNECTION = "Connection"
    DIRECT = "Direct"
    NONSTOP = "Nonstop"


@dataclass
class GlobalDateTimeType:
    """
    :ivar time_window_start: Allowed amount of time before specified time.
    :ivar time_window_end: Allowed amount of time after specified time.
    :ivar time_tolerance: Maximum time difference between actual and desired time.
    :ivar date_flexibility: The number of alternate days around the travel date to search.
    :ivar max_options_per_date: Number of options for requested date.
    :ivar connection_time_min: Minimal amount of time between flights
    :ivar connection_time_max: Maximal amount of time between flights
    :ivar date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS.
    """
    time_window_start: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TimeWindowStart",
            type="Attribute",
            pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    time_window_end: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TimeWindowEnd",
            type="Attribute",
            pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    time_tolerance: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TimeTolerance",
            type="Attribute"
        )
    )
    date_flexibility: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DateFlexibility",
            type="Attribute"
        )
    )
    max_options_per_date: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MaxOptionsPerDate",
            type="Attribute"
        )
    )
    connection_time_min: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ConnectionTimeMin",
            type="Attribute"
        )
    )
    connection_time_max: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ConnectionTimeMax",
            type="Attribute"
        )
    )
    date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DateTime",
            type="Attribute",
            required=True,
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
        )
    )


@dataclass
class GoverningCarrierOverrideType:
    """
    :ivar airline_code: Airline Carrier Code - override the GOVERNING CARRIER to get the fare filed by that carrier.
    """
    airline_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirlineCode",
            type="Attribute",
            required=True,
            pattern=r"[0-9A-Z]{2,3}"
        )
    )


@dataclass
class IncludeVendorPrefType:
    """Consider only these carriers for this leg.

    :ivar code: Identifies a company by the company code.
    """
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )


@dataclass
class JumpCabinLogicType:
    """
    :ivar disabled: Controls if response could contain options with cabin class different than requested.
    """
    disabled: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Disabled",
            type="Attribute",
            required=True
        )
    )


@dataclass
class KeepSameCabinType:
    """
    :ivar enabled: Set to "true" guarantees that all segments within single shopping option belong to the requested cabin.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Enabled",
            type="Attribute",
            required=True
        )
    )


@dataclass
class MileageDisplayType:
    """
    :ivar type: Mileage display type
    :ivar city: Mileage display city
    :ivar surcharge: Mileage surcharge percentage
    """
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    city: Optional[str] = field(
        default=None,
        metadata=dict(
            name="City",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    surcharge: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Surcharge",
            type="Attribute"
        )
    )


@dataclass
class NumTripsType:
    """This element allows a user to specify the number of itineraries returned.

    :ivar number:
    :ivar per_date_min: Minimum number of options to be retrieved for each combination of outbound/inbound dates.
    :ivar per_date_max: Maximum number of options to be retrieved for each combination of outbound/inbound dates.
    :ivar per_market: Number of itineraries per market for alternate cities request. It allows to control market diversity only.
    :ivar per_month: In Advanced Calendar API: Maximum number of itineraries to be retrieved for each departure month and departure/arrival combination.
    """
    number: int = field(
        default=9,
        metadata=dict(
            name="Number",
            type="Attribute",
            min_inclusive=1.0
        )
    )
    per_date_min: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PerDateMin",
            type="Attribute"
        )
    )
    per_date_max: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PerDateMax",
            type="Attribute"
        )
    )
    per_market: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PerMarket",
            type="Attribute"
        )
    )
    per_month: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PerMonth",
            type="Attribute"
        )
    )


@dataclass
class OptionsPerDatePairType:
    """
    :ivar departure: Departure date
    :ivar return_value: Return date
    :ivar min: Minimum number of options per date/date pair
    :ivar max: Maximum number of options per date/date pair
    """
    departure: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Departure",
            type="Attribute",
            required=True,
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
        )
    )
    return_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Return",
            type="Attribute",
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
        )
    )
    min: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Min",
            type="Attribute",
            required=True
        )
    )
    max: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Max",
            type="Attribute",
            required=True
        )
    )


@dataclass
class OverrideDateTimeType:
    """
    :ivar time_window_start: Allowed amount of time before specified time.
    :ivar time_window_end: Allowed amount of time after specified time.
    :ivar time_tolerance: Maximum time difference between actual and desired time.
    :ivar date_flexibility: The number of alternate days around the travel date to search.
    :ivar max_options_per_date: Number of options for requested date.
    :ivar connection_time_min: Minimal amount of time between flights
    :ivar connection_time_max: Maximal amount of time between flights
    :ivar date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS.
    """
    time_window_start: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TimeWindowStart",
            type="Attribute",
            pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    time_window_end: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TimeWindowEnd",
            type="Attribute",
            pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    time_tolerance: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TimeTolerance",
            type="Attribute"
        )
    )
    date_flexibility: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DateFlexibility",
            type="Attribute"
        )
    )
    max_options_per_date: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MaxOptionsPerDate",
            type="Attribute"
        )
    )
    connection_time_min: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ConnectionTimeMin",
            type="Attribute"
        )
    )
    connection_time_max: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ConnectionTimeMax",
            type="Attribute"
        )
    )
    date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DateTime",
            type="Attribute",
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
        )
    )


@dataclass
class PersonNameType:
    """This is an XML Schema representing the OTA Person Name object.

    :ivar name_prefix: Salutation of honorific. (e.g., Mr. Mrs., Ms., Miss, Dr.)
    :ivar given_name: Given name, first name or names
    :ivar middle_name: Person's middle name
    :ivar surname_prefix: e.g "van der", "von", "de"
    :ivar surname: Family name, last name.
    :ivar name_suffix: Hold various name suffixes and letters (e.g. Jr., Sr., III, Ret., Esq.).
    :ivar name_title: Degree or honors (e.g., Ph.D., M.D.)
    :ivar share_synch_ind:
    :ivar share_market_ind:
    :ivar name_type: Type of name of the individual, such as former, nickname, alternate or alias name. Refer to OTA Code List Name Type (NAM).
    """
    name_prefix: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="NamePrefix",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=3,
            min_length=1.0,
            max_length=16.0
        )
    )
    given_name: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="GivenName",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=5,
            min_length=1.0,
            max_length=64.0
        )
    )
    middle_name: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="MiddleName",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=3,
            min_length=1.0,
            max_length=64.0
        )
    )
    surname_prefix: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SurnamePrefix",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_length=1.0,
            max_length=16.0
        )
    )
    surname: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Surname",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True,
            min_length=1.0,
            max_length=64.0
        )
    )
    name_suffix: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="NameSuffix",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=3,
            min_length=1.0,
            max_length=16.0
        )
    )
    name_title: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="NameTitle",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=5,
            min_length=1.0,
            max_length=16.0
        )
    )
    share_synch_ind: Optional["PersonNameType.ShareSynchInd"] = field(
        default=None,
        metadata=dict(
            name="ShareSynchInd",
            type="Attribute"
        )
    )
    share_market_ind: Optional["PersonNameType.ShareMarketInd"] = field(
        default=None,
        metadata=dict(
            name="ShareMarketInd",
            type="Attribute"
        )
    )
    name_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NameType",
            type="Attribute"
        )
    )

    class ShareSynchInd(Enum):
        """value="Inherit" Permission for sharing data for synchronization of
        information held by other travel service providers.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"

    class ShareMarketInd(Enum):
        """value="Inherit" Permission for sharing data for marketing purposes.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"


@dataclass
class PlusUpType:
    """
    :ivar amount: Amount
    :ivar origin_city: Origin City
    :ivar destination_city: Destination City
    :ivar fare_origin_city: Fare Origin City
    :ivar fare_destination_city: Fare Destination City
    :ivar via_city: Via City
    :ivar message: Message
    :ivar country_of_payment: Country of payment
    """
    amount: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True,
            fraction_digits=3
        )
    )
    origin_city: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OriginCity",
            type="Attribute",
            required=True,
            pattern=r"[a-zA-Z]{3}"
        )
    )
    destination_city: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DestinationCity",
            type="Attribute",
            required=True,
            pattern=r"[a-zA-Z]{3}"
        )
    )
    fare_origin_city: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareOriginCity",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    fare_destination_city: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareDestinationCity",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    via_city: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ViaCity",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    message: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute"
        )
    )
    country_of_payment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CountryOfPayment",
            type="Attribute",
            pattern=r"[a-zA-Z]{2}"
        )
    )


@dataclass
class PointOfSaleOverrideType:
    """
    :ivar code:
    """
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )


@dataclass
class PointOfTicketingOverrideType:
    """
    :ivar code:
    """
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )


@dataclass
class PositionType:
    """Used to identify geospatial postion of the requesting entity.

    :ivar latitude:
    :ivar longitude:
    :ivar altitude:
    """
    latitude: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Latitude",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    longitude: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Longitude",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    altitude: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Altitude",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )


class PreferLevelType(Enum):
    """Used to specify a preference level for something that is or will be
    requested (e.g. a supplier of a service, a type of service, a form of payment,
    etc.).

    :cvar ONLY:
    :cvar PREFERRED:
    :cvar UNACCEPTABLE:
    """
    ONLY = "Only"
    PREFERRED = "Preferred"
    UNACCEPTABLE = "Unacceptable"


@dataclass
class RequestLocationType:
    """Code and optional string to describe a location point.

    :ivar value:
    :ivar location_code: Location identifying code. Required unless AirportsGroup or AllAirports is specified. Cannot appear with AirportsGroup nor AllAirports.
    :ivar airports_group: Name of the airports group
    :ivar code_context: Identifies the context of the identifying code, such as IATA, ARC, or internal code, etc.
    """
    value: Optional[str] = field(
        default=None,
    )
    location_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LocationCode",
            type="Attribute",
            pattern=r"[A-Z]{1,8}"
        )
    )
    airports_group: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirportsGroup",
            type="Attribute",
            pattern=r"[A-Za-z0-9]{1,40}"
        )
    )
    code_context: str = field(
        default="IATA",
        metadata=dict(
            name="CodeContext",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )


class RequestPricingSourceType(Enum):
    """It can be used to indicate whether the fare is public or private.

    :cvar BOTH:
    :cvar PRIVATE:
    :cvar PUBLISHED:
    """
    BOTH = "Both"
    PRIVATE = "Private"
    PUBLISHED = "Published"


@dataclass
class ReservationType:
    """
    :ivar status: Reservation status
    :ivar real_status: Real reservation status
    """
    status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            pattern=r"[A-Z]{1,2}"
        )
    )
    real_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RealStatus",
            type="Attribute",
            pattern=r"[A-Z]{1,2}"
        )
    )


@dataclass
class RetailerRulesType:
    """
    :ivar retailer_rule:
    :ivar force: If set to true, only fares with a matched Business Rule containing the specified Retailer Rule Qualifier will be returned
    """
    retailer_rule: List["RetailerRulesType.RetailerRule"] = field(
        default_factory=list,
        metadata=dict(
            name="RetailerRule",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=4
        )
    )
    force: bool = field(
        default=False,
        metadata=dict(
            name="Force",
            type="Attribute"
        )
    )

    @dataclass
    class RetailerRule:
        """
        :ivar code:
        """
        code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Code",
                type="Attribute",
                required=True,
                pattern=r"[0-9a-zA-Z]{2,20}"
            )
        )


@dataclass
class RoutingLegType:
    """Definition of individual routing legs, at least one leg must be present.

    :ivar inbound_outbound_carrier:
    :ivar inbound_carrier:
    :ivar outbound_carrier:
    :ivar connect_point:
    """
    inbound_outbound_carrier: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="InboundOutboundCarrier",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\*|[A-Z][A-Z0-9]{1}|[A-Z0-9][A-Z][A-Z0-9]?"
        )
    )
    inbound_carrier: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="InboundCarrier",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\*|[A-Z][A-Z0-9]{1}|[A-Z0-9][A-Z][A-Z0-9]?"
        )
    )
    outbound_carrier: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="OutboundCarrier",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\*|[A-Z][A-Z0-9]{1}|[A-Z0-9][A-Z][A-Z0-9]?"
        )
    )
    connect_point: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ConnectPoint",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\*|\?|\+|\.|[A-Z]{3,5}"
        )
    )


@dataclass
class SeatStatusSimType:
    """
    :ivar type:
    :ivar command:
    """
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    command: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Command",
            type="Attribute"
        )
    )


@dataclass
class SideTripType:
    """
    :ivar number: Side trip number
    :ivar start: Side trip start
    :ivar end: Side trip end
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute"
        )
    )
    start: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Start",
            type="Attribute"
        )
    )
    end: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="End",
            type="Attribute"
        )
    )


@dataclass
class StateProvType:
    """State, province, or region name or code needed to identify location.

    :ivar value:
    :ivar state_code: The postal service standard code or abbreviation for the state, province, or region.
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=0.0,
            max_length=64.0
        )
    )
    state_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StateCode",
            type="Attribute",
            min_length=2.0,
            max_length=8.0
        )
    )


@dataclass
class StreetNmbrType:
    """Street name; number on street.

    :ivar value:
    :ivar po_box: Defines a Post Office Box number.
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=0.0,
            max_length=64.0
        )
    )
    po_box: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PO_Box",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )


@dataclass
class TaxCodeType:
    """Defines the data fields available for tax code.

    :ivar tax_code: Identifies the code for the tax.
    """
    tax_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TaxCode",
            type="Attribute",
            required=True,
            pattern=r"[A-Z0-9]{2}[A-Z0-9]{0,1}"
        )
    )


@dataclass
class TelephoneType:
    """Construct for holding a telephone number.

    :ivar share_synch_ind:
    :ivar share_market_ind:
    :ivar phone_location_type: Refer to OTA Code List Phone Location Type (PLT).
    :ivar phone_tech_type: Indicates type of technology associated with this telephone number, such as Voice, Data, Fax, Pager, Mobile, TTY, etc. Refer to OTA Code List Phone Technology Type (PTT).
    :ivar country_access_code: Code assigned by telecommunications authorities for international country access identifier.
    :ivar area_city_code: Code assigned for telephones in a specific region, city, or area.
    :ivar phone_number: Telephone number assigned to a single location.
    :ivar extension: Extension to reach a specific party at the phone number.
    :ivar pin: Additional codes used for pager or telephone access rights.
    :ivar formatted_ind: Specifies if the associated data is formatted or not. If true, then it is formatted, if false, then not formatted.
    """
    share_synch_ind: Optional["TelephoneType.ShareSynchInd"] = field(
        default=None,
        metadata=dict(
            name="ShareSynchInd",
            type="Attribute"
        )
    )
    share_market_ind: Optional["TelephoneType.ShareMarketInd"] = field(
        default=None,
        metadata=dict(
            name="ShareMarketInd",
            type="Attribute"
        )
    )
    phone_location_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PhoneLocationType",
            type="Attribute"
        )
    )
    phone_tech_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PhoneTechType",
            type="Attribute"
        )
    )
    country_access_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CountryAccessCode",
            type="Attribute",
            pattern=r"[0-9]{1,3}"
        )
    )
    area_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AreaCityCode",
            type="Attribute",
            pattern=r"[0-9]{1,8}"
        )
    )
    phone_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PhoneNumber",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=32.0
        )
    )
    extension: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Extension",
            type="Attribute",
            pattern=r"[0-9]{1,5}"
        )
    )
    pin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PIN",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )
    formatted_ind: bool = field(
        default=False,
        metadata=dict(
            name="FormattedInd",
            type="Attribute"
        )
    )

    class ShareSynchInd(Enum):
        """value="Inherit" Permission for sharing data for synchronization of
        information held by other travel service providers.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"

    class ShareMarketInd(Enum):
        """value="Inherit" Permission for sharing data for marketing purposes.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"


@dataclass
class TravelDateTimeType:
    """Date and time of trip, that allows specifying a time window before and after
    the given date.

    :ivar departure_date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS
    :ivar arrival_date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS
    :ivar departure_dates:
    :ivar arrival_dates: Allowed only for Advanced Calendar API.
    :ivar departure_window: This should be of the form HHMMHHMM.
    :ivar arrival_window: This should be of the form HHMMHHMM.
    """
    departure_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDateTime",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
        )
    )
    arrival_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalDateTime",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
        )
    )
    departure_dates: Optional["TravelDateTimeType.DepartureDates"] = field(
        default=None,
        metadata=dict(
            name="DepartureDates",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    arrival_dates: Optional["TravelDateTimeType.ArrivalDates"] = field(
        default=None,
        metadata=dict(
            name="ArrivalDates",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    departure_window: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureWindow",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            pattern=r"([0-2][0-9][0-5][0-9]){2}"
        )
    )
    arrival_window: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalWindow",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            pattern=r"([0-2][0-9][0-5][0-9]){2}"
        )
    )

    @dataclass
    class DepartureDates:
        """
        :ivar day:
        :ivar days_range:
        :ivar length_of_stay: Amount of days between previous leg's DEPARTURE date and current leg's DEPARTURE date. NOTE: Allowed only in 2nd or further "OriginDestinationInformation".

        											Example: for outbound departing on Jan 20, LengthOfStay/@Days="2" means inbound departing on Jan 22.
        :ivar length_of_stay_range: See comment on "LengthOfStay" element.
        """
        day: List["TravelDateTimeType.DepartureDates.Day"] = field(
            default_factory=list,
            metadata=dict(
                name="Day",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        days_range: List["TravelDateTimeType.DepartureDates.DaysRange"] = field(
            default_factory=list,
            metadata=dict(
                name="DaysRange",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        length_of_stay: List["TravelDateTimeType.DepartureDates.LengthOfStay"] = field(
            default_factory=list,
            metadata=dict(
                name="LengthOfStay",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        length_of_stay_range: List["TravelDateTimeType.DepartureDates.LengthOfStayRange"] = field(
            default_factory=list,
            metadata=dict(
                name="LengthOfStayRange",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

        @dataclass
        class LengthOfStay:
            """
            :ivar days:
            """
            days: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Days",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class LengthOfStayRange:
            """
            :ivar min_days: (inclusive)
            :ivar max_days: (inclusive)
            """
            min_days: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="MinDays",
                    type="Attribute",
                    required=True
                )
            )
            max_days: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="MaxDays",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class Day:
            """
            :ivar date:
            """
            date: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Date",
                    type="Attribute",
                    pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
                )
            )

        @dataclass
        class DaysRange:
            """
            :ivar from_date:
            :ivar to_date:
            :ivar week_days:
            """
            from_date: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="FromDate",
                    type="Attribute",
                    pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
                )
            )
            to_date: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="ToDate",
                    type="Attribute",
                    pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
                )
            )
            week_days: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="WeekDays",
                    type="Attribute",
                    pattern=r"[S_][M_][T_][W_][T_][F_][S_]"
                )
            )

    @dataclass
    class ArrivalDates:
        """
        :ivar day:
        :ivar days_range:
        """
        day: List["TravelDateTimeType.ArrivalDates.Day"] = field(
            default_factory=list,
            metadata=dict(
                name="Day",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        days_range: List["TravelDateTimeType.ArrivalDates.DaysRange"] = field(
            default_factory=list,
            metadata=dict(
                name="DaysRange",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

        @dataclass
        class Day:
            """
            :ivar date:
            """
            date: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Date",
                    type="Attribute",
                    pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
                )
            )

        @dataclass
        class DaysRange:
            """
            :ivar from_date:
            :ivar to_date:
            :ivar week_days:
            """
            from_date: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="FromDate",
                    type="Attribute",
                    pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
                )
            )
            to_date: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="ToDate",
                    type="Attribute",
                    pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
                )
            )
            week_days: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="WeekDays",
                    type="Attribute",
                    pattern=r"[S_][M_][T_][W_][T_][F_][S_]"
                )
            )


@dataclass
class TravelerInfoSummaryTpaExtensionsType:
    """
    :ivar traveler_rating: Customer Value Scores and Frequent Flyer Tiers for one traveler. It can influence Availability results when provided.
    """
    class Meta:
        name = "TravelerInfoSummary_TPA_ExtensionsType"

    traveler_rating: List["TravelerInfoSummaryTpaExtensionsType.TravelerRating"] = field(
        default_factory=list,
        metadata=dict(
            name="TravelerRating",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class TravelerRating:
        """
        :ivar score:
        :ivar frequent_flyer:
        """
        score: List["TravelerInfoSummaryTpaExtensionsType.TravelerRating.Score"] = field(
            default_factory=list,
            metadata=dict(
                name="Score",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        frequent_flyer: List["TravelerInfoSummaryTpaExtensionsType.TravelerRating.FrequentFlyer"] = field(
            default_factory=list,
            metadata=dict(
                name="FrequentFlyer",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

        @dataclass
        class Score:
            """
            :ivar value:
            :ivar carrier:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )
            carrier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Carrier",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class FrequentFlyer:
            """
            :ivar tier:
            :ivar carrier:
            """
            tier: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Tier",
                    type="Attribute",
                    required=True
                )
            )
            carrier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Carrier",
                    type="Attribute",
                    required=True
                )
            )


@dataclass
class TravelerRefNumberType:
    """A reference place holder used as a pointer to link back to the traveler.

    :ivar rph: Reference place holder.
    """
    rph: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RPH",
            type="Attribute",
            pattern=r"[0-9]{1,8}"
        )
    )


class ValidatingCarrierPreferLevelType(Enum):
    """Used to specify a preference level for ValidatingCarrier. For adding new
    enums see PreferLevelType.

    :cvar PREFERRED:
    :cvar UNACCEPTABLE:
    """
    PREFERRED = "Preferred"
    UNACCEPTABLE = "Unacceptable"


@dataclass
class XofaresType:
    """XOFares indicator.

    :ivar value:
    """
    class Meta:
        name = "XOFaresType"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AddressType:
    """
    :ivar street_nmbr: Street Name and Number within the address
    :ivar bldg_room: Building name, room, apartment, or suite number.
    :ivar address_line:
    :ivar city_name: City name eg. Dublin
    :ivar postal_code: Post Office Code number.
    :ivar county: County Name eg. Fairfax
    :ivar state_prov: State name eg. Texas
    :ivar country_name: Country name eg. Ireland
    :ivar formatted_ind: Specifies if the associated data is formatted or not. If true, then it is formatted, if false, then not formatted.
    :ivar share_synch_ind:
    :ivar share_market_ind:
    :ivar type: Defines the type of address (e.g. home, business, other). Refer to OTA Code List Communication Location Type (CLT).
    """
    street_nmbr: Optional[StreetNmbrType] = field(
        default=None,
        metadata=dict(
            name="StreetNmbr",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    bldg_room: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BldgRoom",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_length=0.0,
            max_length=64.0
        )
    )
    address_line: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AddressLine",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=5,
            min_length=1.0,
            max_length=64.0
        )
    )
    city_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CityName",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_length=1.0,
            max_length=64.0
        )
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PostalCode",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_length=1.0,
            max_length=16.0
        )
    )
    county: Optional[str] = field(
        default=None,
        metadata=dict(
            name="County",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_length=1.0,
            max_length=32.0
        )
    )
    state_prov: Optional[StateProvType] = field(
        default=None,
        metadata=dict(
            name="StateProv",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    country_name: Optional[CountryNameType] = field(
        default=None,
        metadata=dict(
            name="CountryName",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    formatted_ind: bool = field(
        default=False,
        metadata=dict(
            name="FormattedInd",
            type="Attribute"
        )
    )
    share_synch_ind: Optional["AddressType.ShareSynchInd"] = field(
        default=None,
        metadata=dict(
            name="ShareSynchInd",
            type="Attribute"
        )
    )
    share_market_ind: Optional["AddressType.ShareMarketInd"] = field(
        default=None,
        metadata=dict(
            name="ShareMarketInd",
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )

    class ShareSynchInd(Enum):
        """value="Inherit" Permission for sharing data for synchronization of
        information held by other travel service providers.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"

    class ShareMarketInd(Enum):
        """value="Inherit" Permission for sharing data for marketing purposes.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"


@dataclass
class AltCitiesCombinationsType:
    """Which (if any) alt cities locations should be handled in a special way (i.e.
    Validate instead of precomputed path).

    :ivar origins: Which origins to process in live path (All or Main only)
    :ivar destinations: Which destinations to process in live path (All or Main only)
    """
    origins: AltCitiesCombinationsLocationsType = field(
        default="Main",
        metadata=dict(
            name="Origins",
            type="Attribute"
        )
    )
    destinations: AltCitiesCombinationsLocationsType = field(
        default="Main",
        metadata=dict(
            name="Destinations",
            type="Attribute"
        )
    )


@dataclass
class ArunkType:
    """
    :ivar origin_location: Origin code
    :ivar destination_location: Destination code
    :ivar side_trip: Side trip information
    """
    origin_location: Optional[RequestLocationType] = field(
        default=None,
        metadata=dict(
            name="OriginLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    destination_location: Optional[RequestLocationType] = field(
        default=None,
        metadata=dict(
            name="DestinationLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    side_trip: Optional[SideTripType] = field(
        default=None,
        metadata=dict(
            name="SideTrip",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )


@dataclass
class BookingClassPrefType:
    """Booking class code and preference level for specifying booking classes
    preferred/not preferred in a request.

    :ivar res_book_desig_code: Booking class code
    :ivar prefer_level:
    """
    res_book_desig_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ResBookDesigCode",
            type="Attribute",
            required=True,
            pattern=r"[A-Z]{1,2}"
        )
    )
    prefer_level: PreferLevelType = field(
        default="Preferred",
        metadata=dict(
            name="PreferLevel",
            type="Attribute"
        )
    )


@dataclass
class CabinPrefType:
    """Indicates preferences for choice of airline cabin for a given travel
    situation.

    :ivar prefer_level:
    :ivar cabin: Specify cabin type.
    """
    prefer_level: PreferLevelType = field(
        default="Preferred",
        metadata=dict(
            name="PreferLevel",
            type="Attribute"
        )
    )
    cabin: Optional[CabinType] = field(
        default=None,
        metadata=dict(
            name="Cabin",
            type="Attribute"
        )
    )


@dataclass
class CachePartitionGroupType:
    """
    :ivar partition:
    """
    partition: List[CachePartitionType] = field(
        default_factory=list,
        metadata=dict(
            name="Partition",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=2,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class CompanyNamePrefType(CompanyNameType):
    """Identifies a preferred company by name.

    :ivar prefer_level:
    :ivar type: Specify what type  of carrier it comes to.
    """
    prefer_level: PreferLevelType = field(
        default="Preferred",
        metadata=dict(
            name="PreferLevel",
            type="Attribute"
        )
    )
    type: Optional[CarrierType] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )


@dataclass
class ConnectionType:
    """To specify connection locations, preference level for each, min connection
    time, and whether location is specified for stopping or changing.

    :ivar connection_location:
    """
    connection_location: List["ConnectionType.ConnectionLocation"] = field(
        default_factory=list,
        metadata=dict(
            name="ConnectionLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=9
        )
    )

    @dataclass
    class ConnectionLocation(RequestLocationType):
        """
        :ivar inclusive:
        :ivar prefer_level:
        :ivar min_change_time: Number of minutes between connections.
        :ivar connection_info:
        """
        inclusive: bool = field(
            default=True,
            metadata=dict(
                name="Inclusive",
                type="Attribute"
            )
        )
        prefer_level: PreferLevelType = field(
            default="Preferred",
            metadata=dict(
                name="PreferLevel",
                type="Attribute"
            )
        )
        min_change_time: Optional[int] = field(
            default=None,
            metadata=dict(
                name="MinChangeTime",
                type="Attribute"
            )
        )
        connection_info: Optional["ConnectionType.ConnectionLocation.ConnectionInfo"] = field(
            default=None,
            metadata=dict(
                name="ConnectionInfo",
                type="Attribute"
            )
        )

        class ConnectionInfo(Enum):
            """
            :cvar CHANGE: Location is for changing.
            :cvar STOP: Location is for stopping.
            :cvar VIA: Location without stopping or changing.
            """
            CHANGE = "Change"
            STOP = "Stop"
            VIA = "Via"


@dataclass
class DiversityControlType:
    """These parameters control how IntellSell should select itineraries based not
    necessarily on cheapest price, but also on other criteria that guarantee a
    diverse response.

    :ivar low_fare_bucket:
    :ivar dimensions:
    """
    low_fare_bucket: Optional["DiversityControlType.LowFareBucket"] = field(
        default=None,
        metadata=dict(
            name="LowFareBucket",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    dimensions: Optional["DiversityControlType.Dimensions"] = field(
        default=None,
        metadata=dict(
            name="Dimensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )

    @dataclass
    class LowFareBucket:
        """
        :ivar options:
        :ivar fare_cut_off:
        """
        options: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Options",
                type="Attribute",
                pattern=r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%"
            )
        )
        fare_cut_off: Optional[str] = field(
            default=None,
            metadata=dict(
                name="FareCutOff",
                type="Attribute",
                pattern=r"(0|100|[1-9][0-9]?)%"
            )
        )

    @dataclass
    class Dimensions:
        """
        :ivar travel_time:
        :ivar carrier:
        :ivar operating_duplicate:
        :ivar inbound_outbound_pairing:
        :ivar time_of_day:
        :ivar stops_number:
        :ivar price_weight:
        """
        travel_time: Optional["DiversityControlType.Dimensions.TravelTime"] = field(
            default=None,
            metadata=dict(
                name="TravelTime",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        carrier: Optional["DiversityControlType.Dimensions.Carrier"] = field(
            default=None,
            metadata=dict(
                name="Carrier",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        operating_duplicate: Optional["DiversityControlType.Dimensions.OperatingDuplicate"] = field(
            default=None,
            metadata=dict(
                name="OperatingDuplicate",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        inbound_outbound_pairing: Optional["DiversityControlType.Dimensions.InboundOutboundPairing"] = field(
            default=None,
            metadata=dict(
                name="InboundOutboundPairing",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        time_of_day: Optional["DiversityControlType.Dimensions.TimeOfDay"] = field(
            default=None,
            metadata=dict(
                name="TimeOfDay",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        stops_number: Optional["DiversityControlType.Dimensions.StopsNumber"] = field(
            default=None,
            metadata=dict(
                name="StopsNumber",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        price_weight: int = field(
            default=10,
            metadata=dict(
                name="PriceWeight",
                type="Attribute",
                min_inclusive=0.0,
                max_inclusive=10.0
            )
        )

        @dataclass
        class TravelTime:
            """
            :ivar weight:
            """
            weight: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Weight",
                    type="Attribute",
                    required=True,
                    min_inclusive=1.0,
                    max_inclusive=10.0
                )
            )

        @dataclass
        class Carrier:
            """
            :ivar default:
            :ivar override:
            :ivar weight:
            :ivar online_indicator:
            """
            default: Optional["DiversityControlType.Dimensions.Carrier.Default"] = field(
                default=None,
                metadata=dict(
                    name="Default",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            override: List["DiversityControlType.Dimensions.Carrier.Override"] = field(
                default_factory=list,
                metadata=dict(
                    name="Override",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            weight: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Weight",
                    type="Attribute",
                    required=True,
                    min_inclusive=1.0,
                    max_inclusive=10.0
                )
            )
            online_indicator: bool = field(
                default=False,
                metadata=dict(
                    name="OnlineIndicator",
                    type="Attribute"
                )
            )

            @dataclass
            class Default:
                """
                :ivar options:
                """
                options: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Options",
                        type="Attribute",
                        required=True,
                        pattern=r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%"
                    )
                )

            @dataclass
            class Override:
                """
                :ivar code:
                :ivar options:
                """
                code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Code",
                        type="Attribute",
                        required=True,
                        pattern=r"[0-9A-Z]{2,3}"
                    )
                )
                options: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Options",
                        type="Attribute",
                        required=True,
                        pattern=r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%"
                    )
                )

        @dataclass
        class OperatingDuplicate:
            """
            :ivar preferred_carrier:
            :ivar weight:
            """
            preferred_carrier: List["DiversityControlType.Dimensions.OperatingDuplicate.PreferredCarrier"] = field(
                default_factory=list,
                metadata=dict(
                    name="PreferredCarrier",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            weight: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Weight",
                    type="Attribute",
                    required=True,
                    min_inclusive=1.0,
                    max_inclusive=10.0
                )
            )

            @dataclass
            class PreferredCarrier:
                """
                :ivar code:
                """
                code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Code",
                        type="Attribute",
                        required=True,
                        pattern=r"[0-9A-Z]{2,3}"
                    )
                )

        @dataclass
        class InboundOutboundPairing:
            """
            :ivar weight:
            :ivar duplicates:
            """
            weight: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Weight",
                    type="Attribute",
                    required=True,
                    min_inclusive=1.0,
                    max_inclusive=10.0
                )
            )
            duplicates: int = field(
                default=1,
                metadata=dict(
                    name="Duplicates",
                    type="Attribute"
                )
            )

        @dataclass
        class TimeOfDay:
            """
            :ivar distribution: Exactly one attribute: either Direction or Leg must be provided
            :ivar weight:
            """
            distribution: List["DiversityControlType.Dimensions.TimeOfDay.Distribution"] = field(
                default_factory=list,
                metadata=dict(
                    name="Distribution",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            weight: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Weight",
                    type="Attribute",
                    required=True,
                    min_inclusive=1.0,
                    max_inclusive=10.0
                )
            )

            @dataclass
            class Distribution:
                """
                :ivar range:
                :ivar direction:
                :ivar leg:
                :ivar endpoint:
                """
                range: List["DiversityControlType.Dimensions.TimeOfDay.Distribution.Range"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="Range",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=0,
                        max_occurs=4
                    )
                )
                direction: Optional[OutboundOrInbound] = field(
                    default=None,
                    metadata=dict(
                        name="Direction",
                        type="Attribute"
                    )
                )
                leg: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Leg",
                        type="Attribute"
                    )
                )
                endpoint: DepartureOrArrival = field(
                    default="Departure",
                    metadata=dict(
                        name="Endpoint",
                        type="Attribute"
                    )
                )

                @dataclass
                class Range:
                    """Either all Range elements shall contain attribute Options or none. Ranges
                    shall not overlap.

                    :ivar begin:
                    :ivar end:
                    :ivar options:
                    """
                    begin: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Begin",
                            type="Attribute",
                            required=True,
                            pattern=r"([0-1]?[0-9]|2[0-3]):[0-5][0-9]"
                        )
                    )
                    end: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="End",
                            type="Attribute",
                            required=True,
                            pattern=r"([0-1]?[0-9]|2[0-3]):[0-5][0-9]"
                        )
                    )
                    options: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Options",
                            type="Attribute",
                            pattern=r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%"
                        )
                    )

        @dataclass
        class StopsNumber:
            """
            :ivar weight:
            """
            weight: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Weight",
                    type="Attribute",
                    required=True,
                    min_inclusive=1.0,
                    max_inclusive=10.0
                )
            )


@dataclass
class EquipmentTypePref(EquipmentType):
    """
    :ivar prefer_level:
    :ivar wide_body: Specify if equipment should have a wide body or not.
    """
    prefer_level: PreferLevelType = field(
        default="Preferred",
        metadata=dict(
            name="PreferLevel",
            type="Attribute"
        )
    )
    wide_body: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="WideBody",
            type="Attribute"
        )
    )


@dataclass
class ExchangeOriginDestinationFlightType:
    """
    :ivar origin_location: Flight origin code
    :ivar destination_location: Flight destination code
    :ivar airline: Airline information
    :ivar side_trip: Side trip information
    :ivar reservation: Reservation information
    :ivar mileage_display: Mileage information
    :ivar booking_date_time: Booking date and time
    :ivar fare:
    :ivar plus_up:
    :ivar number: Flight number
    :ivar departure_date_time: Departure date and time
    :ivar arrival_date_time: Arrival date and time
    :ivar marriage_status: Marriage status
    :ivar type: Flight type (A: Air Segment, K: ARUNK, O: Open Segment)
    :ivar flown: Specify whether the flight is flown.
    :ivar class_of_service: Class of service
    """
    origin_location: Optional[RequestLocationType] = field(
        default=None,
        metadata=dict(
            name="OriginLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    destination_location: Optional[RequestLocationType] = field(
        default=None,
        metadata=dict(
            name="DestinationLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    airline: Optional[AirlineType] = field(
        default=None,
        metadata=dict(
            name="Airline",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    side_trip: Optional[SideTripType] = field(
        default=None,
        metadata=dict(
            name="SideTrip",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    reservation: Optional[ReservationType] = field(
        default=None,
        metadata=dict(
            name="Reservation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    mileage_display: List[MileageDisplayType] = field(
        default_factory=list,
        metadata=dict(
            name="MileageDisplay",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    booking_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingDateTime",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?"
        )
    )
    fare: Optional["ExchangeOriginDestinationFlightType.Fare"] = field(
        default=None,
        metadata=dict(
            name="Fare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    plus_up: List[PlusUpType] = field(
        default_factory=list,
        metadata=dict(
            name="PlusUp",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True
        )
    )
    departure_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDateTime",
            type="Attribute",
            required=True,
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?"
        )
    )
    arrival_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalDateTime",
            type="Attribute",
            required=True,
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?"
        )
    )
    marriage_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MarriageStatus",
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True,
            pattern=r"[AKO]"
        )
    )
    flown: bool = field(
        default=False,
        metadata=dict(
            name="Flown",
            type="Attribute"
        )
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            required=True,
            pattern=r"[A-Z]{1,2}"
        )
    )

    @dataclass
    class Fare(FareDetailsType):
        """
        :ivar adjustment:
        """
        adjustment: Optional["ExchangeOriginDestinationFlightType.Fare.Adjustment"] = field(
            default=None,
            metadata=dict(
                name="Adjustment",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

        @dataclass
        class Adjustment:
            """
            :ivar value: Adjustment Value, can be positive or negative, number or percentage
            :ivar currency: Currency of Adjustment's Value
            :ivar group: Markup/Discount Group
            """
            value: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True,
                    pattern=r"(\+|-)?([0-9]+(\.[0-9]*)?|\.[0-9]+)%?"
                )
            )
            currency: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Currency",
                    type="Attribute",
                    pattern=r"[a-zA-Z]{3}"
                )
            )
            group: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Group",
                    type="Attribute"
                )
            )


@dataclass
class ExchangeTpaExtensionsType:
    """
    :ivar award_shopping:
    """
    class Meta:
        name = "ExchangeTPA_ExtensionsType"

    award_shopping: Optional[AwardShoppingType] = field(
        default=None,
        metadata=dict(
            name="AwardShopping",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )


@dataclass
class FareRestrictPrefType:
    """Identifies preferences for airfare restrictions acceptable or not acceptable
    for a given travel situation.

    :ivar prefer_level:
    :ivar fare_restriction: Refer to OTA Code List Fare Restriction (FAR).
    """
    prefer_level: PreferLevelType = field(
        default="Preferred",
        metadata=dict(
            name="PreferLevel",
            type="Attribute"
        )
    )
    fare_restriction: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareRestriction",
            type="Attribute"
        )
    )


@dataclass
class FlexibleFaresType:
    """
    :ivar fare_parameters: This element specifies parameters for desired fare.
    """
    fare_parameters: List["FlexibleFaresType.FareParameters"] = field(
        default_factory=list,
        metadata=dict(
            name="FareParameters",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=10
        )
    )

    @dataclass
    class FareParameters:
        """
        :ivar exclude_restricted: Setting this to true means the same as setting ResTicketing, MinMaxStay and RefundPenalty to false.
        :ivar res_ticketing: If set to true, fares that have a reservation/ticketing can be included in the responses. If set to false, then no fares that include reservation/ticketing requirement will be included in the response. This is negation of XA qualifier.
        :ivar min_max_stay: If set to true, fares that have a min/max stay can be included in the responses. If set to false, then no fares that include a min/max stay requirement will be included in the response. This is negation of XS qualifier.
        :ivar refund_penalty: If set to true, fares that have a refund penalty can be included in the responses. If set to false, then no fares that include a refund penalty requirement will be included in the response. This is negation of XP qualifier.
        :ivar public_fare: This element finds only public fares.
        :ivar private_fare: This element finds only private fares.
        :ivar cabin: This element specifies preffered cabin type.
        :ivar passenger_type: This element specifies PTC used to find this fare.
        :ivar negotiated_fares_only: If set to true then returned fares need to match AcccountCode/CorpID specified in Fare Group definition on all fare components.
        :ivar xofares: If set to true only fares matching PTC specified in the Flex Fare Group will be returned on all fare components.
        :ivar passenger_type_quantity: Define information on the number of passengers of a specific type.
        :ivar jump_cabin_logic:
        :ivar keep_same_cabin:
        :ivar corporate_id:
        :ivar account_code:
        """
        exclude_restricted: Optional["FlexibleFaresType.FareParameters.ExcludeRestricted"] = field(
            default=None,
            metadata=dict(
                name="ExcludeRestricted",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        res_ticketing: Optional["FlexibleFaresType.FareParameters.ResTicketing"] = field(
            default=None,
            metadata=dict(
                name="ResTicketing",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        min_max_stay: Optional["FlexibleFaresType.FareParameters.MinMaxStay"] = field(
            default=None,
            metadata=dict(
                name="MinMaxStay",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        refund_penalty: Optional["FlexibleFaresType.FareParameters.RefundPenalty"] = field(
            default=None,
            metadata=dict(
                name="RefundPenalty",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        public_fare: Optional["FlexibleFaresType.FareParameters.PublicFare"] = field(
            default=None,
            metadata=dict(
                name="PublicFare",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        private_fare: Optional["FlexibleFaresType.FareParameters.PrivateFare"] = field(
            default=None,
            metadata=dict(
                name="PrivateFare",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        cabin: Optional["FlexibleFaresType.FareParameters.Cabin"] = field(
            default=None,
            metadata=dict(
                name="Cabin",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        passenger_type: Optional["FlexibleFaresType.FareParameters.PassengerType"] = field(
            default=None,
            metadata=dict(
                name="PassengerType",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        negotiated_fares_only: Optional["FlexibleFaresType.FareParameters.NegotiatedFaresOnly"] = field(
            default=None,
            metadata=dict(
                name="NegotiatedFaresOnly",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        xofares: Optional["FlexibleFaresType.FareParameters.Xofares"] = field(
            default=None,
            metadata=dict(
                name="XOFares",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        passenger_type_quantity: List[PassengerTypeQuantityType] = field(
            default_factory=list,
            metadata=dict(
                name="PassengerTypeQuantity",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=4
            )
        )
        jump_cabin_logic: Optional[JumpCabinLogicType] = field(
            default=None,
            metadata=dict(
                name="JumpCabinLogic",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        keep_same_cabin: Optional[KeepSameCabinType] = field(
            default=None,
            metadata=dict(
                name="KeepSameCabin",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        corporate_id: List["FlexibleFaresType.FareParameters.CorporateId"] = field(
            default_factory=list,
            metadata=dict(
                name="CorporateID",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        account_code: List["FlexibleFaresType.FareParameters.AccountCode"] = field(
            default_factory=list,
            metadata=dict(
                name="AccountCode",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

        @dataclass
        class ExcludeRestricted:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class ResTicketing:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MinMaxStay:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class RefundPenalty:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class PublicFare:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class PrivateFare:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class Cabin:
            """
            :ivar type:
            """
            type: Optional[CabinType] = field(
                default=None,
                metadata=dict(
                    name="Type",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class PassengerType:
            """
            :ivar code: Specify traveler type code.
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True,
                    min_length=1.0,
                    max_length=8.0
                )
            )

        @dataclass
        class NegotiatedFaresOnly:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class Xofares:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class CorporateId:
            """
            :ivar code:
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True,
                    pattern=r"[A-Za-z]{3}[0-9]{2}"
                )
            )

        @dataclass
        class AccountCode:
            """
            :ivar code:
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True,
                    min_length=1.0,
                    max_length=20.0
                )
            )


@dataclass
class FlightTypePrefType:
    """Indicates preferences for certain types of flights, such as connections or
    stopovers, when used for a specific travel situation.

    :ivar prefer_level:
    :ivar flight_type:
    :ivar max_connections: Indicates that if connection is chosen, then this attribute defines the maximum number of connections preferred.
    """
    prefer_level: PreferLevelType = field(
        default="Preferred",
        metadata=dict(
            name="PreferLevel",
            type="Attribute"
        )
    )
    flight_type: Optional[FlightTypeType] = field(
        default=None,
        metadata=dict(
            name="FlightType",
            type="Attribute"
        )
    )
    max_connections: Optional[Union[int, bool]] = field(
        default=None,
        metadata=dict(
            name="MaxConnections",
            type="Attribute"
        )
    )


@dataclass
class InterlineBrandsType:
    """
    :ivar brand: Brand list to be returned
    :ivar change_brand_for_soldout: If specific XX brand is not available for requested date/flight, another cheapest brand will be returned combined with available XX brand.
    """
    brand: List[BrandType] = field(
        default_factory=list,
        metadata=dict(
            name="Brand",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    change_brand_for_soldout: bool = field(
        default=False,
        metadata=dict(
            name="ChangeBrandForSoldout",
            type="Attribute"
        )
    )


@dataclass
class OriginDestinationFlightType:
    """
    :ivar origin_location: Flight origin code
    :ivar destination_location: Flight destination code
    :ivar airline: Airline information
    :ivar side_trip: Side trip information
    :ivar reservation: Reservation information
    :ivar mileage_display: Mileage information
    :ivar booking_date_time: Booking date and time
    :ivar fare:
    :ivar plus_up:
    :ivar number: Flight number
    :ivar departure_date_time: Departure date and time
    :ivar arrival_date_time: Arrival date and time
    :ivar marriage_status: Marriage status
    :ivar type: Flight type (A: Air Segment, K: ARUNK, O: Open Segment)
    :ivar flown: Specify whether the flight is flown.
    :ivar class_of_service: Class of service
    :ivar shopped: Specify whether the flight is shopped.
    """
    origin_location: Optional[RequestLocationType] = field(
        default=None,
        metadata=dict(
            name="OriginLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    destination_location: Optional[RequestLocationType] = field(
        default=None,
        metadata=dict(
            name="DestinationLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    airline: Optional[AirlineType] = field(
        default=None,
        metadata=dict(
            name="Airline",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    side_trip: Optional[SideTripType] = field(
        default=None,
        metadata=dict(
            name="SideTrip",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    reservation: Optional[ReservationType] = field(
        default=None,
        metadata=dict(
            name="Reservation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    mileage_display: List[MileageDisplayType] = field(
        default_factory=list,
        metadata=dict(
            name="MileageDisplay",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    booking_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingDateTime",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?"
        )
    )
    fare: Optional[FareOptionalDetailsType] = field(
        default=None,
        metadata=dict(
            name="Fare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    plus_up: List[PlusUpType] = field(
        default_factory=list,
        metadata=dict(
            name="PlusUp",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True
        )
    )
    departure_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDateTime",
            type="Attribute",
            required=True,
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?"
        )
    )
    arrival_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalDateTime",
            type="Attribute",
            required=True,
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?"
        )
    )
    marriage_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MarriageStatus",
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True,
            pattern=r"[AKO]"
        )
    )
    flown: bool = field(
        default=False,
        metadata=dict(
            name="Flown",
            type="Attribute"
        )
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            pattern=r"[A-Z]{1,2}"
        )
    )
    shopped: bool = field(
        default=False,
        metadata=dict(
            name="Shopped",
            type="Attribute"
        )
    )


@dataclass
class PriceRequestInformationType:
    """Identify pricing source, if negotiated fares are requested and if it is a
    reprice request.

    :ivar negotiated_fare_code:
    :ivar account_code:
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    :ivar fare_qualifier: Fare Type is specific to a specific fare and this is a request for a set of fares based on these qualifiers.
    :ivar negotiated_fares_only: If set to true then returned fares need to match requested AcccountCode/CorpID on all fare components
    :ivar currency_code: Type of funds preferred for reviewing monetary values, in ISO 4217 codes.
    :ivar pricing_source: It can be used to indicate whether the fare is public or private.
    :ivar reprice:
    :ivar process_thru_fares_only: Activates processing of thru fares only.
    :ivar purchase_date: Specify purchase date. Fares returned will be based on the purchase date.
    :ivar purchase_time: Specify purchase time. Fares returned will be based on the purchase time.
    :ivar net_fares_used: Set to true when exchange ticket uses net fare.
    """
    negotiated_fare_code: List["PriceRequestInformationType.NegotiatedFareCode"] = field(
        default_factory=list,
        metadata=dict(
            name="NegotiatedFareCode",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    account_code: List["PriceRequestInformationType.AccountCode"] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tpa_extensions: Optional["PriceRequestInformationType.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    fare_qualifier: Optional[Union[str, bool]] = field(
        default=None,
        metadata=dict(
            name="FareQualifier",
            type="Attribute"
        )
    )
    negotiated_fares_only: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NegotiatedFaresOnly",
            type="Attribute"
        )
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    pricing_source: Optional[RequestPricingSourceType] = field(
        default=None,
        metadata=dict(
            name="PricingSource",
            type="Attribute"
        )
    )
    reprice: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Reprice",
            type="Attribute"
        )
    )
    process_thru_fares_only: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ProcessThruFaresOnly",
            type="Attribute"
        )
    )
    purchase_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PurchaseDate",
            type="Attribute"
        )
    )
    purchase_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PurchaseTime",
            type="Attribute"
        )
    )
    net_fares_used: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NetFaresUsed",
            type="Attribute"
        )
    )

    @dataclass
    class TpaExtensions:
        """
        :ivar public_fare: This element finds only public fares.
        :ivar private_fare: This element finds only private fares.
        :ivar iatafare: This element finds only IATA fares.
        :ivar web_fare:
        :ivar priority: This element governs how flights are returned. A user can uses a priority of 1-4 to make this determination.
        :ivar indicators: This element restricts fares which can be returned in response. If a customer passes this element, all its children should be specified.
        :ivar promo_id: Promotional Identifier - a string which identifies a promotion, possibly giving a discount prices etc.
        :ivar customer_type:
        :ivar multiple_traveler_groups: This element governs how flights are returned when multiple passenger groups are requested.
        :ivar branded_fare_indicators:
        :ivar passenger_status:
        :ivar point_of_sale_override: Will return the fares available for specified point of sale and priced in this point of sale currency. Currency is overriden by PriceRequestInformation@CurrencyCode.
        :ivar point_of_ticketing_override:
        :ivar apply_resident_discount: Apply resident discount in CLFE
        :ivar eticketable_override:
        :ivar currency:
        :ivar use_reduced_constructions: Use reduced constructions (simple fare paths with restrictions on the number of fare components).
        :ivar obfees:
        :ivar fare_breaks_at_legs: Force fare breaks at leg points if split taxes by leg requested. By default set to true.
        :ivar fare_adjustment: Capability to specify Plus-Up and Discount Amount and Percentage.
        """
        public_fare: Optional["PriceRequestInformationType.TpaExtensions.PublicFare"] = field(
            default=None,
            metadata=dict(
                name="PublicFare",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        private_fare: Optional["PriceRequestInformationType.TpaExtensions.PrivateFare"] = field(
            default=None,
            metadata=dict(
                name="PrivateFare",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        iatafare: Optional["PriceRequestInformationType.TpaExtensions.Iatafare"] = field(
            default=None,
            metadata=dict(
                name="IATAFare",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        web_fare: Optional["PriceRequestInformationType.TpaExtensions.WebFare"] = field(
            default=None,
            metadata=dict(
                name="WebFare",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        priority: Optional["PriceRequestInformationType.TpaExtensions.Priority"] = field(
            default=None,
            metadata=dict(
                name="Priority",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        indicators: Optional["PriceRequestInformationType.TpaExtensions.Indicators"] = field(
            default=None,
            metadata=dict(
                name="Indicators",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        promo_id: Optional[str] = field(
            default=None,
            metadata=dict(
                name="PromoID",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        customer_type: Optional["PriceRequestInformationType.TpaExtensions.CustomerType"] = field(
            default=None,
            metadata=dict(
                name="CustomerType",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        multiple_traveler_groups: Optional["PriceRequestInformationType.TpaExtensions.MultipleTravelerGroups"] = field(
            default=None,
            metadata=dict(
                name="MultipleTravelerGroups",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        branded_fare_indicators: Optional["PriceRequestInformationType.TpaExtensions.BrandedFareIndicators"] = field(
            default=None,
            metadata=dict(
                name="BrandedFareIndicators",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        passenger_status: Optional["PriceRequestInformationType.TpaExtensions.PassengerStatus"] = field(
            default=None,
            metadata=dict(
                name="PassengerStatus",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        point_of_sale_override: Optional[PointOfSaleOverrideType] = field(
            default=None,
            metadata=dict(
                name="PointOfSaleOverride",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        point_of_ticketing_override: Optional[PointOfTicketingOverrideType] = field(
            default=None,
            metadata=dict(
                name="PointOfTicketingOverride",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        apply_resident_discount: Optional[ApplyResidentDiscountType] = field(
            default=None,
            metadata=dict(
                name="ApplyResidentDiscount",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        eticketable_override: Optional["PriceRequestInformationType.TpaExtensions.EticketableOverride"] = field(
            default=None,
            metadata=dict(
                name="ETicketableOverride",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        currency: Optional["PriceRequestInformationType.TpaExtensions.Currency"] = field(
            default=None,
            metadata=dict(
                name="Currency",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        use_reduced_constructions: Optional["PriceRequestInformationType.TpaExtensions.UseReducedConstructions"] = field(
            default=None,
            metadata=dict(
                name="UseReducedConstructions",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        obfees: Optional["PriceRequestInformationType.TpaExtensions.Obfees"] = field(
            default=None,
            metadata=dict(
                name="OBFees",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        fare_breaks_at_legs: Optional["PriceRequestInformationType.TpaExtensions.FareBreaksAtLegs"] = field(
            default=None,
            metadata=dict(
                name="FareBreaksAtLegs",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        fare_adjustment: Optional["PriceRequestInformationType.TpaExtensions.FareAdjustment"] = field(
            default=None,
            metadata=dict(
                name="FareAdjustment",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

        @dataclass
        class PublicFare:
            """
            :ivar ind:
            """
            ind: bool = field(
                default=False,
                metadata=dict(
                    name="Ind",
                    type="Attribute"
                )
            )

        @dataclass
        class PrivateFare:
            """
            :ivar ind:
            """
            ind: bool = field(
                default=False,
                metadata=dict(
                    name="Ind",
                    type="Attribute"
                )
            )

        @dataclass
        class Iatafare:
            """
            :ivar ind:
            """
            ind: bool = field(
                default=False,
                metadata=dict(
                    name="Ind",
                    type="Attribute"
                )
            )

        @dataclass
        class WebFare:
            """
            :ivar ind: Web fare
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute"
                )
            )

        @dataclass
        class Priority:
            """
            :ivar price:
            :ivar direct_flights:
            :ivar time:
            :ivar vendor:
            """
            price: Optional["PriceRequestInformationType.TpaExtensions.Priority.Price"] = field(
                default=None,
                metadata=dict(
                    name="Price",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    required=True
                )
            )
            direct_flights: Optional["PriceRequestInformationType.TpaExtensions.Priority.DirectFlights"] = field(
                default=None,
                metadata=dict(
                    name="DirectFlights",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    required=True
                )
            )
            time: Optional["PriceRequestInformationType.TpaExtensions.Priority.Time"] = field(
                default=None,
                metadata=dict(
                    name="Time",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    required=True
                )
            )
            vendor: Optional["PriceRequestInformationType.TpaExtensions.Priority.Vendor"] = field(
                default=None,
                metadata=dict(
                    name="Vendor",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    required=True
                )
            )

            @dataclass
            class Price:
                """
                :ivar priority:
                """
                priority: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Priority",
                        type="Attribute",
                        required=True,
                        min_inclusive=1.0,
                        max_inclusive=4.0
                    )
                )

            @dataclass
            class DirectFlights:
                """
                :ivar priority:
                """
                priority: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Priority",
                        type="Attribute",
                        required=True,
                        min_inclusive=1.0,
                        max_inclusive=4.0
                    )
                )

            @dataclass
            class Time:
                """
                :ivar priority:
                """
                priority: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Priority",
                        type="Attribute",
                        required=True,
                        min_inclusive=1.0,
                        max_inclusive=4.0
                    )
                )

            @dataclass
            class Vendor:
                """
                :ivar priority:
                """
                priority: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Priority",
                        type="Attribute",
                        required=True,
                        min_inclusive=1.0,
                        max_inclusive=4.0
                    )
                )

        @dataclass
        class Indicators:
            """
            :ivar retain_fare: Currently must be set to true.
            :ivar min_max_stay: If set to true, fares that have a min/max stay can be included in the responses. If set to false, then no fares that include a min/max stay requirement will be included in the response.
            :ivar refund_penalty: If set to true, fares that have a refund penalty can be included in the responses. If set to false, then no fares that include a refund penalty requirement will be included in the response.
            :ivar res_ticketing: If set to true, fares that have a reservation/ticketing can be included in the responses. If set to false, then no fares that include reservation/ticketing requirement will be included in the response.
            :ivar travel_policy: This element is currently ignored whether it is true or false.
            """
            retain_fare: Optional["PriceRequestInformationType.TpaExtensions.Indicators.RetainFare"] = field(
                default=None,
                metadata=dict(
                    name="RetainFare",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            min_max_stay: Optional["PriceRequestInformationType.TpaExtensions.Indicators.MinMaxStay"] = field(
                default=None,
                metadata=dict(
                    name="MinMaxStay",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            refund_penalty: Optional["PriceRequestInformationType.TpaExtensions.Indicators.RefundPenalty"] = field(
                default=None,
                metadata=dict(
                    name="RefundPenalty",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            res_ticketing: Optional["PriceRequestInformationType.TpaExtensions.Indicators.ResTicketing"] = field(
                default=None,
                metadata=dict(
                    name="ResTicketing",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            travel_policy: Optional["PriceRequestInformationType.TpaExtensions.Indicators.TravelPolicy"] = field(
                default=None,
                metadata=dict(
                    name="TravelPolicy",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )

            @dataclass
            class RetainFare:
                """
                :ivar ind:
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Ind",
                        type="Attribute",
                        required=True
                    )
                )

            @dataclass
            class MinMaxStay:
                """
                :ivar ind:
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Ind",
                        type="Attribute",
                        required=True
                    )
                )

            @dataclass
            class RefundPenalty:
                """
                :ivar ind:
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Ind",
                        type="Attribute",
                        required=True
                    )
                )

            @dataclass
            class ResTicketing:
                """
                :ivar ind:
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Ind",
                        type="Attribute",
                        required=True
                    )
                )

            @dataclass
            class TravelPolicy:
                """
                :ivar ind:
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Ind",
                        type="Attribute",
                        required=True
                    )
                )

        @dataclass
        class CustomerType:
            """
            :ivar value:
            """
            value: Optional["PriceRequestInformationType.TpaExtensions.CustomerType.Value"] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

            class Value(Enum):
                """
                :cvar LOYALTY: LOYALTY customer type.
                :cvar PREFELITE: PREFERED_ELITE customer type.
                :cvar REGULAR: Regular customer type.
                :cvar TVLYPREF: TVLY_PREFERRED customer type.
                """
                LOYALTY = "LOYALTY"
                PREFELITE = "PREFELITE"
                REGULAR = "REGULAR"
                TVLYPREF = "TVLYPREF"

        @dataclass
        class MultipleTravelerGroups:
            """
            :ivar itineraries_per_group: Indicates desired number of itineraries to be returned in each passenger group at beggining of response.
            """
            itineraries_per_group: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="ItinerariesPerGroup",
                    type="Attribute",
                    min_inclusive=1.0,
                    max_inclusive=99.0
                )
            )

        @dataclass
        class BrandedFareIndicators:
            """
            :ivar return_cheapest_unbranded_fare:
            :ivar single_branded_fare: Return single brand option per itin
            :ivar multiple_branded_fares: Return multiple brand options per itin
            """
            return_cheapest_unbranded_fare: Optional["PriceRequestInformationType.TpaExtensions.BrandedFareIndicators.ReturnCheapestUnbrandedFare"] = field(
                default=None,
                metadata=dict(
                    name="ReturnCheapestUnbrandedFare",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            single_branded_fare: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="SingleBrandedFare",
                    type="Attribute"
                )
            )
            multiple_branded_fares: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="MultipleBrandedFares",
                    type="Attribute"
                )
            )

            @dataclass
            class ReturnCheapestUnbrandedFare:
                """
                :ivar ind: Indicator to turn on or off return of cheapest unbranded fare referred as "catch all" fare for the branded carriers from the branded fares service.
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Ind",
                        type="Attribute",
                        required=True
                    )
                )

        @dataclass
        class PassengerStatus:
            """
            :ivar state_code:
            :ivar country_code:
            :ivar city_code:
            :ivar type:
            """
            state_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="StateCode",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_length=2.0,
                    max_length=8.0
                )
            )
            country_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="CountryCode",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    required=True,
                    pattern=r"[a-zA-Z]{2}"
                )
            )
            city_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="CityCode",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    pattern=r"[a-zA-Z]{3}"
                )
            )
            type: Optional["PriceRequestInformationType.TpaExtensions.PassengerStatus.Type"] = field(
                default=None,
                metadata=dict(
                    name="Type",
                    type="Attribute",
                    required=True
                )
            )

            class Type(Enum):
                """
                :cvar E: Employment.
                :cvar N: Nationality.
                :cvar R: Residency.
                """
                E = "E"
                N = "N"
                R = "R"

        @dataclass
        class EticketableOverride:
            """
            :ivar value: ETicketable override
            """
            value: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute"
                )
            )

        @dataclass
        class Currency:
            """
            :ivar dual: Dual currency
            :ivar moverride: M override
            """
            dual: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Dual",
                    type="Attribute",
                    pattern=r"[a-zA-Z]{3}"
                )
            )
            moverride: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="MOverride",
                    type="Attribute"
                )
            )

        @dataclass
        class UseReducedConstructions:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute"
                )
            )

        @dataclass
        class Obfees:
            """
            :ivar rtype: Indicator Returning R-Type OB Fees
            :ivar ttype: Indicator Returning T-Type OB Fees
            """
            rtype: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="RType",
                    type="Attribute"
                )
            )
            ttype: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="TType",
                    type="Attribute"
                )
            )

        @dataclass
        class FareBreaksAtLegs:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute"
                )
            )

        @dataclass
        class FareAdjustment:
            """
            :ivar value: Adjustment Value, can be positive or negative, number or percentage
            :ivar currency: Currency of Adjustment's Value
            """
            value: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True,
                    pattern=r"(\+|-)?([0-9]+(\.[0-9]*)?|\.[0-9]+)%?"
                )
            )
            currency: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Currency",
                    type="Attribute",
                    pattern=r"[a-zA-Z]{3}"
                )
            )

    @dataclass
    class NegotiatedFareCode:
        """
        :ivar content:
        :ivar supplier: This element indicates the supplier associated with a negotiated fare code.
        :ivar tpa_extensions: This is a place holder for additional elements.
        :ivar code: Any code used to specify an item, for example, type of traveler, service code, room amenity, etc.
        :ivar code_context: Identifies the source authority for the code.
        :ivar uri: Identifies the location of the code table
        :ivar quantity: Used to define a quantity of an associated element or attribute.
        :ivar secondary_code: An additional attribute to allow flexibility for particular organizations who require an additional code.
        :ivar supplier_code: An additional attribute to allow flexibility for particular organizations who require an additional supplier code.
        """
        content: Optional[object] = field(
            default=None,
            metadata=dict(
                type="Wildcard",
                namespace="##any"
            )
        )
        supplier: List[CompanyNameType] = field(
            default_factory=list,
            metadata=dict(
                name="Supplier",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        tpa_extensions: Optional[str] = field(
            default=None,
            metadata=dict(
                name="TPA_Extensions",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Code",
                type="Attribute",
                pattern=r"[A-Za-z]{3}[0-9]{2}"
            )
        )
        code_context: Optional[str] = field(
            default=None,
            metadata=dict(
                name="CodeContext",
                type="Attribute",
                min_length=1.0,
                max_length=32.0
            )
        )
        uri: Optional[str] = field(
            default=None,
            metadata=dict(
                name="URI",
                type="Attribute"
            )
        )
        quantity: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Quantity",
                type="Attribute",
                min_inclusive=1.0,
                max_inclusive=999.0
            )
        )
        secondary_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SecondaryCode",
                type="Attribute",
                min_length=1.0,
                max_length=16.0
            )
        )
        supplier_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SupplierCode",
                type="Attribute",
                min_length=1.0,
                max_length=16.0
            )
        )

    @dataclass
    class AccountCode:
        """
        :ivar code:
        """
        code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Code",
                type="Attribute",
                required=True,
                min_length=1.0,
                max_length=20.0
            )
        )


@dataclass
class RoutingDefinitionType:
    """Definition of a routing.

    :ivar routing_leg:
    :ivar add_wildcards: If true, wildcards will be automatically inserted between each two leg (RoutingLeg) elements. Will be set to 'false' if not present.
    """
    routing_leg: List[RoutingLegType] = field(
        default_factory=list,
        metadata=dict(
            name="RoutingLeg",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    add_wildcards: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AddWildcards",
            type="Attribute"
        )
    )


@dataclass
class SourceBookingChannelType(BookingChannelType):
    """Specifies the booking channel type and whether it is the primary means of
    connectivity of the source.

    :ivar company_name: Identifies the company that is associated with the booking channel.
    """
    company_name: Optional[CompanyNameType] = field(
        default=None,
        metadata=dict(
            name="CompanyName",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )


@dataclass
class TaxCodeAmountType(TaxCodeType):
    """Defines the data fields available for tax code and amount.

    :ivar amount:
    """
    amount: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            fraction_digits=3
        )
    )


@dataclass
class TicketDistribPrefType:
    """Type of ticket distribution to be used with this collection of preferences.

    :ivar value:
    :ivar prefer_level:
    :ivar distrib_type: Ticket distribution method; such as Fax, Email, Courier, Mail, Airport_Pickup, City_Office, Hotel_Desk, WillCall, etc.
    :ivar ticket_time: Ticket turnaround time desired, amount of time requested to deliver tickets.
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=0.0,
            max_length=64.0
        )
    )
    prefer_level: PreferLevelType = field(
        default="Preferred",
        metadata=dict(
            name="PreferLevel",
            type="Attribute"
        )
    )
    distrib_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DistribType",
            type="Attribute"
        )
    )
    ticket_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketTime",
            type="Attribute"
        )
    )


@dataclass
class UniqueIdType:
    """An identifier used to uniquely reference an object in a system (e.g. an
    airline reservation reference, customer profile reference, booking confirmation
    number, or a reference to a previous availability quote).

    :ivar company_name: Identifies the company that is associated with the UniqueID.
    :ivar url: URL that identifies the location associated with the record identified by the UniqueID.
    :ivar type: A reference to the type of object defined by the UniqueID element. Refer to OTA Code List Unique ID Type (UIT).
    :ivar instance: The identification of a record as it exists at a point in time. An instance is used in update messages where the sender must assure the server that the update sent refers to the most recent modification level of the object being updated.
    :ivar id: A unique identifying value assigned by the creating system. The ID attribute may be used to reference a primary-key value within a database or in a particular implementation.
    :ivar id_context: Used to identify the source of the identifier (e.g. IATA, ABTA, etc.).
    """
    class Meta:
        name = "UniqueID_Type"

    company_name: Optional[CompanyNameType] = field(
        default=None,
        metadata=dict(
            name="CompanyName",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    url: Optional[str] = field(
        default=None,
        metadata=dict(
            name="URL",
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    instance: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Instance",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=32.0
        )
    )
    id_context: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID_Context",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )


@dataclass
class ValidatingCarrierType:
    """
    :ivar preference:
    :ivar code: Validating Carrier code
    """
    preference: List["ValidatingCarrierType.Preference"] = field(
        default_factory=list,
        metadata=dict(
            name="Preference",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            pattern=r"[0-9A-Z]{2,3}"
        )
    )

    @dataclass
    class Preference:
        """
        :ivar code:
        :ivar level:
        """
        code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Code",
                type="Attribute",
                required=True,
                pattern=r"[0-9A-Z]{2,3}"
            )
        )
        level: Optional[ValidatingCarrierPreferLevelType] = field(
            default=None,
            metadata=dict(
                name="Level",
                type="Attribute",
                required=True
            )
        )


@dataclass
class AirSearchPrefsType:
    """Defines user preferences to be used in conducting a search.

    :ivar vendor_pref: Specify vendors to include and exclude from the response.
    :ivar flight_type_pref: Defines preferred flight characteristics to be used in a search.
    :ivar fare_restrict_pref: Constrains a fare search to those with restrictions that satisfy user-imposed limitations.
    :ivar equip_pref: Defines preferred equipment profile(s) to be used in a search.
    :ivar cabin_pref: Defines preferred cabin(s) to be used in a search. The Cabin type specified in a OriginDestinationInformation/TPA_Extensions overrides this Cabin type for that specific segment/leg. If a Cabin type is not specified in a OriginDestinationInformation/TPA_Extensions the cabin type in this element will be used as default cabin type for that segment/leg.
    :ivar ticket_distrib_pref: Defines Distribution prefernces.
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    :ivar ancillary_fees:
    :ivar frequent_flyer: Frequent Flyer Status Information
    :ivar spanish_family_discount:
    :ivar interline_brands:
    :ivar smoking_allowed:
    :ivar on_time_rate: Request for flights in response that meet the given Department of Transport on-time rate. This is a number between 0 and 100.
    :ivar eticket_desired: Request flights that are e-ticketable in the response.
    :ivar valid_interline_ticket: Request options that are validated on base of interline ticketing aggrement.
    :ivar max_stops_quantity: Request flights that have no more than the requested number of stops.
    :ivar use_all_flights: Each flight should appear at least once.
    :ivar all_flights_data: Return flights not combinable into roundtrips as one ways is a separate section.
    :ivar hybrid: If false no solutions priced outside of ATSE systems will be returned in response for carriers operating in hybrid content distribution model.
    """
    vendor_pref: List[CompanyNamePrefType] = field(
        default_factory=list,
        metadata=dict(
            name="VendorPref",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    flight_type_pref: Optional[FlightTypePrefType] = field(
        default=None,
        metadata=dict(
            name="FlightTypePref",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    fare_restrict_pref: List["AirSearchPrefsType.FareRestrictPref"] = field(
        default_factory=list,
        metadata=dict(
            name="FareRestrictPref",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=4
        )
    )
    equip_pref: List[EquipmentTypePref] = field(
        default_factory=list,
        metadata=dict(
            name="EquipPref",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9
        )
    )
    cabin_pref: List[CabinPrefType] = field(
        default_factory=list,
        metadata=dict(
            name="CabinPref",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=3
        )
    )
    ticket_distrib_pref: List[TicketDistribPrefType] = field(
        default_factory=list,
        metadata=dict(
            name="TicketDistribPref",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=3
        )
    )
    tpa_extensions: Optional["AirSearchPrefsType.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    ancillary_fees: Optional["AirSearchPrefsType.AncillaryFees"] = field(
        default=None,
        metadata=dict(
            name="AncillaryFees",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    frequent_flyer: List["AirSearchPrefsType.FrequentFlyer"] = field(
        default_factory=list,
        metadata=dict(
            name="FrequentFlyer",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    spanish_family_discount: Optional["AirSearchPrefsType.SpanishFamilyDiscount"] = field(
        default=None,
        metadata=dict(
            name="SpanishFamilyDiscount",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    interline_brands: Optional[InterlineBrandsType] = field(
        default=None,
        metadata=dict(
            name="InterlineBrands",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    smoking_allowed: bool = field(
        default=False,
        metadata=dict(
            name="SmokingAllowed",
            type="Attribute"
        )
    )
    on_time_rate: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="OnTimeRate",
            type="Attribute",
            min_inclusive=0.01,
            max_inclusive=100.0
        )
    )
    eticket_desired: bool = field(
        default=False,
        metadata=dict(
            name="ETicketDesired",
            type="Attribute"
        )
    )
    valid_interline_ticket: bool = field(
        default=False,
        metadata=dict(
            name="ValidInterlineTicket",
            type="Attribute"
        )
    )
    max_stops_quantity: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MaxStopsQuantity",
            type="Attribute",
            min_inclusive=0.0,
            max_inclusive=999.0
        )
    )
    use_all_flights: bool = field(
        default=False,
        metadata=dict(
            name="UseAllFlights",
            type="Attribute"
        )
    )
    all_flights_data: bool = field(
        default=False,
        metadata=dict(
            name="AllFlightsData",
            type="Attribute"
        )
    )
    hybrid: bool = field(
        default=True,
        metadata=dict(
            name="Hybrid",
            type="Attribute"
        )
    )

    @dataclass
    class FareRestrictPref(FareRestrictPrefType):
        """
        :ivar adv_res_ticketing: Identifies whether advance reservation or ticketing restrictions are acceptable in the search results.
        :ivar stay_restrictions: Identifies whether restrictions on minimum or maximum stays should be included in the search results.
        :ivar voluntary_changes: Identifies whether penalties associated with voluntary changes should be included in the search results.
        """
        adv_res_ticketing: Optional[AdvResTicketingType] = field(
            default=None,
            metadata=dict(
                name="AdvResTicketing",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        stay_restrictions: Optional[StayRestrictionsType] = field(
            default=None,
            metadata=dict(
                name="StayRestrictions",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        voluntary_changes: Optional[VoluntaryChangesType] = field(
            default=None,
            metadata=dict(
                name="VoluntaryChanges",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

    @dataclass
    class TpaExtensions:
        """
        :ivar departure_window: This should be of the form HHMMHHMM.
        :ivar arrival_window: This should be of the form HHMMHHMM.
        :ivar exclude_vendor_pref: This element allows a user to exclude certain carriers from the search.
        :ivar include_alliance_pref: Consider only these alliances.
        :ivar exclude_alliance_pref: Do not consider these alliances.
        :ivar num_trips:
        :ivar alt_cities_combinations:
        :ivar num_trips_with_routing: This element allows a user to specify the number of itineraries with special routing returned.
        :ivar online_indicator:
        :ivar interline_indicator:
        :ivar trip_type: Specify air trip type.
        :ivar max_price: Maximum price returned from LFE service.
        :ivar content_type: Restrict content type returned by LFE service.
        :ivar domestic_layover_time: Domestic maximum connecting hours.
        :ivar long_connect_time: Change minimum and maximum connect time per connection in long connection schedules if Long Connect Time logic is enabled. Specified values should be less than 1440 minutes (24 hours).
        :ivar long_connect_points: Minimum and maximum number of connection points (not necessarily long) for Long Connections.
        :ivar air_service_only: Return air service only.
        :ivar jet_service_only: Return jet service only.
        :ivar same_connection_airport_only: Same airport at connection point restriction
        :ivar same_origin_airport_only: Same airport at origin point restriction
        :ivar same_turnaround_airport_only: Same airport at turnaround point restriction
        :ivar aircraft_type_penalty: Aircraft type penalty (in dollars). Used to penalize propeller aircraft type in the response.
        :ivar alternate_airport_penalty: Alternate airport penalty (in dollars). Used to penalize options with alternate airports.
        :ivar fare_amount_threshold: % ESV value above the lowest itinerary
        :ivar num_of_low_fare_sol: Number of low fare solutions for ESV2
        :ivar num_of_must_price_onl_sol: Number of must price online solutions for ESV2
        :ivar num_of_must_price_inrl_sol: Number of must price interline solutions for ESV2
        :ivar num_of_must_price_nstp_onl_sol: Number of must price non-stop online solutions for ESV2
        :ivar num_of_must_price_nstp_inrl_sol: Number of must price non-stop interline solutions for ESV2
        :ivar num_of_must_price_sstop_onl_sol: Number of must price single stop online solutions for ESV2
        :ivar stp_penalty_in_usd: Stop penalty in dollars for ESV2
        :ivar dur_penalty_in_usd: Duration penalty in dollars for ESV2
        :ivar dep_penalty_in_usd: Departure penalty in dollars for ESV2
        :ivar max_allowed_must_price_overage_per_crr: Max allowed must price overage per carrier for ESV2
        :ivar flt_opt_must_price_reuse_limit: Flight option reuse limit (must price) for ESV2
        :ivar upper_bound_must_price_factor_for_not_non_stp: Upper bound factor for not non-stops (must price) for ESV2
        :ivar upper_bound_lfsfactor: Low fare search upper bound factor for ESV2
        :ivar num_of_must_price_nstp1_stp_onl_sol: Number of must price non-stop/one-stop online solutions for ESV2
        :ivar num_of_must_price_nstp1_stp_inrl_sol: Number of must price non-stop/one-stop interline solutions for ESV2
        :ivar upper_bound_must_price_factor_for_non_stp: Upper bound factor for non-stops (must price) for ESV2
        :ivar max_allowed_lfsoverage_per_crr_percent: Low fare search max allowed overage per carrier % for ESV2
        :ivar target_min_num_of_lfsonl_sol_per_crr: Low fare search target minimum number of online solutions per carrier for ESV2
        :ivar target_min_num_of_lfstot_onl_sol_percent: Low fare search target minimum number of total online solutions % for ESV2
        :ivar flt_opt_lfsreuse_limit_for_non_avs: Low fare search flight option reuse limit for non AVS for ESV2
        :ivar flt_opt_lfsreuse_limit_for_avs: Low fare search flight option reuse limit for AVS for ESV2
        :ivar avs_penalty_crrs: AVS penalty carrier list (| delimited) for ESV2
        :ivar max_num_of_non_stp_onl_sol: Max number of nonstop online solutions for ESV2
        :ivar max_num_of_non_stp_inrl_sol: Max number of nonstop interline solutions for ESV2
        :ivar max_num_of_single_stp_onl_sol: Max number of single stop online solutions for ESV2
        :ivar max_num_of2_plus_stp_sol: Max number of 2+ stops solutions for ESV2
        :ivar min_allowed_overage_per_crr_percent: Min allowed overage per carrier % for ESV2
        :ivar min_allowed_overage_per_crr: Min allowed overage per carrier for ESV2
        :ivar max_rel_fare_lvl_ofx_for_non_stp: Max relative fare level of x for nonstops for ESV2
        :ivar max_rel_fare_lvl_ofx_for_cnx: Max relative fare level of x for carrier for ESV2
        :ivar num_of_must_price2_plus_stp_sol: Number of must price 2+ stops solutions for ESV2
        :ivar itinerary_number_threshold: Number of preffered/good itins to price
        :ivar xofares:
        :ivar exempt_all_taxes: Exempt all taxes (/TE)
        :ivar exempt_all_taxes_and_fees: Exempt all taxes and fees (/TN)
        :ivar taxes: Specify Taxes (/TX)
        :ivar exempt_tax: Exempt Tax (/TE)
        :ivar flight_stops_as_connections:
        :ivar ticketing_sum_of_locals: Settings specific to Ticketing Sum of Locals processing
        :ivar multi_airport_codes: Settings specific to Multi Airport Codes processing
        :ivar jump_cabin_logic:
        :ivar keep_same_cabin:
        :ivar governing_carrier_override:
        :ivar exclude_call_direct_carriers:
        :ivar validating_carrier:
        :ivar validating_carrier_check:
        :ivar settlement_method:
        :ivar flight_repeat_limit:
        :ivar flexible_fares:
        :ivar diversity_parameters:
        :ivar additional_fare_limit:
        :ivar fare_focus_rules:
        :ivar selling_levels:
        :ivar budget: Budget Shopping settings
        :ivar options_per_date_pair_list: List of dates/date pairs with different requested number of options
        :ivar country_pref: List of countries to be excluded from processing
        :ivar retailer_rules:
        """
        departure_window: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DepartureWindow",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                pattern=r"([0-2][0-9][0-5][0-9]){2}"
            )
        )
        arrival_window: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ArrivalWindow",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                pattern=r"([0-2][0-9][0-5][0-9]){2}"
            )
        )
        exclude_vendor_pref: List["AirSearchPrefsType.TpaExtensions.ExcludeVendorPref"] = field(
            default_factory=list,
            metadata=dict(
                name="ExcludeVendorPref",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        include_alliance_pref: List[AllianceType] = field(
            default_factory=list,
            metadata=dict(
                name="IncludeAlliancePref",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        exclude_alliance_pref: List[AllianceType] = field(
            default_factory=list,
            metadata=dict(
                name="ExcludeAlliancePref",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        num_trips: Optional[NumTripsType] = field(
            default=None,
            metadata=dict(
                name="NumTrips",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        alt_cities_combinations: Optional[AltCitiesCombinationsType] = field(
            default=None,
            metadata=dict(
                name="AltCitiesCombinations",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        num_trips_with_routing: Optional["AirSearchPrefsType.TpaExtensions.NumTripsWithRouting"] = field(
            default=None,
            metadata=dict(
                name="NumTripsWithRouting",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        online_indicator: Optional["AirSearchPrefsType.TpaExtensions.OnlineIndicator"] = field(
            default=None,
            metadata=dict(
                name="OnlineIndicator",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        interline_indicator: Optional["AirSearchPrefsType.TpaExtensions.InterlineIndicator"] = field(
            default=None,
            metadata=dict(
                name="InterlineIndicator",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        trip_type: Optional["AirSearchPrefsType.TpaExtensions.TripType"] = field(
            default=None,
            metadata=dict(
                name="TripType",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        max_price: Optional["AirSearchPrefsType.TpaExtensions.MaxPrice"] = field(
            default=None,
            metadata=dict(
                name="MaxPrice",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        content_type: Optional["AirSearchPrefsType.TpaExtensions.ContentType"] = field(
            default=None,
            metadata=dict(
                name="ContentType",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        domestic_layover_time: Optional["AirSearchPrefsType.TpaExtensions.DomesticLayoverTime"] = field(
            default=None,
            metadata=dict(
                name="DomesticLayoverTime",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        long_connect_time: Optional["AirSearchPrefsType.TpaExtensions.LongConnectTime"] = field(
            default=None,
            metadata=dict(
                name="LongConnectTime",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        long_connect_points: Optional["AirSearchPrefsType.TpaExtensions.LongConnectPoints"] = field(
            default=None,
            metadata=dict(
                name="LongConnectPoints",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        air_service_only: Optional["AirSearchPrefsType.TpaExtensions.AirServiceOnly"] = field(
            default=None,
            metadata=dict(
                name="AirServiceOnly",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        jet_service_only: Optional["AirSearchPrefsType.TpaExtensions.JetServiceOnly"] = field(
            default=None,
            metadata=dict(
                name="JetServiceOnly",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        same_connection_airport_only: Optional["AirSearchPrefsType.TpaExtensions.SameConnectionAirportOnly"] = field(
            default=None,
            metadata=dict(
                name="SameConnectionAirportOnly",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        same_origin_airport_only: Optional["AirSearchPrefsType.TpaExtensions.SameOriginAirportOnly"] = field(
            default=None,
            metadata=dict(
                name="SameOriginAirportOnly",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        same_turnaround_airport_only: Optional["AirSearchPrefsType.TpaExtensions.SameTurnaroundAirportOnly"] = field(
            default=None,
            metadata=dict(
                name="SameTurnaroundAirportOnly",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        aircraft_type_penalty: Optional["AirSearchPrefsType.TpaExtensions.AircraftTypePenalty"] = field(
            default=None,
            metadata=dict(
                name="AircraftTypePenalty",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        alternate_airport_penalty: Optional["AirSearchPrefsType.TpaExtensions.AlternateAirportPenalty"] = field(
            default=None,
            metadata=dict(
                name="AlternateAirportPenalty",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        fare_amount_threshold: Optional["AirSearchPrefsType.TpaExtensions.FareAmountThreshold"] = field(
            default=None,
            metadata=dict(
                name="FareAmountThreshold",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        num_of_low_fare_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfLowFareSol"] = field(
            default=None,
            metadata=dict(
                name="numOfLowFareSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        num_of_must_price_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceOnlSol"] = field(
            default=None,
            metadata=dict(
                name="numOfMustPriceOnlSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        num_of_must_price_inrl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceInrlSol"] = field(
            default=None,
            metadata=dict(
                name="numOfMustPriceInrlSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        num_of_must_price_nstp_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstpOnlSol"] = field(
            default=None,
            metadata=dict(
                name="numOfMustPriceNStpOnlSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        num_of_must_price_nstp_inrl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstpInrlSol"] = field(
            default=None,
            metadata=dict(
                name="numOfMustPriceNStpInrlSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        num_of_must_price_sstop_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceSstopOnlSol"] = field(
            default=None,
            metadata=dict(
                name="numOfMustPriceSStopOnlSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        stp_penalty_in_usd: Optional["AirSearchPrefsType.TpaExtensions.StpPenaltyInUsd"] = field(
            default=None,
            metadata=dict(
                name="stpPenaltyInUSD",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        dur_penalty_in_usd: Optional["AirSearchPrefsType.TpaExtensions.DurPenaltyInUsd"] = field(
            default=None,
            metadata=dict(
                name="durPenaltyInUSD",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        dep_penalty_in_usd: Optional["AirSearchPrefsType.TpaExtensions.DepPenaltyInUsd"] = field(
            default=None,
            metadata=dict(
                name="depPenaltyInUSD",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        max_allowed_must_price_overage_per_crr: Optional["AirSearchPrefsType.TpaExtensions.MaxAllowedMustPriceOveragePerCrr"] = field(
            default=None,
            metadata=dict(
                name="maxAllowedMustPriceOveragePerCrr",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        flt_opt_must_price_reuse_limit: Optional["AirSearchPrefsType.TpaExtensions.FltOptMustPriceReuseLimit"] = field(
            default=None,
            metadata=dict(
                name="fltOptMustPriceReuseLimit",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        upper_bound_must_price_factor_for_not_non_stp: Optional["AirSearchPrefsType.TpaExtensions.UpperBoundMustPriceFactorForNotNonStp"] = field(
            default=None,
            metadata=dict(
                name="upperBoundMustPriceFactorForNotNonStp",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        upper_bound_lfsfactor: Optional["AirSearchPrefsType.TpaExtensions.UpperBoundLfsfactor"] = field(
            default=None,
            metadata=dict(
                name="upperBoundLFSFactor",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        num_of_must_price_nstp1_stp_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstp1StpOnlSol"] = field(
            default=None,
            metadata=dict(
                name="numOfMustPriceNStp1StpOnlSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        num_of_must_price_nstp1_stp_inrl_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstp1StpInrlSol"] = field(
            default=None,
            metadata=dict(
                name="numOfMustPriceNStp1StpInrlSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        upper_bound_must_price_factor_for_non_stp: Optional["AirSearchPrefsType.TpaExtensions.UpperBoundMustPriceFactorForNonStp"] = field(
            default=None,
            metadata=dict(
                name="upperBoundMustPriceFactorForNonStp",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        max_allowed_lfsoverage_per_crr_percent: Optional["AirSearchPrefsType.TpaExtensions.MaxAllowedLfsoveragePerCrrPercent"] = field(
            default=None,
            metadata=dict(
                name="maxAllowedLFSOveragePerCrrPercent",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        target_min_num_of_lfsonl_sol_per_crr: Optional["AirSearchPrefsType.TpaExtensions.TargetMinNumOfLfsonlSolPerCrr"] = field(
            default=None,
            metadata=dict(
                name="targetMinNumOfLFSOnlSolPerCrr",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        target_min_num_of_lfstot_onl_sol_percent: Optional["AirSearchPrefsType.TpaExtensions.TargetMinNumOfLfstotOnlSolPercent"] = field(
            default=None,
            metadata=dict(
                name="targetMinNumOfLFSTotOnlSolPercent",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        flt_opt_lfsreuse_limit_for_non_avs: Optional["AirSearchPrefsType.TpaExtensions.FltOptLfsreuseLimitForNonAvs"] = field(
            default=None,
            metadata=dict(
                name="fltOptLFSReuseLimitForNonAVS",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        flt_opt_lfsreuse_limit_for_avs: Optional["AirSearchPrefsType.TpaExtensions.FltOptLfsreuseLimitForAvs"] = field(
            default=None,
            metadata=dict(
                name="fltOptLFSReuseLimitForAVS",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        avs_penalty_crrs: Optional["AirSearchPrefsType.TpaExtensions.AvsPenaltyCrrs"] = field(
            default=None,
            metadata=dict(
                name="avsPenaltyCrrs",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        max_num_of_non_stp_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.MaxNumOfNonStpOnlSol"] = field(
            default=None,
            metadata=dict(
                name="maxNumOfNonStpOnlSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        max_num_of_non_stp_inrl_sol: Optional["AirSearchPrefsType.TpaExtensions.MaxNumOfNonStpInrlSol"] = field(
            default=None,
            metadata=dict(
                name="maxNumOfNonStpInrlSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        max_num_of_single_stp_onl_sol: Optional["AirSearchPrefsType.TpaExtensions.MaxNumOfSingleStpOnlSol"] = field(
            default=None,
            metadata=dict(
                name="maxNumOfSingleStpOnlSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        max_num_of2_plus_stp_sol: Optional["AirSearchPrefsType.TpaExtensions.MaxNumOf2PlusStpSol"] = field(
            default=None,
            metadata=dict(
                name="maxNumOf2PlusStpSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        min_allowed_overage_per_crr_percent: Optional["AirSearchPrefsType.TpaExtensions.MinAllowedOveragePerCrrPercent"] = field(
            default=None,
            metadata=dict(
                name="minAllowedOveragePerCrrPercent",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        min_allowed_overage_per_crr: Optional["AirSearchPrefsType.TpaExtensions.MinAllowedOveragePerCrr"] = field(
            default=None,
            metadata=dict(
                name="minAllowedOveragePerCrr",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        max_rel_fare_lvl_ofx_for_non_stp: Optional["AirSearchPrefsType.TpaExtensions.MaxRelFareLvlOfxForNonStp"] = field(
            default=None,
            metadata=dict(
                name="maxRelFareLvlOfxForNonStp",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        max_rel_fare_lvl_ofx_for_cnx: Optional["AirSearchPrefsType.TpaExtensions.MaxRelFareLvlOfxForCnx"] = field(
            default=None,
            metadata=dict(
                name="maxRelFareLvlOfxForCnx",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        num_of_must_price2_plus_stp_sol: Optional["AirSearchPrefsType.TpaExtensions.NumOfMustPrice2PlusStpSol"] = field(
            default=None,
            metadata=dict(
                name="numOfMustPrice2PlusStpSol",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        itinerary_number_threshold: Optional["AirSearchPrefsType.TpaExtensions.ItineraryNumberThreshold"] = field(
            default=None,
            metadata=dict(
                name="ItineraryNumberThreshold",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        xofares: Optional[XofaresType] = field(
            default=None,
            metadata=dict(
                name="XOFares",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        exempt_all_taxes: Optional["AirSearchPrefsType.TpaExtensions.ExemptAllTaxes"] = field(
            default=None,
            metadata=dict(
                name="ExemptAllTaxes",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        exempt_all_taxes_and_fees: Optional["AirSearchPrefsType.TpaExtensions.ExemptAllTaxesAndFees"] = field(
            default=None,
            metadata=dict(
                name="ExemptAllTaxesAndFees",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        taxes: Optional["AirSearchPrefsType.TpaExtensions.Taxes"] = field(
            default=None,
            metadata=dict(
                name="Taxes",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        exempt_tax: List[TaxCodeType] = field(
            default_factory=list,
            metadata=dict(
                name="ExemptTax",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        flight_stops_as_connections: Optional[FlightStopsAsConnectionsType] = field(
            default=None,
            metadata=dict(
                name="FlightStopsAsConnections",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        ticketing_sum_of_locals: Optional["AirSearchPrefsType.TpaExtensions.TicketingSumOfLocals"] = field(
            default=None,
            metadata=dict(
                name="TicketingSumOfLocals",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        multi_airport_codes: Optional["AirSearchPrefsType.TpaExtensions.MultiAirportCodes"] = field(
            default=None,
            metadata=dict(
                name="MultiAirportCodes",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        jump_cabin_logic: Optional[JumpCabinLogicType] = field(
            default=None,
            metadata=dict(
                name="JumpCabinLogic",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        keep_same_cabin: Optional[KeepSameCabinType] = field(
            default=None,
            metadata=dict(
                name="KeepSameCabin",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        governing_carrier_override: Optional[GoverningCarrierOverrideType] = field(
            default=None,
            metadata=dict(
                name="GoverningCarrierOverride",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        exclude_call_direct_carriers: Optional["AirSearchPrefsType.TpaExtensions.ExcludeCallDirectCarriers"] = field(
            default=None,
            metadata=dict(
                name="ExcludeCallDirectCarriers",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        validating_carrier: Optional[ValidatingCarrierType] = field(
            default=None,
            metadata=dict(
                name="ValidatingCarrier",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        validating_carrier_check: Optional["AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck"] = field(
            default=None,
            metadata=dict(
                name="ValidatingCarrierCheck",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        settlement_method: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SettlementMethod",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                pattern=r"[a-zA-Z0-9]{3}"
            )
        )
        flight_repeat_limit: Optional["AirSearchPrefsType.TpaExtensions.FlightRepeatLimit"] = field(
            default=None,
            metadata=dict(
                name="FlightRepeatLimit",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        flexible_fares: Optional[FlexibleFaresType] = field(
            default=None,
            metadata=dict(
                name="FlexibleFares",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        diversity_parameters: Optional["AirSearchPrefsType.TpaExtensions.DiversityParameters"] = field(
            default=None,
            metadata=dict(
                name="DiversityParameters",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        additional_fare_limit: Optional["AirSearchPrefsType.TpaExtensions.AdditionalFareLimit"] = field(
            default=None,
            metadata=dict(
                name="AdditionalFareLimit",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        fare_focus_rules: Optional["AirSearchPrefsType.TpaExtensions.FareFocusRules"] = field(
            default=None,
            metadata=dict(
                name="FareFocusRules",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        selling_levels: Optional["AirSearchPrefsType.TpaExtensions.SellingLevels"] = field(
            default=None,
            metadata=dict(
                name="SellingLevels",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        budget: Optional["AirSearchPrefsType.TpaExtensions.Budget"] = field(
            default=None,
            metadata=dict(
                name="Budget",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        options_per_date_pair_list: Optional["AirSearchPrefsType.TpaExtensions.OptionsPerDatePairList"] = field(
            default=None,
            metadata=dict(
                name="OptionsPerDatePairList",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        country_pref: List["AirSearchPrefsType.TpaExtensions.CountryPref"] = field(
            default_factory=list,
            metadata=dict(
                name="CountryPref",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        retailer_rules: Optional[RetailerRulesType] = field(
            default=None,
            metadata=dict(
                name="RetailerRules",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

        @dataclass
        class ExcludeVendorPref:
            """
            :ivar code: Identifies a company by the company code.
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    min_length=1.0,
                    max_length=8.0
                )
            )

        @dataclass
        class NumTripsWithRouting:
            """
            :ivar number:
            """
            number: int = field(
                default=5,
                metadata=dict(
                    name="Number",
                    type="Attribute",
                    min_inclusive=1.0
                )
            )

        @dataclass
        class TripType:
            """
            :ivar value:
            """
            value: Optional[AirTripType] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute"
                )
            )

        @dataclass
        class MaxPrice:
            """
            :ivar value:
            """
            value: Optional[Decimal] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    fraction_digits=3
                )
            )

        @dataclass
        class ContentType:
            """
            :ivar type:
            """
            type: Optional["AirSearchPrefsType.TpaExtensions.ContentType.Type"] = field(
                default=None,
                metadata=dict(
                    name="Type",
                    type="Attribute"
                )
            )

            class Type(Enum):
                """
                :cvar AIR:
                :cvar RAIL:
                """
                AIR = "Air"
                RAIL = "Rail"

        @dataclass
        class DomesticLayoverTime:
            """
            :ivar hours:
            """
            hours: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Hours",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class LongConnectTime:
            """
            :ivar min:
            :ivar max:
            :ivar enable:
            """
            min: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Min",
                    type="Attribute"
                )
            )
            max: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Max",
                    type="Attribute"
                )
            )
            enable: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Enable",
                    type="Attribute"
                )
            )

        @dataclass
        class LongConnectPoints:
            """
            :ivar min:
            :ivar max:
            """
            min: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Min",
                    type="Attribute"
                )
            )
            max: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Max",
                    type="Attribute"
                )
            )

        @dataclass
        class AirServiceOnly:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class JetServiceOnly:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class SameConnectionAirportOnly:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class SameOriginAirportOnly:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class SameTurnaroundAirportOnly:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class AircraftTypePenalty:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class AlternateAirportPenalty:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class FareAmountThreshold:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class NumOfLowFareSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class NumOfMustPriceOnlSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class NumOfMustPriceInrlSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class NumOfMustPriceNstpOnlSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class NumOfMustPriceNstpInrlSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class NumOfMustPriceSstopOnlSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class StpPenaltyInUsd:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class DurPenaltyInUsd:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class DepPenaltyInUsd:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MaxAllowedMustPriceOveragePerCrr:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class FltOptMustPriceReuseLimit:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class UpperBoundMustPriceFactorForNotNonStp:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class UpperBoundLfsfactor:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class NumOfMustPriceNstp1StpOnlSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class NumOfMustPriceNstp1StpInrlSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class UpperBoundMustPriceFactorForNonStp:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MaxAllowedLfsoveragePerCrrPercent:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class TargetMinNumOfLfsonlSolPerCrr:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class TargetMinNumOfLfstotOnlSolPercent:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class FltOptLfsreuseLimitForNonAvs:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class FltOptLfsreuseLimitForAvs:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class AvsPenaltyCrrs:
            """
            :ivar value:
            """
            value: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MaxNumOfNonStpOnlSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MaxNumOfNonStpInrlSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MaxNumOfSingleStpOnlSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MaxNumOf2PlusStpSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MinAllowedOveragePerCrrPercent:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MinAllowedOveragePerCrr:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MaxRelFareLvlOfxForNonStp:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class MaxRelFareLvlOfxForCnx:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class NumOfMustPrice2PlusStpSol:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class ItineraryNumberThreshold:
            """
            :ivar value:
            """
            value: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class TicketingSumOfLocals:
            """
            :ivar enable: Enable Ticketing Sum of Locals processing.
            """
            enable: bool = field(
                default=False,
                metadata=dict(
                    name="Enable",
                    type="Attribute"
                )
            )

        @dataclass
        class MultiAirportCodes:
            """
            :ivar enable_open_jaw: Enable open jaw leg combinations.
            """
            enable_open_jaw: bool = field(
                default=False,
                metadata=dict(
                    name="EnableOpenJaw",
                    type="Attribute"
                )
            )

        @dataclass
        class ExcludeCallDirectCarriers:
            """
            :ivar enabled: Force DSF to return schedules only for carriers bookable by Sabre.
            """
            enabled: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Enabled",
                    type="Attribute"
                )
            )

        @dataclass
        class ValidatingCarrierCheck:
            """
            :ivar settlement_validation:
            :ivar ietvalidation:
            :ivar carrier:
            :ivar country:
            """
            settlement_validation: Optional["AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.SettlementValidation"] = field(
                default=None,
                metadata=dict(
                    name="SettlementValidation",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    required=True
                )
            )
            ietvalidation: Optional["AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.Ietvalidation"] = field(
                default=None,
                metadata=dict(
                    name="IETValidation",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    required=True
                )
            )
            carrier: List["AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.Carrier"] = field(
                default_factory=list,
                metadata=dict(
                    name="Carrier",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            country: List["AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.Country"] = field(
                default_factory=list,
                metadata=dict(
                    name="Country",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class SettlementValidation:
                """If set to true validate BSP agreement for given carriers.

                :ivar ind:
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Ind",
                        type="Attribute",
                        required=True
                    )
                )

            @dataclass
            class Ietvalidation:
                """If set to true validate IET agreement for listed countries.

                :ivar ind:
                """
                ind: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Ind",
                        type="Attribute",
                        required=True
                    )
                )

            @dataclass
            class Carrier:
                """
                :ivar code:
                """
                code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Code",
                        type="Attribute",
                        required=True,
                        pattern=r"[0-9A-Z]{2,3}"
                    )
                )

            @dataclass
            class Country:
                """
                :ivar code:
                """
                code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Code",
                        type="Attribute",
                        required=True,
                        pattern=r"[a-zA-Z]{2}"
                    )
                )

        @dataclass
        class FlightRepeatLimit:
            """
            :ivar value: Flight Repeat Limit for DSF. Expected value 1-100.
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class DiversityParameters:
            """
            :ivar weightings: Defines how important various parameter options are in the response. Sum of all weightings needs to equal 10.
            :ivar time_of_day_distribution: Defines how the options in the response should be distributed between certain departure time of day ranges. All defined TimeOfDayRanges need to cover the whole day and the sum of all Percentages needs to equal 100.
            :ivar inbound_outbound_pairing: Defines the requested ratio of inbounds to outbounds in the response.
            :ivar additional_non_stops_number: Defines how many additional non-stop options should be added to the response. Overrides @Percentage.
            :ivar additional_non_stops_percentage: Defines how many additional non-stop options should be added to the response as a percentage of the requested number of options.
            """
            weightings: Optional["AirSearchPrefsType.TpaExtensions.DiversityParameters.Weightings"] = field(
                default=None,
                metadata=dict(
                    name="Weightings",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            time_of_day_distribution: Optional["AirSearchPrefsType.TpaExtensions.DiversityParameters.TimeOfDayDistribution"] = field(
                default=None,
                metadata=dict(
                    name="TimeOfDayDistribution",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            inbound_outbound_pairing: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="InboundOutboundPairing",
                    type="Attribute",
                    min_inclusive=1.0,
                    max_inclusive=1000.0
                )
            )
            additional_non_stops_number: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="AdditionalNonStopsNumber",
                    type="Attribute",
                    min_inclusive=1.0
                )
            )
            additional_non_stops_percentage: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="AdditionalNonStopsPercentage",
                    type="Attribute",
                    min_inclusive=0.0,
                    max_inclusive=100.0
                )
            )

            @dataclass
            class Weightings:
                """
                :ivar price_weight: Defines how important price options are on a scale from 0 to 10.
                :ivar travel_time_weight: Defines how important travel time options are on a scale from 0 to 10.
                """
                price_weight: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="PriceWeight",
                        type="Attribute",
                        required=True,
                        min_inclusive=0.0,
                        max_inclusive=10.0
                    )
                )
                travel_time_weight: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="TravelTimeWeight",
                        type="Attribute",
                        required=True,
                        min_inclusive=0.0,
                        max_inclusive=10.0
                    )
                )

            @dataclass
            class TimeOfDayDistribution:
                """
                :ivar time_of_day_range:
                """
                time_of_day_range: List["AirSearchPrefsType.TpaExtensions.DiversityParameters.TimeOfDayDistribution.TimeOfDayRange"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="TimeOfDayRange",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=2,
                        max_occurs=4
                    )
                )

                @dataclass
                class TimeOfDayRange:
                    """
                    :ivar begin: Beginning of the TimeOfDayRange in HHMM format.
                    :ivar end: End of the TimeOfDayRange in HHMM format.
                    :ivar percentage: Defines how many percent options should be in the TimeOfDayRange.
                    """
                    begin: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Begin",
                            type="Attribute",
                            required=True,
                            pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
                        )
                    )
                    end: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="End",
                            type="Attribute",
                            required=True,
                            pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
                        )
                    )
                    percentage: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="Percentage",
                            type="Attribute",
                            required=True,
                            min_inclusive=0.0,
                            max_inclusive=100.0
                        )
                    )

        @dataclass
        class AdditionalFareLimit:
            """
            :ivar value: Additional fare limit.
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class FareFocusRules:
            """
            :ivar exclude: Exclude fare focus rules.
            """
            exclude: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Exclude",
                    type="Attribute"
                )
            )

        @dataclass
        class SellingLevels:
            """
            :ivar selling_level_rules:
            :ivar show_fare_amounts:
            """
            selling_level_rules: Optional["AirSearchPrefsType.TpaExtensions.SellingLevels.SellingLevelRules"] = field(
                default=None,
                metadata=dict(
                    name="SellingLevelRules",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            show_fare_amounts: Optional["AirSearchPrefsType.TpaExtensions.SellingLevels.ShowFareAmounts"] = field(
                default=None,
                metadata=dict(
                    name="ShowFareAmounts",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )

            @dataclass
            class SellingLevelRules:
                """
                :ivar ignore: Force ignore adjustment selling level rules
                """
                ignore: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Ignore",
                        type="Attribute",
                        required=True
                    )
                )

            @dataclass
            class ShowFareAmounts:
                """
                :ivar original: Show original selling fare level amounts and total adjusted amount in Fare Calc line
                :ivar adjusted: Show selling level amounts and total adjusted amount in Fare Calc line
                """
                original: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Original",
                        type="Attribute"
                    )
                )
                adjusted: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Adjusted",
                        type="Attribute"
                    )
                )

        @dataclass
        class Budget:
            """
            :ivar minimum_price: Minimum price to include in response
            :ivar maximum_price: Maximum price to include in response
            :ivar relative_price_threshold: Relative price difference threshold to be respected while choosing alternative options
            """
            minimum_price: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="MinimumPrice",
                    type="Attribute"
                )
            )
            maximum_price: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="MaximumPrice",
                    type="Attribute"
                )
            )
            relative_price_threshold: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="RelativePriceThreshold",
                    type="Attribute",
                    pattern=r"0|-?[1-9][0-9]*%?"
                )
            )

        @dataclass
        class OptionsPerDatePairList:
            """
            :ivar options_per_date_pair:
            """
            options_per_date_pair: List[OptionsPerDatePairType] = field(
                default_factory=list,
                metadata=dict(
                    name="OptionsPerDatePair",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

        @dataclass
        class CountryPref:
            """
            :ivar code:
            :ivar prefer_level:
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True,
                    pattern=r"[a-zA-Z]{2}"
                )
            )
            prefer_level: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="PreferLevel",
                    type="Attribute",
                    required=True,
                    pattern=r"Unacceptable"
                )
            )

        @dataclass
        class OnlineIndicator:
            """
            :ivar ind: Specifies if the associated data is formatted or not. If true, then it is formatted, if false, then not formatted.
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute"
                )
            )

        @dataclass
        class InterlineIndicator:
            """
            :ivar ind: Specifies if the associated data is formatted or not. If true, then it is formatted, if false, then not formatted.
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute"
                )
            )

        @dataclass
        class ExemptAllTaxes:
            """
            :ivar value:
            """
            value: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute"
                )
            )

        @dataclass
        class ExemptAllTaxesAndFees:
            """
            :ivar value:
            """
            value: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute"
                )
            )

        @dataclass
        class Taxes:
            """
            :ivar tax: Specify tax amount and code.
            """
            tax: List[TaxCodeAmountType] = field(
                default_factory=list,
                metadata=dict(
                    name="Tax",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )

    @dataclass
    class AncillaryFees:
        """
        :ivar ancillary_fee_group: List of requested groups
        :ivar enable: Enable Ancillary Fees processing path.
        :ivar summary: Flag whether this is a summary request.
        """
        ancillary_fee_group: List["AirSearchPrefsType.AncillaryFees.AncillaryFeeGroup"] = field(
            default_factory=list,
            metadata=dict(
                name="AncillaryFeeGroup",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        enable: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Enable",
                type="Attribute",
                required=True
            )
        )
        summary: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Summary",
                type="Attribute"
            )
        )

        @dataclass
        class AncillaryFeeGroup:
            """
            :ivar code: Group code
            :ivar count: Number of items
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True
                )
            )
            count: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Count",
                    type="Attribute"
                )
            )

    @dataclass
    class FrequentFlyer:
        """
        :ivar status: Frequent Flyer Status
        :ivar airline_code: Airline Carrier Code
        """
        status: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Status",
                type="Attribute",
                required=True
            )
        )
        airline_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="AirlineCode",
                type="Attribute"
            )
        )

    @dataclass
    class SpanishFamilyDiscount:
        """
        :ivar level: Spanish Large Family Discount Level. Valid values are 1 or 2.
        """
        level: Optional["AirSearchPrefsType.SpanishFamilyDiscount.Level"] = field(
            default=None,
            metadata=dict(
                name="Level",
                type="Attribute",
                required=True
            )
        )

        class Level(Enum):
            """
            :cvar VALUE_1:
            :cvar VALUE_2:
            """
            VALUE_1 = 1
            VALUE_2 = 2


@dataclass
class AirTravelerType:
    """
    Information about the person traveling. Gender - the gender of the customer, if needed. BirthDate - Date of Birth. Currency - the preferred currency in which monetary amounts should be returned.
    :ivar profile_ref: Stored information about a customer. May contain readily available information relevant to the booking.
    :ivar person_name:
    :ivar telephone:
    :ivar email:
    :ivar address:
    :ivar cust_loyalty: Specify a customer loyalty program.
    :ivar document:
    :ivar passenger_type_quantity: Define information on the number of passengers of a specific type.
    :ivar traveler_ref_number: Direct reference of traveler assigned by requesting system. Used as a cross reference between data segments.
    :ivar flight_segment_rphs: Reference pointers to flight segments
    :ivar gender:
    :ivar share_synch_ind:
    :ivar share_market_ind:
    :ivar birth_date: Date of Birth.
    :ivar currency_code: The preferred currency in which monetary amounts should be returned.
    :ivar passenger_type_code: A three-letter code representing passenger type (e.g. .ADT. for adult, .CNN. for child)
    :ivar accompanied_by_infant: Indicates if an infant accompanying a traveler is with or without a seat.
    """
    profile_ref: Optional["AirTravelerType.ProfileRef"] = field(
        default=None,
        metadata=dict(
            name="ProfileRef",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    person_name: Optional[PersonNameType] = field(
        default=None,
        metadata=dict(
            name="PersonName",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    telephone: List[TelephoneType] = field(
        default_factory=list,
        metadata=dict(
            name="Telephone",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=5
        )
    )
    email: List[EmailType] = field(
        default_factory=list,
        metadata=dict(
            name="Email",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=3
        )
    )
    address: List[AddressType] = field(
        default_factory=list,
        metadata=dict(
            name="Address",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=5
        )
    )
    cust_loyalty: List[CustLoyaltyType] = field(
        default_factory=list,
        metadata=dict(
            name="CustLoyalty",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=5
        )
    )
    document: List[DocumentType] = field(
        default_factory=list,
        metadata=dict(
            name="Document",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=10
        )
    )
    passenger_type_quantity: Optional[PassengerTypeQuantityType] = field(
        default=None,
        metadata=dict(
            name="PassengerTypeQuantity",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    traveler_ref_number: Optional[TravelerRefNumberType] = field(
        default=None,
        metadata=dict(
            name="TravelerRefNumber",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    flight_segment_rphs: Optional["AirTravelerType.FlightSegmentRphs"] = field(
        default=None,
        metadata=dict(
            name="FlightSegmentRPHs",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    gender: Optional["AirTravelerType.Gender"] = field(
        default=None,
        metadata=dict(
            name="Gender",
            type="Attribute"
        )
    )
    share_synch_ind: Optional["AirTravelerType.ShareSynchInd"] = field(
        default=None,
        metadata=dict(
            name="ShareSynchInd",
            type="Attribute"
        )
    )
    share_market_ind: Optional["AirTravelerType.ShareMarketInd"] = field(
        default=None,
        metadata=dict(
            name="ShareMarketInd",
            type="Attribute"
        )
    )
    birth_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BirthDate",
            type="Attribute"
        )
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    passenger_type_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PassengerTypeCode",
            type="Attribute",
            required=True,
            pattern=r"[a-zA-Z]{3}"
        )
    )
    accompanied_by_infant: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AccompaniedByInfant",
            type="Attribute"
        )
    )

    @dataclass
    class ProfileRef:
        """
        :ivar unique_id:
        """
        unique_id: Optional[UniqueIdType] = field(
            default=None,
            metadata=dict(
                name="UniqueID",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                required=True
            )
        )

    @dataclass
    class FlightSegmentRphs:
        """
        :ivar flight_segment_rph: Reference to the flight segments for this traveler
        """
        flight_segment_rph: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="FlightSegmentRPH",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=99,
                pattern=r"[0-9]{1,8}"
            )
        )

    class Gender(Enum):
        """
        :cvar FEMALE:
        :cvar MALE:
        :cvar UNKNOWN:
        """
        FEMALE = "Female"
        MALE = "Male"
        UNKNOWN = "Unknown"

    class ShareSynchInd(Enum):
        """value="Inherit" Permission for sharing data for synchronization of
        information held by other travel service providers.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"

    class ShareMarketInd(Enum):
        """value="Inherit" Permission for sharing data for marketing purposes.

        :cvar INHERIT:
        :cvar NO:
        :cvar YES:
        """
        INHERIT = "Inherit"
        NO = "No"
        YES = "Yes"


@dataclass
class ExchangeSourceType:
    """
    :ivar booking_channel:
    :ivar agent_sine: Identifies the party within the requesting entity.
    :ivar pseudo_city_code: An identification code assigned to an office/agency by a reservation system.
    :ivar isocountry: The country code of the requesting party.
    :ivar isocurrency: The currency code in which the reservation will be ticketed.
    :ivar agent_duty_code: An authority code assigned to a requestor.
    :ivar airline_vendor_id: The IATA assigned airline code.
    :ivar airport_code: The IATA assigned airport code.
    :ivar first_depart_point: The point of first departure in a trip.
    :ivar ersp_user_id: Electronic Reservation Service Provider (ERSP) assigned identifier used to identify the individual using the ERSP system.
    :ivar personal_city_code: City code part of Office Accounting Code
    :ivar accounting_code: Accounting Code part of Office Accounting Code
    :ivar office_code: Office Code part of Office Accounting Code
    :ivar default_ticketing_carrier: Default Ticketing Carrier for Office Accounting Code
    :ivar airline_channel_code: Airline Channel Code
    :ivar agent_department_code: Agent department code
    :ivar agent_function: Agent function
    :ivar travel_agency_iata: Travel agency IATA
    :ivar home_agency_iata: Home agency IATA
    :ivar agent_iata: Agent IATA
    :ivar vendor_crscode: Vendor CRS code
    :ivar agent_duty: Agent duty
    :ivar abacus_user: Abacus user
    :ivar agent_city: Agent city
    :ivar main_travel_agency_pcc: Main travel agency PCC
    :ivar carrier: Carrier
    :ivar host_carrier: PCC Host Carrier
    :ivar eticket_capable: Agency is Eticket capable
    :ivar co_host_id: CoHostID
    """
    booking_channel: Optional[SourceBookingChannelType] = field(
        default=None,
        metadata=dict(
            name="BookingChannel",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    agent_sine: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentSine",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    isocountry: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ISOCountry",
            type="Attribute",
            pattern=r"[a-zA-Z]{2}"
        )
    )
    isocurrency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ISOCurrency",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    agent_duty_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentDutyCode",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    airline_vendor_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirlineVendorID",
            type="Attribute",
            pattern=r"[A-Z0-9]{2,3}"
        )
    )
    airport_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirportCode",
            type="Attribute",
            pattern=r"[A-Z0-9]{3,5}"
        )
    )
    first_depart_point: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FirstDepartPoint",
            type="Attribute",
            min_length=3.0,
            max_length=3.0
        )
    )
    ersp_user_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ERSP_UserID",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    personal_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PersonalCityCode",
            type="Attribute",
            pattern=r"[0-9A-Z]{3,4}"
        )
    )
    accounting_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AccountingCode",
            type="Attribute",
            pattern=r"[0-9a-zA-Z]{2,3}"
        )
    )
    office_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OfficeCode",
            type="Attribute",
            pattern=r"[0-9]{7}"
        )
    )
    default_ticketing_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DefaultTicketingCarrier",
            type="Attribute",
            pattern=r"[A-Z0-9]{2}[A-Z]?"
        )
    )
    airline_channel_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirlineChannelCode",
            type="Attribute",
            pattern=r"[A-Z]{3}"
        )
    )
    agent_department_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentDepartmentCode",
            type="Attribute",
            max_length=6.0
        )
    )
    agent_function: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentFunction",
            type="Attribute",
            max_length=3.0
        )
    )
    travel_agency_iata: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelAgencyIATA",
            type="Attribute",
            pattern=r"[0-9]{1,14}"
        )
    )
    home_agency_iata: Optional[str] = field(
        default=None,
        metadata=dict(
            name="HomeAgencyIATA",
            type="Attribute",
            pattern=r"[0-9]{1,14}"
        )
    )
    agent_iata: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentIATA",
            type="Attribute",
            pattern=r"[0-9]{1,14}"
        )
    )
    vendor_crscode: Optional[str] = field(
        default=None,
        metadata=dict(
            name="VendorCRSCode",
            type="Attribute"
        )
    )
    agent_duty: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentDuty",
            type="Attribute",
            length=1
        )
    )
    abacus_user: bool = field(
        default=False,
        metadata=dict(
            name="AbacusUser",
            type="Attribute"
        )
    )
    agent_city: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentCity",
            type="Attribute",
            required=True,
            pattern=r"[a-zA-Z]{3}"
        )
    )
    main_travel_agency_pcc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MainTravelAgencyPCC",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=16.0
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            pattern=r"[0-9A-Z]{2,3}"
        )
    )
    host_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="HostCarrier",
            type="Attribute",
            pattern=r"[0-9A-Z]{2,3}"
        )
    )
    eticket_capable: bool = field(
        default=False,
        metadata=dict(
            name="ETicketCapable",
            type="Attribute"
        )
    )
    co_host_id: Optional[int] = field(
        default=None,
        metadata=dict(
            name="CoHostID",
            type="Attribute"
        )
    )


@dataclass
class ExchangeTravelPreferencesTpaExtensionsType:
    """
    :ivar exempt_all_taxes: Exempt all taxes (/TE)
    :ivar exempt_all_taxes_and_fees: Exempt all taxes and fees (/TN)
    :ivar taxes: Specify Taxes (/TX)
    :ivar exempt_tax: Exempt Tax (/TE)
    :ivar settlement_method:
    """
    class Meta:
        name = "ExchangeTravelPreferencesTPA_ExtensionsType"

    exempt_all_taxes: Optional["ExchangeTravelPreferencesTpaExtensionsType.ExemptAllTaxes"] = field(
        default=None,
        metadata=dict(
            name="ExemptAllTaxes",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    exempt_all_taxes_and_fees: Optional["ExchangeTravelPreferencesTpaExtensionsType.ExemptAllTaxesAndFees"] = field(
        default=None,
        metadata=dict(
            name="ExemptAllTaxesAndFees",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    taxes: Optional["ExchangeTravelPreferencesTpaExtensionsType.Taxes"] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    exempt_tax: List[TaxCodeType] = field(
        default_factory=list,
        metadata=dict(
            name="ExemptTax",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    settlement_method: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SettlementMethod",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            pattern=r"[a-zA-Z0-9]{3}"
        )
    )

    @dataclass
    class ExemptAllTaxes:
        """
        :ivar value:
        """
        value: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Value",
                type="Attribute"
            )
        )

    @dataclass
    class ExemptAllTaxesAndFees:
        """
        :ivar value:
        """
        value: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Value",
                type="Attribute"
            )
        )

    @dataclass
    class Taxes:
        """
        :ivar tax: Specify tax amount and code.
        """
        tax: List[TaxCodeAmountType] = field(
            default_factory=list,
            metadata=dict(
                name="Tax",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )


@dataclass
class OriginDestinationInformationType(TravelDateTimeType):
    """Origin and Destination location, and time information for the request. Also
    includes the ability to specify a connection location for the search.

    :ivar origin_location: Travel Origin Location - for example, air uses the IATA 3 letter code.
    :ivar destination_location: Travel Destination Location - for example, air uses the IATA 3 letter code.
    :ivar connection_locations: Travel Connection Location - for example, air uses the IATA 3 letter code.
    """
    origin_location: Optional["OriginDestinationInformationType.OriginLocation"] = field(
        default=None,
        metadata=dict(
            name="OriginLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    destination_location: Optional["OriginDestinationInformationType.DestinationLocation"] = field(
        default=None,
        metadata=dict(
            name="DestinationLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    connection_locations: Optional[ConnectionType] = field(
        default=None,
        metadata=dict(
            name="ConnectionLocations",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )

    @dataclass
    class OriginLocation(RequestLocationType):
        """
        :ivar all_airports: Flag indicating if all cached origin cities are to be processed as origin airports.
        """
        all_airports: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="AllAirports",
                type="Attribute"
            )
        )

    @dataclass
    class DestinationLocation(RequestLocationType):
        """
        :ivar all_airports: Flag indicating if all cached destination cities are to be processed as destination airports.
        """
        all_airports: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="AllAirports",
                type="Attribute"
            )
        )


@dataclass
class SourceType:
    """
    :ivar requestor_id: An identifier of the entity making the request (e.g. ATA/IATA/ID number, Electronic Reservation Service Provider (ERSP), Association of British Travel Agents (ABTA)).
    :ivar position:
    :ivar booking_channel:
    :ivar agent_sine: Identifies the party within the requesting entity.
    :ivar pseudo_city_code: An identification code assigned to an office/agency by a reservation system.
    :ivar isocountry: The country code of the requesting party.
    :ivar isocurrency: The currency code in which the reservation will be ticketed.
    :ivar agent_duty_code: An authority code assigned to a requestor.
    :ivar airline_vendor_id: The IATA assigned airline code.
    :ivar airport_code: The IATA assigned airport code.
    :ivar first_depart_point: The point of first departure in a trip.
    :ivar ersp_user_id: Electronic Reservation Service Provider (ERSP) assigned identifier used to identify the individual using the ERSP system.
    :ivar personal_city_code: City code part of Office Accounting Code
    :ivar accounting_code: Accounting Code part of Office Accounting Code
    :ivar office_code: Office Code part of Office Accounting Code
    :ivar default_ticketing_carrier: Default Ticketing Carrier for Office Accounting Code
    :ivar airline_channel_code: Airline Channel Code
    :ivar agent_department_code: Agent department code
    :ivar agent_function: Agent function
    :ivar travel_agency_iata: Travel agency IATA
    :ivar home_agency_iata: Home agency IATA
    :ivar agent_iata: Agent IATA
    :ivar vendor_crscode: Vendor CRS code
    :ivar agent_duty: Agent duty
    :ivar abacus_user: Abacus user
    :ivar agent_city: Agent city
    :ivar carrier: Carrier
    :ivar main_travel_agency_pcc: Main travel agency PCC
    :ivar home_pcc: Home PCC
    """
    requestor_id: Optional[UniqueIdType] = field(
        default=None,
        metadata=dict(
            name="RequestorID",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    position: Optional[PositionType] = field(
        default=None,
        metadata=dict(
            name="Position",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    booking_channel: Optional[SourceBookingChannelType] = field(
        default=None,
        metadata=dict(
            name="BookingChannel",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    agent_sine: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentSine",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    isocountry: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ISOCountry",
            type="Attribute",
            pattern=r"[a-zA-Z]{2}"
        )
    )
    isocurrency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ISOCurrency",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    agent_duty_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentDutyCode",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    airline_vendor_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirlineVendorID",
            type="Attribute",
            pattern=r"[A-Z0-9]{2,3}"
        )
    )
    airport_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirportCode",
            type="Attribute",
            pattern=r"[A-Z0-9]{3,5}"
        )
    )
    first_depart_point: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FirstDepartPoint",
            type="Attribute",
            min_length=3.0,
            max_length=3.0
        )
    )
    ersp_user_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ERSP_UserID",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    personal_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PersonalCityCode",
            type="Attribute",
            pattern=r"[0-9A-Z]{3,4}"
        )
    )
    accounting_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AccountingCode",
            type="Attribute",
            pattern=r"[0-9a-zA-Z]{2,3}"
        )
    )
    office_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OfficeCode",
            type="Attribute",
            pattern=r"[0-9]{7}"
        )
    )
    default_ticketing_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DefaultTicketingCarrier",
            type="Attribute",
            pattern=r"[A-Z0-9]{2}[A-Z]?"
        )
    )
    airline_channel_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirlineChannelCode",
            type="Attribute",
            pattern=r"[A-Z]{3}"
        )
    )
    agent_department_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentDepartmentCode",
            type="Attribute",
            max_length=6.0
        )
    )
    agent_function: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentFunction",
            type="Attribute",
            max_length=3.0
        )
    )
    travel_agency_iata: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelAgencyIATA",
            type="Attribute",
            pattern=r"[0-9]{1,14}"
        )
    )
    home_agency_iata: Optional[str] = field(
        default=None,
        metadata=dict(
            name="HomeAgencyIATA",
            type="Attribute",
            pattern=r"[0-9]{1,14}"
        )
    )
    agent_iata: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentIATA",
            type="Attribute",
            pattern=r"[0-9]{1,14}"
        )
    )
    vendor_crscode: Optional[str] = field(
        default=None,
        metadata=dict(
            name="VendorCRSCode",
            type="Attribute"
        )
    )
    agent_duty: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentDuty",
            type="Attribute",
            length=1
        )
    )
    abacus_user: bool = field(
        default=False,
        metadata=dict(
            name="AbacusUser",
            type="Attribute"
        )
    )
    agent_city: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentCity",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            pattern=r"[0-9A-Z]{2,3}"
        )
    )
    main_travel_agency_pcc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MainTravelAgencyPCC",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )
    home_pcc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="HomePCC",
            type="Attribute",
            min_length=1.0,
            max_length=16.0
        )
    )


@dataclass
class TransactionType:
    """IntelliSell Type.

    :ivar request_type: Identifier of the type of request.
    :ivar service_tag: Identifier of the transaction path.
    :ivar purchase_type: A target available for user, that can be used to create specific rules. For example, if the client wants to target preferred customer request, we can use this element to achieve this.
    :ivar sabre_ath: Sabre authentication ID (ATH) - passed into the request to keep session information when communicating with TPF. The use of this element had been deprecated and is achieved by session pooling mechanism in Intellisell.
    :ivar tran_id: Transaction ID.
    :ivar client_session_id: A unique identifier to relate all transactions within a single session. Used by AirShop/LFE transactions.
    :ivar branch: Attribute of the Rule that can be passed in to selectively target a rule. This has been deprecated.
    :ivar compress_response: Decides if the response should be compressed.
    :ivar fare_overrides: Contains a sequence of fare overrides.
    :ivar diagnostics: For internal use
    :ivar subagent_data: Subagent data for LFE transactions.
    :ivar response_sorting: Settings for IntelliSell merchandising
    :ivar seat_status_sim:
    :ivar available_level:
    :ivar atsetest: Allows ATSE Team to test new features. This element and its content is meant to never be published.
    :ivar debug: Turns on or off debug mode.
    :ivar debug_key: Key unlocking disabled debug mode.
    :ivar config_set: Alternative configuration selector.
    :ivar disable_cache: Disables itinerary cache for this request (if it is enabled in this service).
    :ivar chunk_number: Helps Forwarder in keeping track of response parts generated as a result of request processing (AB only).
    :ivar show_itin_source: If enabled, Intellisell will return source for each itinerary.
    """
    request_type: Optional["TransactionType.RequestType"] = field(
        default=None,
        metadata=dict(
            name="RequestType",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    service_tag: Optional["TransactionType.ServiceTag"] = field(
        default=None,
        metadata=dict(
            name="ServiceTag",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    purchase_type: Optional["TransactionType.PurchaseType"] = field(
        default=None,
        metadata=dict(
            name="PurchaseType",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    sabre_ath: Optional["TransactionType.SabreAth"] = field(
        default=None,
        metadata=dict(
            name="SabreAth",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    tran_id: Optional["TransactionType.TranId"] = field(
        default=None,
        metadata=dict(
            name="TranID",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    client_session_id: Optional["TransactionType.ClientSessionId"] = field(
        default=None,
        metadata=dict(
            name="ClientSessionID",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    branch: Optional["TransactionType.Branch"] = field(
        default=None,
        metadata=dict(
            name="Branch",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    compress_response: Optional["TransactionType.CompressResponse"] = field(
        default=None,
        metadata=dict(
            name="CompressResponse",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    fare_overrides: Optional["TransactionType.FareOverrides"] = field(
        default=None,
        metadata=dict(
            name="FareOverrides",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    diagnostics: Optional["TransactionType.Diagnostics"] = field(
        default=None,
        metadata=dict(
            name="Diagnostics",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    subagent_data: Optional["TransactionType.SubagentData"] = field(
        default=None,
        metadata=dict(
            name="SubagentData",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    response_sorting: Optional["TransactionType.ResponseSorting"] = field(
        default=None,
        metadata=dict(
            name="ResponseSorting",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    seat_status_sim: Optional[SeatStatusSimType] = field(
        default=None,
        metadata=dict(
            name="SeatStatusSim",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    available_level: Optional["TransactionType.AvailableLevel"] = field(
        default=None,
        metadata=dict(
            name="AvailableLevel",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    atsetest: Optional["TransactionType.Atsetest"] = field(
        default=None,
        metadata=dict(
            name="ATSETest",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    debug: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Debug",
            type="Attribute"
        )
    )
    debug_key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DebugKey",
            type="Attribute"
        )
    )
    config_set: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ConfigSet",
            type="Attribute"
        )
    )
    disable_cache: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DisableCache",
            type="Attribute"
        )
    )
    chunk_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ChunkNumber",
            type="Attribute"
        )
    )
    show_itin_source: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ShowItinSource",
            type="Attribute"
        )
    )

    @dataclass
    class RequestType:
        """
        :ivar value:
        :ivar name:
        """
        value: Optional[str] = field(
            default=None,
        )
        name: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Name",
                type="Attribute"
            )
        )

    @dataclass
    class ServiceTag:
        """
        :ivar value:
        :ivar name:
        """
        value: Optional[str] = field(
            default=None,
        )
        name: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Name",
                type="Attribute"
            )
        )

    @dataclass
    class PurchaseType:
        """
        :ivar name:
        """
        name: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Name",
                type="Attribute"
            )
        )

    @dataclass
    class SabreAth:
        """
        :ivar value:
        :ivar binary_sec_token:
        :ivar conversation_id:
        """
        value: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Value",
                type="Attribute"
            )
        )
        binary_sec_token: Optional[str] = field(
            default=None,
            metadata=dict(
                name="BinarySecToken",
                type="Attribute"
            )
        )
        conversation_id: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ConversationID",
                type="Attribute"
            )
        )

    @dataclass
    class TranId:
        """
        :ivar value:
        """
        value: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Value",
                type="Attribute"
            )
        )

    @dataclass
    class ClientSessionId:
        """
        :ivar value:
        """
        value: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Value",
                type="Attribute"
            )
        )

    @dataclass
    class Branch:
        """
        :ivar name:
        """
        name: str = field(
            default="Main",
            metadata=dict(
                name="Name",
                type="Attribute"
            )
        )

    @dataclass
    class CompressResponse:
        """
        :ivar value:
        """
        value: bool = field(
            default=False,
            metadata=dict(
                name="Value",
                type="Attribute"
            )
        )

    @dataclass
    class FareOverrides:
        """
        :ivar fare_override: Contains attributes of the FareGroup functionality used during shopping and pricing. If passed in this request, it will override setting in the rule.
        """
        fare_override: List["TransactionType.FareOverrides.FareOverride"] = field(
            default_factory=list,
            metadata=dict(
                name="FareOverride",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=4
            )
        )

        @dataclass
        class FareOverride:
            """
            :ivar vendor_pref: Specify vendors to include and exclude from the response.
            :ivar tpa_extensions: This is a place holder for additional elements.
            :ivar fare_type: Attribute of FareGroup functionality, used in search of fares during shopping.
            :ivar pseudo_city_code:
            :ivar corporate_id: Attribute of FareGroup functionality, used in search of fares during shopping.
            :ivar callable: Indicator to enable/disable this FareOverride.
            """
            vendor_pref: List[CompanyNamePrefType] = field(
                default_factory=list,
                metadata=dict(
                    name="VendorPref",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            tpa_extensions: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="TPA_Extensions",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            fare_type: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="FareType",
                    type="Attribute",
                    required=True
                )
            )
            pseudo_city_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="PseudoCityCode",
                    type="Attribute"
                )
            )
            corporate_id: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="CorporateID",
                    type="Attribute"
                )
            )
            callable: str = field(
                default="true",
                metadata=dict(
                    name="Callable",
                    type="Attribute"
                )
            )

    @dataclass
    class Diagnostics:
        """
        :ivar diagnostic: Specify diagnostic code and which service to sent it to.
        """
        diagnostic: List["TransactionType.Diagnostics.Diagnostic"] = field(
            default_factory=list,
            metadata=dict(
                name="Diagnostic",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=9223372036854775807
            )
        )

        @dataclass
        class Diagnostic:
            """
            :ivar diagnostic_argument: Name-value pairs to be used as arguments for the diagnostic.
            :ivar tpa_extensions: This is a place holder for additional elements.
            :ivar target:
            :ivar code:
            """
            diagnostic_argument: List["TransactionType.Diagnostics.Diagnostic.DiagnosticArgument"] = field(
                default_factory=list,
                metadata=dict(
                    name="DiagnosticArgument",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            tpa_extensions: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="TPA_Extensions",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            target: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Target",
                    type="Attribute"
                )
            )
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True,
                    pattern=r"[A-Za-z0-9_]+(/[A-Za-z0-9_]+)*"
                )
            )

            @dataclass
            class DiagnosticArgument:
                """
                :ivar name:
                :ivar value:
                """
                name: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Name",
                        type="Attribute",
                        required=True
                    )
                )
                value: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Value",
                        type="Attribute"
                    )
                )

    @dataclass
    class SubagentData:
        """
        :ivar code:
        """
        code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Code",
                type="Attribute"
            )
        )

    @dataclass
    class ResponseSorting:
        """
        :ivar enable_chronological_sorting:
        """
        enable_chronological_sorting: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="EnableChronologicalSorting",
                type="Attribute"
            )
        )

    @dataclass
    class AvailableLevel:
        """
        :ivar value:
        """
        value: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Value",
                type="Attribute",
                required=True
            )
        )

    @dataclass
    class Atsetest:
        """
        :ivar feature: Meaning of that attribute is dependent on MIP Team, ISell sends it in all ShoppingRequests when specified.
        """
        feature: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Feature",
                type="Attribute"
            )
        )


@dataclass
class ExchangeAirSearchPrefsType:
    """
    :ivar tpa_extensions:
    :ivar valid_interline_ticket: Request itins that are validated on base of interline ticketing aggrement.
    """
    tpa_extensions: Optional[ExchangeTravelPreferencesTpaExtensionsType] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    valid_interline_ticket: bool = field(
        default=False,
        metadata=dict(
            name="ValidInterlineTicket",
            type="Attribute"
        )
    )


@dataclass
class ExchangeOriginDestinationInformationType(OriginDestinationInformationType):
    """
    :ivar flight:
    :ivar date_flexibility: The number of alternate days around the travel date to search.
    :ivar sister_destination_location: List of alternate destination cities to search
    :ivar sister_destination_mileage:
    :ivar sister_origin_location: List of alternate origin cities to search
    :ivar sister_origin_mileage:
    :ivar segment_type:
    :ivar alternate_time: Maximum time difference/deviation allowed.
    :ivar max_one_way_options: Maximum number of options to return.
    :ivar num_one_way_options: Number of options for requested date.
    :ivar cabin_pref: Defines preferred cabin to be used in a search for this leg level (if SegmentType is "O") or segment (if SegmentType is "X"). The cabin type specified in this element will override the cabin type specified at the request level for this leg/segment. If a cabin type is not specified for this element the cabin type at request level will be used as default for this leg or segment. If the cabin type is not specified at both the leg/segment level and request level a default cabin of "Economy" will be used?
    :ivar connection_time: Connection time between segments.
    :ivar total_travel_time: Total travel time settings
    """
    flight: List[ExchangeOriginDestinationFlightType] = field(
        default_factory=list,
        metadata=dict(
            name="Flight",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    date_flexibility: List["ExchangeOriginDestinationInformationType.DateFlexibility"] = field(
        default_factory=list,
        metadata=dict(
            name="DateFlexibility",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=2
        )
    )
    sister_destination_location: List[RequestLocationType] = field(
        default_factory=list,
        metadata=dict(
            name="SisterDestinationLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sister_destination_mileage: Optional["ExchangeOriginDestinationInformationType.SisterDestinationMileage"] = field(
        default=None,
        metadata=dict(
            name="SisterDestinationMileage",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    sister_origin_location: List[RequestLocationType] = field(
        default_factory=list,
        metadata=dict(
            name="SisterOriginLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sister_origin_mileage: Optional["ExchangeOriginDestinationInformationType.SisterOriginMileage"] = field(
        default=None,
        metadata=dict(
            name="SisterOriginMileage",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    segment_type: Optional["ExchangeOriginDestinationInformationType.SegmentType"] = field(
        default=None,
        metadata=dict(
            name="SegmentType",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    alternate_time: Optional["ExchangeOriginDestinationInformationType.AlternateTime"] = field(
        default=None,
        metadata=dict(
            name="AlternateTime",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    max_one_way_options: Optional["ExchangeOriginDestinationInformationType.MaxOneWayOptions"] = field(
        default=None,
        metadata=dict(
            name="MaxOneWayOptions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    num_one_way_options: Optional["ExchangeOriginDestinationInformationType.NumOneWayOptions"] = field(
        default=None,
        metadata=dict(
            name="NumOneWayOptions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    cabin_pref: Optional[CabinPrefType] = field(
        default=None,
        metadata=dict(
            name="CabinPref",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    connection_time: Optional["ExchangeOriginDestinationInformationType.ConnectionTime"] = field(
        default=None,
        metadata=dict(
            name="ConnectionTime",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    total_travel_time: Optional["ExchangeOriginDestinationInformationType.TotalTravelTime"] = field(
        default=None,
        metadata=dict(
            name="TotalTravelTime",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )

    @dataclass
    class DateFlexibility:
        """
        :ivar nbr_of_days: Number of alternate dates before and after requested travel date.
        :ivar plus: Number of alternate dates before requested travel date.
        :ivar minus: Number of alternate dates after requested travel date.
        :ivar validate: Flag telling if dates within the specified range should be processed in the validate path.
        """
        nbr_of_days: Optional[int] = field(
            default=None,
            metadata=dict(
                name="NbrOfDays",
                type="Attribute"
            )
        )
        plus: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Plus",
                type="Attribute"
            )
        )
        minus: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Minus",
                type="Attribute"
            )
        )
        validate: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Validate",
                type="Attribute"
            )
        )

    @dataclass
    class SegmentType:
        """
        :ivar code: "Code" can be "ARUNK", "O" for normal, or "X" for connection.
        """
        code: Optional["ExchangeOriginDestinationInformationType.SegmentType.Code"] = field(
            default=None,
            metadata=dict(
                name="Code",
                type="Attribute"
            )
        )

        class Code(Enum):
            """
            :cvar ARUNK: Arrival unknown
            :cvar O: Normal
            :cvar X: Connection. Collapses this and subsequent OriginDestinationInformation so that they are treated as single leg.
            """
            ARUNK = "ARUNK"
            O = "O"
            X = "X"

    @dataclass
    class AlternateTime:
        """
        :ivar plus_minus: Maximum time difference between actual and desired time.
        :ivar plus: Maximum number of hours after desired time.
        :ivar minus: Maximum number of hours before desired time.
        """
        plus_minus: Optional[int] = field(
            default=None,
            metadata=dict(
                name="PlusMinus",
                type="Attribute",
                min_inclusive=0.0,
                max_inclusive=9.0
            )
        )
        plus: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Plus",
                type="Attribute",
                min_inclusive=0.0,
                max_inclusive=9.0
            )
        )
        minus: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Minus",
                type="Attribute",
                min_inclusive=0.0,
                max_inclusive=72.0
            )
        )

    @dataclass
    class MaxOneWayOptions:
        """
        :ivar value:
        """
        value: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Value",
                type="Attribute"
            )
        )

    @dataclass
    class NumOneWayOptions:
        """
        :ivar number:
        """
        number: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Number",
                type="Attribute"
            )
        )

    @dataclass
    class ConnectionTime:
        """
        :ivar min:
        :ivar max:
        :ivar excluded_connection_begin: Excluded connection time begin in format HHMM
        :ivar excluded_connection_end: Excluded connection time end in format HHMM
        :ivar enable_excluded_connection: Enable excluded connection time (default: true)
        """
        min: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Min",
                type="Attribute"
            )
        )
        max: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Max",
                type="Attribute"
            )
        )
        excluded_connection_begin: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ExcludedConnectionBegin",
                type="Attribute",
                pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
            )
        )
        excluded_connection_end: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ExcludedConnectionEnd",
                type="Attribute",
                pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
            )
        )
        enable_excluded_connection: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="EnableExcludedConnection",
                type="Attribute"
            )
        )

    @dataclass
    class TotalTravelTime:
        """
        :ivar min:
        :ivar max:
        """
        min: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Min",
                type="Attribute"
            )
        )
        max: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Max",
                type="Attribute"
            )
        )

    @dataclass
    class SisterDestinationMileage:
        """
        :ivar number:
        """
        number: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Number",
                type="Attribute"
            )
        )

    @dataclass
    class SisterOriginMileage:
        """
        :ivar number:
        """
        number: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Number",
                type="Attribute"
            )
        )


@dataclass
class ExchangePostype:
    """
    :ivar source:
    """
    class Meta:
        name = "ExchangePOSType"

    source: Optional[ExchangeSourceType] = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )


@dataclass
class PosType:
    """Point of Sale (POS) is the details identifying the party or connection
    channel making the request.

    :ivar source: This holds details regarding the requestor. It may be repeated to also accommodate the delivery systems.
    """
    class Meta:
        name = "POS_Type"

    source: List[SourceType] = field(
        default_factory=list,
        metadata=dict(
            name="Source",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=5
        )
    )


@dataclass
class TravelerInformationType:
    """Specifies passenger numbers and types.

    :ivar passenger_type_quantity: Specifies number of passengers using Passenger Type Codes.
    :ivar air_traveler: Information profiling the person traveling Gender - the gender of the customer, if needed BirthDate - Date of Birth Currency - the preferred currency in which monetary amounts should be returned.
    """
    passenger_type_quantity: List[PassengerTypeQuantityType] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerTypeQuantity",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=9
        )
    )
    air_traveler: Optional[AirTravelerType] = field(
        default=None,
        metadata=dict(
            name="AirTraveler",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )


@dataclass
class TravelerInfoSummaryType:
    """Specifies passenger numbers and types.

    :ivar seats_requested: The sum of all seats required by all passenger groups.
    :ivar air_traveler_avail: Specifies passenger numbers and types.
    :ivar price_request_information: Identify pricing source, if negotiated fares are requested and if it is a reprice request.
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    :ivar specific_ptc_indicator: If true, this request is for a specific PTC and only fares applicable to that PTC will be checked and returned. It is the same as XOFares flag in Intellisell request.
    """
    seats_requested: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="SeatsRequested",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=4
        )
    )
    air_traveler_avail: List[TravelerInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="AirTravelerAvail",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=4
        )
    )
    price_request_information: Optional[PriceRequestInformationType] = field(
        default=None,
        metadata=dict(
            name="PriceRequestInformation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    tpa_extensions: Optional[TravelerInfoSummaryTpaExtensionsType] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    specific_ptc_indicator: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="SpecificPTC_Indicator",
            type="Attribute"
        )
    )


@dataclass
class ExchangeType:
    """
    :ivar fare:
    :ivar pos:
    :ivar origin_destination_information:
    :ivar arunk:
    :ivar travel_preferences:
    :ivar traveler_info_summary:
    :ivar tpa_extensions:
    :ivar original_tkt_issue_date_time: Original ticket issue date and time
    :ivar exchanged_tkt_issue_date_time: Exchanged ticket issue date and time
    :ivar previous_exchange_date_time: Previous exchange date and time
    :ivar number_of_tax_boxes: Number of tax boxes
    :ivar bypass_advance_purchase_option: Bypass Advance Purchase Option
    """
    fare: Optional[ExchangeFareType] = field(
        default=None,
        metadata=dict(
            name="Fare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    pos: Optional[ExchangePostype] = field(
        default=None,
        metadata=dict(
            name="POS",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    origin_destination_information: List[ExchangeOriginDestinationInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="OriginDestinationInformation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775808,
            sequential=True
        )
    )
    arunk: List[ArunkType] = field(
        default_factory=list,
        metadata=dict(
            name="Arunk",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    travel_preferences: Optional[ExchangeAirSearchPrefsType] = field(
        default=None,
        metadata=dict(
            name="TravelPreferences",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    traveler_info_summary: Optional[TravelerInfoSummaryType] = field(
        default=None,
        metadata=dict(
            name="TravelerInfoSummary",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    tpa_extensions: Optional[ExchangeTpaExtensionsType] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    original_tkt_issue_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OriginalTktIssueDateTime",
            type="Attribute",
            required=True,
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}(T[0-9]{2}:[0-9]{2}:[0-9]{2})?"
        )
    )
    exchanged_tkt_issue_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ExchangedTktIssueDateTime",
            type="Attribute",
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}(T[0-9]{2}:[0-9]{2}:[0-9]{2})?"
        )
    )
    previous_exchange_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PreviousExchangeDateTime",
            type="Attribute",
            pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}(T[0-9]{2}:[0-9]{2}:[0-9]{2})?"
        )
    )
    number_of_tax_boxes: Optional[int] = field(
        default=None,
        metadata=dict(
            name="NumberOfTaxBoxes",
            type="Attribute"
        )
    )
    bypass_advance_purchase_option: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BypassAdvancePurchaseOption",
            type="Attribute",
            length=1
        )
    )


@dataclass
class OtaAirLowFareSearchRq:
    """
    The Low Fare Search Request message requests priced itinerary options for flights between specific city pairs on specific dates for specific numbers and types of passengers. Optional request information can include: - Time / Time Window - Connecting cities. - Client Preferences (airlines, cabin, flight types etc.) The Low Fare Search request contains similar information to a Low Fare Search entry on an airline CRS or GDS.
    :ivar pos: Point of sale object.
    :ivar origin_destination_information: Origin and Destination location, and time information for the Air Low Fare Search request.
    :ivar leg: Single leg specification
    :ivar travel_preferences: Air Low Fare Search Request preference information.
    :ivar traveler_info_summary: Specifies the number of passengers and types for Air Low Fare Search.
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    :ivar echo_token: A sequence number for additional message identification, assigned by the requesting host system. When a request message includes an echo token the corresponding response message MUST include an echo token with an identical value.
    :ivar time_stamp: Indicates the creation date and time of the message in UTC using the following format specified by ISO 8601; YYYY-MM-DDThh:mm:ssZ with time values using the 24 hour clock (e.g. 20 November 2003, 1:59:38 pm UTC becomes 2003-11-20T13:59:38Z).
    :ivar target: Used to indicate whether the request is for the Test or Production system.
    :ivar version: For all OTA versioned messages, the version of the message is indicated by a decimal value.
    :ivar transaction_identifier: A unique identifier to relate all messages within a transaction (e.g. this would be sent in all request and response messages that are part of an on-going transaction).
    :ivar sequence_nmbr: Used to identify the sequence number of the transaction as assigned by the sending system; allows for an application to process messages in a certain order or to request a resynchronization of messages in the event that a system has been off-line and needs to retrieve messages that were missed.
    :ivar transaction_status_code: This indicates where this message falls within a sequence of messages.
    :ivar primary_lang_id: Identifes the primary language preference for the form of travel represented in a collection. The human language is identified by ISO 639 codes.
    :ivar alt_lang_id:
    :ivar max_responses: A positive integer value that indicates the maximum number of responses desired in the return.
    :ivar direct_flights_only: Request direct flights between given locations. This defaults to false.
    :ivar available_flights_only: Include only flights with available booking codes (when True or when attribute not present).
    :ivar response_type:
    :ivar response_version:
    :ivar separate_messages: Whether all messages should be printed in separate MTP element or not. Works only with PSS response serializers.
    :ivar truncate_messages: Whether each MTP content should be truncated to specified length or not. Works only with PSS response serializers.
    """
    class Meta:
        name = "OTA_AirLowFareSearchRQ"
        namespace = "http://www.opentravel.org/OTA/2003/05"

    pos: Optional[PosType] = field(
        default=None,
        metadata=dict(
            name="POS",
            type="Element",
            required=True
        )
    )
    origin_destination_information: List["OtaAirLowFareSearchRq.OriginDestinationInformation"] = field(
        default_factory=list,
        metadata=dict(
            name="OriginDestinationInformation",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )
    leg: List["OtaAirLowFareSearchRq.Leg"] = field(
        default_factory=list,
        metadata=dict(
            name="Leg",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    travel_preferences: Optional[AirSearchPrefsType] = field(
        default=None,
        metadata=dict(
            name="TravelPreferences",
            type="Element"
        )
    )
    traveler_info_summary: Optional[TravelerInfoSummaryType] = field(
        default=None,
        metadata=dict(
            name="TravelerInfoSummary",
            type="Element",
            required=True
        )
    )
    tpa_extensions: Optional["OtaAirLowFareSearchRq.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element"
        )
    )
    echo_token: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EchoToken",
            type="Attribute",
            min_length=1.0,
            max_length=64.0
        )
    )
    time_stamp: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TimeStamp",
            type="Attribute"
        )
    )
    target: "OtaAirLowFareSearchRq.Target" = field(
        default="Production",
        metadata=dict(
            name="Target",
            type="Attribute"
        )
    )
    version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Version",
            type="Attribute",
            required=True
        )
    )
    transaction_identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TransactionIdentifier",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    sequence_nmbr: Optional[Union[int, bool]] = field(
        default=None,
        metadata=dict(
            name="SequenceNmbr",
            type="Attribute"
        )
    )
    transaction_status_code: Optional["OtaAirLowFareSearchRq.TransactionStatusCode"] = field(
        default=None,
        metadata=dict(
            name="TransactionStatusCode",
            type="Attribute"
        )
    )
    primary_lang_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PrimaryLangID",
            type="Attribute"
        )
    )
    alt_lang_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AltLangID",
            type="Attribute"
        )
    )
    max_responses: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MaxResponses",
            type="Attribute"
        )
    )
    direct_flights_only: bool = field(
        default=False,
        metadata=dict(
            name="DirectFlightsOnly",
            type="Attribute"
        )
    )
    available_flights_only: bool = field(
        default=True,
        metadata=dict(
            name="AvailableFlightsOnly",
            type="Attribute"
        )
    )
    response_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ResponseType",
            type="Attribute"
        )
    )
    response_version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ResponseVersion",
            type="Attribute"
        )
    )
    separate_messages: bool = field(
        default=False,
        metadata=dict(
            name="SeparateMessages",
            type="Attribute"
        )
    )
    truncate_messages: bool = field(
        default=True,
        metadata=dict(
            name="TruncateMessages",
            type="Attribute"
        )
    )

    @dataclass
    class TpaExtensions:
        """
        :ivar intelli_sell_transaction:
        :ivar diversity_control:
        :ivar messaging_details:
        :ivar alternate_airport_cities: For each specified location provide an alternate location.
        :ivar alternate_airport_mileage: Specify maximum allowed distance from specified airport.
        :ivar award_shopping:
        :ivar billing:
        :ivar exchange_settings:
        :ivar exchange:
        :ivar split_taxes:
        :ivar alternate_dates_processing:
        :ivar itinerary_cache:
        :ivar multi_ticket:
        :ivar partitions:
        :ivar reservation_data:
        :ivar alternate_pcc:
        """
        intelli_sell_transaction: Optional[TransactionType] = field(
            default=None,
            metadata=dict(
                name="IntelliSellTransaction",
                type="Element"
            )
        )
        diversity_control: Optional[DiversityControlType] = field(
            default=None,
            metadata=dict(
                name="DiversityControl",
                type="Element"
            )
        )
        messaging_details: Optional["OtaAirLowFareSearchRq.TpaExtensions.MessagingDetails"] = field(
            default=None,
            metadata=dict(
                name="MessagingDetails",
                type="Element"
            )
        )
        alternate_airport_cities: List["OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportCities"] = field(
            default_factory=list,
            metadata=dict(
                name="AlternateAirportCities",
                type="Element",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        alternate_airport_mileage: Optional["OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportMileage"] = field(
            default=None,
            metadata=dict(
                name="AlternateAirportMileage",
                type="Element"
            )
        )
        award_shopping: Optional[AwardShoppingType] = field(
            default=None,
            metadata=dict(
                name="AwardShopping",
                type="Element"
            )
        )
        billing: Optional[BillingInformationType] = field(
            default=None,
            metadata=dict(
                name="Billing",
                type="Element"
            )
        )
        exchange_settings: Optional[ExchangeSettingsType] = field(
            default=None,
            metadata=dict(
                name="ExchangeSettings",
                type="Element"
            )
        )
        exchange: List[ExchangeType] = field(
            default_factory=list,
            metadata=dict(
                name="Exchange",
                type="Element",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        split_taxes: Optional["OtaAirLowFareSearchRq.TpaExtensions.SplitTaxes"] = field(
            default=None,
            metadata=dict(
                name="SplitTaxes",
                type="Element"
            )
        )
        alternate_dates_processing: Optional["OtaAirLowFareSearchRq.TpaExtensions.AlternateDatesProcessing"] = field(
            default=None,
            metadata=dict(
                name="AlternateDatesProcessing",
                type="Element"
            )
        )
        itinerary_cache: Optional["OtaAirLowFareSearchRq.TpaExtensions.ItineraryCache"] = field(
            default=None,
            metadata=dict(
                name="ItineraryCache",
                type="Element"
            )
        )
        multi_ticket: Optional["OtaAirLowFareSearchRq.TpaExtensions.MultiTicket"] = field(
            default=None,
            metadata=dict(
                name="MultiTicket",
                type="Element"
            )
        )
        partitions: Optional["OtaAirLowFareSearchRq.TpaExtensions.Partitions"] = field(
            default=None,
            metadata=dict(
                name="Partitions",
                type="Element"
            )
        )
        reservation_data: Optional["OtaAirLowFareSearchRq.TpaExtensions.ReservationData"] = field(
            default=None,
            metadata=dict(
                name="ReservationData",
                type="Element"
            )
        )
        alternate_pcc: List["OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc"] = field(
            default_factory=list,
            metadata=dict(
                name="AlternatePCC",
                type="Element",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

        @dataclass
        class MessagingDetails:
            """
            :ivar mdrsubset:
            """
            mdrsubset: Optional["OtaAirLowFareSearchRq.TpaExtensions.MessagingDetails.Mdrsubset"] = field(
                default=None,
                metadata=dict(
                    name="MDRSubset",
                    type="Element"
                )
            )

            @dataclass
            class Mdrsubset:
                """
                :ivar code:
                """
                code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Code",
                        type="Attribute"
                    )
                )

        @dataclass
        class SplitTaxes:
            """
            :ivar by_leg:
            :ivar by_fare_component:
            """
            by_leg: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="ByLeg",
                    type="Attribute"
                )
            )
            by_fare_component: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="ByFareComponent",
                    type="Attribute"
                )
            )

        @dataclass
        class AlternateDatesProcessing:
            """
            :ivar calendar_mode:
            :ivar num_options_per_alternate_date:
            """
            calendar_mode: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="CalendarMode",
                    type="Attribute"
                )
            )
            num_options_per_alternate_date: int = field(
                default=9,
                metadata=dict(
                    name="NumOptionsPerAlternateDate",
                    type="Attribute"
                )
            )

        @dataclass
        class ItineraryCache:
            """
            :ivar public_time_to_live:
            :ivar remove_previous_on_update:
            """
            public_time_to_live: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="PublicTimeToLive",
                    type="Attribute"
                )
            )
            remove_previous_on_update: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="RemovePreviousOnUpdate",
                    type="Attribute"
                )
            )

        @dataclass
        class MultiTicket:
            """
            :ivar display_policy: Display Option Policy, takes values:
            												- SOW - Show OneWays separately
            												- GOW2RT - Group OneWays and match to RoundTrip
            												- SCHS - Group OneWays, match to RoundTrip and show cheaper solution
            """
            display_policy: Optional["OtaAirLowFareSearchRq.TpaExtensions.MultiTicket.DisplayPolicy"] = field(
                default=None,
                metadata=dict(
                    name="DisplayPolicy",
                    type="Attribute"
                )
            )

            class DisplayPolicy(Enum):
                """
                :cvar GOW2_RT:
                :cvar SCHS:
                :cvar SOW:
                """
                GOW2_RT = "GOW2RT"
                SCHS = "SCHS"
                SOW = "SOW"

        @dataclass
        class Partitions:
            """
            :ivar partition:
            :ivar group:
            """
            partition: List[CachePartitionType] = field(
                default_factory=list,
                metadata=dict(
                    name="Partition",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            group: List[CachePartitionGroupType] = field(
                default_factory=list,
                metadata=dict(
                    name="Group",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )

        @dataclass
        class ReservationData:
            """
            :ivar dknumber: DK number
            """
            dknumber: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="DKNumber",
                    type="Attribute"
                )
            )

        @dataclass
        class AlternatePcc:
            """
            :ivar travel_preferences:
            :ivar pseudo_city_code: An identification code assigned to an office/agency by a reservation system.
            """
            travel_preferences: Optional["OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc.TravelPreferences"] = field(
                default=None,
                metadata=dict(
                    name="TravelPreferences",
                    type="Element"
                )
            )
            pseudo_city_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="PseudoCityCode",
                    type="Attribute",
                    required=True,
                    min_length=1.0,
                    max_length=16.0
                )
            )

            @dataclass
            class TravelPreferences:
                """
                :ivar vendor_pref:
                :ivar tpa_extensions:
                """
                vendor_pref: List["OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc.TravelPreferences.VendorPref"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="VendorPref",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                tpa_extensions: Optional["OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc.TravelPreferences.TpaExtensions"] = field(
                    default=None,
                    metadata=dict(
                        name="TPA_Extensions",
                        type="Element"
                    )
                )

                @dataclass
                class VendorPref:
                    """
                    :ivar code: Identifies a company by the company code.
                    :ivar prefer_level:
                    """
                    code: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Code",
                            type="Attribute",
                            required=True,
                            min_length=1.0,
                            max_length=8.0
                        )
                    )
                    prefer_level: PreferLevelType = field(
                        default="Preferred",
                        metadata=dict(
                            name="PreferLevel",
                            type="Attribute"
                        )
                    )

                @dataclass
                class TpaExtensions:
                    """
                    :ivar include_alliance_pref: Consider only these alliances.
                    :ivar exclude_alliance_pref: Do not consider these alliances.
                    """
                    include_alliance_pref: List[AllianceType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="IncludeAlliancePref",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )
                    exclude_alliance_pref: List[AllianceType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="ExcludeAlliancePref",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )

        @dataclass
        class AlternateAirportCities:
            """
            :ivar specified_location: A desired location (airport city).
            :ivar alternate_location: An alternate location (airport city).
            """
            specified_location: Optional["OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportCities.SpecifiedLocation"] = field(
                default=None,
                metadata=dict(
                    name="SpecifiedLocation",
                    type="Element",
                    required=True
                )
            )
            alternate_location: List["OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportCities.AlternateLocation"] = field(
                default_factory=list,
                metadata=dict(
                    name="AlternateLocation",
                    type="Element",
                    min_occurs=1,
                    max_occurs=5
                )
            )

            @dataclass
            class SpecifiedLocation:
                """
                :ivar location_code:
                """
                location_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="LocationCode",
                        type="Attribute",
                        pattern=r"[A-Z]*"
                    )
                )

            @dataclass
            class AlternateLocation:
                """
                :ivar location_code:
                """
                location_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="LocationCode",
                        type="Attribute",
                        pattern=r"[A-Z]*"
                    )
                )

        @dataclass
        class AlternateAirportMileage:
            """
            :ivar number: Maximum allowed number of miles from desired airport.
            """
            number: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Number",
                    type="Attribute",
                    required=True
                )
            )

    @dataclass
    class OriginDestinationInformation(OriginDestinationInformationType):
        """
        :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
        :ivar rph: A placeholder for OriginDestinationInformation to be referenced wihin the OTA_AirLowFareSearchRS message. PricedItineraryType carries the reference to this RPH.
        :ivar fixed: OriginDestination node with flight and fare information fixed. Used in context shopping
        :ivar full_diversity: Request for full diversity of flights for the particular OriginDestination node. Used in Exchange Context Shopping
        """
        tpa_extensions: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions"] = field(
            default=None,
            metadata=dict(
                name="TPA_Extensions",
                type="Element"
            )
        )
        rph: Optional[str] = field(
            default=None,
            metadata=dict(
                name="RPH",
                type="Attribute",
                pattern=r"[0-9]{1,8}"
            )
        )
        fixed: bool = field(
            default=False,
            metadata=dict(
                name="Fixed",
                type="Attribute"
            )
        )
        full_diversity: bool = field(
            default=False,
            metadata=dict(
                name="FullDiversity",
                type="Attribute"
            )
        )

        @dataclass
        class TpaExtensions:
            """
            :ivar flight:
            :ivar routing:
            :ivar date_flexibility: The number of alternate days around the travel date to search.
            :ivar sister_destination_location: List of alternate destination cities to search
            :ivar sister_destination_mileage:
            :ivar sister_origin_location: List of alternate origin cities to search
            :ivar sister_origin_mileage:
            :ivar segment_type:
            :ivar alternate_time: Maximum time difference/deviation allowed.
            :ivar max_one_way_options: Maximum number of options to return.
            :ivar num_one_way_options: Number of options for requested date.
            :ivar cabin_pref: Defines preferred cabin to be used in a search for this leg level (if SegmentType is "O") or segment (if SegmentType is "X"). The cabin type specified in this element will override the cabin type specified at the request level for this leg/segment. If a cabin type is not specified for this element the cabin type at request level will be used as default for this leg or segment. If the cabin type is not specified at both the leg/segment level and request level a default cabin of "Economy" will be used?
            :ivar connection_time: Connection time between segments.
            :ivar total_travel_time: Total travel time settings
            :ivar include_vendor_pref:
            :ivar include_alliance_pref: Consider only these alliances.
            :ivar departure_days:
            """
            flight: List[OriginDestinationFlightType] = field(
                default_factory=list,
                metadata=dict(
                    name="Flight",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            routing: List[RoutingDefinitionType] = field(
                default_factory=list,
                metadata=dict(
                    name="Routing",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            date_flexibility: List["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.DateFlexibility"] = field(
                default_factory=list,
                metadata=dict(
                    name="DateFlexibility",
                    type="Element",
                    min_occurs=0,
                    max_occurs=2
                )
            )
            sister_destination_location: List[RequestLocationType] = field(
                default_factory=list,
                metadata=dict(
                    name="SisterDestinationLocation",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            sister_destination_mileage: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.SisterDestinationMileage"] = field(
                default=None,
                metadata=dict(
                    name="SisterDestinationMileage",
                    type="Element"
                )
            )
            sister_origin_location: List[RequestLocationType] = field(
                default_factory=list,
                metadata=dict(
                    name="SisterOriginLocation",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            sister_origin_mileage: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.SisterOriginMileage"] = field(
                default=None,
                metadata=dict(
                    name="SisterOriginMileage",
                    type="Element"
                )
            )
            segment_type: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.SegmentType"] = field(
                default=None,
                metadata=dict(
                    name="SegmentType",
                    type="Element"
                )
            )
            alternate_time: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.AlternateTime"] = field(
                default=None,
                metadata=dict(
                    name="AlternateTime",
                    type="Element"
                )
            )
            max_one_way_options: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.MaxOneWayOptions"] = field(
                default=None,
                metadata=dict(
                    name="MaxOneWayOptions",
                    type="Element"
                )
            )
            num_one_way_options: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.NumOneWayOptions"] = field(
                default=None,
                metadata=dict(
                    name="NumOneWayOptions",
                    type="Element"
                )
            )
            cabin_pref: Optional[CabinPrefType] = field(
                default=None,
                metadata=dict(
                    name="CabinPref",
                    type="Element"
                )
            )
            connection_time: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.ConnectionTime"] = field(
                default=None,
                metadata=dict(
                    name="ConnectionTime",
                    type="Element"
                )
            )
            total_travel_time: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.TotalTravelTime"] = field(
                default=None,
                metadata=dict(
                    name="TotalTravelTime",
                    type="Element"
                )
            )
            include_vendor_pref: List[IncludeVendorPrefType] = field(
                default_factory=list,
                metadata=dict(
                    name="IncludeVendorPref",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            include_alliance_pref: List[AllianceType] = field(
                default_factory=list,
                metadata=dict(
                    name="IncludeAlliancePref",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            departure_days: Optional[DepartureDaysType] = field(
                default=None,
                metadata=dict(
                    name="DepartureDays",
                    type="Element"
                )
            )

            @dataclass
            class DateFlexibility:
                """
                :ivar nbr_of_days: Number of alternate dates before and after requested travel date.
                :ivar plus: Number of alternate dates before requested travel date.
                :ivar minus: Number of alternate dates after requested travel date.
                :ivar validate: Flag telling if dates within the specified range should be processed in the validate path.
                """
                nbr_of_days: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="NbrOfDays",
                        type="Attribute"
                    )
                )
                plus: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Plus",
                        type="Attribute"
                    )
                )
                minus: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Minus",
                        type="Attribute"
                    )
                )
                validate: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Validate",
                        type="Attribute"
                    )
                )

            @dataclass
            class SegmentType:
                """
                :ivar code: "Code" can be "ARUNK", "O" for normal, or "X" for connection.
                """
                code: Optional["OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.SegmentType.Code"] = field(
                    default=None,
                    metadata=dict(
                        name="Code",
                        type="Attribute"
                    )
                )

                class Code(Enum):
                    """
                    :cvar ARUNK: Arrival unknown
                    :cvar O: Normal
                    :cvar X: Connection. Collapses this and subsequent OriginDestinationInformation so that they are treated as single leg.
                    """
                    ARUNK = "ARUNK"
                    O = "O"
                    X = "X"

            @dataclass
            class AlternateTime:
                """
                :ivar plus_minus: Maximum time difference between actual and desired time.
                :ivar plus: Maximum number of hours after desired time.
                :ivar minus: Maximum number of hours before desired time.
                """
                plus_minus: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="PlusMinus",
                        type="Attribute",
                        min_inclusive=0.0,
                        max_inclusive=9.0
                    )
                )
                plus: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Plus",
                        type="Attribute",
                        min_inclusive=0.0,
                        max_inclusive=9.0
                    )
                )
                minus: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Minus",
                        type="Attribute",
                        min_inclusive=0.0,
                        max_inclusive=72.0
                    )
                )

            @dataclass
            class MaxOneWayOptions:
                """
                :ivar value:
                """
                value: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Value",
                        type="Attribute"
                    )
                )

            @dataclass
            class NumOneWayOptions:
                """
                :ivar number:
                """
                number: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Number",
                        type="Attribute"
                    )
                )

            @dataclass
            class ConnectionTime:
                """
                :ivar min:
                :ivar max:
                :ivar excluded_connection_begin: Excluded connection time begin in format HHMM
                :ivar excluded_connection_end: Excluded connection time end in format HHMM
                :ivar enable_excluded_connection: Enable excluded connection time (default: true)
                """
                min: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Min",
                        type="Attribute"
                    )
                )
                max: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Max",
                        type="Attribute"
                    )
                )
                excluded_connection_begin: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="ExcludedConnectionBegin",
                        type="Attribute",
                        pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
                    )
                )
                excluded_connection_end: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="ExcludedConnectionEnd",
                        type="Attribute",
                        pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
                    )
                )
                enable_excluded_connection: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="EnableExcludedConnection",
                        type="Attribute"
                    )
                )

            @dataclass
            class TotalTravelTime:
                """
                :ivar min:
                :ivar max:
                """
                min: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Min",
                        type="Attribute"
                    )
                )
                max: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Max",
                        type="Attribute"
                    )
                )

            @dataclass
            class SisterDestinationMileage:
                """
                :ivar number:
                """
                number: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Number",
                        type="Attribute"
                    )
                )

            @dataclass
            class SisterOriginMileage:
                """
                :ivar number:
                """
                number: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Number",
                        type="Attribute"
                    )
                )

    @dataclass
    class Leg:
        """
        :ivar departure_date_time:
        :ivar arrival_date_time:
        :ivar origins:
        :ivar destinations:
        :ivar connection_locations: Travel Connection Location - for example, air uses the IATA 3 letter code.
        :ivar carriers: Carrier preferrence information
        :ivar cabin: Defines preferred cabin to be used in a search for this leg level.
        :ivar rph: A placeholder for OriginDestinationInformation to be referenced wihin the OTA_AirLowFareSearchRS message. PricedItineraryType carries the reference to this RPH.
        :ivar max_options: Maximum number of options to return.
        """
        departure_date_time: Optional["OtaAirLowFareSearchRq.Leg.DepartureDateTime"] = field(
            default=None,
            metadata=dict(
                name="DepartureDateTime",
                type="Element"
            )
        )
        arrival_date_time: Optional[GlobalDateTimeType] = field(
            default=None,
            metadata=dict(
                name="ArrivalDateTime",
                type="Element"
            )
        )
        origins: Optional["OtaAirLowFareSearchRq.Leg.Origins"] = field(
            default=None,
            metadata=dict(
                name="Origins",
                type="Element",
                required=True
            )
        )
        destinations: Optional["OtaAirLowFareSearchRq.Leg.Destinations"] = field(
            default=None,
            metadata=dict(
                name="Destinations",
                type="Element",
                required=True
            )
        )
        connection_locations: Optional[ConnectionType] = field(
            default=None,
            metadata=dict(
                name="ConnectionLocations",
                type="Element"
            )
        )
        carriers: Optional["OtaAirLowFareSearchRq.Leg.Carriers"] = field(
            default=None,
            metadata=dict(
                name="Carriers",
                type="Element"
            )
        )
        cabin: Optional["OtaAirLowFareSearchRq.Leg.Cabin"] = field(
            default=None,
            metadata=dict(
                name="Cabin",
                type="Element"
            )
        )
        rph: Optional[str] = field(
            default=None,
            metadata=dict(
                name="RPH",
                type="Attribute",
                required=True,
                pattern=r"[0-9]{1,8}"
            )
        )
        max_options: Optional[int] = field(
            default=None,
            metadata=dict(
                name="MaxOptions",
                type="Attribute"
            )
        )

        @dataclass
        class Origins:
            """
            :ivar origin:
            """
            origin: List["OtaAirLowFareSearchRq.Leg.Origins.Origin"] = field(
                default_factory=list,
                metadata=dict(
                    name="Origin",
                    type="Element",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class Origin:
                """
                :ivar connection_locations: Travel Connection Location - for example, air uses the IATA 3 letter code.
                :ivar carriers: Carrier preferrence information
                :ivar departure_date_time_override: Overrides DepartureDateTime attributes
                :ivar airport_code: Required unless AirportsGroup is specified. Cannot appear with AirportsGroup.
                :ivar airports_group: Name of the airports group
                """
                connection_locations: Optional[ConnectionType] = field(
                    default=None,
                    metadata=dict(
                        name="ConnectionLocations",
                        type="Element"
                    )
                )
                carriers: Optional["OtaAirLowFareSearchRq.Leg.Origins.Origin.Carriers"] = field(
                    default=None,
                    metadata=dict(
                        name="Carriers",
                        type="Element"
                    )
                )
                departure_date_time_override: Optional[OverrideDateTimeType] = field(
                    default=None,
                    metadata=dict(
                        name="DepartureDateTimeOverride",
                        type="Element"
                    )
                )
                airport_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="AirportCode",
                        type="Attribute",
                        min_length=1.0,
                        max_length=8.0
                    )
                )
                airports_group: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="AirportsGroup",
                        type="Attribute"
                    )
                )

                @dataclass
                class Carriers:
                    """
                    :ivar include_vendor_pref:
                    :ivar exclude_vendor_pref: Do not consider these carriers for this leg.
                    """
                    include_vendor_pref: List[IncludeVendorPrefType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="IncludeVendorPref",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )
                    exclude_vendor_pref: List["OtaAirLowFareSearchRq.Leg.Origins.Origin.Carriers.ExcludeVendorPref"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="ExcludeVendorPref",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )

                    @dataclass
                    class ExcludeVendorPref:
                        """
                        :ivar code: Identifies a company by the company code.
                        """
                        code: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="Code",
                                type="Attribute",
                                required=True,
                                min_length=1.0,
                                max_length=8.0
                            )
                        )

        @dataclass
        class Destinations:
            """
            :ivar destination:
            """
            destination: List["OtaAirLowFareSearchRq.Leg.Destinations.Destination"] = field(
                default_factory=list,
                metadata=dict(
                    name="Destination",
                    type="Element",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class Destination:
                """
                :ivar connection_locations: Travel Connection Location - for example, air uses the IATA 3 letter code.
                :ivar carriers: Carrier preferrence information
                :ivar arrival_date_time_override: Overrides ArrivalDateTime attributes
                :ivar airport_code: Required unless AirportsGroup is specified. Cannot appear with AirportsGroup.
                :ivar airports_group: Name of the airports group
                """
                connection_locations: Optional[ConnectionType] = field(
                    default=None,
                    metadata=dict(
                        name="ConnectionLocations",
                        type="Element"
                    )
                )
                carriers: Optional["OtaAirLowFareSearchRq.Leg.Destinations.Destination.Carriers"] = field(
                    default=None,
                    metadata=dict(
                        name="Carriers",
                        type="Element"
                    )
                )
                arrival_date_time_override: Optional[OverrideDateTimeType] = field(
                    default=None,
                    metadata=dict(
                        name="ArrivalDateTimeOverride",
                        type="Element"
                    )
                )
                airport_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="AirportCode",
                        type="Attribute",
                        min_length=1.0,
                        max_length=8.0
                    )
                )
                airports_group: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="AirportsGroup",
                        type="Attribute"
                    )
                )

                @dataclass
                class Carriers:
                    """
                    :ivar include_vendor_pref:
                    :ivar exclude_vendor_pref: Do not consider these carriers for this leg.
                    """
                    include_vendor_pref: List[IncludeVendorPrefType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="IncludeVendorPref",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )
                    exclude_vendor_pref: List["OtaAirLowFareSearchRq.Leg.Destinations.Destination.Carriers.ExcludeVendorPref"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="ExcludeVendorPref",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )

                    @dataclass
                    class ExcludeVendorPref:
                        """
                        :ivar code: Identifies a company by the company code.
                        """
                        code: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="Code",
                                type="Attribute",
                                required=True,
                                min_length=1.0,
                                max_length=8.0
                            )
                        )

        @dataclass
        class Carriers:
            """
            :ivar include_vendor_pref:
            :ivar exclude_vendor_pref: Do not consider these carriers for this leg.
            """
            include_vendor_pref: List[IncludeVendorPrefType] = field(
                default_factory=list,
                metadata=dict(
                    name="IncludeVendorPref",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            exclude_vendor_pref: List["OtaAirLowFareSearchRq.Leg.Carriers.ExcludeVendorPref"] = field(
                default_factory=list,
                metadata=dict(
                    name="ExcludeVendorPref",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class ExcludeVendorPref:
                """
                :ivar code: Identifies a company by the company code.
                """
                code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Code",
                        type="Attribute",
                        required=True,
                        min_length=1.0,
                        max_length=8.0
                    )
                )

        @dataclass
        class Cabin:
            """
            :ivar preference_level:
            :ivar type: Specifies cabin type.
            """
            preference_level: PreferLevelType = field(
                default="Preferred",
                metadata=dict(
                    name="PreferenceLevel",
                    type="Attribute"
                )
            )
            type: Optional[CabinType] = field(
                default=None,
                metadata=dict(
                    name="Type",
                    type="Attribute"
                )
            )

        @dataclass
        class DepartureDateTime(GlobalDateTimeType):
            """
            :ivar week_days: Specify which days of week  to consider for departure. Value format: First letter of the name of the day or '_', eg. 'SMT___S' means we are interested in departing at Saturday, Sunday, Monday or Tuesday. Even if there are schedules for Wednesday, Thursday or Friday, they won't be returned in ISell response.
            """
            week_days: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="WeekDays",
                    type="Attribute",
                    length=7
                )
            )

    class Target(Enum):
        """
        :cvar PRODUCTION:
        :cvar TEST:
        """
        PRODUCTION = "Production"
        TEST = "Test"

    class TransactionStatusCode(Enum):
        """
        :cvar END: This is the last message within a transaction.
        :cvar IN_SERIES: This is any message that is not the first or last message within a transaction.
        :cvar ROLLBACK: This indicates that all messages within the current transaction must be ignored.
        :cvar START: This is the first message within a transaction.
        """
        END = "End"
        IN_SERIES = "InSeries"
        ROLLBACK = "Rollback"
        START = "Start"
