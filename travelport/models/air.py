from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlTime
from travelport.models.common import (
    AccountCode,
    AddSvc,
    AgencyInfo,
    AgencySellInfo,
    AirExchangeInfo,
    AirSeatAssignment,
    Airport,
    BaseAsyncProviderSpecificResponse,
    BaseCoreReq,
    BaseCoreSearchReq,
    BaseReq,
    BaseReservation,
    BaseRsp,
    BaseSearchReq,
    BaseSearchRsp,
    BookingTraveler,
    BookingTravelerRef,
    CabinClass,
    Carrier,
    Commission,
    ConnectionPoint,
    CreditCardAuth,
    DiscountCard,
    Distance,
    Email,
    Endorsement,
    FormOfPayment,
    FormOfPaymentRef,
    HostToken,
    IndustryStandardSsr,
    LoyaltyCard,
    LoyaltyProgram,
    Mco,
    Mcoinformation,
    MetaData,
    Name,
    OverridePcc,
    Payment,
    PaymentRestriction,
    Penalty as CommonPenalty,
    PhoneNumber,
    PointOfCommencement,
    PointOfSale,
    Provider,
    ProviderReservationDetail,
    ProviderReservationInfoRef,
    RefundRemark,
    Remark,
    ResponseMessage,
    Restriction as CommonRestriction,
    Ssr,
    Ssrinfo,
    SearchPassenger,
    Segment,
    ServiceData,
    ServiceFeeInfo,
    ServiceInfo,
    ServiceRuleType,
    SupplierLocator,
    ThirdPartyInformation,
    AttrDocumentDocumentType,
    TypeAdjustmentTarget,
    TypeAdjustmentType,
    TypeAssociatedRemarkWithSegmentRef,
    TypeDistance,
    TypeElementStatus,
    TypeErrorInfo,
    TypeFeeInfo,
    TypeFlexibleTimeSpec,
    TypeFormOfRefund,
    TypeItineraryCode,
    TypeLocation,
    TypePassengerType,
    TypePriceClassOfService,
    TypePricingType,
    TypePurchaseWindow,
    TypeReqSeat,
    TypeResultMessage,
    TypeSearchLocation,
    TypeSegmentRef as CommonTypeSegmentRef,
    TypeStructuredAddress,
    TypeTaxInfo,
    TypeTicketStatus,
    TypeTimeSpec,
)
from travelport.models.rail import (
    RailFareIdlist,
    RailFareList,
    RailFareNoteList,
    RailJourneyList,
    RailPricingSolution,
    RailSegmentList,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class Advtype:
    """
    Parameters
    ----------
    adv_rsvn_only_if_tk: Reservation only if ticketed. True is advanced
        reservations only if tickets. False is no advanced reservations
    adv_rsvn_any_tm: Reservation anytime. True if advanced reservatiosn
        anytime. False if advanced reservations for a limited time.
    adv_rsvn_hrs: Reservation hours. True if advanced reservation time
        in hours. False if advanced reservation time not in hours.
    adv_rsvn_days: Reservation days. True if advanced reservation time
        in days. False if advanced reservation time not in days.
    adv_rsvn_months: Reservation months. True if advanced reservation
        time in months. False if advanced reservation time not in
        months.
    adv_rsvn_earliest_tm: Earliest reservation time. True if advanced
        reservations time is earliest permitted. False is advanced
        reservation time not earliest permitted time.
    adv_rsvn_latest_tm: Latest reservation time. True if advanced
        reservations time is latest permitted. False is advanced
        reservation time not latest permitted time.
    adv_rsvn_waived: Reservation Waived. True if advanced reservation
        waived. False if advanced reservation not waived.
    adv_rsvn_data_exists: Reservation data exists. True if advanced
        reservation data exists. False if advanced reservation data does
        not exist.
    adv_rsvn_end_item: Reservation end item. True if advanced
        reservation end item and more values. False if it does not
        exist.
    adv_tk_earliest_tm: Earliest ticketing time. True if earliest
        permitted. False if not earliest permitted.
    adv_tk_latest_tm: Latest ticketing time. True if time is latest
        permitted. False if time is not latest permitted.
    adv_tk_rsvn_hrs: Ticketing reservation hours. True if in hours.
        False if not in hours.
    adv_tk_rsvn_days: Ticketing reservation days. True if in days. False
        if not in days.
    adv_tk_rsvn_months: Ticketing reservation months. True if in months.
        False if not in months.
    adv_tk_start_hrs: Latest ticketing departure. True if time is latest
        permitted. False if time is not latest permitted.
    adv_tk_start_days: Ticketing departure days. True if in days. False
        if not in days.
    adv_tk_start_months: Ticketing reservation months. True if in
        months. False if not in months.
    adv_tk_waived: Ticketing waived. True if waived. False if not
        waived.
    adv_tk_any_tm: Ticketing anytime. True if anytime. False if limited
        time.
    adv_tk_end_item: Ticketing end item. True if advanced ticketing item
        and more values. False if end item does not exist.
    adv_rsvn_tm: Advanced reservation time.
    adv_tk_rsvn_tm: Advanced ticketing reservation time.
    adv_tk_start_tm: Advanced ticketing departure time.
    earliest_rsvn_dt_present: Earliest reservation date. True if date is
        present. False if date is not present.
    earliest_tk_dt_present: Earliest ticketing date. True if date is
        present. False if date is not present.
    latest_rsvn_dt_present: Latest reservation date. True if date is
        present. False if date is not present.
    latest_tk_dt_present: Latest ticketing date.  True if date is
        present. False if date is not present.
    earliest_rsvn_dt: Earliest reservation date.
    earliest_tk_dt: Earliest ticketing date.
    latest_rsvn_dt: Latest reservation date.
    latest_tk_dt: Latest ticketing date.
    """
    class Meta:
        name = "ADVType"

    adv_rsvn_only_if_tk: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvRsvnOnlyIfTk",
            "type": "Attribute",
        }
    )
    adv_rsvn_any_tm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvRsvnAnyTm",
            "type": "Attribute",
        }
    )
    adv_rsvn_hrs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvRsvnHrs",
            "type": "Attribute",
        }
    )
    adv_rsvn_days: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvRsvnDays",
            "type": "Attribute",
        }
    )
    adv_rsvn_months: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvRsvnMonths",
            "type": "Attribute",
        }
    )
    adv_rsvn_earliest_tm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvRsvnEarliestTm",
            "type": "Attribute",
        }
    )
    adv_rsvn_latest_tm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvRsvnLatestTm",
            "type": "Attribute",
        }
    )
    adv_rsvn_waived: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvRsvnWaived",
            "type": "Attribute",
        }
    )
    adv_rsvn_data_exists: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvRsvnDataExists",
            "type": "Attribute",
        }
    )
    adv_rsvn_end_item: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvRsvnEndItem",
            "type": "Attribute",
        }
    )
    adv_tk_earliest_tm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkEarliestTm",
            "type": "Attribute",
        }
    )
    adv_tk_latest_tm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkLatestTm",
            "type": "Attribute",
        }
    )
    adv_tk_rsvn_hrs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnHrs",
            "type": "Attribute",
        }
    )
    adv_tk_rsvn_days: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnDays",
            "type": "Attribute",
        }
    )
    adv_tk_rsvn_months: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnMonths",
            "type": "Attribute",
        }
    )
    adv_tk_start_hrs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkStartHrs",
            "type": "Attribute",
        }
    )
    adv_tk_start_days: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkStartDays",
            "type": "Attribute",
        }
    )
    adv_tk_start_months: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkStartMonths",
            "type": "Attribute",
        }
    )
    adv_tk_waived: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkWaived",
            "type": "Attribute",
        }
    )
    adv_tk_any_tm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkAnyTm",
            "type": "Attribute",
        }
    )
    adv_tk_end_item: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTkEndItem",
            "type": "Attribute",
        }
    )
    adv_rsvn_tm: Optional[int] = field(
        default=None,
        metadata={
            "name": "AdvRsvnTm",
            "type": "Attribute",
        }
    )
    adv_tk_rsvn_tm: Optional[int] = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnTm",
            "type": "Attribute",
        }
    )
    adv_tk_start_tm: Optional[int] = field(
        default=None,
        metadata={
            "name": "AdvTkStartTm",
            "type": "Attribute",
        }
    )
    earliest_rsvn_dt_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EarliestRsvnDtPresent",
            "type": "Attribute",
        }
    )
    earliest_tk_dt_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EarliestTkDtPresent",
            "type": "Attribute",
        }
    )
    latest_rsvn_dt_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LatestRsvnDtPresent",
            "type": "Attribute",
        }
    )
    latest_tk_dt_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LatestTkDtPresent",
            "type": "Attribute",
        }
    )
    earliest_rsvn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarliestRsvnDt",
            "type": "Attribute",
        }
    )
    earliest_tk_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarliestTkDt",
            "type": "Attribute",
        }
    )
    latest_rsvn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatestRsvnDt",
            "type": "Attribute",
        }
    )
    latest_tk_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatestTkDt",
            "type": "Attribute",
        }
    )


@dataclass
class ActionDetails:
    """
    Information related to the storing of the fare: Agent, Date and Action for
    Provider: 1P/1J.

    Parameters
    ----------
    pseudo_city_code: PCC in the host of the agent who stored the fare
        for Provider: 1P/1J
    agent_sine: The sign in of the user who stored the fare for
        Provider: 1P/1J
    event_date: Date at which the fare was stored for Provider: 1P/1J
    event_time: Time at which the fare was stored for Provider: 1P/1J
    text: The type of action the agent performed for Provider: 1P/1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    agent_sine: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentSine",
            "type": "Attribute",
        }
    )
    event_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EventDate",
            "type": "Attribute",
        }
    )
    event_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EventTime",
            "type": "Attribute",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        }
    )


@dataclass
class AdditionalInfo:
    """
    Parameters
    ----------
    category: The category code is the code the AdditionalInfo text came
        from, e.g. S5 or S7.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AddlBookingCodeInformation:
    """
    Returns additional booking codes for the selected fare.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
        }
    )


@dataclass
class Adjustment:
    """An indentifier which indentifies adjustment made on original pricing.

    It can a flat amount or percentage of original price. The value of
    Amount/Percent can be negetive. Negative value implies a discount.

    Parameters
    ----------
    amount: Implies a flat amount to be adjusted. Negetive value implies
        a discount.
    percent: Implies an adjustment to be made on original price.
        Negetive value implies a discount.
    adjusted_total_price: The adjusted price after applying adjustment
        on Total price
    approximate_adjusted_total_price: The Converted adjusted total price
        in Default Currency for this entity.
    booking_traveler_ref: Reference to a booking traveler for which
        adjustment is applied.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
        }
    )
    percent: Optional[float] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
        }
    )
    adjusted_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdjustedTotalPrice",
            "type": "Attribute",
            "required": True,
        }
    )
    approximate_adjusted_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateAdjustedTotalPrice",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class AirFareDisplayRuleKey:
    """The Tariff Fare Rule requested using a Key.

    The key is typically a provider specific string which is required to
    make either a following Air Fare Tariff request for Mileage/Routing
    information or Air Fare Tariff Rule Request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )


@dataclass
class AirItinerarySolutionRef:
    """
    Reference to a complete AirItinerarySolution from a shared list.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class AirLegModifiersOrderBy(Enum):
    JOURNEY_TIME = "JourneyTime"
    DEPARTURE_TIME = "DepartureTime"
    ARRIVAL_TIME = "ArrivalTime"


@dataclass
class AirPricingInfoRef:
    """
    Reference to a AirPricing from a shared list.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class AirPricingSolutionItinerary(Enum):
    NEW = "New"
    ORIGINAL = "Original"


class AirRefundBundleRefundType(Enum):
    AUTO = "Auto"
    MANUAL = "Manual"


@dataclass
class AirRefundModifiers:
    """
    Provides controls and switches for the Refund process.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    refund_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundDate",
            "type": "Attribute",
        }
    )
    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        }
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        }
    )


@dataclass
class AirReservationLocatorCode:
    """
    Identifies the AirReservation LocatorCode within the Universal Record.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )


@dataclass
class AirSearchAsynchModifiers:
    """
    Controls and switches for the Air Search request for Asynch Request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    initial_asynch_result: Optional["AirSearchAsynchModifiers.InitialAsynchResult"] = field(
        default=None,
        metadata={
            "name": "InitialAsynchResult",
            "type": "Element",
        }
    )

    @dataclass
    class InitialAsynchResult:
        """
        Parameters
        ----------
        max_wait: Max wait time in seconds.
        """
        max_wait: Optional[int] = field(
            default=None,
            metadata={
                "name": "MaxWait",
                "type": "Attribute",
            }
        )


class AirSearchModifiersOrderBy(Enum):
    JOURNEY_TIME = "JourneyTime"
    DEPARTURE_TIME = "DepartureTime"
    ARRIVAL_TIME = "ArrivalTime"


@dataclass
class AirSegmentRef:
    """
    Reference to a complete AirSegment from a shared list.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AirSegmentTicketingModifiers:
    """Specifies modifiers that a particular segment should be priced with.

    If this is used, then there must be one for each AirSegment in the
    AirItinerary.

    Parameters
    ----------
    air_segment_ref:
    brand_tier: Modifier to price by specific brand tier number.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Attribute",
        }
    )
    brand_tier: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandTier",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        }
    )


class AirSolutionChangedInfoReasonCode(Enum):
    PRICE = "Price"
    SCHEDULE = "Schedule"
    BOTH = "Both"


@dataclass
class Alliance:
    """
    Alliance Code.

    Parameters
    ----------
    code: The possible values are *A for Star Alliance,*O for One
        world,*S for Sky team etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AlternateLocationDistanceRef:
    """
    Reference to a AlternateLocationDistance.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BookingCode:
    """
    The Booking Code (Class of Service) for a segment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 2,
        }
    )


@dataclass
class BookingCodeInfo:
    """Details Cabin class info and class of service information with
    availability counts.

    Only provided on search results and grouped by Cabin class

    Parameters
    ----------
    cabin_class: Specifies Cabin class for a group of class of services.
        Cabin class is not identified if it is not present.
    booking_counts: Lists class of service and their counts for specific
        cabin class
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        }
    )
    booking_counts: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingCounts",
            "type": "Attribute",
        }
    )


@dataclass
class BookingInfo:
    """
    Links segments and fares together.

    Parameters
    ----------
    booking_code:
    booking_count: Seat availability of the BookingCode
    cabin_class:
    fare_info_ref:
    segment_ref:
    coupon_ref: The coupon to which that booking is relative (if
        applicable)
    air_itinerary_solution_ref: Reference to an Air Itinerary Solution
    host_token_ref: HostToken Reference for this segment and fare
        combination.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingCode",
            "type": "Attribute",
            "required": True,
        }
    )
    booking_count: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingCount",
            "type": "Attribute",
        }
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        }
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
            "required": True,
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
    coupon_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CouponRef",
            "type": "Attribute",
        }
    )
    air_itinerary_solution_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirItinerarySolutionRef",
            "type": "Attribute",
        }
    )
    host_token_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        }
    )


@dataclass
class BookingRulesFareReference:
    """Fare Reference associated with the BookingRules.

    Containing a text container for vendor response text.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    ticket_designator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketDesignatorCode",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        }
    )
    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        }
    )
    upgrage_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UpgrageAllowed",
            "type": "Attribute",
        }
    )
    upgrade_class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "UpgradeClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )


@dataclass
class BrandId:
    """
    Brand ids for Merchandising details.
    """
    class Meta:
        name = "BrandID"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BrandInfo:
    """
    Commercially recognized product offered by an airline.

    Parameters
    ----------
    key: Brand Key
    brand_id: The unique identifier of the brand
    air_pricing_info_ref: A reference to a AirPricing. Providers: ACH,
        1G, 1V, 1P, 1J.
    fare_info_ref: A reference to a FareInfo. Providers: ACH, 1G, 1V,
        1P, 1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 19,
        }
    )
    air_pricing_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Attribute",
        }
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        }
    )


@dataclass
class BrandModifiers:
    """
    Used to specify the level of branding requested.

    Parameters
    ----------
    fare_family_display: Used to request a fare family display.
    basic_details_only: Used to request basic details of the brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_family_display: Optional["BrandModifiers.FareFamilyDisplay"] = field(
        default=None,
        metadata={
            "name": "FareFamilyDisplay",
            "type": "Element",
        }
    )
    basic_details_only: Optional["BrandModifiers.BasicDetailsOnly"] = field(
        default=None,
        metadata={
            "name": "BasicDetailsOnly",
            "type": "Element",
        }
    )

    @dataclass
    class FareFamilyDisplay:
        """
        Parameters
        ----------
        modifier_type: "FareFamily" returns the lowest branded fares in
            a fare family. "MaintainBookingCode" attempts to return the
            lowest branded fare in a fare family display based on the
            permitted booking code. Any brand that does not have a fare
            for the permitted booking code will then have the lowest
            fare returned. "LowestFareInBrand" returns the lowest fare
            within each branded fare in a fare family display.
        """
        modifier_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "ModifierType",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class BasicDetailsOnly:
        return_basic_details: Optional[bool] = field(
            default=None,
            metadata={
                "name": "ReturnBasicDetails",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class Co2Emission:
    """
    Carbon emission values.

    Parameters
    ----------
    air_segment_ref: The segment reference
    value: The CO2 emission value for the air segment
    """
    class Meta:
        name = "CO2Emission"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Attribute",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        }
    )


@dataclass
class CarrierCode:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 2,
        }
    )


@dataclass
class CarrierList:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CarrierCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 6,
            "length": 2,
        }
    )
    include_carrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeCarrier",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CodeshareInfo:
    """
    Describes the codeshare disclosure (simple text string) or the specific
    operating flight information (as attributes).

    Parameters
    ----------
    value:
    operating_carrier: The actual carrier that is operating the flight.
    operating_flight_number: The actual flight number of the carrier
        that is operating the flight.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    operating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    operating_flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatingFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )


@dataclass
class CompanyName:
    """
    Supplier info that is specific to the Unique Id.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )


@dataclass
class ContractCode:
    """
    Some private fares (non-ATPCO) are secured to a contract code.

    Parameters
    ----------
    code: The 1-64 character string which uniquely identifies a
        Contract.
    company_name: Providers supported : ACH
    provider_code:
    supplier_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )
    company_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )


@dataclass
class CreditSummary:
    """
    Credit summary associated with the account.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "length": 3,
        }
    )
    current_balance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurrentBalance",
            "type": "Attribute",
            "required": True,
        }
    )
    initial_credit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InitialCredit",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CustomerReceiptInfo:
    """Information about customer receipt via email.

    Supported providers are 1V/1G/1P/1J

    Parameters
    ----------
    booking_traveler_ref: Refererence of the Booking Traveler related to
        the email.
    email_ref: Reference to the email address used for receipt of EMD.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )
    email_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CustomerSearch:
    """
    Detailed customer information for searching pre pay profiles.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


class DirectionInfoDirection(Enum):
    TO = "To"
    FROM = "From"


@dataclass
class Document:
    """
    APIS Document Details.

    Parameters
    ----------
    sequence: Sequence number for the document.
    type: Type of the Document. Visa, Passport, DriverLicense etc.
    level: Applicability level of the Document. Required, Supported,
        API_Supported or Unknown.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    sequence: Optional[int] = field(
        default=None,
        metadata={
            "name": "Sequence",
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
    level: Optional[str] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
        }
    )


@dataclass
class DocumentModifiers:
    """
    Parameters
    ----------
    generate_itinerary_invoice: Generate itinerary/invoice documents
        along with ticket
    generate_accounting_interface: Generate interface message along with
        ticket
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    generate_itinerary_invoice: bool = field(
        default=False,
        metadata={
            "name": "GenerateItineraryInvoice",
            "type": "Attribute",
        }
    )
    generate_accounting_interface: bool = field(
        default=False,
        metadata={
            "name": "GenerateAccountingInterface",
            "type": "Attribute",
        }
    )


@dataclass
class DocumentOptions:
    """
    Allows an agency to set different document options for the itinerary.

    Parameters
    ----------
    passenger_receipt_override:
    override_option: Allows an agency to override print options for
        documents during document generation.
    suppress_itinerary_remarks: True when itinerary remarks are
        suppressed.
    generate_itin_numbers: True when itinerary numbers are system
        generated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    passenger_receipt_override: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerReceiptOverride",
            "type": "Element",
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    override_option: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OverrideOption",
            "type": "Element",
            "max_occurs": 999,
            "max_length": 50,
        }
    )
    suppress_itinerary_remarks: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SuppressItineraryRemarks",
            "type": "Attribute",
        }
    )
    generate_itin_numbers: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GenerateItinNumbers",
            "type": "Attribute",
        }
    )


@dataclass
class DocumentRequired:
    """
    Additional Details, Documents , Project IDs.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    doc_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocType",
            "type": "Attribute",
        }
    )
    include_exclude_use_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeExcludeUseInd",
            "type": "Attribute",
        }
    )
    doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocId",
            "type": "Attribute",
        }
    )
    allowed_ids: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllowedIds",
            "type": "Attribute",
        }
    )


@dataclass
class Emdendorsement:
    """Endorsement for EMD.

    Supported providers are 1V/1G/1P/1J
    """
    class Meta:
        name = "EMDEndorsement"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass
class EmdtravelerInfo:
    """EMD traveler information.

    Supported providers are 1G/1V/1P/1J

    Parameters
    ----------
    name_info: Name information of the EMD traveler.
    traveler_type: Defines the type of traveler used for booking which
        could be a non-defining type (Companion, Web-fare, etc), or a
        standard type (Adult, Child, etc).
    age: Age of the traveler
    """
    class Meta:
        name = "EMDTravelerInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    name_info: Optional["EmdtravelerInfo.NameInfo"] = field(
        default=None,
        metadata={
            "name": "NameInfo",
            "type": "Element",
            "required": True,
        }
    )
    traveler_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        }
    )

    @dataclass
    class NameInfo:
        """
        Parameters
        ----------
        prefix: Name prefix.
        first: First Name.
        middle: Midle name.
        last: Last Name.
        suffix: Name suffix.
        """
        prefix: Optional[str] = field(
            default=None,
            metadata={
                "name": "Prefix",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 20,
            }
        )
        first: Optional[str] = field(
            default=None,
            metadata={
                "name": "First",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 256,
            }
        )
        middle: Optional[str] = field(
            default=None,
            metadata={
                "name": "Middle",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 256,
            }
        )
        last: Optional[str] = field(
            default=None,
            metadata={
                "name": "Last",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 256,
            }
        )
        suffix: Optional[str] = field(
            default=None,
            metadata={
                "name": "Suffix",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 256,
            }
        )


class EmdAvailabilityChargeIndicator(Enum):
    X = "X"
    E = "E"
    F = "F"
    G = "G"
    H = "H"


class EmdRefundReissueIndicator(Enum):
    REFUNDABLE = "Refundable"
    NON_REFUNDABLE = "NonRefundable"
    REUSE = "Reuse"


@dataclass
class Embargo:
    """Embargo details.

    Provider: 1G, 1V, 1P, 1J

    Parameters
    ----------
    key:
    carrier:
    segment_ref:
    name: The commercial name of the optional service on which the
        embargo applies. Provider: 1G, 1V, 1P, 1J
    text: Brief description of the embargo. Provider: 1G, 1V, 1P, 1J
    secondary_type: The secondary type of the optional service on which
        the embargo applies.  Provider: 1G, 1V, 1P, 1J
    type: The type of optional service on which the embargo applies.
        Provider: 1G, 1V, 1P, 1J
    url: Website of the operating carrier. Provider: 1G, 1V, 1P, 1J
    service_sub_code: The service sub code of the optional service on
        which the embargo applies.  Provider: 1G, 1V, 1P, 1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "max_length": 30,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        }
    )
    secondary_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecondaryType",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Attribute",
        }
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "max_length": 3,
        }
    )


@dataclass
class ExchangedTicketInfo:
    """
    Contains Exchanged/Reissued Ticket Information.

    Parameters
    ----------
    number: Original Ticket that was Exchange/Reissued
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "length": 13,
        }
    )


@dataclass
class ExcludeTicketing:
    """Exclude ticketing of traveler referenced.

    Supported Provider: JAL.

    Parameters
    ----------
    booking_traveler_ref: Reference to a booking traveler for which
        ticketing modifier is applied.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class ExemptObfee:
    """
    Used to specify which OB fees are exempt; if none are listed, it means all
    should be exempt.
    """
    class Meta:
        name = "ExemptOBFee"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    sub_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SubCode",
            "type": "Element",
            "max_occurs": 8,
        }
    )


@dataclass
class ExemptTaxes:
    """
    Request tax exemption for specific tax category and/or all taxes of a
    specific country.

    Parameters
    ----------
    country_code: Specify ISO country code for which tax exemption is
        requested.
    tax_category: Specify tax category for which tax exemption is
        requested.
    all_taxes: Request exemption of all taxes.
    tax_territory: exemption is achieved by sending in the TaxTerritory
        in the tax exempt price request.
    company_name: The federal government body name must be provided in
        this element. This field is required by AC
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    country_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CountryCode",
            "type": "Element",
            "max_occurs": 999,
            "length": 2,
        }
    )
    tax_category: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    all_taxes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllTaxes",
            "type": "Attribute",
        }
    )
    tax_territory: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTerritory",
            "type": "Attribute",
            "length": 2,
        }
    )
    company_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 24,
        }
    )


@dataclass
class FareBasis:
    """
    Fare Basis Code.

    Parameters
    ----------
    code: The fare basis code for this fare
    segment_ref: The segment to which this FareBasis Code is to
        connected
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )


@dataclass
class FareCalc:
    """
    The complete fare calculation line.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class FareDetailsRef:
    """
    Reference of the Fare.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FareInfoMessage:
    """A simple textual fare information message.Providers supported : 1G/1V/1P/1J"""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FareInfoRef:
    """
    Reference to a complete FareInfo from a shared list.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FareMileageInformation:
    """
    Contains Fare/Tariff Display Mileage Information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class FareNoteRef:
    """A reference to a fare note from a shared list.

    Used to minimize xml results.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FarePricing:
    """Container for Fare Pricing Information.

    One per PTC type.

    Parameters
    ----------
    passenger_type:
    total_fare_amount:
    private_fare: NegotiatedFare attribute from earlier version of
        schema used to imply whether the fare is private fare or not.
        So, this attribute is renamed to PrivateFare as it best suited.
    negotiated_fare: Identifies the fare as a Negotiated Fare.
    auto_priceable: Identifies the fare as Autopriceable or not. False
        value means the fare filing is incomplete and the fare should
        not be used.
    total_net_fare_amount: Total Net fare amount.
    base_fare: Base fare amount.
    taxes:
    mmid: Contains the Reference id which is generated when the request
        was ReturnMM=”true”.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    passenger_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    total_fare_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalFareAmount",
            "type": "Attribute",
        }
    )
    private_fare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrivateFare",
            "type": "Attribute",
        }
    )
    negotiated_fare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NegotiatedFare",
            "type": "Attribute",
        }
    )
    auto_priceable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoPriceable",
            "type": "Attribute",
        }
    )
    total_net_fare_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNetFareAmount",
            "type": "Attribute",
        }
    )
    base_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    mmid: Optional[str] = field(
        default=None,
        metadata={
            "name": "MMid",
            "type": "Attribute",
        }
    )


@dataclass
class FareRemarkRef:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class FareRestrictionDateEndDateIndicator(Enum):
    COMMENCE = "Commence"
    COMPLETE = "Complete"


@dataclass
class FareRestrictionSaleDate:
    """
    Restrict when this fare can be sold.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        }
    )


@dataclass
class FareRestrictionSeasonal:
    """Fares Restricted based on the season requested.

    StartDate and EndDate are strings representing respective dates. If
    a year component is present then it signifies an exact date. If only
    day and month components are present then it signifies a seasonal
    date, which means applicable for that date in any year
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Attribute",
        }
    )
    variation_by_travel_dates: Optional[str] = field(
        default=None,
        metadata={
            "name": "VariationByTravelDates",
            "type": "Attribute",
        }
    )
    seasonal_range1_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeasonalRange1Ind",
            "type": "Attribute",
        }
    )
    seasonal_range1_start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeasonalRange1StartDate",
            "type": "Attribute",
        }
    )
    seasonal_range1_end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeasonalRange1EndDate",
            "type": "Attribute",
        }
    )
    seasonal_range2_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeasonalRange2Ind",
            "type": "Attribute",
        }
    )
    seasonal_range2_start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeasonalRange2StartDate",
            "type": "Attribute",
        }
    )
    seasonal_range2_end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeasonalRange2EndDate",
            "type": "Attribute",
        }
    )


@dataclass
class FareRoutingInformation:
    """
    Contains Fare/Tariff Display Routing Information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class FareRuleCategory:
    """
    Rule Categories to filter on.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    category: Optional[int] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 50,
        }
    )


@dataclass
class FareRuleFailureInfo:
    """
    Returns fare rule failure reason codes when fare basis code is forced.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    reason: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class FareRuleKey:
    """The Fare Rule requested using a Key.

    The key is typically a provider specific string which is required to
    make a following Air Fare Rule Request. This Key is returned in Low
    Fare Shop or Air Price Response

    Parameters
    ----------
    value:
    fare_info_ref: The Fare Component to which this Rule Key applies
    provider_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )


@dataclass
class FareRuleLong:
    """
    Long Text Fare Rule.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    category: Optional[int] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
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
class FareRuleLongRef:
    """
    A reference to an Long Text Rule in a Shared List.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FareRuleNameValue:
    """
    Fare Rule Name Value Pair, used in Short Rules.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

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
            "required": True,
        }
    )


@dataclass
class FareRuleShortRef:
    """
    A reference to an Short Text Rule in a Shared List.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FareRulesFilterCategory:
    """Fare Rules Filter if requested will return rules for requested category
    in the response.

    Applicable for providers 1G,1V,1P,1J.

    Parameters
    ----------
    category_code: Fare Rules Filter category can be requested.
        Currently only '˜MIN, MAX, ADV, CHG, OTH' is supported.
        Applicable for Providers 1G,1V,1P,1J.
    fare_info_ref: This tells if Low Fare Finder was used.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    category_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 35,
        }
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        }
    )


@dataclass
class FareStatusFailureInfo:
    """
    Denotes the failure reason of a particular fare.

    Parameters
    ----------
    code: The failure code of the fare.
    reason: The reason for the failure.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Attribute",
        }
    )


@dataclass
class FareTicketDesignator:
    """
    Ticket Designator used to further qualify a Fare.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        }
    )


@dataclass
class FareType:
    """
    Used to request fares based on the ATPCO type code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )


@dataclass
class FeeApplication:
    """
    Parameters
    ----------
    value:
    code: The code associated to the fee application. The  choices are:
        1, 2, 3, 4, 5, K, F
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "length": 1,
        }
    )


class FlexExploreModifiersType(Enum):
    ANY_WHERE = "AnyWhere"
    AREA = "Area"
    ZONE = "Zone"
    COUNTRY = "Country"
    STATE = "State"
    DISTANCE_IN_MILES = "DistanceInMiles"
    DISTANCE_IN_KILOMETERS = "DistanceInKilometers"
    DESTINATION = "Destination"
    GROUP = "Group"


@dataclass
class FlightDetailsRef:
    """
    Reference to a complete FlightDetails from a shared list.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FlightInfoCriteria:
    """
    Parameters
    ----------
    key: An identifier to link the flightinfo responses to the criteria.
        The value passed here will be returned in the resulting
        flightinfo(s) from this command.
    carrier: The carrier that is marketing this segment
    flight_number: The flight number under which the marketing carrier
        is marketing this flight
    origin: The IATA location code for this origination of this entity.
    destination: The IATA location code for this destination of this
        entity.
    departure_date: The date at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location.
    class_of_service:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
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
            "length": 2,
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
            "required": True,
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )


@dataclass
class FlightType:
    """
    Modifier to request flight type options example non-stop only, non-stop and
    direct only, include single online connection etc.

    Parameters
    ----------
    require_single_carrier:
    max_connections: The maximum number of connections within a segment
        group.
    max_stops: The maximum number of stops within a connection.
    non_stop_directs:
    stop_directs:
    single_online_con:
    double_online_con:
    triple_online_con:
    single_interline_con:
    double_interline_con:
    triple_interline_con:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    require_single_carrier: bool = field(
        default=False,
        metadata={
            "name": "RequireSingleCarrier",
            "type": "Attribute",
        }
    )
    max_connections: int = field(
        default=-1,
        metadata={
            "name": "MaxConnections",
            "type": "Attribute",
            "min_inclusive": -1,
            "max_inclusive": 3,
        }
    )
    max_stops: int = field(
        default=-1,
        metadata={
            "name": "MaxStops",
            "type": "Attribute",
            "min_inclusive": -1,
            "max_inclusive": 3,
        }
    )
    non_stop_directs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonStopDirects",
            "type": "Attribute",
        }
    )
    stop_directs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StopDirects",
            "type": "Attribute",
        }
    )
    single_online_con: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SingleOnlineCon",
            "type": "Attribute",
        }
    )
    double_online_con: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DoubleOnlineCon",
            "type": "Attribute",
        }
    )
    triple_online_con: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TripleOnlineCon",
            "type": "Attribute",
        }
    )
    single_interline_con: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SingleInterlineCon",
            "type": "Attribute",
        }
    )
    double_interline_con: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DoubleInterlineCon",
            "type": "Attribute",
        }
    )
    triple_interline_con: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TripleInterlineCon",
            "type": "Attribute",
        }
    )


@dataclass
class GroupedOption:
    """
    Parameters
    ----------
    optional_service_ref: Reference to a optionalService which is paired
        with other optional services in the parent PairedOptions
        element.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    optional_service_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptionalServiceRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class HostReservation:
    """
    Defines a reservation that already exists in the host system (e.g an agent
    using Galileo Desktop already booked a reservation on Midwest in Sabre host
    system).

    Parameters
    ----------
    carrier: The carrier code (e.g. YX, UA, ...) that is providing the
        merchandising
    carrier_locator_code: The locator code in the supplier system (also
        could be defined as locator in the carrier host system).
    provider_code: Contains the GDS or other provider code of the entity
        actually housing the reservation. This is optional when used on
        Merchandising Availability but required on
        MerchandisingFulfillment.
    provider_locator_code: Contains the locator of the reservation
        actually housed in the provider.
    universal_locator_code: The locator of the Universal Record, if one
        exists.
    eticket: An flag to indicate if ticket has been issued for the PNR.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    carrier_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarrierLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    universal_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    eticket: bool = field(
        default=False,
        metadata={
            "name": "ETicket",
            "type": "Attribute",
        }
    )


@dataclass
class ImageLocation:
    """
    Parameters
    ----------
    value:
    type: Type of Image Location. E.g., "Agent", "Consumer".
    image_width: The width of the image
    image_height: The height of the image
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    image_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "ImageWidth",
            "type": "Attribute",
            "required": True,
        }
    )
    image_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "ImageHeight",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class InFlightServices:
    """Available InFlight Services.

    They are: 'Movie', 'Telephone', 'Telex', 'AudioProgramming',
    'Television' ,'ResvBookingService' ,'DutyFreeSales' ,'Smoking'
    ,'NonSmoking' ,'ShortFeatureVideo' ,'NoDutyFree'
    ,'InSeatPowerSource' ,'InternetAccess' ,'Email' ,'Library'
    ,'LieFlatSeat' ,'Additional service(s) exists' ,'WiFi' ,'Lie-Flat
    seat first' ,'Lie-Flat seat business' ,'Lie-Flat seat premium
    economy' ,'Amenities subject to change' etc.. These follow the IATA
    standard. Please see the IATA standards for a more complete list.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class LanguageOption:
    """
    Enables itineraries and invoices to print in different languages.

    Parameters
    ----------
    language: 2 Letter ISO Language code
    country: 2 Letter ISO Country code
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )


@dataclass
class LegDetail:
    """
    Information about the journey Leg, Shared by Leg and LegPrice Elements.

    Parameters
    ----------
    key:
    origin_airport: Returns the origin airport code for the Leg Detail.
    destination_airport: Returns the destination airport code for the
        Leg Detail.
    carrier: Carrier for the Search Leg Detail.
    travel_date: The Departure date and time for this Leg Detail.
    flight_number: Flight Number for the Search Leg Detail.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    origin_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginAirport",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationAirport",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    travel_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Attribute",
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )


@dataclass
class LegRef:
    """
    Reference to a Leg.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class LoyaltyCardDetails:
    """
    Passenger Loyalty card details.

    Parameters
    ----------
    supplier_code: Carrier Code
    priority_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    priority_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PriorityCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{1,1}",
        }
    )


@dataclass
class Maxtype:
    """
    Parameters
    ----------
    hours_max: Maximum hours. True if unit of time is hours. False if
        unit of time is not hours.
    days_max: Maximum days. True if unit of time is days. False if unit
        of time is not days.
    months_max: Maximum months. True if unit of time is months. False if
        unit of time is not months.
    occur_ind_max: Maximum cccurance indicator. True if day of the week
        is used. False if day of the week is not used.
    same_day_max: Same day maximum. True if Stay is same day. False if
        Stay is not same day.
    start_ind_max: Start indicator. True if start indicator. False if
        not a start indicator.
    completion_ind: Completion indicator. True if Completion C
        Indicator. False if not Completion C Indicator.
    tm_dowmax: If a max unit of time is true then number corrolates to
        day of the week starting with 1 for Sunday.
    num_occur_max: Number of maximum occurances.
    """
    class Meta:
        name = "MAXType"

    hours_max: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HoursMax",
            "type": "Attribute",
        }
    )
    days_max: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DaysMax",
            "type": "Attribute",
        }
    )
    months_max: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MonthsMax",
            "type": "Attribute",
        }
    )
    occur_ind_max: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OccurIndMax",
            "type": "Attribute",
        }
    )
    same_day_max: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SameDayMax",
            "type": "Attribute",
        }
    )
    start_ind_max: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StartIndMax",
            "type": "Attribute",
        }
    )
    completion_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CompletionInd",
            "type": "Attribute",
        }
    )
    tm_dowmax: Optional[int] = field(
        default=None,
        metadata={
            "name": "TmDOWMax",
            "type": "Attribute",
        }
    )
    num_occur_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumOccurMax",
            "type": "Attribute",
        }
    )


@dataclass
class Mintype:
    """
    Parameters
    ----------
    hours_min: Minimum hours. True if unit of time is hours.  False if
        unit of time is not hours.
    days_min: Minimum days. True if unit of time is days. False if unit
        of time is not days.
    months_min: Minimum months. True if unit of time is months. False if
        unit of time is not months.
    occur_ind_min: Minimum occurance indicator. True if day of the week
        is used. False if day of the week is not used.
    same_day_min: Same day minimum. True if Stay is same day. False if
        Stay is not same day.
    tm_dowmin: If a min unit of time is true then number corrolates to
        day of the week starting with 1 for Sunday.
    fare_component: Fare component number of the most restrictive fare.
    num_occur_min: Number of min occurances. This field is used in
        conjunction with the Day of Week.
    """
    class Meta:
        name = "MINType"

    hours_min: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HoursMin",
            "type": "Attribute",
        }
    )
    days_min: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DaysMin",
            "type": "Attribute",
        }
    )
    months_min: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MonthsMin",
            "type": "Attribute",
        }
    )
    occur_ind_min: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OccurIndMin",
            "type": "Attribute",
        }
    )
    same_day_min: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SameDayMin",
            "type": "Attribute",
        }
    )
    tm_dowmin: Optional[int] = field(
        default=None,
        metadata={
            "name": "TmDOWMin",
            "type": "Attribute",
        }
    )
    fare_component: Optional[int] = field(
        default=None,
        metadata={
            "name": "FareComponent",
            "type": "Attribute",
        }
    )
    num_occur_min: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumOccurMin",
            "type": "Attribute",
        }
    )


@dataclass
class MaxLayoverDurationType:
    """User can specify its attribute's value in Minutes.

    Maximum size of each attribute is 4.

    Parameters
    ----------
    domestic: It will be applied for all Domestic-to-Domestic
        connections.
    gateway: It will be applied for all Domestic to International and
        International to Domestic connections.
    international: It will be applied for all International-to-
        International connections.
    """
    domestic: Optional[int] = field(
        default=None,
        metadata={
            "name": "Domestic",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 9999,
        }
    )
    gateway: Optional[int] = field(
        default=None,
        metadata={
            "name": "Gateway",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 9999,
        }
    )
    international: Optional[int] = field(
        default=None,
        metadata={
            "name": "International",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 9999,
        }
    )


@dataclass
class MultiGdssearchIndicator:
    """
    Indicates whether public fares and/or private fares should be returned.

    Parameters
    ----------
    type: Indicates whether only public fares or both public and private
        fares should be returned or a specific type of private fares.
        Examples of valid values are PublicFaresOnly, PrivateFaresOnly,
        AirlinePrivateFaresOnly, AgencyPrivateFaresOnly,
        PublicandPrivateFares, and NetFaresOnly.
    provider_code:
    default_provider: Use the value “true” if the provider is the
        default (primary) provider.  Use the value “false” if the
        provider is the alternate (secondary).  Use of this attribute
        requires specifically provisioned credentials.
    private_fare_code: The code of the corporate private fare.  This is
        the same as an account code.  Use of this attribute requires
        specifically provisioned credentials.
    private_fare_code_only: :  Indicates whether or not the private
        fares returned should be restricted to only those specific to
        the PrivateFareCode in the previous attribute.  This has the
        same validation as the AccountCodeFaresOnly attribute.  Use of
        this attribute requires specifically provisioned credentials.
    """
    class Meta:
        name = "MultiGDSSearchIndicator"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    default_provider: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DefaultProvider",
            "type": "Attribute",
        }
    )
    private_fare_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateFareCode",
            "type": "Attribute",
        }
    )
    private_fare_code_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrivateFareCodeOnly",
            "type": "Attribute",
        }
    )


@dataclass
class Othtype:
    """
    Parameters
    ----------
    cat0: Category 0 rules. True if category applies.  False if rules do
        not apply.
    cat1: Category 1 rules. True if category applies.  False if rules do
        not apply.
    cat2: Category 2 rules. True if category applies.  False if rules do
        not apply.
    cat3: Category 3 rules. True if category applies.  False if rules do
        not apply.
    cat4: Category 4 rules. True if category applies.  False if rules do
        not apply.
    cat5: Category 5 rules. True if category applies.  False if rules do
        not apply.
    cat6: Category 6 rules. True if category applies.  False if rules do
        not apply.
    cat7: Category 7 rules. True if category applies.  False if rules do
        not apply.
    cat8: Category 8 rules. True if category applies.  False if rules do
        not apply.
    cat9: Category 9 rules. True if category applies.  False if rules do
        not apply.
    cat10: Category 10 rules. True if category applies.  False if rules
        do not apply.
    cat11: Category 11 rules. True if category applies.  False if rules
        do not apply.
    cat12: Category 12 rules. True if category applies.  False if rules
        do not apply.
    cat13: Category 13 rules. True if category applies.  False if rules
        do not apply.
    cat14: Category 14 rules. True if category applies.  False if rules
        do not apply.
    cat15: Category 15 rules. True if category applies.  False if rules
        do not apply.
    cat16: Category 16 rules. True if category applies.  False if rules
        do not apply.
    cat17: Category 17 rules. True if category applies.  False if rules
        do not apply.
    cat18: Category 18 rules. True if category applies.  False if rules
        do not apply.
    cat19: Category 19 rules. True if category applies.  False if rules
        do not apply.
    cat20: Category 20 rules. True if category applies.  False if rules
        do not apply.
    cat21: Category 21 rules. True if category applies.  False if rules
        do not apply.
    cat22: Category 22 rules. True if category applies.  False if rules
        do not apply.
    cat23: Category 23 rules. True if category applies.  False if rules
        do not apply.
    cat24: Category 24 rules. True if category applies.  False if rules
        do not apply.
    cat25: Category 25 rules. True if category applies.  False if rules
        do not apply.
    cat26: Category 26 rules. True if category applies.  False if rules
        do not apply.
    cat27: Category 27 rules. True if category applies.  False if rules
        do not apply.
    cat28: Category 28 rules. True if category applies.  False if rules
        do not apply.
    cat29: Category 29 rules. True if category applies.  False if rules
        do not apply.
    cat30: Category 30 rules. True if category applies.  False if rules
        do not apply.
    cat31: Category 31 rules. True if category applies.  False if rules
        do not apply.
    restrictive_dt: Most restrictive ticketing date.
    surcharge_amt: Surcharge amount
    not_usacity: Not USA city.  True if Origin or final destination not
        a continental U.S. City. False if Origin or final destination a
        continental U.S. City.
    missing_rules: Missing rules.  True if rules are missing.  False if
        rules are not missing.
    """
    class Meta:
        name = "OTHType"

    cat0: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat0",
            "type": "Attribute",
        }
    )
    cat1: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat1",
            "type": "Attribute",
        }
    )
    cat2: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat2",
            "type": "Attribute",
        }
    )
    cat3: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat3",
            "type": "Attribute",
        }
    )
    cat4: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat4",
            "type": "Attribute",
        }
    )
    cat5: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat5",
            "type": "Attribute",
        }
    )
    cat6: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat6",
            "type": "Attribute",
        }
    )
    cat7: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat7",
            "type": "Attribute",
        }
    )
    cat8: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat8",
            "type": "Attribute",
        }
    )
    cat9: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat9",
            "type": "Attribute",
        }
    )
    cat10: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat10",
            "type": "Attribute",
        }
    )
    cat11: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat11",
            "type": "Attribute",
        }
    )
    cat12: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat12",
            "type": "Attribute",
        }
    )
    cat13: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat13",
            "type": "Attribute",
        }
    )
    cat14: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat14",
            "type": "Attribute",
        }
    )
    cat15: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat15",
            "type": "Attribute",
        }
    )
    cat16: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat16",
            "type": "Attribute",
        }
    )
    cat17: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat17",
            "type": "Attribute",
        }
    )
    cat18: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat18",
            "type": "Attribute",
        }
    )
    cat19: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat19",
            "type": "Attribute",
        }
    )
    cat20: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat20",
            "type": "Attribute",
        }
    )
    cat21: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat21",
            "type": "Attribute",
        }
    )
    cat22: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat22",
            "type": "Attribute",
        }
    )
    cat23: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat23",
            "type": "Attribute",
        }
    )
    cat24: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat24",
            "type": "Attribute",
        }
    )
    cat25: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat25",
            "type": "Attribute",
        }
    )
    cat26: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat26",
            "type": "Attribute",
        }
    )
    cat27: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat27",
            "type": "Attribute",
        }
    )
    cat28: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat28",
            "type": "Attribute",
        }
    )
    cat29: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat29",
            "type": "Attribute",
        }
    )
    cat30: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat30",
            "type": "Attribute",
        }
    )
    cat31: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat31",
            "type": "Attribute",
        }
    )
    restrictive_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RestrictiveDt",
            "type": "Attribute",
        }
    )
    surcharge_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SurchargeAmt",
            "type": "Attribute",
        }
    )
    not_usacity: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NotUSACity",
            "type": "Attribute",
        }
    )
    missing_rules: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MissingRules",
            "type": "Attribute",
        }
    )


@dataclass
class OfferAvailabilityModifiers:
    """
    Parameters
    ----------
    service_type: To restrict offers to only this type.
    carrier: The carrier whose paid seat optional services is to be
        returned by uAPI.
    currency_type: Currency code override. Providers: ACH, 1G, 1V, 1P,
        1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    service_type: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ServiceType",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 128,
        }
    )
    carrier: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "max_occurs": 999,
            "length": 2,
        }
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        }
    )


@dataclass
class OptionalServiceModifier:
    """
    Optional service modifiers.

    Parameters
    ----------
    type: Optional service type
    secondary_type: Secondary optional service type
    supplier_code: Optional service supplier code
    service_sub_code: As published by ATPCO
    travel_date: The departure date of the air segment the optional
        service is valid for.
    description: This allows MDS to return specific image and text
        corresponding to the ancillary name (S5 ancillary name).
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    secondary_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecondaryType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "required": True,
        }
    )
    travel_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Attribute",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class OptionalServiceRef:
    """
    Reference to optional service.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class OverrideCode:
    """
    Code corresponding to the type of OverridableException the user wishes to
    override.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "length": 4,
        }
    )


@dataclass
class PassengerDetailsRef:
    """
    Reference of the Passenger.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PassengerReceiptOverride:
    """
    It is required when a passenger receipt is required immediately ,GDS
    overrides the default value.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
        }
    )


@dataclass
class PassengerSeatPrice:
    """
    Only used when a passenger has a different price than the default.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PassengerTicketNumber:
    """
    Information related to Ticket Number.

    Parameters
    ----------
    ticket_number: The identifying number for a Ticket for a passenger.
    booking_traveler_ref: Reference to a passenger associated with a
        ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class PaymentRef:
    """
    Reference to one of the air reservation payments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PenFeeType:
    """
    Parameters
    ----------
    dep_required: Deposit required. True if require. False if not
        required.
    dep_non_ref: Deposit non-refundable.  True is  non-refundanbe.
        False is refundable.
    tk_non_ref: Ticket non-refundable. True if non-refundanbe. False if
        refundable.
    air_vfee: Carrier fee. True if carrier fee is assessed should
        passenger for complete all conditions for travel at fare. False
        if it does not exist.
    cancellation: Cancellation. True if subject to penalty. False if no
        penalty.
    fail_confirm_space: Failure to confirm space. True if subject to
        penalty if seats are not confirmed. False if subject to penalty
        if seats are confirmed.
    itin_chg: Subject to penalty if Itinerary is changed requiring
        reissue of ticket. True if subject to penalty. False if no
        penalty if reissue required.
    replace_tk: Replace ticket. True if subject to penalty, if
        replacement of lost ticket / exchange order. False if no
        penalty, if replacement of lost ticket or exchange order.
    applicable: Applicable. True if amount specified is applicable.
        Flase if amount specified is not applicable.
    applicable_to: Applicable to penalty or deposit. True if amount
        specified applies to penalty. False if amount specified applies
        to deposit.
    amt: Amount of penalty.  If XXX.XX then it is an amount.  If it is
        XX then is is a percenatge.  Eg 100.00 or 000100.
    type: Type of penalty.  If it is D then dollar.  If it is P then
        percentage.
    currency: Currency code of penalty (e.g. USD).
    """
    dep_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DepRequired",
            "type": "Attribute",
        }
    )
    dep_non_ref: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DepNonRef",
            "type": "Attribute",
        }
    )
    tk_non_ref: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TkNonRef",
            "type": "Attribute",
        }
    )
    air_vfee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AirVFee",
            "type": "Attribute",
        }
    )
    cancellation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancellation",
            "type": "Attribute",
        }
    )
    fail_confirm_space: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FailConfirmSpace",
            "type": "Attribute",
        }
    )
    itin_chg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ItinChg",
            "type": "Attribute",
        }
    )
    replace_tk: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReplaceTk",
            "type": "Attribute",
        }
    )
    applicable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Applicable",
            "type": "Attribute",
        }
    )
    applicable_to: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ApplicableTo",
            "type": "Attribute",
        }
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
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
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
        }
    )


@dataclass
class Penalty:
    """
    Parameters
    ----------
    amount: Penalty Amount
    penalty_type: This is the PPC (Price Processing Code)code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    penalty_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PenaltyType",
            "type": "Attribute",
        }
    )


@dataclass
class PenaltyInformation:
    """
    Parameters
    ----------
    value:
    carrier: Fare-owning carrier
    fare_basis: Unique identifier that provides the association to the
        fare amount and fare rules.
    fare_component: A portion of a journey or itinerary between two
        consecutive fare break points.
    priceable_unit: Identifies FareComponents that are priced together
    board_point: Origin for the FareComponent
    off_point: Destination for the FareComponent
    minimum_change_fee: Estimated minimum change fee associated with the
        fare component.  Can be overridden by ChangeFeeApplicationCodes
        for other fare components.
    maximum_change_fee: Estimated maximum change fee associated with the
        fare component.  Can be overridden by ChangeFeeApplicationCodes
        for other fare components.
    filed_currency: Currency of the filed change fee
    conversion_rate: Conversion rate from filed change fee currency to
        reissue location currency
    refundable: Answers whether the FareComponent is refundable
    change_fee_application_code: Unique code associated with the
        PenaltyInformation text which defines how fees will be
        applied/calculated. E.g. J2 translates to "From among all fare
        components, changed and unchanged...."
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
        }
    )
    fare_component: Optional[int] = field(
        default=None,
        metadata={
            "name": "FareComponent",
            "type": "Attribute",
        }
    )
    priceable_unit: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriceableUnit",
            "type": "Attribute",
        }
    )
    board_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "BoardPoint",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    off_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffPoint",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    minimum_change_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinimumChangeFee",
            "type": "Attribute",
        }
    )
    maximum_change_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaximumChangeFee",
            "type": "Attribute",
        }
    )
    filed_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "length": 3,
        }
    )
    conversion_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ConversionRate",
            "type": "Attribute",
        }
    )
    refundable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
        }
    )
    change_fee_application_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeFeeApplicationCode",
            "type": "Attribute",
            "length": 2,
        }
    )


@dataclass
class PersonName:
    """
    Customer name field.

    Parameters
    ----------
    first: Person First Name.
    last: Person Last Name.
    prefix: Person Name prefix.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    first: Optional[str] = field(
        default=None,
        metadata={
            "name": "First",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    last: Optional[str] = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prefix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )


@dataclass
class PersonNameSearch:
    """
    Customer name field.

    Parameters
    ----------
    last: Person Last Name to be searched for Flight Pass content.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    last: Optional[str] = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )


@dataclass
class PolicyCodesList:
    """
    Parameters
    ----------
    policy_code: A code that indicates why an item was determined to be
        ‘out of policy’.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    policy_code: List[int] = field(
        default_factory=list,
        metadata={
            "name": "PolicyCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
            "min_inclusive": 1,
            "max_inclusive": 9999,
        }
    )


@dataclass
class PriceChangeType:
    """
    Indicates a price change is found in Fare Control Manager.

    Parameters
    ----------
    value:
    amount: Contains the currency and amount information. Assume the
        amount is added unless a hyphen is present to indicate
        subtraction.
    carrier: Contains carrier code information
    segment_ref: Contains segment reference information
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )


@dataclass
class PriceRange:
    """
    Parameters
    ----------
    default_currency: Indicates if the currency code of StartPrice /
        EndPrice is the default currency code
    start_price: Price range start value
    end_price: Price range end value
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    default_currency: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Attribute",
        }
    )
    start_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartPrice",
            "type": "Attribute",
        }
    )
    end_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndPrice",
            "type": "Attribute",
        }
    )


@dataclass
class PrintBlankFormItinerary:
    """
    Produce a customized itinerary/Invoice document in blank form format.

    Parameters
    ----------
    include_description: If it is true then document will be printed
        including descriptions.
    include_header: If it is true then document will be printed
        including it's header.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    include_description: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeDescription",
            "type": "Attribute",
            "required": True,
        }
    )
    include_header: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeHeader",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PromoCode:
    """
    A container to specify Promotional code with Provider code and Supplier
    code.

    Parameters
    ----------
    code: To be used to specify Promotional Code.
    provider_code: To be used to specify Provider Code.
    supplier_code: To be used to specify Supplier Code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )


@dataclass
class RailCoachDetails:
    """
    Parameters
    ----------
    rail_coach_number: Rail coach number for the returned coach details.
    available_rail_seats: Number of available seats present in this rail
        coach.
    rail_seat_map_availability: Indicates if seats are available in this
        rail coach which can be mapped.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    rail_coach_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
        }
    )
    available_rail_seats: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailableRailSeats",
            "type": "Attribute",
        }
    )
    rail_seat_map_availability: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RailSeatMapAvailability",
            "type": "Attribute",
        }
    )


class RepricingModifiersFlightType(Enum):
    DIRECT = "Direct"
    NON_STOP = "NonStop"
    SINGLE_CONNECTION = "SingleConnection"
    NO_RESTRICTIONS = "NoRestrictions"


@dataclass
class Restriction:
    """
    Fare Reference associated with the BookingRules.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    days_of_week_restriction: List["Restriction.DaysOfWeekRestriction"] = field(
        default_factory=list,
        metadata={
            "name": "DaysOfWeekRestriction",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    restriction_passenger_types: List["Restriction.RestrictionPassengerTypes"] = field(
        default_factory=list,
        metadata={
            "name": "RestrictionPassengerTypes",
            "type": "Element",
            "max_occurs": 999,
        }
    )

    @dataclass
    class DaysOfWeekRestriction:
        mon: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Mon",
                "type": "Attribute",
            }
        )
        tue: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Tue",
                "type": "Attribute",
            }
        )
        wed: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Wed",
                "type": "Attribute",
            }
        )
        thu: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Thu",
                "type": "Attribute",
            }
        )
        fri: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Fri",
                "type": "Attribute",
            }
        )
        sat: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Sat",
                "type": "Attribute",
            }
        )
        sun: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Sun",
                "type": "Attribute",
            }
        )
        restriction_exists_ind: Optional[bool] = field(
            default=None,
            metadata={
                "name": "RestrictionExistsInd",
                "type": "Attribute",
            }
        )
        application: Optional[str] = field(
            default=None,
            metadata={
                "name": "Application",
                "type": "Attribute",
            }
        )
        include_exclude_use_ind: Optional[bool] = field(
            default=None,
            metadata={
                "name": "IncludeExcludeUseInd",
                "type": "Attribute",
            }
        )

    @dataclass
    class RestrictionPassengerTypes:
        max_nbr_travelers: Optional[str] = field(
            default=None,
            metadata={
                "name": "MaxNbrTravelers",
                "type": "Attribute",
            }
        )
        total_nbr_ptc: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalNbrPTC",
                "type": "Attribute",
            }
        )


@dataclass
class RuleCharges:
    """
    Container for rules related to charges such as deposits, surcharges,
    penalities, etc..

    Parameters
    ----------
    penalty_type:
    departure_status:
    amount:
    percent:
    more_rules_present: If true, specifies that advance purchase
        information will be present in fare rules.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    penalty_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PenaltyType",
            "type": "Attribute",
        }
    )
    departure_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureStatus",
            "type": "Attribute",
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    percent: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
        }
    )
    more_rules_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreRulesPresent",
            "type": "Attribute",
        }
    )


@dataclass
class Rules:
    """
    Parameters
    ----------
    rules_text: Rules text
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    rules_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "RulesText",
            "type": "Element",
        }
    )


@dataclass
class SearchSpecificAirSegment:
    """
    Parameters
    ----------
    departure_time: The date and time at which this entity departs. This
        does not include time zone information since it can be derived
        from the origin location.
    carrier: The carrier that is marketing this segment
    flight_number: The flight number under which the marketing carrier
        is marketing this flight
    origin: The IATA location code for this origination of this entity.
    destination: The IATA location code for this destination of this
        entity.
    segment_index: The sequential AirSegment number that this segment
        connected to.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
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
            "length": 2,
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    segment_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SegmentIndex",
            "type": "Attribute",
        }
    )


@dataclass
class SeatInformation:
    """Additional information about seats.

    Providers: 1G, 1V, 1P, 1J,ACH

    Parameters
    ----------
    power: Detail about any electrical power the seat might have. For
        example: No Power Providers: 1G, 1V, 1P, 1J
    video: Detail about any video components the seat might have. For
        example: No Video Providers: 1G, 1V, 1P, 1J
    type: Detail about the type of seat. For example: Exit Row,
        Standard, etc. Providers: 1G, 1V, 1P, 1J
    description: Detailed description of the seat. Providers: 1G, 1V,
        1P, 1J
    rating: Definition of the seat rating. Providers: 1G, 1V, 1P, 1J
    key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    power: Optional[str] = field(
        default=None,
        metadata={
            "name": "Power",
            "type": "Element",
            "required": True,
        }
    )
    video: Optional[str] = field(
        default=None,
        metadata={
            "name": "Video",
            "type": "Element",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "required": True,
        }
    )
    rating: Optional["SeatInformation.Rating"] = field(
        default=None,
        metadata={
            "name": "Rating",
            "type": "Element",
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Rating:
        """
        Parameters
        ----------
        value:
        number: Numerical rating of the seat from 1 to 5 with 1 being
            bad and 5 being good. Providers: 1G, 1V, 1P, 1J
        """
        value: str = field(
            default="",
            metadata={
                "required": True,
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


@dataclass
class SegmentIndex:
    """
    Identifies the segment that is part of this group.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ServiceSubGroup:
    """The Service Sub Group of the Ancillary Service.

    Providers: 1G, 1V, 1P, 1J, ACH

    Parameters
    ----------
    code: The Service Sub Group Code of the Ancillary Service.
        Providers: 1G, 1V, 1P, 1J, ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )


@dataclass
class SpecificSeatAssignment:
    """
    Request object used to specify a specific seat.

    Parameters
    ----------
    booking_traveler_ref: The passenger that this seat assignment is for
    segment_ref: The segment that we will assign this seat on
    flight_detail_ref: The Flight Detail ref of the AirSegment used when
        requesting seats on Change of Guage flights
    seat_id: The actual seat ID that is being requested. Special
        Characters are not supported in this field.
    rail_coach_number: Coach number for which rail seatmap/coachmap is
        returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
            "required": True,
        }
    )
    flight_detail_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightDetailRef",
            "type": "Attribute",
        }
    )
    seat_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatId",
            "type": "Attribute",
            "required": True,
        }
    )
    rail_coach_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
            "max_length": 4,
        }
    )


@dataclass
class SplitTicketingSearch:
    """SplitTicketingSearch is optional.

    Used to return both One-Way and Roundtrip fares in a single search
    response. Applicable to 1G, 1V, 1P only, the price points results
    path, and a simple roundtrip search only. Cannot be used in
    combination with Flex options.

    Parameters
    ----------
    round_trip: Percentage of Roundtrip price points to be returned in
        the search response. This should be an even number. The One-Way
        price points returned in the response would be evenly
        distributed between the outbound and the inbound.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    round_trip: Optional[int] = field(
        default=None,
        metadata={
            "name": "RoundTrip",
            "type": "Attribute",
        }
    )


@dataclass
class SponsoredFltInfo:
    """This describes whether the segment is determined to be a sponsored
    flight.

    The SponsoredFltInfo node will only come back for Travelport UIs and
    not for other customers.

    Parameters
    ----------
    sponsored_lnb: The line number of the sponsored flight item
    neutral_lnb: The neutral line number for the flight item.
    flt_key: The unique identifying key for the sponsored flight.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    sponsored_lnb: Optional[int] = field(
        default=None,
        metadata={
            "name": "SponsoredLNB",
            "type": "Attribute",
            "required": True,
        }
    )
    neutral_lnb: Optional[int] = field(
        default=None,
        metadata={
            "name": "NeutralLNB",
            "type": "Attribute",
            "required": True,
        }
    )
    flt_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "FltKey",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )


@dataclass
class SvcSegment:
    """Service segment added to collect additional fee.

    1P only

    Parameters
    ----------
    key: The Key of SVC Segment.
    carrier: The platting carrier
    status:
    number_of_items:
    origin: Origin location - Airport code. 1P only.
    destination: Destination location - Airport code. 1P only.
    start_date: Start date of the segment. Generally it is the next date
        after the last air segment. 1P only
    travel_order: To identify the appropriate travel sequence for
        Air/Car/Hotel/Passive segments/reservations based on travel
        dates. This ordering is applicable across the UR not provider or
        traveler specific
    booking_traveler_ref:
    rfic: 1P - Reason for issuance
    rfisc: 1P - Resaon for issuance sub-code
    svc_description: 1P - SVC fee description
    fee: The fee to be collected using SVC segment
    emdnumber: Generated EMD number, if EMD is issued on the SVC
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    number_of_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfItems",
            "type": "Attribute",
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        }
    )
    travel_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
    rfic: Optional[str] = field(
        default=None,
        metadata={
            "name": "RFIC",
            "type": "Attribute",
        }
    )
    rfisc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RFISC",
            "type": "Attribute",
        }
    )
    svc_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcDescription",
            "type": "Attribute",
        }
    )
    fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fee",
            "type": "Attribute",
        }
    )
    emdnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMDNumber",
            "type": "Attribute",
            "length": 13,
        }
    )


class TcrrefundBundleRefundType(Enum):
    AUTO = "Auto"
    MANUAL = "Manual"
    IGNORED = "Ignored"


@dataclass
class Tax:
    """
    Taxes for Land Charges.

    Parameters
    ----------
    category: The tax category represents a valid IATA tax code.
    amount:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TextInfo:
    """
    Information on baggage as published by carrier.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 999,
            "max_length": 250,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
        }
    )


@dataclass
class TicketAgency:
    """This modifier will override the pseudo of the ticketing agency found in
    the AAT (TKAG).

    Used for all plating carrier validation.

    Parameters
    ----------
    provider_code: The code of the Provider (e.g. 1G, 1P)
    pseudo_city_code: The PCC of the host system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TicketDesignator:
    """
    Ticket Designator used to further qualify a Fare Basis Code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )


@dataclass
class TicketEndorsement:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        }
    )


@dataclass
class TicketValidity:
    """
    To be used to pass the selected segment.

    Parameters
    ----------
    not_valid_before: Fare not valid before this date.
    not_valid_after: Fare not valid after this date.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    not_valid_before: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        }
    )
    not_valid_after: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        }
    )


@dataclass
class TicketingModifiersRef:
    """
    Reference to a shared list of Ticketing Modifers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TourCode:
    """
    Tour Code Fare Basis.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )


@dataclass
class TravelArranger:
    """
    Details of Travel Arranger.

    Parameters
    ----------
    value:
    company_short_name: Company Name
    code: IATA Code for Arranger
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    company_short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyShortName",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )


@dataclass
class Url:
    class Meta:
        name = "URL"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
class Urlinfo:
    """
    Contains the text and URL of baggage as published by carrier.
    """
    class Meta:
        name = "URLInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 999,
            "max_length": 250,
        }
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "URL",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class UpsellBrand:
    """
    Upsell brand reference.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
        }
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        }
    )


@dataclass
class ValueDetails:
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
            "required": True,
        }
    )


@dataclass
class VoidFailureInfo:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )


@dataclass
class WaiverCode:
    """
    Waiver code to override fare validations.

    Parameters
    ----------
    tour_code:
    ticket_designator:
    endorsement: Endorsement. Size can be up to 100 characters
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    tour_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        }
    )
    endorsement: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endorsement",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 100,
        }
    )


@dataclass
class Yield:
    """An identifier which identifies yield made on original pricing.

    It can be a flat amount of original price. The value of Amount can
    be negative. Negative value implies a discount.

    Parameters
    ----------
    amount: Yield per passenger level in Default Currency for this
        entity.
    booking_traveler_ref: Reference to a booking traveler for which
        Yield is applied.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


class TypeAtpcoglobalIndicator(Enum):
    """
    Enumeration of ATPCO global indicators.

    Properties
    ----------
    AL: FareByRule -- All fares incl. EH/TS
    AP: Via Atlantic Pacific
    AT: Via Atlantic
    CA: Within Canada.
    CT: Circle trip.
    EH: Within Eastern Hemisphere
    FE: Far East
    IN: FareByRule - For int'l incl. AT/PA/WH/CT/RW
    NA: FareByRule for North America incl US/CA/TB/PV
    PA: Via Pacific
    PN: Via Pacific and via North America
    PO: Via Polar Route.
    RU: Russia - Area 3
    RW: Round The World.
    SA: South Atlantic only
    SP: Via South Polar Route
    TB: Trans-border
    TS: Via Siberia.
    US: Within the United States.
    WH: Within Western Hemisphere
    ZZ: Any Global
    """
    AL = "AL"
    AP = "AP"
    AT = "AT"
    CA = "CA"
    CT = "CT"
    EH = "EH"
    FE = "FE"
    IN = "IN"
    NA = "NA"
    PA = "PA"
    PN = "PN"
    PO = "PO"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SP = "SP"
    TB = "TB"
    TS = "TS"
    US = "US"
    WH = "WH"
    ZZ = "ZZ"


class TypeAlliance(Enum):
    STAR_ALLIANCE = "StarAlliance"
    ONE_WORLD = "OneWorld"
    KLMNORTHWEST_ALLIANCE = "KLMNorthwestAlliance"
    SKY_TEAM = "SkyTeam"
    OWCODE = "OWCode"


@dataclass
class TypeAnchorFlightData:
    """To support Anchor flight search contain the anchor flight details.

    Supported providers 1P, 1J

    Parameters
    ----------
    airline_code: Indicates Anchor flight carrier code
    flight_number: Indicates Anchor flight number
    connection_indicator: Indicates that the Anchor flight has any
        connecting flight or not
    """
    class Meta:
        name = "typeAnchorFlightData"

    airline_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirlineCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )
    connection_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConnectionIndicator",
            "type": "Attribute",
        }
    )


@dataclass
class TypeApplicableSegment:
    """
    Parameters
    ----------
    key:
    air_itinerary_details_ref:
    booking_counts: Classes of service and their counts.
    """
    class Meta:
        name = "typeApplicableSegment"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    air_itinerary_details_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirItineraryDetailsRef",
            "type": "Attribute",
        }
    )
    booking_counts: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingCounts",
            "type": "Attribute",
        }
    )


class TypeAssessIndicator(Enum):
    """
    The type of AssessIndicator.
    """
    MILEAGE_AND_CURRENCY = "MileageAndCurrency"
    MILEAGE_OR_CURRENCY = "MileageOrCurrency"


class TypeBackOffice(Enum):
    ACCOUNTING = "Accounting"
    GLOBAL = "Global"
    NON_ACCOUNTING = "NonAccounting"
    NON_ACCOUNTING_REMOTE = "NonAccountingRemote"
    DUAL = "Dual"


class TypeBillingDetailsDataType(Enum):
    ALPHA = "Alpha"
    NUMERIC = "Numeric"
    ALPHA_NUMERIC = "AlphaNumeric"
    DATE = "Date"


class TypeBillingDetailsName(Enum):
    PERSONAL_ID = "PersonalId"
    COST_ACCOUNT_NUMBER = "CostAccountNumber"
    ACCOUNT_NUMBER = "AccountNumber"
    PROJECT_NUMBER = "ProjectNumber"
    ACTION_CODE = "ActionCode"
    DEPARTMENT_CODE = "DepartmentCode"
    ACCOUNTING_UNIT = "AccountingUnit"
    ORDER_NUMBER = "OrderNumber"
    DESTINATION = "Destination"
    FILE_DATE = "FileDate"


class TypeBooking(Enum):
    """
    Type of booking.
    """
    SSR = "SSR"
    AUXILLARY_SEGMENT = "Auxillary Segment"
    AVAILABLE_FOR_DISPLAY_PRICING = "Available for Display/Pricing"
    CONTACT_CARRIER_FOR_BOOKING = "Contact Carrier for Booking"
    NO_BOOKING_REQUIRED = "No Booking Required"
    APPLY_BOOKING_PER_SERVICE = "Apply booking per service"


@dataclass
class TypeBulkTicketModifierType:
    """
    Bulk ticketing modifier type.

    Parameters
    ----------
    suppress_on_fare_calc: Optional attribute to allow a modifier impact
        such as Bulk Ticketing to have information suppressed on the
        Fare Calc when generating supporting documents Check the
        specific host system which may or may not support this function
    """
    class Meta:
        name = "typeBulkTicketModifierType"

    suppress_on_fare_calc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SuppressOnFareCalc",
            "type": "Attribute",
        }
    )


class TypeCarrierCode(Enum):
    """
    Defines the type of booking codes (Primary or Secondary)
    """
    PRIMARY = "Primary"
    SECONDARY = "Secondary"


class TypeConnectionIndicator(Enum):
    """Types of connection indicator :

    AvailabilityAndPricing : Specified availability and pricing connection;
    TurnAround : Specified turn around;
    Stopover : Specified stopover;
    """
    AVAILABILITY_AND_PRICING = "AvailabilityAndPricing"
    TURN_AROUND = "TurnAround"
    STOPOVER = "Stopover"


class TypeCouponStatus(Enum):
    """
    ATA/IATA Standard coupon status.

    Properties
    ----------
    A: Code="A" Status="Airport Controlled".
    C: Code="C" Status="Checked In"
    F: Code="F" Status="Flown/Used"
    L: Code="L" Status="Boarded/Lifted"
    O: Code="O" Status="Open"
    P: Code="P" Status="Printed"
    R: Code="R" Status="Refunded"
    E: Code="E" Status="Exchanged"
    V: Code="V" Status="Void"
    Z: Code="Z" Status="Archived/Carrier Modified"
    U: Code="U" Status="Unavailable"
    S: Code="S" Status="Suspended"
    I: Code="I" Status="Irregular Ops"
    D: Code="D" "Deleted/Removed"
    """
    A = "A"
    C = "C"
    F = "F"
    L = "L"
    O = "O"
    P = "P"
    R = "R"
    E = "E"
    V = "V"
    Z = "Z"
    U = "U"
    S = "S"
    I = "I"
    D = "D"


@dataclass
class TypeDaysOfOperation:
    class Meta:
        name = "typeDaysOfOperation"

    mon: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mon",
            "type": "Attribute",
        }
    )
    tue: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Tue",
            "type": "Attribute",
        }
    )
    wed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Wed",
            "type": "Attribute",
        }
    )
    thu: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Thu",
            "type": "Attribute",
        }
    )
    fri: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Fri",
            "type": "Attribute",
        }
    )
    sat: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sat",
            "type": "Attribute",
        }
    )
    sun: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sun",
            "type": "Attribute",
        }
    )


class TypeDestinationCode(Enum):
    """
    List of valid Destination Codes.

    Properties
    ----------
    MEXICO_COST_RICA_CENTRAL_AMERICA: Mexico/Central America/Canal
        Zone/Costa Rica
    CARIBBEAN: Island and Countries of The Caribbean
    SOUTH_AMERICA: South America
    EUROPE: Europe
    AFRICA: Africa
    MIDDLE_EAST_WESTERN_ASIA: Middle East/Western Asia
    ASIA: Asia
    AUSTRALIA_NEW_ZEALAND_PACIFIC_ISLANDS: Australia/New Zealand/Pacific
        Islands
    CANADA_GREENLAND: Canada and Greenland
    USA: United States of America
    """
    MEXICO_COST_RICA_CENTRAL_AMERICA = "MexicoCostRicaCentralAmerica"
    CARIBBEAN = "Caribbean"
    SOUTH_AMERICA = "SouthAmerica"
    EUROPE = "Europe"
    AFRICA = "Africa"
    MIDDLE_EAST_WESTERN_ASIA = "MiddleEastWesternAsia"
    ASIA = "Asia"
    AUSTRALIA_NEW_ZEALAND_PACIFIC_ISLANDS = "AustraliaNewZealandPacificIslands"
    CANADA_GREENLAND = "CanadaGreenland"
    USA = "USA"


class TypeDisplayCategory(Enum):
    """
    Type of booking.
    """
    WITH_ITINERARY_PRICING = "With Itinerary Pricing"
    STORE = "Store"
    SPECIAL_SERVICE = "SpecialService"


class TypeDiversity(Enum):
    """
    Used in Low Fare Search to better promote unique results.
    """
    BLEND = "Blend"
    AIRPORTS = "Airports"
    CARRIER = "Carrier"
    ORIGIN = "Origin"
    DESTINATION = "Destination"
    DATE_COMBINATION = "DateCombination"
    FIRST_ODDATE = "FirstODDate"
    SECOND_ODDATE = "SecondODDate"
    FIRST_OD = "FirstOD"
    SECOND_OD = "SecondOD"


class TypeEticketability(Enum):
    """
    Defines the ability to eticket an entity (Yes, No, Required, Ticketless)
    """
    YES = "Yes"
    NO = "No"
    REQUIRED = "Required"
    TICKETLESS = "Ticketless"


class TypeFacility(Enum):
    SEAT = "Seat"
    AISLE = "Aisle"
    OPEN = "Open"
    UNKNOWN = "Unknown"


@dataclass
class TypeFailureInfo:
    class Meta:
        name = "typeFailureInfo"

    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeFareBreak(Enum):
    """
    Types of fare break.

    Properties
    ----------
    MUST_BREAK: Break Fare at the associated segment. Multiple Breaks or
        No Breaks may be allowed.
    MUST_ONLY_BREAK: Only Break Fare at the associated segment. Fare
        Break in the entire itinerary is allowed only at the concerned
        segment.
    MUST_NOT_BREAK: No Fare Break allowed at the associated segment.
    """
    MUST_BREAK = "MustBreak"
    MUST_ONLY_BREAK = "MustOnlyBreak"
    MUST_NOT_BREAK = "MustNotBreak"


class TypeFareDirectionality(Enum):
    """
    A fare's directionality (e.g. one-way, return )
    """
    OUTBOUND = "Outbound"
    RETURN = "Return"
    ALL = "All"


class TypeFareDiscount(Enum):
    """
    Fare Discount Calculation Method.
    """
    BASE_RE_CALC_USTAXES = "BaseReCalcUSTaxes"
    BASE_NO_RE_CALC_USTAXES = "BaseNoReCalcUSTaxes"
    BASE_TAX = "BaseTax"


class TypeFareGuarantee(Enum):
    """
    The status of a fare.

    Properties
    ----------
    AUTO: Automatically generated
    MANUAL: Agent has overridden default(s)
    MANUAL_FARE: Fare has been constructed by agent
    GUARANTEED: Fare is guaranteed
    INVALID: Invalid fare, e.g. due to name or itinerary change
    RESTORED: Ticketed stored fare has been restored
    TICKETED:
    UNTICKETABLE: Unable to ticket
    REPRICE: Need requote to ticket
    EXPIRED: Expired fare due to older fare guarantee date typically
        older than 7 days
    AUTO_USING_PRIVATE_FARE: Agency private fares that are not
        guaranteed
    GUARANTEED_USING_AIRLINE_PRIVATE_FARE: Guaranteed fare using Airline
        private fare that was filed with a fare distributor.
    AIRLINE: Fare guaranteed by Airline.
    GUARANTEE_EXPIRED: Guaranteed fare recently got expired as ticketing
        hadn't been done within a time frame typically midnight local
        time of POS .
    AGENCY_PRIVATE_FARE_NO_OVERRIDE: Agency Private Fare with no rules
        override
    UNKNOWN: To handle new enumerations added by provider but currently
        not recognized by API
    """
    AUTO = "Auto"
    MANUAL = "Manual"
    MANUAL_FARE = "ManualFare"
    GUARANTEED = "Guaranteed"
    INVALID = "Invalid"
    RESTORED = "Restored"
    TICKETED = "Ticketed"
    UNTICKETABLE = "Unticketable"
    REPRICE = "Reprice"
    EXPIRED = "Expired"
    AUTO_USING_PRIVATE_FARE = "AutoUsingPrivateFare"
    GUARANTEED_USING_AIRLINE_PRIVATE_FARE = "GuaranteedUsingAirlinePrivateFare"
    AIRLINE = "Airline"
    GUARANTEE_EXPIRED = "GuaranteeExpired"
    AGENCY_PRIVATE_FARE_NO_OVERRIDE = "AgencyPrivateFareNoOverride"
    UNKNOWN = "Unknown"


class TypeFarePenaltyPenaltyApplies(Enum):
    """
    The values can be "Anytime", "Before Departure" or "After Departure".
    """
    ANYTIME = "Anytime"
    BEFORE_DEPARTURE = "Before Departure"
    AFTER_DEPARTURE = "After Departure"


class TypeFareRestrictionType(Enum):
    """
    The type of fare restriction.
    """
    DAY_OF_WEEK = "DayOfWeek"
    FLIGHT_TIME_OF_DAY = "FlightTimeOfDay"
    BOTH = "Both"


class TypeFareRuleCategoryCode(Enum):
    """
    Kestrel Long Fare Rule Category Codes.

    Properties
    ----------
    APP: Rule App/Other Conditions
    WHO: Eligibility
    DAY: Day/Time
    SEA: Seasonal
    FLT: Flight App
    ADV: Advance Res/Tkt
    MIN: Minimum Stay
    MAX: Maximum Stay
    STP: Stopovers
    TRF: Transfers/Routing
    CMB: Combinability
    BLA: Blackouts
    SUR: Surcharges
    ACC: Accompanied
    TVL: Travel Restrictions
    TKT: Sales Restrictions
    CHG: Penalties
    HIP: HIP and Mileage Exceptions
    END: Ticket Endorsements
    CHD: Children"s Discounts
    TUC: Tour Conductor Disc
    AGT: Agent Discounts
    DSC: All Other Disc
    MIS: Misc Fare Tags
    FBR: Fare By Rule
    GRP: Groups
    TUR: Tours
    VAC: Visit Another Country
    DEP: Deposits
    VOL: Voluntary Changes
    IVE: Involuntary Exchanges
    VOR: Voluntary Refunds
    IVR: Involuntary Refunds
    NET: Negotiated Fares
    OTH: Other
    """
    APP = "APP"
    WHO = "WHO"
    DAY = "DAY"
    SEA = "SEA"
    FLT = "FLT"
    ADV = "ADV"
    MIN = "MIN"
    MAX = "MAX"
    STP = "STP"
    TRF = "TRF"
    CMB = "CMB"
    BLA = "BLA"
    SUR = "SUR"
    ACC = "ACC"
    TVL = "TVL"
    TKT = "TKT"
    CHG = "CHG"
    HIP = "HIP"
    END = "END"
    CHD = "CHD"
    TUC = "TUC"
    AGT = "AGT"
    DSC = "DSC"
    MIS = "MIS"
    FBR = "FBR"
    GRP = "GRP"
    TUR = "TUR"
    VAC = "VAC"
    DEP = "DEP"
    VOL = "VOL"
    IVE = "IVE"
    VOR = "VOR"
    IVR = "IVR"
    NET = "NET"
    OTH = "OTH"


class TypeFareRuleType(Enum):
    """
    The valid rule types.
    """
    NONE = "none"
    SHORT = "short"
    LONG = "long"


class TypeFareSearchOption(Enum):
    """
    Fare Search option indicator.
    """
    LEAVE = "Leave"
    RETURN = "Return"
    SEASONAL = "Seasonal"
    BLACKOUT = "Blackout"
    ADVANCE_PURCHASE = "Advance Purchase"
    DAY_OF_WEEK = "Day-of-week"
    EFFECTIVE_DATE = "Effective Date"


class TypeFareStatusCode(Enum):
    """
    Properties
    ----------
    READY_TO_TICKET: Fare is enabled and available for ticketing
    UNABLE_TO_TICKET: Fare could not be ticketed
    REPRICE: Fare needs to be repriced
    TICKETED: Fare is ticketed
    UNABLE: Fare is not enabled
    UNKNOWN: To handle new enumerations added by provider but currently
        not recognized by API
    """
    READY_TO_TICKET = "ReadyToTicket"
    UNABLE_TO_TICKET = "UnableToTicket"
    REPRICE = "Reprice"
    TICKETED = "Ticketed"
    UNABLE = "Unable"
    UNKNOWN = "Unknown"


class TypeFareTripType(Enum):
    """Type of trip for this fare ( One-way, Return, etc..)

    OneWay - one way fare
    OneWayOnly - one way fare only. Do not
    double
    Return - round trip fare
    ReturnOnly -- Round Trip fare only.
    Cannot be divided for use in half Round Trip
    HalfReturn - Half roundtrip fare
    CircleTrip -- circle trip fare
    RoundTheWorld -- round the world fare
    """
    ONE_WAY = "OneWay"
    ONE_WAY_ONLY = "OneWayOnly"
    RETURN = "Return"
    RETURN_ONLY = "ReturnOnly"
    HALF_RETURN = "HalfReturn"
    CIRCLE_TRIP = "CircleTrip"
    ROUND_THE_WORLD = "RoundTheWorld"


class TypeFaresIndicator(Enum):
    """
    Defines the type of fares to return (Only public fares, Only private fares,
    Only agency private fares, Only airline private fares or all fares)

    Properties
    ----------
    PUBLIC_FARES_ONLY:
    PRIVATE_FARES_ONLY:
    AGENCY_PRIVATE_FARES_ONLY:
    AIRLINE_PRIVATE_FARES_ONLY:
    PUBLIC_AND_PRIVATE_FARES:
    NET_FARES_ONLY:
    ALL_FARES: Applicable for 1G/1V air shop only
    """
    PUBLIC_FARES_ONLY = "PublicFaresOnly"
    PRIVATE_FARES_ONLY = "PrivateFaresOnly"
    AGENCY_PRIVATE_FARES_ONLY = "AgencyPrivateFaresOnly"
    AIRLINE_PRIVATE_FARES_ONLY = "AirlinePrivateFaresOnly"
    PUBLIC_AND_PRIVATE_FARES = "PublicAndPrivateFares"
    NET_FARES_ONLY = "NetFaresOnly"
    ALL_FARES = "AllFares"


class TypeIgnoreStopOver(Enum):
    """
    The stop over inluded to quote fare.

    Properties
    ----------
    NO_STOP_OVER: No Stop over included.
    STOP_OVER: Stop over included.
    IGNORE_SEGMENT: Segment Ignored.
    """
    NO_STOP_OVER = "NoStopOver"
    STOP_OVER = "StopOver"
    IGNORE_SEGMENT = "IgnoreSegment"


class TypeInventoryRequest(Enum):
    """The valid inventory types are Seamless - A, DirectAccess - B, Basic - C"""
    SEAMLESS = "Seamless"
    DIRECT_ACCESS = "DirectAccess"
    BASIC = "Basic"


class TypeItinerary(Enum):
    INVOICE = "Invoice"
    POCKET = "Pocket"


class TypeItineraryOption(Enum):
    NO_FARE = "NoFare"
    NO_AMOUNT = "NoAmount"
    SEQUENCE_NUMBER = "SequenceNumber"


class TypeMealService(Enum):
    """
    Available Meal Service.
    """
    MEAL = "Meal"
    COLD_MEAL = "ColdMeal"
    HOT_MEAL = "HotMeal"
    BREAKFAST = "Breakfast"
    CONTINENTAL_BREAKFAST = "ContinentalBreakfast"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    SNACK_OR_BRUNCH = "SnackOrBrunch"
    FOOD_FOR_PURCHASE = "FoodForPurchase"
    COMPLIMENTARY_REFRESHMENTS = "ComplimentaryRefreshments"
    ALCOHOLIC_BEVERAGES_FOR_PURCHASE = "AlcoholicBeveragesForPurchase"
    COMPLIMENTARY_ALCOHOLIC_BEVERAGES = "ComplimentaryAlcoholicBeverages"
    FOOD_AND_BEVERAGES_FOR_PURCHASE = "FoodAndBeveragesForPurchase"
    NO_MEAL_SERVICE = "NoMealService"
    REFRESHMENTS_FOR_PURCHASE = "RefreshmentsForPurchase"


class TypeMileOrRouteBasedFare(Enum):
    """
    Whether the fare is Mile or Route based.
    """
    MILE = "Mile"
    ROUTE = "Route"
    BOTH = "Both"


@dataclass
class TypeNativeSearchModifier:
    """
    Parameters
    ----------
    value:
    provider_code: The host for which the NativeModfier being added to
    """
    class Meta:
        name = "typeNativeSearchModifier"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )


@dataclass
class TypeNonAirReservationRef:
    class Meta:
        name = "typeNonAirReservationRef"

    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )


class TypePosition(Enum):
    """Facility position with respect to position within the aircraft cabin.

    Possible values are – Left, Right, Center, Left Center, Right Center
    """
    LEFT = "Left"
    RIGHT = "Right"
    CENTER = "Center"
    LEFT_CENTER = "LeftCenter"
    RIGHT_CENTER = "RightCenter"


class TypePricingMethod(Enum):
    """
    The method at which the pricing data was acquired.

    Properties
    ----------
    AUTO: Automatically generated
    MANUAL: Agent has overridden default(s)
    MANUAL_FARE: Fare has been constructed by agent
    GUARANTEED: Fare is guaranteed
    INVALID: Invalid fare, e.g. due to name or itinerary change
    RESTORED: Ticketed stored fare has been restored
    TICKETED:
    UNTICKETABLE: Unable to ticket
    REPRICE: Need requote to ticket
    EXPIRED: Expired fare, older than 7 days
    AUTO_USING_PRIVATE_FARE: Agency private fares that are not
        guaranteed
    GUARANTEED_USING_AIRLINE_PRIVATE_FARE: Guaranteed fare using Airline
        private fare that was filed with a fare distributor.
    AIRLINE: Fare created as a result of Claim PNR which transfers data
        to GDS for ticketing purposes.
    AGENT_ASSISTED: Fare is created using Agent Asisted Pricing.
        Worldspan TKG FAX Line Documentation - AGENT ASSISTEDPRICED
    VERIFY_PRICE: Verify existing saved price on PNR . Worldspan TKG FAX
        Line Documentation -  AWAITING PRICE VERIFICATION
    ALT_SEGMENT_REMOVED_REPRICE: ALT Segment removed, Reprice pricing.
        Worldspan TKG FAX Line Documentation - AWAITING REPRICING ALT
        SEGS RMVD
    AUXILIARY_SEGMENT_REMOVED_REPRICE: AUX Segment removed, Reprice
        pricing. Worldspan TKG FAX Line Documentation -  AWAITING
        REPRICING AUX SEGS REMOVED
    DUPLICATE_SEGMENT_REMOVED_REPRICE: Duplicate Segment removed,
        Reprice pricing. Worldspan TKG FAX Line Documentation - AWAITING
        REPRICING DUPE SEGS REMOVED
    UNKNOWN: Any other kind of Pricing Method which is not supported by
        API.
    GUARANTEED_USING_AGENCY_PRIVATE_FARE: Guaranteed fare using Agency
        private fare that was filed with a fare distributor.
    AUTO_RAPID_REPRICE: Auto priced by rapid reprice. Provider 1P FCI
        code 4 .
    """
    AUTO = "Auto"
    MANUAL = "Manual"
    MANUAL_FARE = "ManualFare"
    GUARANTEED = "Guaranteed"
    INVALID = "Invalid"
    RESTORED = "Restored"
    TICKETED = "Ticketed"
    UNTICKETABLE = "Unticketable"
    REPRICE = "Reprice"
    EXPIRED = "Expired"
    AUTO_USING_PRIVATE_FARE = "AutoUsingPrivateFare"
    GUARANTEED_USING_AIRLINE_PRIVATE_FARE = "GuaranteedUsingAirlinePrivateFare"
    AIRLINE = "Airline"
    AGENT_ASSISTED = "AgentAssisted"
    VERIFY_PRICE = "VerifyPrice"
    ALT_SEGMENT_REMOVED_REPRICE = "AltSegmentRemovedReprice"
    AUXILIARY_SEGMENT_REMOVED_REPRICE = "AuxiliarySegmentRemovedReprice"
    DUPLICATE_SEGMENT_REMOVED_REPRICE = "DuplicateSegmentRemovedReprice"
    UNKNOWN = "Unknown"
    GUARANTEED_USING_AGENCY_PRIVATE_FARE = "GuaranteedUsingAgencyPrivateFare"
    AUTO_RAPID_REPRICE = "AutoRapidReprice"


class TypePrivateFare(Enum):
    """List the types of private fares, Agency private fare, Airline private
    Fare and Unknown.

    Also, this enumaration list includes PrivateFare to indetify private
    fares for GDSs where we can not identify specific private fares.
    """
    UNKNOWN_TYPE = "UnknownType"
    PRIVATE_FARE = "PrivateFare"
    AGENCY_PRIVATE_FARE = "AgencyPrivateFare"
    AIRLINE_PRIVATE_FARE = "AirlinePrivateFare"


class TypePurposeCode(Enum):
    """
    List of valid Purpose Codes.

    Properties
    ----------
    BUSINESS: Business
    PLEASURE: Pleasure
    CHARTER_SERVICE: Charter Service
    """
    BUSINESS = "Business"
    PLEASURE = "Pleasure"
    CHARTER_SERVICE = "CharterService"


class TypeReportingType(Enum):
    """
    The valid reporting types.
    """
    AVAILABILITY_FAILURE = "AvailabilityFailure"
    PRICE_DISCREPANCIES = "PriceDiscrepancies"
    MARRIAGE_DISCREPANCIES = "MarriageDiscrepancies"
    SUCCESS = "Success"
    SCHEDULE_DISCREPANCIES = "ScheduleDiscrepancies"


class TypeRowLocation(Enum):
    """Facility Position with respect to a Row.

    Possible values are Rear, Front
    """
    REAR = "Rear"
    FRONT = "Front"


class TypeSeatAvailability(Enum):
    """
    Seat availability info of a seat map.
    """
    AVAILABLE = "Available"
    OCCUPIED = "Occupied"
    RESERVED = "Reserved"
    ADVANCED_BOARDING_PASS = "AdvancedBoardingPass"
    INTERLINE_CHECKIN = "InterlineCheckin"
    CODESHARE = "Codeshare"
    PROTECTED = "Protected"
    PARTNER_AIRLINE = "PartnerAirline"
    ADV_SEAT_SELECTION = "AdvSeatSelection"
    BLOCKED = "Blocked"
    EXTRA = "Extra"
    RBDRESTRICTION = "RBDRestriction"
    GROUP = "Group"
    NO_SEAT = "NoSeat"
    UNOCCUPIED_BUT_NOT_ELIGIBLE = "UnoccupiedButNotEligible"


@dataclass
class TypeSegmentRef:
    class Meta:
        name = "typeSegmentRef"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeStayUnit(Enum):
    """
    Units for the Length of Stay.
    """
    MINUTES = "Minutes"
    HOURS = "Hours"
    DAYS = "Days"
    MONTHS = "Months"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class TypeTcrstatus(Enum):
    UNKNOWN = "Unknown"
    CONFIRMED = "Confirmed"
    REFUNDED = "Refunded"
    EXCHANGED = "Exchanged"
    CANCELLED = "Cancelled"
    PENDING = "Pending"


@dataclass
class TypeTextElement:
    """
    Parameters
    ----------
    value:
    type:
    language_code: ISO 639 two-character language codes are used to
        retrieve specific information in the requested language. For
        Rich Content and Branding, language codes ZH-HANT (Chinese
        Traditional), ZH-HANS (Chinese Simplified), FR-CA (French
        Canadian) and PT-BR (Portuguese Brazil) can also be used. For
        RCH, language codes ENGB, ENUS, DEDE, DECH can also be used.
        Only certain services support this attribute. Providers: ACH,
        RCH, 1G, 1V, 1P, 1J.
    """
    class Meta:
        name = "typeTextElement"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    language_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Attribute",
        }
    )


@dataclass
class TypeTicketModifierAccountingType:
    """Ticketing Modifier used to add accounting.

    - discount information.
    """
    class Meta:
        name = "typeTicketModifierAccountingType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "required": True,
        }
    )


@dataclass
class TypeTicketModifierAmountType:
    """
    Ticketing Modifier used to alter a fare amount before or during the
    ticketing operation.

    Parameters
    ----------
    amount: Amount associated with a ticketing modifier
    """
    class Meta:
        name = "typeTicketModifierAmountType"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TypeTicketModifierPercentType:
    """
    Ticketing Modifier used to alter a fare percentage before or during the
    ticketing operation.

    Parameters
    ----------
    percent: Percent associated with a ticketing modifier
    """
    class Meta:
        name = "typeTicketModifierPercentType"

    percent: Optional[str] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
            "required": True,
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )


@dataclass
class TypeTicketModifierValueType:
    """
    Ticketing Modifier used to add value discount information.

    Parameters
    ----------
    value:
    net_fare_value: Treat the value as net fare discount information
    """
    class Meta:
        name = "typeTicketModifierValueType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "required": True,
        }
    )
    net_fare_value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NetFareValue",
            "type": "Attribute",
        }
    )


class TypeTripType(Enum):
    """
    Used in Low Fare Search to better target the results.
    """
    CHEAPEST = "Cheapest"
    QUICKEST = "Quickest"
    MOST_CONVENIENT = "MostConvenient"
    LEISURE = "Leisure"
    BUSINESS = "Business"
    LUXURY = "Luxury"
    PREFER_FIRST = "PreferFirst"
    BUSINESS_OR_FIRST = "BusinessOrFirst"
    NO_PENALTY = "NoPenalty"


@dataclass
class TypeUnitOfMeasure:
    """
    Parameters
    ----------
    value:
    unit: Unit values would be lb,Lb,kg etc.
    """
    class Meta:
        name = "typeUnitOfMeasure"

    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        }
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Attribute",
        }
    )


class TypeUnitWeight(Enum):
    """
    The available units of weight.
    """
    KILOGRAMS = "Kilograms"
    POUNDS = "Pounds"


class TypeVarianceIndicator(Enum):
    """
    Type code for Variance.
    """
    EARLY = "Early"
    LATE = "Late"


class TypeVarianceType(Enum):
    """
    Type code for Variance.
    """
    ACTUAL = "Actual"
    ESTIMATED = "Estimated"
    CANCELED = "Canceled"
    DIVERSION = "Diversion"


@dataclass
class Apisrequirements:
    """
    Specific details for APIS Requirements.

    Parameters
    ----------
    document:
    key: Unique identifier for this APIS Requirements - use this key
        when a single APIS Requirements is shared by multiple elements.
    level: Applicability level of the Document. Required, Supported,
        API_Supported or Unknown
    gender_required:
    date_of_birth_required:
    required_documents: What are required documents for the APIS
        Requirement. One, FirstAndOneOther or All
    nationality_required: Nationality of the traveler is required for
        booking for some suppliers.
    """
    class Meta:
        name = "APISRequirements"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    document: List[Document] = field(
        default_factory=list,
        metadata={
            "name": "Document",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    level: Optional[str] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
        }
    )
    gender_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GenderRequired",
            "type": "Attribute",
        }
    )
    date_of_birth_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DateOfBirthRequired",
            "type": "Attribute",
        }
    )
    required_documents: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequiredDocuments",
            "type": "Attribute",
        }
    )
    nationality_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NationalityRequired",
            "type": "Attribute",
        }
    )


@dataclass
class Affiliations:
    """
    Affiliations related for pre pay profiles.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    travel_arranger: List[TravelArranger] = field(
        default_factory=list,
        metadata={
            "name": "TravelArranger",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirAvailInfo:
    """Matches class of service information with availability counts.

    Only provided on search results.

    Parameters
    ----------
    booking_code_info:
    fare_token_info: Associates Fare with HostToken
    provider_code:
    host_token_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_code_info: List[BookingCodeInfo] = field(
        default_factory=list,
        metadata={
            "name": "BookingCodeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_token_info: List["AirAvailInfo.FareTokenInfo"] = field(
        default_factory=list,
        metadata={
            "name": "FareTokenInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    host_token_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        }
    )

    @dataclass
    class FareTokenInfo:
        fare_info_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "FareInfoRef",
                "type": "Attribute",
                "required": True,
            }
        )
        host_token_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "HostTokenRef",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class AirBaseReq(BaseReq):
    """
    Context for Requests and Responses.
    """


@dataclass
class AirExchangeBundleTotal:
    """
    Total exchange and penalty information for one ticket number.

    Parameters
    ----------
    air_exchange_info:
    penalty: Only used within an AirExchangeQuoteRsp
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_exchange_info: Optional[AirExchangeInfo] = field(
        default=None,
        metadata={
            "name": "AirExchangeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    penalty: List[CommonPenalty] = field(
        default_factory=list,
        metadata={
            "name": "Penalty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeEligibilityReq(BaseReq):
    """
    Request to determine if the fares in an itinerary are exchangeable.

    Parameters
    ----------
    provider_reservation_info: Provider:1P - Represents a valid Provider
        Reservation/PNR whose itinerary is to be exchanged
    type: Type choices are "Detail" or "Summary"  Default will be
        Summary
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    provider_reservation_info: Optional["AirExchangeEligibilityReq.ProviderReservationInfo"] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "required": True,
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
    class ProviderReservationInfo:
        provider_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProviderCode",
                "type": "Attribute",
                "required": True,
                "min_length": 2,
                "max_length": 5,
            }
        )
        provider_locator_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProviderLocatorCode",
                "type": "Attribute",
                "required": True,
                "max_length": 15,
            }
        )


@dataclass
class AirExchangeModifiers:
    """
    Provides controls and switches for the Exchange process.

    Parameters
    ----------
    contract_codes:
    booking_date:
    ticketing_date:
    account_code:
    ticket_designator:
    allow_penalty_fares:
    private_fares_only:
    universal_record_locator_code: Which UniversalRecord should this new
        reservation be applied to. If blank, then a new one is created.
    provider_locator_code: Which Provider reservation does this
        reservation get added to.
    provider_code: To be used with ProviderLocatorCode, which host the
        reservation being added to belongs to.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    contract_codes: Optional["AirExchangeModifiers.ContractCodes"] = field(
        default=None,
        metadata={
            "name": "ContractCodes",
            "type": "Element",
        }
    )
    booking_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingDate",
            "type": "Attribute",
        }
    )
    ticketing_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketingDate",
            "type": "Attribute",
        }
    )
    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        }
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        }
    )
    allow_penalty_fares: bool = field(
        default=True,
        metadata={
            "name": "AllowPenaltyFares",
            "type": "Attribute",
        }
    )
    private_fares_only: bool = field(
        default=False,
        metadata={
            "name": "PrivateFaresOnly",
            "type": "Attribute",
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
        }
    )

    @dataclass
    class ContractCodes:
        contract_code: List[ContractCode] = field(
            default_factory=list,
            metadata={
                "name": "ContractCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class AirExchangeTicketBundle:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
            "min_length": 1,
            "max_length": 13,
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 2,
        }
    )
    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )


@dataclass
class AirFareDiscount:
    """
    Fare Discounts.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    percentage: Optional[float] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Attribute",
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    discount_method: Optional[TypeFareDiscount] = field(
        default=None,
        metadata={
            "name": "DiscountMethod",
            "type": "Attribute",
        }
    )


@dataclass
class AirFareRuleCategory:
    """
    A collection of fare rule category codes.

    Parameters
    ----------
    category_code: The Category Code for Air Fare Rule.
    fare_info_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    category_code: List[TypeFareRuleCategoryCode] = field(
        default_factory=list,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        }
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        }
    )


@dataclass
class AirPrePayReq(BaseReq):
    """
    Flight Pass Request.

    Parameters
    ----------
    list_search: Provider: ACH.
    pre_pay_retrieve: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    list_search: Optional["AirPrePayReq.ListSearch"] = field(
        default=None,
        metadata={
            "name": "ListSearch",
            "type": "Element",
        }
    )
    pre_pay_retrieve: Optional["AirPrePayReq.PrePayRetrieve"] = field(
        default=None,
        metadata={
            "name": "PrePayRetrieve",
            "type": "Element",
        }
    )

    @dataclass
    class ListSearch:
        """
        Parameters
        ----------
        person_name_search: Customer name detail for searching flight
            pass content.
        loyalty_card: Customer loyalty card for searching flight pass
            content.
        start_from_result: Start index of the section of flight pass
            numbers that is being requested.
        max_results: Max Number of Flight Passes being requested for.
        """
        person_name_search: Optional[PersonNameSearch] = field(
            default=None,
            metadata={
                "name": "PersonNameSearch",
                "type": "Element",
            }
        )
        loyalty_card: List[LoyaltyCard] = field(
            default_factory=list,
            metadata={
                "name": "LoyaltyCard",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "max_occurs": 999,
            }
        )
        start_from_result: Optional[int] = field(
            default=None,
            metadata={
                "name": "StartFromResult",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
            }
        )
        max_results: Optional[int] = field(
            default=None,
            metadata={
                "name": "MaxResults",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 200,
            }
        )

    @dataclass
    class PrePayRetrieve:
        """
        Parameters
        ----------
        id: Pre pay id to retrieved,example flight pass  number
        type: Pre pay id type,example 'FlightPass'
        """
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 36,
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
class AirPricingAdjustment:
    """This is a container to adjust price of AirPricingInfo.

    Pass zero values to remove existing adjustment.

    Parameters
    ----------
    adjustment:
    key: Key of AirPricingInfo from booking.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    adjustment: Optional[Adjustment] = field(
        default=None,
        metadata={
            "name": "Adjustment",
            "type": "Element",
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AirPricingPayment:
    """AirPricing Payment information - used to
    associate a FormOfPayment withiin the UR with one or more
    AirPricingInfos"""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    payment: List[Payment] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AirRefundInfo:
    """
    Provides results of a refund quote.

    Parameters
    ----------
    refund_remark:
    refund_amount:
    retain_amount:
    refund_fee: Refund fee for ACH/1P
    refundable_taxes: 1P - None : All taxes are not refundable. Unknown
        : Refundability of taxes are not known.
    filed_currency: 1P  Currency of filed CAT33 refund fee
    conversion_rate: 1P - Currency conversion rate used for conversion
        between FiledCurrency and PCC base currency in which the
        response is returned.
    taxes: 1P - The total value of taxes.
    original_ticket_total: 1P - The original ticket amount.
    forfeit_amount:
    retain: This indicates whether any amount is retained by the
        provider.
    refund: This indicates whether carrier/host supports refund for the
        correcponding pnr.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    refund_remark: List[RefundRemark] = field(
        default_factory=list,
        metadata={
            "name": "RefundRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    refund_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
        }
    )
    retain_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetainAmount",
            "type": "Attribute",
        }
    )
    refund_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundFee",
            "type": "Attribute",
        }
    )
    refundable_taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundableTaxes",
            "type": "Attribute",
        }
    )
    filed_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "length": 3,
        }
    )
    conversion_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ConversionRate",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    original_ticket_total: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalTicketTotal",
            "type": "Attribute",
        }
    )
    forfeit_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForfeitAmount",
            "type": "Attribute",
        }
    )
    retain: bool = field(
        default=False,
        metadata={
            "name": "Retain",
            "type": "Attribute",
        }
    )
    refund: bool = field(
        default=False,
        metadata={
            "name": "Refund",
            "type": "Attribute",
        }
    )


@dataclass
class AirRefundQuoteReq(BaseReq):
    """
    Request to quote a refund for an itinerary.

    Parameters
    ----------
    ticket_number: Provider: ACH.
    tcrnumber: Provider: ACH-The identifying number for a Ticketless Air
        Reservation
    air_refund_modifiers: Provider: ACH.
    host_token: Provider: ACH.
    provider_reservation_info: Provider: 1P - Represents a valid
        Provider Reservation/PNR whose itinerary is to be requested
    ignore: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 13,
        }
    )
    tcrnumber: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TCRNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_refund_modifiers: Optional[AirRefundModifiers] = field(
        default=None,
        metadata={
            "name": "AirRefundModifiers",
            "type": "Element",
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    provider_reservation_info: List["AirRefundQuoteReq.ProviderReservationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ignore: bool = field(
        default=False,
        metadata={
            "name": "Ignore",
            "type": "Attribute",
        }
    )

    @dataclass
    class ProviderReservationInfo:
        provider_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProviderCode",
                "type": "Attribute",
                "required": True,
                "min_length": 2,
                "max_length": 5,
            }
        )
        provider_locator_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProviderLocatorCode",
                "type": "Attribute",
                "required": True,
                "max_length": 15,
            }
        )


@dataclass
class AirRetrieveDocumentReq(BaseReq):
    """Retrieve the post booking information for a PNR.

    ETRs will be returned for standard carriers. TCRs will be returned
    for Ticketless carriers. If the locator is send on a standard
    carrier, all ETRs will be retrieved.

    Parameters
    ----------
    air_reservation_locator_code: Provider: 1G,1V,1P,1J.
    ticket_number: Provider: 1G,1V,1P,1J.
    tcrnumber: Provider: 1G,1V,1P,1J-The identifying number for a
        Ticketless Air Reservation.
    return_restrictions: Will return a response which includes a set of
        restrictions associated with the document.
    return_pricing: Provider: 1G,1V,1P,1J-Will return a response which
        includes the pricing associated with the ETR.
    retrieve_mco: When true, returns MCO Information. The default value
        is false.
    universal_record_locator_code: Contains the Locator Code of the
        Universal Record that houses this reservation.
    provider_code: Contains the Provider Code of the provider that
        houses this reservation.
    provider_locator_code: Contains the Locator Code of the Provider
        Reservation that houses this reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 13,
        }
    )
    tcrnumber: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TCRNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    return_restrictions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnRestrictions",
            "type": "Attribute",
        }
    )
    return_pricing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnPricing",
            "type": "Attribute",
        }
    )
    retrieve_mco: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RetrieveMCO",
            "type": "Attribute",
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )


@dataclass
class AirSegmentDetails:
    """
    An Air marketable travel segment.

    Parameters
    ----------
    passenger_details_ref:
    brand_id:
    booking_code_list: Lists classes of service and their counts
        separated by delimiter |.
    key:
    provider_code:
    carrier:
    origin: The IATA location code for this origination of this entity.
    destination: The IATA location code for this destination of this
        entity.
    departure_time: The date and time at which this entity departs. This
        does not include time zone information since it can be derived
        from the origin location.
    arrival_time: The date and time at which this entity arrives at the
        destination. This does not include time zone information since
        it can be derived from the origin location.
    equipment:
    class_of_service:
    cabin_class:
    operating_carrier: The actual carrier that is operating the flight.
    flight_number: Flight Number for the Search Leg Detail.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    passenger_details_ref: List[PassengerDetailsRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerDetailsRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    brand_id: List[BrandId] = field(
        default_factory=list,
        metadata={
            "name": "BrandID",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    booking_code_list: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingCodeList",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
            "required": True,
        }
    )
    equipment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Attribute",
            "length": 3,
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        }
    )
    operating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )


@dataclass
class AirSegmentPricingModifiers:
    """Specifies modifiers that a particular segment should be priced in.

    If this is used, then there must be one for each AirSegment in the
    AirItinerary.

    Parameters
    ----------
    permitted_booking_codes:
    air_segment_ref:
    cabin_class:
    account_code:
    prohibit_advance_purchase_fares:
    prohibit_non_refundable_fares:
    prohibit_penalty_fares:
    fare_basis_code: The fare basis code to be used for pricing.
    fare_break: Fare break point modifier to instruct Fares where it
        should or should not break the fare.
    connection_indicator: ConnectionIndicator attribute will be used to
        map connection indicators AvailabilityAndPricing, TurnAround and
        Stopover. This attribute is for Wordspan/1P only.
    brand_tier: Modifier to price by specific brand tier number.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    permitted_booking_codes: Optional["AirSegmentPricingModifiers.PermittedBookingCodes"] = field(
        default=None,
        metadata={
            "name": "PermittedBookingCodes",
            "type": "Element",
        }
    )
    air_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Attribute",
        }
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        }
    )
    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        }
    )
    prohibit_advance_purchase_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitAdvancePurchaseFares",
            "type": "Attribute",
        }
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonRefundableFares",
            "type": "Attribute",
        }
    )
    prohibit_penalty_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitPenaltyFares",
            "type": "Attribute",
        }
    )
    fare_basis_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasisCode",
            "type": "Attribute",
        }
    )
    fare_break: Optional[TypeFareBreak] = field(
        default=None,
        metadata={
            "name": "FareBreak",
            "type": "Attribute",
        }
    )
    connection_indicator: Optional[TypeConnectionIndicator] = field(
        default=None,
        metadata={
            "name": "ConnectionIndicator",
            "type": "Attribute",
        }
    )
    brand_tier: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandTier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )

    @dataclass
    class PermittedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata={
                "name": "BookingCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class AirTicketingModifiers:
    """
    Modifiers used during ticketing.

    Parameters
    ----------
    document_modifiers:
    air_pricing_info_ref:
    tour_code: Allows an agency to modify the tour code information
        during ticket issuance. Providers supported: Worldspan and JAL.
    ticket_endorsement: Allows an agency to add user defined ticketing
        endorsements in the ticket. Providers supported: Worldspan and
        JAL.
    commission: Allows an agency to add the commission to a new or
        different commission rate which will be applied at time of
        ticketing. The commission Modifier allows the user specify how
        the commission change is to applied. Providers supported:
        Worldspan and JAL.
    form_of_payment: FormOfPayment information to be used as ticketing
        modifier at the time of ticketing. Providers supported: Galileo,
        Apollo, Worldspan and JAL.
    credit_card_auth: CreditCardAuth information to be used as ticketing
        modifier at the time of ticketing. Providers supported: Galileo,
        Apollo, Worldspan and JAL.
    payment: Provide Payment for FOP. Providers supported: Galileo,
        Apollo, Worldspan and JAL.
    plating_carrier: The Plating Carrier used for this ticket
    ticketed_fare_override: It is a modifier to allow re-issuance of
        tickets for stored fares which are already ticketed. Providers
        supported are 1P/1J
    suppress_tax_and_fee: Allow to suppress Taxand Fee in ticketing
        response.Providers supported: Worldspan and JAL.
    no_comparison_sfq: 1P/1J - Set to "true" to include the no
        comparison overide #NC to override the existing SFQ and issue
        the ticket. Only valid for AirTicketingReq, not valid  for
        AirExchangeTicketingReq.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    document_modifiers: Optional[DocumentModifiers] = field(
        default=None,
        metadata={
            "name": "DocumentModifiers",
            "type": "Element",
        }
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tour_code: Optional[TourCode] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Element",
        }
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata={
            "name": "TicketEndorsement",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    commission: Optional[Commission] = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    ticketed_fare_override: bool = field(
        default=False,
        metadata={
            "name": "TicketedFareOverride",
            "type": "Attribute",
        }
    )
    suppress_tax_and_fee: bool = field(
        default=False,
        metadata={
            "name": "SuppressTaxAndFee",
            "type": "Attribute",
        }
    )
    no_comparison_sfq: bool = field(
        default=False,
        metadata={
            "name": "NoComparisonSFQ",
            "type": "Attribute",
        }
    )


@dataclass
class AlternateLocationDistance:
    """
    Information about the Original Search Airport to Alternate Search Airport.

    Parameters
    ----------
    distance:
    key:
    search_location: The Searching City or Airport specified in the
        Request.
    alternate_location: The nearby Alternate City or Airport to
        SearchLocation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    distance: Optional[Distance] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    search_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "SearchLocation",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    alternate_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternateLocation",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )


@dataclass
class ApplicableSegment(TypeApplicableSegment):
    """
    Applicable air segment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AssociatedRemark(TypeAssociatedRemarkWithSegmentRef):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AsyncProviderSpecificResponse(BaseAsyncProviderSpecificResponse):
    """
    Identifies pending responses from a specific provider using MoreResults
    attribute.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AutoSeatAssignment:
    """
    Request object used to request seats automatically by seat type.

    Parameters
    ----------
    segment_ref: The segment that this assignment belongs to
    smoking: Indicates that the requested seat type should be a smoking
        seat.
    seat_type: The type of seat that is requested
    group: Indicates that this seat request is for group seating for all
        passengers. If no SegmentRef is included, group seating will be
        requested for all segments.
    booking_traveler_ref: The booking traveler that this seat assignment
        is for. If not entered, this applies to the primary booking
        traveler and other passengers are adjacent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
    smoking: bool = field(
        default=False,
        metadata={
            "name": "Smoking",
            "type": "Attribute",
        }
    )
    seat_type: Optional[TypeReqSeat] = field(
        default=None,
        metadata={
            "name": "SeatType",
            "type": "Attribute",
            "required": True,
        }
    )
    group: bool = field(
        default=False,
        metadata={
            "name": "Group",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class AvailableDiscount:
    """
    Parameters
    ----------
    loyalty_program: Customer Loyalty Program Detail.
    amount:
    percent:
    description:
    discount_qualifier:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    loyalty_program: List[LoyaltyProgram] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyProgram",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    percent: Optional[str] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    discount_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountQualifier",
            "type": "Attribute",
        }
    )


@dataclass
class AvailableSsr:
    """
    A wrapper for all the information regarding each of the available SSR.

    Parameters
    ----------
    ssr:
    ssrrules: Holds the rules for selecting the SSR in the itinerary
    industry_standard_ssr:
    """
    class Meta:
        name = "AvailableSSR"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    ssrrules: List[ServiceRuleType] = field(
        default_factory=list,
        metadata={
            "name": "SSRRules",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    industry_standard_ssr: List[IndustryStandardSsr] = field(
        default_factory=list,
        metadata={
            "name": "IndustryStandardSSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class BackOfficeHandOff:
    """
    Allows an agency to select the back office documents and also route to
    different host to produce for the itinerary.

    Parameters
    ----------
    type: The type of back office document,valid options are
        Accounting,Global,NonAccounting,NonAccountingRemote,Dual.
    location: This is required for NonAccountingRemote,Dual and Global
        type back office.
    pseudo_city_code: The PCC of the host system where it would be
        routed.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[TypeBackOffice] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )


@dataclass
class BaseBaggageAllowanceInfo:
    """This contains common elements that are used for Baggage Allowance info,
    carry-on allowance info and embargo Info.

    Supported providers are 1V/1G/1P/1J

    Parameters
    ----------
    urlinfo: Contains the text and URL information as published by
        carrier.
    text_info: Text information as published by carrier.
    origin:
    destination:
    carrier:
    """
    urlinfo: List[Urlinfo] = field(
        default_factory=list,
        metadata={
            "name": "URLInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    text_info: List[TextInfo] = field(
        default_factory=list,
        metadata={
            "name": "TextInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )


@dataclass
class BillingDetailItem:
    """
    The Billing Details Information.

    Parameters
    ----------
    name: Detailed Billing Information Name(e.g Personal ID, Account
        Number)
    data_type: Detailed Billing Information DataType (Alpha, Numeric,
        etc.)
    min_length: Detailed Billing Information Minimum Length.
    max_length: Detailed Billing Information Maximum Length.
    value: Detailed Billing Information Value
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    name: Optional[TypeBillingDetailsName] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    data_type: Optional[TypeBillingDetailsDataType] = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Attribute",
            "required": True,
        }
    )
    min_length: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinLength",
            "type": "Attribute",
            "required": True,
        }
    )
    max_length: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxLength",
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
class BundledService:
    """
    Displays the services bundled together.

    Parameters
    ----------
    carrier: Carrier the service is applicable.
    carrier_sub_code: Carrier sub code. True means the carrier used
        their own sub code. False means the carrier used an ATPCO sub
        code
    service_type: The type of service or what the service is used for,
        e.g. F type is flight type, meaning the service is used on a
        flight
    service_sub_code: The sub code of the service, e.g. OAA for Pre paid
        baggage
    name: Name of the bundled service.
    booking: Booking method for the bundled service, e..g SSR.
    occurrence: How many of the service are included in the bundled
        service.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    carrier_sub_code: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CarrierSubCode",
            "type": "Attribute",
        }
    )
    service_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceType",
            "type": "Attribute",
        }
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    booking: Optional[TypeBooking] = field(
        default=None,
        metadata={
            "name": "Booking",
            "type": "Attribute",
        }
    )
    occurrence: Optional[int] = field(
        default=None,
        metadata={
            "name": "Occurrence",
            "type": "Attribute",
        }
    )


@dataclass
class Chgtype:
    """
    PenFee list will be populated.
    """
    class Meta:
        name = "CHGType"

    pen_fee: List[PenFeeType] = field(
        default_factory=list,
        metadata={
            "name": "PenFee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 2,
        }
    )


@dataclass
class Co2Emissions:
    """
    The carbon emissions produced by the journey.

    Parameters
    ----------
    co2_emission:
    total_value: The total CO2 emission value for the journey
    unit: The unit used in the TotalValue attribute
    category: The category name of the type of cabin, either Economy or
        Premium.  Premium is any cabin that is not considered Economy
    source: The source responsible for the values
    """
    class Meta:
        name = "CO2Emissions"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    co2_emission: List[Co2Emission] = field(
        default_factory=list,
        metadata={
            "name": "CO2Emission",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    total_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "TotalValue",
            "type": "Attribute",
        }
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )


@dataclass
class CategoryDetailsType:
    """
    Parameters
    ----------
    category_details: For each category Details of Structured Fare Rules
    value:
    """
    category_details: List[ValueDetails] = field(
        default_factory=list,
        metadata={
            "name": "CategoryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 99,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Characteristic:
    """
    Parameters
    ----------
    value:
    position:
    row_location:
    padiscode: Industry standard code that defines seat and row
        characteristic.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
    position: Optional[TypePosition] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Attribute",
        }
    )
    row_location: Optional[TypeRowLocation] = field(
        default=None,
        metadata={
            "name": "RowLocation",
            "type": "Attribute",
        }
    )
    padiscode: Optional[str] = field(
        default=None,
        metadata={
            "name": "PADISCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 99,
        }
    )


@dataclass
class ChargesRules:
    """
    Fare Reference associated with the BookingRules.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    voluntary_changes: List["ChargesRules.VoluntaryChanges"] = field(
        default_factory=list,
        metadata={
            "name": "VoluntaryChanges",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    voluntary_refunds: List["ChargesRules.VoluntaryRefunds"] = field(
        default_factory=list,
        metadata={
            "name": "VoluntaryRefunds",
            "type": "Element",
            "max_occurs": 999,
        }
    )

    @dataclass
    class VoluntaryChanges:
        penalty: Optional[Penalty] = field(
            default=None,
            metadata={
                "name": "Penalty",
                "type": "Element",
            }
        )
        vol_change_ind: Optional[bool] = field(
            default=None,
            metadata={
                "name": "VolChangeInd",
                "type": "Attribute",
            }
        )

    @dataclass
    class VoluntaryRefunds:
        penalty: Optional[Penalty] = field(
            default=None,
            metadata={
                "name": "Penalty",
                "type": "Element",
            }
        )
        vol_change_ind: Optional[bool] = field(
            default=None,
            metadata={
                "name": "VolChangeInd",
                "type": "Attribute",
            }
        )


@dataclass
class ConjunctedTicketInfo:
    """
    Parameters
    ----------
    number:
    iatanumber:
    ticket_issue_date:
    ticketing_agent_sign_on:
    country_code: Contains Ticketed PCC’s Country code.
    status:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    iatanumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    ticket_issue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TicketIssueDate",
            "type": "Attribute",
        }
    )
    ticketing_agent_sign_on: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketingAgentSignOn",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    status: Optional[TypeTicketStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Coupon:
    """
    The flight coupon that resulted from the ticketing operation.

    Parameters
    ----------
    ticket_designator:
    key:
    coupon_number: The sequential number of this coupon.
    operating_carrier: The true carrier.
    operating_flight_number: The true carrier's flight number.
    marketing_carrier: If codeshare applies to this, this is the
        marketing carrier (as opposed to the operating carrier).
    marketing_flight_number: If codeshare applies to this, this is the
        marketing flight number (as opposed to the operating flight
        number).
    origin: Returns the airport or city code that defines the origin
        market for this fare.
    destination: Returns the airport or city code that defines the
        destination market for this fare.
    departure_time: The date and time at which this entity departs. This
        does not include time zone information since it can be derived
        from the origin location. In case of open segment this will not
        be returned.
    arrival_time: The date and time at which this entity arrives at the
        destination. This does not include time zone information since
        it can be derived from the origin location.
    stopover_code: Stopover code - indicator that stopover is allowed at
        Origin Airport or City.
    booking_class: Booked fare class for coupon.
    fare_basis: The fare basis code for this fare
    not_valid_before: Fare not valid before this date.
    not_valid_after: Fare not valid after this date.
    status: The status of this coupon returend from host is mapped as
        follows Code="A" Status="Airport Controlled" Code="C"
        Status="Checked In" Code="F" Status="Flown/Used" Code="L"
        Status="Boarded/Lifted" Code="O" Status="Open" Code="P"
        Status="Printed" Code="R" Status="Refunded" Code="E"
        Status="Exchanged" Code="V" Status="Void" Code="Z"
        Status="Archived/Carrier Modified" Code="U" Status="Unavailable"
        Code="S" Status="Suspended" Code="I" Status="Irregular Ops"
        Code="D" Status="Deleted/Removed" Code="X" Status="Unknown"
    segment_group: Indicates the grouping in which this segment resides
        based on Origin/Destination pairs in itinerary
    marriage_group: Airline Marrraige group indicator
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_designator: List[TicketDesignator] = field(
        default_factory=list,
        metadata={
            "name": "TicketDesignator",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    coupon_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "CouponNumber",
            "type": "Attribute",
        }
    )
    operating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    operating_flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatingFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    marketing_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarketingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    marketing_flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarketingFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        }
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    stopover_code: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StopoverCode",
            "type": "Attribute",
            "required": True,
        }
    )
    booking_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingClass",
            "type": "Attribute",
            "required": True,
            "max_length": 2,
        }
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
        }
    )
    not_valid_before: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        }
    )
    not_valid_after: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
            "max_length": 1,
        }
    )
    segment_group: Optional[int] = field(
        default=None,
        metadata={
            "name": "SegmentGroup",
            "type": "Attribute",
        }
    )
    marriage_group: Optional[int] = field(
        default=None,
        metadata={
            "name": "MarriageGroup",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class DestinationPurposeCode:
    """This code is required to indicate destination and purpose of Travel.

    It is applicable for Canada and Bermuda agency only. This is used by
    Worldspan.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    destination: Optional[TypeDestinationCode] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
        }
    )
    purpose: Optional[TypePurposeCode] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Dimension(TypeUnitOfMeasure):
    """
    Information related to Length,Height,Width of a baggage.

    Parameters
    ----------
    type: Type denotes Length,Height,Width of a baggage.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Emd:
    """
    Parameters
    ----------
    fulfillment_type: A one digit code specifying how the service must
        be fulfilled. See FulfillmentTypeDescription for the description
        of this value.
    fulfillment_type_description: EMD description.
    associated_item: The type of Optional Service.  The choices are
        Flight, Ticket, Merchandising, Rule Buster, Allowance,
        Chargeable Baggage, Carry On Baggage Allowance, Prepaid Baggage.
        Provider: 1G, 1V, 1P, 1J
    availability_charge_indicator: A one-letter code specifying whether
        the service is available or if there is a charge associated with
        it. X = Service not available F = No charge for service (free)
        and an EMD is not issued to reflect free service E = No charge
        for service (free) and an EMD is issued to reflect the free
        service. G = No charge for service (free), booking is not
        required and an EMD is not issued to reflect free service H = No
        charge for service (free), booking is not required, and an EMD
        is issued to reflect the free service. Blank = No application.
        Charges apply according to the data in the Service Fee fields.
    refund_reissue_indicator: An attribute specifying whether the
        service is refundable or reissuable.
    commissionable: True/False value to whether or not the service is
        comissionable.
    mileage_indicator: True/False value to whether or not the service
        has miles.
    location: 3 letter location code where the service will be availed.
    date: The date at which the service will be used.
    booking: Holds the booking description for the service, e.g., SSR.
    display_category: Describes when the service should be displayed.
    reusable: Identifies if the service can be re-used towards a future
        purchase.
    """
    class Meta:
        name = "EMD"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fulfillment_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "FulfillmentType",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 5,
        }
    )
    fulfillment_type_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "FulfillmentTypeDescription",
            "type": "Attribute",
        }
    )
    associated_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssociatedItem",
            "type": "Attribute",
        }
    )
    availability_charge_indicator: Optional[EmdAvailabilityChargeIndicator] = field(
        default=None,
        metadata={
            "name": "AvailabilityChargeIndicator",
            "type": "Attribute",
        }
    )
    refund_reissue_indicator: Optional[EmdRefundReissueIndicator] = field(
        default=None,
        metadata={
            "name": "RefundReissueIndicator",
            "type": "Attribute",
        }
    )
    commissionable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Commissionable",
            "type": "Attribute",
        }
    )
    mileage_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MileageIndicator",
            "type": "Attribute",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Attribute",
        }
    )
    booking: Optional[TypeBooking] = field(
        default=None,
        metadata={
            "name": "Booking",
            "type": "Attribute",
        }
    )
    display_category: Optional[TypeDisplayCategory] = field(
        default=None,
        metadata={
            "name": "DisplayCategory",
            "type": "Attribute",
        }
    )
    reusable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reusable",
            "type": "Attribute",
        }
    )


@dataclass
class Emdcommission:
    """Commission information to be used for EMD issuance.

    Supported providers are 1V/1G/1P/1J

    Parameters
    ----------
    type: Type of the commission applied.One of Amount/Percentage
    value: Value of the commission applied for EMD issuance.Could
        represent amount or percentage depending on the type
    currency_code: Currency of the commission amount applied.Applicable
        only with type - Amount
    """
    class Meta:
        name = "EMDCommission"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[TypeAdjustmentType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "length": 3,
        }
    )


@dataclass
class Emdcoupon:
    """The coupon information for the EMD issued.

    Supported providers are 1G/1V/1P/1J

    Parameters
    ----------
    number: Number of the EMD coupon
    status: Status of the coupon. Possible values Open, Void, Refunded,
        Exchanged, Irregular Operations,Airport Control, Checked In,
        Flown/Used, Boarded/Lifted, Suspended, Unknown
    svc_description: Description of the service related to the EMD
        Coupon
    consumed_at_issuance_ind: Indicates if the EMD coupon has been
        considered used as soon as issued.
    rfic: Reason For Issuance Code for the EMD coupon
    rfisc: Reason For Issueance Sub code for the EMD coupon
    rfidescription: Reason for Issueance Description for the EMD coupon
    origin: Departure Airport Code for the flight with which the Coupon
        is associated
    destination: Destination Airport Code for the flight with which the
        Coupon is associated
    flight_number: Flight Number of the flight with which the coupon is
        associated.
    present_to: Service provider to present the coupon to
    present_at: Location of service provider where this coupon should be
        presented at
    non_refundable_ind: Indicates whether the coupon is non-refundable
    marketing_carrier: Marketing carrier associated with the coupon
    key: System generated Key
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "EMDCoupon"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    svc_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcDescription",
            "type": "Attribute",
        }
    )
    consumed_at_issuance_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConsumedAtIssuanceInd",
            "type": "Attribute",
        }
    )
    rfic: Optional[str] = field(
        default=None,
        metadata={
            "name": "RFIC",
            "type": "Attribute",
            "required": True,
            "length": 1,
        }
    )
    rfisc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RFISC",
            "type": "Attribute",
        }
    )
    rfidescription: Optional[str] = field(
        default=None,
        metadata={
            "name": "RFIDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 86,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    present_to: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresentTo",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 71,
        }
    )
    present_at: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresentAt",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 71,
        }
    )
    non_refundable_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonRefundableInd",
            "type": "Attribute",
        }
    )
    marketing_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarketingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class EmdretrieveReq(BaseReq):
    """
    Electronic Miscellaneous Document retrieve request.Supported providers are
    1G/1V/1P/1J.

    Parameters
    ----------
    list_retrieve: Provider: 1G/1V/1P/1J-Information required for
        retrieval of list of EMDs
    detail_retrieve: Provider: 1G/1V/1P/1J-Information required for a
        detailed EMD retrieve
    """
    class Meta:
        name = "EMDRetrieveReq"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    list_retrieve: Optional["EmdretrieveReq.ListRetrieve"] = field(
        default=None,
        metadata={
            "name": "ListRetrieve",
            "type": "Element",
        }
    )
    detail_retrieve: Optional["EmdretrieveReq.DetailRetrieve"] = field(
        default=None,
        metadata={
            "name": "DetailRetrieve",
            "type": "Element",
        }
    )

    @dataclass
    class ListRetrieve:
        """
        Parameters
        ----------
        provider_reservation_detail: Provider reservation details to be
            provided to fetch list of EMDs associated with it.
        """
        provider_reservation_detail: Optional[ProviderReservationDetail] = field(
            default=None,
            metadata={
                "name": "ProviderReservationDetail",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "required": True,
            }
        )

    @dataclass
    class DetailRetrieve:
        """
        Parameters
        ----------
        provider_reservation_detail: Provider reservation locator to be
            specified for display operation, if mentioned along woth the
            EMD number then synchronization of that EMD is performed
            considering the same to be associated with the mentioned
            PNR.
        emdnumber: EMD number to be specified for display operation. If
            mentioned along with provider reservation detail then
            synchronization of that EMD is performed considering the
            same to be associated with the mentioned PNR.
        """
        provider_reservation_detail: Optional[ProviderReservationDetail] = field(
            default=None,
            metadata={
                "name": "ProviderReservationDetail",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
            }
        )
        emdnumber: Optional[str] = field(
            default=None,
            metadata={
                "name": "EMDNumber",
                "type": "Element",
                "required": True,
                "length": 13,
            }
        )


@dataclass
class EmbargoList:
    """List of embargoes.

    Provider: 1G, 1V, 1P, 1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    embargo: List[Embargo] = field(
        default_factory=list,
        metadata={
            "name": "Embargo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        }
    )


@dataclass
class ExchangePenaltyInfo:
    """
    Parameters
    ----------
    penalty_information:
    ptc:
    minimum_change_fee: Minimum change fee for changes to the itinerary.
    maximum_change_fee: Maximum change fee for changes  to the
        itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    penalty_information: List[PenaltyInformation] = field(
        default_factory=list,
        metadata={
            "name": "PenaltyInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ptc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTC",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    minimum_change_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinimumChangeFee",
            "type": "Attribute",
        }
    )
    maximum_change_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaximumChangeFee",
            "type": "Attribute",
        }
    )


@dataclass
class FareDetails:
    """
    Information about this fare component.

    Parameters
    ----------
    fare_ticket_designator:
    key: Fare key
    passenger_detail_ref: PassengerRef key
    fare_basis: The fare basis code for this fare
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_ticket_designator: Optional[FareTicketDesignator] = field(
        default=None,
        metadata={
            "name": "FareTicketDesignator",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    passenger_detail_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerDetailRef",
            "type": "Attribute",
            "required": True,
        }
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
            "max_length": 20,
        }
    )


@dataclass
class FareGuaranteeInfo:
    """
    The information related to fare guarantee details.

    Parameters
    ----------
    guarantee_date: The date till which the fare is guaranteed.
    guarantee_type: Determines the status of a fare for a passenger.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    guarantee_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "GuaranteeDate",
            "type": "Attribute",
        }
    )
    guarantee_type: Optional[TypeFareGuarantee] = field(
        default=None,
        metadata={
            "name": "GuaranteeType",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FareNote:
    """A simple textual fare note.

    Used within several other objects.

    Parameters
    ----------
    value:
    key:
    precedence:
    note_name:
    fare_info_message_ref:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    precedence: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precedence",
            "type": "Attribute",
        }
    )
    note_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoteName",
            "type": "Attribute",
        }
    )
    fare_info_message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoMessageRef",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class FareRemark:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    url: List[Url] = field(
        default_factory=list,
        metadata={
            "name": "URL",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
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
class FareRestrictionDate:
    """Fare restriction based on date ranges.

    StartDate and EndDate are strings representing respective dates. If
    a year component is present then it signifies an exact date. If only
    day and month components are present then it signifies a seasonal
    date, which means applicable for that date in any year

    Parameters
    ----------
    direction:
    start_date:
    end_date:
    end_date_indicator: This field indicates the end date/last date for
        which travel on the fare component being validated must be
        commenced or completed
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    direction: Optional[TypeFareDirectionality] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        }
    )
    end_date_indicator: Optional[FareRestrictionDateEndDateIndicator] = field(
        default=None,
        metadata={
            "name": "EndDateIndicator",
            "type": "Attribute",
        }
    )


@dataclass
class FareRestrictionDaysOfWeek:
    """
    Days of the week that the restriction applies too.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    direction: Optional[TypeFareDirectionality] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
        }
    )
    trip_type: Optional[TypeFareTripType] = field(
        default=None,
        metadata={
            "name": "TripType",
            "type": "Attribute",
        }
    )
    monday: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monday",
            "type": "Attribute",
        }
    )
    tuesday: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Tuesday",
            "type": "Attribute",
        }
    )
    wednesday: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Wednesday",
            "type": "Attribute",
        }
    )
    thursday: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Thursday",
            "type": "Attribute",
        }
    )
    friday: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Friday",
            "type": "Attribute",
        }
    )
    saturday: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Saturday",
            "type": "Attribute",
        }
    )
    sunday: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sunday",
            "type": "Attribute",
        }
    )


@dataclass
class FareRuleLookup:
    """
    Parameters to use for a fare rule lookup that is not associated with an Air
    Reservation Locator Code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    point_of_sale: Optional[PointOfSale] = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    departure_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        }
    )
    ticketing_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TicketingDate",
            "type": "Attribute",
        }
    )


@dataclass
class FareRuleShort:
    """
    Short Text Fare Rule.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_rule_name_value: List[FareRuleNameValue] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleNameValue",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    category: Optional[int] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TableNumber",
            "type": "Attribute",
        }
    )


@dataclass
class FareStatus:
    """
    Denotes the status of a particular fare.

    Parameters
    ----------
    fare_status_failure_info:
    code: The status of the fare.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_status_failure_info: Optional[FareStatusFailureInfo] = field(
        default=None,
        metadata={
            "name": "FareStatusFailureInfo",
            "type": "Element",
        }
    )
    code: Optional[TypeFareStatusCode] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FareSurcharge:
    """
    Surcharges for a fare component.

    Parameters
    ----------
    key:
    type:
    amount:
    segment_ref:
    coupon_ref: The coupon to which that surcharge is relative (if
        applicable)
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
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
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
    coupon_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CouponRef",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class FeeInfo(TypeFeeInfo):
    """
    A generic type of fee for those charges which are incurred by the
    passenger, but not necessarily shown on tickets.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class FlexExploreModifiers:
    """This is the container for a set of modifiers which allow the user to
    perform a special kind of low fare search, depicted as flex explore, based
    on different parameters like Area, Zone, Country, State, Specific
    locations, Distance around the actual destination of the itinerary.

    Applicable for providers 1G,1V,1P

    Parameters
    ----------
    destination: List of specific destinations for performing flex
        explore. Applicable only with flex explore type - Destination
    type: Type of flex explore to be performed
    radius: Radius around the destination of actual itinerary in which
        the search would be performed. Supported only with types -
        DistanceInMiles and DistanceInKilometers
    group_name: Group name for a set of destinations to be searched.
        Use with Type=Group. Group names are defined in the Search
        Control Console. Supported Providers:  1G/1V/1P
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    destination: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Destination",
            "type": "Element",
            "max_occurs": 59,
            "length": 3,
            "white_space": "collapse",
        }
    )
    type: Optional[FlexExploreModifiersType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    radius: Optional[int] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Attribute",
        }
    )
    group_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GroupName",
            "type": "Attribute",
            "max_length": 15,
        }
    )


@dataclass
class FlightInformationReq(BaseReq):
    """
    Request for the Flight Info of segments.

    Parameters
    ----------
    flight_info_criteria: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_info_criteria: List[FlightInfoCriteria] = field(
        default_factory=list,
        metadata={
            "name": "FlightInfoCriteria",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class GeneralTimeTable:
    """
    Parameters
    ----------
    days_of_operation:
    flight_origin:
    flight_destination:
    carrier_list:
    start_date:
    end_date:
    start_time: Flight start time of flight time tabel .
    end_time: Flight end time of flight time tabel .
    include_connection: Include or exclude connecting flights.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    days_of_operation: Optional[TypeDaysOfOperation] = field(
        default=None,
        metadata={
            "name": "DaysOfOperation",
            "type": "Element",
        }
    )
    flight_origin: Optional[TypeLocation] = field(
        default=None,
        metadata={
            "name": "FlightOrigin",
            "type": "Element",
            "required": True,
        }
    )
    flight_destination: Optional[TypeLocation] = field(
        default=None,
        metadata={
            "name": "FlightDestination",
            "type": "Element",
            "required": True,
        }
    )
    carrier_list: Optional[CarrierList] = field(
        default=None,
        metadata={
            "name": "CarrierList",
            "type": "Element",
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Attribute",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Attribute",
        }
    )
    include_connection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeConnection",
            "type": "Attribute",
        }
    )


@dataclass
class GroupedOptionInfo:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    grouped_option: List[GroupedOption] = field(
        default_factory=list,
        metadata={
            "name": "GroupedOption",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class HostTokenList:
    """
    The shared object list of Host Tokens.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class IncludeAddlBookingCodeInfo:
    """
    Used to include primary or secondary carrier's booking code details.

    Parameters
    ----------
    type: The type defines that the booking code info is for primary or
        secondary carrier.
    secondary_carrier: The secondary carrier code is required when type
        is secondary .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[TypeCarrierCode] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    secondary_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecondaryCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )


@dataclass
class InvoluntaryChange:
    """
    Specify the Ticket Endorsement value.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_endorsement: Optional[TicketEndorsement] = field(
        default=None,
        metadata={
            "name": "TicketEndorsement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Itinerary:
    """
    Allows an agency to select the itinenary option for ticket.

    Parameters
    ----------
    type: Specifies the type of itinenary option for ticket like Invoice
        type or Pocket itinenary.
    option: Specifies the itinerary option like NoFare,NoAmount.
    separate_indicator: Set to true if one itinerary to be printed per
        passenger.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[TypeItinerary] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    option: Optional[TypeItineraryOption] = field(
        default=None,
        metadata={
            "name": "Option",
            "type": "Attribute",
        }
    )
    separate_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SeparateIndicator",
            "type": "Attribute",
        }
    )


@dataclass
class Journey:
    """
    Information about all connecting segment list and total traveling time.

    Parameters
    ----------
    air_segment_ref:
    travel_time: Total traveling time that is difference between the
        departure time of the first segment and the arrival time of the
        last segments for that particular entire set of connection.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    travel_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        }
    )


@dataclass
class LandCharges:
    """
    Prints non-air charges on a document.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    tax: List[Tax] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Attribute",
        }
    )
    total: Optional[str] = field(
        default=None,
        metadata={
            "name": "Total",
            "type": "Attribute",
        }
    )
    miscellaneous: Optional[str] = field(
        default=None,
        metadata={
            "name": "Miscellaneous",
            "type": "Attribute",
        }
    )
    pre_paid: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrePaid",
            "type": "Attribute",
        }
    )
    deposit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Deposit",
            "type": "Attribute",
        }
    )


@dataclass
class Leg:
    """
    Information about the journey Leg.

    Parameters
    ----------
    leg_detail:
    key:
    group: Returns the Group Number for the leg.
    origin: Returns the origin airport or city code for the leg.
    destination: Returns the destination airport or city code for the
        leg.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    leg_detail: List[LegDetail] = field(
        default_factory=list,
        metadata={
            "name": "LegDetail",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    group: Optional[int] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Attribute",
            "required": True,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )


@dataclass
class LegPrice:
    """
    Information about the journey Leg Price.

    Parameters
    ----------
    leg_detail:
    key:
    total_price: The Total Prices for the Combination of Journey legs
        for this Price.
    approximate_total_price: The Converted Total Price in Agency's
        Default Currency Value
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    leg_detail: List[LegDetail] = field(
        default_factory=list,
        metadata={
            "name": "LegDetail",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
            "required": True,
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )


@dataclass
class ManualFareAdjustment:
    """
    Parameters
    ----------
    applied_on: Represents pricing component upon which manual
        increment/discount to be applied. Presently supported values are
        Base and Total. Other is present as a future place holder but
        presently no request processing logic is available for value
        Other
    adjustment_type: Represents process used for applying manual
        discount/increment. Presently supported values are Flat,
        Percentage.
    value: Represents value of increment/discount applied. Negative
        value is considered as discount whereas positive value
        represents increment
    passenger_ref: Represents passenger association.
    ticket_designator: Providers: 1p/1j
    fare_type: Providers: 1p/1j
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    applied_on: Optional[TypeAdjustmentTarget] = field(
        default=None,
        metadata={
            "name": "AppliedOn",
            "type": "Attribute",
            "required": True,
        }
    )
    adjustment_type: Optional[TypeAdjustmentType] = field(
        default=None,
        metadata={
            "name": "AdjustmentType",
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
    passenger_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerRef",
            "type": "Attribute",
        }
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        }
    )
    fare_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )


@dataclass
class Meals:
    """
    Available Meal Service.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[TypeMealService] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class MerchandisingPricingModifiers:
    """
    Parameters
    ----------
    account_code: The account code is used to get corporate discounted
        pricing on paid seats. Provider:ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 10,
        }
    )


@dataclass
class OptionalServiceModifiers:
    """
    Rich Content and Branding for an optional service.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    optional_service_modifier: List[OptionalServiceModifier] = field(
        default_factory=list,
        metadata={
            "name": "OptionalServiceModifier",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        }
    )


@dataclass
class OriginalItineraryDetails:
    """Used for rapid reprice to provide additional information about the
    original itinerary.

    Providers: 1G/1V/1P/1S/1A

    Parameters
    ----------
    itinerary_type: Values allowed are International or Domestic. This
        tells if the itinerary is international or domestic.
    bulk_ticket: Set to true and the itinerary is/will be a bulk ticket.
        Set to false and the itinerary being repriced will not be a bulk
        ticket. Default is false.
    ticketing_pcc: This is the PCC or SID where the ticket was issued
    ticketing_iata: This is the IATA where the ticket was issued.
    ticketing_country: This is the country where the ticket was issued.
    tour_code:
    ticketing_date: The date the repriced itinerary was ticketed
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    itinerary_type: Optional[TypeItineraryCode] = field(
        default=None,
        metadata={
            "name": "ItineraryType",
            "type": "Attribute",
        }
    )
    bulk_ticket: bool = field(
        default=False,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        }
    )
    ticketing_pcc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketingPCC",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    ticketing_iata: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketingIATA",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    ticketing_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketingCountry",
            "type": "Attribute",
            "length": 2,
        }
    )
    tour_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    ticketing_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TicketingDate",
            "type": "Attribute",
        }
    )


@dataclass
class Pcc:
    """
    Specify pseudo City.
    """
    class Meta:
        name = "PCC"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    override_pcc: Optional[OverridePcc] = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 5,
        }
    )
    ticket_agency: Optional[TicketAgency] = field(
        default=None,
        metadata={
            "name": "TicketAgency",
            "type": "Element",
        }
    )


@dataclass
class PassengerDetails:
    """
    Details of passenger.

    Parameters
    ----------
    loyalty_card_details:
    key: Passenger key
    code: Passenger code
    age: Passenger age
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    loyalty_card_details: List[LoyaltyCardDetails] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCardDetails",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 5,
        }
    )
    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        }
    )


@dataclass
class PermittedCabins:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    cabin_class: List[CabinClass] = field(
        default_factory=list,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )


@dataclass
class PermittedCarriers:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier: List[Carrier] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class PocketItineraryRemark(TypeAssociatedRemarkWithSegmentRef):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class PrePayId:
    """
    Pre pay unique identifier , example Flight Pass Number.

    Parameters
    ----------
    company_name: Supplier info that is specific to the pre pay Id
    id: This is the exact pre pay number. Example flight pass number
    type: Type of pre pay unique identifier,presently only available
        value is FlightPass.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    company_name: Optional[CompanyName] = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 36,
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
class PreferredBookingCodes:
    """
    This is the container to specify all preferred booking codes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata={
            "name": "BookingCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class PreferredCabins:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    cabin_class: Optional[CabinClass] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )


@dataclass
class PreferredCarriers:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier: List[Carrier] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class PricingDetails:
    """Used for rapid reprice.

    This is a response element.  Additional information about how
    pricing was obtain, messages, etc.  Providers: 1G/1V/1P/1S/1A

    Parameters
    ----------
    advisory_message: Advisory messages returned from the host.
    endorsement_text: Endorsement text returned from the host.
    waiver_text: Waiver text returned from the host.
    low_fare_pricing: This tells if Low Fare Finder was used.
    low_fare_found: This tells if the lowest fare was found.
    penalty_applies: This tells if penalties apply.
    discount_applies: This tells if a discount applies.
    itinerary_type: Values allowed are International or Domestic. This
        tells if the itinerary is international or domestic.
    validating_vendor_code: The vendor code of the validating carrier.
    for_ticketing_on_date: The ticketing date of the itinerary.
    last_date_to_ticket: The last date to issue the ticket.
    form_of_refund: How the refund will be issued. Values will be MCO or
        FormOfPayment
    account_code:
    bankers_selling_rate: The selling rate at time of quote.
    pricing_type: Ties with the RepricingModifiers sent in the request
        and tells how the itinerary was priced.
    conversion_rate: The conversion rate at the time of quote.
    rate_of_exchange: The exchange rate at time of quote.
    original_ticket_currency: The currency of the original ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    advisory_message: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AdvisoryMessage",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    endorsement_text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EndorsementText",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    waiver_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "WaiverText",
            "type": "Element",
        }
    )
    low_fare_pricing: bool = field(
        default=False,
        metadata={
            "name": "LowFarePricing",
            "type": "Attribute",
        }
    )
    low_fare_found: bool = field(
        default=False,
        metadata={
            "name": "LowFareFound",
            "type": "Attribute",
        }
    )
    penalty_applies: bool = field(
        default=False,
        metadata={
            "name": "PenaltyApplies",
            "type": "Attribute",
        }
    )
    discount_applies: bool = field(
        default=False,
        metadata={
            "name": "DiscountApplies",
            "type": "Attribute",
        }
    )
    itinerary_type: Optional[TypeItineraryCode] = field(
        default=None,
        metadata={
            "name": "ItineraryType",
            "type": "Attribute",
        }
    )
    validating_vendor_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidatingVendorCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    for_ticketing_on_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ForTicketingOnDate",
            "type": "Attribute",
        }
    )
    last_date_to_ticket: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LastDateToTicket",
            "type": "Attribute",
        }
    )
    form_of_refund: Optional[TypeFormOfRefund] = field(
        default=None,
        metadata={
            "name": "FormOfRefund",
            "type": "Attribute",
        }
    )
    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        }
    )
    bankers_selling_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BankersSellingRate",
            "type": "Attribute",
        }
    )
    pricing_type: Optional[TypePricingType] = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Attribute",
        }
    )
    conversion_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ConversionRate",
            "type": "Attribute",
        }
    )
    rate_of_exchange: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RateOfExchange",
            "type": "Attribute",
        }
    )
    original_ticket_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalTicketCurrency",
            "type": "Attribute",
            "length": 3,
        }
    )


@dataclass
class ProhibitedCabins:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    cabin_class: List[CabinClass] = field(
        default_factory=list,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )


@dataclass
class ProhibitedCarriers:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier: List[Carrier] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class RefundFailureInfo:
    """
    Will be optionally returned as part of AirRefunTicketingRsp if one or all
    ticket refund requests fail.

    Parameters
    ----------
    ticket_number:
    name:
    tcrnumber: The identifying number for a Ticketless Air Reservation.
    booking_traveler_ref:
    code:
    message:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_length": 1,
            "max_length": 13,
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "TCRNumber",
            "type": "Element",
        }
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
        }
    )


@dataclass
class RelatedTraveler:
    """
    Detailed related Traveler information for pre pay profiles.

    Parameters
    ----------
    loyalty_card: Traveler loyalty card detail
    person_name: Traveler name detail
    credits_used: Traveler pre pay credit detail
    status_code: Traveler status code(One of Marked for
        deletion,Lapsed,Terminated,Active,Inactive)
    relation: Relation to the pre pay id. Example flight pass user
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    person_name: Optional[PersonName] = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
        }
    )
    credits_used: Optional["RelatedTraveler.CreditsUsed"] = field(
        default=None,
        metadata={
            "name": "CreditsUsed",
            "type": "Element",
        }
    )
    status_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Attribute",
        }
    )
    relation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Relation",
            "type": "Attribute",
        }
    )

    @dataclass
    class CreditsUsed:
        used_credit: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "UsedCredit",
                "type": "Attribute",
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Attribute",
                "length": 3,
            }
        )


@dataclass
class RetrieveLowFareSearchReq(BaseReq):
    """
    Retrieve low fare search responses that were initiated by an asynchronous
    request.

    Parameters
    ----------
    search_id: Provider: 1G,1V,1P,1J,ACH-SearchID to be used for
        Asynchronous LowFareSearch Request
    provider_code: Provider: 1G,1V,1P,1J,ACH-Provider code of a specific
        host
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    search_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SearchId",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )


@dataclass
class RoutingRules:
    """
    Rules related to routing.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    routing: List["RoutingRules.Routing"] = field(
        default_factory=list,
        metadata={
            "name": "Routing",
            "type": "Element",
            "max_occurs": 999,
        }
    )

    @dataclass
    class Routing:
        direction_info: List["RoutingRules.Routing.DirectionInfo"] = field(
            default_factory=list,
            metadata={
                "name": "DirectionInfo",
                "type": "Element",
                "max_occurs": 999,
            }
        )
        routing_constructed_ind: Optional[bool] = field(
            default=None,
            metadata={
                "name": "RoutingConstructedInd",
                "type": "Attribute",
            }
        )
        number: Optional[str] = field(
            default=None,
            metadata={
                "name": "Number",
                "type": "Attribute",
            }
        )
        routing_restriction: Optional[str] = field(
            default=None,
            metadata={
                "name": "RoutingRestriction",
                "type": "Attribute",
            }
        )

        @dataclass
        class DirectionInfo:
            location_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "LocationCode",
                    "type": "Attribute",
                    "length": 3,
                    "white_space": "collapse",
                }
            )
            direction: Optional[DirectionInfoDirection] = field(
                default=None,
                metadata={
                    "name": "Direction",
                    "type": "Attribute",
                }
            )


@dataclass
class RuleAdvancedPurchase:
    """Container for rules regarding advance purchase restrictions.

    TicketingEarliestDate and TicketingLatestDate are strings
    representing respective dates. If a year component is present then
    it signifies an exact date. If only day and month components are
    present then it signifies a seasonal date, which means applicable
    for that date in any year

    Parameters
    ----------
    reservation_latest_period:
    reservation_latest_unit:
    ticketing_earliest_date:
    ticketing_latest_date:
    more_rules_present: If true, specifies that advance purchase
        information will be present in fare rules.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    reservation_latest_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLatestPeriod",
            "type": "Attribute",
        }
    )
    reservation_latest_unit: Optional[TypeStayUnit] = field(
        default=None,
        metadata={
            "name": "ReservationLatestUnit",
            "type": "Attribute",
        }
    )
    ticketing_earliest_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketingEarliestDate",
            "type": "Attribute",
        }
    )
    ticketing_latest_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketingLatestDate",
            "type": "Attribute",
        }
    )
    more_rules_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreRulesPresent",
            "type": "Attribute",
        }
    )


@dataclass
class SearchTraveler(TypePassengerType):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_seat_assignment: List[AirSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "AirSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class SegmentSelect:
    """
    To be used to pass the selected segment.

    Parameters
    ----------
    air_segment_ref: Reference to AirSegment from an Air Reservation.
    hotel_reservation_ref: Specify the locator code of Hotel reservation
        if it needs to be considered as Auxiliary segment
    vehicle_reservation_ref: Specify the locator code of Vehicle
        reservation if it needs to be considered as Auxiliary segment
    passive_segment_ref: Reference to PassiveSegment from a Passive
        Reservation.Specify the passive segment if it needs to be
        considered as Auxiliary segment
    all_confirmed_air: Set to true to consider all Confirmed segments
        including active and passive and set to false to discard
        confirmed segments
    all_waitlisted_air: Set to true to consider all Waitlisted segments
        and false to discard all waitlisted segments
    all_hotel: Set to true to consider all Hotel reservations as
        Auxiliary segment and false to discard all Hotel reservations
    all_vehicle: Set to true to consider all Vehicle reservations as
        Auxiliary segment and false to discard all Vehicle reservations
    all_passive: Set to true to consider all Passive segments as
        Auxiliary segment and false to discard passive segments
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_reservation_ref: List[TypeNonAirReservationRef] = field(
        default_factory=list,
        metadata={
            "name": "HotelReservationRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_reservation_ref: List[TypeNonAirReservationRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleReservationRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    passive_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    all_confirmed_air: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllConfirmedAir",
            "type": "Attribute",
        }
    )
    all_waitlisted_air: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllWaitlistedAir",
            "type": "Attribute",
        }
    )
    all_hotel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllHotel",
            "type": "Attribute",
        }
    )
    all_vehicle: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllVehicle",
            "type": "Attribute",
        }
    )
    all_passive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllPassive",
            "type": "Attribute",
        }
    )


@dataclass
class SelectionModifiers:
    """Modifiers supported for selection of services during EMD Issuance.

    Supported providers are 1V/1G/1P/1J

    Parameters
    ----------
    air_segment_ref: References to airsegments for which EMDs will be
        generated on all the associated services.
    svc_segment_ref: SVC segment reference to which the EMD is being
        issued
    supplier_code: Supplier/Vendor code for which EMDs will be generated
        on all the associated services. Required if PNR contains more
        than one supplier.
    rfic: Reason for issuance code for which EMDs will be generated on
        all the associated services.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    svc_segment_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SvcSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    rfic: Optional[str] = field(
        default=None,
        metadata={
            "name": "RFIC",
            "type": "Attribute",
            "length": 1,
        }
    )


@dataclass
class ServiceAssociations:
    """
    Parameters
    ----------
    applicable_segment: Applicable air segment associated with this
        brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    applicable_segment: List["ServiceAssociations.ApplicableSegment"] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )

    @dataclass
    class ApplicableSegment:
        """
        Parameters
        ----------
        response_message:
        optional_service_ref:
        key: Applicable air segment key
        """
        response_message: Optional[ResponseMessage] = field(
            default=None,
            metadata={
                "name": "ResponseMessage",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
            }
        )
        optional_service_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "OptionalServiceRef",
                "type": "Element",
            }
        )
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
            }
        )


@dataclass
class ServiceGroup:
    """The Service Group of the Ancillary Service.

    Providers: 1G, 1V, 1P, 1J, ACH

    Parameters
    ----------
    service_sub_group:
    code: The Service Group Code of the Ancillary Service.  Providers:
        1G, 1V, 1P, 1J, ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    service_sub_group: List[ServiceSubGroup] = field(
        default_factory=list,
        metadata={
            "name": "ServiceSubGroup",
            "type": "Element",
            "max_occurs": 15,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SolutionGroup:
    """
    Specifies the trip type and diversity of all or a subset of the result
    solutions.

    Parameters
    ----------
    permitted_account_codes:
    preferred_account_codes:
    prohibited_account_codes:
    permitted_point_of_sales:
    prohibited_point_of_sales:
    count: The number of solution to include in this group. If only one
        group specified, this can be left blank. If multiple groups
        specified, all counts must add up to the MaxResults of the
        request.
    trip_type: Specifies the trip type for this group of results. Allows
        targeting a result set to a particular set of characterists.
    diversification: Specifies the diversification of this group of
        results, if specified. Allows targeting a result set to ensure
        they contain more unique results.
    tag: An arbitrary name for this group of solutions. Will be returned
        with the solution for idetification.
    primary: Indicates that this is a primary SolutionGroup when using
        alternate pricing concepts
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    permitted_account_codes: Optional["SolutionGroup.PermittedAccountCodes"] = field(
        default=None,
        metadata={
            "name": "PermittedAccountCodes",
            "type": "Element",
        }
    )
    preferred_account_codes: Optional["SolutionGroup.PreferredAccountCodes"] = field(
        default=None,
        metadata={
            "name": "PreferredAccountCodes",
            "type": "Element",
        }
    )
    prohibited_account_codes: Optional["SolutionGroup.ProhibitedAccountCodes"] = field(
        default=None,
        metadata={
            "name": "ProhibitedAccountCodes",
            "type": "Element",
        }
    )
    permitted_point_of_sales: Optional["SolutionGroup.PermittedPointOfSales"] = field(
        default=None,
        metadata={
            "name": "PermittedPointOfSales",
            "type": "Element",
        }
    )
    prohibited_point_of_sales: Optional["SolutionGroup.ProhibitedPointOfSales"] = field(
        default=None,
        metadata={
            "name": "ProhibitedPointOfSales",
            "type": "Element",
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
        }
    )
    trip_type: Optional[TypeTripType] = field(
        default=None,
        metadata={
            "name": "TripType",
            "type": "Attribute",
            "required": True,
        }
    )
    diversification: Optional[TypeDiversity] = field(
        default=None,
        metadata={
            "name": "Diversification",
            "type": "Attribute",
        }
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Attribute",
            "max_length": 20,
        }
    )
    primary: bool = field(
        default=False,
        metadata={
            "name": "Primary",
            "type": "Attribute",
        }
    )

    @dataclass
    class PermittedAccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata={
                "name": "AccountCode",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class PreferredAccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata={
                "name": "AccountCode",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ProhibitedAccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata={
                "name": "AccountCode",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class PermittedPointOfSales:
        point_of_sale: List[PointOfSale] = field(
            default_factory=list,
            metadata={
                "name": "PointOfSale",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ProhibitedPointOfSales:
        point_of_sale: List[PointOfSale] = field(
            default_factory=list,
            metadata={
                "name": "PointOfSale",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class SpecificTimeTable:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_origin: Optional["SpecificTimeTable.FlightOrigin"] = field(
        default=None,
        metadata={
            "name": "FlightOrigin",
            "type": "Element",
        }
    )
    flight_destination: Optional["SpecificTimeTable.FlightDestination"] = field(
        default=None,
        metadata={
            "name": "FlightDestination",
            "type": "Element",
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
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
            "length": 2,
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )

    @dataclass
    class FlightOrigin:
        airport: Optional[Airport] = field(
            default=None,
            metadata={
                "name": "Airport",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "required": True,
            }
        )

    @dataclass
    class FlightDestination:
        airport: Optional[Airport] = field(
            default=None,
            metadata={
                "name": "Airport",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "required": True,
            }
        )


@dataclass
class Tcrinfo:
    """
    Parameters
    ----------
    status:
    date:
    tcrnumber: The identifying number for a Ticketless Air Reservation.
    provider_reservation_info_ref: Provider reservation reference key.
    """
    class Meta:
        name = "TCRInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    status: Optional[TypeTcrstatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Attribute",
        }
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "TCRNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TaxInfo(TypeTaxInfo):
    """
    The tax information for a.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class TermConditions:
    """
    The terms and conditions to be included in Fax details.

    Parameters
    ----------
    language_option:
    include_term_conditions: Specifies whether Term and Conditions
        included in the Fax or not .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    language_option: List[LanguageOption] = field(
        default_factory=list,
        metadata={
            "name": "LanguageOption",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    include_term_conditions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeTermConditions",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Text(TypeTextElement):
    """
    Type of Text, Eg-'Upsell','Marketing Agent','Marketing
    Consumer','Strapline','Rule'.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class TicketFailureInfo:
    """Will be optionally returned as part of AirTicketingRsp if one or all
    ticket requests fail.

    Atrributes are faiilure code, failure message, and passenger
    reference key. Passenger name is a child element.

    Parameters
    ----------
    air_pricing_info_ref: Returns related air pricing infos.
    name:
    code:
    message:
    booking_traveler_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Title(TypeTextElement):
    """The additional titles associated to the brand or optional service.

    Providers: ACH, RCH, 1G, 1V, 1P, 1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class Variance:
    """
    Indicates any variance in the requested flight.

    Parameters
    ----------
    type: Indicates type Variance, i.e. Actual, Estimated, Canceled and
        Diversion.
    time: Indicates time for Variance.
    indicator: Indicates VAriance Indicator, i.e. Early, Late.
    reason: Reason for Variance
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[TypeVarianceType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    time: Optional[str] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
        }
    )
    indicator: Optional[TypeVarianceIndicator] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Attribute",
        }
    )


@dataclass
class VoidDocumentInfo:
    """
    Container to represent document information.

    Parameters
    ----------
    document_number: Identifies the document number to be voided.
    document_type: Identifies the document type to be voided, Document
        Type can have four values like Service Fee, Paper Ticket , MCO
        and E-Ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    document_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        }
    )
    document_type: Optional[AttrDocumentDocumentType] = field(
        default=None,
        metadata={
            "name": "DocumentType",
            "type": "Attribute",
        }
    )


@dataclass
class VoidResultInfo:
    """
    List of Successful Or Failed void document results.

    Parameters
    ----------
    failure_remark: Container to show all provider failure information.
    document_number: Identifies the document number to be voided.
    document_type: Identifies the document type to be voided, Document
        Type can have four values like Service Fee, Paper Ticket , MCO
        and E-Ticket.
    result_type: Successful Or Failed result indicator.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    failure_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "FailureRemark",
            "type": "Element",
        }
    )
    document_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        }
    )
    document_type: Optional[AttrDocumentDocumentType] = field(
        default=None,
        metadata={
            "name": "DocumentType",
            "type": "Attribute",
        }
    )
    result_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResultType",
            "type": "Attribute",
        }
    )


@dataclass
class TypeFarePenalty:
    """
    Penalty applicable on a Fare for change/ cancellation etc- expressed in
    both Money and Percentage.

    Parameters
    ----------
    amount: The penalty (if any) - expressed as the actual amount of
        money. Both Amount and Percentage can be present.
    percentage: The penalty (if any) - expressed in percentage. Both
        Amount and Percentage can be present.
    penalty_applies:
    no_show: The No Show penalty (if any) to change/cancel the fare.
    """
    class Meta:
        name = "typeFarePenalty"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    percentage: Optional[str] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
    penalty_applies: Optional[TypeFarePenaltyPenaltyApplies] = field(
        default=None,
        metadata={
            "name": "PenaltyApplies",
            "type": "Attribute",
        }
    )
    no_show: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoShow",
            "type": "Attribute",
        }
    )


@dataclass
class TypeRestrictionLengthOfStay:
    """
    Length Of Stay Restriction ( e.g. 2 day minimum..)

    Parameters
    ----------
    length:
    stay_unit:
    stay_date:
    more_rules_present: If true, specifies that advance purchase
        information will be present in fare rules.
    """
    class Meta:
        name = "typeRestrictionLengthOfStay"

    length: Optional[int] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Attribute",
        }
    )
    stay_unit: Optional[TypeStayUnit] = field(
        default=None,
        metadata={
            "name": "StayUnit",
            "type": "Attribute",
        }
    )
    stay_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StayDate",
            "type": "Attribute",
        }
    )
    more_rules_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreRulesPresent",
            "type": "Attribute",
        }
    )


@dataclass
class TypeTaxInfoWithPaymentRef(TypeTaxInfo):
    """
    Parameters
    ----------
    payment_ref: This reference elements will associate relevant payment
        to this tax
    """
    class Meta:
        name = "typeTaxInfoWithPaymentRef"

    payment_ref: List[PaymentRef] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class TypeTicketFailureInfo:
    """
    Will be optionally returned as part if one or all ticketing requests fail.

    Parameters
    ----------
    ticket_number:
    name:
    tcrnumber: The identifying number for a Ticketless Air Reservation.
    booking_traveler_ref:
    code:
    message:
    """
    class Meta:
        name = "typeTicketFailureInfo"

    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_length": 1,
            "max_length": 13,
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "TCRNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
        }
    )


@dataclass
class TypeTicketingModifiersRef:
    class Meta:
        name = "typeTicketingModifiersRef"

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TypeWeight:
    class Meta:
        name = "typeWeight"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        }
    )
    unit: Optional[TypeUnitWeight] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Attribute",
        }
    )


@dataclass
class ApisrequirementsList:
    """
    The shared object list of APISRequirements.
    """
    class Meta:
        name = "APISRequirementsList"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    apisrequirements: List[Apisrequirements] = field(
        default_factory=list,
        metadata={
            "name": "APISRequirements",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeBundle:
    """
    Bundle exchange, pricing, and penalty information for one ticket number
    Used both in request and response.

    Parameters
    ----------
    air_exchange_info:
    air_pricing_info_ref:
    tax_info:
    penalty: Only used within an AirExchangeQuoteRsp
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_exchange_info: Optional[AirExchangeInfo] = field(
        default=None,
        metadata={
            "name": "AirExchangeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    penalty: List[CommonPenalty] = field(
        default_factory=list,
        metadata={
            "name": "Penalty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class AirFareRulesModifier:
    """
    The modifiers for Air Fare Rules.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_fare_rule_category: List[AirFareRuleCategory] = field(
        default_factory=list,
        metadata={
            "name": "AirFareRuleCategory",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirItineraryDetails:
    """
    Itinerary details containing brand details.

    Parameters
    ----------
    air_segment_details:
    passenger_details:
    key: Air itinerary details key
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_details: List[AirSegmentDetails] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 16,
        }
    )
    passenger_details: List[PassengerDetails] = field(
        default_factory=list,
        metadata={
            "name": "PassengerDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AirLegModifiers:
    """
    Parameters
    ----------
    permitted_cabins:
    preferred_cabins:
    permitted_carriers:
    prohibited_carriers:
    preferred_carriers:
    permitted_connection_points: This is the container to specify all
        permitted connection points. Applicable for 1G/1V/1P/1J.
    prohibited_connection_points: This is the container to specify all
        prohibited connection points. Applicable for 1G/1V/1P/1J.
    preferred_connection_points: This is the container to specify all
        preferred connection points. Applicable for 1G/1V only.
    permitted_booking_codes: This is the container to specify all
        permitted booking codes
    preferred_booking_codes:
    preferred_alliances:
    prohibited_booking_codes: This is the container to specify all
        prohibited booking codes
    disfavored_alliances:
    flight_type:
    anchor_flight_data:
    prohibit_overnight_layovers: If true, excludes connections if
        arrival time of first flight and departure time of second flight
        is on 2 different calendar days. When used in conjunction with
        MaxConnectionTime, it would exclude all connections if the
        connecting flights wait time exceeds the time specified in
        MaxConnectionTime.
    max_connection_time:
    return_first_available_only: If it is true then it will search for
        first available for the booking code designated or any booking
        code in same cabin.
    allow_direct_access: If it is true request will be sent directly to
        the carrier.
    prohibit_multi_airport_connection: Indicates whether to restrict
        multi-airport connections
    prefer_non_stop: When non-stops are preferred, the distribution of
        search results should skew heavily toward non-stop flights while
        still returning some one stop flights for comparison and price
        competitiveness. The search request will ‘boost' the preference
        towards non-stops. If true then Non Stop flights will be
        preferred.
    order_by: Indicates whether to sort by Journey Time, Deparature Time
        or Arrival Time
    max_journey_time: Maximum Journey Time for this leg (in hours) 0-99.
        Supported Providers 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    permitted_cabins: Optional[PermittedCabins] = field(
        default=None,
        metadata={
            "name": "PermittedCabins",
            "type": "Element",
        }
    )
    preferred_cabins: Optional[PreferredCabins] = field(
        default=None,
        metadata={
            "name": "PreferredCabins",
            "type": "Element",
        }
    )
    permitted_carriers: Optional[PermittedCarriers] = field(
        default=None,
        metadata={
            "name": "PermittedCarriers",
            "type": "Element",
        }
    )
    prohibited_carriers: Optional[ProhibitedCarriers] = field(
        default=None,
        metadata={
            "name": "ProhibitedCarriers",
            "type": "Element",
        }
    )
    preferred_carriers: Optional[PreferredCarriers] = field(
        default=None,
        metadata={
            "name": "PreferredCarriers",
            "type": "Element",
        }
    )
    permitted_connection_points: Optional["AirLegModifiers.PermittedConnectionPoints"] = field(
        default=None,
        metadata={
            "name": "PermittedConnectionPoints",
            "type": "Element",
        }
    )
    prohibited_connection_points: Optional["AirLegModifiers.ProhibitedConnectionPoints"] = field(
        default=None,
        metadata={
            "name": "ProhibitedConnectionPoints",
            "type": "Element",
        }
    )
    preferred_connection_points: Optional["AirLegModifiers.PreferredConnectionPoints"] = field(
        default=None,
        metadata={
            "name": "PreferredConnectionPoints",
            "type": "Element",
        }
    )
    permitted_booking_codes: Optional["AirLegModifiers.PermittedBookingCodes"] = field(
        default=None,
        metadata={
            "name": "PermittedBookingCodes",
            "type": "Element",
        }
    )
    preferred_booking_codes: Optional[PreferredBookingCodes] = field(
        default=None,
        metadata={
            "name": "PreferredBookingCodes",
            "type": "Element",
        }
    )
    preferred_alliances: Optional["AirLegModifiers.PreferredAlliances"] = field(
        default=None,
        metadata={
            "name": "PreferredAlliances",
            "type": "Element",
        }
    )
    prohibited_booking_codes: Optional["AirLegModifiers.ProhibitedBookingCodes"] = field(
        default=None,
        metadata={
            "name": "ProhibitedBookingCodes",
            "type": "Element",
        }
    )
    disfavored_alliances: Optional["AirLegModifiers.DisfavoredAlliances"] = field(
        default=None,
        metadata={
            "name": "DisfavoredAlliances",
            "type": "Element",
        }
    )
    flight_type: Optional[FlightType] = field(
        default=None,
        metadata={
            "name": "FlightType",
            "type": "Element",
        }
    )
    anchor_flight_data: Optional[TypeAnchorFlightData] = field(
        default=None,
        metadata={
            "name": "AnchorFlightData",
            "type": "Element",
        }
    )
    prohibit_overnight_layovers: bool = field(
        default=False,
        metadata={
            "name": "ProhibitOvernightLayovers",
            "type": "Attribute",
        }
    )
    max_connection_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxConnectionTime",
            "type": "Attribute",
        }
    )
    return_first_available_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnFirstAvailableOnly",
            "type": "Attribute",
        }
    )
    allow_direct_access: bool = field(
        default=False,
        metadata={
            "name": "AllowDirectAccess",
            "type": "Attribute",
        }
    )
    prohibit_multi_airport_connection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProhibitMultiAirportConnection",
            "type": "Attribute",
        }
    )
    prefer_non_stop: bool = field(
        default=False,
        metadata={
            "name": "PreferNonStop",
            "type": "Attribute",
        }
    )
    order_by: Optional[AirLegModifiersOrderBy] = field(
        default=None,
        metadata={
            "name": "OrderBy",
            "type": "Attribute",
        }
    )
    max_journey_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxJourneyTime",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 99,
        }
    )

    @dataclass
    class PermittedConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionPoint",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ProhibitedConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionPoint",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class PreferredConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionPoint",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 99,
            }
        )

    @dataclass
    class PermittedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata={
                "name": "BookingCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class PreferredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata={
                "name": "Alliance",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ProhibitedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata={
                "name": "BookingCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class DisfavoredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata={
                "name": "Alliance",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class AirRefundBundle:
    """
    Bundle refund, pricing, and penalty information for one ticket number Used
    both in request and response.

    Parameters
    ----------
    air_refund_info:
    name:
    tax_info:
    waiver_code:
    ticket_number:
    ptc: Specifies the passenger type code for 1P
    refund_type: Specifies whether this bundle was auto or manually
        generated
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_refund_info: Optional[AirRefundInfo] = field(
        default=None,
        metadata={
            "name": "AirRefundInfo",
            "type": "Element",
            "required": True,
        }
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
        }
    )
    ptc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTC",
            "type": "Attribute",
        }
    )
    refund_type: Optional[AirRefundBundleRefundType] = field(
        default=None,
        metadata={
            "name": "RefundType",
            "type": "Attribute",
        }
    )


@dataclass
class AirSearchModifiers:
    """
    Controls and switches for the Air Search request.

    Parameters
    ----------
    disfavored_providers:
    preferred_providers:
    disfavored_carriers:
    permitted_carriers:
    prohibited_carriers:
    preferred_carriers:
    permitted_cabins:
    preferred_cabins:
    preferred_alliances:
    disfavored_alliances:
    permitted_booking_codes: This is the container to specify all
        permitted booking codes
    preferred_booking_codes:
    prohibited_booking_codes: This is the container to specify all
        prohibited booking codes
    flight_type:
    max_layover_duration: This is the maximum duration the layover may
        have for each trip in the request. Supported providers 1P, 1J.
    native_search_modifier: Container for Native command modifiers.
        Providers supported : 1P
    distance_type:
    include_flight_details:
    allow_change_of_airport:
    prohibit_overnight_layovers: If true, excludes connections if
        arrival time of first flight and departure time of second flight
        is on 2 different calendar days. When used in conjunction with
        MaxConnectionTime, it would exclude all connections if the
        connecting flights wait time exceeds the time specified in
        MaxConnectionTime.
    max_solutions: The maximum number of solutions to return. Decreasing
        this number
    max_connection_time: The maximum anount of time (in minutes) that a
        solution can contain for connections between flights.
    search_weekends: A value of true indicates that search should be
        expanded to include weekend combinations, if applicable.
    include_extra_solutions: If true, indicates that search should be
        made for returning more solutions, if available. For example,
        for certain providers, premium members may have the facility to
        get more solutions. This attribute may have to be combined with
        other applicable modifiers (like SearchWeekends) to return more
        results.
    prohibit_multi_airport_connection: Indicates whether to restrict
        multi-airport connections
    prefer_non_stop: When non-stops are preferred, the distribution of
        search results should skew heavily toward non-stop flights while
        still returning some one stop flights for comparison and price
        competitiveness. The search request will ‘boost' the preference
        towards non-stops. If true then Non Stop flights will be
        preferred.
    order_by: Indicates whether to sort by Journey Time, Deparature Time
        or Arrival Time. Applicable to air availability only.
    exclude_open_jaw_airport: This option ensures that travel into/out
        of each location will be into/out of the same airport of that
        location. Values are true or false. Default value is 'false'. If
        value is true then open jaws are exclude. If false the open jaws
        are included. The supported providers: 1P, 1J
    exclude_ground_transportation: Indicates whether to allow the user
        to exclude ground transportation or not. Default value is
        'false'. If value is true then ground transportations are
        excluded. If false then ground transportations are included. The
        supported providers: 1P, 1J
    max_journey_time: Maximum Journey Time for all legs (in hours) 0-99.
        For LFS Supported Providers are 1G,1V,1P,1J. For AirAvail
        Supported Providers are 1G,1V.
    jet_service_only: Restricts results to Jet service flights only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    disfavored_providers: Optional["AirSearchModifiers.DisfavoredProviders"] = field(
        default=None,
        metadata={
            "name": "DisfavoredProviders",
            "type": "Element",
        }
    )
    preferred_providers: Optional["AirSearchModifiers.PreferredProviders"] = field(
        default=None,
        metadata={
            "name": "PreferredProviders",
            "type": "Element",
        }
    )
    disfavored_carriers: Optional["AirSearchModifiers.DisfavoredCarriers"] = field(
        default=None,
        metadata={
            "name": "DisfavoredCarriers",
            "type": "Element",
        }
    )
    permitted_carriers: Optional[PermittedCarriers] = field(
        default=None,
        metadata={
            "name": "PermittedCarriers",
            "type": "Element",
        }
    )
    prohibited_carriers: Optional[ProhibitedCarriers] = field(
        default=None,
        metadata={
            "name": "ProhibitedCarriers",
            "type": "Element",
        }
    )
    preferred_carriers: Optional[PreferredCarriers] = field(
        default=None,
        metadata={
            "name": "PreferredCarriers",
            "type": "Element",
        }
    )
    permitted_cabins: Optional[PermittedCabins] = field(
        default=None,
        metadata={
            "name": "PermittedCabins",
            "type": "Element",
        }
    )
    preferred_cabins: Optional[PreferredCabins] = field(
        default=None,
        metadata={
            "name": "PreferredCabins",
            "type": "Element",
        }
    )
    preferred_alliances: Optional["AirSearchModifiers.PreferredAlliances"] = field(
        default=None,
        metadata={
            "name": "PreferredAlliances",
            "type": "Element",
        }
    )
    disfavored_alliances: Optional["AirSearchModifiers.DisfavoredAlliances"] = field(
        default=None,
        metadata={
            "name": "DisfavoredAlliances",
            "type": "Element",
        }
    )
    permitted_booking_codes: Optional["AirSearchModifiers.PermittedBookingCodes"] = field(
        default=None,
        metadata={
            "name": "PermittedBookingCodes",
            "type": "Element",
        }
    )
    preferred_booking_codes: Optional[PreferredBookingCodes] = field(
        default=None,
        metadata={
            "name": "PreferredBookingCodes",
            "type": "Element",
        }
    )
    prohibited_booking_codes: Optional["AirSearchModifiers.ProhibitedBookingCodes"] = field(
        default=None,
        metadata={
            "name": "ProhibitedBookingCodes",
            "type": "Element",
        }
    )
    flight_type: Optional[FlightType] = field(
        default=None,
        metadata={
            "name": "FlightType",
            "type": "Element",
        }
    )
    max_layover_duration: Optional[MaxLayoverDurationType] = field(
        default=None,
        metadata={
            "name": "MaxLayoverDuration",
            "type": "Element",
        }
    )
    native_search_modifier: Optional[TypeNativeSearchModifier] = field(
        default=None,
        metadata={
            "name": "NativeSearchModifier",
            "type": "Element",
        }
    )
    distance_type: TypeDistance = field(
        default=TypeDistance.MI,
        metadata={
            "name": "DistanceType",
            "type": "Attribute",
        }
    )
    include_flight_details: bool = field(
        default=True,
        metadata={
            "name": "IncludeFlightDetails",
            "type": "Attribute",
        }
    )
    allow_change_of_airport: bool = field(
        default=True,
        metadata={
            "name": "AllowChangeOfAirport",
            "type": "Attribute",
        }
    )
    prohibit_overnight_layovers: bool = field(
        default=False,
        metadata={
            "name": "ProhibitOvernightLayovers",
            "type": "Attribute",
        }
    )
    max_solutions: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxSolutions",
            "type": "Attribute",
        }
    )
    max_connection_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxConnectionTime",
            "type": "Attribute",
        }
    )
    search_weekends: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SearchWeekends",
            "type": "Attribute",
        }
    )
    include_extra_solutions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeExtraSolutions",
            "type": "Attribute",
        }
    )
    prohibit_multi_airport_connection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProhibitMultiAirportConnection",
            "type": "Attribute",
        }
    )
    prefer_non_stop: bool = field(
        default=False,
        metadata={
            "name": "PreferNonStop",
            "type": "Attribute",
        }
    )
    order_by: Optional[AirSearchModifiersOrderBy] = field(
        default=None,
        metadata={
            "name": "OrderBy",
            "type": "Attribute",
        }
    )
    exclude_open_jaw_airport: bool = field(
        default=False,
        metadata={
            "name": "ExcludeOpenJawAirport",
            "type": "Attribute",
        }
    )
    exclude_ground_transportation: bool = field(
        default=False,
        metadata={
            "name": "ExcludeGroundTransportation",
            "type": "Attribute",
        }
    )
    max_journey_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxJourneyTime",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 99,
        }
    )
    jet_service_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "JetServiceOnly",
            "type": "Attribute",
        }
    )

    @dataclass
    class DisfavoredProviders:
        provider: List[Provider] = field(
            default_factory=list,
            metadata={
                "name": "Provider",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class PreferredProviders:
        provider: List[Provider] = field(
            default_factory=list,
            metadata={
                "name": "Provider",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class DisfavoredCarriers:
        carrier: List[Carrier] = field(
            default_factory=list,
            metadata={
                "name": "Carrier",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class PreferredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata={
                "name": "Alliance",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class DisfavoredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata={
                "name": "Alliance",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class PermittedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata={
                "name": "BookingCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ProhibitedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata={
                "name": "BookingCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class AirVoidDocumentReq(BaseReq):
    """
    Request to void all previously issued tickets for the PNR.

    Parameters
    ----------
    air_reservation_locator_code: Provider: 1G,1V.
    void_document_info: Provider: 1G,1V-All tickets that belong to this
        PNR must be enumerated here. Voiding only some tickets of a
        multi-ticket PNR not currently supported.
    show_etr: Provider: 1G,1V-If set as true, response will display the
        detailed ETR for successfully voided E-Tickets.
    provider_code: Provider: 1G,1V-Provider code of a specific host.
    provider_locator_code: Provider: 1G,1V-Contains the locator of the
        host reservation.
    validate_spanish_residency: Provider: 1G - If set as true, Spanish
        Residency will be validated for Provisioned Customers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    void_document_info: List[VoidDocumentInfo] = field(
        default_factory=list,
        metadata={
            "name": "VoidDocumentInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    show_etr: bool = field(
        default=False,
        metadata={
            "name": "ShowETR",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
        }
    )
    validate_spanish_residency: bool = field(
        default=False,
        metadata={
            "name": "ValidateSpanishResidency",
            "type": "Attribute",
        }
    )


@dataclass
class AlternateLocationDistanceList:
    """
    Provides the Distance Information between Original Search Airports or City
    to Alternate Search Airports.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    alternate_location_distance: List[AlternateLocationDistance] = field(
        default_factory=list,
        metadata={
            "name": "AlternateLocationDistance",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AlternateRoute:
    """
    Information about this Alternate Route component.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    leg: List[Leg] = field(
        default_factory=list,
        metadata={
            "name": "Leg",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AuditData:
    """
    Container for Pricing Audit Data.For providers 1P/1J.

    Parameters
    ----------
    tax_info:
    key:
    total_price: The total price for this entity including base price
        and all taxes.
    base_price: Represents the base price for this entity. This does not
        include any taxes or surcharges.
    approximate_total_price: The Converted total price in Default
        Currency for this entity including base price and all taxes.
    approximate_base_price: The Converted base price in Default Currency
        for this entity. This does not include any taxes or surcharges.
    equivalent_base_price: Represents the base price in the related
        currency for this entity. This does not include any taxes or
        surcharges.
    taxes: The aggregated amount of all the taxes that are associated
        with this entity. See the associated TaxInfo array for a
        breakdown of the individual taxes.
    fees: The aggregated amount of all the fees that are associated with
        this entity. See the associated FeeInfo array for a breakdown of
        the individual fees.
    services: The total cost for all optional services.
    approximate_taxes: The Converted tax amount in Default Currency.
    approximate_fees: The Converted fee amount in Default Currency.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: Optional[str] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )


@dataclass
class BaggageAllowance:
    """
    Free Baggage Allowance.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    number_of_pieces: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfPieces",
            "type": "Element",
        }
    )
    max_weight: Optional[TypeWeight] = field(
        default=None,
        metadata={
            "name": "MaxWeight",
            "type": "Element",
        }
    )


@dataclass
class BaggageRestriction:
    """
    Information related to  Baggage restriction rules .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    dimension: List[Dimension] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    max_weight: List[TypeUnitOfMeasure] = field(
        default_factory=list,
        metadata={
            "name": "MaxWeight",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    text_info: List[TextInfo] = field(
        default_factory=list,
        metadata={
            "name": "TextInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class BookingRules:
    """
    Rules related to pre pay booking.

    Parameters
    ----------
    booking_rules_fare_reference:
    rule_info: Pre pay booking rule information
    restriction: Booking restrictions for associated pre pay account
    document_required: Detail about required documents for this pre pay
        id
    gender_dob_required: Vendor populates if gender/DOB data is required
        in book.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_rules_fare_reference: List[BookingRulesFareReference] = field(
        default_factory=list,
        metadata={
            "name": "BookingRulesFareReference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rule_info: List["BookingRules.RuleInfo"] = field(
        default_factory=list,
        metadata={
            "name": "RuleInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    restriction: List[Restriction] = field(
        default_factory=list,
        metadata={
            "name": "Restriction",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    document_required: List[DocumentRequired] = field(
        default_factory=list,
        metadata={
            "name": "DocumentRequired",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    gender_dob_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GenderDobRequired",
            "type": "Attribute",
        }
    )

    @dataclass
    class RuleInfo:
        charges_rules: Optional[ChargesRules] = field(
            default=None,
            metadata={
                "name": "ChargesRules",
                "type": "Element",
            }
        )


@dataclass
class BrandingInfo:
    """Branding information for the Ancillary Service.

    Returned in Seat Map only.  Providers: 1G, 1V, 1P, 1J, ACH

    Parameters
    ----------
    price_range: The price range of the Ancillary Service.  Providers:
        1G, 1V, 1P, 1J, ACH
    text:
    title: The additional titles associated to the brand or optional
        service. Providers: ACH, 1G, 1V, 1P, 1J
    image_location:
    service_group:
    air_segment_ref: Specifies the AirSegment the branding information
        is for. Providers: ACH, 1G, 1V, 1P, 1J
    key:
    service_sub_code: The Service Sub Code of the Ancillary Service.
        Providers: 1G, 1V, 1P, 1J, ACH
    external_service_name: The external name of the Ancillary Service.
        Providers: 1G, 1V, 1P, 1J, ACH
    service_type: The type of Ancillary Service.  Providers: 1G, 1V, 1P,
        1J, ACH
    commercial_name: The commercial name of the Ancillary Service.
        Providers: 1G, 1V, 1P, 1J, ACH
    chargeable: Indicates if the optional service is not offered, is
        available for a charge, or is included in the brand.  Providers:
        1G, 1V, 1P, 1J, ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    price_range: List[PriceRange] = field(
        default_factory=list,
        metadata={
            "name": "PriceRange",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    text: List[Text] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata={
            "name": "ImageLocation",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    service_group: Optional[ServiceGroup] = field(
        default=None,
        metadata={
            "name": "ServiceGroup",
            "type": "Element",
        }
    )
    air_segment_ref: List[CommonTypeSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
        }
    )
    external_service_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalServiceName",
            "type": "Attribute",
        }
    )
    service_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceType",
            "type": "Attribute",
        }
    )
    commercial_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommercialName",
            "type": "Attribute",
            "required": True,
        }
    )
    chargeable: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chargeable",
            "type": "Attribute",
        }
    )


@dataclass
class BundledServices:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    bundled_service: List[BundledService] = field(
        default_factory=list,
        metadata={
            "name": "BundledService",
            "type": "Element",
            "max_occurs": 16,
        }
    )


@dataclass
class Connection:
    """
    Flight Connection Information.

    Parameters
    ----------
    fare_note:
    change_of_plane: Indicates the traveler must change planes between
        flights.
    change_of_terminal: Indicates the traveler must change terminals
        between flights.
    change_of_airport: Indicates the traveler must change airports
        between flights.
    stop_over: Indicates that there is a significant delay between
        flights (usually 12 hours or more)
    min_connection_time: The minimum time needed to connect between the
        two different destinations.
    duration: The actual duration (in minutes) between flights.
    segment_index: The sequential AirSegment number that this connection
        information applies to.
    flight_details_index: The sequential FlightDetails number that this
        connection information applies to.
    include_stop_over_to_fare_quote: The field determines to quote fares
        with or without stop overs,the values can be NoStopOver,StopOver
        and IgnoreSegment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_note: Optional[FareNote] = field(
        default=None,
        metadata={
            "name": "FareNote",
            "type": "Element",
        }
    )
    change_of_plane: bool = field(
        default=False,
        metadata={
            "name": "ChangeOfPlane",
            "type": "Attribute",
        }
    )
    change_of_terminal: bool = field(
        default=False,
        metadata={
            "name": "ChangeOfTerminal",
            "type": "Attribute",
        }
    )
    change_of_airport: bool = field(
        default=False,
        metadata={
            "name": "ChangeOfAirport",
            "type": "Attribute",
        }
    )
    stop_over: bool = field(
        default=False,
        metadata={
            "name": "StopOver",
            "type": "Attribute",
        }
    )
    min_connection_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinConnectionTime",
            "type": "Attribute",
        }
    )
    duration: Optional[int] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Attribute",
        }
    )
    segment_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SegmentIndex",
            "type": "Attribute",
        }
    )
    flight_details_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "FlightDetailsIndex",
            "type": "Attribute",
        }
    )
    include_stop_over_to_fare_quote: Optional[TypeIgnoreStopOver] = field(
        default=None,
        metadata={
            "name": "IncludeStopOverToFareQuote",
            "type": "Attribute",
        }
    )


@dataclass
class DetailedBillingInformation:
    """
    Container to send Detailed Billing Information for ticketing.

    Parameters
    ----------
    form_of_payment_ref:
    air_pricing_info_ref: Returns related air pricing infos.
    billing_detail_item:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    billing_detail_item: List[BillingDetailItem] = field(
        default_factory=list,
        metadata={
            "name": "BillingDetailItem",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class DocumentSelect:
    """
    Allows an agency to select the documents to produce for the itinerary.

    Parameters
    ----------
    back_office_hand_off:
    itinerary:
    issue_ticket_only: Set to true to alter system default of
        itinerary,ticket and back office.
    issue_electronic_ticket: Set to true for electronic tickets.
    fax_indicator: Set to true for providing fax details.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    back_office_hand_off: Optional[BackOfficeHandOff] = field(
        default=None,
        metadata={
            "name": "BackOfficeHandOff",
            "type": "Element",
        }
    )
    itinerary: Optional[Itinerary] = field(
        default=None,
        metadata={
            "name": "Itinerary",
            "type": "Element",
        }
    )
    issue_ticket_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IssueTicketOnly",
            "type": "Attribute",
        }
    )
    issue_electronic_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IssueElectronicTicket",
            "type": "Attribute",
        }
    )
    fax_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FaxIndicator",
            "type": "Attribute",
        }
    )


@dataclass
class EmdpricingInfo:
    """Fare related information for these electronic miscellaneous documents.

    Supported providers are 1G/1V/1P/1J
    """
    class Meta:
        name = "EMDPricingInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    base_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Attribute",
        }
    )
    total_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalFare",
            "type": "Attribute",
        }
    )
    total_tax: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalTax",
            "type": "Attribute",
        }
    )
    equiv_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivFare",
            "type": "Attribute",
        }
    )


@dataclass
class Emdsummary:
    """EMD summary information.

    Supported providers are 1G/1V/1P/1J

    Parameters
    ----------
    emdcoupon: The coupon information for the EMD issued.
    number: EMD Number
    primary_document_indicator: Indicates whether the EMD is a primary
        EMD.
    in_conjunction_with: Returns the number of the Primary EMD, if this
        EMD is a conjunctive EMD
    associated_ticket_number: This number indicates the e-Ticket number
        associated with this EMD
    plating_carrier: Plating carrier code for which this EMD is issued
    issue_date: Issue Date for this EMD
    key: System generated Key
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "EMDSummary"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdcoupon: List[Emdcoupon] = field(
        default_factory=list,
        metadata={
            "name": "EMDCoupon",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "length": 13,
        }
    )
    primary_document_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrimaryDocumentIndicator",
            "type": "Attribute",
        }
    )
    in_conjunction_with: Optional[str] = field(
        default=None,
        metadata={
            "name": "InConjunctionWith",
            "type": "Attribute",
            "length": 13,
        }
    )
    associated_ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssociatedTicketNumber",
            "type": "Attribute",
            "length": 13,
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    issue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class ElectronicMiscDocument:
    """Electronic miscellaneous document.

    Supported providers are 1G/1V/1P/1J

    Parameters
    ----------
    emdcoupon: The coupon information for the EMD issued.
    number: EMD Number
    primary_document_indicator: Indicates whether the EMD is a primary
        EMD.
    in_conjunction_with: Returns the number of the Primary EMD, if this
        EMD is a conjunctive EMD
    associated_ticket_number: This number indicates the e-Ticket number
        associated with this EMD
    plating_carrier: Plating carrier code for which this EMD is issued
    issue_date: Issue Date for this EMD
    status: Status of the EMD calculated on the basis of coupon status.
        Possible values Open, Void, Refunded, Exchanged, Irregular
        Operations,Airport Control, Checked In, Flown/Used,
        Boarded/Lifted, Suspended, Unknown
    key: System generated Key
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdcoupon: List[Emdcoupon] = field(
        default_factory=list,
        metadata={
            "name": "EMDCoupon",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "length": 13,
        }
    )
    primary_document_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrimaryDocumentIndicator",
            "type": "Attribute",
        }
    )
    in_conjunction_with: Optional[str] = field(
        default=None,
        metadata={
            "name": "InConjunctionWith",
            "type": "Attribute",
            "length": 13,
        }
    )
    associated_ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssociatedTicketNumber",
            "type": "Attribute",
            "length": 13,
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    issue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Attribute",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class EmbargoInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Embargo.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class Enumeration:
    """
    Provides the capability to group the results into differnt trip type and
    diversification strategies.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    solution_group: List[SolutionGroup] = field(
        default_factory=list,
        metadata={
            "name": "SolutionGroup",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class ExchangeEligibilityInfo:
    """
    Parameters
    ----------
    exchange_penalty_info:
    eligible_fares: Identifies which fares are eligible for Exchange
    refundable_fares: Fares eligible for refund: All, Some, None
    passed_automation_checks: Indicates whether the itinerary passed
        initial validation for automated exchange
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    exchange_penalty_info: List[ExchangePenaltyInfo] = field(
        default_factory=list,
        metadata={
            "name": "ExchangePenaltyInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    eligible_fares: Optional[str] = field(
        default=None,
        metadata={
            "name": "EligibleFares",
            "type": "Attribute",
        }
    )
    refundable_fares: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundableFares",
            "type": "Attribute",
        }
    )
    passed_automation_checks: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PassedAutomationChecks",
            "type": "Attribute",
        }
    )


@dataclass
class ExpertSolution:
    """
    Information about Expert Solution Route component retrieved from Knowledge
    Base.

    Parameters
    ----------
    leg_price:
    key:
    total_price: The Total Price for the Solution.
    approximate_total_price: The Converted Total Price in Agency's
        Default Currency Value
    created_date: The Date on which this solution was created
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    leg_price: List[LegPrice] = field(
        default_factory=list,
        metadata={
            "name": "LegPrice",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    created_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CreatedDate",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Facility:
    """
    The facility definition for a part of a row or a seat map.

    Parameters
    ----------
    characteristic:
    remark:
    passenger_seat_price:
    tax_info: Tax information related to seat price. This is presently
        populated for MCH and ACH content. Applicable providers are
        MCH/ACH
    emd:
    service_data:
    tour_code:
    type: The type of facility
    seat_code: If a seat type, the seat identifier
    availability: If a seat type, the availability of the seat
    seat_price: The price of the seat, if applicable.
    paid: Set to True if either SeatPrice or GroupSeatPrice are
        returned.
    service_sub_code: The service subcode associated with the Facility
    ssrcode: The SSR Code associated with the Facility
    issuance_reason: A one-letter RFIC value filed by the airline in
        each Optional Service will be mapped to this attribute. RFIC is
        IATA Reason for Issuance Code. Possible codes are A (Air
        transportation),B (Surface Transportation),C(Bagage),
        D(Financial Impact),E(Airport
        Services),F(Merchandise),G(Inflight Services),I (Individual
        Airline use).
    base_seat_price: Price of the seats excluding Taxes.
    taxes: Tax amount for the seat price.
    quantity: The number of units availed for each optional service
        (e.g. 2 baggage availed will be specified as 2 in quantity for
        optional service BAGGAGE)
    sequence_number: The sequence number associated with the
        OptionalService
    inclusive_of_tax: Identifies if the service was filed with a fee
        that is inclusive of tax.
    interline_settlement_allowed: Identifies if the interline settlement
        is allowed in service .
    geography_specification: Sector, Portion, Journey.
    source: The Source of the optional service. The source can be ACH,
        MCE, or MCH.
    optional_service_ref: References the OptionalService for the
        Row/Facility. Providers: ACH, 1G, 1V, 1P, 1J
    seat_information_ref: Specifies the seat information for the seat.
        Providers: ACH, 1G, 1V, 1P, 1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    characteristic: List[Characteristic] = field(
        default_factory=list,
        metadata={
            "name": "Characteristic",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    passenger_seat_price: List[PassengerSeatPrice] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSeatPrice",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    emd: Optional[Emd] = field(
        default=None,
        metadata={
            "name": "EMD",
            "type": "Element",
        }
    )
    service_data: List[ServiceData] = field(
        default_factory=list,
        metadata={
            "name": "ServiceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    tour_code: Optional[TourCode] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Element",
        }
    )
    type: Optional[TypeFacility] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    seat_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatCode",
            "type": "Attribute",
        }
    )
    availability: Optional[TypeSeatAvailability] = field(
        default=None,
        metadata={
            "name": "Availability",
            "type": "Attribute",
        }
    )
    seat_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatPrice",
            "type": "Attribute",
        }
    )
    paid: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Paid",
            "type": "Attribute",
        }
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    ssrcode: Optional[str] = field(
        default=None,
        metadata={
            "name": "SSRCode",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 4,
        }
    )
    issuance_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuanceReason",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 1,
        }
    )
    base_seat_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseSeatPrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Attribute",
        }
    )
    inclusive_of_tax: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InclusiveOfTax",
            "type": "Attribute",
        }
    )
    interline_settlement_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InterlineSettlementAllowed",
            "type": "Attribute",
        }
    )
    geography_specification: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeographySpecification",
            "type": "Attribute",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
        }
    )
    optional_service_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptionalServiceRef",
            "type": "Attribute",
        }
    )
    seat_information_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatInformationRef",
            "type": "Attribute",
        }
    )


@dataclass
class FareNoteList:
    """
    The shared object list of Notes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata={
            "name": "FareNote",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class FareRemarkList:
    """
    The shared object list of FareInfos.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_remark: List[FareRemark] = field(
        default_factory=list,
        metadata={
            "name": "FareRemark",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class FareRestriction:
    """
    Fare Restriction.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_restriction_days_of_week: List[FareRestrictionDaysOfWeek] = field(
        default_factory=list,
        metadata={
            "name": "FareRestrictionDaysOfWeek",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    fare_restriction_date: List[FareRestrictionDate] = field(
        default_factory=list,
        metadata={
            "name": "FareRestrictionDate",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_restriction_sale_date: Optional[FareRestrictionSaleDate] = field(
        default=None,
        metadata={
            "name": "FareRestrictionSaleDate",
            "type": "Element",
        }
    )
    fare_restriction_seasonal: List[FareRestrictionSeasonal] = field(
        default_factory=list,
        metadata={
            "name": "FareRestrictionSeasonal",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_restrictiontype: Optional[TypeFareRestrictionType] = field(
        default=None,
        metadata={
            "name": "FareRestrictiontype",
            "type": "Attribute",
        }
    )


@dataclass
class FareRuleCategoryTypes:
    """
    Parameters
    ----------
    category_details: To indicate details of which category is displayed
    variable_category_details: If the specified category of Structured
        Fare Rules is of variable lenght
    value:
    """
    category_details: List[ValueDetails] = field(
        default_factory=list,
        metadata={
            "name": "CategoryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 99,
        }
    )
    variable_category_details: List[CategoryDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "VariableCategoryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 99,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FareRulesFilter:
    """Fare Rules Filter about this fare component.

    Applicable Providers are 1P,1J,1G,1V.

    Parameters
    ----------
    refundability: Refundability/Penalty Fare Rules about this fare
        component.
    latest_ticketing_time: For Future Use
    chg: For Penalties
    min: For Minimum Stay
    max: For Maximum Stay
    adv: For Advance Res/Tkt
    oth: Other
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    refundability: Optional["FareRulesFilter.Refundability"] = field(
        default=None,
        metadata={
            "name": "Refundability",
            "type": "Element",
        }
    )
    latest_ticketing_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LatestTicketingTime",
            "type": "Element",
        }
    )
    chg: Optional[Chgtype] = field(
        default=None,
        metadata={
            "name": "CHG",
            "type": "Element",
        }
    )
    min: Optional[Mintype] = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Element",
        }
    )
    max: Optional[Maxtype] = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Element",
        }
    )
    adv: Optional[Advtype] = field(
        default=None,
        metadata={
            "name": "ADV",
            "type": "Element",
        }
    )
    oth: Optional[Othtype] = field(
        default=None,
        metadata={
            "name": "OTH",
            "type": "Element",
        }
    )

    @dataclass
    class Refundability:
        """
        Parameters
        ----------
        value: Currently returned: FullyRefundable (1G,1V),
            RefundableWithPenalty (1G,1V), Refundable (1P,1J),
            NonRefundable (1G,1V,1P,1J).Refundable.
        """
        value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class FaxDetails:
    """
    The Fax Details Information.

    Parameters
    ----------
    phone_number: Send type as Fax for fax number.
    term_conditions: Term and Conditions for the fax .
    remark:
    include_cover_sheet: Specifies whether to include a cover page with
        fax or not.
    to: To address.
    from_value: From address.
    dept_billing_code: Department billing code.
    invoice_number: Invoice number.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    term_conditions: Optional[TermConditions] = field(
        default=None,
        metadata={
            "name": "TermConditions",
            "type": "Element",
        }
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    include_cover_sheet: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeCoverSheet",
            "type": "Attribute",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Attribute",
        }
    )
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Attribute",
        }
    )
    dept_billing_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeptBillingCode",
            "type": "Attribute",
        }
    )
    invoice_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceNumber",
            "type": "Attribute",
        }
    )


@dataclass
class FlightInfoDetail:
    """
    Parameters
    ----------
    codeshare_info:
    meals:
    in_flight_services:
    variance:
    origin: The IATA location code for this origination of this entity.
    destination: The IATA location code for this destination of this
        entity.
    scheduled_departure_time: The date and time at which this entity is
        scheduled to depart. This does not include time zone information
        since it can be derived from the origin location.
    scheduled_arrival_time: The date and time at which this entity is
        scheduled to arrive at the destination. This does not include
        time zone information since it can be derived from the origin
        location.
    travel_time: Total time spent (minutes) traveling including flight
        time and ground time.
    eticketability: Identifies if this particular segment is
        E-Ticketable
    equipment:
    origin_terminal:
    origin_gate: To be used to display origin flight gate number
    destination_terminal:
    destination_gate: To be used to display destination flight gate
        number
    automated_checkin: “True” indicates that the flight allows automated
        check-in. The default is “False”.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    codeshare_info: Optional[CodeshareInfo] = field(
        default=None,
        metadata={
            "name": "CodeshareInfo",
            "type": "Element",
        }
    )
    meals: List[TypeMealService] = field(
        default_factory=list,
        metadata={
            "name": "Meals",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    in_flight_services: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InFlightServices",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    variance: List[Variance] = field(
        default_factory=list,
        metadata={
            "name": "Variance",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    scheduled_departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduledDepartureTime",
            "type": "Attribute",
        }
    )
    scheduled_arrival_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduledArrivalTime",
            "type": "Attribute",
        }
    )
    travel_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        }
    )
    eticketability: Optional[TypeEticketability] = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
        }
    )
    equipment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Attribute",
            "length": 3,
        }
    )
    origin_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginTerminal",
            "type": "Attribute",
        }
    )
    origin_gate: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginGate",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    destination_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationTerminal",
            "type": "Attribute",
        }
    )
    destination_gate: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationGate",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    automated_checkin: bool = field(
        default=False,
        metadata={
            "name": "AutomatedCheckin",
            "type": "Attribute",
        }
    )


@dataclass
class FlightTimeTableCriteria:
    """
    Flight Time Table Search Criteria.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    general_time_table: Optional[GeneralTimeTable] = field(
        default=None,
        metadata={
            "name": "GeneralTimeTable",
            "type": "Element",
        }
    )
    specific_time_table: Optional[SpecificTimeTable] = field(
        default=None,
        metadata={
            "name": "SpecificTimeTable",
            "type": "Element",
        }
    )


@dataclass
class IssuanceModifiers:
    """
    General modifiers supported for EMD Issuance.Supported providers are
    1V/1G/1P/1J.

    Parameters
    ----------
    form_of_payment_ref: Reference to FormOfPayment present in the UR to
        be used for EMD issuance.
    form_of_payment: FormOfPayment information to be used for EMD
        issuance.
    customer_receipt_info: Information about customer receipt via email.
    emdendorsement: Endorsement details to be used during EMD issuance.
    emdcommission: Commission information to be used for EMD issuance.
    plating_carrier: Plating carrier code for which this EMD is issued.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    customer_receipt_info: Optional[CustomerReceiptInfo] = field(
        default=None,
        metadata={
            "name": "CustomerReceiptInfo",
            "type": "Element",
        }
    )
    emdendorsement: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMDEndorsement",
            "type": "Element",
            "min_length": 1,
            "max_length": 255,
        }
    )
    emdcommission: Optional[Emdcommission] = field(
        default=None,
        metadata={
            "name": "EMDCommission",
            "type": "Element",
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )


@dataclass
class PassengerType(TypePassengerType):
    """
    The passenger type details associated to a fare.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_guarantee_info: Optional[FareGuaranteeInfo] = field(
        default=None,
        metadata={
            "name": "FareGuaranteeInfo",
            "type": "Element",
        }
    )


@dataclass
class PenaltyFareInformation:
    """
    Parameters
    ----------
    penalty_info: Penalty Limit if requested.
    prohibit_penalty_fares: Indicates whether user wants penalty fares
        to be returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    penalty_info: Optional[TypeFarePenalty] = field(
        default=None,
        metadata={
            "name": "PenaltyInfo",
            "type": "Element",
        }
    )
    prohibit_penalty_fares: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProhibitPenaltyFares",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PrePayCustomer:
    """
    Detailed customer information for searching pre pay profiles.

    Parameters
    ----------
    person_name:
    email: Customer email detail
    address: Customer address detail
    related_traveler: Travelers related to this pre pay id
    loyalty_card: Customer loyalty card detail
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    person_name: Optional[PersonName] = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    address: List[TypeStructuredAddress] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    related_traveler: List[RelatedTraveler] = field(
        default_factory=list,
        metadata={
            "name": "RelatedTraveler",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class PrePayPriceInfo:
    """
    Pricing detail for the Pre Pay Account.

    Parameters
    ----------
    tax_info: Detailed tax information for the pre pay account
    base_fare:
    total_fare:
    total_tax:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    base_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Attribute",
        }
    )
    total_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalFare",
            "type": "Attribute",
        }
    )
    total_tax: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalTax",
            "type": "Attribute",
        }
    )


@dataclass
class RepricingModifiers:
    """Used for rapid reprice to provide additional options for the reprice.

    Providers: 1G/1V/1P/1S/1A

    Parameters
    ----------
    private_fare_options: Public and/or Private Fares requested for
        pricing.            Currently supported: AccountCodeOnly,
        PrivateFaresOnly, PublicPrivateFaresOnly.
    fare_type:
    fare_ticket_designator:
    override_currency:
    air_segment_pricing_modifiers:
    withhold_tax_code: Used to request tax withholding for the tax code
        specified. Providers supported 1G/1P
    price_class_of_service: Values allowed are ClassBooked or
        LowestClass. This tells how to price the new itinerary.
    create_date: This is either today’s date or the date the repriced
        itinerary was created
    reissue_loc_city_code: This is the city code of the reissue location
    reissue_loc_country_code: This is the country code of the reissue
        location
    bulk_ticket: Set to true and the itinerary is/will be a bulk ticket.
        Set to false and the itinerary being repriced will not be a bulk
        ticket.
    account_code: May be used in conjunction with PrivateFareOptions
    penalty_as_tax_code: Used to request that the penalty be applied as
        a tax, to the tax code specified. Providers supported 1G/1P
    air_pricing_solution_ref: A reference to a AirPricingSolution.
        Providers: 1G, 1V, 1P, 1J.
    penalty_to_fare: Will add the change fee/penalty amount to the total
        fare amount. Supported Providers: 1P
    price_ptconly: A value of true forces the price for the PTC even if
        that fare is not the lowest fare for the passenger.
    brand_details: Set to true full brand details will be returned.
    brand_modifier: A value of MaintainBrand will maintain the brand
        from the original ticket if applicable.
    jet_service_only: Request flights that are jet service only.
        Available in AirExchangeMultiQuoteReq only.
    time_window: A value of Time Window is optional. Available in
        AirExchangeMultiQuoteReq only.
    flight_type: Type of flights to be returned. Values are 'NonStop',
        'Direct', 'SingleConnection' and 'NoRestrictions'. Available in
        AirExchangeMultiQuoteReq only.
    multi_airport_search: A value of Multi Airport Search Indicator is
        optional. Available in AirExchangeMultiQuoteReq only.
    connection_point: A value of Connection City Code is optional.
        Available in AirExchangeMultiQuoteReq only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    private_fare_options: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateFareOptions",
            "type": "Element",
            "max_length": 50,
        }
    )
    fare_type: List[FareType] = field(
        default_factory=list,
        metadata={
            "name": "FareType",
            "type": "Element",
            "max_occurs": 100,
        }
    )
    fare_ticket_designator: Optional[FareTicketDesignator] = field(
        default=None,
        metadata={
            "name": "FareTicketDesignator",
            "type": "Element",
        }
    )
    override_currency: Optional["RepricingModifiers.OverrideCurrency"] = field(
        default=None,
        metadata={
            "name": "OverrideCurrency",
            "type": "Element",
        }
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    withhold_tax_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "WithholdTaxCode",
            "type": "Element",
            "max_occurs": 4,
            "length": 2,
        }
    )
    price_class_of_service: Optional[TypePriceClassOfService] = field(
        default=None,
        metadata={
            "name": "PriceClassOfService",
            "type": "Attribute",
        }
    )
    create_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
        }
    )
    reissue_loc_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReissueLocCityCode",
            "type": "Attribute",
            "length": 3,
        }
    )
    reissue_loc_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReissueLocCountryCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    bulk_ticket: bool = field(
        default=False,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        }
    )
    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        }
    )
    penalty_as_tax_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PenaltyAsTaxCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    air_pricing_solution_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirPricingSolutionRef",
            "type": "Attribute",
        }
    )
    penalty_to_fare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PenaltyToFare",
            "type": "Attribute",
        }
    )
    price_ptconly: bool = field(
        default=False,
        metadata={
            "name": "PricePTCOnly",
            "type": "Attribute",
        }
    )
    brand_details: bool = field(
        default=False,
        metadata={
            "name": "BrandDetails",
            "type": "Attribute",
        }
    )
    brand_modifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandModifier",
            "type": "Attribute",
        }
    )
    jet_service_only: bool = field(
        default=False,
        metadata={
            "name": "JetServiceOnly",
            "type": "Attribute",
        }
    )
    time_window: Optional[int] = field(
        default=None,
        metadata={
            "name": "TimeWindow",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 12,
        }
    )
    flight_type: RepricingModifiersFlightType = field(
        default=RepricingModifiersFlightType.DIRECT,
        metadata={
            "name": "FlightType",
            "type": "Attribute",
        }
    )
    multi_airport_search: bool = field(
        default=True,
        metadata={
            "name": "MultiAirportSearch",
            "type": "Attribute",
        }
    )
    connection_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionPoint",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )

    @dataclass
    class OverrideCurrency:
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Attribute",
                "length": 3,
            }
        )
        country_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryCode",
                "type": "Attribute",
                "length": 2,
            }
        )


@dataclass
class Route:
    """
    Information about this Route component.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    leg: List[Leg] = field(
        default_factory=list,
        metadata={
            "name": "Leg",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RuleLengthOfStay:
    """
    Container for rules providing minimum and maximum stay requirements.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    minimum_stay: Optional[TypeRestrictionLengthOfStay] = field(
        default=None,
        metadata={
            "name": "MinimumStay",
            "type": "Element",
        }
    )
    maximum_stay: Optional[TypeRestrictionLengthOfStay] = field(
        default=None,
        metadata={
            "name": "MaximumStay",
            "type": "Element",
        }
    )


@dataclass
class TcrexchangeBundle:
    """
    Bundle exchange, pricing, and penalty information for one ticketless
    carrier reservation Used in AirExchangeReq request and AirExchangeQuoteRsp
    response.

    Parameters
    ----------
    air_exchange_info:
    air_pricing_info_ref:
    fee_info:
    tax_info: Itinerary level taxes
    penalty: Only used within an AirExchangeQuoteRsp
    tcrnumber: The identifying number for a Ticketless Air Reservation.
    """
    class Meta:
        name = "TCRExchangeBundle"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_exchange_info: Optional[AirExchangeInfo] = field(
        default=None,
        metadata={
            "name": "AirExchangeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    penalty: List[CommonPenalty] = field(
        default_factory=list,
        metadata={
            "name": "Penalty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "TCRNumber",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Ticket:
    """
    The ticket that resulted from an air booking.

    Parameters
    ----------
    coupon:
    ticket_endorsement:
    tour_code:
    exchanged_ticket_info:
    key:
    ticket_number:
    ticket_status:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    coupon: List[Coupon] = field(
        default_factory=list,
        metadata={
            "name": "Coupon",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 4,
        }
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata={
            "name": "TicketEndorsement",
            "type": "Element",
            "max_occurs": 6,
        }
    )
    tour_code: List[TourCode] = field(
        default_factory=list,
        metadata={
            "name": "TourCode",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    exchanged_ticket_info: List[ExchangedTicketInfo] = field(
        default_factory=list,
        metadata={
            "name": "ExchangedTicketInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
            "required": True,
            "length": 13,
        }
    )
    ticket_status: Optional[TypeTicketStatus] = field(
        default=None,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class TicketInfo:
    """
    Parameters
    ----------
    name:
    conjuncted_ticket_info:
    exchanged_ticket_info:
    number:
    iatanumber:
    ticket_issue_date:
    ticketing_agent_sign_on:
    country_code: Contains Ticketed PCC’s Country code.
    status:
    bulk_ticket: Whether the ticket was issued as bulk.
    booking_traveler_ref: A reference to a passenger.
    air_pricing_info_ref: A reference to a AirPricing.Applicable
        Providers 1G and 1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    conjuncted_ticket_info: List[ConjunctedTicketInfo] = field(
        default_factory=list,
        metadata={
            "name": "ConjunctedTicketInfo",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    exchanged_ticket_info: List[ExchangedTicketInfo] = field(
        default_factory=list,
        metadata={
            "name": "ExchangedTicketInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    iatanumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    ticket_issue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TicketIssueDate",
            "type": "Attribute",
        }
    )
    ticketing_agent_sign_on: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketingAgentSignOn",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    status: Optional[TypeTicketStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    bulk_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )
    air_pricing_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Attribute",
        }
    )


@dataclass
class TypeDefaultBrandDetail:
    """
    Parameters
    ----------
    text: Text associated to the brand
    image_location: Images associated to the brand
    applicable_segment: Defines for which air segment the brand is
        applicable.
    brand_id: The unique identifier of the brand
    """
    class Meta:
        name = "typeDefaultBrandDetail"

    text: List[Text] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 4,
        }
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata={
            "name": "ImageLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 3,
        }
    )
    applicable_segment: List[ApplicableSegment] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 99,
        }
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 19,
        }
    )


@dataclass
class AccountRelatedRules:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_rules: List[BookingRules] = field(
        default_factory=list,
        metadata={
            "name": "BookingRules",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    routing_rules: Optional[RoutingRules] = field(
        default=None,
        metadata={
            "name": "RoutingRules",
            "type": "Element",
        }
    )


@dataclass
class AirExchangeBundleList:
    """
    The shared object list of AirsegmentData.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeEligibilityRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    exchange_eligibility_info: Optional[ExchangeEligibilityInfo] = field(
        default=None,
        metadata={
            "name": "ExchangeEligibilityInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AirExchangeTicketingReq(BaseReq):
    """Request to ticket an exchanged itinerary.

    Providers 1G, 1V, 1P.

    Parameters
    ----------
    air_reservation_locator_code: Identifies the PNR to ticket.
        Providers 1G, 1V, 1P.
    ticket_number: Ticket number to reissue. Providers 1G, 1V, 1P.
    ticketing_modifiers_ref: Provider: 1P-Reference to a shared list of
        Ticketing Modifiers. This is supported for Worldspan provider
        only. When AirPricingInfoRef is used along with
        TicketingModifiersRef means that particular TicketingModifiers
        will to be applied while ticketing the Stored fare corresponding
        to the AirPricingInfo. Absence of AirPricingInfoRef means that
        particular TicketingModifiers will be applied to all Stored
        fares which are requested to be ticketed.
    waiver_code:
    detailed_billing_information: Providers 1G, 1V, 1P.
    air_ticketing_modifiers: Provider: 1G,1V,1P.
    bulk_ticket: Providers 1G, 1V, 1P.
    change_fee_on_ticket: Applies the change fee/penalty to the original
        form of payment. Providers: 1V
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
            "min_length": 1,
            "max_length": 13,
        }
    )
    ticketing_modifiers_ref: List[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_ticketing_modifiers: List[AirTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirTicketingModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    bulk_ticket: bool = field(
        default=False,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        }
    )
    change_fee_on_ticket: bool = field(
        default=True,
        metadata={
            "name": "ChangeFeeOnTicket",
            "type": "Attribute",
        }
    )


@dataclass
class AirFareDisplayModifiers:
    """
    Parameters
    ----------
    trip_type:
    cabin_class:
    penalty_fare_information: Request Fares with specific Penalty
        Information.
    fare_search_option:
    max_responses:
    departure_date:
    ticketing_date:
    return_date:
    base_fare_only:
    unrestricted_fares_only:
    fares_indicator: Indicates whether only public fares should be
        returned or specific type of private fares
    currency_type:
    include_taxes:
    include_estimated_taxes: Indicates to include estimated taxes i.e.
        if set to true estimated total fare,base fare and taxes would be
        returned.
    include_surcharges:
    global_indicator:
    prohibit_min_stay_fares:
    prohibit_max_stay_fares:
    prohibit_advance_purchase_fares:
    prohibit_non_refundable_fares: Indicates whether it prohibits
        NonRefundable Fares.
    validated_fares_only: Indicates that the requested Fares should be
        Validated Fares only. If set to true, then only valid fares will
        be returned. If set to false, both valid and non valid fares
        will be returned. If not sent, then no validation will be done.
        All fares will be returned.
    prohibit_travel_restricted_fares: Indicates that the Fares not
        complying Travel Restrictions and Seasonality fare rules are
        prohibited
    filed_currency: Represents the filed currency of the fare
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    trip_type: List[TypeFareTripType] = field(
        default_factory=list,
        metadata={
            "name": "TripType",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    cabin_class: Optional[CabinClass] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    penalty_fare_information: Optional[PenaltyFareInformation] = field(
        default=None,
        metadata={
            "name": "PenaltyFareInformation",
            "type": "Element",
        }
    )
    fare_search_option: List[TypeFareSearchOption] = field(
        default_factory=list,
        metadata={
            "name": "FareSearchOption",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    max_responses: int = field(
        default=200,
        metadata={
            "name": "MaxResponses",
            "type": "Attribute",
        }
    )
    departure_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        }
    )
    ticketing_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TicketingDate",
            "type": "Attribute",
        }
    )
    return_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReturnDate",
            "type": "Attribute",
        }
    )
    base_fare_only: bool = field(
        default=False,
        metadata={
            "name": "BaseFareOnly",
            "type": "Attribute",
        }
    )
    unrestricted_fares_only: bool = field(
        default=False,
        metadata={
            "name": "UnrestrictedFaresOnly",
            "type": "Attribute",
        }
    )
    fares_indicator: Optional[TypeFaresIndicator] = field(
        default=None,
        metadata={
            "name": "FaresIndicator",
            "type": "Attribute",
        }
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        }
    )
    include_taxes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeTaxes",
            "type": "Attribute",
        }
    )
    include_estimated_taxes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeEstimatedTaxes",
            "type": "Attribute",
        }
    )
    include_surcharges: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeSurcharges",
            "type": "Attribute",
        }
    )
    global_indicator: Optional[TypeAtpcoglobalIndicator] = field(
        default=None,
        metadata={
            "name": "GlobalIndicator",
            "type": "Attribute",
        }
    )
    prohibit_min_stay_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitMinStayFares",
            "type": "Attribute",
        }
    )
    prohibit_max_stay_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitMaxStayFares",
            "type": "Attribute",
        }
    )
    prohibit_advance_purchase_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitAdvancePurchaseFares",
            "type": "Attribute",
        }
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonRefundableFares",
            "type": "Attribute",
        }
    )
    validated_fares_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ValidatedFaresOnly",
            "type": "Attribute",
        }
    )
    prohibit_travel_restricted_fares: bool = field(
        default=True,
        metadata={
            "name": "ProhibitTravelRestrictedFares",
            "type": "Attribute",
        }
    )
    filed_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "length": 3,
        }
    )


@dataclass
class AirFareRulesReq(BaseReq):
    """
    Request to display the full text fare rules.

    Parameters
    ----------
    air_reservation_selector: Provider: 1G,1V,1P,1J,ACH-Parameters to
        use for a fare rule lookup associated with an Air Reservation
        Locator Code
    fare_rule_lookup: Used to look up fare rules based on the origin,
        destination, and carrier of the air segment, the fare basis code
        and the provider code.  Providers: 1P, 1J.
    fare_rule_key: Used to look up fare rules based on a fare rule key.
        Providers: 1G, 1V, 1P, 1J, ACH.
    air_fare_display_rule_key: Provider: 1G,1V,1P,1J.
    air_fare_rules_modifier: Provider: 1G,1V.
    fare_rules_filter_category: Structured Fare Rules Filter if
        requested will return rules for requested categories in the
        response. Applicable for providers 1G, 1V.
    fare_rule_type: Provider: 1G,1V,1P,1J,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_selector: Optional["AirFareRulesReq.AirReservationSelector"] = field(
        default=None,
        metadata={
            "name": "AirReservationSelector",
            "type": "Element",
        }
    )
    fare_rule_lookup: Optional[FareRuleLookup] = field(
        default=None,
        metadata={
            "name": "FareRuleLookup",
            "type": "Element",
        }
    )
    fare_rule_key: List[FareRuleKey] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleKey",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_fare_display_rule_key: Optional[AirFareDisplayRuleKey] = field(
        default=None,
        metadata={
            "name": "AirFareDisplayRuleKey",
            "type": "Element",
        }
    )
    air_fare_rules_modifier: Optional[AirFareRulesModifier] = field(
        default=None,
        metadata={
            "name": "AirFareRulesModifier",
            "type": "Element",
        }
    )
    fare_rules_filter_category: List["AirFareRulesReq.FareRulesFilterCategory"] = field(
        default_factory=list,
        metadata={
            "name": "FareRulesFilterCategory",
            "type": "Element",
            "max_occurs": 16,
        }
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.LONG,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
        }
    )

    @dataclass
    class FareRulesFilterCategory:
        """
        Parameters
        ----------
        category_code: Structured Fare Rules can be requested for "ADV",
            "MIN", "MAX",  "STP", and "CHG".
        fare_info_ref: Key reference for multiple fare rule
        """
        category_code: List[object] = field(
            default_factory=list,
            metadata={
                "name": "CategoryCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 35,
            }
        )
        fare_info_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "FareInfoRef",
                "type": "Attribute",
            }
        )

    @dataclass
    class AirReservationSelector:
        """
        Parameters
        ----------
        fare_info_ref:
        air_reservation_locator_code: The Air Reservation locator code
            which is an unique identifier for the reservation
        """
        fare_info_ref: List[FareInfoRef] = field(
            default_factory=list,
            metadata={
                "name": "FareInfoRef",
                "type": "Element",
                "max_occurs": 999,
            }
        )
        air_reservation_locator_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "AirReservationLocatorCode",
                "type": "Attribute",
                "required": True,
                "min_length": 5,
                "max_length": 8,
            }
        )


@dataclass
class AirItinerarySolution:
    """
    The pricing container for an air travel itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AirPricingModifiers:
    """
    Controls and switches for a Air Search request that contains Pricing
    Information.

    Parameters
    ----------
    prohibited_rule_categories:
    account_codes:
    permitted_cabins:
    contract_codes:
    exempt_taxes:
    penalty_fare_information: Request Fares with specific Penalty
        Information.
    discount_card: Discount request for rail.
    promo_codes:
    manual_fare_adjustment: Represents increment/discount applied
        manually by agent.
    point_of_sale: User can use this node to send a specific PCC to
        access fares allowed only for that PCC. This node gives the
        capability for fare redistribution at stored fare level. As
        multiple UAPI AirPricingInfos (all having same
        AirPricingInfoGroup) can converge to a single stored fare, UAPI
        will map PoinOfSale information from the first available one
        from each group
    brand_modifiers: Used to specify the level of branding requested.
    multi_gdssearch_indicator:
    preferred_cabins:
    prohibit_min_stay_fares:
    prohibit_max_stay_fares:
    currency_type:
    prohibit_advance_purchase_fares:
    prohibit_non_refundable_fares:
    prohibit_restricted_fares:
    fares_indicator: Indicates whether only public fares should be
        returned or specific type of private fares
    filed_currency: Currency in which Fares/Prices will be filed if
        supported by the supplier else approximated to.
    plating_carrier: The Plating Carrier for this journey.
    override_carrier: The Plating Carrier for this journey.
    eticketability: Request a search based on whether only E-ticketable
        fares are required.
    account_code_fares_only: Indicates whether or not the private fares
        returned should be restricted to only those specific to the
        input account code and contract code.
    key:
    prohibit_non_exchangeable_fares:
    force_segment_select: This indicator allows agent to force segment
        select option in host while selecting all air segments to store
        price on a PNR. This is relevent only when agent selects all air
        segmnets to price. if agent selects specific segments to price
        then this attribute will be ignored by the system. This is
        currently used by Worldspan only.
    inventory_request_type: This allows user to make request for a
        particular source of inventory for pricing modifier purposes.
        This is currently used by Worldspan only.
    one_way_shop: Via this attribute one way shop can be requested.
        Applicable provider is 1G
    prohibit_unbundled_fare_types: A "True" value wiill remove fares
        with EOU and ERU fare types from consideration. A "False" value
        is the same as no value.  Default is no value. Applicable
        providers:  1P/1J/1G/1V
    return_services: When set to false, ATPCO filed Optional Services
        will not be returned. Default is true. Provider: 1G, 1V, 1P, 1J
    channel_id: A Channel ID is 2 to 4 alpha-numeric characters used to
        activate the Search Control Console filter for a specific group
        of travelers being served by the agency credential.
    return_fare_attributes: Returns attributes that are associated to a
        fare
    sell_check: Checks if the segment is bookable before pricing
    return_failed_segments: If "true", returns failed segments
        information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    prohibited_rule_categories: Optional["AirPricingModifiers.ProhibitedRuleCategories"] = field(
        default=None,
        metadata={
            "name": "ProhibitedRuleCategories",
            "type": "Element",
        }
    )
    account_codes: Optional["AirPricingModifiers.AccountCodes"] = field(
        default=None,
        metadata={
            "name": "AccountCodes",
            "type": "Element",
        }
    )
    permitted_cabins: Optional[PermittedCabins] = field(
        default=None,
        metadata={
            "name": "PermittedCabins",
            "type": "Element",
        }
    )
    contract_codes: Optional["AirPricingModifiers.ContractCodes"] = field(
        default=None,
        metadata={
            "name": "ContractCodes",
            "type": "Element",
        }
    )
    exempt_taxes: Optional[ExemptTaxes] = field(
        default=None,
        metadata={
            "name": "ExemptTaxes",
            "type": "Element",
        }
    )
    penalty_fare_information: Optional[PenaltyFareInformation] = field(
        default=None,
        metadata={
            "name": "PenaltyFareInformation",
            "type": "Element",
        }
    )
    discount_card: List[DiscountCard] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 9,
        }
    )
    promo_codes: Optional["AirPricingModifiers.PromoCodes"] = field(
        default=None,
        metadata={
            "name": "PromoCodes",
            "type": "Element",
        }
    )
    manual_fare_adjustment: List[ManualFareAdjustment] = field(
        default_factory=list,
        metadata={
            "name": "ManualFareAdjustment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    point_of_sale: Optional[PointOfSale] = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    brand_modifiers: Optional[BrandModifiers] = field(
        default=None,
        metadata={
            "name": "BrandModifiers",
            "type": "Element",
        }
    )
    multi_gdssearch_indicator: List[MultiGdssearchIndicator] = field(
        default_factory=list,
        metadata={
            "name": "MultiGDSSearchIndicator",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    preferred_cabins: List[PreferredCabins] = field(
        default_factory=list,
        metadata={
            "name": "PreferredCabins",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    prohibit_min_stay_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitMinStayFares",
            "type": "Attribute",
        }
    )
    prohibit_max_stay_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitMaxStayFares",
            "type": "Attribute",
        }
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        }
    )
    prohibit_advance_purchase_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitAdvancePurchaseFares",
            "type": "Attribute",
        }
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonRefundableFares",
            "type": "Attribute",
        }
    )
    prohibit_restricted_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitRestrictedFares",
            "type": "Attribute",
        }
    )
    fares_indicator: Optional[TypeFaresIndicator] = field(
        default=None,
        metadata={
            "name": "FaresIndicator",
            "type": "Attribute",
        }
    )
    filed_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "length": 3,
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    override_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "OverrideCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    eticketability: Optional[TypeEticketability] = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
        }
    )
    account_code_fares_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccountCodeFaresOnly",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    prohibit_non_exchangeable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonExchangeableFares",
            "type": "Attribute",
        }
    )
    force_segment_select: bool = field(
        default=False,
        metadata={
            "name": "ForceSegmentSelect",
            "type": "Attribute",
        }
    )
    inventory_request_type: Optional[TypeInventoryRequest] = field(
        default=None,
        metadata={
            "name": "InventoryRequestType",
            "type": "Attribute",
        }
    )
    one_way_shop: bool = field(
        default=False,
        metadata={
            "name": "OneWayShop",
            "type": "Attribute",
        }
    )
    prohibit_unbundled_fare_types: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProhibitUnbundledFareTypes",
            "type": "Attribute",
        }
    )
    return_services: bool = field(
        default=True,
        metadata={
            "name": "ReturnServices",
            "type": "Attribute",
        }
    )
    channel_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 4,
        }
    )
    return_fare_attributes: bool = field(
        default=False,
        metadata={
            "name": "ReturnFareAttributes",
            "type": "Attribute",
        }
    )
    sell_check: bool = field(
        default=False,
        metadata={
            "name": "SellCheck",
            "type": "Attribute",
        }
    )
    return_failed_segments: bool = field(
        default=False,
        metadata={
            "name": "ReturnFailedSegments",
            "type": "Attribute",
        }
    )

    @dataclass
    class ProhibitedRuleCategories:
        fare_rule_category: List[FareRuleCategory] = field(
            default_factory=list,
            metadata={
                "name": "FareRuleCategory",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class AccountCodes:
        """
        Parameters
        ----------
        account_code: Used to get negotiated pricing. Provider:ACH.
        """
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata={
                "name": "AccountCode",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ContractCodes:
        contract_code: List[ContractCode] = field(
            default_factory=list,
            metadata={
                "name": "ContractCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class PromoCodes:
        promo_code: List[PromoCode] = field(
            default_factory=list,
            metadata={
                "name": "PromoCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class AlternateRouteList:
    """
    Identifies the alternate routes for the request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    alternate_route: List[AlternateRoute] = field(
        default_factory=list,
        metadata={
            "name": "AlternateRoute",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class BagDetails:
    """
    Information related to Bag details .

    Parameters
    ----------
    baggage_restriction:
    available_discount:
    applicable_bags: Applicable baggage like Carry-On,1st Check-in,2nd
        Check -in etc.
    base_price:
    approximate_base_price:
    taxes:
    total_price:
    approximate_total_price:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    baggage_restriction: List[BaggageRestriction] = field(
        default_factory=list,
        metadata={
            "name": "BaggageRestriction",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    available_discount: List[AvailableDiscount] = field(
        default_factory=list,
        metadata={
            "name": "AvailableDiscount",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    applicable_bags: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicableBags",
            "type": "Attribute",
            "required": True,
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )


@dataclass
class CarryOnAllowanceInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Carry-On allowance like URL, pricing etc.

    Parameters
    ----------
    carry_on_details: Information related to Carry-On Bag details .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carry_on_details: List["CarryOnAllowanceInfo.CarryOnDetails"] = field(
        default_factory=list,
        metadata={
            "name": "CarryOnDetails",
            "type": "Element",
            "max_occurs": 999,
        }
    )

    @dataclass
    class CarryOnDetails:
        """
        Parameters
        ----------
        baggage_restriction:
        applicable_carry_on_bags: Applicable Carry-On baggage "First",
            "Second", "Third" etc
        base_price:
        approximate_base_price:
        taxes:
        total_price:
        approximate_total_price:
        """
        baggage_restriction: List[BaggageRestriction] = field(
            default_factory=list,
            metadata={
                "name": "BaggageRestriction",
                "type": "Element",
                "max_occurs": 99,
            }
        )
        applicable_carry_on_bags: Optional[str] = field(
            default=None,
            metadata={
                "name": "ApplicableCarryOnBags",
                "type": "Attribute",
            }
        )
        base_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "BasePrice",
                "type": "Attribute",
            }
        )
        approximate_base_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "ApproximateBasePrice",
                "type": "Attribute",
            }
        )
        taxes: Optional[str] = field(
            default=None,
            metadata={
                "name": "Taxes",
                "type": "Attribute",
            }
        )
        total_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalPrice",
                "type": "Attribute",
            }
        )
        approximate_total_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "ApproximateTotalPrice",
                "type": "Attribute",
            }
        )


@dataclass
class DefaultBrandDetail(TypeDefaultBrandDetail):
    """
    Applicable air segment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class DocumentInfo:
    """
    Container for the document information summary line.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_info: List[TicketInfo] = field(
        default_factory=list,
        metadata={
            "name": "TicketInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    mcoinfo: List[Mcoinformation] = field(
        default_factory=list,
        metadata={
            "name": "MCOInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tcrinfo: List[Tcrinfo] = field(
        default_factory=list,
        metadata={
            "name": "TCRInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class Emdinfo:
    """This is the parent container to display EMD information.

    Occurrence of multiple unique EMDs inside this container indicate
    that those EMDs are conjunctive to each other. Supported providers
    are 1G/1V/1P/1J

    Parameters
    ----------
    emdtraveler_info: Basic information of the traveler associated with
        this EMDInfo.
    supplier_locator: List of Supplier Locator information that is
        associated with this document
    electronic_misc_document: Electronic miscellaneous documents.As an
        EMDInfo container displays all the EMDs which are in
        conjunction, there can be maximum 4 ElectronicMiscDocuments
        present in an EMDInfo
    payment: Payment charged for EMD isuance
    form_of_payment: FormOfPayment used for issuing these electronic
        miscellaneous documents
    emdpricing_info: Fare related information for these electronic
        miscellaneous documents
    emdendorsement:
    fare_calc: Infomration about the fare calculation
    emdcommission: Commission information applied during EMD issuance
    provider_code:
    provider_locator_code:
    key: System generated Key
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "EMDInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdtraveler_info: Optional[EmdtravelerInfo] = field(
        default=None,
        metadata={
            "name": "EMDTravelerInfo",
            "type": "Element",
            "required": True,
        }
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    electronic_misc_document: List[ElectronicMiscDocument] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicMiscDocument",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    payment: Optional[Payment] = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    emdpricing_info: Optional[EmdpricingInfo] = field(
        default=None,
        metadata={
            "name": "EMDPricingInfo",
            "type": "Element",
        }
    )
    emdendorsement: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EMDEndorsement",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 255,
        }
    )
    fare_calc: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareCalc",
            "type": "Element",
        }
    )
    emdcommission: Optional[Emdcommission] = field(
        default=None,
        metadata={
            "name": "EMDCommission",
            "type": "Element",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class EmdissuanceReq(BaseReq):
    """
    Electronic Miscellaneous Document issuance request.Supported providers are
    1V/1G/1P/1J.

    Parameters
    ----------
    provider_reservation_detail: PNR information for which EMD is going
        to be issued.
    ticket_number: Ticket number for which EMD is going to be
        issued.Required for EMD-A issuance.
    issuance_modifiers: General modifiers related to EMD issuance.
    selection_modifiers: Modifiers related to selection of services
        during EMD issuance.
    universal_record_locator_code: Represents a valid Universal Record
        locator code.
    show_details: This attribute gives the control to request for
        complete information on Issued EMDs or minimal
        information.Requesting complete information leads to possible
        multiple supplier calls for fetching all the details.
    issue_all_open_svc: Issues EMDS to all SVC segments. If it is true,
        TicketNumber and SVC segment reference need not be provided.
        Supported provider 1P.
    """
    class Meta:
        name = "EMDIssuanceReq"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    provider_reservation_detail: Optional[ProviderReservationDetail] = field(
        default=None,
        metadata={
            "name": "ProviderReservationDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_length": 1,
            "max_length": 13,
        }
    )
    issuance_modifiers: Optional[IssuanceModifiers] = field(
        default=None,
        metadata={
            "name": "IssuanceModifiers",
            "type": "Element",
        }
    )
    selection_modifiers: Optional[SelectionModifiers] = field(
        default=None,
        metadata={
            "name": "SelectionModifiers",
            "type": "Element",
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    show_details: bool = field(
        default=False,
        metadata={
            "name": "ShowDetails",
            "type": "Attribute",
        }
    )
    issue_all_open_svc: bool = field(
        default=False,
        metadata={
            "name": "IssueAllOpenSVC",
            "type": "Attribute",
        }
    )


@dataclass
class EmdsummaryInfo:
    """Container for EMD summary information.

    Supported providers are 1G/1V/1P/1J

    Parameters
    ----------
    emdsummary: Summary information for EMDs conjuncted to each other.
    emdtraveler_info: EMD traveler information.
    payment: Payment charged to issue EMD.
    provider_reservation_info_ref: A reference to the provider
        reservation with which the document is associated.Displayed when
        shown as part of UR.Not displayed in EMDRetrieveRsp
    key: System generated Key
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "EMDSummaryInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdsummary: List[Emdsummary] = field(
        default_factory=list,
        metadata={
            "name": "EMDSummary",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    emdtraveler_info: Optional[EmdtravelerInfo] = field(
        default=None,
        metadata={
            "name": "EMDTravelerInfo",
            "type": "Element",
            "required": True,
        }
    )
    payment: Optional[Payment] = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class ExpertSolutionList:
    """
    Identifies the Expert Solutions retrieved from the Knowledge Base.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    expert_solution: List[ExpertSolution] = field(
        default_factory=list,
        metadata={
            "name": "ExpertSolution",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class FareDisplayRule:
    """
    Fare Display Rule Container.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    rule_advanced_purchase: Optional[RuleAdvancedPurchase] = field(
        default=None,
        metadata={
            "name": "RuleAdvancedPurchase",
            "type": "Element",
        }
    )
    rule_length_of_stay: Optional[RuleLengthOfStay] = field(
        default=None,
        metadata={
            "name": "RuleLengthOfStay",
            "type": "Element",
        }
    )
    rule_charges: Optional[RuleCharges] = field(
        default=None,
        metadata={
            "name": "RuleCharges",
            "type": "Element",
        }
    )
    rule_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleNumber",
            "type": "Attribute",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
        }
    )
    tariff_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TariffNumber",
            "type": "Attribute",
        }
    )


@dataclass
class FaxDetailsInformation:
    """
    Container to send Fax details Information for ticketing.

    Parameters
    ----------
    air_pricing_info_ref: Returns related air pricing infos.
    fax_details:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    fax_details: Optional[FaxDetails] = field(
        default=None,
        metadata={
            "name": "FaxDetails",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class FlightDetails:
    """
    Specific details within a flight segment.

    Parameters
    ----------
    connection:
    meals:
    in_flight_services:
    key:
    origin: The IATA location code for this origination of this entity.
    destination: The IATA location code for this destination of this
        entity.
    departure_time: The date and time at which this entity departs. Date
        and time are represented as Airport Local Time at the place of
        departure. The correct time zone offset is also included.
    arrival_time: The date and time at which this entity arrives at the
        destination. Date and time are represented as Airport Local Time
        at the place of arrival. The correct time zone offset is also
        included.
    flight_time: Time spent (minutes) traveling in flight, including
        airport taxi time.
    travel_time: Total time spent (minutes) traveling including flight
        time and ground time.
    distance: The distance traveled. Units are specified in the parent
        response element.
    equipment:
    on_time_performance: Represents flight on time performance as a
        percentage from 0 to 100
    origin_terminal:
    destination_terminal:
    ground_time:
    automated_checkin: “True” indicates that the flight allows automated
        check-in. The default is “False”.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    connection: Optional[Connection] = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Element",
        }
    )
    meals: List[TypeMealService] = field(
        default_factory=list,
        metadata={
            "name": "Meals",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    in_flight_services: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InFlightServices",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        }
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    flight_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "FlightTime",
            "type": "Attribute",
        }
    )
    travel_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        }
    )
    distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Attribute",
        }
    )
    equipment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Attribute",
            "length": 3,
        }
    )
    on_time_performance: Optional[int] = field(
        default=None,
        metadata={
            "name": "OnTimePerformance",
            "type": "Attribute",
        }
    )
    origin_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginTerminal",
            "type": "Attribute",
        }
    )
    destination_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationTerminal",
            "type": "Attribute",
        }
    )
    ground_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "GroundTime",
            "type": "Attribute",
        }
    )
    automated_checkin: bool = field(
        default=False,
        metadata={
            "name": "AutomatedCheckin",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class FlightInfo:
    """
    Parameters
    ----------
    flight_info_detail:
    flight_info_error_message: Errors, Warnings and informational
        messages for the Flight referenced above.
    criteria_key: An identifier to link the flightinfo responses to the
        criteria in request. The value populated here is passed in
        request.
    carrier: The carrier that is marketing this segment
    flight_number: The flight number under which the marketing carrier
        is marketing this flight
    origin: The IATA location code for this origination of this entity.
    destination: The IATA location code for this destination of this
        entity.
    departure_date: The date at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location.
    class_of_service:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_info_detail: List[FlightInfoDetail] = field(
        default_factory=list,
        metadata={
            "name": "FlightInfoDetail",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    flight_info_error_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata={
            "name": "FlightInfoErrorMessage",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    criteria_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "CriteriaKey",
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
            "length": 2,
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
            "required": True,
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )


@dataclass
class FlightTimeDetail:
    """
    Flight Time Table Response Details.

    Parameters
    ----------
    days_of_operation:
    connection:
    key:
    vendor_code:
    flight_number:
    origin:
    destination:
    departure_time: Flight departure time
    arrival_time: Flight arrival time
    stop_count:
    equipment:
    schedule_start_date: Flight time table search start date
    schedule_end_date: Flight time table search end date
    display_option: Indicates if carrier has link (carrier specific)
        display option.
    on_time_performance: On time performance indicator in percentage.
    day_change: Indicates if flight arrives on same day as departure,
        previous day, or next day. Like values  00 means Same day ,  01
        means next day, -1 mean Previous day etc.
    journey_time: Indicates total journey time in minutes.
    flight_time: Indicates total flight time in minutes.
    start_terminal: Flight start terminal code.
    end_terminal: Flight end terminal code.
    first_intermediate_stop: First intermediate stop after board point.
    last_intermediate_stop: Last intermediate stop before off point.
    inside_availability:
    secure_sell:
    availability_source:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    days_of_operation: Optional[TypeDaysOfOperation] = field(
        default=None,
        metadata={
            "name": "DaysOfOperation",
            "type": "Element",
        }
    )
    connection: Optional[Connection] = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    vendor_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
        }
    )
    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        }
    )
    arrival_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    stop_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "StopCount",
            "type": "Attribute",
        }
    )
    equipment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Attribute",
            "length": 3,
        }
    )
    schedule_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ScheduleStartDate",
            "type": "Attribute",
        }
    )
    schedule_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ScheduleEndDate",
            "type": "Attribute",
        }
    )
    display_option: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayOption",
            "type": "Attribute",
        }
    )
    on_time_performance: Optional[int] = field(
        default=None,
        metadata={
            "name": "OnTimePerformance",
            "type": "Attribute",
        }
    )
    day_change: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayChange",
            "type": "Attribute",
        }
    )
    journey_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "JourneyTime",
            "type": "Attribute",
        }
    )
    flight_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "FlightTime",
            "type": "Attribute",
        }
    )
    start_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTerminal",
            "type": "Attribute",
        }
    )
    end_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTerminal",
            "type": "Attribute",
        }
    )
    first_intermediate_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstIntermediateStop",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    last_intermediate_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastIntermediateStop",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    inside_availability: Optional[str] = field(
        default=None,
        metadata={
            "name": "InsideAvailability",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 1,
        }
    )
    secure_sell: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecureSell",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 2,
        }
    )
    availability_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilitySource",
            "type": "Attribute",
            "max_length": 1,
        }
    )


@dataclass
class FlightTimeTableReq(BaseSearchReq):
    """
    Request for Flight Time Table.

    Parameters
    ----------
    flight_time_table_criteria: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_time_table_criteria: Optional[FlightTimeTableCriteria] = field(
        default=None,
        metadata={
            "name": "FlightTimeTableCriteria",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class MerchandisingAvailabilityDetails:
    """
    Rich Content and Branding for an air segment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_itinerary_details: Optional[AirItineraryDetails] = field(
        default=None,
        metadata={
            "name": "AirItineraryDetails",
            "type": "Element",
            "required": True,
        }
    )
    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )


@dataclass
class MerchandisingDetails:
    """
    Rich Content and Branding for a fare brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_itinerary_details: List[AirItineraryDetails] = field(
        default_factory=list,
        metadata={
            "name": "AirItineraryDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        }
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 10,
        }
    )


@dataclass
class Option:
    """
    List of segment and fare available for the search air leg.

    Parameters
    ----------
    booking_info:
    connection:
    key:
    travel_time: Total traveling time that is difference between the
        departure time of the first segment and the arrival time of the
        last segments for that particular entire set of connection.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_info: List[BookingInfo] = field(
        default_factory=list,
        metadata={
            "name": "BookingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    travel_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        }
    )


@dataclass
class OptionalService:
    """
    Parameters
    ----------
    service_data:
    service_info:
    remark: Information regarding any specific for this service.
    tax_info:
    fee_info:
    emd:
    bundled_services:
    additional_info:
    fee_application: Specifies how the Optional Service fee is to be
        applied.  The choices are Per One Way, Per Round Trip, Per Item
        (Per Piece), Per Travel, Per Ticket, Per 1 Kilo, Per 5 Kilos.
        Provider: 1G, 1V, 1P, 1J
    text:
    price_range:
    tour_code:
    branding_info:
    title:
    provider_code:
    supplier_code:
    optional_services_rule_ref: UniqueID to associate a rule to the
        Optional Service
    type: Specify the type of service offered (e.g. seats, baggage,
        etc.)
    confirmation: Confirmation number provided by the supplier
    secondary_type: The secondary option code type required for certain
        options
    purchase_window: Describes when the Service is available for
        confirmation or purchase (e.g. Booking Only, Check-in Only,
        Anytime, etc.)
    priority: Numeric value that represents the priority order of the
        Service
    available: Boolean to describe whether the Service is available for
        sale or not
    entitled: Boolean to describe whether the passenger is entitled for
        the service without charge or not
    per_traveler: Boolean to describe whether the Amount on the Service
        is charged per traveler.
    create_date: Timestamp when this service/offer got created.
    payment_ref: Reference to a payment for merchandising services.
    service_status: Specify the service status (e.g. active, canceled,
        etc.)
    quantity: The number of units availed for each optional service
        (e.g. 2 baggage availed will be specified as 2 in quantity for
        optional service BAGGAGE)
    sequence_number: The sequence number associated with the
        OptionalService
    service_sub_code: The service subcode associated with the
        OptionalService
    ssrcode: The SSR Code associated with the OptionalService
    issuance_reason: A one-letter code specifying the reason for
        issuance of the OptionalService
    provider_defined_type: Original Type as sent by the provider
    total_price: The total price for this entity including base price
        and all taxes.
    base_price: Represents the base price for this entity. This does not
        include any taxes or surcharges.
    approximate_total_price: The Converted total price in Default
        Currency for this entity including base price and all taxes.
    approximate_base_price: The Converted base price in Default Currency
        for this entity. This does not include any taxes or surcharges.
    equivalent_base_price: Represents the base price in the related
        currency for this entity. This does not include any taxes or
        surcharges.
    taxes: The aggregated amount of all the taxes that are associated
        with this entity. See the associated TaxInfo array for a
        breakdown of the individual taxes.
    fees: The aggregated amount of all the fees that are associated with
        this entity. See the associated FeeInfo array for a breakdown of
        the individual fees.
    services: The total cost for all optional services.
    approximate_taxes: The Converted tax amount in Default Currency.
    approximate_fees: The Converted fee amount in Default Currency.
    key:
    assess_indicator: Indicates whether price is assessed by mileage or
        currency or both
    mileage: Indicates mileage fee/amount
    applicable_fflevel: Numerical value of the loyalty card level for
        which this service is available.
    private: Describes if service is private or not.
    ssrfree_text: Certain SSR types sent in OptionalService SSRCode
        require a free text message. For example, PETC Pet in Cabin.
    is_pricing_approximate: When set to True indicates that the pricing
        returned is approximate. Supported providers are MCH/ACH
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    chargeable: Indicates if the optional service is not offered, is
        available for a charge, or is included in the brand
    inclusive_of_tax: Identifies if the service was filed with a fee
        that is inclusive of tax.
    interline_settlement_allowed: Identifies if the interline settlement
        is allowed in service .
    geography_specification: Sector, Portion, Journey.
    excess_weight_rate: The cost of the bag per unit weight.
    source: The Source of the optional service. The source can be ACH,
        MCE, or MCH.
    viewable_only: Describes if the OptionalService is viewable only or
        not. If viewable only then the service cannot be sold.
    display_text: Title of the Optional Service.  Provider: ACH
    weight_in_excess: The excess weight of a bag. Providers: 1G, 1V, 1P,
        1J
    total_weight: The total weight of a bag. Providers: 1G, 1V, 1P, 1J
    baggage_unit_price: The per unit price of baggage. Providers: 1G,
        1V, 1P, 1J
    first_piece: Indicates the minimum occurrence of excess
        baggage.Provider: 1G, 1V, 1P, 1J.
    last_piece: Indicates the maximum occurrence of excess baggage.
        Provider: 1G, 1V, 1P, 1J.
    restricted: When set to “true”, the Optional Service is restricted
        by an embargo. Provider: 1G, 1V, 1P, 1J
    is_reprice_required: When set to “true”, the Optional Service must
        be re-priced. Provider: 1G, 1V, 1P, 1J
    booked_quantity: Indicates the Optional Service quantity already
        booked. Provider: 1G, 1V, 1P, 1J
    group: Associates Optional Services with the same ServiceSub Code,
        Air Segment, Passenger, and EMD Associated Item. Provider:1G,
        1V, 1P, 1J
    pseudo_city_code: The PCC or SID that booked the Optional Service.
    tag: Optional service group name.
    display_order: Optional service group display order.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    service_data: List[ServiceData] = field(
        default_factory=list,
        metadata={
            "name": "ServiceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    service_info: Optional[ServiceInfo] = field(
        default=None,
        metadata={
            "name": "ServiceInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    emd: Optional[Emd] = field(
        default=None,
        metadata={
            "name": "EMD",
            "type": "Element",
        }
    )
    bundled_services: Optional[BundledServices] = field(
        default=None,
        metadata={
            "name": "BundledServices",
            "type": "Element",
        }
    )
    additional_info: List[AdditionalInfo] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalInfo",
            "type": "Element",
            "max_occurs": 16,
        }
    )
    fee_application: Optional[FeeApplication] = field(
        default=None,
        metadata={
            "name": "FeeApplication",
            "type": "Element",
        }
    )
    text: List[Text] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    price_range: List[PriceRange] = field(
        default_factory=list,
        metadata={
            "name": "PriceRange",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    tour_code: Optional[TourCode] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Element",
        }
    )
    branding_info: Optional[BrandingInfo] = field(
        default=None,
        metadata={
            "name": "BrandingInfo",
            "type": "Element",
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    optional_services_rule_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptionalServicesRuleRef",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    confirmation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Confirmation",
            "type": "Attribute",
        }
    )
    secondary_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecondaryType",
            "type": "Attribute",
        }
    )
    purchase_window: Optional[TypePurchaseWindow] = field(
        default=None,
        metadata={
            "name": "PurchaseWindow",
            "type": "Attribute",
        }
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Attribute",
        }
    )
    available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Available",
            "type": "Attribute",
        }
    )
    entitled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Entitled",
            "type": "Attribute",
        }
    )
    per_traveler: bool = field(
        default=True,
        metadata={
            "name": "PerTraveler",
            "type": "Attribute",
        }
    )
    create_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
        }
    )
    payment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRef",
            "type": "Attribute",
        }
    )
    service_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceStatus",
            "type": "Attribute",
        }
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Attribute",
        }
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    ssrcode: Optional[str] = field(
        default=None,
        metadata={
            "name": "SSRCode",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 4,
        }
    )
    issuance_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuanceReason",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 1,
        }
    )
    provider_defined_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderDefinedType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: Optional[str] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    assess_indicator: Optional[TypeAssessIndicator] = field(
        default=None,
        metadata={
            "name": "AssessIndicator",
            "type": "Attribute",
        }
    )
    mileage: Optional[int] = field(
        default=None,
        metadata={
            "name": "Mileage",
            "type": "Attribute",
        }
    )
    applicable_fflevel: Optional[int] = field(
        default=None,
        metadata={
            "name": "ApplicableFFLevel",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 9,
        }
    )
    private: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Private",
            "type": "Attribute",
        }
    )
    ssrfree_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "SSRFreeText",
            "type": "Attribute",
        }
    )
    is_pricing_approximate: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsPricingApproximate",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    chargeable: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chargeable",
            "type": "Attribute",
        }
    )
    inclusive_of_tax: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InclusiveOfTax",
            "type": "Attribute",
        }
    )
    interline_settlement_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InterlineSettlementAllowed",
            "type": "Attribute",
        }
    )
    geography_specification: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeographySpecification",
            "type": "Attribute",
        }
    )
    excess_weight_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExcessWeightRate",
            "type": "Attribute",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
        }
    )
    viewable_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ViewableOnly",
            "type": "Attribute",
        }
    )
    display_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "DisplayText",
            "type": "Attribute",
        }
    )
    weight_in_excess: Optional[str] = field(
        default=None,
        metadata={
            "name": "WeightInExcess",
            "type": "Attribute",
        }
    )
    total_weight: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalWeight",
            "type": "Attribute",
        }
    )
    baggage_unit_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaggageUnitPrice",
            "type": "Attribute",
        }
    )
    first_piece: Optional[int] = field(
        default=None,
        metadata={
            "name": "FirstPiece",
            "type": "Attribute",
        }
    )
    last_piece: Optional[int] = field(
        default=None,
        metadata={
            "name": "LastPiece",
            "type": "Attribute",
        }
    )
    restricted: bool = field(
        default=False,
        metadata={
            "name": "Restricted",
            "type": "Attribute",
        }
    )
    is_reprice_required: bool = field(
        default=False,
        metadata={
            "name": "IsRepriceRequired",
            "type": "Attribute",
        }
    )
    booked_quantity: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookedQuantity",
            "type": "Attribute",
        }
    )
    group: Optional[str] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Attribute",
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        }
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        }
    )


@dataclass
class PrePayAccount:
    """
    PrePay Account associated with the customer.

    Parameters
    ----------
    credit_summary:
    pre_pay_price_info:
    program_title: Pre pay program title
    certificate_number:
    program_name: Pre pay program name
    effective_date: Effective date for the pre pay account
    expire_date: Expiry date for the pre pay account
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    credit_summary: Optional[CreditSummary] = field(
        default=None,
        metadata={
            "name": "CreditSummary",
            "type": "Element",
        }
    )
    pre_pay_price_info: Optional[PrePayPriceInfo] = field(
        default=None,
        metadata={
            "name": "PrePayPriceInfo",
            "type": "Element",
        }
    )
    program_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProgramTitle",
            "type": "Attribute",
        }
    )
    certificate_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertificateNumber",
            "type": "Attribute",
        }
    )
    program_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProgramName",
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
class RouteList:
    """
    Identifies the routes and sub-routes that were requested.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    route: List[Route] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class Row:
    """
    Identifies the row of in a seat map.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    facility: List[Facility] = field(
        default_factory=list,
        metadata={
            "name": "Facility",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    characteristic: List[Characteristic] = field(
        default_factory=list,
        metadata={
            "name": "Characteristic",
            "type": "Element",
            "max_occurs": 999,
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
    search_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SearchTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class SearchAirLeg:
    """
    Search version of AirLeg used to specify search criteria.

    Parameters
    ----------
    search_origin:
    search_destination:
    search_dep_time:
    search_arv_time: Specifies the preferred time within the time range.
        For 1G, 1V, 1P, 1J, it is supported for AvailabilitySearchReq
        (TimeRange must also be specified) and not supported for
        LowFareSearchReq. ACH does not support search by arrival time.
    air_leg_modifiers:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    search_origin: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata={
            "name": "SearchOrigin",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    search_destination: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata={
            "name": "SearchDestination",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    search_dep_time: List[TypeFlexibleTimeSpec] = field(
        default_factory=list,
        metadata={
            "name": "SearchDepTime",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    search_arv_time: List[TypeTimeSpec] = field(
        default_factory=list,
        metadata={
            "name": "SearchArvTime",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_leg_modifiers: Optional[AirLegModifiers] = field(
        default=None,
        metadata={
            "name": "AirLegModifiers",
            "type": "Element",
        }
    )


@dataclass
class SegmentModifiers:
    """
    To be used to modify the ticket modifiers for air segment.

    Parameters
    ----------
    air_segment_ref:
    ticket_validity: To be used to pass the ticket validity dates
    baggage_allowance:
    ticket_designator:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: Optional[AirSegmentRef] = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "required": True,
        }
    )
    ticket_validity: Optional[TicketValidity] = field(
        default=None,
        metadata={
            "name": "TicketValidity",
            "type": "Element",
        }
    )
    baggage_allowance: Optional[BaggageAllowance] = field(
        default=None,
        metadata={
            "name": "BaggageAllowance",
            "type": "Element",
        }
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Element",
            "min_length": 0,
            "max_length": 20,
        }
    )


@dataclass
class StructuredFareRulesType:
    """
    Parameters
    ----------
    fare_rule_category_type: For FareRulesType element
    """
    fare_rule_category_type: List[FareRuleCategoryTypes] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleCategoryType",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 99,
        }
    )


@dataclass
class AirFareDisplayReq(BaseReq):
    """
    Request to display a tariff for based on origin, destination, and other
    options.

    Parameters
    ----------
    fare_type: Provider: 1G,1V,1P,1J.
    passenger_type: Provider: 1G,1V,1P,1J.
    booking_code: Provider: 1G,1V,1P,1J.
    include_addl_booking_code_info: Provider: 1G,1V,1P,1J.
    fare_basis: Provider: 1G,1V,1P,1J.
    carrier: Provider: 1G,1V,1P,1J.
    account_code: Provider: 1G,1V,1P,1J.
    contract_code: Provider: 1G,1V.
    air_fare_display_modifiers: Provider: 1G,1V,1P,1J.
    point_of_sale: Provider: 1G,1V.
    air_fare_display_rule_key: Provider: 1G,1V,1P,1J.
    origin: Provider: 1G,1V,1P,1J.
    destination: Provider: 1G,1V,1P,1J.
    provider_code: Provider: 1G,1V,1P,1J.
    include_mile_route_information: Provider: 1G,1V,1P,1J-Used to
        request Mile/Route Information in follow on (Mile, Route, Both)
    un_saleable_fares_only: Provider: 1G,1V,1P,1J-Used to request
        unsaleable fares only also known as place of sale fares.
    channel_id: A Channel ID is 4 alpha-numeric characters used to
        activate the Search Control Console filter for a specific group
        of travelers being served by the agency credential.
    nscc: 1 to 3 numeric that define a Search Control Console
        filter.This attribute is used to override that filter.
    return_mm: If this attribute is set to true, Fare Control Manager
        processing will be invoked.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_type: List[FareType] = field(
        default_factory=list,
        metadata={
            "name": "FareType",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    passenger_type: List[TypePassengerType] = field(
        default_factory=list,
        metadata={
            "name": "PassengerType",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata={
            "name": "BookingCode",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    include_addl_booking_code_info: Optional[IncludeAddlBookingCodeInfo] = field(
        default=None,
        metadata={
            "name": "IncludeAddlBookingCodeInfo",
            "type": "Element",
        }
    )
    fare_basis: Optional[FareBasis] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Element",
        }
    )
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 10,
        }
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 5,
        }
    )
    contract_code: Optional[ContractCode] = field(
        default=None,
        metadata={
            "name": "ContractCode",
            "type": "Element",
        }
    )
    air_fare_display_modifiers: Optional[AirFareDisplayModifiers] = field(
        default=None,
        metadata={
            "name": "AirFareDisplayModifiers",
            "type": "Element",
        }
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 5,
        }
    )
    air_fare_display_rule_key: Optional[AirFareDisplayRuleKey] = field(
        default=None,
        metadata={
            "name": "AirFareDisplayRuleKey",
            "type": "Element",
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    include_mile_route_information: Optional[TypeMileOrRouteBasedFare] = field(
        default=None,
        metadata={
            "name": "IncludeMileRouteInformation",
            "type": "Attribute",
        }
    )
    un_saleable_fares_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnSaleableFaresOnly",
            "type": "Attribute",
        }
    )
    channel_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 4,
        }
    )
    nscc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        }
    )
    return_mm: bool = field(
        default=False,
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
        }
    )


@dataclass
class AirMerchandisingDetailsReq(BaseReq):
    """
    Request to retrieve brand details and optional services included in the
    brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    merchandising_details: Optional[MerchandisingDetails] = field(
        default=None,
        metadata={
            "name": "MerchandisingDetails",
            "type": "Element",
        }
    )
    optional_service_modifiers: Optional[OptionalServiceModifiers] = field(
        default=None,
        metadata={
            "name": "OptionalServiceModifiers",
            "type": "Element",
        }
    )
    merchandising_availability_details: Optional[MerchandisingAvailabilityDetails] = field(
        default=None,
        metadata={
            "name": "MerchandisingAvailabilityDetails",
            "type": "Element",
        }
    )


@dataclass
class AirPricingCommand:
    """A containter to identify individual pricing events.

    A pricing result will be returned for each pricing command according
    to its parameters.

    Parameters
    ----------
    air_pricing_modifiers:
    air_segment_pricing_modifiers:
    command_key: An identifier to link the pricing responses to the
        pricing commands. The value passed here will be returned in the
        resulting AirPricingInfo(s) from this command.
    cabin_class: Specify the cabin type to price the entire itinerary
        in. If segment level cabin selection is required, this attribute
        should not be used.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
        }
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    command_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommandKey",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        }
    )


@dataclass
class AirTicketingReq(AirBaseReq):
    """
    Request to ticket a previously stored reservation.

    Parameters
    ----------
    air_reservation_locator_code: Provider: 1G,1V,1P,1J.
    air_pricing_info_ref: Provider: 1G,1V,1P,1J-Indicates air pricing
        infos to be ticketed.
    ticketing_modifiers_ref: Provider: 1P,1J-Reference to a shared list
        of Ticketing Modifiers. This is supported for Worldspan and JAL
        providers only. When AirPricingInfoRef is used along with
        TicketingModifiersRef means that particular TicketingModifiers
        will to be applied while ticketing the Stored fare corresponding
        to the AirPricingInfo. Absence of AirPricingInfoRef means that
        particular TicketingModifiers will be applied to all Stored
        fares which are requested to be ticketed.
    waiver_code:
    commission:
    detailed_billing_information: Provider: 1G,1V.
    fax_details_information: Provider: 1V.
    air_ticketing_modifiers: Provider: 1G,1V,1P,1J.
    air_segment_ticketing_modifiers: Provider: 1P,1J.
    return_info_on_fail:
    bulk_ticket: Provider: 1G,1V,1P,1J.
    validate_spanish_residency: Provider: 1G - If set as true, Spanish
        Residency will be validated for Provisioned Customers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    air_pricing_info_ref: List["AirTicketingReq.AirPricingInfoRef"] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ticketing_modifiers_ref: List[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 18,
        }
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fax_details_information: Optional[FaxDetailsInformation] = field(
        default=None,
        metadata={
            "name": "FaxDetailsInformation",
            "type": "Element",
        }
    )
    air_ticketing_modifiers: List[AirTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirTicketingModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_segment_ticketing_modifiers: List[AirSegmentTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentTicketingModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    return_info_on_fail: bool = field(
        default=True,
        metadata={
            "name": "ReturnInfoOnFail",
            "type": "Attribute",
        }
    )
    bulk_ticket: bool = field(
        default=False,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        }
    )
    validate_spanish_residency: bool = field(
        default=False,
        metadata={
            "name": "ValidateSpanishResidency",
            "type": "Attribute",
        }
    )

    @dataclass
    class AirPricingInfoRef:
        booking_traveler_ref: List[BookingTravelerRef] = field(
            default_factory=list,
            metadata={
                "name": "BookingTravelerRef",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "max_occurs": 9,
            }
        )
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class AutoPricingInfo:
    """
    Auto Pricing based on Segment and Traveler Association.

    Parameters
    ----------
    air_segment_ref:
    booking_traveler_ref:
    air_pricing_modifiers:
    air_segment_pricing_modifiers:
    key:
    pricing_type: Indicates the Pricing Type used. The possible values
        are TicketRecord, StoredFare, PricingInstruction.
    plating_carrier: The Plating Carrier for this journey
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 100,
        }
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 100,
        }
    )
    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
        }
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
            "max_occurs": 100,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    pricing_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class BaggageAllowanceInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Baggage allowance like URL,Height,Weight etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    bag_details: List[BagDetails] = field(
        default_factory=list,
        metadata={
            "name": "BagDetails",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    traveler_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        }
    )


@dataclass
class EmdissuanceRsp(BaseRsp):
    """
    Electronic Miscellaneous Document issuance response.Supported providers are
    1V/1G/1P/1J.

    Parameters
    ----------
    emdsummary_info: List of EMDSummaryInfo elements to show minimal
        information in issuance response. Appears for ShowDetails=false
        in the request.This is the default behaviour.
    emdinfo: List of EMDInfo elements to show detailoed information in
        issuance response. Appears for ShowDetails=true in the request.
    """
    class Meta:
        name = "EMDIssuanceRsp"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDSummaryInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    emdinfo: List[Emdinfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class EmdretrieveRsp(BaseRsp):
    """
    Electronic Miscellaneous Document list and detail retrieve
    response.Supported providers are 1G/1V/1P/1J.

    Parameters
    ----------
    emdinfo: Provider: 1G/1V/1P/1J.
    emdsummary_info: Provider: 1G/1V/1P/1J.
    """
    class Meta:
        name = "EMDRetrieveRsp"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdinfo: Optional[Emdinfo] = field(
        default=None,
        metadata={
            "name": "EMDInfo",
            "type": "Element",
        }
    )
    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDSummaryInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class FareDisplay:
    """
    Fare/Tariff Display.

    Parameters
    ----------
    fare_display_rule:
    fare_pricing:
    fare_restriction:
    fare_routing_information:
    fare_mileage_information:
    air_fare_display_rule_key:
    booking_code:
    account_code:
    addl_booking_code_information:
    fare_rule_failure_info: Returns fare rule failure info for Non Valid
        fares.
    price_change: Indicates a price change is found in Fare Control
        Manager
    carrier:
    fare_basis:
    amount:
    trip_type:
    fare_type_code:
    special_fare:
    instant_purchase:
    eligibility_restricted:
    flight_restricted:
    stopovers_restricted:
    transfers_restricted:
    blackouts_exist:
    accompanied_travel:
    mile_or_route_based_fare:
    global_indicator:
    origin: Returns the origin airport or city code for which this
        tariff is applicable.
    destination: Returns the destination airport or city code for which
        this tariff is applicable.
    fare_ticketing_code: Returns the ticketing code for which this
        tariff is applicable.
    fare_ticketing_designator: Returns the ticketing designator for
        which this tariff is applicable.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_display_rule: Optional[FareDisplayRule] = field(
        default=None,
        metadata={
            "name": "FareDisplayRule",
            "type": "Element",
            "required": True,
        }
    )
    fare_pricing: List[FarePricing] = field(
        default_factory=list,
        metadata={
            "name": "FarePricing",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    fare_restriction: List[FareRestriction] = field(
        default_factory=list,
        metadata={
            "name": "FareRestriction",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    fare_routing_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareRoutingInformation",
            "type": "Element",
        }
    )
    fare_mileage_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareMileageInformation",
            "type": "Element",
        }
    )
    air_fare_display_rule_key: Optional[AirFareDisplayRuleKey] = field(
        default=None,
        metadata={
            "name": "AirFareDisplayRuleKey",
            "type": "Element",
        }
    )
    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata={
            "name": "BookingCode",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    addl_booking_code_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddlBookingCodeInformation",
            "type": "Element",
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    fare_rule_failure_info: Optional[FareRuleFailureInfo] = field(
        default=None,
        metadata={
            "name": "FareRuleFailureInfo",
            "type": "Element",
        }
    )
    price_change: List[PriceChangeType] = field(
        default_factory=list,
        metadata={
            "name": "PriceChange",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    trip_type: Optional[TypeFareTripType] = field(
        default=None,
        metadata={
            "name": "TripType",
            "type": "Attribute",
        }
    )
    fare_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareTypeCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    special_fare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpecialFare",
            "type": "Attribute",
        }
    )
    instant_purchase: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InstantPurchase",
            "type": "Attribute",
        }
    )
    eligibility_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EligibilityRestricted",
            "type": "Attribute",
        }
    )
    flight_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FlightRestricted",
            "type": "Attribute",
        }
    )
    stopovers_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StopoversRestricted",
            "type": "Attribute",
        }
    )
    transfers_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TransfersRestricted",
            "type": "Attribute",
        }
    )
    blackouts_exist: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BlackoutsExist",
            "type": "Attribute",
        }
    )
    accompanied_travel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccompaniedTravel",
            "type": "Attribute",
        }
    )
    mile_or_route_based_fare: Optional[TypeMileOrRouteBasedFare] = field(
        default=None,
        metadata={
            "name": "MileOrRouteBasedFare",
            "type": "Attribute",
        }
    )
    global_indicator: Optional[TypeAtpcoglobalIndicator] = field(
        default=None,
        metadata={
            "name": "GlobalIndicator",
            "type": "Attribute",
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    fare_ticketing_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareTicketingCode",
            "type": "Attribute",
        }
    )
    fare_ticketing_designator: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareTicketingDesignator",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        }
    )


@dataclass
class FareRule:
    """
    Fare Rule Container.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_rule_long: List[FareRuleLong] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleLong",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_rule_short: List[FareRuleShort] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleShort",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rule_advanced_purchase: Optional[RuleAdvancedPurchase] = field(
        default=None,
        metadata={
            "name": "RuleAdvancedPurchase",
            "type": "Element",
        }
    )
    rule_length_of_stay: Optional[RuleLengthOfStay] = field(
        default=None,
        metadata={
            "name": "RuleLengthOfStay",
            "type": "Element",
        }
    )
    rule_charges: Optional[RuleCharges] = field(
        default=None,
        metadata={
            "name": "RuleCharges",
            "type": "Element",
        }
    )
    fare_rule_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleResultMessage",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    structured_fare_rules: Optional[StructuredFareRulesType] = field(
        default=None,
        metadata={
            "name": "StructuredFareRules",
            "type": "Element",
        }
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
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
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
        }
    )
    tariff_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TariffNumber",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )


@dataclass
class FlightDetailsList:
    """
    The shared object list of FlightDetails.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_details: List[FlightDetails] = field(
        default_factory=list,
        metadata={
            "name": "FlightDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class FlightInformationRsp(BaseRsp):
    """
    Parameters
    ----------
    flight_info: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_info: List[FlightInfo] = field(
        default_factory=list,
        metadata={
            "name": "FlightInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class FlightOption:
    """
    List of Options available for any search air leg.

    Parameters
    ----------
    option: List of BookingInfo available for the search air leg.
    leg_ref: Identifies the Leg Reference for this Flight Option.
    origin: The IATA location code for this origination of this entity.
    destination: The IATA location code for this destination of this
        entity.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    option: List[Option] = field(
        default_factory=list,
        metadata={
            "name": "Option",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    leg_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegRef",
            "type": "Attribute",
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )


@dataclass
class FlightTimeTableRsp(BaseSearchRsp):
    """
    Response for Flight Time Table.

    Parameters
    ----------
    flight_time_table_list: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_time_table_list: Optional["FlightTimeTableRsp.FlightTimeTableList"] = field(
        default=None,
        metadata={
            "name": "FlightTimeTableList",
            "type": "Element",
        }
    )

    @dataclass
    class FlightTimeTableList:
        flight_time_detail: List[FlightTimeDetail] = field(
            default_factory=list,
            metadata={
                "name": "FlightTimeDetail",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class OptionalServices:
    """
    A wrapper for all the information regarding each of the Optional services.

    Parameters
    ----------
    optional_services_total: The total fares, fees and taxes associated
        with the Optional Services
    optional_service:
    grouped_option_info: Details about an unselected or "other" option
        when optional services are grouped together.
    optional_service_rules: Holds the rules for selecting the optional
        service in the itinerary
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    optional_services_total: Optional["OptionalServices.OptionalServicesTotal"] = field(
        default=None,
        metadata={
            "name": "OptionalServicesTotal",
            "type": "Element",
        }
    )
    optional_service: List[OptionalService] = field(
        default_factory=list,
        metadata={
            "name": "OptionalService",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    grouped_option_info: List[GroupedOptionInfo] = field(
        default_factory=list,
        metadata={
            "name": "GroupedOptionInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    optional_service_rules: List[ServiceRuleType] = field(
        default_factory=list,
        metadata={
            "name": "OptionalServiceRules",
            "type": "Element",
            "max_occurs": 999,
        }
    )

    @dataclass
    class OptionalServicesTotal:
        """
        Parameters
        ----------
        tax_info:
        fee_info:
        total_price: The total price for this entity including base
            price and all taxes.
        base_price: Represents the base price for this entity. This does
            not include any taxes or surcharges.
        approximate_total_price: The Converted total price in Default
            Currency for this entity including base price and all taxes.
        approximate_base_price: The Converted base price in Default
            Currency for this entity. This does not include any taxes or
            surcharges.
        equivalent_base_price: Represents the base price in the related
            currency for this entity. This does not include any taxes or
            surcharges.
        taxes: The aggregated amount of all the taxes that are
            associated with this entity. See the associated TaxInfo
            array for a breakdown of the individual taxes.
        fees: The aggregated amount of all the fees that are associated
            with this entity. See the associated FeeInfo array for a
            breakdown of the individual fees.
        services: The total cost for all optional services.
        approximate_taxes: The Converted tax amount in Default Currency.
        approximate_fees: The Converted fee amount in Default Currency.
        """
        tax_info: List[TaxInfo] = field(
            default_factory=list,
            metadata={
                "name": "TaxInfo",
                "type": "Element",
                "max_occurs": 999,
            }
        )
        fee_info: List[FeeInfo] = field(
            default_factory=list,
            metadata={
                "name": "FeeInfo",
                "type": "Element",
                "max_occurs": 999,
            }
        )
        total_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalPrice",
                "type": "Attribute",
            }
        )
        base_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "BasePrice",
                "type": "Attribute",
            }
        )
        approximate_total_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "ApproximateTotalPrice",
                "type": "Attribute",
            }
        )
        approximate_base_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "ApproximateBasePrice",
                "type": "Attribute",
            }
        )
        equivalent_base_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "EquivalentBasePrice",
                "type": "Attribute",
            }
        )
        taxes: Optional[str] = field(
            default=None,
            metadata={
                "name": "Taxes",
                "type": "Attribute",
            }
        )
        fees: Optional[str] = field(
            default=None,
            metadata={
                "name": "Fees",
                "type": "Attribute",
            }
        )
        services: Optional[str] = field(
            default=None,
            metadata={
                "name": "Services",
                "type": "Attribute",
            }
        )
        approximate_taxes: Optional[str] = field(
            default=None,
            metadata={
                "name": "ApproximateTaxes",
                "type": "Attribute",
            }
        )
        approximate_fees: Optional[str] = field(
            default=None,
            metadata={
                "name": "ApproximateFees",
                "type": "Attribute",
            }
        )


@dataclass
class PrePayProfileInfo:
    """
    PrePay Profile associated with the customer.

    Parameters
    ----------
    pre_pay_id: Pre pay unique identifier detail.This information block
        is returned both in list and  detail retrieve
        transactions.Example flight pass number
    pre_pay_customer: Pre pay customer detail.This information block is
        returned both in list and  detail retrieve transactions.
    pre_pay_account: Pre pay account detail.This information block is
        returned both in list and  detail retrieve transactions.
    affiliations: Pre pay affiliations detail.This information block is
        returned only in detail retrieve transactions.
    account_related_rules: Pre pay account related rules.This
        information block is returned only in detail retrieve
        transactions.
    status_code: Customer pre pay profile status code(One of Marked for
        deletion,Lapsed,Terminated,Active,Inactive)
    creator_id: This is the loyalty card number of the person who
        originally purchased/setup the flight pass
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    pre_pay_id: Optional[PrePayId] = field(
        default=None,
        metadata={
            "name": "PrePayId",
            "type": "Element",
            "required": True,
        }
    )
    pre_pay_customer: Optional[PrePayCustomer] = field(
        default=None,
        metadata={
            "name": "PrePayCustomer",
            "type": "Element",
        }
    )
    pre_pay_account: Optional[PrePayAccount] = field(
        default=None,
        metadata={
            "name": "PrePayAccount",
            "type": "Element",
        }
    )
    affiliations: Optional[Affiliations] = field(
        default=None,
        metadata={
            "name": "Affiliations",
            "type": "Element",
        }
    )
    account_related_rules: Optional[AccountRelatedRules] = field(
        default=None,
        metadata={
            "name": "AccountRelatedRules",
            "type": "Element",
        }
    )
    status_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Attribute",
        }
    )
    creator_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreatorID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 36,
        }
    )


@dataclass
class Rows:
    """A wrapper for all the information regarding each of the rows.

    Providers: ACH, 1G, 1V, 1P, 1J

    Parameters
    ----------
    row: Provider: 1G,1V,1P,1J,ACH,MCH.
    segment_ref: Specifies the AirSegment the seat map is for.
        Providers: ACH, 1G, 1V, 1P, 1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    row: List[Row] = field(
        default_factory=list,
        metadata={
            "name": "Row",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )


@dataclass
class TicketingModifiers:
    """
    A container to identify individual ticketing modifiers.

    Parameters
    ----------
    booking_traveler_ref: Reference to a booking traveler for which
        ticketing modifier is applied.
    net_remit: Allows an agency to override the net remittance amount -
        varies by BSP agreement
    net_fare: Net Fare amount for a ticketed fare
    actual_selling_fare: Allows an agency to report an Actual Selling
        Fare as part of the net remittance BSP agreement
    invoice_fare: Allows an agency to report an Invoice Fare as part of
        the net remittance BSP agreement
    corporate_discount: Allows an agency to add a corporate discount to
        the itinerary to be ticketed
    accounting_info: Allows an agency to report Accounting Information
        as part of the net remittance BSP agreement
    bulk_ticket: Allows an agency to update the fare as a Bulk ticket -
        Optional SuppressOnFareCalc attribute will control how fare
        calculation is printed on the ticket
    group_tour: Allows an agency to update the fare as a Group Tour
        (inclusive tour) ticket - Optional SuppressOnFareCalc attribute
        will control how fare calculation is printed on the ticket
    commission: Allows an agency to update the commission to a new or
        different commission rate which will be applied at time of
        ticketing. The commission Modifier allows the user specify how
        the commission change is to applied
    tour_code: Allows an agency to modify the tour code information on
        the ticket
    ticket_endorsement: Allows an agency to add user defined ticketing
        endorsements the ticket
    value_modifier: Allows an agency to modify value or commission of
        the ticket. The modifier is generic and depends on the specific
        GDS and BSP implementation
    document_select:
    document_options:
    segment_select:
    segment_modifiers:
    supplier_locator:
    destination_purpose_code:
    language_option:
    land_charges:
    print_blank_form_itinerary:
    exclude_ticketing:
    exempt_obfee:
    is_primary_di: Indicates if the DI is Primary DI. 1P only
    document_instruction_number: The Document Instruction line number.
        1P only
    reference: Identifies if TicketingModifiers contains DI line
        information. 1P only.
    status: DI line status - ex:Ticketed
    free_text: DI line information shown as free text as in Host. 1P
        only
    name_number: Host Name Number
    ticket_record: Ticket Record Number
    plating_carrier: Allows an agency to specify the Plating Carrier for
        ticketing
    exempt_vat: Allows an agency to update if VAT is Exemtped on the
        fare.
    net_remit_applied: Indicator to the BSP net remittance scheme
        applies to ticketed fare.
    free_ticket: Indicates free ticket.
    currency_override_code: This modifier allows an agency to specify
        the currency like L for Local, E for Euro, U for USD, C for CAD
        (Canadian dollars).
    key:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    net_remit: Optional[TypeTicketModifierAmountType] = field(
        default=None,
        metadata={
            "name": "NetRemit",
            "type": "Element",
        }
    )
    net_fare: Optional[TypeTicketModifierAmountType] = field(
        default=None,
        metadata={
            "name": "NetFare",
            "type": "Element",
        }
    )
    actual_selling_fare: Optional[TypeTicketModifierAmountType] = field(
        default=None,
        metadata={
            "name": "ActualSellingFare",
            "type": "Element",
        }
    )
    invoice_fare: Optional[TypeTicketModifierAccountingType] = field(
        default=None,
        metadata={
            "name": "InvoiceFare",
            "type": "Element",
        }
    )
    corporate_discount: Optional[TypeTicketModifierAccountingType] = field(
        default=None,
        metadata={
            "name": "CorporateDiscount",
            "type": "Element",
        }
    )
    accounting_info: Optional[TypeTicketModifierAccountingType] = field(
        default=None,
        metadata={
            "name": "AccountingInfo",
            "type": "Element",
        }
    )
    bulk_ticket: Optional["TicketingModifiers.BulkTicket"] = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Element",
        }
    )
    group_tour: Optional[TypeBulkTicketModifierType] = field(
        default=None,
        metadata={
            "name": "GroupTour",
            "type": "Element",
        }
    )
    commission: Optional[Commission] = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    tour_code: Optional[TourCode] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Element",
        }
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata={
            "name": "TicketEndorsement",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    value_modifier: Optional[TypeTicketModifierValueType] = field(
        default=None,
        metadata={
            "name": "ValueModifier",
            "type": "Element",
        }
    )
    document_select: Optional[DocumentSelect] = field(
        default=None,
        metadata={
            "name": "DocumentSelect",
            "type": "Element",
        }
    )
    document_options: Optional[DocumentOptions] = field(
        default=None,
        metadata={
            "name": "DocumentOptions",
            "type": "Element",
        }
    )
    segment_select: Optional[SegmentSelect] = field(
        default=None,
        metadata={
            "name": "SegmentSelect",
            "type": "Element",
        }
    )
    segment_modifiers: List[SegmentModifiers] = field(
        default_factory=list,
        metadata={
            "name": "SegmentModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    supplier_locator: Optional[SupplierLocator] = field(
        default=None,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    destination_purpose_code: Optional[DestinationPurposeCode] = field(
        default=None,
        metadata={
            "name": "DestinationPurposeCode",
            "type": "Element",
        }
    )
    language_option: List[LanguageOption] = field(
        default_factory=list,
        metadata={
            "name": "LanguageOption",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    land_charges: Optional[LandCharges] = field(
        default=None,
        metadata={
            "name": "LandCharges",
            "type": "Element",
        }
    )
    print_blank_form_itinerary: Optional[PrintBlankFormItinerary] = field(
        default=None,
        metadata={
            "name": "PrintBlankFormItinerary",
            "type": "Element",
        }
    )
    exclude_ticketing: Optional[ExcludeTicketing] = field(
        default=None,
        metadata={
            "name": "ExcludeTicketing",
            "type": "Element",
        }
    )
    exempt_obfee: Optional[ExemptObfee] = field(
        default=None,
        metadata={
            "name": "ExemptOBFee",
            "type": "Element",
        }
    )
    is_primary_di: bool = field(
        default=False,
        metadata={
            "name": "IsPrimaryDI",
            "type": "Attribute",
        }
    )
    document_instruction_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentInstructionNumber",
            "type": "Attribute",
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "max_length": 30,
        }
    )
    free_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "FreeText",
            "type": "Attribute",
            "max_length": 756,
        }
    )
    name_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameNumber",
            "type": "Attribute",
        }
    )
    ticket_record: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketRecord",
            "type": "Attribute",
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    exempt_vat: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExemptVAT",
            "type": "Attribute",
        }
    )
    net_remit_applied: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NetRemitApplied",
            "type": "Attribute",
        }
    )
    free_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeTicket",
            "type": "Attribute",
        }
    )
    currency_override_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyOverrideCode",
            "type": "Attribute",
            "length": 1,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )

    @dataclass
    class BulkTicket(TypeBulkTicketModifierType):
        """
        Parameters
        ----------
        non_refundable: Indicates bulk ticket being non-refundable
        """
        non_refundable: Optional[bool] = field(
            default=None,
            metadata={
                "name": "NonRefundable",
                "type": "Attribute",
            }
        )


@dataclass
class TypeBaseAirSegment(Segment):
    """
    Parameters
    ----------
    sponsored_flt_info:
    codeshare_info:
    air_avail_info:
    flight_details:
    flight_details_ref:
    alternate_location_distance_ref:
    connection:
    sell_message:
    rail_coach_details:
    open_segment: Indicates OpenSegment when True
    group: The Origin Destination Grouping of this segment.
    carrier: The carrier that is marketing this segment
    cabin_class: Specifies Cabin class for a group of class of services.
        Cabin class is not identified if it is not present.
    flight_number: The flight number under which the marketing carrier
        is marketing this flight
    origin: The IATA location code for this origination of this entity.
    destination: The IATA location code for this destination of this
        entity.
    departure_time: The date and time at which this entity departs. Date
        and time are represented as Airport Local Time at the place of
        departure. The correct time zone offset is also included.
    arrival_time: The date and time at which this entity arrives at the
        destination. Date and time are represented as Airport Local Time
        at the place of arrival. The correct time zone offset is also
        included.
    flight_time: Time spent (minutes) traveling in flight, including
        airport taxi time.
    travel_time: Total time spent (minutes) traveling including flight
        time and ground time.
    distance: The distance traveled. Units are specified in the parent
        response element.
    provider_code:
    supplier_code:
    participant_level: Type of sell agreement between host and link
        carrier.
    link_availability: Indicates if carrier has link (carrier specific)
        display option.
    polled_availability_option: Indicates if carrier has Inside
        (polled)Availability option.
    availability_display_type: The type of availability from which the
        segment is sold.Possible Values (List): G - General S - Flight
        Specific L - Carrier Specific/Direct Access M - Manual Sell F -
        Fare Shop/Optimal Shop Q - Fare Specific Fare Quote unbooked R -
        Redemption Availability used to complete the sell. Supported
        Providers: 1G,1V.
    class_of_service:
    eticketability: Identifies if this particular segment is
        E-Ticketable
    equipment: Identifies the equipment that this segment is operating
        under.
    marriage_group: Identifies this segment as being a married segment.
        It is paired with other segments of the same value.
    number_of_stops: Identifies the number of stops for each within the
        segment.
    seamless: Identifies that this segment was sold via a direct access
        channel to the marketing carrier.
    change_of_plane: Indicates the traveler must change planes between
        flights.
    guaranteed_payment_carrier: Identifies that this segment has
        Guaranteed Payment Carrier.
    host_token_ref: Identifies that this segment has Guaranteed Payment
        Carrier.
    provider_reservation_info_ref: Provider reservation reference key.
    passive_provider_reservation_info_ref: Provider reservation
        reference key.
    optional_services_indicator: Indicates true if flight provides
        optional services.
    availability_source: Indicates Availability source of AirSegment.
    apisrequirements_ref: Reference to the APIS Requirements for this
        AirSegment.
    black_listed: Indicates blacklisted carriers which are banned from
        servicing points to, from and within the European Community.
    operational_status: Refers to the flight operational status for the
        segment. This attribute will only be returned in the
        AvailabilitySearchRsp and not used/returned in any other
        request/responses. If this attribute is not returned back in the
        response, it means the flight is operational and not past
        scheduled departure.
    number_in_party: Number of person traveling in this air segment
        excluding the number of infants on lap.
    rail_coach_number: Coach number for which rail seatmap/coachmap is
        returned.
    booking_date: Used for rapid reprice. The date the booking was made.
        Providers: 1G/1V/1P/1S/1A
    flown_segment: Used for rapid reprice. Tells whether or not the air
        segment has been flown. Providers: 1G/1V/1P/1S/1A
    schedule_change: Used for rapid reprice. Tells whether or not the
        air segment had a schedule change by the carrier. This tells
        rapid reprice that the change in the air segment was involuntary
        and because of a schedule change, not because the user is
        changing the segment. Providers: 1G/1V/1P/1S/1A
    brand_indicator: Value “B” specifies that the carrier supports Rich
        Content and Branding.  The Brand Indicator is only returned in
        the availability search response.  Provider: 1G, 1V, 1P, 1J, ACH
    """
    class Meta:
        name = "typeBaseAirSegment"

    sponsored_flt_info: Optional[SponsoredFltInfo] = field(
        default=None,
        metadata={
            "name": "SponsoredFltInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    codeshare_info: Optional[CodeshareInfo] = field(
        default=None,
        metadata={
            "name": "CodeshareInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    air_avail_info: List[AirAvailInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirAvailInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    flight_details: List[FlightDetails] = field(
        default_factory=list,
        metadata={
            "name": "FlightDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    flight_details_ref: List[FlightDetailsRef] = field(
        default_factory=list,
        metadata={
            "name": "FlightDetailsRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    alternate_location_distance_ref: List[AlternateLocationDistanceRef] = field(
        default_factory=list,
        metadata={
            "name": "AlternateLocationDistanceRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    connection: Optional[Connection] = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    sell_message: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SellMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    rail_coach_details: List[RailCoachDetails] = field(
        default_factory=list,
        metadata={
            "name": "RailCoachDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    open_segment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OpenSegment",
            "type": "Attribute",
        }
    )
    group: Optional[int] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Attribute",
            "required": True,
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        }
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    flight_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "FlightTime",
            "type": "Attribute",
        }
    )
    travel_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        }
    )
    distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    participant_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantLevel",
            "type": "Attribute",
        }
    )
    link_availability: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LinkAvailability",
            "type": "Attribute",
        }
    )
    polled_availability_option: Optional[str] = field(
        default=None,
        metadata={
            "name": "PolledAvailabilityOption",
            "type": "Attribute",
        }
    )
    availability_display_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityDisplayType",
            "type": "Attribute",
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    eticketability: Optional[TypeEticketability] = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
        }
    )
    equipment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Attribute",
            "length": 3,
        }
    )
    marriage_group: Optional[int] = field(
        default=None,
        metadata={
            "name": "MarriageGroup",
            "type": "Attribute",
        }
    )
    number_of_stops: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfStops",
            "type": "Attribute",
        }
    )
    seamless: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Seamless",
            "type": "Attribute",
        }
    )
    change_of_plane: bool = field(
        default=False,
        metadata={
            "name": "ChangeOfPlane",
            "type": "Attribute",
        }
    )
    guaranteed_payment_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "GuaranteedPaymentCarrier",
            "type": "Attribute",
        }
    )
    host_token_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    passive_provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    optional_services_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OptionalServicesIndicator",
            "type": "Attribute",
        }
    )
    availability_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilitySource",
            "type": "Attribute",
            "max_length": 1,
        }
    )
    apisrequirements_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "APISRequirementsRef",
            "type": "Attribute",
        }
    )
    black_listed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BlackListed",
            "type": "Attribute",
        }
    )
    operational_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationalStatus",
            "type": "Attribute",
        }
    )
    number_in_party: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberInParty",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    rail_coach_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    booking_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingDate",
            "type": "Attribute",
        }
    )
    flown_segment: bool = field(
        default=False,
        metadata={
            "name": "FlownSegment",
            "type": "Attribute",
        }
    )
    schedule_change: bool = field(
        default=False,
        metadata={
            "name": "ScheduleChange",
            "type": "Attribute",
        }
    )
    brand_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandIndicator",
            "type": "Attribute",
        }
    )


@dataclass
class AirFareDisplayRsp(BaseRsp):
    """
    Response to an AirFareDisplayReq.

    Parameters
    ----------
    fare_display: Provider: 1G,1V,1P,1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_display: List[FareDisplay] = field(
        default_factory=list,
        metadata={
            "name": "FareDisplay",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirFareRulesRsp(BaseRsp):
    """
    Response to an AirFareRuleReq.

    Parameters
    ----------
    fare_rule: Provider: 1G,1V,1P,1J,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirPrePayRsp(BaseRsp):
    """
    Flight Pass Response.

    Parameters
    ----------
    pre_pay_profile_info: Provider: ACH.
    max_results: Provider: ACH-Max Number of Flight Passes being
        returned.
    more_indicator: Provider: ACH-Indicates if there are more flight
        passes to be offered
    more_data_start_index: Provider: ACH-Indicates start index of the
        next flight Passes
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    pre_pay_profile_info: List[PrePayProfileInfo] = field(
        default_factory=list,
        metadata={
            "name": "PrePayProfileInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    max_results: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 200,
        }
    )
    more_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreIndicator",
            "type": "Attribute",
        }
    )
    more_data_start_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "MoreDataStartIndex",
            "type": "Attribute",
        }
    )


@dataclass
class AirPricingTicketingModifiers:
    """AirPricing TicketingModifier information.

    - used to associate Ticketing Modifiers with one or more
    AirPricingInfos/ProviderReservationInfo
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ticketing_modifiers: Optional[TicketingModifiers] = field(
        default=None,
        metadata={
            "name": "TicketingModifiers",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AirSegment(TypeBaseAirSegment):
    """
    An Air marketable travel segment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class BaggageAllowances:
    """
    Details of Baggage allowance.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    baggage_allowance_info: List[BaggageAllowanceInfo] = field(
        default_factory=list,
        metadata={
            "name": "BaggageAllowanceInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    carry_on_allowance_info: List[CarryOnAllowanceInfo] = field(
        default_factory=list,
        metadata={
            "name": "CarryOnAllowanceInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    embargo_info: List[EmbargoInfo] = field(
        default_factory=list,
        metadata={
            "name": "EmbargoInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class Brand:
    """
    Commercially recognized product offered by an airline.

    Parameters
    ----------
    title: The additional titles associated to the brand
    text: Text associated to the brand
    image_location: Images associated to the brand
    optional_services:
    rules: Brand rules
    service_associations: Service associated with this brand
    upsell_brand: The unique identifier of the Upsell brand
    applicable_segment:
    default_brand_detail: Default brand details.
    key: Brand Key
    brand_id: The unique identifier of the brand
    name: The Title of the brand
    air_itinerary_details_ref: AirItinerary associated with this brand
    up_sell_brand_id:
    brand_found: Indicates whether brand for the fare was found for
        carrier or not
    up_sell_brand_found: Indicates whether upsell brand for the fare was
        found for carrier or not
    branded_details_available: Indicates if full details of the brand is
        available
    carrier:
    brand_tier: Modifier to price by specific brand tier number.
    brand_maintained: Indicates whether the brand was maintained from
        the original ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    title: List[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    text: List[Text] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata={
            "name": "ImageLocation",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    rules: List[Rules] = field(
        default_factory=list,
        metadata={
            "name": "Rules",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    service_associations: Optional[ServiceAssociations] = field(
        default=None,
        metadata={
            "name": "ServiceAssociations",
            "type": "Element",
        }
    )
    upsell_brand: Optional[UpsellBrand] = field(
        default=None,
        metadata={
            "name": "UpsellBrand",
            "type": "Element",
        }
    )
    applicable_segment: List[TypeApplicableSegment] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableSegment",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    default_brand_detail: List[DefaultBrandDetail] = field(
        default_factory=list,
        metadata={
            "name": "DefaultBrandDetail",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 19,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    air_itinerary_details_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirItineraryDetailsRef",
            "type": "Attribute",
        }
    )
    up_sell_brand_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UpSellBrandID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 19,
        }
    )
    brand_found: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BrandFound",
            "type": "Attribute",
        }
    )
    up_sell_brand_found: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UpSellBrandFound",
            "type": "Attribute",
        }
    )
    branded_details_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BrandedDetailsAvailable",
            "type": "Attribute",
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    brand_tier: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandTier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )
    brand_maintained: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandMaintained",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 99,
        }
    )


@dataclass
class FlightOptionsList:
    """
    List of Flight Options for the itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_option: List[FlightOption] = field(
        default_factory=list,
        metadata={
            "name": "FlightOption",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirItinerary:
    """
    A container for an Air only travel itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    apisrequirements: List[Apisrequirements] = field(
        default_factory=list,
        metadata={
            "name": "APISRequirements",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirMerchandisingDetailsRsp(BaseRsp):
    """
    Response for retrieved brand details and optional services included in
    them.

    Parameters
    ----------
    optional_services:
    brand:
    unassociated_booking_code_list: Lists classes of service by segment
        sent in the request which are not associated to a brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    brand: List[Brand] = field(
        default_factory=list,
        metadata={
            "name": "Brand",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    unassociated_booking_code_list: Optional["AirMerchandisingDetailsRsp.UnassociatedBookingCodeList"] = field(
        default=None,
        metadata={
            "name": "UnassociatedBookingCodeList",
            "type": "Element",
        }
    )

    @dataclass
    class UnassociatedBookingCodeList:
        applicable_segment: List[TypeApplicableSegment] = field(
            default_factory=list,
            metadata={
                "name": "ApplicableSegment",
                "type": "Element",
                "max_occurs": 99,
            }
        )


@dataclass
class AirSegmentData:
    """
    The shared object list of AirsegmentData.

    Parameters
    ----------
    air_segment_ref:
    baggage_allowance:
    brand:
    cabin_class: Specifies Cabin class for a group of class of services.
        Cabin class is not identified if it is not present.
    class_of_service:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    baggage_allowance: List[BaggageAllowance] = field(
        default_factory=list,
        metadata={
            "name": "BaggageAllowance",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    brand: List[Brand] = field(
        default_factory=list,
        metadata={
            "name": "Brand",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )


@dataclass
class AirSegmentError:
    """
    Container to return error messages corresponding to AirSegment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: Optional[AirSegment] = field(
        default=None,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "required": True,
        }
    )
    error_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AirSegmentList:
    """
    The shared object list of AirSegments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AirSolution:
    """
    Defines an air solution that is comprised of an itinerary (the segments)
    along with the passengers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "name": "SearchTraveler",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 16,
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 16,
        }
    )
    fare_basis: List[FareBasis] = field(
        default_factory=list,
        metadata={
            "name": "FareBasis",
            "type": "Element",
            "max_occurs": 16,
        }
    )


@dataclass
class BrandList:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    brand: List[Brand] = field(
        default_factory=list,
        metadata={
            "name": "Brand",
            "type": "Element",
            "max_occurs": 99,
        }
    )


@dataclass
class ExchangeAirSegment:
    """
    A container to define segment and cabin class in order to process an
    exchange.

    Parameters
    ----------
    air_segment:
    cabin_class:
    fare_basis_code: The fare basis code to be used for exchange of this
        segment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: Optional[AirSegment] = field(
        default=None,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "required": True,
        }
    )
    cabin_class: Optional[CabinClass] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    fare_basis_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasisCode",
            "type": "Attribute",
        }
    )


@dataclass
class FareInfo:
    """
    Information about this fare component.

    Parameters
    ----------
    fare_ticket_designator:
    fare_surcharge:
    account_code:
    contract_code:
    endorsement:
    baggage_allowance:
    fare_rule_key:
    fare_rule_failure_info:
    fare_remark_ref:
    brand:
    commission: Specifies the Commission for Agency for a particular
        Fare component. Apllicable Providers are 1G and 1V.
    fare_attributes: Returns all fare attributes separated by pipe ‘|’.
        Attribute information is returned by comma separated values for
        each attribute. These information include attribute number,
        chargeable indicator and supplementary info. Attribute numbers:
        1 - Checked Bag, 2 - Carry On, 3 - Rebooking, 4 - Refund, 5 -
        Seats, 6 - Meals, 7 - WiFi. Chargeable Indicator: Y -
        Chargeable, N - Not Chargeable. Supplementary Information that
        will be returned is : For 1 and 2 - Baggage weights. For 3 –
        Changeable Info. For 4 – Refundable Info. For 5 - Seat
        description. For 6 – Meal description. For 7 – WiFi description.
        Example:
        1,Y,23|1,N,50|2,N,8|3,N,CHANGEABLE|4,Y,REFUNDABLE|5,N,SEATING|5,N,MIDDLE|6,Y,SOFT
        DRINK|6,N,ALCOHOLIC DRINK|6,Y,SNACK|7,X,WIFI
    change_penalty: The penalty (if any) to change the itinerary
    cancel_penalty: The penalty (if any) to cancel the fare
    fare_rules_filter:
    key:
    fare_basis: The fare basis code for this fare
    passenger_type_code: The PTC that is associated with this fare.
    origin: Returns the airport or city code that defines the origin
        market for this fare.
    destination: Returns the airport or city code that defines the
        destination market for this fare.
    effective_date: Returns the date on which this fare was quoted
    travel_date: Returns the departure date of the first segment that
        uses this fare.
    departure_date: Returns the departure date of the first segment of
        the journey.
    amount:
    private_fare:
    negotiated_fare: Identifies the fare as a Negotiated Fare.
    tour_code:
    waiver_code:
    not_valid_before: Fare not valid before this date.
    not_valid_after: Fare not valid after this date.
    pseudo_city_code: Provider PseudoCityCode associated with private
        fare.
    fare_family: An alpha-numeric string which denotes fare family. Some
        carriers may return this in lieu of or in addition to the
        CabinClass.
    promotional_fare: Boolean to describe whether the Fare is
        Promotional fare or not.
    car_code:
    value_code:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    bulk_ticket: Whether the ticket can be issued as bulk for this fare.
        Providers supported: Worldspan and JAL
    inclusive_tour: Whether the ticket can be issued as part of included
        package for this fare. Providers supported: Worldspan and JAL
    value: Used in rapid reprice
    supplier_code: Code of the provider returning this fare info
    tax_amount: Currency code and value for the approximate tax amount
        for this fare component.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_ticket_designator: List[FareTicketDesignator] = field(
        default_factory=list,
        metadata={
            "name": "FareTicketDesignator",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_surcharge: List[FareSurcharge] = field(
        default_factory=list,
        metadata={
            "name": "FareSurcharge",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    contract_code: List[ContractCode] = field(
        default_factory=list,
        metadata={
            "name": "ContractCode",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    endorsement: List[Endorsement] = field(
        default_factory=list,
        metadata={
            "name": "Endorsement",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    baggage_allowance: Optional[BaggageAllowance] = field(
        default=None,
        metadata={
            "name": "BaggageAllowance",
            "type": "Element",
        }
    )
    fare_rule_key: Optional[FareRuleKey] = field(
        default=None,
        metadata={
            "name": "FareRuleKey",
            "type": "Element",
        }
    )
    fare_rule_failure_info: Optional[FareRuleFailureInfo] = field(
        default=None,
        metadata={
            "name": "FareRuleFailureInfo",
            "type": "Element",
        }
    )
    fare_remark_ref: List[FareRemarkRef] = field(
        default_factory=list,
        metadata={
            "name": "FareRemarkRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    brand: Optional[Brand] = field(
        default=None,
        metadata={
            "name": "Brand",
            "type": "Element",
        }
    )
    commission: Optional[Commission] = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    fare_attributes: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareAttributes",
            "type": "Element",
        }
    )
    change_penalty: Optional[TypeFarePenalty] = field(
        default=None,
        metadata={
            "name": "ChangePenalty",
            "type": "Element",
        }
    )
    cancel_penalty: Optional[TypeFarePenalty] = field(
        default=None,
        metadata={
            "name": "CancelPenalty",
            "type": "Element",
        }
    )
    fare_rules_filter: Optional[FareRulesFilter] = field(
        default=None,
        metadata={
            "name": "FareRulesFilter",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
        }
    )
    passenger_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 5,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    effective_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
        }
    )
    travel_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Attribute",
        }
    )
    departure_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    private_fare: Optional[TypePrivateFare] = field(
        default=None,
        metadata={
            "name": "PrivateFare",
            "type": "Attribute",
        }
    )
    negotiated_fare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NegotiatedFare",
            "type": "Attribute",
        }
    )
    tour_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    waiver_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Attribute",
        }
    )
    not_valid_before: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        }
    )
    not_valid_after: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    fare_family: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareFamily",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 32,
        }
    )
    promotional_fare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PromotionalFare",
            "type": "Attribute",
        }
    )
    car_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    value_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValueCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    bulk_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        }
    )
    inclusive_tour: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InclusiveTour",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    tax_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxAmount",
            "type": "Attribute",
        }
    )


@dataclass
class FlightDetailsReq(BaseReq):
    """
    Request for the Flight Details of segments.

    Parameters
    ----------
    air_segment: Provider: 1G,1V,1P,1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class FlightDetailsRsp(BaseRsp):
    """
    Parameters
    ----------
    air_segment: Provider: 1G,1V,1P,1J.
    co2_emissions:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    co2_emissions: List[Co2Emissions] = field(
        default_factory=list,
        metadata={
            "name": "CO2Emissions",
            "type": "Element",
            "max_occurs": 99,
        }
    )


@dataclass
class JourneyData:
    """
    Performs journey aware air availability.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        }
    )


@dataclass
class SeatMapReq(BaseReq):
    """
    Request a seat map for the give flight information.

    Parameters
    ----------
    agency_sell_info: Provider: ACH-Required if the user requesting the
        seat map is not the same agent authenticated in the request.
    air_segment: Provider: 1G,1V,1P,1J,ACH,MCH.
    host_token: Provider: ACH-Required if the carrier has multiple
        adapters.
    search_traveler: Provider: 1G,1V,ACH,MCH.
    host_reservation: Provider: ACH,MCH-Required when seat price is
        requested.
    merchandising_pricing_modifiers: Used to provide additional pricing
        options. Provider:ACH.
    return_seat_pricing: Provider: 1G,1V,1P,1J,ACH-When set to true the
        price of the seat will be returned if it exists.
    return_branding_info: A value of true will return the BrandingInfo
        block in the response if applicable. A value of false will not
        return the BrandingInfo block in the response. Providers: 1G,
        1V, 1P, 1J, ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    agency_sell_info: Optional[AgencySellInfo] = field(
        default=None,
        metadata={
            "name": "AgencySellInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 99,
        }
    )
    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "name": "SearchTraveler",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_reservation: Optional[HostReservation] = field(
        default=None,
        metadata={
            "name": "HostReservation",
            "type": "Element",
        }
    )
    merchandising_pricing_modifiers: Optional[MerchandisingPricingModifiers] = field(
        default=None,
        metadata={
            "name": "MerchandisingPricingModifiers",
            "type": "Element",
        }
    )
    return_seat_pricing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnSeatPricing",
            "type": "Attribute",
            "required": True,
        }
    )
    return_branding_info: bool = field(
        default=False,
        metadata={
            "name": "ReturnBrandingInfo",
            "type": "Attribute",
        }
    )


@dataclass
class SeatMapRsp(BaseRsp):
    """
    Parameters
    ----------
    host_token: Provider: ACH,MCH.
    cabin_class: Provider: 1G,1V,1P,1J,ACH,MCH.
    air_segment: Provider: ACH,MCH.
    search_traveler: Provider: ACH,MCH.
    optional_services: A wrapper for all the information regarding each
        of the Optional Services. Provider: 1G,1V,1P,1J,ACH.
    remark: Provider: 1G,1V,1P,1J,ACH,MCH.
    rows:
    payment_restriction: Provider: MCH-Information regarding valid
        payment types, if restrictions apply(supplier specific)
    seat_information:
    copyright: Copyright text applicable for some seat content.
        Providers: 1G, 1V, 1P, 1J,ACH
    group_seat_price: Provider: 1G,1V-Seat price for the all passengers
        traveling together only when supplier provides group flat fee.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 99,
        }
    )
    cabin_class: Optional[CabinClass] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "name": "SearchTraveler",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    remark: Optional[Remark] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    rows: List[Rows] = field(
        default_factory=list,
        metadata={
            "name": "Rows",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    payment_restriction: List[PaymentRestriction] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    seat_information: List[SeatInformation] = field(
        default_factory=list,
        metadata={
            "name": "SeatInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    copyright: Optional[str] = field(
        default=None,
        metadata={
            "name": "Copyright",
            "type": "Element",
        }
    )
    group_seat_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "GroupSeatPrice",
            "type": "Attribute",
        }
    )


@dataclass
class TcrrefundBundle:
    """
    Bundle refund, pricing, and penalty information for a TCR reservation Used
    both in request and response.

    Parameters
    ----------
    air_refund_info:
    waiver_code:
    air_segment:
    fee_info:
    tax_info: Itinerary level taxes
    host_token:
    tcrnumber: The identifying number for a Ticketless Air Reservation.
    refund_type: Specifies whether this bundle was auto or manually
        generated
    refund_access_code:
    """
    class Meta:
        name = "TCRRefundBundle"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_refund_info: Optional[AirRefundInfo] = field(
        default=None,
        metadata={
            "name": "AirRefundInfo",
            "type": "Element",
            "required": True,
        }
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "TCRNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    refund_type: Optional[TcrrefundBundleRefundType] = field(
        default=None,
        metadata={
            "name": "RefundType",
            "type": "Attribute",
            "required": True,
        }
    )
    refund_access_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundAccessCode",
            "type": "Attribute",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "min_length": 1,
            "max_length": 32,
        }
    )


@dataclass
class AirExchangeMultiQuoteOption:
    """
    The shared object list of AirExchangeMultiQuoteOptions.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_data: List[AirSegmentData] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
        }
    )
    air_exchange_bundle_list: List[AirExchangeBundleList] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundleList",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirMerchandisingOfferAvailabilityReq(BaseReq):
    """
    Check with the supplier whether or not the reservation or air solution
    supports any merchandising offerings.

    Parameters
    ----------
    agency_sell_info: Provider: 1G,1V,1P,1J,ACH.
    air_solution: Provider: 1G,1V,1P,1J,ACH.
    host_reservation: Provider: 1G,1V,1P,1J,ACH.
    offer_availability_modifiers: Provider: 1G,1V,1P,1J,ACH.
    merchandising_pricing_modifiers: Used to provide additional pricing
        modifiers. Provider:ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    agency_sell_info: Optional[AgencySellInfo] = field(
        default=None,
        metadata={
            "name": "AgencySellInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    air_solution: Optional[AirSolution] = field(
        default=None,
        metadata={
            "name": "AirSolution",
            "type": "Element",
        }
    )
    host_reservation: List[HostReservation] = field(
        default_factory=list,
        metadata={
            "name": "HostReservation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    offer_availability_modifiers: List[OfferAvailabilityModifiers] = field(
        default_factory=list,
        metadata={
            "name": "OfferAvailabilityModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    merchandising_pricing_modifiers: Optional[MerchandisingPricingModifiers] = field(
        default=None,
        metadata={
            "name": "MerchandisingPricingModifiers",
            "type": "Element",
        }
    )


@dataclass
class AirMerchandisingOfferAvailabilityRsp(BaseRsp):
    """
    Contains the merchandising offerings for the given passenger and itinerary.

    Parameters
    ----------
    air_solution: Provider: 1G,1V,1P,1J,ACH.
    remark: Provider: 1G,1V,1P,1J,ACH.
    optional_services:
    embargo_list:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_solution: Optional[AirSolution] = field(
        default=None,
        metadata={
            "name": "AirSolution",
            "type": "Element",
            "required": True,
        }
    )
    remark: Optional[Remark] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    embargo_list: Optional[EmbargoList] = field(
        default=None,
        metadata={
            "name": "EmbargoList",
            "type": "Element",
        }
    )


@dataclass
class AirPricingInfo:
    """Per traveler type pricing breakdown.

    This will reflect the pricing for all travelers of the specified
    type.

    Parameters
    ----------
    fare_info:
    fare_status:
    fare_info_ref:
    booking_info:
    tax_info:
    fare_calc:
    passenger_type:
    booking_traveler_ref:
    waiver_code:
    payment_ref: The reference to the Payment if Air Pricing is charged
    change_penalty: The penalty (if any) to change the itinerary
    cancel_penalty: The penalty (if any) to cancel the fare
    no_show_penalty: The NoShow penalty (if any)
    fee_info:
    adjustment:
    yield_value:
    air_pricing_modifiers:
    ticketing_modifiers_ref:
    air_segment_pricing_modifiers:
    flight_options_list:
    baggage_allowances:
    fare_rules_filter:
    policy_codes_list: A list of codes that indicate why an item was
        determined to be ‘out of policy’
    price_change: Indicates a price change is found in Fare Control
        Manager
    action_details:
    commission: Allows an agency to update the commission to a new or
        different commission rate which will be applied at time of
        ticketing. The commission Modifier allows the user specify how
        the commission change is to applied
    origin: The IATA location code for this origination of this entity.
    destination: The IATA location code for this destination of this
        entity.
    key:
    command_key: The command identifier used when this is in response to
        an AirPricingCommand. Not used in any request processing.
    total_price: The total price for this entity including base price
        and all taxes.
    base_price: Represents the base price for this entity. This does not
        include any taxes or surcharges.
    approximate_total_price: The Converted total price in Default
        Currency for this entity including base price and all taxes.
    approximate_base_price: The Converted base price in Default Currency
        for this entity. This does not include any taxes or surcharges.
    equivalent_base_price: Represents the base price in the related
        currency for this entity. This does not include any taxes or
        surcharges.
    taxes: The aggregated amount of all the taxes that are associated
        with this entity. See the associated TaxInfo array for a
        breakdown of the individual taxes.
    fees: The aggregated amount of all the fees that are associated with
        this entity. See the associated FeeInfo array for a breakdown of
        the individual fees.
    services: The total cost for all optional services.
    approximate_taxes: The Converted tax amount in Default Currency.
    approximate_fees: The Converted fee amount in Default Currency.
    provider_code:
    supplier_code:
    amount_type: This field displays type of payment amount when it is
        non-monetary. Presently available/supported value is "Flight
        Pass Credits".
    includes_vat: Indicates whether the Base Price includes VAT.
    exchange_amount: The amount to pay to cover the exchange of the fare
        (includes penalties).
    forfeit_amount: The amount forfeited when the fare is exchanged.
    refundable: Indicates whether the fare is refundable
    exchangeable: Indicates whether the fare is exchangeable
    latest_ticketing_time: The latest date/time at which this pricing
        information is valid
    pricing_method:
    checksum: A security value used to guarantee that the pricing data
        sent in matches the pricing data previously returned
    eticketability: The E-Ticketability of this AirPricing
    plating_carrier: The Plating Carrier for this journey
    provider_reservation_info_ref: Provider reservation reference key.
    air_pricing_info_group: This attribute is added to support multiple
        store fare in Host. All AirPricingInfo with same group number
        will be stored together.
    total_net_price: The total price of a negotiated fare.
    ticketed: Indicates if the associated stored fare is ticketed or
        not.
    pricing_type: Indicates the Pricing Type used. The possible values
        are TicketRecord, StoredFare, PricingInstruction.
    true_last_date_to_ticket: This date indicates the true last
        date/time to ticket for the fare. This date comes from the filed
        fare . There is no guarantee the fare will still be available on
        that date or that the fare amount may change. It is merely the
        last date to purchase a ticket based on the carriers fare rules
        at the time the itinerary was quoted and stored
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    in_policy: This attribute will be used to indicate if a fare or rate
        has been determined to be ‘in policy’ based on the associated
        policy settings.
    preferred_option: This attribute is used to indicate if the vendors
        responsible for the fare or rate being returned have been
        determined to be ‘preferred’ based on the associated policy
        settings.
    fare_calculation_ind: Fare calculation that was used to price the
        itinerary.
    cat35_indicator: A true value indicates that the fare has a Cat35
        rule. A false valud indicates that the fare does not have a
        Cat35 rule
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_info: List[FareInfo] = field(
        default_factory=list,
        metadata={
            "name": "FareInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_status: Optional[FareStatus] = field(
        default=None,
        metadata={
            "name": "FareStatus",
            "type": "Element",
        }
    )
    fare_info_ref: List[FareInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "FareInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    booking_info: List[BookingInfo] = field(
        default_factory=list,
        metadata={
            "name": "BookingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_calc: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareCalc",
            "type": "Element",
        }
    )
    passenger_type: List[PassengerType] = field(
        default_factory=list,
        metadata={
            "name": "PassengerType",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )
    payment_ref: List[PaymentRef] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    change_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata={
            "name": "ChangePenalty",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    cancel_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata={
            "name": "CancelPenalty",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    no_show_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata={
            "name": "NoShowPenalty",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    adjustment: List[Adjustment] = field(
        default_factory=list,
        metadata={
            "name": "Adjustment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    yield_value: List[Yield] = field(
        default_factory=list,
        metadata={
            "name": "Yield",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
        }
    )
    ticketing_modifiers_ref: List[TicketingModifiersRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    flight_options_list: Optional[FlightOptionsList] = field(
        default=None,
        metadata={
            "name": "FlightOptionsList",
            "type": "Element",
        }
    )
    baggage_allowances: Optional[BaggageAllowances] = field(
        default=None,
        metadata={
            "name": "BaggageAllowances",
            "type": "Element",
        }
    )
    fare_rules_filter: Optional[FareRulesFilter] = field(
        default=None,
        metadata={
            "name": "FareRulesFilter",
            "type": "Element",
        }
    )
    policy_codes_list: Optional[PolicyCodesList] = field(
        default=None,
        metadata={
            "name": "PolicyCodesList",
            "type": "Element",
        }
    )
    price_change: List[PriceChangeType] = field(
        default_factory=list,
        metadata={
            "name": "PriceChange",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    action_details: Optional[ActionDetails] = field(
        default=None,
        metadata={
            "name": "ActionDetails",
            "type": "Element",
        }
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    command_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommandKey",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: Optional[str] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    amount_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AmountType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    includes_vat: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludesVAT",
            "type": "Attribute",
        }
    )
    exchange_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
        }
    )
    forfeit_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForfeitAmount",
            "type": "Attribute",
        }
    )
    refundable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
        }
    )
    exchangeable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exchangeable",
            "type": "Attribute",
        }
    )
    latest_ticketing_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "LatestTicketingTime",
            "type": "Attribute",
        }
    )
    pricing_method: Optional[TypePricingMethod] = field(
        default=None,
        metadata={
            "name": "PricingMethod",
            "type": "Attribute",
            "required": True,
        }
    )
    checksum: Optional[str] = field(
        default=None,
        metadata={
            "name": "Checksum",
            "type": "Attribute",
        }
    )
    eticketability: Optional[TypeEticketability] = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    air_pricing_info_group: Optional[int] = field(
        default=None,
        metadata={
            "name": "AirPricingInfoGroup",
            "type": "Attribute",
        }
    )
    total_net_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNetPrice",
            "type": "Attribute",
        }
    )
    ticketed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ticketed",
            "type": "Attribute",
        }
    )
    pricing_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    true_last_date_to_ticket: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrueLastDateToTicket",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    in_policy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InPolicy",
            "type": "Attribute",
        }
    )
    preferred_option: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        }
    )
    fare_calculation_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareCalculationInd",
            "type": "Attribute",
            "length": 1,
        }
    )
    cat35_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cat35Indicator",
            "type": "Attribute",
        }
    )


@dataclass
class AirRefundQuoteRsp(BaseRsp):
    """
    Parameters
    ----------
    air_refund_bundle:
    tcrrefund_bundle: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_refund_bundle: List[AirRefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tcrrefund_bundle: List[TcrrefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "TCRRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirRefundReq(BaseReq):
    """
    Request to refund an itinerary for the amount previously quoted.

    Parameters
    ----------
    air_refund_bundle: Provider: ACH.
    tcrrefund_bundle: Provider: ACH.
    air_refund_modifiers:
    commission: Provider: ACH.
    form_of_payment: Provider: ACH-Form of Payment for any Additional
        Collection charges for the Refund.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_refund_bundle: List[AirRefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tcrrefund_bundle: List[TcrrefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "TCRRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_refund_modifiers: Optional[AirRefundModifiers] = field(
        default=None,
        metadata={
            "name": "AirRefundModifiers",
            "type": "Element",
        }
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 9,
        }
    )
    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )


@dataclass
class AirSearchReq(BaseSearchReq):
    """
    Base Request for Air Search.
    """
    point_of_commencement: Optional[PointOfCommencement] = field(
        default=None,
        metadata={
            "name": "PointOfCommencement",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    search_air_leg: List[SearchAirLeg] = field(
        default_factory=list,
        metadata={
            "name": "SearchAirLeg",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 16,
        }
    )
    search_specific_air_segment: List[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata={
            "name": "SearchSpecificAirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    air_search_modifiers: Optional[AirSearchModifiers] = field(
        default=None,
        metadata={
            "name": "AirSearchModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    journey_data: Optional[JourneyData] = field(
        default=None,
        metadata={
            "name": "JourneyData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )


@dataclass
class AirSegmentSellFailureInfo:
    """
    Container to return air segment sell failures.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_error: List[AirSegmentError] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentError",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AvailabilityErrorInfo(TypeErrorInfo):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_error: List[AirSegmentError] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentError",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class BaseAirPriceReq(BaseCoreReq):
    """
    Parameters
    ----------
    air_itinerary: Provider: 1G,1V,1P,1J,ACH.
    air_pricing_modifiers: Provider: 1G,1V,1P,1J,ACH.
    search_passenger: Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger
        increased in to 18 to support 9 INF passenger along with 9
        ADT,CHD,INS                                      passenger
    air_pricing_command: Provider: 1G,1V,1P,1J,ACH.
    air_reservation_locator_code: Provider: ACH,1P,1J
    optional_services: Provider: ACH.
    form_of_payment: Provider: 1G,1V,1P,1J,ACH.
    pcc:
    ssr: Special Service Request for GST tax details. Provider: ACH
    check_obfees: A flag to return fees for ticketing and for various
        forms of payment. The default is “TicketingOnly” and will return
        only ticketing fees.  The value “All” will return ticketing fees
        and the applicable form of payment fees for the form of payment
        information specified in the request.  “FOPOnly” will return the
        applicable form of payment fees for the form of payment
        information specified in the request. Form of payment fees are
        never included in the total unless specific card details are in
        the request.Provider notes:ACH - CheckOBFees is valid only for
        LowFareSearch.  The valid values are “All”, “TicketingOnly” and
        “None” and the default value is “None”. 1P/1J -The valid values
        are “All”, “None” and “TicketingOnly”.1G – All four values are
        supported.1V/RCH – CheckOBFees are not supported.”
    fare_rule_type: Provider: 1G,1V,1P,1J,ACH.
    supplier_code: Specifies the supplier/ vendor for vendor specific
        price requests
    ticket_date: YYYY-MM-DD Using a date in the past is a request for an
        historical fare
    check_flight_details: To Include FlightDetails in Response set to
        “true” the Default value is “false”.
    return_mm: If this attribute is set to “true”, Fare Control Manager
        processing will be invoked.
    nscc: 1 to 3 numeric that defines a Search Control Console
        filter.This attribute is used to override that filter.
    split_pricing: Indicates whether the AirSegments should be priced
        together or separately. Set ‘true’ for split pricing. Set
        ‘false’ for pricing together.SplitPricing is not supported with
        post book re-pricing.
    ignore_availability: Provides a method of pricing a book itinerary
        with the lowest fare regardless of the availability for the
        class of service. Only for providers 1P/1J.
    """
    air_itinerary: Optional[AirItinerary] = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "required": True,
        }
    )
    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 18,
        }
    )
    air_pricing_command: List[AirPricingCommand] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingCommand",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "min_occurs": 1,
            "max_occurs": 16,
        }
    )
    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "min_length": 5,
            "max_length": 8,
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    pcc: Optional[Pcc] = field(
        default=None,
        metadata={
            "name": "PCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 99,
        }
    )
    check_obfees: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckOBFees",
            "type": "Attribute",
        }
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    ticket_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TicketDate",
            "type": "Attribute",
        }
    )
    check_flight_details: bool = field(
        default=False,
        metadata={
            "name": "CheckFlightDetails",
            "type": "Attribute",
        }
    )
    return_mm: bool = field(
        default=False,
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
        }
    )
    nscc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        }
    )
    split_pricing: bool = field(
        default=False,
        metadata={
            "name": "SplitPricing",
            "type": "Attribute",
        }
    )
    ignore_availability: bool = field(
        default=False,
        metadata={
            "name": "IgnoreAvailability",
            "type": "Attribute",
        }
    )


@dataclass
class BaseAirSearchReq(BaseCoreSearchReq):
    """
    Base Request for Low fare air Search.
    """
    search_air_leg: List[SearchAirLeg] = field(
        default_factory=list,
        metadata={
            "name": "SearchAirLeg",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 9,
        }
    )
    search_specific_air_segment: List[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata={
            "name": "SearchSpecificAirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    air_search_modifiers: Optional[AirSearchModifiers] = field(
        default=None,
        metadata={
            "name": "AirSearchModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    split_ticketing_search: Optional[SplitTicketingSearch] = field(
        default=None,
        metadata={
            "name": "SplitTicketingSearch",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    journey_data: Optional[JourneyData] = field(
        default=None,
        metadata={
            "name": "JourneyData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )


@dataclass
class FareInfoList:
    """
    The shared object list of FareInfos.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_info: List[FareInfo] = field(
        default_factory=list,
        metadata={
            "name": "FareInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeMulitQuoteList:
    """
    The shared object list of AirExchangeMultiQuotes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_exchange_multi_quote_option: List[AirExchangeMultiQuoteOption] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeMultiQuoteOption",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AirPricePoint:
    """
    The container which holds the Non Solutioned result.

    Parameters
    ----------
    air_pricing_info:
    air_pricing_result_message:
    fee_info: Supported by ACH only
    fare_note:
    tax_info: Itinerary level taxes
    key:
    total_price: The total price for this entity including base price
        and all taxes.
    base_price: Represents the base price for this entity. This does not
        include any taxes or surcharges.
    approximate_total_price: The Converted total price in Default
        Currency for this entity including base price and all taxes.
    approximate_base_price: The Converted base price in Default Currency
        for this entity. This does not include any taxes or surcharges.
    equivalent_base_price: Represents the base price in the related
        currency for this entity. This does not include any taxes or
        surcharges.
    taxes: The aggregated amount of all the taxes that are associated
        with this entity. See the associated TaxInfo array for a
        breakdown of the individual taxes.
    fees: The aggregated amount of all the fees that are associated with
        this entity. See the associated FeeInfo array for a breakdown of
        the individual fees.
    services: The total cost for all optional services.
    approximate_taxes: The Converted tax amount in Default Currency.
    approximate_fees: The Converted fee amount in Default Currency.
    complete_itinerary: This attribute is used to return whether
        complete Itinerary is present in the AirPricePoint structure or
        not. If set to true means AirPricePoint contains the result for
        full requested itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingResultMessage",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata={
            "name": "FareNote",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: Optional[str] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    complete_itinerary: bool = field(
        default=True,
        metadata={
            "name": "CompleteItinerary",
            "type": "Attribute",
        }
    )


@dataclass
class AirPriceReq(BaseAirPriceReq):
    """Request to price an itinerary in one to many ways.

    Pricing commands can be specified globally, or specifically per
    command.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AirPricingInfoList:
    """
    The shared object list of AirSegments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirPricingSolution:
    """
    The pricing container for an air travel itinerary.

    Parameters
    ----------
    air_segment:
    air_segment_ref:
    journey:
    leg_ref:
    air_pricing_info:
    fare_note:
    fare_note_ref:
    connection:
    meta_data:
    air_pricing_result_message:
    fee_info:
    tax_info: Itinerary level taxes
    air_itinerary_solution_ref:
    host_token:
    optional_services:
    available_ssr:
    pricing_details:
    key:
    complete_itinerary: This attribute is used to return whether
        complete Itinerary is present in the AirPricingSolution
        structure or not. If set to true means AirPricingSolution
        contains the result for full requested itinerary.
    quote_date: This date will be equal to the date of the transaction
        unless the request included a modified ticket date.
    total_price: The total price for this entity including base price
        and all taxes.
    base_price: Represents the base price for this entity. This does not
        include any taxes or surcharges.
    approximate_total_price: The Converted total price in Default
        Currency for this entity including base price and all taxes.
    approximate_base_price: The Converted base price in Default Currency
        for this entity. This does not include any taxes or surcharges.
    equivalent_base_price: Represents the base price in the related
        currency for this entity. This does not include any taxes or
        surcharges.
    taxes: The aggregated amount of all the taxes that are associated
        with this entity. See the associated TaxInfo array for a
        breakdown of the individual taxes.
    fees: The aggregated amount of all the fees that are associated with
        this entity. See the associated FeeInfo array for a breakdown of
        the individual fees.
    services: The total cost for all optional services.
    approximate_taxes: The Converted tax amount in Default Currency.
    approximate_fees: The Converted fee amount in Default Currency.
    itinerary: For an exchange request this tells if the itinerary is
        the original one or new one. A value of Original will only apply
        to 1G/1V/1P/1S/1A. A value of New will apply to
        1G/1V/1P/1S/1A/ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    journey: List[Journey] = field(
        default_factory=list,
        metadata={
            "name": "Journey",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    leg_ref: List[LegRef] = field(
        default_factory=list,
        metadata={
            "name": "LegRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata={
            "name": "FareNote",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_note_ref: List[FareNoteRef] = field(
        default_factory=list,
        metadata={
            "name": "FareNoteRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    meta_data: List[MetaData] = field(
        default_factory=list,
        metadata={
            "name": "MetaData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    air_pricing_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingResultMessage",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_itinerary_solution_ref: List[AirItinerarySolutionRef] = field(
        default_factory=list,
        metadata={
            "name": "AirItinerarySolutionRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    available_ssr: Optional[AvailableSsr] = field(
        default=None,
        metadata={
            "name": "AvailableSSR",
            "type": "Element",
        }
    )
    pricing_details: Optional[PricingDetails] = field(
        default=None,
        metadata={
            "name": "PricingDetails",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    complete_itinerary: bool = field(
        default=True,
        metadata={
            "name": "CompleteItinerary",
            "type": "Attribute",
        }
    )
    quote_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "QuoteDate",
            "type": "Attribute",
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: Optional[str] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    itinerary: Optional[AirPricingSolutionItinerary] = field(
        default=None,
        metadata={
            "name": "Itinerary",
            "type": "Attribute",
        }
    )


@dataclass
class AvailabilitySearchReq(AirSearchReq):
    """
    Availability Search request.

    Parameters
    ----------
    search_passenger: Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger
        increased in to 18 to support 9 INF passenger along with 9
        ADT,CHD,INS
        passenger
    point_of_sale: Provider: ACH.
    return_brand_indicator: When set to “true”, the Brand Indicator can
        be returned in the availability search response. Provider: 1G,
        1V, 1P, 1J, ACH
    channel_id: A Channel ID is 4 alpha-numeric characters used to
        activate the Search Control Console filter for a specific group
        of travelers being served by the agency credential.
    nscc: Allows the agency to bypass/override the Search Control
        Console rule.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 18,
        }
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 5,
        }
    )
    return_brand_indicator: bool = field(
        default=False,
        metadata={
            "name": "ReturnBrandIndicator",
            "type": "Attribute",
        }
    )
    channel_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 4,
        }
    )
    nscc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        }
    )


@dataclass
class BaseAvailabilitySearchRsp(BaseSearchRsp):
    """
    Availability Search response.
    """
    flight_details_list: Optional[FlightDetailsList] = field(
        default=None,
        metadata={
            "name": "FlightDetailsList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    air_segment_list: Optional[AirSegmentList] = field(
        default=None,
        metadata={
            "name": "AirSegmentList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    fare_info_list: Optional[FareInfoList] = field(
        default=None,
        metadata={
            "name": "FareInfoList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    fare_remark_list: Optional[FareRemarkList] = field(
        default=None,
        metadata={
            "name": "FareRemarkList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    air_itinerary_solution: List[AirItinerarySolution] = field(
        default_factory=list,
        metadata={
            "name": "AirItinerarySolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    host_token_list: Optional[HostTokenList] = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    apisrequirements_list: Optional[ApisrequirementsList] = field(
        default=None,
        metadata={
            "name": "APISRequirementsList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    distance_units: Optional[TypeDistance] = field(
        default=None,
        metadata={
            "name": "DistanceUnits",
            "type": "Attribute",
        }
    )


@dataclass
class BaseLowFareSearchReq(BaseAirSearchReq):
    """
    Base Low Fare Search Request.

    Parameters
    ----------
    search_passenger: Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger
        increased in to 18 to support 9 INF passenger along with 9
        ADT,CHD,INS                                      passenger
    air_pricing_modifiers: Provider: 1G,1V,1P,1J,ACH.
    enumeration: Provider: 1G,1V,1P,1J,ACH.
    air_exchange_modifiers: Provider: ACH.
    flex_explore_modifiers: This is the container for a set of modifiers
        which allow the user to perform a special kind of low fare
        search, depicted as flex explore, based on different parameters
        like Area, Zone, Country, State, Specific locations, Distance
        around the actual destination of the itinerary. Applicable for
        providers 1G,1V,1P.
    pcc:
    fare_rules_filter_category:
    form_of_payment: Provider: 1P,1J
    enable_point_to_point_search: Provider: 1G,1V,1P,1J,ACH-Indicates
        that low cost providers should be queried for top connection
        options and the results returned with the search.
    enable_point_to_point_alternates: Provider: 1G,1V,1P,1J,ACH-
        Indicates that suggestions for alternate connection cities for
        low cost providers should be returned with the search.
    max_number_of_expert_solutions: Provider: 1G,1V,1P,1J,ACH-Indicates
        the Maximum Number of Expert Solutions to be returned from the
        Knowledge Base for the provided search criteria
    solution_result: Provider: 1G,1V,1P,1J,ACH-Indicates whether the
        response will contain Solution result (AirPricingSolution) or
        Non Solution Result (AirPricingPoints). The default value is
        false. This attribute cannot be combined with
        EnablePointToPointSearch, EnablePointToPointAlternates and
        MaxNumberOfExpertSolutions.
    prefer_complete_itinerary: Provider: ACH-This attribute is only
        supported for ACH .It works in conjunction with the
        @SolutionResult flag
    meta_option_identifier: Invoke Meta Search.  Valid values are 00 to
        99, or D for the default meta search configuration.  When Meta
        Search not requested, normal LowFareSearch applies.  Supported
        Providers;  1g/1v/1p/1j
    return_upsell_fare: When set to “true”, Upsell information will be
        returned in the shop response. Provider supported : 1G, 1V, 1P,
        1J
    include_fare_info_messages: Set to True to return
        FareInfoMessageList. Providers supported: 1G/1V/1P/1J
    return_branded_fares: When ReturnBrandedFares is set to “false”,
        Rich Content and Branding will not be returned in the shop
        response.  When ReturnBrandedFares it is set to “true” or is not
        sent, Rich Content and Branding will be returned in the shop
        response.  Provider: 1P/1J/ACH.
    multi_gdssearch: A "true" value indicates MultiGDSSearch. Specific
        provisioning is required.
    return_mm: If this attribute is set to “true”, Fare Control Manager
        processing will be invoked.
    check_obfees: A flag to return fees for ticketing and for various
        forms of payment. The default is “TicketingOnly” and will return
        only ticketing fees.  The value “All” will return ticketing fees
        and the applicable form of payment fees for the form of payment
        information specified in the request.  “FOPOnly” will return the
        applicable form of payment fees for the form of payment
        information specified in the request. Form of payment fees are
        never included in the total unless specific card details are in
        the request.Provider notes:ACH - CheckOBFees is valid only for
        LowFareSearch.  The valid values are “All”, “TicketingOnly” and
        “None” and the default value is “None”. 1P/1J -The valid values
        are “All”, “None” and “TicketingOnly”.1G – All four values are
        supported.1V/RCH – CheckOBFees are not supported.”
    nscc: 1 to 3 numeric that defines a Search Control Console
        filter.This attribute is used to override that filter.
    fare_info_rules: Returns ChangePenalty and CancelPenalty values at
        the FareInfo level. If FareRulesFilterCategory is sent
        FareRulesFilter will be returned at FareInfo level.  Provider:
        1G/1V.
    """
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 18,
        }
    )
    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    enumeration: Optional[Enumeration] = field(
        default=None,
        metadata={
            "name": "Enumeration",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    air_exchange_modifiers: Optional[AirExchangeModifiers] = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    flex_explore_modifiers: Optional[FlexExploreModifiers] = field(
        default=None,
        metadata={
            "name": "FlexExploreModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    pcc: Optional[Pcc] = field(
        default=None,
        metadata={
            "name": "PCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    fare_rules_filter_category: Optional[FareRulesFilterCategory] = field(
        default=None,
        metadata={
            "name": "FareRulesFilterCategory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 99,
        }
    )
    enable_point_to_point_search: bool = field(
        default=False,
        metadata={
            "name": "EnablePointToPointSearch",
            "type": "Attribute",
        }
    )
    enable_point_to_point_alternates: bool = field(
        default=False,
        metadata={
            "name": "EnablePointToPointAlternates",
            "type": "Attribute",
        }
    )
    max_number_of_expert_solutions: int = field(
        default=0,
        metadata={
            "name": "MaxNumberOfExpertSolutions",
            "type": "Attribute",
        }
    )
    solution_result: bool = field(
        default=False,
        metadata={
            "name": "SolutionResult",
            "type": "Attribute",
        }
    )
    prefer_complete_itinerary: bool = field(
        default=True,
        metadata={
            "name": "PreferCompleteItinerary",
            "type": "Attribute",
        }
    )
    meta_option_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MetaOptionIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    return_upsell_fare: bool = field(
        default=False,
        metadata={
            "name": "ReturnUpsellFare",
            "type": "Attribute",
        }
    )
    include_fare_info_messages: bool = field(
        default=False,
        metadata={
            "name": "IncludeFareInfoMessages",
            "type": "Attribute",
        }
    )
    return_branded_fares: bool = field(
        default=True,
        metadata={
            "name": "ReturnBrandedFares",
            "type": "Attribute",
        }
    )
    multi_gdssearch: bool = field(
        default=False,
        metadata={
            "name": "MultiGDSSearch",
            "type": "Attribute",
        }
    )
    return_mm: bool = field(
        default=False,
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
        }
    )
    check_obfees: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckOBFees",
            "type": "Attribute",
        }
    )
    nscc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        }
    )
    fare_info_rules: bool = field(
        default=False,
        metadata={
            "name": "FareInfoRules",
            "type": "Attribute",
        }
    )


@dataclass
class Etr:
    """
    Result of ticketing request.

    Parameters
    ----------
    air_reservation_locator_code:
    agency_info:
    booking_traveler:
    form_of_payment:
    payment:
    credit_card_auth: This is a container to display detail information
        of credit card auth. Providers supported: Worldspan and JAL.
    supplier_locator:
    fare_calc:
    ticket:
    commission:
    air_pricing_info:
    audit_data:
    restriction:
    waiver_code:
    baggage_allowances: Baggage Allowance Info after Ticketing
    key:
    total_price: The total price for this entity including base price
        and all taxes.
    base_price: Represents the base price for this entity. This does not
        include any taxes or surcharges.
    approximate_total_price: The Converted total price in Default
        Currency for this entity including base price and all taxes.
    approximate_base_price: The Converted base price in Default Currency
        for this entity. This does not include any taxes or surcharges.
    equivalent_base_price: Represents the base price in the related
        currency for this entity. This does not include any taxes or
        surcharges.
    taxes: The aggregated amount of all the taxes that are associated
        with this entity. See the associated TaxInfo array for a
        breakdown of the individual taxes.
    fees: The aggregated amount of all the fees that are associated with
        this entity. See the associated FeeInfo array for a breakdown of
        the individual fees.
    services: The total cost for all optional services.
    approximate_taxes: The Converted tax amount in Default Currency.
    approximate_fees: The Converted fee amount in Default Currency.
    refundable:
    exchangeable:
    tour_code:
    issued_date: Ticket issue date.
    bulk_ticket: Whether the ticket was issued as bulk.
    provider_code: Contains the Provider Code of the provider that
        houses this ETR.
    provider_locator_code: Contains the Locator Code of the Provider
        Reservation that houses this ETR.
    iatanumber: Contains the IATA Number of the agent initiating the
        request.
    pseudo_city_code: Contain Pseudo City, city/office number, branch
        ID, etc.
    country_code: Contains Ticketed PCC’s Country code.
    plating_carrier: Contains the Plating Carrier of this ETR.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "ETR"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    agency_info: Optional[AgencyInfo] = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    booking_traveler: Optional[BookingTraveler] = field(
        default=None,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    fare_calc: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareCalc",
            "type": "Element",
            "required": True,
        }
    )
    ticket: List[Ticket] = field(
        default_factory=list,
        metadata={
            "name": "Ticket",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    air_pricing_info: Optional[AirPricingInfo] = field(
        default=None,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
        }
    )
    audit_data: Optional[AuditData] = field(
        default=None,
        metadata={
            "name": "AuditData",
            "type": "Element",
        }
    )
    restriction: List[CommonRestriction] = field(
        default_factory=list,
        metadata={
            "name": "Restriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )
    baggage_allowances: Optional[BaggageAllowances] = field(
        default=None,
        metadata={
            "name": "BaggageAllowances",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: Optional[str] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    refundable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
        }
    )
    exchangeable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exchangeable",
            "type": "Attribute",
        }
    )
    tour_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    issued_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuedDate",
            "type": "Attribute",
            "required": True,
        }
    )
    bulk_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    iatanumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class ScheduleSearchReq(AirSearchReq):
    """
    Schedule Search request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class Tcr:
    """
    Information related to Ticketless carriers.

    Parameters
    ----------
    form_of_payment:
    payment:
    booking_traveler:
    passenger_ticket_number:
    air_pricing_info:
    agency_info:
    air_reservation_locator_code:
    supplier_locator:
    refund_remark:
    tcrnumber: The identifying number for a Ticketless Air Reservation.
    status: The current status of this TCR. Some status values are not
        applicable by some Airlines.
    modified_date: The date at which the status was changed on this TCR
        due to an action event (itemized from the booleans below).
    confirmed_date: The date at which this TCR was confirmed (not
        created). This mean the payment was approved and processed and
        travel for this TCR is confirmed.
    base_price: The base price of this TCR as a whole as it was when it
        was first booked.
    taxes: The taxes of this TCR as a whole as it was when it was first
        booked.
    fees: The fees of this TCR as a whole as it was when it was first
        booked.
    refundable: Is it possible to perform a Refund for this TCR.
    exchangeable: Is it possible to perform an Exchange for this TCR.
    voidable: Is it possible to perform a Void on this TCR.
    modifiable: Is it possible to modify this TCR (opposed to
        Refund/Exchange/Void).
    provider_code:
    provider_locator_code:
    refund_access_code:
    refund_amount: Total Amount refunded to the customer.
    refund_fee: Charges incurred for processing refund.
    forfeit_amount: Amount forfeited as a result of refund.
    """
    class Meta:
        name = "TCR"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    passenger_ticket_number: List[PassengerTicketNumber] = field(
        default_factory=list,
        metadata={
            "name": "PassengerTicketNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    agency_info: Optional[AgencyInfo] = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    refund_remark: List[RefundRemark] = field(
        default_factory=list,
        metadata={
            "name": "RefundRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "TCRNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    status: Optional[TypeTcrstatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    modified_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        }
    )
    confirmed_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfirmedDate",
            "type": "Attribute",
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
            "required": True,
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
            "required": True,
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
            "required": True,
        }
    )
    refundable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
            "required": True,
        }
    )
    exchangeable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exchangeable",
            "type": "Attribute",
            "required": True,
        }
    )
    voidable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Voidable",
            "type": "Attribute",
            "required": True,
        }
    )
    modifiable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Modifiable",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    refund_access_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundAccessCode",
            "type": "Attribute",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "min_length": 1,
            "max_length": 32,
        }
    )
    refund_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
        }
    )
    refund_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundFee",
            "type": "Attribute",
        }
    )
    forfeit_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForfeitAmount",
            "type": "Attribute",
        }
    )


@dataclass
class TypeBaseAirReservation(BaseReservation):
    """
    Parent Container for Air Reservation.

    Parameters
    ----------
    optional_services:
    supplier_locator:
    third_party_information:
    document_info:
    booking_traveler_ref:
    provider_reservation_info_ref:
    air_segment:
    svc_segment: Service segment added to collect additional fee. 1P
        only
    air_pricing_info:
    payment:
    credit_card_auth:
    fare_note:
    fee_info:
    tax_info: Itinerary level taxes
    ticketing_modifiers:
    associated_remark:
    pocket_itinerary_remark:
    air_exchange_bundle_total:
    air_exchange_bundle: Bundle exchange, pricing, and penalty
        information. Providers ACH/1G/1V/1P
    """
    class Meta:
        name = "typeBaseAirReservation"

    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    third_party_information: List[ThirdPartyInformation] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    document_info: Optional[DocumentInfo] = field(
        default=None,
        metadata={
            "name": "DocumentInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    svc_segment: List[SvcSegment] = field(
        default_factory=list,
        metadata={
            "name": "SvcSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata={
            "name": "FareNote",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    tax_info: List[TypeTaxInfoWithPaymentRef] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    ticketing_modifiers: List[TicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "TicketingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    associated_remark: List[AssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    pocket_itinerary_remark: List[PocketItineraryRemark] = field(
        default_factory=list,
        metadata={
            "name": "PocketItineraryRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeMultiQuoteRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_list: List[AirSegmentList] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentList",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    brand_list: List[BrandList] = field(
        default_factory=list,
        metadata={
            "name": "BrandList",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_exchange_mulit_quote_list: List[AirExchangeMulitQuoteList] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeMulitQuoteList",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeQuoteRsp(BaseRsp):
    """
    Parameters
    ----------
    ticket_number:
    air_pricing_solution: Provider: 1G/1V/1P/1S/1A.
    air_exchange_bundle_total:
    air_exchange_bundle: Bundle exchange, pricing, and penalty
        information. Providers ACH/1G/1V/1P
    host_token: Encrypted data from the host. Required to send the
        HostToken from the AirExchangeQuoteRsp in the AirExchangeReq.
        Providers ACH/1G/1V/1P.
    optional_services: Provider: ACH.
    fare_rule: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 13,
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
        }
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeReq(BaseReq):
    """
    Request to exchange an itinerary.

    Parameters
    ----------
    air_reservation_locator_code: Identifies the PNR locator code.
        Providers ACH/1G/1V/1P
    ticket_number:
    specific_seat_assignment: Identifies the standard seat. Providers
        ACH/1G/1V/1P
    air_pricing_solution: Providers ACH/1G/1V/1P.
    air_exchange_modifiers: Provider: ACH.
    air_exchange_bundle_total: Provider: 1G/1V/1P/1S/1A.
    air_exchange_bundle: Bundle exchange, pricing, and penalty
        information. Providers ACH/1G/1V/1P.
    host_token: Encrypted data from the host. Required to send the
        HostToken from the AirExchangeQuoteRsp in the AirExchangeReq.
        Providers ACH/1G/1V/1P
    optional_services: Provider: ACH.
    form_of_payment: Form of Payment for any additional collection
        charges for the Exchange. For ACH, most carriers will only allow
        refund amounts to the original form of payment. Providers
        ACH/1G/1V/1P
    form_of_payment_ref: Provider: ACH-Universal Record reference to
        Form of Payment for any Additional Collection charges or Refund
        due for the itinerary exchange
    ssrinfo: Providers ACH, 1G, 1V, 1P.
    add_svc: 1P - Add SVC segments to collect additional fee
    return_reservation: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 13,
        }
    )
    specific_seat_assignment: List[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    air_exchange_modifiers: Optional[AirExchangeModifiers] = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
        }
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
        }
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    ssrinfo: List[Ssrinfo] = field(
        default_factory=list,
        metadata={
            "name": "SSRInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    add_svc: Optional[AddSvc] = field(
        default=None,
        metadata={
            "name": "AddSvc",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    return_reservation: bool = field(
        default=False,
        metadata={
            "name": "ReturnReservation",
            "type": "Attribute",
        }
    )


@dataclass
class AirPricePointList:
    """
    Provides the list of AirPricePoint (Non Solutioned Result)

    Parameters
    ----------
    air_price_point: The container which holds the Non Solutioned
        result. Different options for each search leg requested will be
        returned and one option for each search leg can be selected.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_price_point: List[AirPricePoint] = field(
        default_factory=list,
        metadata={
            "name": "AirPricePoint",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirPriceResult:
    """A solution will be returned if one exists.

    Otherwise an error will be present

    Parameters
    ----------
    air_pricing_solution:
    fare_rule:
    air_price_error:
    command_key: The command identifier used when this is in response to
        an AirPricingCommand. Not used in any request processing.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_price_error: Optional[TypeResultMessage] = field(
        default=None,
        metadata={
            "name": "AirPriceError",
            "type": "Element",
        }
    )
    command_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommandKey",
            "type": "Attribute",
            "max_length": 10,
        }
    )


@dataclass
class AirRefundRsp(BaseRsp):
    """
    Parameters
    ----------
    etr: Provider: ACH.
    tcr: Provider: ACH.
    refund_failure_info: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tcr: List[Tcr] = field(
        default_factory=list,
        metadata={
            "name": "TCR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    refund_failure_info: List[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "RefundFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirRepriceReq(AirBaseReq):
    """
    Request to reprice a solution.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
        }
    )
    ignore_availability: bool = field(
        default=False,
        metadata={
            "name": "IgnoreAvailability",
            "type": "Attribute",
        }
    )


@dataclass
class AirRepriceRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirReservation(TypeBaseAirReservation):
    """
    The parent container for all booking data.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AirRetrieveDocumentRsp(BaseRsp):
    """
    Parameters
    ----------
    etr: Provider: 1G,1V,1P,1J.
    mco: Provider: 1G,1V,1P,1J.
    tcr: Provider: 1G,1V,1P,1J.
    document_failure_info: Provider: 1G,1V,1P,1J-Will be optionally
        returned if there are duplicate ticket numbers.
    service_fee_info: Provider: 1G,1V
    universal_record_locator_code: Provider: 1G,1V,1P,1J-Represents a
        valid Universal Record locator code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    mco: List[Mco] = field(
        default_factory=list,
        metadata={
            "name": "MCO",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    tcr: List[Tcr] = field(
        default_factory=list,
        metadata={
            "name": "TCR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    document_failure_info: List[TypeFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "DocumentFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    service_fee_info: List[ServiceFeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 99,
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )


@dataclass
class AirScheduleChangedInfo:
    """
    Returned when the requested schedule does not match the host system
    schedule Contents will be a new AirPricingSolution that contains all the
    new schedule information as well as the pricing information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AirSolutionChangedInfo:
    """If RetainReservation is None, this will contain the new values returned
    from the provider.

    If RetainReservation is Price, Schedule, or Both and there is a
    price/schedule change, this will contain the new values that were
    returned from the provider. If RetainReservation is Price, Schedule,
    or Both and there isn’t a price/schedule change, this element will
    not be returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    reason_code: Optional[AirSolutionChangedInfoReasonCode] = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AirVoidDocumentRsp(BaseRsp):
    """Result of void ticket request.

    Includes ticket number of voided tickets and air segments with
    updated status.

    Parameters
    ----------
    etr: Provider: 1G,1V.
    void_result_info: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    void_result_info: List[VoidResultInfo] = field(
        default_factory=list,
        metadata={
            "name": "VoidResultInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AvailabilitySearchRsp(BaseAvailabilitySearchRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class BaseAirExchangeMultiQuoteReq(BaseCoreReq):
    """
    Parameters
    ----------
    ticket_number:
    provider_reservation_info: Provider: 1P - Represents a valid
        Provider Reservation/PNR whose itinerary is to be exchanged
    air_pricing_solution:
    repricing_modifiers:
    original_itinerary_details:
    override_pcc:
    """
    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 13,
        }
    )
    provider_reservation_info: Optional["BaseAirExchangeMultiQuoteReq.ProviderReservationInfo"] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 2,
        }
    )
    repricing_modifiers: Optional[RepricingModifiers] = field(
        default=None,
        metadata={
            "name": "RepricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    original_itinerary_details: Optional[OriginalItineraryDetails] = field(
        default=None,
        metadata={
            "name": "OriginalItineraryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    override_pcc: Optional[OverridePcc] = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )

    @dataclass
    class ProviderReservationInfo:
        provider_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProviderCode",
                "type": "Attribute",
                "required": True,
                "min_length": 2,
                "max_length": 5,
            }
        )
        provider_locator_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProviderLocatorCode",
                "type": "Attribute",
                "required": True,
                "max_length": 15,
            }
        )


@dataclass
class BaseAirExchangeQuoteReq(BaseCoreReq):
    """
    Parameters
    ----------
    ticket_number:
    provider_reservation_info: Provider: 1G/1V/1P/ACH - Represents a
        valid Provider Reservation/PNR whose itinerary is to be
        exchanged
    air_pricing_solution:
    air_exchange_modifiers: Provider: ACH.
    host_token: Provider: ACH.
    optional_services: Provider: ACH.
    form_of_payment: Provider: ACH-This would allow a user to see the
        fees if they are changing from one Form Of Payment to other .
    repricing_modifiers:
    original_itinerary_details:
    pcc:
    fare_rule_type: Provider: ACH.
    """
    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 13,
        }
    )
    provider_reservation_info: Optional["BaseAirExchangeQuoteReq.ProviderReservationInfo"] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 2,
        }
    )
    air_exchange_modifiers: Optional[AirExchangeModifiers] = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    repricing_modifiers: Optional[RepricingModifiers] = field(
        default=None,
        metadata={
            "name": "RepricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    original_itinerary_details: Optional[OriginalItineraryDetails] = field(
        default=None,
        metadata={
            "name": "OriginalItineraryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    pcc: Optional[Pcc] = field(
        default=None,
        metadata={
            "name": "PCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
        }
    )

    @dataclass
    class ProviderReservationInfo:
        provider_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProviderCode",
                "type": "Attribute",
                "required": True,
                "min_length": 2,
                "max_length": 5,
            }
        )
        provider_locator_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProviderLocatorCode",
                "type": "Attribute",
                "required": True,
                "max_length": 15,
            }
        )


@dataclass
class LowFareSearchAsynchReq(BaseLowFareSearchReq):
    """
    Asynchronous Low Fare Search request.

    Parameters
    ----------
    air_search_asynch_modifiers: Provider: 1G,1V,1P,1J,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_search_asynch_modifiers: Optional[AirSearchAsynchModifiers] = field(
        default=None,
        metadata={
            "name": "AirSearchAsynchModifiers",
            "type": "Element",
        }
    )


@dataclass
class LowFareSearchReq(BaseLowFareSearchReq):
    """
    Low Fare Search request.

    Parameters
    ----------
    policy_reference: This attribute will be used to pass in a value on
        the request which would be used to link to a ‘Policy Group’ in a
        policy engine external to UAPI.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    policy_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )


@dataclass
class OptionalServicesInfo:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    form_of_payment_ref: List[FormOfPaymentRef] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class TypeAirReservationWithFop(TypeBaseAirReservation):
    """
    Air Reservation With Form Of Payment.
    """
    class Meta:
        name = "typeAirReservationWithFOP"

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeMultiQuoteReq(BaseAirExchangeMultiQuoteReq):
    """Request multiple quotes for the exchange of an itinerary.

    1P transactions only

    Parameters
    ----------
    type: Type choices are "Detail" or "Summary"  Default will be
        Summary
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: str = field(
        default="Summary",
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class AirExchangeQuoteReq(BaseAirExchangeQuoteReq):
    """
    Request to quote the exchange of an itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AirExchangeRsp(BaseRsp):
    """
    Parameters
    ----------
    ticket_number:
    booking_traveler: Provider: ACH.
    air_reservation: Provider: ACH.
    exchange_failure_info: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 13,
        }
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    air_reservation: Optional[TypeAirReservationWithFop] = field(
        default=None,
        metadata={
            "name": "AirReservation",
            "type": "Element",
        }
    )
    exchange_failure_info: List[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "ExchangeFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeTicketingRsp(BaseRsp):
    """
    Response to reissue a ticket.

    Parameters
    ----------
    air_solution_changed_info:
    etr: Provider 1G, 1V, 1P.
    ticket_failure_info: Provider 1G, 1V, 1P.
    detailed_billing_information: Providers 1G, 1V, 1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_solution_changed_info: Optional[AirSolutionChangedInfo] = field(
        default=None,
        metadata={
            "name": "AirSolutionChangedInfo",
            "type": "Element",
        }
    )
    etr: Optional[Etr] = field(
        default=None,
        metadata={
            "name": "ETR",
            "type": "Element",
        }
    )
    ticket_failure_info: Optional[TicketFailureInfo] = field(
        default=None,
        metadata={
            "name": "TicketFailureInfo",
            "type": "Element",
        }
    )
    detailed_billing_information: Optional[DetailedBillingInformation] = field(
        default=None,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
        }
    )


@dataclass
class AirSearchRsp(BaseAvailabilitySearchRsp):
    """
    Base Response for Air Search.
    """
    fare_note_list: Optional[FareNoteList] = field(
        default=None,
        metadata={
            "name": "FareNoteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    expert_solution_list: Optional[ExpertSolutionList] = field(
        default=None,
        metadata={
            "name": "ExpertSolutionList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    route_list: Optional[RouteList] = field(
        default=None,
        metadata={
            "name": "RouteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    alternate_route_list: Optional[AlternateRouteList] = field(
        default=None,
        metadata={
            "name": "AlternateRouteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    alternate_location_distance_list: Optional[AlternateLocationDistanceList] = field(
        default=None,
        metadata={
            "name": "AlternateLocationDistanceList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    fare_info_message: List[FareInfoMessage] = field(
        default_factory=list,
        metadata={
            "name": "FareInfoMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 99,
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "max_occurs": 999,
        }
    )
    air_price_point_list: Optional[AirPricePointList] = field(
        default=None,
        metadata={
            "name": "AirPricePointList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
        }
    )
    rail_segment_list: Optional[RailSegmentList] = field(
        default=None,
        metadata={
            "name": "RailSegmentList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v48_0",
        }
    )
    rail_journey_list: Optional[RailJourneyList] = field(
        default=None,
        metadata={
            "name": "RailJourneyList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v48_0",
        }
    )
    rail_fare_note_list: Optional[RailFareNoteList] = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v48_0",
        }
    )
    rail_fare_idlist: Optional[RailFareIdlist] = field(
        default=None,
        metadata={
            "name": "RailFareIDList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v48_0",
        }
    )
    rail_fare_list: Optional[RailFareList] = field(
        default=None,
        metadata={
            "name": "RailFareList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v48_0",
        }
    )
    rail_pricing_solution: List[RailPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class AirTicketingRsp(BaseRsp):
    """
    Response to ticket a previously stored reservation.

    Parameters
    ----------
    air_solution_changed_info:
    etr: Provider: 1G,1V,1P,1J.
    ticket_failure_info: Provider: 1G,1V,1P,1J.
    detailed_billing_information: Provider: 1G,1V,1P,1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_solution_changed_info: Optional[AirSolutionChangedInfo] = field(
        default=None,
        metadata={
            "name": "AirSolutionChangedInfo",
            "type": "Element",
        }
    )
    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ticket_failure_info: List[TicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "TicketFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirUpsellSearchReq(AirBaseReq):
    """
    Request to search for Upsell Offers based on the Itinerary.

    Parameters
    ----------
    air_itinerary: Provider: 1G,1V,1P,1J,ACH-AirItinerary of the pricing
        request.
    air_price_result: Provider: 1G,1V,1P,1J,ACH-Result of AirPrice
        request. Upsell uses this to search for new offer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_itinerary: Optional[AirItinerary] = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "required": True,
        }
    )
    air_price_result: List[AirPriceResult] = field(
        default_factory=list,
        metadata={
            "name": "AirPriceResult",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 16,
        }
    )


@dataclass
class BaseAirPriceRsp(BaseRsp):
    """
    Parameters
    ----------
    air_itinerary: Provider: 1G,1V,1P,1J,ACH.
    air_price_result: Provider: 1G,1V,1P,1J,ACH.
    """
    air_itinerary: Optional[AirItinerary] = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "required": True,
        }
    )
    air_price_result: List[AirPriceResult] = field(
        default_factory=list,
        metadata={
            "name": "AirPriceResult",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v48_0",
            "min_occurs": 1,
            "max_occurs": 16,
        }
    )


@dataclass
class AirPriceRsp(BaseAirPriceRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AirUpsellSearchRsp(BaseAirPriceRsp):
    """
    Response of Upsell Offers search for the given Itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class LowFareSearchAsynchRsp(AirSearchRsp):
    """
    Asynchronous Low Fare Search Response contains only the 1st Provider
    response unless time out occurs.

    Parameters
    ----------
    async_provider_specific_response: Provider: 1G,1V,1P,1J,ACH-
        Identifies pending responses from a specific provider using
        MoreResults attribute
    brand_list:
    search_id: Provider: 1G,1V,1P,1J,ACH-Indicates the Search Id of the
        LFS search
    currency_type: Provider: 1G,1V,1P,1J,ACH-Specifies the default
        Currency Type in the response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    async_provider_specific_response: List[AsyncProviderSpecificResponse] = field(
        default_factory=list,
        metadata={
            "name": "AsyncProviderSpecificResponse",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    brand_list: Optional[BrandList] = field(
        default=None,
        metadata={
            "name": "BrandList",
            "type": "Element",
        }
    )
    search_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SearchId",
            "type": "Attribute",
            "required": True,
        }
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        }
    )


@dataclass
class LowFareSearchRsp(AirSearchRsp):
    """
    Low Fare Search Response.

    Parameters
    ----------
    brand_list:
    currency_type: Provider: 1G,1V,1P,1J,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    brand_list: Optional[BrandList] = field(
        default=None,
        metadata={
            "name": "BrandList",
            "type": "Element",
        }
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
    )


@dataclass
class RetrieveLowFareSearchRsp(AirSearchRsp):
    """
    Low Fare Search Asynchronous Result response.

    Parameters
    ----------
    async_provider_specific_response: Provider: 1G,1V,1P,1J,ACH-
        Identifies pending responses from a specific provider using
        MoreResults attribute
    brand_list:
    currency_type: Provider: 1G,1V,1P,1J,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    async_provider_specific_response: List[AsyncProviderSpecificResponse] = field(
        default_factory=list,
        metadata={
            "name": "AsyncProviderSpecificResponse",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    brand_list: Optional[BrandList] = field(
        default=None,
        metadata={
            "name": "BrandList",
            "type": "Element",
        }
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        }
    )


@dataclass
class ScheduleSearchRsp(AirSearchRsp):
    """
    Schedule Search response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"
