from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
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
    SellMessage,
    ServiceData,
    ServiceFeeInfo,
    ServiceInfo,
    ServiceRuleType,
    SupplierLocator,
    ThirdPartyInformation,
    TicketNumber,
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
    :ivar adv_rsvn_only_if_tk: Reservation only if ticketed. True is advanced reservations only if tickets. False is no advanced reservations
    :ivar adv_rsvn_any_tm: Reservation anytime. True if advanced reservatiosn anytime. False if advanced reservations for a limited time.
    :ivar adv_rsvn_hrs: Reservation hours. True if advanced reservation time in hours. False if advanced reservation time not in hours.
    :ivar adv_rsvn_days: Reservation days. True if advanced reservation time in days. False if advanced reservation time not in days.
    :ivar adv_rsvn_months: Reservation months. True if advanced reservation time in months. False if advanced reservation time not in months.
    :ivar adv_rsvn_earliest_tm: Earliest reservation time. True if advanced reservations time is earliest permitted. False is advanced reservation time not earliest permitted time.
    :ivar adv_rsvn_latest_tm: Latest reservation time. True if advanced reservations time is latest permitted. False is advanced reservation time not latest permitted time.
    :ivar adv_rsvn_waived: Reservation Waived. True if advanced reservation waived. False if advanced reservation not waived.
    :ivar adv_rsvn_data_exists: Reservation data exists. True if advanced reservation data exists. False if advanced reservation data does not exist.
    :ivar adv_rsvn_end_item: Reservation end item. True if advanced reservation end item and more values. False if it does not exist.
    :ivar adv_tk_earliest_tm: Earliest ticketing time. True if earliest permitted. False if not earliest permitted.
    :ivar adv_tk_latest_tm: Latest ticketing time. True if time is latest permitted. False if time is not latest permitted.
    :ivar adv_tk_rsvn_hrs: Ticketing reservation hours. True if in hours. False if not in hours.
    :ivar adv_tk_rsvn_days: Ticketing reservation days. True if in days. False if not in days.
    :ivar adv_tk_rsvn_months: Ticketing reservation months. True if in months. False if not in months.
    :ivar adv_tk_start_hrs: Latest ticketing departure. True if time is latest permitted. False if time is not latest permitted.
    :ivar adv_tk_start_days: Ticketing departure days. True if in days. False if not in days.
    :ivar adv_tk_start_months: Ticketing reservation months. True if in months. False if not in months.
    :ivar adv_tk_waived: Ticketing waived. True if waived. False if not waived.
    :ivar adv_tk_any_tm: Ticketing anytime. True if anytime. False if limited time.
    :ivar adv_tk_end_item: Ticketing end item. True if advanced ticketing item and more values. False if end item does not exist.
    :ivar adv_rsvn_tm: Advanced reservation time.
    :ivar adv_tk_rsvn_tm: Advanced ticketing reservation time.
    :ivar adv_tk_start_tm: Advanced ticketing departure time.
    :ivar earliest_rsvn_dt_present: Earliest reservation date. True if date is present. False if date is not present.
    :ivar earliest_tk_dt_present: Earliest ticketing date. True if date is present. False if date is not present.
    :ivar latest_rsvn_dt_present: Latest reservation date. True if date is present. False if date is not present.
    :ivar latest_tk_dt_present: Latest ticketing date.  True if date is present. False if date is not present.
    :ivar earliest_rsvn_dt: Earliest reservation date.
    :ivar earliest_tk_dt: Earliest ticketing date.
    :ivar latest_rsvn_dt: Latest reservation date.
    :ivar latest_tk_dt: Latest ticketing date.
    """
    class Meta:
        name = "ADVType"

    adv_rsvn_only_if_tk: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnOnlyIfTk",
            type="Attribute"
        )
    )
    adv_rsvn_any_tm: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnAnyTm",
            type="Attribute"
        )
    )
    adv_rsvn_hrs: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnHrs",
            type="Attribute"
        )
    )
    adv_rsvn_days: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnDays",
            type="Attribute"
        )
    )
    adv_rsvn_months: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnMonths",
            type="Attribute"
        )
    )
    adv_rsvn_earliest_tm: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnEarliestTm",
            type="Attribute"
        )
    )
    adv_rsvn_latest_tm: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnLatestTm",
            type="Attribute"
        )
    )
    adv_rsvn_waived: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnWaived",
            type="Attribute"
        )
    )
    adv_rsvn_data_exists: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnDataExists",
            type="Attribute"
        )
    )
    adv_rsvn_end_item: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnEndItem",
            type="Attribute"
        )
    )
    adv_tk_earliest_tm: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkEarliestTm",
            type="Attribute"
        )
    )
    adv_tk_latest_tm: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkLatestTm",
            type="Attribute"
        )
    )
    adv_tk_rsvn_hrs: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkRsvnHrs",
            type="Attribute"
        )
    )
    adv_tk_rsvn_days: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkRsvnDays",
            type="Attribute"
        )
    )
    adv_tk_rsvn_months: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkRsvnMonths",
            type="Attribute"
        )
    )
    adv_tk_start_hrs: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkStartHrs",
            type="Attribute"
        )
    )
    adv_tk_start_days: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkStartDays",
            type="Attribute"
        )
    )
    adv_tk_start_months: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkStartMonths",
            type="Attribute"
        )
    )
    adv_tk_waived: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkWaived",
            type="Attribute"
        )
    )
    adv_tk_any_tm: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkAnyTm",
            type="Attribute"
        )
    )
    adv_tk_end_item: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTkEndItem",
            type="Attribute"
        )
    )
    adv_rsvn_tm: Optional[int] = field(
        default=None,
        metadata=dict(
            name="AdvRsvnTm",
            type="Attribute"
        )
    )
    adv_tk_rsvn_tm: Optional[int] = field(
        default=None,
        metadata=dict(
            name="AdvTkRsvnTm",
            type="Attribute"
        )
    )
    adv_tk_start_tm: Optional[int] = field(
        default=None,
        metadata=dict(
            name="AdvTkStartTm",
            type="Attribute"
        )
    )
    earliest_rsvn_dt_present: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="EarliestRsvnDtPresent",
            type="Attribute"
        )
    )
    earliest_tk_dt_present: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="EarliestTkDtPresent",
            type="Attribute"
        )
    )
    latest_rsvn_dt_present: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="LatestRsvnDtPresent",
            type="Attribute"
        )
    )
    latest_tk_dt_present: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="LatestTkDtPresent",
            type="Attribute"
        )
    )
    earliest_rsvn_dt: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EarliestRsvnDt",
            type="Attribute"
        )
    )
    earliest_tk_dt: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EarliestTkDt",
            type="Attribute"
        )
    )
    latest_rsvn_dt: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LatestRsvnDt",
            type="Attribute"
        )
    )
    latest_tk_dt: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LatestTkDt",
            type="Attribute"
        )
    )


@dataclass
class ActionDetails:
    """Information related to the storing of the fare: Agent, Date and Action for
    Provider: 1P/1J.

    :ivar pseudo_city_code: PCC in the host of the agent who stored the fare for Provider: 1P/1J
    :ivar agent_sine: The sign in of the user who stored the fare for Provider: 1P/1J
    :ivar event_date: Date at which the fare was stored for Provider: 1P/1J
    :ivar event_time: Time at which the fare was stored for Provider: 1P/1J
    :ivar text: The type of action the agent performed for Provider: 1P/1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=2,
            max_length=10
        )
    )
    agent_sine: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AgentSine",
            type="Attribute"
        )
    )
    event_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EventDate",
            type="Attribute"
        )
    )
    event_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EventTime",
            type="Attribute"
        )
    )
    text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute"
        )
    )


@dataclass
class AdditionalInfo:
    """
    :ivar category: The category code is the code the AdditionalInfo text came from, e.g. S5 or S7.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    category: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AddlBookingCodeInformation:
    """Returns additional booking codes for the selected fare.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=1,
            white_space="collapse"
        )
    )


@dataclass
class Adjustment:
    """An indentifier which indentifies adjustment made on original pricing. It can
    a flat amount or percentage of original price. The value of Amount/Percent can
    be negetive. Negative value implies a discount.

    :ivar amount: Implies a flat amount to be adjusted.
                                Negetive value implies a discount.
    :ivar percent: Implies an adjustment to be made on
                                original price. Negetive value implies a discount.
    :ivar adjusted_total_price: The adjusted price after applying adjustment
                            on Total price
    :ivar approximate_adjusted_total_price: The Converted adjusted total price in Default
                            Currency for this entity.
    :ivar booking_traveler_ref: Reference to a booking traveler for which adjustment is applied.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Element"
        )
    )
    percent: Optional[float] = field(
        default=None,
        metadata=dict(
            name="Percent",
            type="Element"
        )
    )
    adjusted_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AdjustedTotalPrice",
            type="Attribute",
            required=True
        )
    )
    approximate_adjusted_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateAdjustedTotalPrice",
            type="Attribute"
        )
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute"
        )
    )


@dataclass
class AirFareDisplayRuleKey:
    """The Tariff Fare Rule requested using a Key. The key is typically a provider
    specific string which is required to make either a following Air Fare Tariff
    request for Mileage/Routing information or Air Fare Tariff Rule Request.

    :ivar value:
    :ivar provider_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=1,
            white_space="collapse"
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )


@dataclass
class AirItinerarySolutionRef:
    """Reference to a complete AirItinerarySolution from a shared list.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AirPricingInfoRef:
    """Reference to a AirPricing from a shared list.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AirRefundModifiers:
    """Provides controls and switches for the Refund process.

    :ivar refund_date:
    :ivar account_code:
    :ivar ticket_designator:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    refund_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RefundDate",
            type="Attribute"
        )
    )
    account_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute"
        )
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketDesignator",
            type="Attribute",
            min_length=0,
            max_length=20
        )
    )


@dataclass
class AirReservationLocatorCode:
    """Identifies the AirReservation LocatorCode within the Universal Record.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=5,
            max_length=8
        )
    )


@dataclass
class AirSearchAsynchModifiers:
    """Controls and switches for the Air Search request for Asynch Request.

    :ivar initial_asynch_result:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    initial_asynch_result: Optional["AirSearchAsynchModifiers.InitialAsynchResult"] = field(
        default=None,
        metadata=dict(
            name="InitialAsynchResult",
            type="Element"
        )
    )

    @dataclass
    class InitialAsynchResult:
        """
        :ivar max_wait: Max wait time in seconds.
        """
        max_wait: Optional[int] = field(
            default=None,
            metadata=dict(
                name="MaxWait",
                type="Attribute"
            )
        )


@dataclass
class AirSegmentRef:
    """Reference to a complete AirSegment from a shared list.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AirSegmentTicketingModifiers:
    """Specifies modifiers that a particular segment should be priced with. If this
    is used, then there must be one for each AirSegment in the AirItinerary.

    :ivar air_segment_ref:
    :ivar brand_tier: Modifier to price by specific brand tier number.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Attribute"
        )
    )
    brand_tier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandTier",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=10
        )
    )


@dataclass
class Alliance:
    """Alliance Code.

    :ivar code: The possible values are *A for Star Alliance,*O for One world,*S for Sky team etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AlternateLocationDistanceRef:
    """Reference to a AlternateLocationDistance.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class BookingCode:
    """The Booking Code (Class of Service) for a segment.

    :ivar code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=2
        )
    )


@dataclass
class BookingCodeInfo:
    """Details Cabin class info and class of service information with availability
    counts. Only provided on search results and grouped by Cabin class.

    :ivar cabin_class: Specifies Cabin class for a group of
                            class of services. Cabin class is not identified if it is not
                            present.
    :ivar booking_counts: Lists class of service and their counts for
                            specific cabin class
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    cabin_class: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute"
        )
    )
    booking_counts: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingCounts",
            type="Attribute"
        )
    )


@dataclass
class BookingInfo:
    """Links segments and fares together.

    :ivar booking_code:
    :ivar booking_count: Seat availability of the BookingCode
    :ivar cabin_class:
    :ivar fare_info_ref:
    :ivar segment_ref:
    :ivar coupon_ref: The coupon to which that booking is relative
                            (if applicable)
    :ivar air_itinerary_solution_ref: Reference to an Air Itinerary Solution
    :ivar host_token_ref: HostToken Reference for this segment and fare combination.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingCode",
            type="Attribute",
            required=True
        )
    )
    booking_count: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingCount",
            type="Attribute"
        )
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute"
        )
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            required=True
        )
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )
    coupon_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CouponRef",
            type="Attribute"
        )
    )
    air_itinerary_solution_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirItinerarySolutionRef",
            type="Attribute"
        )
    )
    host_token_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="HostTokenRef",
            type="Attribute"
        )
    )


@dataclass
class BookingRulesFareReference:
    """Fare Reference associated with the BookingRules. Containing a text container
    for vendor response text.

    :ivar value:
    :ivar class_of_service:
    :ivar ticket_designator_code:
    :ivar account_code:
    :ivar upgrage_allowed:
    :ivar upgrade_class_of_service:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            min_length=1,
            max_length=2
        )
    )
    ticket_designator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketDesignatorCode",
            type="Attribute",
            min_length=0,
            max_length=20
        )
    )
    account_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute"
        )
    )
    upgrage_allowed: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="UpgrageAllowed",
            type="Attribute"
        )
    )
    upgrade_class_of_service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="UpgradeClassOfService",
            type="Attribute",
            min_length=1,
            max_length=2
        )
    )


@dataclass
class BrandId:
    """Brand ids for Merchandising details.

    :ivar id:
    """
    class Meta:
        name = "BrandID"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Id",
            type="Attribute",
            required=True
        )
    )


@dataclass
class BrandInfo:
    """Commercially recognized product offered by an airline.

    :ivar key: Brand Key
    :ivar brand_id: The unique identifier of the brand
    :ivar air_pricing_info_ref: A reference to a AirPricing. Providers: ACH, 1G, 1V, 1P, 1J.
    :ivar fare_info_ref: A reference to a FareInfo. Providers: ACH, 1G, 1V, 1P, 1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandID",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=19
        )
    )
    air_pricing_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Attribute"
        )
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute"
        )
    )


@dataclass
class BrandModifiers:
    """Used to specify the level of branding requested.

    :ivar fare_family_display: Used to request a fare family display.
    :ivar basic_details_only: Used to request basic details of the brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_family_display: Optional["BrandModifiers.FareFamilyDisplay"] = field(
        default=None,
        metadata=dict(
            name="FareFamilyDisplay",
            type="Element"
        )
    )
    basic_details_only: Optional["BrandModifiers.BasicDetailsOnly"] = field(
        default=None,
        metadata=dict(
            name="BasicDetailsOnly",
            type="Element"
        )
    )

    @dataclass
    class FareFamilyDisplay:
        """
        :ivar modifier_type: "FareFamily" returns the lowest branded fares in a fare family.
        													"MaintainBookingCode" attempts to return the lowest branded fare in a fare family display based on the permitted booking code. Any brand that does not have a fare for the permitted booking code will then have the lowest fare returned.
        													"LowestFareInBrand" returns the lowest fare within each branded fare in a fare family display.
        """
        modifier_type: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ModifierType",
                type="Attribute",
                required=True
            )
        )

    @dataclass
    class BasicDetailsOnly:
        """
        :ivar return_basic_details:
        """
        return_basic_details: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="ReturnBasicDetails",
                type="Attribute",
                required=True
            )
        )


@dataclass
class Co2Emission:
    """Carbon emission values.

    :ivar air_segment_ref: The segment reference
    :ivar value: The CO2 emission value for the air segment
    """
    class Meta:
        name = "CO2Emission"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Attribute"
        )
    )
    value: Optional[float] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute"
        )
    )


@dataclass
class CarrierCode:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            length=2
        )
    )


@dataclass
class CodeshareInfo:
    """Describes the codeshare disclosure (simple text string) or the specific
    operating flight information (as attributes).

    :ivar value:
    :ivar operating_carrier: The actual carrier that is operating the
                                    flight.
    :ivar operating_flight_number: The actual flight number of the carrier that
                                    is operating the flight.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    operating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OperatingCarrier",
            type="Attribute",
            length=2
        )
    )
    operating_flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OperatingFlightNumber",
            type="Attribute",
            max_length=5
        )
    )


@dataclass
class CompanyName:
    """Supplier info that is specific to the Unique Id.

    :ivar supplier_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            required=True,
            length=2
        )
    )


@dataclass
class ContractCode:
    """Some private fares (non-ATPCO) are secured to a contract code.

    :ivar code: The 1-64 character string which uniquely
                            identifies a Contract.
    :ivar company_name: Providers supported : ACH
    :ivar provider_code:
    :ivar supplier_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=64
        )
    )
    company_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CompanyName",
            type="Attribute"
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            min_length=1,
            max_length=5
        )
    )


@dataclass
class CreditSummary:
    """Credit summary associated with the account.

    :ivar currency_code:
    :ivar current_balance:
    :ivar initial_credit:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    currency_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            length=3
        )
    )
    current_balance: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="CurrentBalance",
            type="Attribute",
            required=True
        )
    )
    initial_credit: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="InitialCredit",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CustomerReceiptInfo:
    """Information about customer receipt via email. Supported providers are
    1V/1G/1P/1J.

    :ivar booking_traveler_ref: Refererence of the Booking Traveler related to the email.
    :ivar email_ref: Reference to the email address used for receipt of EMD.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            required=True
        )
    )
    email_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EmailRef",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CustomerSearch:
    """Detailed customer information for searching pre pay profiles."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class Document:
    """APIS Document Details.

    :ivar sequence: Sequence number for the document.
    :ivar type: Type of the Document. Visa, Passport,
                            DriverLicense etc.
    :ivar level: Applicability level of the Document.
                            Required, Supported, API_Supported or Unknown.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    sequence: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Sequence",
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
    level: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Level",
            type="Attribute"
        )
    )


@dataclass
class DocumentModifiers:
    """
    :ivar generate_itinerary_invoice: Generate itinerary/invoice documents along with
                            ticket
    :ivar generate_accounting_interface: Generate interface message along with ticket
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    generate_itinerary_invoice: bool = field(
        default=False,
        metadata=dict(
            name="GenerateItineraryInvoice",
            type="Attribute"
        )
    )
    generate_accounting_interface: bool = field(
        default=False,
        metadata=dict(
            name="GenerateAccountingInterface",
            type="Attribute"
        )
    )


@dataclass
class DocumentRequired:
    """Additional Details, Documents , Project IDs.

    :ivar doc_type:
    :ivar include_exclude_use_ind:
    :ivar doc_id:
    :ivar allowed_ids:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    doc_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocType",
            type="Attribute"
        )
    )
    include_exclude_use_ind: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeExcludeUseInd",
            type="Attribute"
        )
    )
    doc_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocId",
            type="Attribute"
        )
    )
    allowed_ids: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AllowedIds",
            type="Attribute"
        )
    )


@dataclass
class Emdendorsement:
    """Endorsement for EMD. Supported providers are 1V/1G/1P/1J.

    :ivar value:
    """
    class Meta:
        name = "EMDEndorsement"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=1,
            max_length=255
        )
    )


@dataclass
class EmdtravelerInfo:
    """EMD traveler information. Supported providers are 1G/1V/1P/1J.

    :ivar name_info: Name information of the EMD traveler.
    :ivar traveler_type: Defines the type of traveler used for booking which could be a non-defining type (Companion, Web-fare, etc), or a standard type (Adult, Child, etc).
    :ivar age: Age of the traveler
    """
    class Meta:
        name = "EMDTravelerInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    name_info: Optional["EmdtravelerInfo.NameInfo"] = field(
        default=None,
        metadata=dict(
            name="NameInfo",
            type="Element",
            required=True
        )
    )
    traveler_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            min_length=3,
            max_length=5
        )
    )
    age: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute"
        )
    )

    @dataclass
    class NameInfo:
        """
        :ivar prefix: Name prefix.
        :ivar first: First Name.
        :ivar middle: Midle name.
        :ivar last: Last Name.
        :ivar suffix: Name suffix.
        """
        prefix: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Prefix",
                type="Attribute",
                min_length=1,
                max_length=20
            )
        )
        first: Optional[str] = field(
            default=None,
            metadata=dict(
                name="First",
                type="Attribute",
                required=True,
                min_length=1,
                max_length=256
            )
        )
        middle: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Middle",
                type="Attribute",
                min_length=1,
                max_length=256
            )
        )
        last: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Last",
                type="Attribute",
                required=True,
                min_length=1,
                max_length=256
            )
        )
        suffix: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Suffix",
                type="Attribute",
                min_length=1,
                max_length=256
            )
        )


@dataclass
class Embargo:
    """Embargo details. Provider: 1G, 1V, 1P, 1J.

    :ivar key:
    :ivar carrier:
    :ivar segment_ref:
    :ivar name: The commercial name of the optional service on
                        which the embargo applies. Provider: 1G, 1V, 1P, 1J
    :ivar text: Brief description of the embargo. Provider: 1G,
                        1V, 1P, 1J
    :ivar secondary_type: The secondary type of the optional service on which the embargo applies.  Provider: 1G, 1V, 1P, 1J
    :ivar type: The type of optional service on which the embargo applies.  Provider: 1G, 1V, 1P, 1J
    :ivar url: Website of the operating carrier. Provider: 1G,
                        1V, 1P, 1J
    :ivar service_sub_code: The service sub code of the optional service on which the embargo applies.  Provider: 1G, 1V, 1P, 1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            length=2
        )
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            max_length=30
        )
    )
    text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute"
        )
    )
    secondary_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SecondaryType",
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            min_length=1,
            max_length=128
        )
    )
    url: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Url",
            type="Attribute"
        )
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute",
            max_length=3
        )
    )


@dataclass
class ExchangedTicketInfo:
    """Contains Exchanged/Reissued Ticket Information.

    :ivar number: Original Ticket that was Exchange/Reissued
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True,
            length=13
        )
    )


@dataclass
class ExcludeTicketing:
    """Exclude ticketing of traveler referenced. Supported Provider: JAL.

    :ivar booking_traveler_ref: Reference to a booking traveler for which ticketing modifier is applied.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class ExemptObfee:
    """Used to specify which OB fees are exempt; if none are listed, it means all
    should be exempt.

    :ivar sub_code:
    """
    class Meta:
        name = "ExemptOBFee"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    sub_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SubCode",
            type="Element",
            min_occurs=0,
            max_occurs=8
        )
    )


@dataclass
class ExemptTaxes:
    """Request tax exemption for specific tax category and/or all taxes of a
    specific country.

    :ivar country_code: Specify ISO country code for which tax
                             exemption is requested.
    :ivar tax_category: Specify tax category for which tax
                             exemption is requested.
    :ivar all_taxes: Request exemption of all taxes.
    :ivar tax_territory: exemption is achieved by sending in the TaxTerritory in the tax exempt price request.
    :ivar company_name: The federal government body name must be provided in this element. This field is required by AC
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    country_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="CountryCode",
            type="Element",
            min_occurs=0,
            max_occurs=999,
            length=2
        )
    )
    tax_category: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TaxCategory",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    all_taxes: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AllTaxes",
            type="Attribute"
        )
    )
    tax_territory: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TaxTerritory",
            type="Attribute",
            length=2
        )
    )
    company_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CompanyName",
            type="Attribute",
            min_length=1,
            max_length=24
        )
    )


@dataclass
class FareBasis:
    """Fare Basis Code.

    :ivar code: The fare basis code for this fare
    :ivar segment_ref: The segment to which this FareBasis Code is to
                            connected
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )


@dataclass
class FareCalc:
    """The complete fare calculation line.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class FareDetailsRef:
    """Reference of the Fare.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FareInfoMessage:
    """
    A simple textual fare information message.Providers supported : 1G/1V/1P/1J
    :ivar value:
    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FareInfoRef:
    """Reference to a complete FareInfo from a shared list.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FareMileageInformation:
    """Contains Fare/Tariff Display Mileage Information.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class FareNoteRef:
    """A reference to a fare note from a shared list. Used to minimize xml results.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FarePricing:
    """Container for Fare Pricing Information. One per PTC type.

    :ivar passenger_type:
    :ivar total_fare_amount:
    :ivar private_fare: NegotiatedFare attribute from
                            earlier version of schema used to imply whether the fare is
                            private fare or not. So, this attribute is renamed to PrivateFare
                            as it best suited.
    :ivar negotiated_fare: Identifies the fare as a Negotiated
                            Fare.
    :ivar auto_priceable: Identifies the fare as Autopriceable or not. False value means the fare filing is incomplete and the fare should not be used.
    :ivar total_net_fare_amount: Total Net fare amount.
    :ivar base_fare: Base fare amount.
    :ivar taxes:
    :ivar mmid: Contains the Reference id which is generated when the request was ReturnMM=”true”.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    passenger_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PassengerType",
            type="Attribute",
            min_length=3,
            max_length=5
        )
    )
    total_fare_amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalFareAmount",
            type="Attribute"
        )
    )
    private_fare: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="PrivateFare",
            type="Attribute"
        )
    )
    negotiated_fare: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NegotiatedFare",
            type="Attribute"
        )
    )
    auto_priceable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AutoPriceable",
            type="Attribute"
        )
    )
    total_net_fare_amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalNetFareAmount",
            type="Attribute"
        )
    )
    base_fare: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BaseFare",
            type="Attribute"
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    mmid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MMid",
            type="Attribute"
        )
    )


@dataclass
class FareRemarkRef:
    """
    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FareRestrictionSaleDate:
    """Restrict when this fare can be sold.

    :ivar start_date:
    :ivar end_date:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    start_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute"
        )
    )
    end_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EndDate",
            type="Attribute"
        )
    )


@dataclass
class FareRestrictionSeasonal:
    """Fares Restricted based on the season requested. StartDate and EndDate are
    strings representing respective dates. If a year component is present then it
    signifies an exact date. If only day and month components are present then it
    signifies a seasonal date, which means applicable for that date in any year.

    :ivar comment:
    :ivar variation_by_travel_dates:
    :ivar seasonal_range1_ind:
    :ivar seasonal_range1_start_date:
    :ivar seasonal_range1_end_date:
    :ivar seasonal_range2_ind:
    :ivar seasonal_range2_start_date:
    :ivar seasonal_range2_end_date:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Comment",
            type="Attribute"
        )
    )
    variation_by_travel_dates: Optional[str] = field(
        default=None,
        metadata=dict(
            name="VariationByTravelDates",
            type="Attribute"
        )
    )
    seasonal_range1_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SeasonalRange1Ind",
            type="Attribute"
        )
    )
    seasonal_range1_start_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SeasonalRange1StartDate",
            type="Attribute"
        )
    )
    seasonal_range1_end_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SeasonalRange1EndDate",
            type="Attribute"
        )
    )
    seasonal_range2_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SeasonalRange2Ind",
            type="Attribute"
        )
    )
    seasonal_range2_start_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SeasonalRange2StartDate",
            type="Attribute"
        )
    )
    seasonal_range2_end_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SeasonalRange2EndDate",
            type="Attribute"
        )
    )


@dataclass
class FareRoutingInformation:
    """Contains Fare/Tariff Display Routing Information.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class FareRuleCategory:
    """Rule Categories to filter on.

    :ivar category:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    category: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            required=True,
            min_inclusive=1,
            max_inclusive=50
        )
    )


@dataclass
class FareRuleFailureInfo:
    """Returns fare rule failure reason codes when fare basis code is forced.

    :ivar reason:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    reason: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Reason",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FareRuleKey:
    """The Fare Rule requested using a Key. The key is typically a provider
    specific string which is required to make a following Air Fare Rule Request.
    This Key is returned in Low Fare Shop or Air Price Response.

    :ivar value:
    :ivar fare_info_ref: The Fare Component to which this Rule Key
                                    applies
    :ivar provider_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=1,
            white_space="collapse"
        )
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            required=True
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2,
            max_length=5
        )
    )


@dataclass
class FareRuleLong:
    """Long Text Fare Rule.

    :ivar value:
    :ivar category:
    :ivar type:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    category: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            required=True
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )


@dataclass
class FareRuleLongRef:
    """A reference to an Long Text Rule in a Shared List.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FareRuleNameValue:
    """Fare Rule Name Value Pair, used in Short Rules.

    :ivar name:
    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

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
            type="Attribute",
            required=True
        )
    )


@dataclass
class FareRuleShortRef:
    """A reference to an Short Text Rule in a Shared List.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FareRulesFilterCategory:
    """Fare Rules Filter if requested will return rules for requested category in
    the response. Applicable for providers 1G,1V,1P,1J.

    :ivar category_code: Fare Rules Filter category can be requested. Currently only '˜MIN, MAX, ADV, CHG, OTH' is supported. Applicable for Providers 1G,1V,1P,1J.
    :ivar fare_info_ref: This tells if Low Fare Finder was used.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    category_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="CategoryCode",
            type="Element",
            min_occurs=1,
            max_occurs=35
        )
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute"
        )
    )


@dataclass
class FareStatusFailureInfo:
    """Denotes the failure reason of a particular fare.

    :ivar code: The failure code of the fare.
    :ivar reason: The reason for the failure.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )
    reason: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Reason",
            type="Attribute"
        )
    )


@dataclass
class FareTicketDesignator:
    """Ticket Designator used to further qualify a Fare.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            min_length=0,
            max_length=20
        )
    )


@dataclass
class FareType:
    """Used to request fares based on the ATPCO type code.

    :ivar code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=5
        )
    )


@dataclass
class FeeApplication:
    """
    :ivar value:
    :ivar code: The code associated to the fee application. The  choices are: 1, 2, 3, 4, 5, K, F
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            length=1
        )
    )


@dataclass
class FlexExploreModifiers:
    """This is the container for a set of modifiers which allow the user to perform
    a special kind of low fare search, depicted as flex explore, based on different
    parameters like Area, Zone, Country, State, Specific locations, Distance around
    the actual destination of the itinerary. Applicable for providers 1G,1V,1P.

    :ivar destination: List of specific destinations for performing flex explore. Applicable only with flex explore type - Destination
    :ivar type: Type of flex explore to be performed
    :ivar radius: Radius around the destination of actual itinerary in which the search would be performed. Supported only with types - DistanceInMiles and DistanceInKilometers
    :ivar group_name: Group name for a set of destinations to be searched.  Use with Type=Group. Group names are defined in the Search Control Console. Supported Providers:  1G/1V/1P
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    destination: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Destination",
            type="Element",
            min_occurs=0,
            max_occurs=59,
            length=3,
            white_space="collapse"
        )
    )
    type: Optional["FlexExploreModifiers.Type"] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    radius: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Radius",
            type="Attribute"
        )
    )
    group_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="GroupName",
            type="Attribute",
            max_length=15
        )
    )

    class Type(Enum):
        """
        :cvar ANY_WHERE:
        :cvar AREA:
        :cvar ZONE:
        :cvar COUNTRY:
        :cvar STATE:
        :cvar DISTANCE_IN_MILES:
        :cvar DISTANCE_IN_KILOMETERS:
        :cvar DESTINATION:
        :cvar GROUP:
        """
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
    """Reference to a complete FlightDetails from a shared list.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FlightInfoCriteria:
    """
    :ivar key: An identifier to link the flightinfo responses
                            to the criteria. The value passed here will be returned in the
                            resulting flightinfo(s) from this command.
    :ivar carrier: The carrier that is marketing this segment
    :ivar flight_number: The flight number under which the marketing
                            carrier is marketing this flight
    :ivar origin: The IATA location code for this origination of
                            this entity.
    :ivar destination: The IATA location code for this destination of
                            this entity.
    :ivar departure_date: The date at which this entity departs. This
                            does not include time zone information since it can be derived
                            from the origin location.
    :ivar class_of_service:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            length=2
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            required=True,
            max_length=5
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    departure_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute",
            required=True
        )
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            min_length=1,
            max_length=2
        )
    )


@dataclass
class FlightType:
    """Modifier to request flight type options example non-stop only, non-stop and
    direct only, include single online connection etc.

    :ivar require_single_carrier:
    :ivar max_connections: The maximum number of connections within a
                            segment group.
    :ivar max_stops: The maximum number of stops within a
                            connection.
    :ivar non_stop_directs:
    :ivar stop_directs:
    :ivar single_online_con:
    :ivar double_online_con:
    :ivar triple_online_con:
    :ivar single_interline_con:
    :ivar double_interline_con:
    :ivar triple_interline_con:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    require_single_carrier: bool = field(
        default=False,
        metadata=dict(
            name="RequireSingleCarrier",
            type="Attribute"
        )
    )
    max_connections: int = field(
        default=-1,
        metadata=dict(
            name="MaxConnections",
            type="Attribute",
            min_inclusive=-1,
            max_inclusive=3
        )
    )
    max_stops: int = field(
        default=-1,
        metadata=dict(
            name="MaxStops",
            type="Attribute",
            min_inclusive=-1,
            max_inclusive=3
        )
    )
    non_stop_directs: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NonStopDirects",
            type="Attribute"
        )
    )
    stop_directs: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="StopDirects",
            type="Attribute"
        )
    )
    single_online_con: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="SingleOnlineCon",
            type="Attribute"
        )
    )
    double_online_con: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DoubleOnlineCon",
            type="Attribute"
        )
    )
    triple_online_con: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="TripleOnlineCon",
            type="Attribute"
        )
    )
    single_interline_con: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="SingleInterlineCon",
            type="Attribute"
        )
    )
    double_interline_con: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DoubleInterlineCon",
            type="Attribute"
        )
    )
    triple_interline_con: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="TripleInterlineCon",
            type="Attribute"
        )
    )


@dataclass
class GroupedOption:
    """
    :ivar optional_service_ref: Reference to a optionalService which is paired with other optional services in the parent PairedOptions element.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    optional_service_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OptionalServiceRef",
            type="Attribute",
            required=True
        )
    )


@dataclass
class HostReservation:
    """Defines a reservation that already exists in the host system (e.g an agent
    using Galileo Desktop already booked a reservation on Midwest in Sabre host
    system).

    :ivar carrier: The carrier code (e.g. YX, UA, ...) that is
                            providing the merchandising
    :ivar carrier_locator_code: The locator code in the supplier system (also
                            could be defined as locator in the carrier host system).
    :ivar provider_code: Contains the GDS or other provider code
                            of the entity actually housing the reservation. This is optional
                            when used on Merchandising Availability but required on
                            MerchandisingFulfillment.
    :ivar provider_locator_code: Contains the locator of the reservation
                            actually housed in the provider.
    :ivar universal_locator_code: The locator of the Universal Record, if one
                            exists.
    :ivar eticket: An flag to indicate if ticket has been issued for the PNR.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            length=2
        )
    )
    carrier_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CarrierLocatorCode",
            type="Attribute",
            required=True,
            min_length=5,
            max_length=8
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2,
            max_length=5
        )
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            required=True,
            max_length=15
        )
    )
    universal_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="UniversalLocatorCode",
            type="Attribute",
            min_length=5,
            max_length=8
        )
    )
    eticket: bool = field(
        default=False,
        metadata=dict(
            name="ETicket",
            type="Attribute"
        )
    )


@dataclass
class ImageLocation:
    """
    :ivar value:
    :ivar type: Type of Image Location. E.g., "Agent", "Consumer".
    :ivar image_width: The width of the image
    :ivar image_height: The height of the image
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    image_width: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ImageWidth",
            type="Attribute",
            required=True
        )
    )
    image_height: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ImageHeight",
            type="Attribute",
            required=True
        )
    )


@dataclass
class InFlightServices:
    """Available InFlight Services. They are: 'Movie', 'Telephone', 'Telex',
    'AudioProgramming', 'Television' ,'ResvBookingService' ,'DutyFreeSales'
    ,'Smoking' ,'NonSmoking' ,'ShortFeatureVideo' ,'NoDutyFree'
    ,'InSeatPowerSource' ,'InternetAccess' ,'Email' ,'Library' ,'LieFlatSeat'
    ,'Additional service(s) exists' ,'WiFi' ,'Lie-Flat seat first' ,'Lie-Flat seat
    business' ,'Lie-Flat seat premium economy' ,'Amenities subject to change' etc..
    These follow the IATA standard. Please see the IATA standards for a more
    complete list.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class LanguageOption:
    """Enables itineraries and invoices to print in different languages.

    :ivar language: 2 Letter ISO Language code
    :ivar country: 2 Letter ISO Country code
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    language: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Language",
            type="Attribute",
            required=True,
            length=2
        )
    )
    country: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Country",
            type="Attribute",
            required=True,
            length=2
        )
    )


@dataclass
class LegDetail:
    """Information about the journey Leg, Shared by Leg and LegPrice Elements.

    :ivar key:
    :ivar origin_airport: Returns the origin airport code for the
                            Leg Detail.
    :ivar destination_airport: Returns the destination airport code for
                            the Leg Detail.
    :ivar carrier: Carrier for the Search Leg Detail.
    :ivar travel_date: The Departure date and time for this Leg
                            Detail.
    :ivar flight_number: Flight Number for the Search Leg Detail.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    origin_airport: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OriginAirport",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination_airport: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DestinationAirport",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            length=2
        )
    )
    travel_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelDate",
            type="Attribute"
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            max_length=5
        )
    )


@dataclass
class LegRef:
    """Reference to a Leg.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class LoyaltyCardDetails:
    """Passenger Loyalty card details.

    :ivar supplier_code: Carrier Code
    :ivar priority_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            required=True,
            length=2
        )
    )
    priority_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PriorityCode",
            type="Attribute",
            required=True,
            pattern=r"[a-zA-Z0-9]{1,1}"
        )
    )


@dataclass
class Maxtype:
    """
    :ivar hours_max: Maximum hours. True if unit of time is hours. False if unit of time is not hours.
    :ivar days_max: Maximum days. True if unit of time is days. False if unit of time is not days.
    :ivar months_max: Maximum months. True if unit of time is months. False if unit of time is not months.
    :ivar occur_ind_max: Maximum cccurance indicator. True if day of the week is used. False if day of the week is not used.
    :ivar same_day_max: Same day maximum. True if Stay is same day. False if Stay is not same day.
    :ivar start_ind_max: Start indicator. True if start indicator. False if not a start indicator.
    :ivar completion_ind: Completion indicator. True if Completion C Indicator. False if not Completion C Indicator.
    :ivar tm_dowmax: If a max unit of time is true then number corrolates to day of the week starting with 1 for Sunday.
    :ivar num_occur_max: Number of maximum occurances.
    """
    class Meta:
        name = "MAXType"

    hours_max: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="HoursMax",
            type="Attribute"
        )
    )
    days_max: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DaysMax",
            type="Attribute"
        )
    )
    months_max: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="MonthsMax",
            type="Attribute"
        )
    )
    occur_ind_max: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="OccurIndMax",
            type="Attribute"
        )
    )
    same_day_max: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="SameDayMax",
            type="Attribute"
        )
    )
    start_ind_max: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="StartIndMax",
            type="Attribute"
        )
    )
    completion_ind: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="CompletionInd",
            type="Attribute"
        )
    )
    tm_dowmax: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TmDOWMax",
            type="Attribute"
        )
    )
    num_occur_max: Optional[int] = field(
        default=None,
        metadata=dict(
            name="NumOccurMax",
            type="Attribute"
        )
    )


@dataclass
class Mintype:
    """
    :ivar hours_min: Minimum hours. True if unit of time is hours.  False if unit of time is not hours.
    :ivar days_min: Minimum days. True if unit of time is days. False if unit of time is not days.
    :ivar months_min: Minimum months. True if unit of time is months. False if unit of time is not months.
    :ivar occur_ind_min: Minimum occurance indicator. True if day of the week is used. False if day of the week is not used.
    :ivar same_day_min: Same day minimum. True if Stay is same day. False if Stay is not same day.
    :ivar tm_dowmin: If a min unit of time is true then number corrolates to day of the week starting with 1 for Sunday.
    :ivar fare_component: Fare component number of the most restrictive fare.
    :ivar num_occur_min: Number of min occurances. This field is used in conjunction with the Day of Week.
    """
    class Meta:
        name = "MINType"

    hours_min: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="HoursMin",
            type="Attribute"
        )
    )
    days_min: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DaysMin",
            type="Attribute"
        )
    )
    months_min: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="MonthsMin",
            type="Attribute"
        )
    )
    occur_ind_min: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="OccurIndMin",
            type="Attribute"
        )
    )
    same_day_min: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="SameDayMin",
            type="Attribute"
        )
    )
    tm_dowmin: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TmDOWMin",
            type="Attribute"
        )
    )
    fare_component: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FareComponent",
            type="Attribute"
        )
    )
    num_occur_min: Optional[int] = field(
        default=None,
        metadata=dict(
            name="NumOccurMin",
            type="Attribute"
        )
    )


@dataclass
class MaxLayoverDurationType:
    """User can specify its attribute's value in Minutes. Maximum size of each
    attribute is 4.

    :ivar domestic: It will be applied for all Domestic-to-Domestic connections.
    :ivar gateway: It will be applied for all Domestic to International and International to Domestic connections.
    :ivar international: It will be applied for all International-to-International connections.
    """
    domestic: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Domestic",
            type="Attribute",
            min_inclusive=0,
            max_inclusive=9999
        )
    )
    gateway: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Gateway",
            type="Attribute",
            min_inclusive=0,
            max_inclusive=9999
        )
    )
    international: Optional[int] = field(
        default=None,
        metadata=dict(
            name="International",
            type="Attribute",
            min_inclusive=0,
            max_inclusive=9999
        )
    )


@dataclass
class MultiGdssearchIndicator:
    """Indicates whether public fares and/or private fares should be returned.

    :ivar type: Indicates whether only public fares or both public and private fares should be returned or a specific type of private fares. Examples of valid values are PublicFaresOnly, PrivateFaresOnly, AirlinePrivateFaresOnly, AgencyPrivateFaresOnly, PublicandPrivateFares, and NetFaresOnly.
    :ivar provider_code:
    :ivar default_provider: Use the value “true” if the provider is the default (primary) provider.  Use the value “false” if the provider is the alternate (secondary).  Use of this attribute requires specifically provisioned credentials.
    :ivar private_fare_code: The code of the corporate private fare.  This is the same as an account code.  Use of this attribute requires specifically provisioned credentials.
    :ivar private_fare_code_only: :  Indicates whether or not the private fares returned should be restricted to only those specific to the PrivateFareCode in the previous attribute.  This has the same validation as the AccountCodeFaresOnly attribute.  Use of this attribute requires specifically provisioned credentials.
    """
    class Meta:
        name = "MultiGDSSearchIndicator"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )
    default_provider: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DefaultProvider",
            type="Attribute"
        )
    )
    private_fare_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PrivateFareCode",
            type="Attribute"
        )
    )
    private_fare_code_only: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="PrivateFareCodeOnly",
            type="Attribute"
        )
    )


@dataclass
class Othtype:
    """
    :ivar cat0: Category 0 rules. True if category applies.  False if rules do not apply.
    :ivar cat1: Category 1 rules. True if category applies.  False if rules do not apply.
    :ivar cat2: Category 2 rules. True if category applies.  False if rules do not apply.
    :ivar cat3: Category 3 rules. True if category applies.  False if rules do not apply.
    :ivar cat4: Category 4 rules. True if category applies.  False if rules do not apply.
    :ivar cat5: Category 5 rules. True if category applies.  False if rules do not apply.
    :ivar cat6: Category 6 rules. True if category applies.  False if rules do not apply.
    :ivar cat7: Category 7 rules. True if category applies.  False if rules do not apply.
    :ivar cat8: Category 8 rules. True if category applies.  False if rules do not apply.
    :ivar cat9: Category 9 rules. True if category applies.  False if rules do not apply.
    :ivar cat10: Category 10 rules. True if category applies.  False if rules do not apply.
    :ivar cat11: Category 11 rules. True if category applies.  False if rules do not apply.
    :ivar cat12: Category 12 rules. True if category applies.  False if rules do not apply.
    :ivar cat13: Category 13 rules. True if category applies.  False if rules do not apply.
    :ivar cat14: Category 14 rules. True if category applies.  False if rules do not apply.
    :ivar cat15: Category 15 rules. True if category applies.  False if rules do not apply.
    :ivar cat16: Category 16 rules. True if category applies.  False if rules do not apply.
    :ivar cat17: Category 17 rules. True if category applies.  False if rules do not apply.
    :ivar cat18: Category 18 rules. True if category applies.  False if rules do not apply.
    :ivar cat19: Category 19 rules. True if category applies.  False if rules do not apply.
    :ivar cat20: Category 20 rules. True if category applies.  False if rules do not apply.
    :ivar cat21: Category 21 rules. True if category applies.  False if rules do not apply.
    :ivar cat22: Category 22 rules. True if category applies.  False if rules do not apply.
    :ivar cat23: Category 23 rules. True if category applies.  False if rules do not apply.
    :ivar cat24: Category 24 rules. True if category applies.  False if rules do not apply.
    :ivar cat25: Category 25 rules. True if category applies.  False if rules do not apply.
    :ivar cat26: Category 26 rules. True if category applies.  False if rules do not apply.
    :ivar cat27: Category 27 rules. True if category applies.  False if rules do not apply.
    :ivar cat28: Category 28 rules. True if category applies.  False if rules do not apply.
    :ivar cat29: Category 29 rules. True if category applies.  False if rules do not apply.
    :ivar cat30: Category 30 rules. True if category applies.  False if rules do not apply.
    :ivar cat31: Category 31 rules. True if category applies.  False if rules do not apply.
    :ivar restrictive_dt: Most restrictive ticketing date.
    :ivar surcharge_amt: Surcharge amount
    :ivar not_usacity: Not USA city.  True if Origin or final destination not a continental U.S. City. False if Origin or final destination a continental U.S. City.
    :ivar missing_rules: Missing rules.  True if rules are missing.  False if rules are not missing.
    """
    class Meta:
        name = "OTHType"

    cat0: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat0",
            type="Attribute"
        )
    )
    cat1: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat1",
            type="Attribute"
        )
    )
    cat2: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat2",
            type="Attribute"
        )
    )
    cat3: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat3",
            type="Attribute"
        )
    )
    cat4: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat4",
            type="Attribute"
        )
    )
    cat5: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat5",
            type="Attribute"
        )
    )
    cat6: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat6",
            type="Attribute"
        )
    )
    cat7: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat7",
            type="Attribute"
        )
    )
    cat8: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat8",
            type="Attribute"
        )
    )
    cat9: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat9",
            type="Attribute"
        )
    )
    cat10: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat10",
            type="Attribute"
        )
    )
    cat11: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat11",
            type="Attribute"
        )
    )
    cat12: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat12",
            type="Attribute"
        )
    )
    cat13: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat13",
            type="Attribute"
        )
    )
    cat14: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat14",
            type="Attribute"
        )
    )
    cat15: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat15",
            type="Attribute"
        )
    )
    cat16: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat16",
            type="Attribute"
        )
    )
    cat17: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat17",
            type="Attribute"
        )
    )
    cat18: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat18",
            type="Attribute"
        )
    )
    cat19: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat19",
            type="Attribute"
        )
    )
    cat20: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat20",
            type="Attribute"
        )
    )
    cat21: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat21",
            type="Attribute"
        )
    )
    cat22: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat22",
            type="Attribute"
        )
    )
    cat23: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat23",
            type="Attribute"
        )
    )
    cat24: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat24",
            type="Attribute"
        )
    )
    cat25: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat25",
            type="Attribute"
        )
    )
    cat26: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat26",
            type="Attribute"
        )
    )
    cat27: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat27",
            type="Attribute"
        )
    )
    cat28: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat28",
            type="Attribute"
        )
    )
    cat29: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat29",
            type="Attribute"
        )
    )
    cat30: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat30",
            type="Attribute"
        )
    )
    cat31: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat31",
            type="Attribute"
        )
    )
    restrictive_dt: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RestrictiveDt",
            type="Attribute"
        )
    )
    surcharge_amt: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="SurchargeAmt",
            type="Attribute"
        )
    )
    not_usacity: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NotUSACity",
            type="Attribute"
        )
    )
    missing_rules: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="MissingRules",
            type="Attribute"
        )
    )


@dataclass
class OfferAvailabilityModifiers:
    """
    :ivar service_type: To restrict offers to only this type.
    :ivar carrier: The carrier whose paid seat optional services is to be returned by uAPI.
    :ivar currency_type: Currency code override. Providers: ACH, 1G, 1V, 1P, 1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    service_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceType",
            type="Element",
            min_occurs=0,
            max_occurs=999,
            min_length=1,
            max_length=128
        )
    )
    carrier: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            min_occurs=0,
            max_occurs=999,
            length=2
        )
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            length=3
        )
    )


@dataclass
class OptionalServiceModifier:
    """Optional service modifiers.

    :ivar type: Optional service type
    :ivar secondary_type: Secondary optional service type
    :ivar supplier_code: Optional service supplier code
    :ivar service_sub_code: As published by ATPCO
    :ivar travel_date: The departure date of the air segment the optional service is valid for.
    :ivar description: This allows MDS to return specific image and text corresponding to the ancillary name (S5 ancillary name).
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=128
        )
    )
    secondary_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SecondaryType",
            type="Attribute",
            min_length=1,
            max_length=128
        )
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=5
        )
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute",
            required=True
        )
    )
    travel_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelDate",
            type="Attribute",
            required=True
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            required=True
        )
    )


@dataclass
class OptionalServiceRef:
    """Reference to optional service.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class OverrideCode:
    """Code corresponding to the type of OverridableException the user wishes to
    override.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            length=4
        )
    )


@dataclass
class PassengerDetailsRef:
    """Reference of the Passenger.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class PassengerReceiptOverride:
    """It is required when a passenger receipt is required immediately ,GDS
    overrides the default value.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=1,
            white_space="collapse"
        )
    )


@dataclass
class PassengerSeatPrice:
    """Only used when a passenger has a different price than the default.

    :ivar booking_traveler_ref:
    :ivar amount:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            required=True
        )
    )
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True
        )
    )


@dataclass
class PassengerTicketNumber:
    """Information related to Ticket Number.

    :ivar ticket_number: The identifying number for a Ticket for a
                            passenger.
    :ivar booking_traveler_ref: Reference to a passenger associated with
                            a ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            min_length=1,
            max_length=13
        )
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute"
        )
    )


@dataclass
class PaymentRef:
    """Reference to one of the air reservation payments.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class PenFeeType:
    """
    :ivar dep_required: Deposit required. True if require. False if not required.
    :ivar dep_non_ref: Deposit non-refundable.  True is  non-refundanbe.  False is refundable.
    :ivar tk_non_ref: Ticket non-refundable. True if non-refundanbe. False if refundable.
    :ivar air_vfee: Carrier fee. True if carrier fee is assessed should passenger for complete all conditions for travel at fare. False if it does not exist.
    :ivar cancellation: Cancellation. True if subject to penalty. False if no penalty.
    :ivar fail_confirm_space: Failure to confirm space. True if subject to penalty if seats are not confirmed. False if subject to penalty if seats are confirmed.
    :ivar itin_chg: Subject to penalty if Itinerary is changed requiring reissue of ticket. True if subject to penalty. False if no penalty if reissue required.
    :ivar replace_tk: Replace ticket. True if subject to penalty, if replacement of lost ticket / exchange order. False if no penalty, if replacement of lost ticket or exchange order.
    :ivar applicable: Applicable. True if amount specified is applicable. Flase if amount specified is not applicable.
    :ivar applicable_to: Applicable to penalty or deposit. True if amount specified applies to penalty. False if amount specified applies to deposit.
    :ivar amt: Amount of penalty.  If XXX.XX then it is an amount.  If it is XX then is is a percenatge.  Eg 100.00 or 000100.
    :ivar type: Type of penalty.  If it is D then dollar.  If it is P then percentage.
    :ivar currency: Currency code of penalty (e.g. USD).
    """
    dep_required: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DepRequired",
            type="Attribute"
        )
    )
    dep_non_ref: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DepNonRef",
            type="Attribute"
        )
    )
    tk_non_ref: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="TkNonRef",
            type="Attribute"
        )
    )
    air_vfee: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AirVFee",
            type="Attribute"
        )
    )
    cancellation: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cancellation",
            type="Attribute"
        )
    )
    fail_confirm_space: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="FailConfirmSpace",
            type="Attribute"
        )
    )
    itin_chg: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ItinChg",
            type="Attribute"
        )
    )
    replace_tk: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ReplaceTk",
            type="Attribute"
        )
    )
    applicable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Applicable",
            type="Attribute"
        )
    )
    applicable_to: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ApplicableTo",
            type="Attribute"
        )
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Amt",
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
    currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Currency",
            type="Attribute"
        )
    )


@dataclass
class Penalty:
    """
    :ivar amount: Penalty Amount
    :ivar penalty_type: This is the PPC (Price Processing Code)code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    penalty_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PenaltyType",
            type="Attribute"
        )
    )


@dataclass
class PenaltyInformation:
    """
    :ivar value:
    :ivar carrier: Fare-owning carrier
    :ivar fare_basis: Unique identifier that provides the association to the fare amount and fare rules.
    :ivar fare_component: A portion of a journey or itinerary between two consecutive fare break points.
    :ivar priceable_unit: Identifies FareComponents that are priced together
    :ivar board_point: Origin for the FareComponent
    :ivar off_point: Destination for the FareComponent
    :ivar minimum_change_fee: Estimated minimum change fee associated with the fare component.  Can be overridden by ChangeFeeApplicationCodes for other fare components.
    :ivar maximum_change_fee: Estimated maximum change fee associated with the fare component.  Can be overridden by ChangeFeeApplicationCodes for other fare components.
    :ivar filed_currency: Currency of the filed change fee
    :ivar conversion_rate: Conversion rate from filed change fee currency to reissue location currency
    :ivar refundable: Answers whether the FareComponent is refundable
    :ivar change_fee_application_code: Unique code associated with the PenaltyInformation text which defines how fees will be applied/calculated. E.g. J2 translates to "From among all fare components, changed and unchanged...."
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            length=2
        )
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute"
        )
    )
    fare_component: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FareComponent",
            type="Attribute"
        )
    )
    priceable_unit: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PriceableUnit",
            type="Attribute"
        )
    )
    board_point: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BoardPoint",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    off_point: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OffPoint",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    minimum_change_fee: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MinimumChangeFee",
            type="Attribute"
        )
    )
    maximum_change_fee: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MaximumChangeFee",
            type="Attribute"
        )
    )
    filed_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FiledCurrency",
            type="Attribute",
            length=3
        )
    )
    conversion_rate: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="ConversionRate",
            type="Attribute"
        )
    )
    refundable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute"
        )
    )
    change_fee_application_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ChangeFeeApplicationCode",
            type="Attribute",
            length=2
        )
    )


@dataclass
class PersonName:
    """Customer name field.

    :ivar first: Person First Name.
    :ivar last: Person Last Name.
    :ivar prefix: Person Name prefix.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    first: Optional[str] = field(
        default=None,
        metadata=dict(
            name="First",
            type="Attribute",
            min_length=1,
            max_length=64
        )
    )
    last: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=64
        )
    )
    prefix: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Prefix",
            type="Attribute",
            min_length=1,
            max_length=16
        )
    )


@dataclass
class PersonNameSearch:
    """Customer name field.

    :ivar last: Person Last Name to be searched for Flight Pass content.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    last: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=64
        )
    )


@dataclass
class PolicyCodesList:
    """
    :ivar policy_code: A code that indicates why an item was determined to be ‘out of policy’.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    policy_code: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="PolicyCode",
            type="Element",
            min_occurs=1,
            max_occurs=10,
            min_inclusive=1,
            max_inclusive=9999
        )
    )


@dataclass
class PriceChangeType:
    """Indicates a price change is found in Fare Control Manager.

    :ivar value:
    :ivar amount: Contains the currency and amount information.
                            Assume the amount is added unless a hyphen is present to indicate subtraction.
    :ivar carrier: Contains carrier code information
    :ivar segment_ref: Contains segment reference information
    """
    value: Optional[str] = field(
        default=None,
    )
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute"
        )
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )


@dataclass
class PriceRange:
    """
    :ivar default_currency: Indicates if the currency code of StartPrice / EndPrice is the default currency code
    :ivar start_price: Price range start value
    :ivar end_price: Price range end value
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    default_currency: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DefaultCurrency",
            type="Attribute"
        )
    )
    start_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StartPrice",
            type="Attribute"
        )
    )
    end_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EndPrice",
            type="Attribute"
        )
    )


@dataclass
class PrintBlankFormItinerary:
    """Produce a customized itinerary/Invoice document in blank form format.

    :ivar include_description: If it is true then document will be printed including descriptions.
    :ivar include_header: If it is true then document will be printed including it's header.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    include_description: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeDescription",
            type="Attribute",
            required=True
        )
    )
    include_header: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeHeader",
            type="Attribute",
            required=True
        )
    )


@dataclass
class PromoCode:
    """A container to specify Promotional code with Provider code and Supplier
    code.

    :ivar code: To be used to specify Promotional Code.
    :ivar provider_code: To be used to specify Provider Code.
    :ivar supplier_code: To be used to specify Supplier Code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=64
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2,
            max_length=5
        )
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=5
        )
    )


@dataclass
class RailCoachDetails:
    """
    :ivar rail_coach_number: Rail coach number for the returned coach details.
    :ivar available_rail_seats: Number of available seats present in this rail coach.
    :ivar rail_seat_map_availability: Indicates if seats are available in this rail coach which can be mapped.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    rail_coach_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RailCoachNumber",
            type="Attribute"
        )
    )
    available_rail_seats: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AvailableRailSeats",
            type="Attribute"
        )
    )
    rail_seat_map_availability: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="RailSeatMapAvailability",
            type="Attribute"
        )
    )


class RepricingModifiersFlightType(Enum):
    """
    :cvar DIRECT:
    :cvar NON_STOP:
    :cvar SINGLE_CONNECTION:
    :cvar NO_RESTRICTIONS:
    """
    DIRECT = "Direct"
    NON_STOP = "NonStop"
    SINGLE_CONNECTION = "SingleConnection"
    NO_RESTRICTIONS = "NoRestrictions"


@dataclass
class Restriction:
    """Fare Reference associated with the BookingRules.

    :ivar days_of_week_restriction:
    :ivar restriction_passenger_types:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    days_of_week_restriction: List["Restriction.DaysOfWeekRestriction"] = field(
        default_factory=list,
        metadata=dict(
            name="DaysOfWeekRestriction",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    restriction_passenger_types: List["Restriction.RestrictionPassengerTypes"] = field(
        default_factory=list,
        metadata=dict(
            name="RestrictionPassengerTypes",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class DaysOfWeekRestriction:
        """
        :ivar mon:
        :ivar tue:
        :ivar wed:
        :ivar thu:
        :ivar fri:
        :ivar sat:
        :ivar sun:
        :ivar restriction_exists_ind:
        :ivar application:
        :ivar include_exclude_use_ind:
        """
        mon: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Mon",
                type="Attribute"
            )
        )
        tue: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Tue",
                type="Attribute"
            )
        )
        wed: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Wed",
                type="Attribute"
            )
        )
        thu: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Thu",
                type="Attribute"
            )
        )
        fri: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Fri",
                type="Attribute"
            )
        )
        sat: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Sat",
                type="Attribute"
            )
        )
        sun: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="Sun",
                type="Attribute"
            )
        )
        restriction_exists_ind: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="RestrictionExistsInd",
                type="Attribute"
            )
        )
        application: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Application",
                type="Attribute"
            )
        )
        include_exclude_use_ind: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="IncludeExcludeUseInd",
                type="Attribute"
            )
        )

    @dataclass
    class RestrictionPassengerTypes:
        """
        :ivar max_nbr_travelers:
        :ivar total_nbr_ptc:
        """
        max_nbr_travelers: Optional[str] = field(
            default=None,
            metadata=dict(
                name="MaxNbrTravelers",
                type="Attribute"
            )
        )
        total_nbr_ptc: Optional[str] = field(
            default=None,
            metadata=dict(
                name="TotalNbrPTC",
                type="Attribute"
            )
        )


@dataclass
class RoutingRules:
    """Rules related to routing.

    :ivar routing:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    routing: List["RoutingRules.Routing"] = field(
        default_factory=list,
        metadata=dict(
            name="Routing",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class Routing:
        """
        :ivar direction_info:
        :ivar routing_constructed_ind:
        :ivar number:
        :ivar routing_restriction:
        """
        direction_info: List["RoutingRules.Routing.DirectionInfo"] = field(
            default_factory=list,
            metadata=dict(
                name="DirectionInfo",
                type="Element",
                min_occurs=0,
                max_occurs=999
            )
        )
        routing_constructed_ind: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="RoutingConstructedInd",
                type="Attribute"
            )
        )
        number: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Number",
                type="Attribute"
            )
        )
        routing_restriction: Optional[str] = field(
            default=None,
            metadata=dict(
                name="RoutingRestriction",
                type="Attribute"
            )
        )

        @dataclass
        class DirectionInfo:
            """
            :ivar location_code:
            :ivar direction:
            """
            location_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="LocationCode",
                    type="Attribute",
                    length=3,
                    white_space="collapse"
                )
            )
            direction: Optional["RoutingRules.Routing.DirectionInfo.Direction"] = field(
                default=None,
                metadata=dict(
                    name="Direction",
                    type="Attribute"
                )
            )

            class Direction(Enum):
                """
                :cvar TO:
                :cvar FROM_VALUE:
                """
                TO = "To"
                FROM_VALUE = "From"


@dataclass
class RuleCharges:
    """Container for rules related to charges such as deposits, surcharges,
    penalities, etc..

    :ivar penalty_type:
    :ivar departure_status:
    :ivar amount:
    :ivar percent:
    :ivar more_rules_present: If true, specifies that advance purchase
                            information will be present in fare rules.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    penalty_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PenaltyType",
            type="Attribute"
        )
    )
    departure_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureStatus",
            type="Attribute"
        )
    )
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    percent: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Percent",
            type="Attribute"
        )
    )
    more_rules_present: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="MoreRulesPresent",
            type="Attribute"
        )
    )


@dataclass
class Rules:
    """
    :ivar rules_text: Rules text
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    rules_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RulesText",
            type="Element"
        )
    )


@dataclass
class SearchSpecificAirSegment:
    """
    :ivar departure_time: The date and time at which this entity departs.
                        This does not include time zone information since it can be derived
                        from the origin location.
    :ivar carrier: The carrier that is marketing this segment
    :ivar flight_number: The flight number under which the marketing
                        carrier is marketing this flight
    :ivar origin: The IATA location code for this origination of
                        this entity.
    :ivar destination: The IATA location code for this destination of
                        this entity.
    :ivar segment_index: The sequential AirSegment number that this segment
                        connected to.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    departure_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            required=True
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            length=2
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            required=True,
            max_length=5
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    segment_index: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SegmentIndex",
            type="Attribute"
        )
    )


@dataclass
class SeatInformation:
    """Additional information about seats. Providers: 1G, 1V, 1P, 1J,ACH.

    :ivar power: Detail about any electrical power the seat might have. For example: No Power Providers: 1G, 1V, 1P, 1J
    :ivar video: Detail about any video components the seat might have. For example: No Video Providers: 1G, 1V, 1P, 1J
    :ivar type: Detail about the type of seat. For example: Exit Row, Standard, etc. Providers: 1G, 1V, 1P, 1J
    :ivar description: Detailed description of the seat. Providers: 1G, 1V, 1P, 1J
    :ivar rating: Definition of the seat rating. Providers: 1G, 1V, 1P, 1J
    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    power: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Power",
            type="Element",
            required=True
        )
    )
    video: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Video",
            type="Element",
            required=True
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Element",
            required=True
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Element",
            required=True
        )
    )
    rating: Optional["SeatInformation.Rating"] = field(
        default=None,
        metadata=dict(
            name="Rating",
            type="Element",
            required=True
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class Rating:
        """
        :ivar value:
        :ivar number: Numerical rating of the seat from 1 to 5 with 1 being bad and 5 being good. Providers: 1G, 1V, 1P, 1J
        """
        value: Optional[str] = field(
            default=None,
        )
        number: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Number",
                type="Attribute",
                required=True
            )
        )


@dataclass
class SegmentIndex:
    """Identifies the segment that is part of this group.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ServiceSubGroup:
    """The Service Sub Group of the Ancillary Service.  Providers: 1G, 1V, 1P, 1J,
    ACH.

    :ivar code: The Service Sub Group Code of the Ancillary Service.  Providers: 1G, 1V, 1P, 1J, ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute"
        )
    )


@dataclass
class SpecificSeatAssignment:
    """Request object used to specify a specific seat.

    :ivar booking_traveler_ref: The passenger that this seat assignment is for
    :ivar segment_ref: The segment that we will assign this seat on
    :ivar flight_detail_ref: The Flight Detail ref of the AirSegment used
                            when requesting seats on Change of Guage flights
    :ivar seat_id: The actual seat ID that is being requested.
                            Special Characters are not supported in this field.
    :ivar rail_coach_number: Coach number for which rail seatmap/coachmap is returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            required=True
        )
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            required=True
        )
    )
    flight_detail_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightDetailRef",
            type="Attribute"
        )
    )
    seat_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SeatId",
            type="Attribute",
            required=True
        )
    )
    rail_coach_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RailCoachNumber",
            type="Attribute",
            max_length=4
        )
    )


@dataclass
class SplitTicketingSearch:
    """SplitTicketingSearch is optional. Used to return both One-Way and Roundtrip
    fares in a single search response. Applicable to 1G, 1V, 1P only, the price
    points results path, and a simple roundtrip search only. Cannot be used in
    combination with Flex options.

    :ivar round_trip: Percentage of Roundtrip price points to be returned in the search response. This should be an even number. The One-Way price points returned in the response would be evenly distributed between the outbound and the inbound.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    round_trip: Optional[int] = field(
        default=None,
        metadata=dict(
            name="RoundTrip",
            type="Attribute"
        )
    )


@dataclass
class SponsoredFltInfo:
    """This describes whether the segment is determined to be a sponsored flight.
    The SponsoredFltInfo node will only come back for Travelport UIs and not for
    other customers.

    :ivar sponsored_lnb: The line number of the sponsored flight item
    :ivar neutral_lnb: The neutral line number for the flight item.
    :ivar flt_key: The unique identifying key for the sponsored flight.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    sponsored_lnb: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SponsoredLNB",
            type="Attribute",
            required=True
        )
    )
    neutral_lnb: Optional[int] = field(
        default=None,
        metadata=dict(
            name="NeutralLNB",
            type="Attribute",
            required=True
        )
    )
    flt_key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FltKey",
            type="Attribute",
            required=True,
            max_length=5
        )
    )


@dataclass
class SvcSegment:
    """Service segment added to collect additional fee. 1P only.

    :ivar key: The Key of SVC Segment.
    :ivar carrier: The platting carrier
    :ivar status:
    :ivar number_of_items:
    :ivar origin: Origin location - Airport code. 1P only.
    :ivar destination: Destination location - Airport code. 1P only.
    :ivar start_date: Start date of the segment. Generally it is the
                                                    next date after the last air segment. 1P only
    :ivar travel_order: To identify the appropriate travel sequence for
                                                    Air/Car/Hotel/Passive segments/reservations based on travel dates.
                                                    This ordering is applicable across the UR not provider or traveler
                                                    specific
    :ivar booking_traveler_ref:
    :ivar rfic: 1P - Reason for issuance
    :ivar rfisc: 1P - Resaon for issuance sub-code
    :ivar svc_description: 1P - SVC fee description
    :ivar fee: The fee to be collected using SVC segment
    :ivar emdnumber: Generated EMD number, if EMD is issued on the SVC
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            length=2
        )
    )
    status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute"
        )
    )
    number_of_items: Optional[int] = field(
        default=None,
        metadata=dict(
            name="NumberOfItems",
            type="Attribute"
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    start_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute"
        )
    )
    travel_order: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TravelOrder",
            type="Attribute"
        )
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute"
        )
    )
    rfic: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RFIC",
            type="Attribute"
        )
    )
    rfisc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RFISC",
            type="Attribute"
        )
    )
    svc_description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SvcDescription",
            type="Attribute"
        )
    )
    fee: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Fee",
            type="Attribute"
        )
    )
    emdnumber: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EMDNumber",
            type="Attribute",
            length=13
        )
    )


@dataclass
class Tax:
    """Taxes for Land Charges.

    :ivar category: The tax category represents a valid IATA tax code.
    :ivar amount:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    category: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute"
        )
    )
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TextInfo:
    """Information on baggage as published by carrier.

    :ivar text:
    :ivar title:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=0,
            max_occurs=999,
            max_length=250
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Title",
            type="Attribute"
        )
    )


@dataclass
class TicketAgency:
    """This modifier will override the pseudo of the ticketing agency found in the
    AAT (TKAG). Used for all plating carrier validation.

    :ivar provider_code: The code of the Provider (e.g. 1G, 1P)
    :ivar pseudo_city_code: The PCC of the host system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True
        )
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TicketDesignator:
    """Ticket Designator used to further qualify a Fare Basis Code.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True,
            min_length=0,
            max_length=20
        )
    )


@dataclass
class TicketEndorsement:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=256
        )
    )


@dataclass
class TicketValidity:
    """To be used to pass the selected segment.

    :ivar not_valid_before: Fare not valid before this date.
    :ivar not_valid_after: Fare not valid after this date.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    not_valid_before: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NotValidBefore",
            type="Attribute"
        )
    )
    not_valid_after: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NotValidAfter",
            type="Attribute"
        )
    )


@dataclass
class TicketingModifiersRef:
    """Reference to a shared list of Ticketing Modifers.

    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TourCode:
    """Tour Code Fare Basis.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True,
            max_length=15
        )
    )


@dataclass
class TravelArranger:
    """Details of Travel Arranger.

    :ivar value:
    :ivar company_short_name: Company Name
    :ivar code: IATA Code for Arranger
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    company_short_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CompanyShortName",
            type="Attribute"
        )
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute"
        )
    )


@dataclass
class Url:
    """
    :ivar value:
    :ivar type:
    """
    class Meta:
        name = "URL"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )


@dataclass
class Urlinfo:
    """Contains the text and URL of baggage as published by carrier.

    :ivar text:
    :ivar url:
    """
    class Meta:
        name = "URLInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=0,
            max_occurs=999,
            max_length=250
        )
    )
    url: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="URL",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class UpsellBrand:
    """Upsell brand reference.

    :ivar fare_basis:
    :ivar fare_info_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_basis: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute"
        )
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute"
        )
    )


@dataclass
class ValueDetails:
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
            type="Attribute",
            required=True
        )
    )


@dataclass
class VoidDocumentInfo:
    """Container to represent document information.

    :ivar document_number: Identifies the document number to be voided.
    :ivar document_type: Identifies the document type to be voided, Document Type can have four values like Service Fee, Paper Ticket , MCO and E-Ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    document_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocumentNumber",
            type="Attribute",
            min_length=1,
            max_length=13
        )
    )
    document_type: Optional["VoidDocumentInfo.DocumentType"] = field(
        default=None,
        metadata=dict(
            name="DocumentType",
            type="Attribute"
        )
    )

    class DocumentType(Enum):
        """
        :cvar SERVICE_FEE:
        :cvar PAPER_TICKET:
        :cvar MCO:
        :cvar E_TICKET:
        """
        SERVICE_FEE = "Service Fee"
        PAPER_TICKET = "Paper Ticket"
        MCO = "MCO"
        E_TICKET = "E-Ticket"


@dataclass
class VoidFailureInfo:
    """
    :ivar value:
    :ivar ticket_number:
    :ivar code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            required=True
        )
    )
    code: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute"
        )
    )


@dataclass
class VoidResultInfo:
    """List of Successful Or Failed void document results.

    :ivar failure_remark: Container to show all provider failure information.
    :ivar document_number: Identifies the document number to be voided.
    :ivar document_type: Identifies the document type to be voided, Document Type can have four values like Service Fee, Paper Ticket , MCO and E-Ticket.
    :ivar result_type: Successful Or Failed result indicator.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    failure_remark: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FailureRemark",
            type="Element"
        )
    )
    document_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocumentNumber",
            type="Attribute",
            min_length=1,
            max_length=13
        )
    )
    document_type: Optional["VoidResultInfo.DocumentType"] = field(
        default=None,
        metadata=dict(
            name="DocumentType",
            type="Attribute"
        )
    )
    result_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ResultType",
            type="Attribute"
        )
    )

    class DocumentType(Enum):
        """
        :cvar SERVICE_FEE:
        :cvar PAPER_TICKET:
        :cvar MCO:
        :cvar E_TICKET:
        """
        SERVICE_FEE = "Service Fee"
        PAPER_TICKET = "Paper Ticket"
        MCO = "MCO"
        E_TICKET = "E-Ticket"


@dataclass
class WaiverCode:
    """Waiver code to override fare validations.

    :ivar tour_code:
    :ivar ticket_designator:
    :ivar endorsement: Endorsement. Size can be up to 100
                            characters
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    tour_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Attribute",
            max_length=15
        )
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketDesignator",
            type="Attribute",
            min_length=0,
            max_length=20
        )
    )
    endorsement: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Endorsement",
            type="Attribute",
            min_length=0,
            max_length=100
        )
    )


@dataclass
class YieldType:
    """An identifier which identifies yield made on original pricing. It can be a
    flat amount of original price. The value of Amount can be negative. Negative
    value implies a discount.

    :ivar amount: Yield per passenger level in Default
                            Currency for this entity.
    :ivar booking_traveler_ref: Reference to a booking traveler for which Yield is applied.
    """
    class Meta:
        name = "Yield"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute"
        )
    )


class TypeAtpcoglobalIndicator(Enum):
    """Enumeration of ATPCO global indicators.

    :cvar AL: FareByRule -- All fares incl. EH/TS
    :cvar AP: Via Atlantic Pacific
    :cvar AT: Via Atlantic
    :cvar CA: Within Canada.
    :cvar CT: Circle trip.
    :cvar EH: Within Eastern Hemisphere
    :cvar FE: Far East
    :cvar IN_VALUE: FareByRule - For int'l incl.
                            AT/PA/WH/CT/RW
    :cvar NA: FareByRule for North America incl
                            US/CA/TB/PV
    :cvar PA: Via Pacific
    :cvar PN: Via Pacific and via North America
    :cvar PO: Via Polar Route.
    :cvar RU: Russia - Area 3
    :cvar RW: Round The World.
    :cvar SA: South Atlantic only
    :cvar SP: Via South Polar Route
    :cvar TB: Trans-border
    :cvar TS: Via Siberia.
    :cvar US: Within the United States.
    :cvar WH: Within Western Hemisphere
    :cvar ZZ: Any Global
    """
    AL = "AL"
    AP = "AP"
    AT = "AT"
    CA = "CA"
    CT = "CT"
    EH = "EH"
    FE = "FE"
    IN_VALUE = "IN"
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
    """
    :cvar STAR_ALLIANCE:
    :cvar ONE_WORLD:
    :cvar KLMNORTHWEST_ALLIANCE:
    :cvar SKY_TEAM:
    :cvar OWCODE:
    """
    STAR_ALLIANCE = "StarAlliance"
    ONE_WORLD = "OneWorld"
    KLMNORTHWEST_ALLIANCE = "KLMNorthwestAlliance"
    SKY_TEAM = "SkyTeam"
    OWCODE = "OWCode"


@dataclass
class TypeAnchorFlightData:
    """To support Anchor flight search contain the anchor flight details. Supported
    providers 1P, 1J.

    :ivar airline_code: Indicates Anchor flight carrier code
    :ivar flight_number: Indicates Anchor flight number
    :ivar connection_indicator: Indicates that the Anchor flight has any connecting flight or not
    """
    class Meta:
        name = "typeAnchorFlightData"

    airline_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirlineCode",
            type="Attribute",
            required=True,
            length=2
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            required=True,
            max_length=5
        )
    )
    connection_indicator: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ConnectionIndicator",
            type="Attribute"
        )
    )


@dataclass
class TypeApplicableSegment:
    """
    :ivar key:
    :ivar air_itinerary_details_ref:
    :ivar booking_counts: Classes of service and their counts.
    """
    class Meta:
        name = "typeApplicableSegment"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    air_itinerary_details_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirItineraryDetailsRef",
            type="Attribute"
        )
    )
    booking_counts: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingCounts",
            type="Attribute"
        )
    )


class TypeAssessIndicator(Enum):
    """The type of AssessIndicator.

    :cvar MILEAGE_AND_CURRENCY:
    :cvar MILEAGE_OR_CURRENCY:
    """
    MILEAGE_AND_CURRENCY = "MileageAndCurrency"
    MILEAGE_OR_CURRENCY = "MileageOrCurrency"


class TypeBackOffice(Enum):
    """
    :cvar ACCOUNTING:
    :cvar GLOBAL_VALUE:
    :cvar NON_ACCOUNTING:
    :cvar NON_ACCOUNTING_REMOTE:
    :cvar DUAL:
    """
    ACCOUNTING = "Accounting"
    GLOBAL_VALUE = "Global"
    NON_ACCOUNTING = "NonAccounting"
    NON_ACCOUNTING_REMOTE = "NonAccountingRemote"
    DUAL = "Dual"


class TypeBillingDetailsDataType(Enum):
    """
    :cvar ALPHA:
    :cvar NUMERIC:
    :cvar ALPHA_NUMERIC:
    :cvar DATE:
    """
    ALPHA = "Alpha"
    NUMERIC = "Numeric"
    ALPHA_NUMERIC = "AlphaNumeric"
    DATE = "Date"


class TypeBillingDetailsName(Enum):
    """
    :cvar PERSONAL_ID:
    :cvar COST_ACCOUNT_NUMBER:
    :cvar ACCOUNT_NUMBER:
    :cvar PROJECT_NUMBER:
    :cvar ACTION_CODE:
    :cvar DEPARTMENT_CODE:
    :cvar ACCOUNTING_UNIT:
    :cvar ORDER_NUMBER:
    :cvar DESTINATION:
    :cvar FILE_DATE:
    """
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
    """Type of booking.

    :cvar SSR:
    :cvar AUXILLARY_SEGMENT:
    :cvar AVAILABLE_FOR_DISPLAY_PRICING:
    :cvar CONTACT_CARRIER_FOR_BOOKING:
    :cvar NO_BOOKING_REQUIRED:
    :cvar APPLY_BOOKING_PER_SERVICE:
    """
    SSR = "SSR"
    AUXILLARY_SEGMENT = "Auxillary Segment"
    AVAILABLE_FOR_DISPLAY_PRICING = "Available for Display/Pricing"
    CONTACT_CARRIER_FOR_BOOKING = "Contact Carrier for Booking"
    NO_BOOKING_REQUIRED = "No Booking Required"
    APPLY_BOOKING_PER_SERVICE = "Apply booking per service"


@dataclass
class TypeBulkTicketModifierType:
    """Bulk ticketing modifier type.

    :ivar suppress_on_fare_calc: Optional attribute to allow a modifier
                        impact such as Bulk Ticketing to have information suppressed on the
                        Fare Calc when generating supporting documents Check the specific
                        host system which may or may not support this function
    """
    class Meta:
        name = "typeBulkTicketModifierType"

    suppress_on_fare_calc: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="SuppressOnFareCalc",
            type="Attribute"
        )
    )


class TypeCarrierCode(Enum):
    """Defines the type of booking codes (Primary or Secondary)

    :cvar PRIMARY:
    :cvar SECONDARY:
    """
    PRIMARY = "Primary"
    SECONDARY = "Secondary"


class TypeConnectionIndicator(Enum):
    """
    Types of connection indicator :
                         AvailabilityAndPricing : Specified availability and pricing connection;
                         TurnAround : Specified turn around;
                         Stopover : Specified stopover;
    :cvar AVAILABILITY_AND_PRICING:
    :cvar TURN_AROUND:
    :cvar STOPOVER:
    """
    AVAILABILITY_AND_PRICING = "AvailabilityAndPricing"
    TURN_AROUND = "TurnAround"
    STOPOVER = "Stopover"


class TypeCouponStatus(Enum):
    """ATA/IATA Standard coupon status.

    :cvar A: Code="A" Status="Airport Controlled".
    :cvar C: Code="C" Status="Checked In"
    :cvar F: Code="F" Status="Flown/Used"
    :cvar L: Code="L" Status="Boarded/Lifted"
    :cvar O: Code="O" Status="Open"
    :cvar P: Code="P" Status="Printed"
    :cvar R: Code="R" Status="Refunded"
    :cvar E: Code="E" Status="Exchanged"
    :cvar V: Code="V" Status="Void"
    :cvar Z: Code="Z" Status="Archived/Carrier
                            Modified"
    :cvar U: Code="U" Status="Unavailable"
    :cvar S: Code="S" Status="Suspended"
    :cvar I: Code="I" Status="Irregular Ops"
    :cvar D: Code="D" "Deleted/Removed"
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
    """
    :ivar mon:
    :ivar tue:
    :ivar wed:
    :ivar thu:
    :ivar fri:
    :ivar sat:
    :ivar sun:
    """
    class Meta:
        name = "typeDaysOfOperation"

    mon: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Mon",
            type="Attribute"
        )
    )
    tue: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Tue",
            type="Attribute"
        )
    )
    wed: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Wed",
            type="Attribute"
        )
    )
    thu: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Thu",
            type="Attribute"
        )
    )
    fri: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Fri",
            type="Attribute"
        )
    )
    sat: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Sat",
            type="Attribute"
        )
    )
    sun: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Sun",
            type="Attribute"
        )
    )


class TypeDestinationCode(Enum):
    """List of valid Destination Codes.

    :cvar MEXICO_COST_RICA_CENTRAL_AMERICA: Mexico/Central America/Canal
                            Zone/Costa Rica
    :cvar CARIBBEAN: Island and Countries of The Caribbean
    :cvar SOUTH_AMERICA: South America
    :cvar EUROPE: Europe
    :cvar AFRICA: Africa
    :cvar MIDDLE_EAST_WESTERN_ASIA: Middle East/Western Asia
    :cvar ASIA: Asia
    :cvar AUSTRALIA_NEW_ZEALAND_PACIFIC_ISLANDS: Australia/New Zealand/Pacific Islands
    :cvar CANADA_GREENLAND: Canada and Greenland
    :cvar USA: United States of America
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
    """Type of booking.

    :cvar WITH_ITINERARY_PRICING:
    :cvar STORE:
    :cvar SPECIAL_SERVICE:
    """
    WITH_ITINERARY_PRICING = "With Itinerary Pricing"
    STORE = "Store"
    SPECIAL_SERVICE = "SpecialService"


class TypeDiversity(Enum):
    """Used in Low Fare Search to better promote unique results.

    :cvar BLEND:
    :cvar AIRPORTS:
    :cvar CARRIER:
    :cvar ORIGIN:
    :cvar DESTINATION:
    :cvar DATE_COMBINATION:
    :cvar FIRST_ODDATE:
    :cvar SECOND_ODDATE:
    :cvar FIRST_OD:
    :cvar SECOND_OD:
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
    """Defines the ability to eticket an entity (Yes, No, Required, Ticketless)

    :cvar YES:
    :cvar NO:
    :cvar REQUIRED:
    :cvar TICKETLESS:
    """
    YES = "Yes"
    NO = "No"
    REQUIRED = "Required"
    TICKETLESS = "Ticketless"


class TypeFacility(Enum):
    """
    :cvar SEAT:
    :cvar AISLE:
    :cvar OPEN:
    :cvar UNKNOWN:
    """
    SEAT = "Seat"
    AISLE = "Aisle"
    OPEN = "Open"
    UNKNOWN = "Unknown"


@dataclass
class TypeFailureInfo:
    """
    :ivar code:
    :ivar message:
    """
    class Meta:
        name = "typeFailureInfo"

    code: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )
    message: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute",
            required=True
        )
    )


class TypeFareBreak(Enum):
    """Types of fare break.

    :cvar MUST_BREAK: Break Fare at the associated segment.
                            Multiple Breaks or No Breaks may be allowed.
    :cvar MUST_ONLY_BREAK: Only Break Fare at the associated segment.
                            Fare Break in the entire itinerary is allowed only at the
                            concerned segment.
    :cvar MUST_NOT_BREAK: No Fare Break allowed at the associated
                            segment.
    """
    MUST_BREAK = "MustBreak"
    MUST_ONLY_BREAK = "MustOnlyBreak"
    MUST_NOT_BREAK = "MustNotBreak"


class TypeFareDirectionality(Enum):
    """A fare's directionality (e.g. one-way, return )

    :cvar OUTBOUND:
    :cvar RETURN_VALUE:
    :cvar ALL:
    """
    OUTBOUND = "Outbound"
    RETURN_VALUE = "Return"
    ALL = "All"


class TypeFareDiscount(Enum):
    """Fare Discount Calculation Method.

    :cvar BASE_RE_CALC_USTAXES:
    :cvar BASE_NO_RE_CALC_USTAXES:
    :cvar BASE_TAX:
    """
    BASE_RE_CALC_USTAXES = "BaseReCalcUSTaxes"
    BASE_NO_RE_CALC_USTAXES = "BaseNoReCalcUSTaxes"
    BASE_TAX = "BaseTax"


class TypeFareGuarantee(Enum):
    """The status of a fare.

    :cvar AUTO: Automatically generated
    :cvar MANUAL: Agent has overridden default(s)
    :cvar MANUAL_FARE: Fare has been constructed by agent
    :cvar GUARANTEED: Fare is guaranteed
    :cvar INVALID: Invalid fare, e.g. due to name or
                      itinerary change
    :cvar RESTORED: Ticketed stored fare has been restored
    :cvar TICKETED:
    :cvar UNTICKETABLE: Unable to ticket
    :cvar REPRICE: Need requote to ticket
    :cvar EXPIRED: Expired fare due to older fare guarantee date typically older than 7 days
    :cvar AUTO_USING_PRIVATE_FARE: Agency private fares that are not guaranteed
    :cvar GUARANTEED_USING_AIRLINE_PRIVATE_FARE: Guaranteed fare using Airline private fare that was filed with a fare distributor.
    :cvar AIRLINE: Fare guaranteed by Airline.
    :cvar GUARANTEE_EXPIRED: Guaranteed fare recently got expired as ticketing hadn't been done within a time frame typically midnight local time of POS .
    :cvar AGENCY_PRIVATE_FARE_NO_OVERRIDE: Agency Private Fare with no rules override
    :cvar UNKNOWN: To handle new enumerations added by provider but currently not recognized by API
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


@dataclass
class TypeFarePenalty:
    """Penalty applicable on a Fare for change/ cancellation etc- expressed in both
    Money and Percentage.

    :ivar amount: The penalty (if any) - expressed as the actual
                            amount of money. Both Amount and Percentage can be present.
    :ivar percentage: The penalty (if any) - expressed in
                            percentage. Both Amount and Percentage can be present.
    :ivar penalty_applies:
    :ivar no_show: The No Show penalty (if any) to change/cancel the fare.
    """
    class Meta:
        name = "typeFarePenalty"

    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    percentage: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Percentage",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            pattern=r"([0-9]{1,2}|100)\.[0-9]{1,2}"
        )
    )
    penalty_applies: Optional["TypeFarePenalty.PenaltyApplies"] = field(
        default=None,
        metadata=dict(
            name="PenaltyApplies",
            type="Attribute"
        )
    )
    no_show: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NoShow",
            type="Attribute"
        )
    )

    class PenaltyApplies(Enum):
        """The values can be "Anytime", "Before Departure" or "After Departure".

        :cvar ANYTIME:
        :cvar BEFORE_DEPARTURE:
        :cvar AFTER_DEPARTURE:
        """
        ANYTIME = "Anytime"
        BEFORE_DEPARTURE = "Before Departure"
        AFTER_DEPARTURE = "After Departure"


class TypeFareRestrictionType(Enum):
    """The type of fare restriction.

    :cvar DAY_OF_WEEK:
    :cvar FLIGHT_TIME_OF_DAY:
    :cvar BOTH:
    """
    DAY_OF_WEEK = "DayOfWeek"
    FLIGHT_TIME_OF_DAY = "FlightTimeOfDay"
    BOTH = "Both"


class TypeFareRuleCategoryCode(Enum):
    """Kestrel Long Fare Rule Category Codes.

    :cvar APP: Rule App/Other Conditions
    :cvar WHO: Eligibility
    :cvar DAY: Day/Time
    :cvar SEA: Seasonal
    :cvar FLT: Flight App
    :cvar ADV: Advance Res/Tkt
    :cvar MIN: Minimum Stay
    :cvar MAX: Maximum Stay
    :cvar STP: Stopovers
    :cvar TRF: Transfers/Routing
    :cvar CMB: Combinability
    :cvar BLA: Blackouts
    :cvar SUR: Surcharges
    :cvar ACC: Accompanied
    :cvar TVL: Travel Restrictions
    :cvar TKT: Sales Restrictions
    :cvar CHG: Penalties
    :cvar HIP: HIP and Mileage Exceptions
    :cvar END: Ticket Endorsements
    :cvar CHD: Children"s Discounts
    :cvar TUC: Tour Conductor Disc
    :cvar AGT: Agent Discounts
    :cvar DSC: All Other Disc
    :cvar MIS: Misc Fare Tags
    :cvar FBR: Fare By Rule
    :cvar GRP: Groups
    :cvar TUR: Tours
    :cvar VAC: Visit Another Country
    :cvar DEP: Deposits
    :cvar VOL: Voluntary Changes
    :cvar IVE: Involuntary Exchanges
    :cvar VOR: Voluntary Refunds
    :cvar IVR: Involuntary Refunds
    :cvar NET: Negotiated Fares
    :cvar OTH: Other
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
    """The valid rule types.

    :cvar NONE_VALUE:
    :cvar SHORT:
    :cvar LONG:
    """
    NONE_VALUE = "none"
    SHORT = "short"
    LONG = "long"


class TypeFareSearchOption(Enum):
    """Fare Search option indicator.

    :cvar LEAVE:
    :cvar RETURN_VALUE:
    :cvar SEASONAL:
    :cvar BLACKOUT:
    :cvar ADVANCE_PURCHASE:
    :cvar DAY_OF_WEEK:
    :cvar EFFECTIVE_DATE:
    """
    LEAVE = "Leave"
    RETURN_VALUE = "Return"
    SEASONAL = "Seasonal"
    BLACKOUT = "Blackout"
    ADVANCE_PURCHASE = "Advance Purchase"
    DAY_OF_WEEK = "Day-of-week"
    EFFECTIVE_DATE = "Effective Date"


class TypeFareStatusCode(Enum):
    """
    :cvar READY_TO_TICKET: Fare is enabled and available for ticketing
    :cvar UNABLE_TO_TICKET: Fare could not be ticketed
    :cvar REPRICE: Fare needs to be repriced
    :cvar TICKETED: Fare is ticketed
    :cvar UNABLE: Fare is not enabled
    :cvar UNKNOWN: To handle new enumerations added by provider but currently not recognized by API
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
    :cvar ONE_WAY:
    :cvar ONE_WAY_ONLY:
    :cvar RETURN_VALUE:
    :cvar RETURN_ONLY:
    :cvar HALF_RETURN:
    :cvar CIRCLE_TRIP:
    :cvar ROUND_THE_WORLD:
    """
    ONE_WAY = "OneWay"
    ONE_WAY_ONLY = "OneWayOnly"
    RETURN_VALUE = "Return"
    RETURN_ONLY = "ReturnOnly"
    HALF_RETURN = "HalfReturn"
    CIRCLE_TRIP = "CircleTrip"
    ROUND_THE_WORLD = "RoundTheWorld"


class TypeFaresIndicator(Enum):
    """Defines the type of fares to return (Only public fares, Only private fares,
    Only agency private fares, Only airline private fares or all fares)

    :cvar PUBLIC_FARES_ONLY:
    :cvar PRIVATE_FARES_ONLY:
    :cvar AGENCY_PRIVATE_FARES_ONLY:
    :cvar AIRLINE_PRIVATE_FARES_ONLY:
    :cvar PUBLIC_AND_PRIVATE_FARES:
    :cvar NET_FARES_ONLY:
    :cvar ALL_FARES: Applicable for 1G/1V air shop only
    """
    PUBLIC_FARES_ONLY = "PublicFaresOnly"
    PRIVATE_FARES_ONLY = "PrivateFaresOnly"
    AGENCY_PRIVATE_FARES_ONLY = "AgencyPrivateFaresOnly"
    AIRLINE_PRIVATE_FARES_ONLY = "AirlinePrivateFaresOnly"
    PUBLIC_AND_PRIVATE_FARES = "PublicAndPrivateFares"
    NET_FARES_ONLY = "NetFaresOnly"
    ALL_FARES = "AllFares"


class TypeIgnoreStopOver(Enum):
    """The stop over inluded to quote fare.

    :cvar NO_STOP_OVER: No Stop over included.
    :cvar STOP_OVER: Stop over included.
    :cvar IGNORE_SEGMENT: Segment Ignored.
    """
    NO_STOP_OVER = "NoStopOver"
    STOP_OVER = "StopOver"
    IGNORE_SEGMENT = "IgnoreSegment"


class TypeInventoryRequest(Enum):
    """
    The valid inventory types are Seamless - A, DirectAccess - B, Basic - C
    :cvar SEAMLESS:
    :cvar DIRECT_ACCESS:
    :cvar BASIC:
    """
    SEAMLESS = "Seamless"
    DIRECT_ACCESS = "DirectAccess"
    BASIC = "Basic"


class TypeItinerary(Enum):
    """
    :cvar INVOICE:
    :cvar POCKET:
    """
    INVOICE = "Invoice"
    POCKET = "Pocket"


class TypeItineraryOption(Enum):
    """
    :cvar NO_FARE:
    :cvar NO_AMOUNT:
    :cvar SEQUENCE_NUMBER:
    """
    NO_FARE = "NoFare"
    NO_AMOUNT = "NoAmount"
    SEQUENCE_NUMBER = "SequenceNumber"


class TypeMealService(Enum):
    """Available Meal Service.

    :cvar MEAL:
    :cvar COLD_MEAL:
    :cvar HOT_MEAL:
    :cvar BREAKFAST:
    :cvar CONTINENTAL_BREAKFAST:
    :cvar LUNCH:
    :cvar DINNER:
    :cvar SNACK_OR_BRUNCH:
    :cvar FOOD_FOR_PURCHASE:
    :cvar COMPLIMENTARY_REFRESHMENTS:
    :cvar ALCOHOLIC_BEVERAGES_FOR_PURCHASE:
    :cvar COMPLIMENTARY_ALCOHOLIC_BEVERAGES:
    :cvar FOOD_AND_BEVERAGES_FOR_PURCHASE:
    :cvar NO_MEAL_SERVICE:
    :cvar REFRESHMENTS_FOR_PURCHASE:
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
    """Whether the fare is Mile or Route based.

    :cvar MILE:
    :cvar ROUTE:
    :cvar BOTH:
    """
    MILE = "Mile"
    ROUTE = "Route"
    BOTH = "Both"


@dataclass
class TypeNativeSearchModifier:
    """
    :ivar value:
    :ivar provider_code: The host for which the NativeModfier being added to
    """
    class Meta:
        name = "typeNativeSearchModifier"

    value: Optional[str] = field(
        default=None,
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2,
            max_length=5
        )
    )


@dataclass
class TypeNonAirReservationRef:
    """
    :ivar locator_code:
    """
    class Meta:
        name = "typeNonAirReservationRef"

    locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LocatorCode",
            type="Attribute",
            required=True,
            min_length=5,
            max_length=8
        )
    )


class TypePosition(Enum):
    """Facility position with respect to position within the aircraft cabin.
    Possible values are – Left, Right, Center, Left Center, Right Center.

    :cvar LEFT:
    :cvar RIGHT:
    :cvar CENTER:
    :cvar LEFT_CENTER:
    :cvar RIGHT_CENTER:
    """
    LEFT = "Left"
    RIGHT = "Right"
    CENTER = "Center"
    LEFT_CENTER = "LeftCenter"
    RIGHT_CENTER = "RightCenter"


class TypePricingMethod(Enum):
    """The method at which the pricing data was acquired.

    :cvar AUTO: Automatically generated
    :cvar MANUAL: Agent has overridden default(s)
    :cvar MANUAL_FARE: Fare has been constructed by agent
    :cvar GUARANTEED: Fare is guaranteed
    :cvar INVALID: Invalid fare, e.g. due to name or
                      itinerary change
    :cvar RESTORED: Ticketed stored fare has been restored
    :cvar TICKETED:
    :cvar UNTICKETABLE: Unable to ticket
    :cvar REPRICE: Need requote to ticket
    :cvar EXPIRED: Expired fare, older than 7 days
    :cvar AUTO_USING_PRIVATE_FARE: Agency private fares that are not guaranteed
    :cvar GUARANTEED_USING_AIRLINE_PRIVATE_FARE: Guaranteed fare using Airline private fare that was filed with a fare distributor.
    :cvar AIRLINE: Fare created as a result of Claim PNR which transfers data to GDS for ticketing purposes.
    :cvar AGENT_ASSISTED: Fare is created using Agent Asisted Pricing.
    Worldspan TKG FAX Line Documentation - AGENT ASSISTEDPRICED
    :cvar VERIFY_PRICE: Verify existing saved price on PNR .
    Worldspan TKG FAX Line Documentation -  AWAITING PRICE VERIFICATION
    :cvar ALT_SEGMENT_REMOVED_REPRICE: ALT Segment removed, Reprice pricing.
    Worldspan TKG FAX Line Documentation - AWAITING REPRICING ALT SEGS RMVD
    :cvar AUXILIARY_SEGMENT_REMOVED_REPRICE: AUX Segment removed, Reprice pricing.
    Worldspan TKG FAX Line Documentation -  AWAITING REPRICING AUX SEGS REMOVED
    :cvar DUPLICATE_SEGMENT_REMOVED_REPRICE: Duplicate Segment removed, Reprice pricing.
    Worldspan TKG FAX Line Documentation - AWAITING REPRICING DUPE SEGS REMOVED
    :cvar UNKNOWN: Any other kind of Pricing Method which is not supported by API.
    :cvar GUARANTEED_USING_AGENCY_PRIVATE_FARE: Guaranteed fare using Agency private fare that was filed with a fare distributor.
    :cvar AUTO_RAPID_REPRICE: Auto priced by rapid reprice. Provider 1P FCI code 4 .
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
    """List the types of private fares, Agency private fare, Airline private Fare
    and Unknown. Also, this enumaration list includes PrivateFare to indetify
    private fares for GDSs where we can not identify specific private fares.

    :cvar UNKNOWN_TYPE:
    :cvar PRIVATE_FARE:
    :cvar AGENCY_PRIVATE_FARE:
    :cvar AIRLINE_PRIVATE_FARE:
    """
    UNKNOWN_TYPE = "UnknownType"
    PRIVATE_FARE = "PrivateFare"
    AGENCY_PRIVATE_FARE = "AgencyPrivateFare"
    AIRLINE_PRIVATE_FARE = "AirlinePrivateFare"


class TypePurposeCode(Enum):
    """List of valid Purpose Codes.

    :cvar BUSINESS: Business
    :cvar PLEASURE: Pleasure
    :cvar CHARTER_SERVICE: Charter Service
    """
    BUSINESS = "Business"
    PLEASURE = "Pleasure"
    CHARTER_SERVICE = "CharterService"


class TypeReportingType(Enum):
    """The valid reporting types.

    :cvar AVAILABILITY_FAILURE:
    :cvar PRICE_DISCREPANCIES:
    :cvar MARRIAGE_DISCREPANCIES:
    :cvar SUCCESS:
    :cvar SCHEDULE_DISCREPANCIES:
    """
    AVAILABILITY_FAILURE = "AvailabilityFailure"
    PRICE_DISCREPANCIES = "PriceDiscrepancies"
    MARRIAGE_DISCREPANCIES = "MarriageDiscrepancies"
    SUCCESS = "Success"
    SCHEDULE_DISCREPANCIES = "ScheduleDiscrepancies"


class TypeRowLocation(Enum):
    """Facility Position with respect to a Row. Possible values are Rear, Front.

    :cvar REAR:
    :cvar FRONT:
    """
    REAR = "Rear"
    FRONT = "Front"


class TypeSeatAvailability(Enum):
    """Seat availability info of a seat map.

    :cvar AVAILABLE:
    :cvar OCCUPIED:
    :cvar RESERVED:
    :cvar ADVANCED_BOARDING_PASS:
    :cvar INTERLINE_CHECKIN:
    :cvar CODESHARE:
    :cvar PROTECTED:
    :cvar PARTNER_AIRLINE:
    :cvar ADV_SEAT_SELECTION:
    :cvar BLOCKED:
    :cvar EXTRA:
    :cvar RBDRESTRICTION:
    :cvar GROUP:
    :cvar NO_SEAT:
    :cvar UNOCCUPIED_BUT_NOT_ELIGIBLE:
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
    """
    :ivar key:
    """
    class Meta:
        name = "typeSegmentRef"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


class TypeStayUnit(Enum):
    """Units for the Length of Stay.

    :cvar MINUTES:
    :cvar HOURS:
    :cvar DAYS:
    :cvar MONTHS:
    :cvar MONDAY:
    :cvar TUESDAY:
    :cvar WEDNESDAY:
    :cvar THURSDAY:
    :cvar FRIDAY:
    :cvar SATURDAY:
    :cvar SUNDAY:
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
    """
    :cvar UNKNOWN:
    :cvar CONFIRMED:
    :cvar REFUNDED:
    :cvar EXCHANGED:
    :cvar CANCELLED:
    :cvar PENDING:
    """
    UNKNOWN = "Unknown"
    CONFIRMED = "Confirmed"
    REFUNDED = "Refunded"
    EXCHANGED = "Exchanged"
    CANCELLED = "Cancelled"
    PENDING = "Pending"


@dataclass
class TypeTextElement:
    """
    :ivar value:
    :ivar type:
    :ivar language_code: ISO 639 two-character language codes are used to retrieve specific information in the requested language. For Rich Content and Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE, DECH can also be used. Only certain services support this attribute. Providers: ACH, RCH, 1G, 1V, 1P, 1J.
    """
    class Meta:
        name = "typeTextElement"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    language_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LanguageCode",
            type="Attribute"
        )
    )


@dataclass
class TypeTicketModifierAccountingType:
    """Ticketing Modifier used to add accounting.

                    - discount information.
    :ivar value:
    """
    class Meta:
        name = "typeTicketModifierAccountingType"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            required=True
        )
    )


@dataclass
class TypeTicketModifierAmountType:
    """Ticketing Modifier used to alter a fare amount before or during the
    ticketing operation.

    :ivar amount: Amount associated with a ticketing modifier
    """
    class Meta:
        name = "typeTicketModifierAmountType"

    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TypeTicketModifierPercentType:
    """Ticketing Modifier used to alter a fare percentage before or during the
    ticketing operation.

    :ivar percent: Percent associated with a ticketing
                        modifier
    """
    class Meta:
        name = "typeTicketModifierPercentType"

    percent: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Percent",
            type="Attribute",
            required=True,
            pattern=r"([0-9]{1,2}|100)\.[0-9]{1,2}"
        )
    )


@dataclass
class TypeTicketModifierValueType:
    """Ticketing Modifier used to add value discount information.

    :ivar value:
    :ivar net_fare_value: Treat the value as net fare discount
                        information
    """
    class Meta:
        name = "typeTicketModifierValueType"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            required=True
        )
    )
    net_fare_value: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NetFareValue",
            type="Attribute"
        )
    )


class TypeTripType(Enum):
    """Used in Low Fare Search to better target the results.

    :cvar CHEAPEST:
    :cvar QUICKEST:
    :cvar MOST_CONVENIENT:
    :cvar LEISURE:
    :cvar BUSINESS:
    :cvar LUXURY:
    :cvar PREFER_FIRST:
    :cvar BUSINESS_OR_FIRST:
    :cvar NO_PENALTY:
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
    :ivar value:
    :ivar unit: Unit values would be lb,Lb,kg etc.
    """
    class Meta:
        name = "typeUnitOfMeasure"

    value: Optional[float] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute"
        )
    )
    unit: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Unit",
            type="Attribute"
        )
    )


class TypeUnitWeight(Enum):
    """The available units of weight.

    :cvar KILOGRAMS:
    :cvar POUNDS:
    """
    KILOGRAMS = "Kilograms"
    POUNDS = "Pounds"


class TypeVarianceIndicator(Enum):
    """Type code for Variance.

    :cvar EARLY:
    :cvar LATE:
    """
    EARLY = "Early"
    LATE = "Late"


class TypeVarianceType(Enum):
    """Type code for Variance.

    :cvar ACTUAL:
    :cvar ESTIMATED:
    :cvar CANCELED:
    :cvar DIVERSION:
    """
    ACTUAL = "Actual"
    ESTIMATED = "Estimated"
    CANCELED = "Canceled"
    DIVERSION = "Diversion"


@dataclass
class Apisrequirements:
    """Specific details for APIS Requirements.

    :ivar document:
    :ivar key: Unique identifier for this APIS
                            Requirements - use this key when a single APIS Requirements is
                            shared by multiple elements.
    :ivar level: Applicability level of the Document.
                            Required, Supported, API_Supported or Unknown
    :ivar gender_required:
    :ivar date_of_birth_required:
    :ivar required_documents: What are required documents for the APIS
                            Requirement. One, FirstAndOneOther or All
    :ivar nationality_required: Nationality of the traveler is required for booking for some suppliers.
    """
    class Meta:
        name = "APISRequirements"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    document: List[Document] = field(
        default_factory=list,
        metadata=dict(
            name="Document",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    level: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Level",
            type="Attribute"
        )
    )
    gender_required: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="GenderRequired",
            type="Attribute"
        )
    )
    date_of_birth_required: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DateOfBirthRequired",
            type="Attribute"
        )
    )
    required_documents: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RequiredDocuments",
            type="Attribute"
        )
    )
    nationality_required: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NationalityRequired",
            type="Attribute"
        )
    )


@dataclass
class Affiliations:
    """Affiliations related for pre pay profiles.

    :ivar travel_arranger:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    travel_arranger: List[TravelArranger] = field(
        default_factory=list,
        metadata=dict(
            name="TravelArranger",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirAvailInfo:
    """Matches class of service information with availability counts. Only provided
    on search results.

    :ivar booking_code_info:
    :ivar fare_token_info: Associates Fare with HostToken
    :ivar provider_code:
    :ivar host_token_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_code_info: List[BookingCodeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="BookingCodeInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_token_info: List["AirAvailInfo.FareTokenInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="FareTokenInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )
    host_token_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="HostTokenRef",
            type="Attribute"
        )
    )

    @dataclass
    class FareTokenInfo:
        """
        :ivar fare_info_ref:
        :ivar host_token_ref:
        """
        fare_info_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="FareInfoRef",
                type="Attribute",
                required=True
            )
        )
        host_token_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="HostTokenRef",
                type="Attribute",
                required=True
            )
        )


@dataclass
class AirBaseReq(BaseReq):
    """Context for Requests and Responses."""


@dataclass
class AirExchangeBundleTotal:
    """Total exchange and penalty information for one ticket number.

    :ivar air_exchange_info:
    :ivar penalty: Only used within an AirExchangeQuoteRsp
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_exchange_info: Optional[AirExchangeInfo] = field(
        default=None,
        metadata=dict(
            name="AirExchangeInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    penalty: List[CommonPenalty] = field(
        default_factory=list,
        metadata=dict(
            name="Penalty",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeEligibilityReq(BaseReq):
    """Request to determine if the fares in an itinerary are exchangeable.

    :ivar provider_reservation_info: Provider:1P - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged
    :ivar type: Type choices are "Detail" or "Summary"  Default will be Summary
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    provider_reservation_info: Optional["AirExchangeEligibilityReq.ProviderReservationInfo"] = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element",
            required=True
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )

    @dataclass
    class ProviderReservationInfo:
        """
        :ivar provider_code:
        :ivar provider_locator_code:
        """
        provider_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ProviderCode",
                type="Attribute",
                required=True,
                min_length=2,
                max_length=5
            )
        )
        provider_locator_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ProviderLocatorCode",
                type="Attribute",
                required=True,
                max_length=15
            )
        )


@dataclass
class AirExchangeModifiers:
    """Provides controls and switches for the Exchange process.

    :ivar contract_codes:
    :ivar booking_date:
    :ivar ticketing_date:
    :ivar account_code:
    :ivar ticket_designator:
    :ivar allow_penalty_fares:
    :ivar private_fares_only:
    :ivar universal_record_locator_code: Which UniversalRecord should this new reservation
                            be applied to. If blank, then a new one is created.
    :ivar provider_locator_code: Which Provider reservation does this reservation
                            get added to.
    :ivar provider_code: To be used with ProviderLocatorCode, which host
                            the
                            reservation being added to belongs to.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    contract_codes: Optional["AirExchangeModifiers.ContractCodes"] = field(
        default=None,
        metadata=dict(
            name="ContractCodes",
            type="Element"
        )
    )
    booking_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingDate",
            type="Attribute"
        )
    )
    ticketing_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingDate",
            type="Attribute"
        )
    )
    account_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute"
        )
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketDesignator",
            type="Attribute",
            min_length=0,
            max_length=20
        )
    )
    allow_penalty_fares: bool = field(
        default=True,
        metadata=dict(
            name="AllowPenaltyFares",
            type="Attribute"
        )
    )
    private_fares_only: bool = field(
        default=False,
        metadata=dict(
            name="PrivateFaresOnly",
            type="Attribute"
        )
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            min_length=5,
            max_length=8
        )
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            min_length=5,
            max_length=8
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute"
        )
    )

    @dataclass
    class ContractCodes:
        """
        :ivar contract_code:
        """
        contract_code: List[ContractCode] = field(
            default_factory=list,
            metadata=dict(
                name="ContractCode",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class AirExchangeTicketBundle:
    """
    :ivar ticket_number:
    :ivar form_of_payment:
    :ivar form_of_payment_ref:
    :ivar waiver_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: Optional[TicketNumber] = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=2
        )
    )
    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element"
        )
    )


@dataclass
class AirFareDiscount:
    """Fare Discounts.

    :ivar percentage:
    :ivar amount:
    :ivar discount_method:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    percentage: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Percentage",
            type="Attribute"
        )
    )
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    discount_method: Optional[TypeFareDiscount] = field(
        default=None,
        metadata=dict(
            name="DiscountMethod",
            type="Attribute"
        )
    )


@dataclass
class AirFareRuleCategory:
    """A collection of fare rule category codes.

    :ivar category_code: The Category Code for Air Fare Rule.
    :ivar fare_info_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    category_code: List[TypeFareRuleCategoryCode] = field(
        default_factory=list,
        metadata=dict(
            name="CategoryCode",
            type="Element",
            min_occurs=1,
            max_occurs=10
        )
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute"
        )
    )


@dataclass
class AirPrePayReq(BaseReq):
    """Flight Pass Request.

    :ivar list_search: Provider: ACH.
    :ivar pre_pay_retrieve: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    list_search: Optional["AirPrePayReq.ListSearch"] = field(
        default=None,
        metadata=dict(
            name="ListSearch",
            type="Element"
        )
    )
    pre_pay_retrieve: Optional["AirPrePayReq.PrePayRetrieve"] = field(
        default=None,
        metadata=dict(
            name="PrePayRetrieve",
            type="Element"
        )
    )

    @dataclass
    class ListSearch:
        """
        :ivar person_name_search: Customer name detail for searching flight pass content.
        :ivar loyalty_card: Customer loyalty card for searching flight pass content.
        :ivar start_from_result: Start index of the section of flight pass numbers that is being requested.
        :ivar max_results: Max Number of Flight Passes being requested for.
        """
        person_name_search: Optional[PersonNameSearch] = field(
            default=None,
            metadata=dict(
                name="PersonNameSearch",
                type="Element"
            )
        )
        loyalty_card: List[LoyaltyCard] = field(
            default_factory=list,
            metadata=dict(
                name="LoyaltyCard",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=0,
                max_occurs=999
            )
        )
        start_from_result: Optional[int] = field(
            default=None,
            metadata=dict(
                name="StartFromResult",
                type="Attribute",
                required=True,
                min_inclusive=1
            )
        )
        max_results: Optional[int] = field(
            default=None,
            metadata=dict(
                name="MaxResults",
                type="Attribute",
                required=True,
                min_inclusive=1,
                max_inclusive=200
            )
        )

    @dataclass
    class PrePayRetrieve:
        """
        :ivar id: Pre pay id to retrieved,example flight pass  number
        :ivar type: Pre pay id type,example 'FlightPass'
        """
        id: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Id",
                type="Attribute",
                required=True,
                min_length=1,
                max_length=36
            )
        )
        type: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Type",
                type="Attribute"
            )
        )


@dataclass
class AirPricingAdjustment:
    """This is a container to adjust price of AirPricingInfo. Pass zero values to
    remove existing adjustment.

    :ivar adjustment:
    :ivar key: Key of AirPricingInfo from booking.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    adjustment: Optional[Adjustment] = field(
        default=None,
        metadata=dict(
            name="Adjustment",
            type="Element",
            required=True
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AirPricingPayment:
    """
    AirPricing Payment information - used to
                    associate a FormOfPayment withiin the UR with one or more
                    AirPricingInfos
    :ivar payment:
    :ivar form_of_payment:
    :ivar form_of_payment_ref:
    :ivar air_pricing_info_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirRefundInfo:
    """Provides results of a refund quote.

    :ivar refund_remark:
    :ivar refund_amount:
    :ivar retain_amount:
    :ivar refund_fee: Refund fee for ACH/1P
    :ivar refundable_taxes: 1P - None : All taxes are not refundable.
                                            Unknown : Refundability of taxes are not known.
    :ivar filed_currency: 1P  Currency of filed CAT33 refund fee
    :ivar conversion_rate: 1P - Currency conversion rate used for conversion
                                            between FiledCurrency and PCC base currency in which the response is
                                            returned.
    :ivar taxes: 1P - The total value of taxes.
    :ivar original_ticket_total: 1P - The original ticket amount.
    :ivar forfeit_amount:
    :ivar retain: This indicates whether any amount is retained by the provider.
    :ivar refund: This indicates whether carrier/host supports refund for the correcponding pnr.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    refund_remark: List[RefundRemark] = field(
        default_factory=list,
        metadata=dict(
            name="RefundRemark",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    refund_amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RefundAmount",
            type="Attribute"
        )
    )
    retain_amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RetainAmount",
            type="Attribute"
        )
    )
    refund_fee: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RefundFee",
            type="Attribute"
        )
    )
    refundable_taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RefundableTaxes",
            type="Attribute"
        )
    )
    filed_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FiledCurrency",
            type="Attribute",
            length=3
        )
    )
    conversion_rate: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="ConversionRate",
            type="Attribute"
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    original_ticket_total: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OriginalTicketTotal",
            type="Attribute"
        )
    )
    forfeit_amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ForfeitAmount",
            type="Attribute"
        )
    )
    retain: bool = field(
        default=False,
        metadata=dict(
            name="Retain",
            type="Attribute"
        )
    )
    refund: bool = field(
        default=False,
        metadata=dict(
            name="Refund",
            type="Attribute"
        )
    )


@dataclass
class AirRefundQuoteReq(BaseReq):
    """Request to quote a refund for an itinerary.

    :ivar ticket_number: Provider: ACH.
    :ivar tcrnumber: Provider: ACH-The identifying number for a Ticketless Air Reservation
    :ivar air_refund_modifiers: Provider: ACH.
    :ivar host_token: Provider: ACH.
    :ivar provider_reservation_info: Provider: 1P - Represents a valid Provider Reservation/PNR whose itinerary is to be requested
    :ivar ignore: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TCRNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_refund_modifiers: Optional[AirRefundModifiers] = field(
        default=None,
        metadata=dict(
            name="AirRefundModifiers",
            type="Element"
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info: List["AirRefundQuoteReq.ProviderReservationInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ignore: bool = field(
        default=False,
        metadata=dict(
            name="Ignore",
            type="Attribute"
        )
    )

    @dataclass
    class ProviderReservationInfo:
        """
        :ivar provider_code:
        :ivar provider_locator_code:
        """
        provider_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ProviderCode",
                type="Attribute",
                required=True,
                min_length=2,
                max_length=5
            )
        )
        provider_locator_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ProviderLocatorCode",
                type="Attribute",
                required=True,
                max_length=15
            )
        )


@dataclass
class AirRetrieveDocumentReq(BaseReq):
    """Retrieve the post booking information for a PNR. ETRs will be returned for
    standard carriers. TCRs will be returned for Ticketless carriers. If the
    locator is send on a standard carrier, all ETRs will be retrieved.

    :ivar air_reservation_locator_code: Provider: 1G,1V,1P,1J.
    :ivar ticket_number: Provider: 1G,1V,1P,1J.
    :ivar tcrnumber: Provider: 1G,1V,1P,1J-The identifying number for a Ticketless Air Reservation.
    :ivar return_restrictions: Will return a response which includes a set of restrictions associated with the document.
    :ivar return_pricing: Provider: 1G,1V,1P,1J-Will return a response which includes the pricing associated with the ETR.
    :ivar retrieve_mco: When true, returns MCO Information. The default value is false.
    :ivar universal_record_locator_code: Contains the Locator Code of the Universal Record that houses this reservation.
    :ivar provider_code: Contains the Provider Code of the provider that houses this reservation.
    :ivar provider_locator_code: Contains the Locator Code of the Provider Reservation that houses this reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[AirReservationLocatorCode] = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element"
        )
    )
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TCRNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    return_restrictions: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ReturnRestrictions",
            type="Attribute"
        )
    )
    return_pricing: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ReturnPricing",
            type="Attribute"
        )
    )
    retrieve_mco: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="RetrieveMCO",
            type="Attribute"
        )
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            min_length=5,
            max_length=8
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            max_length=15
        )
    )


@dataclass
class AirSegmentDetails:
    """An Air marketable travel segment.

    :ivar passenger_details_ref:
    :ivar brand_id:
    :ivar booking_code_list: Lists classes of service and their counts separated by delimiter |.
    :ivar key:
    :ivar provider_code:
    :ivar carrier:
    :ivar origin: The IATA location code for this origination of this entity.
    :ivar destination: The IATA location code for this destination of this entity.
    :ivar departure_time: The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.
    :ivar arrival_time: The date and time at which this entity arrives at the destination. This does not include time zone information since it can be derived from the origin location.
    :ivar equipment:
    :ivar class_of_service:
    :ivar cabin_class:
    :ivar operating_carrier: The actual carrier that is operating the flight.
    :ivar flight_number: Flight Number for the Search Leg Detail.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    passenger_details_ref: List[PassengerDetailsRef] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerDetailsRef",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    brand_id: List[BrandId] = field(
        default_factory=list,
        metadata=dict(
            name="BrandID",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    booking_code_list: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingCodeList",
            type="Element"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2,
            max_length=5
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            length=2
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            required=True
        )
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute",
            required=True
        )
    )
    equipment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Equipment",
            type="Attribute",
            length=3
        )
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            min_length=1,
            max_length=2
        )
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute"
        )
    )
    operating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OperatingCarrier",
            type="Attribute",
            length=2
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            required=True,
            max_length=5
        )
    )


@dataclass
class AirSegmentPricingModifiers:
    """Specifies modifiers that a particular segment should be priced in. If this
    is used, then there must be one for each AirSegment in the AirItinerary.

    :ivar permitted_booking_codes:
    :ivar air_segment_ref:
    :ivar cabin_class:
    :ivar account_code:
    :ivar prohibit_advance_purchase_fares:
    :ivar prohibit_non_refundable_fares:
    :ivar prohibit_penalty_fares:
    :ivar fare_basis_code: The fare basis code to be used for pricing.
    :ivar fare_break: Fare break point modifier to instruct Fares
                            where it should or should not break the fare.
    :ivar connection_indicator: ConnectionIndicator attribute will be used to map connection indicators
                            AvailabilityAndPricing, TurnAround and Stopover. This attribute is for Wordspan/1P only.
    :ivar brand_tier: Modifier to price by specific brand tier number.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    permitted_booking_codes: Optional["AirSegmentPricingModifiers.PermittedBookingCodes"] = field(
        default=None,
        metadata=dict(
            name="PermittedBookingCodes",
            type="Element"
        )
    )
    air_segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Attribute"
        )
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute"
        )
    )
    account_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute"
        )
    )
    prohibit_advance_purchase_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitAdvancePurchaseFares",
            type="Attribute"
        )
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitNonRefundableFares",
            type="Attribute"
        )
    )
    prohibit_penalty_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitPenaltyFares",
            type="Attribute"
        )
    )
    fare_basis_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareBasisCode",
            type="Attribute"
        )
    )
    fare_break: Optional[TypeFareBreak] = field(
        default=None,
        metadata=dict(
            name="FareBreak",
            type="Attribute"
        )
    )
    connection_indicator: Optional[TypeConnectionIndicator] = field(
        default=None,
        metadata=dict(
            name="ConnectionIndicator",
            type="Attribute"
        )
    )
    brand_tier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandTier",
            type="Attribute",
            min_length=1,
            max_length=10
        )
    )

    @dataclass
    class PermittedBookingCodes:
        """
        :ivar booking_code:
        """
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata=dict(
                name="BookingCode",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class AirTicketingModifiers:
    """Modifiers used during ticketing.

    :ivar document_modifiers:
    :ivar air_pricing_info_ref:
    :ivar tour_code: Allows an agency to modify the tour code information during ticket issuance. Providers supported: Worldspan and JAL.
    :ivar ticket_endorsement: Allows an agency to add user defined
                                           ticketing endorsements in the ticket. Providers supported: Worldspan and JAL.
    :ivar commission: Allows an agency to add the commission
                                           to a new or different commission rate which will be applied at
                                           time of ticketing. The commission Modifier allows the user
                                           specify how the commission change is to applied. Providers supported: Worldspan and JAL.
    :ivar form_of_payment: FormOfPayment information to be used as ticketing modifier at the time of ticketing. Providers supported: Galileo, Apollo, Worldspan and JAL.
    :ivar credit_card_auth: CreditCardAuth information to be used as ticketing modifier at the time of ticketing. Providers supported: Galileo, Apollo, Worldspan and JAL.
    :ivar payment: Provide Payment for FOP. Providers supported: Galileo, Apollo, Worldspan and JAL.
    :ivar plating_carrier: The Plating Carrier used for this ticket
    :ivar ticketed_fare_override: It is a modifier to allow re-issuance of tickets for stored fares which are already ticketed. Providers supported are 1P/1J
    :ivar suppress_tax_and_fee: Allow to suppress Taxand Fee in ticketing response.Providers supported: Worldspan and JAL.
    :ivar no_comparison_sfq: 1P/1J - Set to "true" to include the no comparison overide #NC to override the existing SFQ and issue the ticket. Only valid for AirTicketingReq, not valid  for AirExchangeTicketingReq.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    document_modifiers: Optional[DocumentModifiers] = field(
        default=None,
        metadata=dict(
            name="DocumentModifiers",
            type="Element"
        )
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tour_code: Optional[TourCode] = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Element"
        )
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata=dict(
            name="TicketEndorsement",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    commission: Optional[Commission] = field(
        default=None,
        metadata=dict(
            name="Commission",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata=dict(
            name="CreditCardAuth",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            length=2
        )
    )
    ticketed_fare_override: bool = field(
        default=False,
        metadata=dict(
            name="TicketedFareOverride",
            type="Attribute"
        )
    )
    suppress_tax_and_fee: bool = field(
        default=False,
        metadata=dict(
            name="SuppressTaxAndFee",
            type="Attribute"
        )
    )
    no_comparison_sfq: bool = field(
        default=False,
        metadata=dict(
            name="NoComparisonSFQ",
            type="Attribute"
        )
    )


@dataclass
class AirVoidDocumentReq(BaseReq):
    """Request to void all previously issued tickets for the PNR.

    :ivar air_reservation_locator_code: Provider: 1G,1V.
    :ivar void_document_info: Provider: 1G,1V-All tickets that belong to this PNR must be enumerated here. Voiding only some tickets of a multi-ticket PNR not currently supported.
    :ivar show_etr: Provider: 1G,1V-If set as true, response will display the detailed ETR for successfully voided E-Tickets.
    :ivar provider_code: Provider: 1G,1V-Provider code of a specific host.
    :ivar provider_locator_code: Provider: 1G,1V-Contains the locator of the host reservation.
    :ivar validate_spanish_residency: Provider: 1G - If set as true, Spanish Residency will be validated for
                                                                            Provisioned Customers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[AirReservationLocatorCode] = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element"
        )
    )
    void_document_info: List[VoidDocumentInfo] = field(
        default_factory=list,
        metadata=dict(
            name="VoidDocumentInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    show_etr: bool = field(
        default=False,
        metadata=dict(
            name="ShowETR",
            type="Attribute"
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute"
        )
    )
    validate_spanish_residency: bool = field(
        default=False,
        metadata=dict(
            name="ValidateSpanishResidency",
            type="Attribute"
        )
    )


@dataclass
class AlternateLocationDistance:
    """Information about the Original Search Airport to Alternate Search Airport.

    :ivar distance:
    :ivar key:
    :ivar search_location: The Searching City or Airport specified in the
                            Request.
    :ivar alternate_location: The nearby Alternate City or Airport to
                            SearchLocation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    distance: Optional[Distance] = field(
        default=None,
        metadata=dict(
            name="Distance",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    search_location: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SearchLocation",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    alternate_location: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AlternateLocation",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )


@dataclass
class ApplicableSegment(TypeApplicableSegment):
    """Applicable air segment."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AssociatedRemark(TypeAssociatedRemarkWithSegmentRef):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AsyncProviderSpecificResponse(BaseAsyncProviderSpecificResponse):
    """Identifies pending responses from a specific provider using MoreResults
    attribute."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AutoSeatAssignment:
    """Request object used to request seats automatically by seat type.

    :ivar segment_ref: The segment that this assignment belongs to
    :ivar smoking: Indicates that the requested seat type
                            should be a smoking seat.
    :ivar seat_type: The type of seat that is requested
    :ivar group: Indicates that this seat request is for
                            group seating for all passengers. If no SegmentRef is included,
                            group seating will be requested for all segments.
    :ivar booking_traveler_ref: The booking traveler that this seat assignment
                            is for. If not entered, this applies to the primary booking
                            traveler and other passengers are adjacent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )
    smoking: bool = field(
        default=False,
        metadata=dict(
            name="Smoking",
            type="Attribute"
        )
    )
    seat_type: Optional[TypeReqSeat] = field(
        default=None,
        metadata=dict(
            name="SeatType",
            type="Attribute",
            required=True
        )
    )
    group: bool = field(
        default=False,
        metadata=dict(
            name="Group",
            type="Attribute"
        )
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute"
        )
    )


@dataclass
class AvailableDiscount:
    """
    :ivar loyalty_program: Customer Loyalty Program Detail.
    :ivar amount:
    :ivar percent:
    :ivar description:
    :ivar discount_qualifier:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    loyalty_program: List[LoyaltyProgram] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyProgram",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    percent: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Percent",
            type="Attribute",
            pattern=r"([0-9]{1,2}|100)\.[0-9]{1,2}"
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute"
        )
    )
    discount_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DiscountQualifier",
            type="Attribute"
        )
    )


@dataclass
class AvailableSsr:
    """A wrapper for all the information regarding each of the available SSR.

    :ivar ssr:
    :ivar ssrrules: Holds the rules for selecting the SSR in
                                the itinerary
    :ivar industry_standard_ssr:
    """
    class Meta:
        name = "AvailableSSR"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ssr: List[Ssr] = field(
        default_factory=list,
        metadata=dict(
            name="SSR",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    ssrrules: List[ServiceRuleType] = field(
        default_factory=list,
        metadata=dict(
            name="SSRRules",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    industry_standard_ssr: List[IndustryStandardSsr] = field(
        default_factory=list,
        metadata=dict(
            name="IndustryStandardSSR",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class BackOfficeHandOff:
    """Allows an agency to select the back office documents and also route to
    different host to produce for the itinerary.

    :ivar type: The type of back office document,valid options
                            are Accounting,Global,NonAccounting,NonAccountingRemote,Dual.
    :ivar location: This is required for NonAccountingRemote,Dual
                            and Global type back office.
    :ivar pseudo_city_code: The PCC of the host system where it would be
                            routed.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[TypeBackOffice] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    location: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Location",
            type="Attribute"
        )
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=2,
            max_length=10
        )
    )


@dataclass
class BaseBaggageAllowanceInfo:
    """This contains common elements that are used for Baggage Allowance info,
    carry-on allowance info and embargo Info. Supported providers are 1V/1G/1P/1J.

    :ivar urlinfo: Contains the text and URL information as published by carrier.
    :ivar text_info: Text information as published by carrier.
    :ivar origin:
    :ivar destination:
    :ivar carrier:
    """
    urlinfo: List[Urlinfo] = field(
        default_factory=list,
        metadata=dict(
            name="URLInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    text_info: List[TextInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TextInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            length=2
        )
    )


@dataclass
class BillingDetailItem:
    """The Billing Details Information.

    :ivar name: Detailed Billing Information Name(e.g
                            Personal ID, Account Number)
    :ivar data_type: Detailed Billing Information DataType
                            (Alpha, Numeric, etc.)
    :ivar min_length: Detailed Billing Information Minimum
                            Length.
    :ivar max_length: Detailed Billing Information Maximum
                            Length.
    :ivar value: Detailed Billing Information Value
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    name: Optional[TypeBillingDetailsName] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            required=True
        )
    )
    data_type: Optional[TypeBillingDetailsDataType] = field(
        default=None,
        metadata=dict(
            name="DataType",
            type="Attribute",
            required=True
        )
    )
    min_length: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MinLength",
            type="Attribute",
            required=True
        )
    )
    max_length: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MaxLength",
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
class BundledService:
    """Displays the services bundled together.

    :ivar carrier: Carrier the service is applicable.
    :ivar carrier_sub_code: Carrier sub code. True means the carrier used their own sub code. False means the carrier used an ATPCO sub code
    :ivar service_type: The type of service or what the service is used for, e.g. F type is flight type, meaning the service is used on a flight
    :ivar service_sub_code: The sub code of the service, e.g. OAA for Pre paid baggage
    :ivar name: Name of the bundled service.
    :ivar booking: Booking method for the bundled service, e..g SSR.
    :ivar occurrence: How many of the service are included in the bundled service.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            length=2
        )
    )
    carrier_sub_code: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="CarrierSubCode",
            type="Attribute"
        )
    )
    service_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ServiceType",
            type="Attribute"
        )
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute"
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute"
        )
    )
    booking: Optional[TypeBooking] = field(
        default=None,
        metadata=dict(
            name="Booking",
            type="Attribute"
        )
    )
    occurrence: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Occurrence",
            type="Attribute"
        )
    )


@dataclass
class Chgtype:
    """PenFee list will be populated.

    :ivar pen_fee:
    """
    class Meta:
        name = "CHGType"

    pen_fee: List[PenFeeType] = field(
        default_factory=list,
        metadata=dict(
            name="PenFee",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=2
        )
    )


@dataclass
class Co2Emissions:
    """The carbon emissions produced by the journey.

    :ivar co2_emission:
    :ivar total_value: The total CO2 emission value for the journey
    :ivar unit: The unit used in the TotalValue attribute
    :ivar category: The category name of the type of cabin, either Economy or Premium.  Premium is any cabin that is not considered Economy
    :ivar source: The source responsible for the values
    """
    class Meta:
        name = "CO2Emissions"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    co2_emission: List[Co2Emission] = field(
        default_factory=list,
        metadata=dict(
            name="CO2Emission",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    total_value: Optional[float] = field(
        default=None,
        metadata=dict(
            name="TotalValue",
            type="Attribute"
        )
    )
    unit: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Unit",
            type="Attribute",
            min_length=1,
            max_length=64
        )
    )
    category: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            min_length=1,
            max_length=64
        )
    )
    source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute",
            min_length=1,
            max_length=64
        )
    )


@dataclass
class CarrierList:
    """
    :ivar carrier_code:
    :ivar include_carrier:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier_code: List[CarrierCode] = field(
        default_factory=list,
        metadata=dict(
            name="CarrierCode",
            type="Element",
            min_occurs=1,
            max_occurs=6
        )
    )
    include_carrier: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeCarrier",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CategoryDetailsType:
    """
    :ivar category_details: For each category Details of Structured Fare
    						Rules
    :ivar value:
    """
    category_details: List[ValueDetails] = field(
        default_factory=list,
        metadata=dict(
            name="CategoryDetails",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Characteristic:
    """
    :ivar value:
    :ivar position:
    :ivar row_location:
    :ivar padiscode: Industry standard code that defines seat and row characteristic.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True
        )
    )
    position: Optional[TypePosition] = field(
        default=None,
        metadata=dict(
            name="Position",
            type="Attribute"
        )
    )
    row_location: Optional[TypeRowLocation] = field(
        default=None,
        metadata=dict(
            name="RowLocation",
            type="Attribute"
        )
    )
    padiscode: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PADISCode",
            type="Attribute",
            min_length=1,
            max_length=99
        )
    )


@dataclass
class ChargesRules:
    """Fare Reference associated with the BookingRules.

    :ivar voluntary_changes:
    :ivar voluntary_refunds:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    voluntary_changes: List["ChargesRules.VoluntaryChanges"] = field(
        default_factory=list,
        metadata=dict(
            name="VoluntaryChanges",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    voluntary_refunds: List["ChargesRules.VoluntaryRefunds"] = field(
        default_factory=list,
        metadata=dict(
            name="VoluntaryRefunds",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class VoluntaryChanges:
        """
        :ivar penalty:
        :ivar vol_change_ind:
        """
        penalty: Optional[Penalty] = field(
            default=None,
            metadata=dict(
                name="Penalty",
                type="Element"
            )
        )
        vol_change_ind: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="VolChangeInd",
                type="Attribute"
            )
        )

    @dataclass
    class VoluntaryRefunds:
        """
        :ivar penalty:
        :ivar vol_change_ind:
        """
        penalty: Optional[Penalty] = field(
            default=None,
            metadata=dict(
                name="Penalty",
                type="Element"
            )
        )
        vol_change_ind: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="VolChangeInd",
                type="Attribute"
            )
        )


@dataclass
class ConjunctedTicketInfo:
    """
    :ivar number:
    :ivar iatanumber:
    :ivar ticket_issue_date:
    :ivar ticketing_agent_sign_on:
    :ivar country_code: Contains Ticketed PCC’s Country code.
    :ivar status:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True
        )
    )
    iatanumber: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IATANumber",
            type="Attribute",
            max_length=8
        )
    )
    ticket_issue_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketIssueDate",
            type="Attribute"
        )
    )
    ticketing_agent_sign_on: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingAgentSignOn",
            type="Attribute",
            max_length=8
        )
    )
    country_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Attribute",
            length=2
        )
    )
    status: Optional[TypeTicketStatus] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Coupon:
    """The flight coupon that resulted from the ticketing operation.

    :ivar ticket_designator:
    :ivar key:
    :ivar coupon_number: The sequential number of this coupon.
    :ivar operating_carrier: The true carrier.
    :ivar operating_flight_number: The true carrier's flight number.
    :ivar marketing_carrier: If codeshare applies to this, this is the
                            marketing carrier (as opposed to the operating carrier).
    :ivar marketing_flight_number: If codeshare applies to this, this is the
                            marketing flight number (as opposed to the operating flight
                            number).
    :ivar origin: Returns the airport or city code that
                            defines the origin market for this fare.
    :ivar destination: Returns the airport or city code that
                            defines the destination market for this fare.
    :ivar departure_time: The date and time at which this entity
                            departs. This does not include time zone information since it can
                            be derived from the origin location. In case of open segment this
                            will not be returned.
    :ivar arrival_time: The date and time at which this entity arrives
                            at the destination. This does not include time zone information
                            since it can be derived from the origin location.
    :ivar stopover_code: Stopover code - indicator that stopover
                            is allowed at Origin Airport or City.
    :ivar booking_class: Booked fare class for coupon.
    :ivar fare_basis: The fare basis code for this fare
    :ivar not_valid_before: Fare not valid before this date.
    :ivar not_valid_after: Fare not valid after this date.
    :ivar status: The status of this coupon returend from host is mapped as follows
                                  Code="A" Status="Airport Controlled"
                                  Code="C" Status="Checked In"
                                  Code="F" Status="Flown/Used"
                                  Code="L" Status="Boarded/Lifted"
                                  Code="O" Status="Open"
                                  Code="P" Status="Printed"
                                  Code="R" Status="Refunded"
                                  Code="E" Status="Exchanged"
                                  Code="V" Status="Void"
                                  Code="Z" Status="Archived/Carrier Modified"
                                  Code="U" Status="Unavailable"
                                  Code="S" Status="Suspended"
                                  Code="I" Status="Irregular Ops"
                                  Code="D" Status="Deleted/Removed"
                                  Code="X" Status="Unknown"
    :ivar segment_group: Indicates the grouping in which this
                            segment resides based on Origin/Destination pairs in itinerary
    :ivar marriage_group: Airline Marrraige group indicator
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_designator: List[TicketDesignator] = field(
        default_factory=list,
        metadata=dict(
            name="TicketDesignator",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    coupon_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="CouponNumber",
            type="Attribute"
        )
    )
    operating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OperatingCarrier",
            type="Attribute",
            length=2
        )
    )
    operating_flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OperatingFlightNumber",
            type="Attribute",
            max_length=5
        )
    )
    marketing_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MarketingCarrier",
            type="Attribute",
            length=2
        )
    )
    marketing_flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MarketingFlightNumber",
            type="Attribute",
            max_length=5
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute"
        )
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute"
        )
    )
    stopover_code: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="StopoverCode",
            type="Attribute",
            required=True
        )
    )
    booking_class: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingClass",
            type="Attribute",
            required=True,
            max_length=2
        )
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            required=True
        )
    )
    not_valid_before: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NotValidBefore",
            type="Attribute"
        )
    )
    not_valid_after: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NotValidAfter",
            type="Attribute"
        )
    )
    status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            required=True,
            max_length=1
        )
    )
    segment_group: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SegmentGroup",
            type="Attribute"
        )
    )
    marriage_group: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MarriageGroup",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class DestinationPurposeCode:
    """This code is required to indicate destination and purpose of Travel. It is
    applicable for Canada and Bermuda agency only. This is used by Worldspan.

    :ivar destination:
    :ivar purpose:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    destination: Optional[TypeDestinationCode] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True
        )
    )
    purpose: Optional[TypePurposeCode] = field(
        default=None,
        metadata=dict(
            name="Purpose",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Dimension(TypeUnitOfMeasure):
    """Information related to Length,Height,Width of a baggage.

    :ivar type: Type denotes Length,Height,Width of a baggage.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class DocumentOptions:
    """Allows an agency to set different document options for the itinerary.

    :ivar passenger_receipt_override:
    :ivar override_option: Allows an agency to override print options for documents during document generation.
    :ivar suppress_itinerary_remarks: True when itinerary remarks are suppressed.
    :ivar generate_itin_numbers: True when itinerary numbers are system
                            generated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    passenger_receipt_override: Optional[PassengerReceiptOverride] = field(
        default=None,
        metadata=dict(
            name="PassengerReceiptOverride",
            type="Element"
        )
    )
    override_option: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="OverrideOption",
            type="Element",
            min_occurs=0,
            max_occurs=999,
            max_length=50
        )
    )
    suppress_itinerary_remarks: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="SuppressItineraryRemarks",
            type="Attribute"
        )
    )
    generate_itin_numbers: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="GenerateItinNumbers",
            type="Attribute"
        )
    )


@dataclass
class Emd:
    """
    :ivar fulfillment_type: A one digit code specifying how the service must be fulfilled.
                            See FulfillmentTypeDescription for the description of this value.
    :ivar fulfillment_type_description: EMD description.
    :ivar associated_item: The type of Optional Service.  The choices are Flight, Ticket, Merchandising, Rule Buster, Allowance, Chargeable Baggage, Carry On Baggage Allowance, Prepaid Baggage.  Provider: 1G, 1V, 1P, 1J
    :ivar availability_charge_indicator: A one-letter code specifying whether the service
                            is available or if there is a charge associated with it.
                            X = Service not available
                            F = No charge for service (free) and an EMD is not issued to
                            reflect free service
                            E = No charge for service (free) and an EMD is issued to reflect
                            the free service.
                            G = No charge for service (free), booking is not required and an
                            EMD is not issued to reflect free service
                            H = No charge for service (free), booking is not required, and an
                            EMD is issued to reflect the free service.
                            Blank = No application. Charges apply according to the data in the
                            Service Fee fields.
    :ivar refund_reissue_indicator: An attribute specifying whether the service is
                            refundable or reissuable.
    :ivar commissionable: True/False value to whether or not the
                            service is comissionable.
    :ivar mileage_indicator: True/False value to whether or not the
                            service has miles.
    :ivar location: 3 letter location code where the service will be availed.
    :ivar date: The date at which the service will be used.
    :ivar booking: Holds the booking description for the service, e.g., SSR.
    :ivar display_category: Describes when the service should be displayed.
    :ivar reusable: Identifies if the service can be re-used towards a future purchase.
    """
    class Meta:
        name = "EMD"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fulfillment_type: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FulfillmentType",
            type="Attribute",
            min_inclusive=1,
            max_inclusive=5
        )
    )
    fulfillment_type_description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FulfillmentTypeDescription",
            type="Attribute"
        )
    )
    associated_item: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AssociatedItem",
            type="Attribute"
        )
    )
    availability_charge_indicator: Optional["Emd.AvailabilityChargeIndicator"] = field(
        default=None,
        metadata=dict(
            name="AvailabilityChargeIndicator",
            type="Attribute"
        )
    )
    refund_reissue_indicator: Optional["Emd.RefundReissueIndicator"] = field(
        default=None,
        metadata=dict(
            name="RefundReissueIndicator",
            type="Attribute"
        )
    )
    commissionable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Commissionable",
            type="Attribute"
        )
    )
    mileage_indicator: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="MileageIndicator",
            type="Attribute"
        )
    )
    location: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Location",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Date",
            type="Attribute"
        )
    )
    booking: Optional[TypeBooking] = field(
        default=None,
        metadata=dict(
            name="Booking",
            type="Attribute"
        )
    )
    display_category: Optional[TypeDisplayCategory] = field(
        default=None,
        metadata=dict(
            name="DisplayCategory",
            type="Attribute"
        )
    )
    reusable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Reusable",
            type="Attribute"
        )
    )

    class AvailabilityChargeIndicator(Enum):
        """
        :cvar X:
        :cvar E:
        :cvar F:
        :cvar G:
        :cvar H:
        """
        X = "X"
        E = "E"
        F = "F"
        G = "G"
        H = "H"

    class RefundReissueIndicator(Enum):
        """
        :cvar REFUNDABLE:
        :cvar NON_REFUNDABLE:
        :cvar REUSE:
        """
        REFUNDABLE = "Refundable"
        NON_REFUNDABLE = "NonRefundable"
        REUSE = "Reuse"


@dataclass
class Emdcommission:
    """Commission information to be used for EMD issuance. Supported providers are
    1V/1G/1P/1J.

    :ivar type: Type of the commission applied.One of Amount/Percentage
    :ivar value: Value of the commission applied for EMD issuance.Could represent amount or percentage depending on the type
    :ivar currency_code: Currency of the commission amount applied.Applicable only with type - Amount
    """
    class Meta:
        name = "EMDCommission"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[TypeAdjustmentType] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True
        )
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            length=3
        )
    )


@dataclass
class Emdcoupon:
    """The coupon information for the EMD issued. Supported providers are
    1G/1V/1P/1J.

    :ivar number: Number of the EMD coupon
    :ivar status: Status of the coupon. Possible values Open, Void, Refunded, Exchanged, Irregular Operations,Airport Control, Checked In, Flown/Used, Boarded/Lifted, Suspended, Unknown
    :ivar svc_description: Description of the service related to the EMD Coupon
    :ivar consumed_at_issuance_ind: Indicates if the EMD coupon has been considered used as soon as issued.
    :ivar rfic: Reason For Issuance Code for the EMD coupon
    :ivar rfisc: Reason For Issueance Sub code for the EMD coupon
    :ivar rfidescription: Reason for Issueance Description for the EMD coupon
    :ivar origin: Departure Airport Code for the flight with which the Coupon is associated
    :ivar destination: Destination Airport Code for the flight with which the Coupon is associated
    :ivar flight_number: Flight Number of the flight with which the coupon is associated.
    :ivar present_to: Service provider to present the coupon to
    :ivar present_at: Location of service provider where this coupon should be presented at
    :ivar non_refundable_ind: Indicates whether the coupon is non-refundable
    :ivar marketing_carrier: Marketing carrier associated with the coupon
    :ivar key: System generated Key
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        name = "EMDCoupon"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True
        )
    )
    status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            required=True
        )
    )
    svc_description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SvcDescription",
            type="Attribute"
        )
    )
    consumed_at_issuance_ind: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ConsumedAtIssuanceInd",
            type="Attribute"
        )
    )
    rfic: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RFIC",
            type="Attribute",
            required=True,
            length=1
        )
    )
    rfisc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RFISC",
            type="Attribute"
        )
    )
    rfidescription: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RFIDescription",
            type="Attribute",
            min_length=1,
            max_length=86
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            max_length=5
        )
    )
    present_to: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PresentTo",
            type="Attribute",
            min_length=1,
            max_length=71
        )
    )
    present_at: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PresentAt",
            type="Attribute",
            min_length=1,
            max_length=71
        )
    )
    non_refundable_ind: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NonRefundableInd",
            type="Attribute"
        )
    )
    marketing_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MarketingCarrier",
            type="Attribute",
            length=2
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class EmdretrieveReq(BaseReq):
    """Electronic Miscellaneous Document retrieve request.Supported providers are
    1G/1V/1P/1J.

    :ivar list_retrieve: Provider: 1G/1V/1P/1J-Information required for retrieval of list of EMDs
    :ivar detail_retrieve: Provider: 1G/1V/1P/1J-Information required for a detailed EMD retrieve
    """
    class Meta:
        name = "EMDRetrieveReq"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    list_retrieve: Optional["EmdretrieveReq.ListRetrieve"] = field(
        default=None,
        metadata=dict(
            name="ListRetrieve",
            type="Element"
        )
    )
    detail_retrieve: Optional["EmdretrieveReq.DetailRetrieve"] = field(
        default=None,
        metadata=dict(
            name="DetailRetrieve",
            type="Element"
        )
    )

    @dataclass
    class ListRetrieve:
        """
        :ivar provider_reservation_detail: Provider reservation details to be provided to fetch list of EMDs associated with it.
        """
        provider_reservation_detail: Optional[ProviderReservationDetail] = field(
            default=None,
            metadata=dict(
                name="ProviderReservationDetail",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                required=True
            )
        )

    @dataclass
    class DetailRetrieve:
        """
        :ivar provider_reservation_detail: Provider reservation locator to be specified for display operation, if mentioned along woth the EMD number then synchronization of that EMD is performed considering the same to be associated with the mentioned PNR.
        :ivar emdnumber: EMD number to be specified for display operation. If mentioned along with provider reservation detail then synchronization of that EMD is performed considering the same to be associated with the mentioned PNR.
        """
        provider_reservation_detail: Optional[ProviderReservationDetail] = field(
            default=None,
            metadata=dict(
                name="ProviderReservationDetail",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0"
            )
        )
        emdnumber: Optional[str] = field(
            default=None,
            metadata=dict(
                name="EMDNumber",
                type="Element",
                required=True,
                length=13
            )
        )


@dataclass
class EmbargoList:
    """List of embargoes. Provider: 1G, 1V, 1P, 1J.

    :ivar embargo:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    embargo: List[Embargo] = field(
        default_factory=list,
        metadata=dict(
            name="Embargo",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class ExchangePenaltyInfo:
    """
    :ivar penalty_information:
    :ivar ptc:
    :ivar minimum_change_fee: Minimum change fee for changes to the itinerary.
    :ivar maximum_change_fee: Maximum change fee for changes  to the itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    penalty_information: List[PenaltyInformation] = field(
        default_factory=list,
        metadata=dict(
            name="PenaltyInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ptc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PTC",
            type="Attribute",
            min_length=3,
            max_length=5
        )
    )
    minimum_change_fee: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MinimumChangeFee",
            type="Attribute"
        )
    )
    maximum_change_fee: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MaximumChangeFee",
            type="Attribute"
        )
    )


@dataclass
class FareDetails:
    """Information about this fare component.

    :ivar fare_ticket_designator:
    :ivar key: Fare key
    :ivar passenger_detail_ref: PassengerRef key
    :ivar fare_basis: The fare basis code for this fare
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_ticket_designator: Optional[FareTicketDesignator] = field(
        default=None,
        metadata=dict(
            name="FareTicketDesignator",
            type="Element"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    passenger_detail_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PassengerDetailRef",
            type="Attribute",
            required=True
        )
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            required=True,
            max_length=20
        )
    )


@dataclass
class FareGuaranteeInfo:
    """The information related to fare guarantee details.

    :ivar guarantee_date: The date till which the fare is guaranteed.
    :ivar guarantee_type: Determines the status of a fare for a passenger.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    guarantee_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="GuaranteeDate",
            type="Attribute"
        )
    )
    guarantee_type: Optional[TypeFareGuarantee] = field(
        default=None,
        metadata=dict(
            name="GuaranteeType",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FareNote:
    """A simple textual fare note. Used within several other objects.

    :ivar value:
    :ivar key:
    :ivar precedence:
    :ivar note_name:
    :ivar fare_info_message_ref:
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[str] = field(
        default=None,
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    precedence: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Precedence",
            type="Attribute"
        )
    )
    note_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NoteName",
            type="Attribute"
        )
    )
    fare_info_message_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareInfoMessageRef",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class FareRemark:
    """
    :ivar text:
    :ivar url:
    :ivar key:
    :ivar name:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    url: List[Url] = field(
        default_factory=list,
        metadata=dict(
            name="URL",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute"
        )
    )


@dataclass
class FareRestrictionDate:
    """Fare restriction based on date ranges. StartDate and EndDate are strings
    representing respective dates. If a year component is present then it signifies
    an exact date. If only day and month components are present then it signifies a
    seasonal date, which means applicable for that date in any year.

    :ivar direction:
    :ivar start_date:
    :ivar end_date:
    :ivar end_date_indicator: This field indicates the end date/last date
                            for which travel on the fare component being validated must be
                            commenced or completed
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    direction: Optional[TypeFareDirectionality] = field(
        default=None,
        metadata=dict(
            name="Direction",
            type="Attribute"
        )
    )
    start_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute"
        )
    )
    end_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EndDate",
            type="Attribute"
        )
    )
    end_date_indicator: Optional["FareRestrictionDate.EndDateIndicator"] = field(
        default=None,
        metadata=dict(
            name="EndDateIndicator",
            type="Attribute"
        )
    )

    class EndDateIndicator(Enum):
        """
        :cvar COMMENCE:
        :cvar COMPLETE:
        """
        COMMENCE = "Commence"
        COMPLETE = "Complete"


@dataclass
class FareRestrictionDaysOfWeek:
    """Days of the week that the restriction applies too.

    :ivar direction:
    :ivar trip_type:
    :ivar monday:
    :ivar tuesday:
    :ivar wednesday:
    :ivar thursday:
    :ivar friday:
    :ivar saturday:
    :ivar sunday:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    direction: Optional[TypeFareDirectionality] = field(
        default=None,
        metadata=dict(
            name="Direction",
            type="Attribute"
        )
    )
    trip_type: Optional[TypeFareTripType] = field(
        default=None,
        metadata=dict(
            name="TripType",
            type="Attribute"
        )
    )
    monday: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Monday",
            type="Attribute"
        )
    )
    tuesday: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Tuesday",
            type="Attribute"
        )
    )
    wednesday: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Wednesday",
            type="Attribute"
        )
    )
    thursday: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Thursday",
            type="Attribute"
        )
    )
    friday: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Friday",
            type="Attribute"
        )
    )
    saturday: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Saturday",
            type="Attribute"
        )
    )
    sunday: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Sunday",
            type="Attribute"
        )
    )


@dataclass
class FareRuleLookup:
    """Parameters to use for a fare rule lookup that is not associated with an Air
    Reservation Locator Code.

    :ivar account_code:
    :ivar point_of_sale:
    :ivar origin:
    :ivar destination:
    :ivar carrier:
    :ivar fare_basis:
    :ivar provider_code:
    :ivar departure_date:
    :ivar ticketing_date:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    account_code: Optional[AccountCode] = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    point_of_sale: Optional[PointOfSale] = field(
        default=None,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            length=2
        )
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            required=True
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2,
            max_length=5
        )
    )
    departure_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute"
        )
    )
    ticketing_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingDate",
            type="Attribute"
        )
    )


@dataclass
class FareRuleShort:
    """Short Text Fare Rule.

    :ivar fare_rule_name_value:
    :ivar category:
    :ivar table_number:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_rule_name_value: List[FareRuleNameValue] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleNameValue",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    category: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            required=True
        )
    )
    table_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TableNumber",
            type="Attribute"
        )
    )


@dataclass
class FareStatus:
    """Denotes the status of a particular fare.

    :ivar fare_status_failure_info:
    :ivar code: The status of the fare.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_status_failure_info: Optional[FareStatusFailureInfo] = field(
        default=None,
        metadata=dict(
            name="FareStatusFailureInfo",
            type="Element"
        )
    )
    code: Optional[TypeFareStatusCode] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FareSurcharge:
    """Surcharges for a fare component.

    :ivar key:
    :ivar type:
    :ivar amount:
    :ivar segment_ref:
    :ivar coupon_ref: The coupon to which that surcharge is relative
                            (if applicable)
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
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
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True
        )
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )
    coupon_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CouponRef",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class FeeInfo(TypeFeeInfo):
    """A generic type of fee for those charges which are incurred by the passenger,
    but not necessarily shown on tickets."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class FlightInformationReq(BaseReq):
    """Request for the Flight Info of segments.

    :ivar flight_info_criteria: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_info_criteria: List[FlightInfoCriteria] = field(
        default_factory=list,
        metadata=dict(
            name="FlightInfoCriteria",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class GroupedOptionInfo:
    """
    :ivar grouped_option:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    grouped_option: List[GroupedOption] = field(
        default_factory=list,
        metadata=dict(
            name="GroupedOption",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class HostTokenList:
    """The shared object list of Host Tokens.

    :ivar host_token:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class IncludeAddlBookingCodeInfo:
    """Used to include primary or secondary carrier's booking code details.

    :ivar type: The type defines that the booking code info is
                            for primary or secondary carrier.
    :ivar secondary_carrier: The secondary carrier code is required when
                            type is secondary .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[TypeCarrierCode] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    secondary_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SecondaryCarrier",
            type="Attribute",
            length=2
        )
    )


@dataclass
class InvoluntaryChange:
    """Specify the Ticket Endorsement value.

    :ivar ticket_endorsement:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_endorsement: Optional[TicketEndorsement] = field(
        default=None,
        metadata=dict(
            name="TicketEndorsement",
            type="Element",
            required=True
        )
    )


@dataclass
class Itinerary:
    """Allows an agency to select the itinenary option for ticket.

    :ivar type: Specifies the type of itinenary option
                            for ticket like Invoice type or Pocket itinenary.
    :ivar option: Specifies the itinerary option like
                            NoFare,NoAmount.
    :ivar separate_indicator: Set to true if one itinerary to be printed per
                            passenger.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[TypeItinerary] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )
    option: Optional[TypeItineraryOption] = field(
        default=None,
        metadata=dict(
            name="Option",
            type="Attribute"
        )
    )
    separate_indicator: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="SeparateIndicator",
            type="Attribute"
        )
    )


@dataclass
class Journey:
    """Information about all connecting segment list and total traveling time.

    :ivar air_segment_ref:
    :ivar travel_time: Total traveling time that is difference between the departure time of the first segment and the arrival time of the last segments for that particular entire set of connection.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    travel_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute"
        )
    )


@dataclass
class LandCharges:
    """Prints non-air charges on a document.

    :ivar tax:
    :ivar base:
    :ivar total:
    :ivar miscellaneous:
    :ivar pre_paid:
    :ivar deposit:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    tax: List[Tax] = field(
        default_factory=list,
        metadata=dict(
            name="Tax",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    base: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Base",
            type="Attribute"
        )
    )
    total: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Total",
            type="Attribute"
        )
    )
    miscellaneous: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Miscellaneous",
            type="Attribute"
        )
    )
    pre_paid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PrePaid",
            type="Attribute"
        )
    )
    deposit: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Deposit",
            type="Attribute"
        )
    )


@dataclass
class Leg:
    """Information about the journey Leg.

    :ivar leg_detail:
    :ivar key:
    :ivar group: Returns the Group Number for the leg.
    :ivar origin: Returns the origin airport or city code
                            for the leg.
    :ivar destination: Returns the destination airport or city
                            code for the leg.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    leg_detail: List[LegDetail] = field(
        default_factory=list,
        metadata=dict(
            name="LegDetail",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    group: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Group",
            type="Attribute",
            required=True
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            min_length=3,
            max_length=8,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            min_length=3,
            max_length=8,
            white_space="collapse"
        )
    )


@dataclass
class LegPrice:
    """Information about the journey Leg Price.

    :ivar leg_detail:
    :ivar key:
    :ivar total_price: The Total Prices for the Combination of
                            Journey legs for this Price.
    :ivar approximate_total_price: The Converted Total Price in Agency's Default
                            Currency Value
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    leg_detail: List[LegDetail] = field(
        default_factory=list,
        metadata=dict(
            name="LegDetail",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute",
            required=True
        )
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute"
        )
    )


@dataclass
class ManualFareAdjustment:
    """
    :ivar applied_on: Represents pricing component upon which manual increment/discount to be applied. Presently supported values are Base and Total. Other is present as a future place holder but presently no request processing logic is available for value Other
    :ivar adjustment_type: Represents process used for applying manual discount/increment. Presently supported values are Flat, Percentage.
    :ivar value: Represents value of increment/discount applied. Negative value is considered as discount whereas positive value represents increment
    :ivar passenger_ref: Represents passenger association.
    :ivar ticket_designator: Providers: 1p/1j
    :ivar fare_type: Providers: 1p/1j
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    applied_on: Optional[TypeAdjustmentTarget] = field(
        default=None,
        metadata=dict(
            name="AppliedOn",
            type="Attribute",
            required=True
        )
    )
    adjustment_type: Optional[TypeAdjustmentType] = field(
        default=None,
        metadata=dict(
            name="AdjustmentType",
            type="Attribute",
            required=True
        )
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True
        )
    )
    passenger_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PassengerRef",
            type="Attribute"
        )
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketDesignator",
            type="Attribute",
            min_length=0,
            max_length=20
        )
    )
    fare_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareType",
            type="Attribute",
            min_length=1,
            max_length=5
        )
    )


@dataclass
class Meals:
    """Available Meal Service.

    :ivar value:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    value: Optional[TypeMealService] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class MerchandisingPricingModifiers:
    """
    :ivar account_code: The account code is used to get corporate discounted pricing on paid seats. Provider:ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class OptionalServiceModifiers:
    """Rich Content and Branding for an optional service.

    :ivar optional_service_modifier:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    optional_service_modifier: List[OptionalServiceModifier] = field(
        default_factory=list,
        metadata=dict(
            name="OptionalServiceModifier",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class OriginalItineraryDetails:
    """Used for rapid reprice to provide additional information about the original
    itinerary. Providers: 1G/1V/1P/1S/1A.

    :ivar itinerary_type: Values allowed are International or Domestic. This tells if the itinerary is international or domestic.
    :ivar bulk_ticket: Set to true and the itinerary is/will be a bulk ticket.
                                            Set to false and the itinerary being repriced will not be a bulk ticket.
                                            Default is false.
    :ivar ticketing_pcc: This is the PCC or SID where the ticket was issued
    :ivar ticketing_iata: This is the IATA where the ticket was issued.
    :ivar ticketing_country: This is the country where the ticket was issued.
    :ivar tour_code:
    :ivar ticketing_date: The date the repriced itinerary was ticketed
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    itinerary_type: Optional[TypeItineraryCode] = field(
        default=None,
        metadata=dict(
            name="ItineraryType",
            type="Attribute"
        )
    )
    bulk_ticket: bool = field(
        default=False,
        metadata=dict(
            name="BulkTicket",
            type="Attribute"
        )
    )
    ticketing_pcc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingPCC",
            type="Attribute",
            min_length=2,
            max_length=10
        )
    )
    ticketing_iata: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingIATA",
            type="Attribute",
            max_length=8
        )
    )
    ticketing_country: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingCountry",
            type="Attribute",
            length=2
        )
    )
    tour_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Attribute",
            max_length=15
        )
    )
    ticketing_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingDate",
            type="Attribute"
        )
    )


@dataclass
class Pcc:
    """Specify pseudo City.

    :ivar override_pcc:
    :ivar point_of_sale:
    :ivar ticket_agency:
    """
    class Meta:
        name = "PCC"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    override_pcc: Optional[OverridePcc] = field(
        default=None,
        metadata=dict(
            name="OverridePCC",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=5
        )
    )
    ticket_agency: Optional[TicketAgency] = field(
        default=None,
        metadata=dict(
            name="TicketAgency",
            type="Element"
        )
    )


@dataclass
class PassengerDetails:
    """Details of passenger.

    :ivar loyalty_card_details:
    :ivar key: Passenger key
    :ivar code: Passenger code
    :ivar age: Passenger age
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    loyalty_card_details: List[LoyaltyCardDetails] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyCardDetails",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True,
            min_length=3,
            max_length=5
        )
    )
    age: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute"
        )
    )


@dataclass
class PenaltyFareInformation:
    """
    :ivar penalty_info: Penalty Limit if requested.
    :ivar prohibit_penalty_fares: Indicates whether user wants penalty
                            fares to be returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    penalty_info: Optional[TypeFarePenalty] = field(
        default=None,
        metadata=dict(
            name="PenaltyInfo",
            type="Element"
        )
    )
    prohibit_penalty_fares: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ProhibitPenaltyFares",
            type="Attribute",
            required=True
        )
    )


@dataclass
class PermittedCabins:
    """
    :ivar cabin_class:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    cabin_class: List[CabinClass] = field(
        default_factory=list,
        metadata=dict(
            name="CabinClass",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=5
        )
    )


@dataclass
class PermittedCarriers:
    """
    :ivar carrier:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier: List[Carrier] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class PocketItineraryRemark(TypeAssociatedRemarkWithSegmentRef):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class PrePayId:
    """Pre pay unique identifier , example Flight Pass Number.

    :ivar company_name: Supplier info that is specific to the pre pay Id
    :ivar id: This is the exact pre pay number. Example flight pass number
    :ivar type: Type of pre pay unique identifier,presently only available value is FlightPass.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    company_name: Optional[CompanyName] = field(
        default=None,
        metadata=dict(
            name="CompanyName",
            type="Element"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Id",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=36
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )


@dataclass
class PreferredBookingCodes:
    """This is the container to specify all preferred booking codes.

    :ivar booking_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata=dict(
            name="BookingCode",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class PreferredCabins:
    """
    :ivar cabin_class:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    cabin_class: Optional[CabinClass] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )


@dataclass
class PreferredCarriers:
    """
    :ivar carrier:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier: List[Carrier] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class PricingDetails:
    """Used for rapid reprice. This is a response element.  Additional information
    about how pricing was obtain, messages, etc.  Providers: 1G/1V/1P/1S/1A.

    :ivar advisory_message: Advisory messages returned from the host.
    :ivar endorsement_text: Endorsement text returned from the host.
    :ivar waiver_text: Waiver text returned from the host.
    :ivar low_fare_pricing: This tells if Low Fare Finder was used.
    :ivar low_fare_found: This tells if the lowest fare was found.
    :ivar penalty_applies: This tells if penalties apply.
    :ivar discount_applies: This tells if a discount applies.
    :ivar itinerary_type: Values allowed are International or Domestic. This tells if the itinerary is international or domestic.
    :ivar validating_vendor_code: The vendor code of the validating carrier.
    :ivar for_ticketing_on_date: The ticketing date of the itinerary.
    :ivar last_date_to_ticket: The last date to issue the ticket.
    :ivar form_of_refund: How the refund will be issued. Values will be MCO or FormOfPayment
    :ivar account_code:
    :ivar bankers_selling_rate: The selling rate at time of quote.
    :ivar pricing_type: Ties with the RepricingModifiers sent in the request and tells how the itinerary was priced.
    :ivar conversion_rate: The conversion rate at the time of quote.
    :ivar rate_of_exchange: The exchange rate at time of quote.
    :ivar original_ticket_currency: The currency of the original ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    advisory_message: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AdvisoryMessage",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    endorsement_text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="EndorsementText",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="WaiverText",
            type="Element"
        )
    )
    low_fare_pricing: bool = field(
        default=False,
        metadata=dict(
            name="LowFarePricing",
            type="Attribute"
        )
    )
    low_fare_found: bool = field(
        default=False,
        metadata=dict(
            name="LowFareFound",
            type="Attribute"
        )
    )
    penalty_applies: bool = field(
        default=False,
        metadata=dict(
            name="PenaltyApplies",
            type="Attribute"
        )
    )
    discount_applies: bool = field(
        default=False,
        metadata=dict(
            name="DiscountApplies",
            type="Attribute"
        )
    )
    itinerary_type: Optional[TypeItineraryCode] = field(
        default=None,
        metadata=dict(
            name="ItineraryType",
            type="Attribute"
        )
    )
    validating_vendor_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ValidatingVendorCode",
            type="Attribute",
            length=2
        )
    )
    for_ticketing_on_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ForTicketingOnDate",
            type="Attribute"
        )
    )
    last_date_to_ticket: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LastDateToTicket",
            type="Attribute"
        )
    )
    form_of_refund: Optional[TypeFormOfRefund] = field(
        default=None,
        metadata=dict(
            name="FormOfRefund",
            type="Attribute"
        )
    )
    account_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute"
        )
    )
    bankers_selling_rate: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="BankersSellingRate",
            type="Attribute"
        )
    )
    pricing_type: Optional[TypePricingType] = field(
        default=None,
        metadata=dict(
            name="PricingType",
            type="Attribute"
        )
    )
    conversion_rate: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="ConversionRate",
            type="Attribute"
        )
    )
    rate_of_exchange: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="RateOfExchange",
            type="Attribute"
        )
    )
    original_ticket_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OriginalTicketCurrency",
            type="Attribute",
            length=3
        )
    )


@dataclass
class ProhibitedCabins:
    """
    :ivar cabin_class:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    cabin_class: List[CabinClass] = field(
        default_factory=list,
        metadata=dict(
            name="CabinClass",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=3
        )
    )


@dataclass
class ProhibitedCarriers:
    """
    :ivar carrier:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carrier: List[Carrier] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class RefundFailureInfo:
    """Will be optionally returned as part of AirRefunTicketingRsp if one or all
    ticket refund requests fail.

    :ivar ticket_number:
    :ivar name:
    :ivar tcrnumber: The identifying number for a Ticketless Air
                                    Reservation.
    :ivar booking_traveler_ref:
    :ivar code:
    :ivar message:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: Optional[TicketNumber] = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Element"
        )
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    code: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )
    message: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute"
        )
    )


@dataclass
class RelatedTraveler:
    """Detailed related Traveler information for pre pay profiles.

    :ivar loyalty_card: Traveler loyalty card detail
    :ivar person_name: Traveler name detail
    :ivar credits_used: Traveler pre pay credit detail
    :ivar status_code: Traveler status code(One of Marked for deletion,Lapsed,Terminated,Active,Inactive)
    :ivar relation: Relation to the pre pay id. Example flight pass user
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyCard",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    person_name: Optional[PersonName] = field(
        default=None,
        metadata=dict(
            name="PersonName",
            type="Element"
        )
    )
    credits_used: Optional["RelatedTraveler.CreditsUsed"] = field(
        default=None,
        metadata=dict(
            name="CreditsUsed",
            type="Element"
        )
    )
    status_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StatusCode",
            type="Attribute"
        )
    )
    relation: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Relation",
            type="Attribute"
        )
    )

    @dataclass
    class CreditsUsed:
        """
        :ivar used_credit:
        :ivar currency_code:
        """
        used_credit: Optional[Decimal] = field(
            default=None,
            metadata=dict(
                name="UsedCredit",
                type="Attribute"
            )
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="CurrencyCode",
                type="Attribute",
                length=3
            )
        )


@dataclass
class RetrieveLowFareSearchReq(BaseReq):
    """Retrieve low fare search responses that were initiated by an asynchronous
    request.

    :ivar search_id: Provider: 1G,1V,1P,1J,ACH-SearchID to be used for Asynchronous LowFareSearch Request
    :ivar provider_code: Provider: 1G,1V,1P,1J,ACH-Provider code of a specific host
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    search_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SearchId",
            type="Attribute",
            required=True
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2,
            max_length=5
        )
    )


@dataclass
class RuleAdvancedPurchase:
    """Container for rules regarding advance purchase restrictions.
    TicketingEarliestDate and TicketingLatestDate are strings representing
    respective dates. If a year component is present then it signifies an exact
    date. If only day and month components are present then it signifies a seasonal
    date, which means applicable for that date in any year.

    :ivar reservation_latest_period:
    :ivar reservation_latest_unit:
    :ivar ticketing_earliest_date:
    :ivar ticketing_latest_date:
    :ivar more_rules_present: If true, specifies that advance purchase
                            information will be present in fare rules.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    reservation_latest_period: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ReservationLatestPeriod",
            type="Attribute"
        )
    )
    reservation_latest_unit: Optional[TypeStayUnit] = field(
        default=None,
        metadata=dict(
            name="ReservationLatestUnit",
            type="Attribute"
        )
    )
    ticketing_earliest_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingEarliestDate",
            type="Attribute"
        )
    )
    ticketing_latest_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingLatestDate",
            type="Attribute"
        )
    )
    more_rules_present: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="MoreRulesPresent",
            type="Attribute"
        )
    )


@dataclass
class SearchTraveler(TypePassengerType):
    """
    :ivar air_seat_assignment:
    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_seat_assignment: List[AirSeatAssignment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSeatAssignment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )


@dataclass
class SegmentSelect:
    """To be used to pass the selected segment.

    :ivar air_segment_ref: Reference to AirSegment from an Air Reservation.
    :ivar hotel_reservation_ref: Specify the locator code of Hotel reservation if it needs to be considered as Auxiliary segment
    :ivar vehicle_reservation_ref: Specify the locator code of Vehicle reservation if it needs to be considered as Auxiliary segment
    :ivar passive_segment_ref: Reference to PassiveSegment from a Passive Reservation.Specify the passive segment if it needs to be considered as Auxiliary segment
    :ivar all_confirmed_air: Set to true to consider all Confirmed segments including active and passive and set to false to discard confirmed segments
    :ivar all_waitlisted_air: Set to true to consider all Waitlisted segments and false to discard all waitlisted segments
    :ivar all_hotel: Set to true to consider all Hotel reservations as Auxiliary segment and false to discard all Hotel reservations
    :ivar all_vehicle: Set to true to consider all Vehicle reservations as Auxiliary segment and false to discard all Vehicle reservations
    :ivar all_passive: Set to true to consider all Passive segments as Auxiliary segment and false to discard passive segments
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    hotel_reservation_ref: List[TypeNonAirReservationRef] = field(
        default_factory=list,
        metadata=dict(
            name="HotelReservationRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    vehicle_reservation_ref: List[TypeNonAirReservationRef] = field(
        default_factory=list,
        metadata=dict(
            name="VehicleReservationRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    passive_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="PassiveSegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    all_confirmed_air: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AllConfirmedAir",
            type="Attribute"
        )
    )
    all_waitlisted_air: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AllWaitlistedAir",
            type="Attribute"
        )
    )
    all_hotel: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AllHotel",
            type="Attribute"
        )
    )
    all_vehicle: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AllVehicle",
            type="Attribute"
        )
    )
    all_passive: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AllPassive",
            type="Attribute"
        )
    )


@dataclass
class SelectionModifiers:
    """Modifiers supported for selection of services during EMD Issuance. Supported
    providers are 1V/1G/1P/1J.

    :ivar air_segment_ref: References to airsegments for which EMDs will be generated on all the associated services.
    :ivar svc_segment_ref: SVC segment reference to which the EMD is being issued
    :ivar supplier_code: Supplier/Vendor code for which EMDs will be generated on all the associated services. Required if PNR contains more than one supplier.
    :ivar rfic: Reason for issuance code for which EMDs will be generated on all the associated services.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    svc_segment_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="SvcSegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            length=2
        )
    )
    rfic: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RFIC",
            type="Attribute",
            length=1
        )
    )


@dataclass
class ServiceAssociations:
    """
    :ivar applicable_segment: Applicable air segment associated with this brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    applicable_segment: List["ServiceAssociations.ApplicableSegment"] = field(
        default_factory=list,
        metadata=dict(
            name="ApplicableSegment",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )

    @dataclass
    class ApplicableSegment:
        """
        :ivar response_message:
        :ivar optional_service_ref:
        :ivar key: Applicable air segment key
        """
        response_message: Optional[ResponseMessage] = field(
            default=None,
            metadata=dict(
                name="ResponseMessage",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0"
            )
        )
        optional_service_ref: Optional[OptionalServiceRef] = field(
            default=None,
            metadata=dict(
                name="OptionalServiceRef",
                type="Element"
            )
        )
        key: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Key",
                type="Attribute"
            )
        )


@dataclass
class ServiceGroup:
    """The Service Group of the Ancillary Service.  Providers: 1G, 1V, 1P, 1J, ACH.

    :ivar service_sub_group:
    :ivar code: The Service Group Code of the Ancillary Service.  Providers: 1G, 1V, 1P, 1J, ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    service_sub_group: List[ServiceSubGroup] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceSubGroup",
            type="Element",
            min_occurs=0,
            max_occurs=15
        )
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )


@dataclass
class SolutionGroup:
    """Specifies the trip type and diversity of all or a subset of the result
    solutions.

    :ivar permitted_account_codes:
    :ivar preferred_account_codes:
    :ivar prohibited_account_codes:
    :ivar permitted_point_of_sales:
    :ivar prohibited_point_of_sales:
    :ivar count: The number of solution to include in this
                            group. If only one group specified, this can be left blank. If
                            multiple groups specified, all counts must add up to the
                            MaxResults of the request.
    :ivar trip_type: Specifies the trip type for this group
                            of results. Allows targeting a result set to a particular set of
                            characterists.
    :ivar diversification: Specifies the diversification of this
                            group of results, if specified. Allows targeting a result set to
                            ensure they contain more unique results.
    :ivar tag: An arbitrary name for this group of solutions.
                            Will be returned with the solution for idetification.
    :ivar primary: Indicates that this is a primary
                            SolutionGroup when using alternate pricing concepts
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    permitted_account_codes: Optional["SolutionGroup.PermittedAccountCodes"] = field(
        default=None,
        metadata=dict(
            name="PermittedAccountCodes",
            type="Element"
        )
    )
    preferred_account_codes: Optional["SolutionGroup.PreferredAccountCodes"] = field(
        default=None,
        metadata=dict(
            name="PreferredAccountCodes",
            type="Element"
        )
    )
    prohibited_account_codes: Optional["SolutionGroup.ProhibitedAccountCodes"] = field(
        default=None,
        metadata=dict(
            name="ProhibitedAccountCodes",
            type="Element"
        )
    )
    permitted_point_of_sales: Optional["SolutionGroup.PermittedPointOfSales"] = field(
        default=None,
        metadata=dict(
            name="PermittedPointOfSales",
            type="Element"
        )
    )
    prohibited_point_of_sales: Optional["SolutionGroup.ProhibitedPointOfSales"] = field(
        default=None,
        metadata=dict(
            name="ProhibitedPointOfSales",
            type="Element"
        )
    )
    count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Count",
            type="Attribute"
        )
    )
    trip_type: Optional[TypeTripType] = field(
        default=None,
        metadata=dict(
            name="TripType",
            type="Attribute",
            required=True
        )
    )
    diversification: Optional[TypeDiversity] = field(
        default=None,
        metadata=dict(
            name="Diversification",
            type="Attribute"
        )
    )
    tag: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Tag",
            type="Attribute",
            max_length=20
        )
    )
    primary: bool = field(
        default=False,
        metadata=dict(
            name="Primary",
            type="Attribute"
        )
    )

    @dataclass
    class PermittedAccountCodes:
        """
        :ivar account_code:
        """
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata=dict(
                name="AccountCode",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PreferredAccountCodes:
        """
        :ivar account_code:
        """
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata=dict(
                name="AccountCode",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedAccountCodes:
        """
        :ivar account_code:
        """
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata=dict(
                name="AccountCode",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PermittedPointOfSales:
        """
        :ivar point_of_sale:
        """
        point_of_sale: List[PointOfSale] = field(
            default_factory=list,
            metadata=dict(
                name="PointOfSale",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedPointOfSales:
        """
        :ivar point_of_sale:
        """
        point_of_sale: List[PointOfSale] = field(
            default_factory=list,
            metadata=dict(
                name="PointOfSale",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class SpecificTimeTable:
    """
    :ivar flight_origin:
    :ivar flight_destination:
    :ivar start_date:
    :ivar carrier:
    :ivar flight_number:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_origin: Optional["SpecificTimeTable.FlightOrigin"] = field(
        default=None,
        metadata=dict(
            name="FlightOrigin",
            type="Element"
        )
    )
    flight_destination: Optional["SpecificTimeTable.FlightDestination"] = field(
        default=None,
        metadata=dict(
            name="FlightDestination",
            type="Element"
        )
    )
    start_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute",
            required=True
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            length=2
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            required=True,
            max_length=5
        )
    )

    @dataclass
    class FlightOrigin:
        """
        :ivar airport:
        """
        airport: Optional[Airport] = field(
            default=None,
            metadata=dict(
                name="Airport",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                required=True
            )
        )

    @dataclass
    class FlightDestination:
        """
        :ivar airport:
        """
        airport: Optional[Airport] = field(
            default=None,
            metadata=dict(
                name="Airport",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                required=True
            )
        )


@dataclass
class Tcrinfo:
    """
    :ivar status:
    :ivar date:
    :ivar tcrnumber: The identifying number for a Ticketless Air
                            Reservation.
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    """
    class Meta:
        name = "TCRInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    status: Optional[TypeTcrstatus] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            required=True
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Date",
            type="Attribute"
        )
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Attribute",
            required=True
        )
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TaxInfo(TypeTaxInfo):
    """The tax information for a."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class TermConditions:
    """The terms and conditions to be included in Fax details.

    :ivar language_option:
    :ivar include_term_conditions: Specifies whether Term and Conditions included in the Fax or not .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    language_option: List[LanguageOption] = field(
        default_factory=list,
        metadata=dict(
            name="LanguageOption",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )
    include_term_conditions: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeTermConditions",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Text(TypeTextElement):
    """Type of Text, Eg-'Upsell','Marketing Agent','Marketing
    Consumer','Strapline','Rule'."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class TicketFailureInfo:
    """Will be optionally returned as part of AirTicketingRsp if one or all ticket
    requests fail. Atrributes are faiilure code, failure message, and passenger
    reference key. Passenger name is a child element.

    :ivar air_pricing_info_ref: Returns related air pricing infos.
    :ivar name:
    :ivar code:
    :ivar message:
    :ivar booking_traveler_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    code: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )
    message: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute"
        )
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            required=True
        )
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
    """Indicates any variance in the requested flight.

    :ivar type: Indicates type Variance, i.e. Actual,
                            Estimated, Canceled and Diversion.
    :ivar time: Indicates time for Variance.
    :ivar indicator: Indicates VAriance Indicator, i.e.
                            Early, Late.
    :ivar reason: Reason for Variance
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: Optional[TypeVarianceType] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Time",
            type="Attribute"
        )
    )
    indicator: Optional[TypeVarianceIndicator] = field(
        default=None,
        metadata=dict(
            name="Indicator",
            type="Attribute"
        )
    )
    reason: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Reason",
            type="Attribute"
        )
    )


@dataclass
class TypeRestrictionLengthOfStay:
    """Length Of Stay Restriction ( e.g. 2 day minimum..)

    :ivar length:
    :ivar stay_unit:
    :ivar stay_date:
    :ivar more_rules_present: If true, specifies that advance purchase
                        information will be present in fare rules.
    """
    class Meta:
        name = "typeRestrictionLengthOfStay"

    length: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Length",
            type="Attribute"
        )
    )
    stay_unit: Optional[TypeStayUnit] = field(
        default=None,
        metadata=dict(
            name="StayUnit",
            type="Attribute"
        )
    )
    stay_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StayDate",
            type="Attribute"
        )
    )
    more_rules_present: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="MoreRulesPresent",
            type="Attribute"
        )
    )


@dataclass
class TypeTaxInfoWithPaymentRef(TypeTaxInfo):
    """
    :ivar payment_ref: This reference elements will associate relevant payment to this tax
    """
    class Meta:
        name = "typeTaxInfoWithPaymentRef"

    payment_ref: List[PaymentRef] = field(
        default_factory=list,
        metadata=dict(
            name="PaymentRef",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class TypeTicketFailureInfo:
    """Will be optionally returned as part if one or all ticketing requests fail.

    :ivar ticket_number:
    :ivar name:
    :ivar tcrnumber: The identifying number for a Ticketless Air
                                Reservation.
    :ivar booking_traveler_ref:
    :ivar code:
    :ivar message:
    """
    class Meta:
        name = "typeTicketFailureInfo"

    ticket_number: Optional[TicketNumber] = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=1,
            max_occurs=999
        )
    )
    code: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            required=True
        )
    )
    message: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute"
        )
    )


@dataclass
class TypeTicketingModifiersRef:
    """
    :ivar air_pricing_info_ref:
    :ivar key:
    """
    class Meta:
        name = "typeTicketingModifiersRef"

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TypeWeight:
    """
    :ivar value:
    :ivar unit:
    """
    class Meta:
        name = "typeWeight"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute"
        )
    )
    unit: Optional[TypeUnitWeight] = field(
        default=None,
        metadata=dict(
            name="Unit",
            type="Attribute"
        )
    )


@dataclass
class ApisrequirementsList:
    """The shared object list of APISRequirements.

    :ivar apisrequirements:
    """
    class Meta:
        name = "APISRequirementsList"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    apisrequirements: List[Apisrequirements] = field(
        default_factory=list,
        metadata=dict(
            name="APISRequirements",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeBundle:
    """Bundle exchange, pricing, and penalty information for one ticket number Used
    both in request and response.

    :ivar air_exchange_info:
    :ivar air_pricing_info_ref:
    :ivar tax_info:
    :ivar penalty: Only used within an AirExchangeQuoteRsp
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_exchange_info: Optional[AirExchangeInfo] = field(
        default=None,
        metadata=dict(
            name="AirExchangeInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    penalty: List[CommonPenalty] = field(
        default_factory=list,
        metadata=dict(
            name="Penalty",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirFareDisplayModifiers:
    """
    :ivar trip_type:
    :ivar cabin_class:
    :ivar penalty_fare_information: Request Fares with specific Penalty
                                Information.
    :ivar fare_search_option:
    :ivar max_responses:
    :ivar departure_date:
    :ivar ticketing_date:
    :ivar return_date:
    :ivar base_fare_only:
    :ivar unrestricted_fares_only:
    :ivar fares_indicator: Indicates whether only public fares
                            should be returned or specific type of private fares
    :ivar currency_type:
    :ivar include_taxes:
    :ivar include_estimated_taxes: Indicates to include estimated taxes i.e. if set to true
                            estimated total fare,base fare and taxes would be
                            returned.
    :ivar include_surcharges:
    :ivar global_indicator:
    :ivar prohibit_min_stay_fares:
    :ivar prohibit_max_stay_fares:
    :ivar prohibit_advance_purchase_fares:
    :ivar prohibit_non_refundable_fares: Indicates whether it prohibits
                            NonRefundable Fares.
    :ivar validated_fares_only: Indicates that the requested Fares
                            should be Validated Fares only.
                            If set to true, then only valid fares will be returned.
                            If set to false, both valid and non valid fares will be returned.
                            If not sent, then no validation will be done. All fares will be
                            returned.
    :ivar prohibit_travel_restricted_fares: Indicates that the Fares not complying
                            Travel Restrictions and Seasonality fare rules are prohibited
    :ivar filed_currency: Represents the filed currency of the fare
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    trip_type: List[TypeFareTripType] = field(
        default_factory=list,
        metadata=dict(
            name="TripType",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    cabin_class: Optional[CabinClass] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    penalty_fare_information: Optional[PenaltyFareInformation] = field(
        default=None,
        metadata=dict(
            name="PenaltyFareInformation",
            type="Element"
        )
    )
    fare_search_option: List[TypeFareSearchOption] = field(
        default_factory=list,
        metadata=dict(
            name="FareSearchOption",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    max_responses: int = field(
        default=200,
        metadata=dict(
            name="MaxResponses",
            type="Attribute"
        )
    )
    departure_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute"
        )
    )
    ticketing_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingDate",
            type="Attribute"
        )
    )
    return_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ReturnDate",
            type="Attribute"
        )
    )
    base_fare_only: bool = field(
        default=False,
        metadata=dict(
            name="BaseFareOnly",
            type="Attribute"
        )
    )
    unrestricted_fares_only: bool = field(
        default=False,
        metadata=dict(
            name="UnrestrictedFaresOnly",
            type="Attribute"
        )
    )
    fares_indicator: Optional[TypeFaresIndicator] = field(
        default=None,
        metadata=dict(
            name="FaresIndicator",
            type="Attribute"
        )
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            length=3
        )
    )
    include_taxes: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeTaxes",
            type="Attribute"
        )
    )
    include_estimated_taxes: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeEstimatedTaxes",
            type="Attribute"
        )
    )
    include_surcharges: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeSurcharges",
            type="Attribute"
        )
    )
    global_indicator: Optional[TypeAtpcoglobalIndicator] = field(
        default=None,
        metadata=dict(
            name="GlobalIndicator",
            type="Attribute"
        )
    )
    prohibit_min_stay_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitMinStayFares",
            type="Attribute"
        )
    )
    prohibit_max_stay_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitMaxStayFares",
            type="Attribute"
        )
    )
    prohibit_advance_purchase_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitAdvancePurchaseFares",
            type="Attribute"
        )
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitNonRefundableFares",
            type="Attribute"
        )
    )
    validated_fares_only: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ValidatedFaresOnly",
            type="Attribute"
        )
    )
    prohibit_travel_restricted_fares: bool = field(
        default=True,
        metadata=dict(
            name="ProhibitTravelRestrictedFares",
            type="Attribute"
        )
    )
    filed_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FiledCurrency",
            type="Attribute",
            length=3
        )
    )


@dataclass
class AirFareRulesModifier:
    """The modifiers for Air Fare Rules.

    :ivar air_fare_rule_category:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_fare_rule_category: List[AirFareRuleCategory] = field(
        default_factory=list,
        metadata=dict(
            name="AirFareRuleCategory",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirItineraryDetails:
    """Itinerary details containing brand details.

    :ivar air_segment_details:
    :ivar passenger_details:
    :ivar key: Air itinerary details key
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_details: List[AirSegmentDetails] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentDetails",
            type="Element",
            min_occurs=1,
            max_occurs=16
        )
    )
    passenger_details: List[PassengerDetails] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerDetails",
            type="Element",
            min_occurs=1,
            max_occurs=15
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AirLegModifiers:
    """
    :ivar permitted_cabins:
    :ivar preferred_cabins:
    :ivar permitted_carriers:
    :ivar prohibited_carriers:
    :ivar preferred_carriers:
    :ivar permitted_connection_points: This is the container to specify all permitted connection points. Applicable for 1G/1V/1P/1J.
    :ivar prohibited_connection_points: This is the container to specify all prohibited connection points. Applicable for 1G/1V/1P/1J.
    :ivar preferred_connection_points: This is the container to specify all preferred connection points. Applicable for 1G/1V only.
    :ivar permitted_booking_codes: This is the container to specify all permitted booking codes
    :ivar preferred_booking_codes:
    :ivar preferred_alliances:
    :ivar prohibited_booking_codes: This is the container to specify all prohibited booking codes
    :ivar disfavored_alliances:
    :ivar flight_type:
    :ivar anchor_flight_data:
    :ivar prohibit_overnight_layovers: If true, excludes connections if arrival time of first flight and departure time of second flight
                       is on 2 different calendar days. When used in conjunction with MaxConnectionTime, it would exclude all connections if the
                       connecting flights wait time exceeds the time specified in MaxConnectionTime.
    :ivar max_connection_time:
    :ivar return_first_available_only: If it is true then it will search for first
                            available for the booking code designated or any booking code in
                            same cabin.
    :ivar allow_direct_access: If it is true request will be sent directly to the carrier.
    :ivar prohibit_multi_airport_connection: Indicates whether to restrict multi-airport connections
    :ivar prefer_non_stop: When non-stops are preferred, the distribution of search results should skew heavily toward non-stop flights while still returning
                      some one stop flights for comparison and price competitiveness. The search request will ‘boost' the preference towards non-stops. If true then Non Stop
                      flights will be preferred.
    :ivar order_by: Indicates whether to sort by Journey Time, Deparature Time or Arrival Time
    :ivar max_journey_time: Maximum Journey Time for this leg (in hours) 0-99. Supported Providers 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    permitted_cabins: Optional[PermittedCabins] = field(
        default=None,
        metadata=dict(
            name="PermittedCabins",
            type="Element"
        )
    )
    preferred_cabins: Optional[PreferredCabins] = field(
        default=None,
        metadata=dict(
            name="PreferredCabins",
            type="Element"
        )
    )
    permitted_carriers: Optional[PermittedCarriers] = field(
        default=None,
        metadata=dict(
            name="PermittedCarriers",
            type="Element"
        )
    )
    prohibited_carriers: Optional[ProhibitedCarriers] = field(
        default=None,
        metadata=dict(
            name="ProhibitedCarriers",
            type="Element"
        )
    )
    preferred_carriers: Optional[PreferredCarriers] = field(
        default=None,
        metadata=dict(
            name="PreferredCarriers",
            type="Element"
        )
    )
    permitted_connection_points: Optional["AirLegModifiers.PermittedConnectionPoints"] = field(
        default=None,
        metadata=dict(
            name="PermittedConnectionPoints",
            type="Element"
        )
    )
    prohibited_connection_points: Optional["AirLegModifiers.ProhibitedConnectionPoints"] = field(
        default=None,
        metadata=dict(
            name="ProhibitedConnectionPoints",
            type="Element"
        )
    )
    preferred_connection_points: Optional["AirLegModifiers.PreferredConnectionPoints"] = field(
        default=None,
        metadata=dict(
            name="PreferredConnectionPoints",
            type="Element"
        )
    )
    permitted_booking_codes: Optional["AirLegModifiers.PermittedBookingCodes"] = field(
        default=None,
        metadata=dict(
            name="PermittedBookingCodes",
            type="Element"
        )
    )
    preferred_booking_codes: Optional[PreferredBookingCodes] = field(
        default=None,
        metadata=dict(
            name="PreferredBookingCodes",
            type="Element"
        )
    )
    preferred_alliances: Optional["AirLegModifiers.PreferredAlliances"] = field(
        default=None,
        metadata=dict(
            name="PreferredAlliances",
            type="Element"
        )
    )
    prohibited_booking_codes: Optional["AirLegModifiers.ProhibitedBookingCodes"] = field(
        default=None,
        metadata=dict(
            name="ProhibitedBookingCodes",
            type="Element"
        )
    )
    disfavored_alliances: Optional["AirLegModifiers.DisfavoredAlliances"] = field(
        default=None,
        metadata=dict(
            name="DisfavoredAlliances",
            type="Element"
        )
    )
    flight_type: Optional[FlightType] = field(
        default=None,
        metadata=dict(
            name="FlightType",
            type="Element"
        )
    )
    anchor_flight_data: Optional[TypeAnchorFlightData] = field(
        default=None,
        metadata=dict(
            name="AnchorFlightData",
            type="Element"
        )
    )
    prohibit_overnight_layovers: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitOvernightLayovers",
            type="Attribute"
        )
    )
    max_connection_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MaxConnectionTime",
            type="Attribute"
        )
    )
    return_first_available_only: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ReturnFirstAvailableOnly",
            type="Attribute"
        )
    )
    allow_direct_access: bool = field(
        default=False,
        metadata=dict(
            name="AllowDirectAccess",
            type="Attribute"
        )
    )
    prohibit_multi_airport_connection: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ProhibitMultiAirportConnection",
            type="Attribute"
        )
    )
    prefer_non_stop: bool = field(
        default=False,
        metadata=dict(
            name="PreferNonStop",
            type="Attribute"
        )
    )
    order_by: Optional["AirLegModifiers.OrderBy"] = field(
        default=None,
        metadata=dict(
            name="OrderBy",
            type="Attribute"
        )
    )
    max_journey_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MaxJourneyTime",
            type="Attribute",
            min_inclusive=0,
            max_inclusive=99
        )
    )

    @dataclass
    class PermittedConnectionPoints:
        """
        :ivar connection_point:
        """
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata=dict(
                name="ConnectionPoint",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedConnectionPoints:
        """
        :ivar connection_point:
        """
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata=dict(
                name="ConnectionPoint",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PreferredConnectionPoints:
        """
        :ivar connection_point:
        """
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata=dict(
                name="ConnectionPoint",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=99
            )
        )

    @dataclass
    class PermittedBookingCodes:
        """
        :ivar booking_code:
        """
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata=dict(
                name="BookingCode",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PreferredAlliances:
        """
        :ivar alliance:
        """
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata=dict(
                name="Alliance",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedBookingCodes:
        """
        :ivar booking_code:
        """
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata=dict(
                name="BookingCode",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class DisfavoredAlliances:
        """
        :ivar alliance:
        """
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata=dict(
                name="Alliance",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

    class OrderBy(Enum):
        """
        :cvar JOURNEY_TIME:
        :cvar DEPARTURE_TIME:
        :cvar ARRIVAL_TIME:
        """
        JOURNEY_TIME = "JourneyTime"
        DEPARTURE_TIME = "DepartureTime"
        ARRIVAL_TIME = "ArrivalTime"


@dataclass
class AirPricingModifiers:
    """Controls and switches for a Air Search request that contains Pricing
    Information.

    :ivar prohibited_rule_categories:
    :ivar account_codes:
    :ivar permitted_cabins:
    :ivar contract_codes:
    :ivar exempt_taxes:
    :ivar penalty_fare_information: Request Fares with specific Penalty
                                Information.
    :ivar discount_card: Discount request for rail.
    :ivar promo_codes:
    :ivar manual_fare_adjustment: Represents increment/discount applied manually by agent.
    :ivar point_of_sale: User can use this node to send a specific PCC to access fares allowed only for that PCC. This node gives the capability for fare redistribution at stored fare level. As multiple UAPI AirPricingInfos (all having same AirPricingInfoGroup) can converge to a single stored fare, UAPI will map PoinOfSale information from the first available one from each group
    :ivar brand_modifiers: Used to specify the level of branding requested.
    :ivar multi_gdssearch_indicator:
    :ivar preferred_cabins:
    :ivar prohibit_min_stay_fares:
    :ivar prohibit_max_stay_fares:
    :ivar currency_type:
    :ivar prohibit_advance_purchase_fares:
    :ivar prohibit_non_refundable_fares:
    :ivar prohibit_restricted_fares:
    :ivar fares_indicator: Indicates whether only public fares
                            should be returned or specific type of private fares
    :ivar filed_currency: Currency in which Fares/Prices will be filed if supported by the supplier else approximated to.
    :ivar plating_carrier: The Plating Carrier for this journey.
    :ivar override_carrier: The Plating Carrier for this journey.
    :ivar eticketability: Request a search based on whether only
                            E-ticketable fares are required.
    :ivar account_code_fares_only: Indicates whether or not the private
                            fares returned should be restricted to only those specific to the
                            input account code and contract code.
    :ivar key:
    :ivar prohibit_non_exchangeable_fares:
    :ivar force_segment_select: This indicator allows agent to force segment select option in host while selecting all air segments to store price on a PNR. This is relevent only when agent selects all air segmnets to price. if agent selects specific segments to price then this attribute will be ignored by the system. This is currently used by Worldspan only.
    :ivar inventory_request_type: This allows user to make request for a particular source of inventory for pricing modifier purposes. This is currently used by Worldspan only.
    :ivar one_way_shop: Via this attribute one way shop can be requested. Applicable provider is 1G
    :ivar prohibit_unbundled_fare_types: A "True" value wiill remove fares with EOU and ERU fare types from consideration. A "False" value is the same as no value.  Default is no value. Applicable providers:  1P/1J/1G/1V
    :ivar return_services: When set to false, ATPCO filed Optional Services will not be returned. Default is true. Provider: 1G, 1V, 1P, 1J
    :ivar channel_id: A Channel ID is 2 to 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.
    :ivar return_fare_attributes: Returns attributes that are associated to a fare
    :ivar sell_check: Checks if the segment is bookable before pricing
    :ivar return_failed_segments: If "true", returns failed segments information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    prohibited_rule_categories: Optional["AirPricingModifiers.ProhibitedRuleCategories"] = field(
        default=None,
        metadata=dict(
            name="ProhibitedRuleCategories",
            type="Element"
        )
    )
    account_codes: Optional["AirPricingModifiers.AccountCodes"] = field(
        default=None,
        metadata=dict(
            name="AccountCodes",
            type="Element"
        )
    )
    permitted_cabins: Optional[PermittedCabins] = field(
        default=None,
        metadata=dict(
            name="PermittedCabins",
            type="Element"
        )
    )
    contract_codes: Optional["AirPricingModifiers.ContractCodes"] = field(
        default=None,
        metadata=dict(
            name="ContractCodes",
            type="Element"
        )
    )
    exempt_taxes: Optional[ExemptTaxes] = field(
        default=None,
        metadata=dict(
            name="ExemptTaxes",
            type="Element"
        )
    )
    penalty_fare_information: Optional[PenaltyFareInformation] = field(
        default=None,
        metadata=dict(
            name="PenaltyFareInformation",
            type="Element"
        )
    )
    discount_card: List[DiscountCard] = field(
        default_factory=list,
        metadata=dict(
            name="DiscountCard",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=9
        )
    )
    promo_codes: Optional["AirPricingModifiers.PromoCodes"] = field(
        default=None,
        metadata=dict(
            name="PromoCodes",
            type="Element"
        )
    )
    manual_fare_adjustment: List[ManualFareAdjustment] = field(
        default_factory=list,
        metadata=dict(
            name="ManualFareAdjustment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    point_of_sale: Optional[PointOfSale] = field(
        default=None,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    brand_modifiers: Optional[BrandModifiers] = field(
        default=None,
        metadata=dict(
            name="BrandModifiers",
            type="Element"
        )
    )
    multi_gdssearch_indicator: List[MultiGdssearchIndicator] = field(
        default_factory=list,
        metadata=dict(
            name="MultiGDSSearchIndicator",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    preferred_cabins: List[PreferredCabins] = field(
        default_factory=list,
        metadata=dict(
            name="PreferredCabins",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    prohibit_min_stay_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitMinStayFares",
            type="Attribute"
        )
    )
    prohibit_max_stay_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitMaxStayFares",
            type="Attribute"
        )
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            length=3
        )
    )
    prohibit_advance_purchase_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitAdvancePurchaseFares",
            type="Attribute"
        )
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitNonRefundableFares",
            type="Attribute"
        )
    )
    prohibit_restricted_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitRestrictedFares",
            type="Attribute"
        )
    )
    fares_indicator: Optional[TypeFaresIndicator] = field(
        default=None,
        metadata=dict(
            name="FaresIndicator",
            type="Attribute"
        )
    )
    filed_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FiledCurrency",
            type="Attribute",
            length=3
        )
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            length=2
        )
    )
    override_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OverrideCarrier",
            type="Attribute",
            length=2
        )
    )
    eticketability: Optional[TypeEticketability] = field(
        default=None,
        metadata=dict(
            name="ETicketability",
            type="Attribute"
        )
    )
    account_code_fares_only: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AccountCodeFaresOnly",
            type="Attribute"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    prohibit_non_exchangeable_fares: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitNonExchangeableFares",
            type="Attribute"
        )
    )
    force_segment_select: bool = field(
        default=False,
        metadata=dict(
            name="ForceSegmentSelect",
            type="Attribute"
        )
    )
    inventory_request_type: Optional[TypeInventoryRequest] = field(
        default=None,
        metadata=dict(
            name="InventoryRequestType",
            type="Attribute"
        )
    )
    one_way_shop: bool = field(
        default=False,
        metadata=dict(
            name="OneWayShop",
            type="Attribute"
        )
    )
    prohibit_unbundled_fare_types: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ProhibitUnbundledFareTypes",
            type="Attribute"
        )
    )
    return_services: bool = field(
        default=True,
        metadata=dict(
            name="ReturnServices",
            type="Attribute"
        )
    )
    channel_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ChannelId",
            type="Attribute",
            min_length=2,
            max_length=4
        )
    )
    return_fare_attributes: bool = field(
        default=False,
        metadata=dict(
            name="ReturnFareAttributes",
            type="Attribute"
        )
    )
    sell_check: bool = field(
        default=False,
        metadata=dict(
            name="SellCheck",
            type="Attribute"
        )
    )
    return_failed_segments: bool = field(
        default=False,
        metadata=dict(
            name="ReturnFailedSegments",
            type="Attribute"
        )
    )

    @dataclass
    class ProhibitedRuleCategories:
        """
        :ivar fare_rule_category:
        """
        fare_rule_category: List[FareRuleCategory] = field(
            default_factory=list,
            metadata=dict(
                name="FareRuleCategory",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class AccountCodes:
        """
        :ivar account_code: Used to get negotiated pricing. Provider:ACH.
        """
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata=dict(
                name="AccountCode",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ContractCodes:
        """
        :ivar contract_code:
        """
        contract_code: List[ContractCode] = field(
            default_factory=list,
            metadata=dict(
                name="ContractCode",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PromoCodes:
        """
        :ivar promo_code:
        """
        promo_code: List[PromoCode] = field(
            default_factory=list,
            metadata=dict(
                name="PromoCode",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class AirRefundBundle:
    """Bundle refund, pricing, and penalty information for one ticket number Used
    both in request and response.

    :ivar air_refund_info:
    :ivar name:
    :ivar tax_info:
    :ivar waiver_code:
    :ivar ticket_number:
    :ivar ptc: Specifies the passenger type code for 1P
    :ivar refund_type: Specifies whether this bundle was auto
                            or manually generated
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_refund_info: Optional[AirRefundInfo] = field(
        default=None,
        metadata=dict(
            name="AirRefundInfo",
            type="Element",
            required=True
        )
    )
    name: List[Name] = field(
        default_factory=list,
        metadata=dict(
            name="Name",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element"
        )
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute"
        )
    )
    ptc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PTC",
            type="Attribute"
        )
    )
    refund_type: Optional["AirRefundBundle.RefundType"] = field(
        default=None,
        metadata=dict(
            name="RefundType",
            type="Attribute"
        )
    )

    class RefundType(Enum):
        """
        :cvar AUTO:
        :cvar MANUAL:
        """
        AUTO = "Auto"
        MANUAL = "Manual"


@dataclass
class AirSearchModifiers:
    """Controls and switches for the Air Search request.

    :ivar disfavored_providers:
    :ivar preferred_providers:
    :ivar disfavored_carriers:
    :ivar permitted_carriers:
    :ivar prohibited_carriers:
    :ivar preferred_carriers:
    :ivar permitted_cabins:
    :ivar preferred_cabins:
    :ivar preferred_alliances:
    :ivar disfavored_alliances:
    :ivar permitted_booking_codes: This is the container to specify all permitted booking codes
    :ivar preferred_booking_codes:
    :ivar prohibited_booking_codes: This is the container to specify all prohibited booking codes
    :ivar flight_type:
    :ivar max_layover_duration: This is the maximum duration the layover may have for each trip in the request. Supported providers 1P, 1J.
    :ivar native_search_modifier: Container for Native command modifiers. Providers supported : 1P
    :ivar distance_type:
    :ivar include_flight_details:
    :ivar allow_change_of_airport:
    :ivar prohibit_overnight_layovers: If true, excludes connections if arrival time of first flight and departure time of second flight
                       is on 2 different calendar days. When used in conjunction with MaxConnectionTime, it would exclude all connections if the
                       connecting flights wait time exceeds the time specified in MaxConnectionTime.
    :ivar max_solutions: The maximum number of solutions to return.
                            Decreasing this number
    :ivar max_connection_time: The maximum anount of time (in minutes) that a
                            solution can contain for connections between flights.
    :ivar search_weekends: A value of true indicates that search should be
                            expanded to include weekend combinations, if applicable.
    :ivar include_extra_solutions: If true, indicates that search should be made
                            for returning more solutions, if available. For example, for
                            certain providers, premium members may have the facility to get
                            more solutions. This attribute may have to be combined with other
                            applicable modifiers (like SearchWeekends) to return more results.
    :ivar prohibit_multi_airport_connection: Indicates whether to restrict multi-airport connections
    :ivar prefer_non_stop: When non-stops are preferred, the distribution of search results should skew heavily toward non-stop flights while still returning
                      some one stop flights for comparison and price competitiveness. The search request will ‘boost' the preference towards non-stops. If true then Non Stop
                      flights will be preferred.
    :ivar order_by: Indicates whether to sort by Journey Time, Deparature Time or Arrival Time. Applicable to air availability only.
    :ivar exclude_open_jaw_airport: This option ensures that travel into/out of each location will be into/out of the same airport of that location. Values are true or false. Default value is 'false'. If value is true then open jaws are exclude. If false the open jaws are included. The supported providers: 1P, 1J
    :ivar exclude_ground_transportation: Indicates whether to allow the user to exclude ground transportation or not. Default value is 'false'. If value is true then ground transportations are excluded. If false then ground transportations are included. The supported providers: 1P, 1J
    :ivar max_journey_time: Maximum Journey Time for all legs (in hours) 0-99. For LFS Supported Providers are 1G,1V,1P,1J. For AirAvail Supported Providers are 1G,1V.
    :ivar jet_service_only: Restricts results to Jet service flights only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    disfavored_providers: Optional["AirSearchModifiers.DisfavoredProviders"] = field(
        default=None,
        metadata=dict(
            name="DisfavoredProviders",
            type="Element"
        )
    )
    preferred_providers: Optional["AirSearchModifiers.PreferredProviders"] = field(
        default=None,
        metadata=dict(
            name="PreferredProviders",
            type="Element"
        )
    )
    disfavored_carriers: Optional["AirSearchModifiers.DisfavoredCarriers"] = field(
        default=None,
        metadata=dict(
            name="DisfavoredCarriers",
            type="Element"
        )
    )
    permitted_carriers: Optional[PermittedCarriers] = field(
        default=None,
        metadata=dict(
            name="PermittedCarriers",
            type="Element"
        )
    )
    prohibited_carriers: Optional[ProhibitedCarriers] = field(
        default=None,
        metadata=dict(
            name="ProhibitedCarriers",
            type="Element"
        )
    )
    preferred_carriers: Optional[PreferredCarriers] = field(
        default=None,
        metadata=dict(
            name="PreferredCarriers",
            type="Element"
        )
    )
    permitted_cabins: Optional[PermittedCabins] = field(
        default=None,
        metadata=dict(
            name="PermittedCabins",
            type="Element"
        )
    )
    preferred_cabins: Optional[PreferredCabins] = field(
        default=None,
        metadata=dict(
            name="PreferredCabins",
            type="Element"
        )
    )
    preferred_alliances: Optional["AirSearchModifiers.PreferredAlliances"] = field(
        default=None,
        metadata=dict(
            name="PreferredAlliances",
            type="Element"
        )
    )
    disfavored_alliances: Optional["AirSearchModifiers.DisfavoredAlliances"] = field(
        default=None,
        metadata=dict(
            name="DisfavoredAlliances",
            type="Element"
        )
    )
    permitted_booking_codes: Optional["AirSearchModifiers.PermittedBookingCodes"] = field(
        default=None,
        metadata=dict(
            name="PermittedBookingCodes",
            type="Element"
        )
    )
    preferred_booking_codes: Optional[PreferredBookingCodes] = field(
        default=None,
        metadata=dict(
            name="PreferredBookingCodes",
            type="Element"
        )
    )
    prohibited_booking_codes: Optional["AirSearchModifiers.ProhibitedBookingCodes"] = field(
        default=None,
        metadata=dict(
            name="ProhibitedBookingCodes",
            type="Element"
        )
    )
    flight_type: Optional[FlightType] = field(
        default=None,
        metadata=dict(
            name="FlightType",
            type="Element"
        )
    )
    max_layover_duration: Optional[MaxLayoverDurationType] = field(
        default=None,
        metadata=dict(
            name="MaxLayoverDuration",
            type="Element"
        )
    )
    native_search_modifier: Optional[TypeNativeSearchModifier] = field(
        default=None,
        metadata=dict(
            name="NativeSearchModifier",
            type="Element"
        )
    )
    distance_type: TypeDistance = field(
        default=TypeDistance.MI,
        metadata=dict(
            name="DistanceType",
            type="Attribute"
        )
    )
    include_flight_details: bool = field(
        default=True,
        metadata=dict(
            name="IncludeFlightDetails",
            type="Attribute"
        )
    )
    allow_change_of_airport: bool = field(
        default=True,
        metadata=dict(
            name="AllowChangeOfAirport",
            type="Attribute"
        )
    )
    prohibit_overnight_layovers: bool = field(
        default=False,
        metadata=dict(
            name="ProhibitOvernightLayovers",
            type="Attribute"
        )
    )
    max_solutions: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MaxSolutions",
            type="Attribute"
        )
    )
    max_connection_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MaxConnectionTime",
            type="Attribute"
        )
    )
    search_weekends: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="SearchWeekends",
            type="Attribute"
        )
    )
    include_extra_solutions: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeExtraSolutions",
            type="Attribute"
        )
    )
    prohibit_multi_airport_connection: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ProhibitMultiAirportConnection",
            type="Attribute"
        )
    )
    prefer_non_stop: bool = field(
        default=False,
        metadata=dict(
            name="PreferNonStop",
            type="Attribute"
        )
    )
    order_by: Optional["AirSearchModifiers.OrderBy"] = field(
        default=None,
        metadata=dict(
            name="OrderBy",
            type="Attribute"
        )
    )
    exclude_open_jaw_airport: bool = field(
        default=False,
        metadata=dict(
            name="ExcludeOpenJawAirport",
            type="Attribute"
        )
    )
    exclude_ground_transportation: bool = field(
        default=False,
        metadata=dict(
            name="ExcludeGroundTransportation",
            type="Attribute"
        )
    )
    max_journey_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MaxJourneyTime",
            type="Attribute",
            min_inclusive=0,
            max_inclusive=99
        )
    )
    jet_service_only: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="JetServiceOnly",
            type="Attribute"
        )
    )

    @dataclass
    class DisfavoredProviders:
        """
        :ivar provider:
        """
        provider: List[Provider] = field(
            default_factory=list,
            metadata=dict(
                name="Provider",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PreferredProviders:
        """
        :ivar provider:
        """
        provider: List[Provider] = field(
            default_factory=list,
            metadata=dict(
                name="Provider",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class DisfavoredCarriers:
        """
        :ivar carrier:
        """
        carrier: List[Carrier] = field(
            default_factory=list,
            metadata=dict(
                name="Carrier",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PreferredAlliances:
        """
        :ivar alliance:
        """
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata=dict(
                name="Alliance",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class DisfavoredAlliances:
        """
        :ivar alliance:
        """
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata=dict(
                name="Alliance",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PermittedBookingCodes:
        """
        :ivar booking_code:
        """
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata=dict(
                name="BookingCode",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedBookingCodes:
        """
        :ivar booking_code:
        """
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata=dict(
                name="BookingCode",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )

    class OrderBy(Enum):
        """
        :cvar JOURNEY_TIME:
        :cvar DEPARTURE_TIME:
        :cvar ARRIVAL_TIME:
        """
        JOURNEY_TIME = "JourneyTime"
        DEPARTURE_TIME = "DepartureTime"
        ARRIVAL_TIME = "ArrivalTime"


@dataclass
class AlternateLocationDistanceList:
    """Provides the Distance Information between Original Search Airports or City
    to Alternate Search Airports.

    :ivar alternate_location_distance:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    alternate_location_distance: List[AlternateLocationDistance] = field(
        default_factory=list,
        metadata=dict(
            name="AlternateLocationDistance",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AlternateRoute:
    """Information about this Alternate Route component.

    :ivar leg:
    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    leg: List[Leg] = field(
        default_factory=list,
        metadata=dict(
            name="Leg",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AuditData:
    """Container for Pricing Audit Data.For providers 1P/1J.

    :ivar tax_info:
    :ivar key:
    :ivar total_price: The total price for this entity including base price and all taxes.
    :ivar base_price: Represents the base price for this entity. This does not include any taxes or surcharges.
    :ivar approximate_total_price: The Converted total price in Default Currency for this entity including base price and all taxes.
    :ivar approximate_base_price: The Converted base price in Default Currency for this entity. This does not include any taxes or surcharges.
    :ivar equivalent_base_price: Represents the base price in the related currency for this entity. This does not include any taxes or surcharges.
    :ivar taxes: The aggregated amount of all the taxes that are associated with this entity. See the associated TaxInfo array for a breakdown of the individual taxes.
    :ivar fees: The aggregated amount of all the fees that are associated with this entity. See the associated FeeInfo array for a breakdown of the individual fees.
    :ivar services: The total cost for all optional services.
    :ivar approximate_taxes: The Converted tax amount in Default Currency.
    :ivar approximate_fees: The Converted fee amount in Default Currency.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute"
        )
    )
    base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute"
        )
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute"
        )
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateBasePrice",
            type="Attribute"
        )
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EquivalentBasePrice",
            type="Attribute"
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Attribute"
        )
    )
    services: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Services",
            type="Attribute"
        )
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTaxes",
            type="Attribute"
        )
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateFees",
            type="Attribute"
        )
    )


@dataclass
class BaggageAllowance:
    """Free Baggage Allowance.

    :ivar number_of_pieces:
    :ivar max_weight:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    number_of_pieces: Optional[int] = field(
        default=None,
        metadata=dict(
            name="NumberOfPieces",
            type="Element"
        )
    )
    max_weight: Optional[TypeWeight] = field(
        default=None,
        metadata=dict(
            name="MaxWeight",
            type="Element"
        )
    )


@dataclass
class BaggageRestriction:
    """Information related to  Baggage restriction rules .

    :ivar dimension:
    :ivar max_weight:
    :ivar text_info:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    dimension: List[Dimension] = field(
        default_factory=list,
        metadata=dict(
            name="Dimension",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    max_weight: List[TypeUnitOfMeasure] = field(
        default_factory=list,
        metadata=dict(
            name="MaxWeight",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    text_info: List[TextInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TextInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class BookingRules:
    """Rules related to pre pay booking.

    :ivar booking_rules_fare_reference:
    :ivar rule_info: Pre pay booking rule information
    :ivar restriction: Booking restrictions for associated pre pay account
    :ivar document_required: Detail about required documents for this pre pay id
    :ivar gender_dob_required: Vendor populates if gender/DOB data is required in book.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_rules_fare_reference: List[BookingRulesFareReference] = field(
        default_factory=list,
        metadata=dict(
            name="BookingRulesFareReference",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    rule_info: List["BookingRules.RuleInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="RuleInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    restriction: List[Restriction] = field(
        default_factory=list,
        metadata=dict(
            name="Restriction",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    document_required: List[DocumentRequired] = field(
        default_factory=list,
        metadata=dict(
            name="DocumentRequired",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    gender_dob_required: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="GenderDobRequired",
            type="Attribute"
        )
    )

    @dataclass
    class RuleInfo:
        """
        :ivar charges_rules:
        """
        charges_rules: Optional[ChargesRules] = field(
            default=None,
            metadata=dict(
                name="ChargesRules",
                type="Element"
            )
        )


@dataclass
class BrandingInfo:
    """Branding information for the Ancillary Service.  Returned in Seat Map only.
    Providers: 1G, 1V, 1P, 1J, ACH.

    :ivar price_range: The price range of the Ancillary Service.  Providers: 1G, 1V, 1P, 1J, ACH
    :ivar text:
    :ivar title: The additional titles associated to the brand or optional service. Providers: ACH, 1G, 1V, 1P, 1J
    :ivar image_location:
    :ivar service_group:
    :ivar air_segment_ref: Specifies the AirSegment the branding information is for. Providers: ACH, 1G, 1V, 1P, 1J
    :ivar key:
    :ivar service_sub_code: The Service Sub Code of the Ancillary Service.  Providers: 1G, 1V, 1P, 1J, ACH
    :ivar external_service_name: The external name of the Ancillary Service.  Providers: 1G, 1V, 1P, 1J, ACH
    :ivar service_type: The type of Ancillary Service.  Providers: 1G, 1V, 1P, 1J, ACH
    :ivar commercial_name: The commercial name of the Ancillary Service.  Providers: 1G, 1V, 1P, 1J, ACH
    :ivar chargeable: Indicates if the optional service is not offered, is available for a charge, or is included in the brand.  Providers: 1G, 1V, 1P, 1J, ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    price_range: List[PriceRange] = field(
        default_factory=list,
        metadata=dict(
            name="PriceRange",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    text: List[Text] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    title: List[Title] = field(
        default_factory=list,
        metadata=dict(
            name="Title",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata=dict(
            name="ImageLocation",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    service_group: Optional[ServiceGroup] = field(
        default=None,
        metadata=dict(
            name="ServiceGroup",
            type="Element"
        )
    )
    air_segment_ref: List[CommonTypeSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute"
        )
    )
    external_service_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ExternalServiceName",
            type="Attribute"
        )
    )
    service_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ServiceType",
            type="Attribute"
        )
    )
    commercial_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CommercialName",
            type="Attribute",
            required=True
        )
    )
    chargeable: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Chargeable",
            type="Attribute"
        )
    )


@dataclass
class BundledServices:
    """
    :ivar bundled_service:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    bundled_service: List[BundledService] = field(
        default_factory=list,
        metadata=dict(
            name="BundledService",
            type="Element",
            min_occurs=0,
            max_occurs=16
        )
    )


@dataclass
class Connection:
    """Flight Connection Information.

    :ivar fare_note:
    :ivar change_of_plane: Indicates the traveler must change
                            planes between flights.
    :ivar change_of_terminal: Indicates the traveler must change
                            terminals between flights.
    :ivar change_of_airport: Indicates the traveler must change
                            airports between flights.
    :ivar stop_over: Indicates that there is a significant
                            delay between flights (usually 12 hours or more)
    :ivar min_connection_time: The minimum time needed to connect between the
                            two different destinations.
    :ivar duration: The actual duration (in minutes) between
                            flights.
    :ivar segment_index: The sequential AirSegment number that this
                            connection information applies to.
    :ivar flight_details_index: The sequential FlightDetails number that this
                            connection information applies to.
    :ivar include_stop_over_to_fare_quote: The field determines to quote fares with or
                            without stop overs,the values can be NoStopOver,StopOver and
                            IgnoreSegment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_note: Optional[FareNote] = field(
        default=None,
        metadata=dict(
            name="FareNote",
            type="Element"
        )
    )
    change_of_plane: bool = field(
        default=False,
        metadata=dict(
            name="ChangeOfPlane",
            type="Attribute"
        )
    )
    change_of_terminal: bool = field(
        default=False,
        metadata=dict(
            name="ChangeOfTerminal",
            type="Attribute"
        )
    )
    change_of_airport: bool = field(
        default=False,
        metadata=dict(
            name="ChangeOfAirport",
            type="Attribute"
        )
    )
    stop_over: bool = field(
        default=False,
        metadata=dict(
            name="StopOver",
            type="Attribute"
        )
    )
    min_connection_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MinConnectionTime",
            type="Attribute"
        )
    )
    duration: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Duration",
            type="Attribute"
        )
    )
    segment_index: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SegmentIndex",
            type="Attribute"
        )
    )
    flight_details_index: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FlightDetailsIndex",
            type="Attribute"
        )
    )
    include_stop_over_to_fare_quote: Optional[TypeIgnoreStopOver] = field(
        default=None,
        metadata=dict(
            name="IncludeStopOverToFareQuote",
            type="Attribute"
        )
    )


@dataclass
class DetailedBillingInformation:
    """Container to send Detailed Billing Information for ticketing.

    :ivar form_of_payment_ref:
    :ivar air_pricing_info_ref: Returns related air pricing infos.
    :ivar billing_detail_item:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    billing_detail_item: List[BillingDetailItem] = field(
        default_factory=list,
        metadata=dict(
            name="BillingDetailItem",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class DocumentSelect:
    """Allows an agency to select the documents to produce for the itinerary.

    :ivar back_office_hand_off:
    :ivar itinerary:
    :ivar issue_ticket_only: Set to true to alter system default of
                            itinerary,ticket and back office.
    :ivar issue_electronic_ticket: Set to true for electronic tickets.
    :ivar fax_indicator: Set to true for providing fax details.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    back_office_hand_off: Optional[BackOfficeHandOff] = field(
        default=None,
        metadata=dict(
            name="BackOfficeHandOff",
            type="Element"
        )
    )
    itinerary: Optional[Itinerary] = field(
        default=None,
        metadata=dict(
            name="Itinerary",
            type="Element"
        )
    )
    issue_ticket_only: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IssueTicketOnly",
            type="Attribute"
        )
    )
    issue_electronic_ticket: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IssueElectronicTicket",
            type="Attribute"
        )
    )
    fax_indicator: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="FaxIndicator",
            type="Attribute"
        )
    )


@dataclass
class EmdpricingInfo:
    """Fare related information for these electronic miscellaneous documents.
    Supported providers are 1G/1V/1P/1J.

    :ivar tax_info:
    :ivar base_fare:
    :ivar total_fare:
    :ivar total_tax:
    :ivar equiv_fare:
    """
    class Meta:
        name = "EMDPricingInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    base_fare: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BaseFare",
            type="Attribute"
        )
    )
    total_fare: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalFare",
            type="Attribute"
        )
    )
    total_tax: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalTax",
            type="Attribute"
        )
    )
    equiv_fare: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EquivFare",
            type="Attribute"
        )
    )


@dataclass
class Emdsummary:
    """EMD summary information. Supported providers are 1G/1V/1P/1J.

    :ivar emdcoupon: The coupon information for the EMD issued.
    :ivar number: EMD Number
    :ivar primary_document_indicator: Indicates whether the EMD is a primary EMD.
    :ivar in_conjunction_with: Returns the number of the Primary EMD, if this EMD is a conjunctive EMD
    :ivar associated_ticket_number: This number indicates the e-Ticket number associated with this EMD
    :ivar plating_carrier: Plating carrier code for which this EMD is issued
    :ivar issue_date: Issue Date for this EMD
    :ivar key: System generated Key
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        name = "EMDSummary"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdcoupon: List[Emdcoupon] = field(
        default_factory=list,
        metadata=dict(
            name="EMDCoupon",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True,
            length=13
        )
    )
    primary_document_indicator: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="PrimaryDocumentIndicator",
            type="Attribute"
        )
    )
    in_conjunction_with: Optional[str] = field(
        default=None,
        metadata=dict(
            name="InConjunctionWith",
            type="Attribute",
            length=13
        )
    )
    associated_ticket_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AssociatedTicketNumber",
            type="Attribute",
            length=13
        )
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            length=2
        )
    )
    issue_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IssueDate",
            type="Attribute"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class ElectronicMiscDocument:
    """Electronic miscellaneous document. Supported providers are 1G/1V/1P/1J.

    :ivar emdcoupon: The coupon information for the EMD issued.
    :ivar number: EMD Number
    :ivar primary_document_indicator: Indicates whether the EMD is a primary EMD.
    :ivar in_conjunction_with: Returns the number of the Primary EMD, if this EMD is a conjunctive EMD
    :ivar associated_ticket_number: This number indicates the e-Ticket number associated with this EMD
    :ivar plating_carrier: Plating carrier code for which this EMD is issued
    :ivar issue_date: Issue Date for this EMD
    :ivar status: Status of the EMD calculated on the basis of coupon status. Possible values Open, Void, Refunded, Exchanged, Irregular Operations,Airport Control, Checked In, Flown/Used, Boarded/Lifted, Suspended, Unknown
    :ivar key: System generated Key
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdcoupon: List[Emdcoupon] = field(
        default_factory=list,
        metadata=dict(
            name="EMDCoupon",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True,
            length=13
        )
    )
    primary_document_indicator: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="PrimaryDocumentIndicator",
            type="Attribute"
        )
    )
    in_conjunction_with: Optional[str] = field(
        default=None,
        metadata=dict(
            name="InConjunctionWith",
            type="Attribute",
            length=13
        )
    )
    associated_ticket_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AssociatedTicketNumber",
            type="Attribute",
            length=13
        )
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            length=2
        )
    )
    issue_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IssueDate",
            type="Attribute"
        )
    )
    status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class EmbargoInfo(BaseBaggageAllowanceInfo):
    """Information related to Embargo."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class Enumeration:
    """Provides the capability to group the results into differnt trip type and
    diversification strategies.

    :ivar solution_group:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    solution_group: List[SolutionGroup] = field(
        default_factory=list,
        metadata=dict(
            name="SolutionGroup",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class ExchangeEligibilityInfo:
    """
    :ivar exchange_penalty_info:
    :ivar eligible_fares: Identifies which fares are eligible for Exchange
    :ivar refundable_fares: Fares eligible for refund: All, Some, None
    :ivar passed_automation_checks: Indicates whether the itinerary passed initial validation for automated exchange
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    exchange_penalty_info: List[ExchangePenaltyInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangePenaltyInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    eligible_fares: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EligibleFares",
            type="Attribute"
        )
    )
    refundable_fares: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RefundableFares",
            type="Attribute"
        )
    )
    passed_automation_checks: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="PassedAutomationChecks",
            type="Attribute"
        )
    )


@dataclass
class ExpertSolution:
    """Information about Expert Solution Route component retrieved from Knowledge
    Base.

    :ivar leg_price:
    :ivar key:
    :ivar total_price: The Total Price for the Solution.
    :ivar approximate_total_price: The Converted Total Price in Agency's Default
                            Currency Value
    :ivar created_date: The Date on which this solution was created
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    leg_price: List[LegPrice] = field(
        default_factory=list,
        metadata=dict(
            name="LegPrice",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute"
        )
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute"
        )
    )
    created_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CreatedDate",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Facility:
    """The facility definition for a part of a row or a seat map.

    :ivar characteristic:
    :ivar remark:
    :ivar passenger_seat_price:
    :ivar tax_info: Tax information related to seat price. This is presently populated for MCH and ACH content. Applicable providers are MCH/ACH
    :ivar emd:
    :ivar service_data:
    :ivar tour_code:
    :ivar type: The type of facility
    :ivar seat_code: If a seat type, the seat identifier
    :ivar availability: If a seat type, the availability of the seat
    :ivar seat_price: The price of the seat, if applicable.
    :ivar paid: Set to True if either SeatPrice or GroupSeatPrice are returned.
    :ivar service_sub_code: The service subcode associated with the
                            Facility
    :ivar ssrcode: The SSR Code associated with the
                            Facility
    :ivar issuance_reason: A one-letter RFIC value filed by the airline in each Optional Service will be mapped to this attribute.
                           RFIC is IATA Reason for Issuance Code. Possible codes are A (Air transportation),B (Surface Transportation),C(Bagage),
                           D(Financial Impact),E(Airport Services),F(Merchandise),G(Inflight Services),I (Individual Airline use).
    :ivar base_seat_price: Price of the seats excluding Taxes.
    :ivar taxes: Tax amount for the seat price.
    :ivar quantity: The number of units availed for each optional
                            service (e.g. 2 baggage availed will be specified as 2 in quantity
                            for optional service BAGGAGE)
    :ivar sequence_number: The sequence number associated with the
                            OptionalService
    :ivar inclusive_of_tax: Identifies if the service was filed with a fee that is inclusive of tax.
    :ivar interline_settlement_allowed: Identifies if the interline settlement is allowed in service .
    :ivar geography_specification: Sector, Portion, Journey.
    :ivar source: The Source of the optional service. The source can be ACH, MCE, or MCH.
    :ivar optional_service_ref: References the OptionalService for the Row/Facility. Providers: ACH, 1G, 1V, 1P, 1J
    :ivar seat_information_ref: Specifies the seat information for the seat. Providers: ACH, 1G, 1V, 1P, 1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    characteristic: List[Characteristic] = field(
        default_factory=list,
        metadata=dict(
            name="Characteristic",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata=dict(
            name="Remark",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    passenger_seat_price: List[PassengerSeatPrice] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerSeatPrice",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    emd: Optional[Emd] = field(
        default=None,
        metadata=dict(
            name="EMD",
            type="Element"
        )
    )
    service_data: List[ServiceData] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceData",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    tour_code: Optional[TourCode] = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Element"
        )
    )
    type: Optional[TypeFacility] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    seat_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SeatCode",
            type="Attribute"
        )
    )
    availability: Optional[TypeSeatAvailability] = field(
        default=None,
        metadata=dict(
            name="Availability",
            type="Attribute"
        )
    )
    seat_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SeatPrice",
            type="Attribute"
        )
    )
    paid: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Paid",
            type="Attribute"
        )
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute",
            max_length=3
        )
    )
    ssrcode: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SSRCode",
            type="Attribute",
            min_length=4,
            max_length=4
        )
    )
    issuance_reason: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IssuanceReason",
            type="Attribute",
            min_length=1,
            max_length=1
        )
    )
    base_seat_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BaseSeatPrice",
            type="Attribute"
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    quantity: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Quantity",
            type="Attribute"
        )
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SequenceNumber",
            type="Attribute"
        )
    )
    inclusive_of_tax: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="InclusiveOfTax",
            type="Attribute"
        )
    )
    interline_settlement_allowed: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="InterlineSettlementAllowed",
            type="Attribute"
        )
    )
    geography_specification: Optional[str] = field(
        default=None,
        metadata=dict(
            name="GeographySpecification",
            type="Attribute"
        )
    )
    source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute"
        )
    )
    optional_service_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OptionalServiceRef",
            type="Attribute"
        )
    )
    seat_information_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SeatInformationRef",
            type="Attribute"
        )
    )


@dataclass
class FareNoteList:
    """The shared object list of Notes.

    :ivar fare_note:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata=dict(
            name="FareNote",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class FareRemarkList:
    """The shared object list of FareInfos.

    :ivar fare_remark:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_remark: List[FareRemark] = field(
        default_factory=list,
        metadata=dict(
            name="FareRemark",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FareRestriction:
    """Fare Restriction.

    :ivar fare_restriction_days_of_week:
    :ivar fare_restriction_date:
    :ivar fare_restriction_sale_date:
    :ivar fare_restriction_seasonal:
    :ivar fare_restrictiontype:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_restriction_days_of_week: List[FareRestrictionDaysOfWeek] = field(
        default_factory=list,
        metadata=dict(
            name="FareRestrictionDaysOfWeek",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    fare_restriction_date: List[FareRestrictionDate] = field(
        default_factory=list,
        metadata=dict(
            name="FareRestrictionDate",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_restriction_sale_date: Optional[FareRestrictionSaleDate] = field(
        default=None,
        metadata=dict(
            name="FareRestrictionSaleDate",
            type="Element"
        )
    )
    fare_restriction_seasonal: List[FareRestrictionSeasonal] = field(
        default_factory=list,
        metadata=dict(
            name="FareRestrictionSeasonal",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_restrictiontype: Optional[TypeFareRestrictionType] = field(
        default=None,
        metadata=dict(
            name="FareRestrictiontype",
            type="Attribute"
        )
    )


@dataclass
class FareRuleCategoryTypes:
    """
    :ivar category_details: To indicate details of which category is displayed
    :ivar variable_category_details: If the specified category of Structured Fare
    						Rules is of variable lenght
    :ivar value:
    """
    category_details: List[ValueDetails] = field(
        default_factory=list,
        metadata=dict(
            name="CategoryDetails",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )
    variable_category_details: List[CategoryDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="VariableCategoryDetails",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            required=True
        )
    )


@dataclass
class FareRulesFilter:
    """Fare Rules Filter about this fare component. Applicable Providers are
    1P,1J,1G,1V.

    :ivar refundability: Refundability/Penalty Fare Rules about this fare component.
    :ivar latest_ticketing_time: For Future Use
    :ivar chg: For Penalties
    :ivar min: For Minimum Stay
    :ivar max: For Maximum Stay
    :ivar adv: For Advance Res/Tkt
    :ivar oth: Other
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    refundability: Optional["FareRulesFilter.Refundability"] = field(
        default=None,
        metadata=dict(
            name="Refundability",
            type="Element"
        )
    )
    latest_ticketing_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LatestTicketingTime",
            type="Element"
        )
    )
    chg: Optional[Chgtype] = field(
        default=None,
        metadata=dict(
            name="CHG",
            type="Element"
        )
    )
    min: Optional[Mintype] = field(
        default=None,
        metadata=dict(
            name="MIN",
            type="Element"
        )
    )
    max: Optional[Maxtype] = field(
        default=None,
        metadata=dict(
            name="MAX",
            type="Element"
        )
    )
    adv: Optional[Advtype] = field(
        default=None,
        metadata=dict(
            name="ADV",
            type="Element"
        )
    )
    oth: Optional[Othtype] = field(
        default=None,
        metadata=dict(
            name="OTH",
            type="Element"
        )
    )

    @dataclass
    class Refundability:
        """
        :ivar value: Currently returned: FullyRefundable (1G,1V), RefundableWithPenalty (1G,1V), Refundable (1P,1J),  NonRefundable (1G,1V,1P,1J).Refundable.
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
class FaxDetails:
    """The Fax Details Information.

    :ivar phone_number: Send type as Fax for fax number.
    :ivar term_conditions: Term and Conditions for the fax .
    :ivar remark:
    :ivar include_cover_sheet: Specifies whether to include a cover page with fax or not.
    :ivar to: To address.
    :ivar from_value: From address.
    :ivar dept_billing_code: Department billing code.
    :ivar invoice_number: Invoice number.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    term_conditions: Optional[TermConditions] = field(
        default=None,
        metadata=dict(
            name="TermConditions",
            type="Element"
        )
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata=dict(
            name="Remark",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    include_cover_sheet: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeCoverSheet",
            type="Attribute"
        )
    )
    to: Optional[str] = field(
        default=None,
        metadata=dict(
            name="To",
            type="Attribute"
        )
    )
    from_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="From",
            type="Attribute"
        )
    )
    dept_billing_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DeptBillingCode",
            type="Attribute"
        )
    )
    invoice_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="InvoiceNumber",
            type="Attribute"
        )
    )


@dataclass
class FlightInfoDetail:
    """
    :ivar codeshare_info:
    :ivar meals:
    :ivar in_flight_services:
    :ivar variance:
    :ivar origin: The IATA location code for this origination of
                            this entity.
    :ivar destination: The IATA location code for this destination of
                            this entity.
    :ivar scheduled_departure_time: The date and time at which this entity is
                            scheduled to depart. This does not include time zone information
                            since it can be derived from the origin location.
    :ivar scheduled_arrival_time: The date and time at which this entity is
                            scheduled to arrive at the destination. This does not include time
                            zone information since it can be derived from the origin location.
    :ivar travel_time: Total time spent (minutes) traveling
                            including flight time and ground time.
    :ivar eticketability: Identifies if this particular segment
                            is E-Ticketable
    :ivar equipment:
    :ivar origin_terminal:
    :ivar origin_gate: To be used to display origin flight gate number
    :ivar destination_terminal:
    :ivar destination_gate: To be used to display destination flight gate number
    :ivar automated_checkin: “True” indicates that the flight allows automated check-in. The default is “False”.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    codeshare_info: Optional[CodeshareInfo] = field(
        default=None,
        metadata=dict(
            name="CodeshareInfo",
            type="Element"
        )
    )
    meals: List[Meals] = field(
        default_factory=list,
        metadata=dict(
            name="Meals",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    in_flight_services: List[InFlightServices] = field(
        default_factory=list,
        metadata=dict(
            name="InFlightServices",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    variance: List[Variance] = field(
        default_factory=list,
        metadata=dict(
            name="Variance",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    scheduled_departure_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ScheduledDepartureTime",
            type="Attribute"
        )
    )
    scheduled_arrival_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ScheduledArrivalTime",
            type="Attribute"
        )
    )
    travel_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute"
        )
    )
    eticketability: Optional[TypeEticketability] = field(
        default=None,
        metadata=dict(
            name="ETicketability",
            type="Attribute"
        )
    )
    equipment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Equipment",
            type="Attribute",
            length=3
        )
    )
    origin_terminal: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OriginTerminal",
            type="Attribute"
        )
    )
    origin_gate: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OriginGate",
            type="Attribute",
            max_length=6
        )
    )
    destination_terminal: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DestinationTerminal",
            type="Attribute"
        )
    )
    destination_gate: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DestinationGate",
            type="Attribute",
            max_length=6
        )
    )
    automated_checkin: bool = field(
        default=False,
        metadata=dict(
            name="AutomatedCheckin",
            type="Attribute"
        )
    )


@dataclass
class GeneralTimeTable:
    """
    :ivar days_of_operation:
    :ivar flight_origin:
    :ivar flight_destination:
    :ivar carrier_list:
    :ivar start_date:
    :ivar end_date:
    :ivar start_time: Flight start time of flight time tabel .
    :ivar end_time: Flight end time of flight time tabel .
    :ivar include_connection: Include or exclude connecting flights.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    days_of_operation: Optional[TypeDaysOfOperation] = field(
        default=None,
        metadata=dict(
            name="DaysOfOperation",
            type="Element"
        )
    )
    flight_origin: Optional[TypeLocation] = field(
        default=None,
        metadata=dict(
            name="FlightOrigin",
            type="Element",
            required=True
        )
    )
    flight_destination: Optional[TypeLocation] = field(
        default=None,
        metadata=dict(
            name="FlightDestination",
            type="Element",
            required=True
        )
    )
    carrier_list: Optional[CarrierList] = field(
        default=None,
        metadata=dict(
            name="CarrierList",
            type="Element"
        )
    )
    start_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute",
            required=True
        )
    )
    end_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EndDate",
            type="Attribute"
        )
    )
    start_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StartTime",
            type="Attribute"
        )
    )
    end_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EndTime",
            type="Attribute"
        )
    )
    include_connection: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludeConnection",
            type="Attribute"
        )
    )


@dataclass
class IssuanceModifiers:
    """General modifiers supported for EMD Issuance.Supported providers are
    1V/1G/1P/1J.

    :ivar form_of_payment_ref: Reference to FormOfPayment present in the UR to be used for EMD issuance.
    :ivar form_of_payment: FormOfPayment information to be used for EMD issuance.
    :ivar customer_receipt_info: Information about customer receipt via email.
    :ivar emdendorsement: Endorsement details to be used during EMD issuance.
    :ivar emdcommission: Commission information to be used for EMD issuance.
    :ivar plating_carrier: Plating carrier code for which this EMD is issued.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    customer_receipt_info: Optional[CustomerReceiptInfo] = field(
        default=None,
        metadata=dict(
            name="CustomerReceiptInfo",
            type="Element"
        )
    )
    emdendorsement: Optional[Emdendorsement] = field(
        default=None,
        metadata=dict(
            name="EMDEndorsement",
            type="Element"
        )
    )
    emdcommission: Optional[Emdcommission] = field(
        default=None,
        metadata=dict(
            name="EMDCommission",
            type="Element"
        )
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            length=2
        )
    )


@dataclass
class PassengerType(TypePassengerType):
    """The passenger type details associated to a fare.

    :ivar fare_guarantee_info:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_guarantee_info: Optional[FareGuaranteeInfo] = field(
        default=None,
        metadata=dict(
            name="FareGuaranteeInfo",
            type="Element"
        )
    )


@dataclass
class PrePayCustomer:
    """Detailed customer information for searching pre pay profiles.

    :ivar person_name:
    :ivar email: Customer email detail
    :ivar address: Customer address detail
    :ivar related_traveler: Travelers related to this pre pay id
    :ivar loyalty_card: Customer loyalty card detail
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    person_name: Optional[PersonName] = field(
        default=None,
        metadata=dict(
            name="PersonName",
            type="Element"
        )
    )
    email: List[Email] = field(
        default_factory=list,
        metadata=dict(
            name="Email",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    address: List[TypeStructuredAddress] = field(
        default_factory=list,
        metadata=dict(
            name="Address",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    related_traveler: List[RelatedTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="RelatedTraveler",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyCard",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class PrePayPriceInfo:
    """Pricing detail for the Pre Pay Account.

    :ivar tax_info: Detailed tax information for the pre pay account
    :ivar base_fare:
    :ivar total_fare:
    :ivar total_tax:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    base_fare: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BaseFare",
            type="Attribute"
        )
    )
    total_fare: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalFare",
            type="Attribute"
        )
    )
    total_tax: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalTax",
            type="Attribute"
        )
    )


@dataclass
class RepricingModifiers:
    """Used for rapid reprice to provide additional options for the reprice.
    Providers: 1G/1V/1P/1S/1A.

    :ivar private_fare_options: Public and/or Private Fares requested for pricing.            Currently supported: AccountCodeOnly, PrivateFaresOnly, PublicPrivateFaresOnly.
    :ivar fare_type:
    :ivar fare_ticket_designator:
    :ivar override_currency:
    :ivar air_segment_pricing_modifiers:
    :ivar withhold_tax_code: Used to request tax withholding for the tax code specified. Providers supported 1G/1P
    :ivar price_class_of_service: Values allowed are ClassBooked or LowestClass. This tells how to price the new itinerary.
    :ivar create_date: This is either today’s date or the date the repriced itinerary was created
    :ivar reissue_loc_city_code: This is the city code of the reissue location
    :ivar reissue_loc_country_code: This is the country code of the reissue location
    :ivar bulk_ticket: Set to true and the itinerary is/will be a bulk ticket.
                                            Set to false and the itinerary being repriced will not be a bulk ticket.
    :ivar account_code: May be used in conjunction with PrivateFareOptions
    :ivar penalty_as_tax_code: Used to request that the penalty be applied as a tax, to the tax code specified. Providers supported 1G/1P
    :ivar air_pricing_solution_ref: A reference to a AirPricingSolution. Providers: 1G, 1V, 1P, 1J.
    :ivar penalty_to_fare: Will add the change fee/penalty amount to the total fare amount. Supported Providers: 1P
    :ivar price_ptconly: A value of true forces the price for the PTC even if that fare is not the lowest fare for the passenger.
    :ivar brand_details: Set to true full brand details will be returned.
    :ivar brand_modifier: A value of MaintainBrand will maintain the brand from the original ticket if applicable.
    :ivar jet_service_only: Request flights that are jet service only. Available in AirExchangeMultiQuoteReq only.
    :ivar time_window: A value of Time Window is optional. Available in AirExchangeMultiQuoteReq only.
    :ivar flight_type: Type of flights to be returned. Values are 'NonStop', 'Direct', 'SingleConnection' and 'NoRestrictions'. Available in AirExchangeMultiQuoteReq only.
    :ivar multi_airport_search: A value of Multi Airport Search Indicator is optional. Available in AirExchangeMultiQuoteReq only.
    :ivar connection_point: A value of Connection City Code is optional. Available in AirExchangeMultiQuoteReq only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    private_fare_options: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PrivateFareOptions",
            type="Element",
            max_length=50
        )
    )
    fare_type: List[FareType] = field(
        default_factory=list,
        metadata=dict(
            name="FareType",
            type="Element",
            min_occurs=0,
            max_occurs=100
        )
    )
    fare_ticket_designator: Optional[FareTicketDesignator] = field(
        default=None,
        metadata=dict(
            name="FareTicketDesignator",
            type="Element"
        )
    )
    override_currency: Optional["RepricingModifiers.OverrideCurrency"] = field(
        default=None,
        metadata=dict(
            name="OverrideCurrency",
            type="Element"
        )
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentPricingModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    withhold_tax_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="WithholdTaxCode",
            type="Element",
            min_occurs=0,
            max_occurs=4,
            length=2
        )
    )
    price_class_of_service: Optional[TypePriceClassOfService] = field(
        default=None,
        metadata=dict(
            name="PriceClassOfService",
            type="Attribute"
        )
    )
    create_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CreateDate",
            type="Attribute"
        )
    )
    reissue_loc_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ReissueLocCityCode",
            type="Attribute",
            length=3
        )
    )
    reissue_loc_country_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ReissueLocCountryCode",
            type="Attribute",
            length=2
        )
    )
    bulk_ticket: bool = field(
        default=False,
        metadata=dict(
            name="BulkTicket",
            type="Attribute"
        )
    )
    account_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute"
        )
    )
    penalty_as_tax_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PenaltyAsTaxCode",
            type="Attribute",
            length=2
        )
    )
    air_pricing_solution_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirPricingSolutionRef",
            type="Attribute"
        )
    )
    penalty_to_fare: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="PenaltyToFare",
            type="Attribute"
        )
    )
    price_ptconly: bool = field(
        default=False,
        metadata=dict(
            name="PricePTCOnly",
            type="Attribute"
        )
    )
    brand_details: bool = field(
        default=False,
        metadata=dict(
            name="BrandDetails",
            type="Attribute"
        )
    )
    brand_modifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandModifier",
            type="Attribute"
        )
    )
    jet_service_only: bool = field(
        default=False,
        metadata=dict(
            name="JetServiceOnly",
            type="Attribute"
        )
    )
    time_window: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TimeWindow",
            type="Attribute",
            min_inclusive=1,
            max_inclusive=12
        )
    )
    flight_type: RepricingModifiersFlightType = field(
        default=RepricingModifiersFlightType.DIRECT,
        metadata=dict(
            name="FlightType",
            type="Attribute"
        )
    )
    multi_airport_search: bool = field(
        default=True,
        metadata=dict(
            name="MultiAirportSearch",
            type="Attribute"
        )
    )
    connection_point: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ConnectionPoint",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )

    @dataclass
    class OverrideCurrency:
        """
        :ivar currency_code:
        :ivar country_code:
        """
        currency_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="CurrencyCode",
                type="Attribute",
                length=3
            )
        )
        country_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="CountryCode",
                type="Attribute",
                length=2
            )
        )


@dataclass
class Route:
    """Information about this Route component.

    :ivar leg:
    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    leg: List[Leg] = field(
        default_factory=list,
        metadata=dict(
            name="Leg",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RuleLengthOfStay:
    """Container for rules providing minimum and maximum stay requirements.

    :ivar minimum_stay:
    :ivar maximum_stay:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    minimum_stay: Optional[TypeRestrictionLengthOfStay] = field(
        default=None,
        metadata=dict(
            name="MinimumStay",
            type="Element"
        )
    )
    maximum_stay: Optional[TypeRestrictionLengthOfStay] = field(
        default=None,
        metadata=dict(
            name="MaximumStay",
            type="Element"
        )
    )


@dataclass
class TcrexchangeBundle:
    """Bundle exchange, pricing, and penalty information for one ticketless carrier
    reservation Used in AirExchangeReq request and AirExchangeQuoteRsp response.

    :ivar air_exchange_info:
    :ivar air_pricing_info_ref:
    :ivar fee_info:
    :ivar tax_info: Itinerary level taxes
    :ivar penalty: Only used within an AirExchangeQuoteRsp
    :ivar tcrnumber: The identifying number for a Ticketless Air
                            Reservation.
    """
    class Meta:
        name = "TCRExchangeBundle"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_exchange_info: Optional[AirExchangeInfo] = field(
        default=None,
        metadata=dict(
            name="AirExchangeInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    penalty: List[CommonPenalty] = field(
        default_factory=list,
        metadata=dict(
            name="Penalty",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Ticket:
    """The ticket that resulted from an air booking.

    :ivar coupon:
    :ivar ticket_endorsement:
    :ivar tour_code:
    :ivar exchanged_ticket_info:
    :ivar key:
    :ivar ticket_number:
    :ivar ticket_status:
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    coupon: List[Coupon] = field(
        default_factory=list,
        metadata=dict(
            name="Coupon",
            type="Element",
            min_occurs=1,
            max_occurs=4
        )
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata=dict(
            name="TicketEndorsement",
            type="Element",
            min_occurs=0,
            max_occurs=6
        )
    )
    tour_code: List[TourCode] = field(
        default_factory=list,
        metadata=dict(
            name="TourCode",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    exchanged_ticket_info: List[ExchangedTicketInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangedTicketInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            required=True,
            length=13
        )
    )
    ticket_status: Optional[TypeTicketStatus] = field(
        default=None,
        metadata=dict(
            name="TicketStatus",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class TicketInfo:
    """
    :ivar name:
    :ivar conjuncted_ticket_info:
    :ivar exchanged_ticket_info:
    :ivar number:
    :ivar iatanumber:
    :ivar ticket_issue_date:
    :ivar ticketing_agent_sign_on:
    :ivar country_code: Contains Ticketed PCC’s Country code.
    :ivar status:
    :ivar bulk_ticket: Whether the ticket was issued as bulk.
    :ivar booking_traveler_ref: A reference to a passenger.
    :ivar air_pricing_info_ref: A reference to a AirPricing.Applicable Providers 1G and 1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    conjuncted_ticket_info: List[ConjunctedTicketInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ConjunctedTicketInfo",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    exchanged_ticket_info: List[ExchangedTicketInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangedTicketInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True
        )
    )
    iatanumber: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IATANumber",
            type="Attribute",
            max_length=8
        )
    )
    ticket_issue_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketIssueDate",
            type="Attribute"
        )
    )
    ticketing_agent_sign_on: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketingAgentSignOn",
            type="Attribute",
            max_length=8
        )
    )
    country_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Attribute",
            length=2
        )
    )
    status: Optional[TypeTicketStatus] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            required=True
        )
    )
    bulk_ticket: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="BulkTicket",
            type="Attribute"
        )
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            required=True
        )
    )
    air_pricing_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Attribute"
        )
    )


@dataclass
class TypeDefaultBrandDetail:
    """
    :ivar text: Text associated to the brand
    :ivar image_location: Images associated to the brand
    :ivar applicable_segment: Defines for which air segment the brand is applicable.
    :ivar brand_id: The unique identifier of the brand
    """
    class Meta:
        name = "typeDefaultBrandDetail"

    text: List[Text] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=4
        )
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata=dict(
            name="ImageLocation",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=3
        )
    )
    applicable_segment: List[ApplicableSegment] = field(
        default_factory=list,
        metadata=dict(
            name="ApplicableSegment",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandID",
            type="Attribute",
            min_length=1,
            max_length=19
        )
    )


@dataclass
class AccountRelatedRules:
    """
    :ivar booking_rules:
    :ivar routing_rules:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_rules: List[BookingRules] = field(
        default_factory=list,
        metadata=dict(
            name="BookingRules",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    routing_rules: Optional[RoutingRules] = field(
        default=None,
        metadata=dict(
            name="RoutingRules",
            type="Element"
        )
    )


@dataclass
class AirExchangeBundleList:
    """The shared object list of AirsegmentData.

    :ivar air_exchange_bundle:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundle",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeEligibilityRsp(BaseRsp):
    """
    :ivar exchange_eligibility_info:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    exchange_eligibility_info: Optional[ExchangeEligibilityInfo] = field(
        default=None,
        metadata=dict(
            name="ExchangeEligibilityInfo",
            type="Element",
            required=True
        )
    )


@dataclass
class AirExchangeTicketingReq(BaseReq):
    """Request to ticket an exchanged itinerary. Providers 1G, 1V, 1P.

    :ivar air_reservation_locator_code: Identifies the PNR to ticket. Providers 1G, 1V, 1P.
    :ivar ticket_number: Ticket number to reissue. Providers 1G, 1V, 1P.
    :ivar ticketing_modifiers_ref: Provider: 1P-Reference to a shared list of Ticketing Modifiers. This is supported for Worldspan provider only. When AirPricingInfoRef is used along with TicketingModifiersRef means that particular TicketingModifiers will to be applied while ticketing the Stored fare corresponding to the AirPricingInfo. Absence of AirPricingInfoRef means that particular TicketingModifiers will be applied to all Stored fares which are requested to be ticketed.
    :ivar waiver_code:
    :ivar detailed_billing_information: Providers 1G, 1V, 1P.
    :ivar air_ticketing_modifiers: Provider: 1G,1V,1P.
    :ivar bulk_ticket: Providers 1G, 1V, 1P.
    :ivar change_fee_on_ticket: Applies the change fee/penalty to the original form of payment. Providers: 1V
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[AirReservationLocatorCode] = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            required=True
        )
    )
    ticket_number: Optional[TicketNumber] = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    ticketing_modifiers_ref: List[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata=dict(
            name="TicketingModifiersRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element"
        )
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_ticketing_modifiers: List[AirTicketingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirTicketingModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    bulk_ticket: bool = field(
        default=False,
        metadata=dict(
            name="BulkTicket",
            type="Attribute"
        )
    )
    change_fee_on_ticket: bool = field(
        default=True,
        metadata=dict(
            name="ChangeFeeOnTicket",
            type="Attribute"
        )
    )


@dataclass
class AirFareDisplayReq(BaseReq):
    """Request to display a tariff for based on origin, destination, and other
    options.

    :ivar fare_type: Provider: 1G,1V,1P,1J.
    :ivar passenger_type: Provider: 1G,1V,1P,1J.
    :ivar booking_code: Provider: 1G,1V,1P,1J.
    :ivar include_addl_booking_code_info: Provider: 1G,1V,1P,1J.
    :ivar fare_basis: Provider: 1G,1V,1P,1J.
    :ivar carrier: Provider: 1G,1V,1P,1J.
    :ivar account_code: Provider: 1G,1V,1P,1J.
    :ivar contract_code: Provider: 1G,1V.
    :ivar air_fare_display_modifiers: Provider: 1G,1V,1P,1J.
    :ivar point_of_sale: Provider: 1G,1V.
    :ivar air_fare_display_rule_key: Provider: 1G,1V,1P,1J.
    :ivar origin: Provider: 1G,1V,1P,1J.
    :ivar destination: Provider: 1G,1V,1P,1J.
    :ivar provider_code: Provider: 1G,1V,1P,1J.
    :ivar include_mile_route_information: Provider: 1G,1V,1P,1J-Used to request Mile/Route Information in follow on (Mile, Route, Both)
    :ivar un_saleable_fares_only: Provider: 1G,1V,1P,1J-Used to request unsaleable fares only also known as place of sale fares.
    :ivar channel_id: A Channel ID is 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.
    :ivar nscc: 1 to 3 numeric that define a Search Control Console filter.This attribute is used to override that filter.
    :ivar return_mm: If this attribute is set to true, Fare Control Manager processing will be invoked.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_type: List[FareType] = field(
        default_factory=list,
        metadata=dict(
            name="FareType",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    passenger_type: List[TypePassengerType] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerType",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata=dict(
            name="BookingCode",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    include_addl_booking_code_info: Optional[IncludeAddlBookingCodeInfo] = field(
        default=None,
        metadata=dict(
            name="IncludeAddlBookingCodeInfo",
            type="Element"
        )
    )
    fare_basis: Optional[FareBasis] = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Element"
        )
    )
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=10
        )
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=5
        )
    )
    contract_code: Optional[ContractCode] = field(
        default=None,
        metadata=dict(
            name="ContractCode",
            type="Element"
        )
    )
    air_fare_display_modifiers: Optional[AirFareDisplayModifiers] = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayModifiers",
            type="Element"
        )
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=5
        )
    )
    air_fare_display_rule_key: Optional[AirFareDisplayRuleKey] = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayRuleKey",
            type="Element"
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2,
            max_length=5
        )
    )
    include_mile_route_information: Optional[TypeMileOrRouteBasedFare] = field(
        default=None,
        metadata=dict(
            name="IncludeMileRouteInformation",
            type="Attribute"
        )
    )
    un_saleable_fares_only: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="UnSaleableFaresOnly",
            type="Attribute"
        )
    )
    channel_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ChannelId",
            type="Attribute",
            min_length=2,
            max_length=4
        )
    )
    nscc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            min_length=1,
            max_length=3
        )
    )
    return_mm: bool = field(
        default=False,
        metadata=dict(
            name="ReturnMM",
            type="Attribute"
        )
    )


@dataclass
class AirFareRulesReq(BaseReq):
    """Request to display the full text fare rules.

    :ivar air_reservation_selector: Provider: 1G,1V,1P,1J,ACH-Parameters to use for a fare rule lookup associated with an Air Reservation Locator Code
    :ivar fare_rule_lookup: Used to look up fare rules based on the origin, destination, and carrier of the air segment, the fare basis code and the provider code.  Providers: 1P, 1J.
    :ivar fare_rule_key: Used to look up fare rules based on a fare rule key. Providers: 1G, 1V, 1P, 1J, ACH.
    :ivar air_fare_display_rule_key: Provider: 1G,1V,1P,1J.
    :ivar air_fare_rules_modifier: Provider: 1G,1V.
    :ivar fare_rules_filter_category: Structured Fare Rules Filter if requested will return rules for requested categories in the response. Applicable for providers 1G, 1V.
    :ivar fare_rule_type: Provider: 1G,1V,1P,1J,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_selector: Optional["AirFareRulesReq.AirReservationSelector"] = field(
        default=None,
        metadata=dict(
            name="AirReservationSelector",
            type="Element"
        )
    )
    fare_rule_lookup: Optional[FareRuleLookup] = field(
        default=None,
        metadata=dict(
            name="FareRuleLookup",
            type="Element"
        )
    )
    fare_rule_key: List[FareRuleKey] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleKey",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_fare_display_rule_key: Optional[AirFareDisplayRuleKey] = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayRuleKey",
            type="Element"
        )
    )
    air_fare_rules_modifier: Optional[AirFareRulesModifier] = field(
        default=None,
        metadata=dict(
            name="AirFareRulesModifier",
            type="Element"
        )
    )
    fare_rules_filter_category: List["AirFareRulesReq.FareRulesFilterCategory"] = field(
        default_factory=list,
        metadata=dict(
            name="FareRulesFilterCategory",
            type="Element",
            min_occurs=0,
            max_occurs=16
        )
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.LONG,
        metadata=dict(
            name="FareRuleType",
            type="Attribute"
        )
    )

    @dataclass
    class FareRulesFilterCategory:
        """
        :ivar category_code: Structured Fare Rules can be requested for "ADV", "MIN", "MAX",  "STP", and "CHG".
        :ivar fare_info_ref: Key reference for multiple fare rule
        """
        category_code: List[object] = field(
            default_factory=list,
            metadata=dict(
                name="CategoryCode",
                type="Element",
                min_occurs=1,
                max_occurs=35
            )
        )
        fare_info_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="FareInfoRef",
                type="Attribute"
            )
        )

    @dataclass
    class AirReservationSelector:
        """
        :ivar fare_info_ref:
        :ivar air_reservation_locator_code: The Air Reservation locator code which is an unique identifier for the reservation
        """
        fare_info_ref: List[FareInfoRef] = field(
            default_factory=list,
            metadata=dict(
                name="FareInfoRef",
                type="Element",
                min_occurs=0,
                max_occurs=999
            )
        )
        air_reservation_locator_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="AirReservationLocatorCode",
                type="Attribute",
                required=True,
                min_length=5,
                max_length=8
            )
        )


@dataclass
class AirItinerarySolution:
    """The pricing container for an air travel itinerary.

    :ivar air_segment_ref:
    :ivar connection:
    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata=dict(
            name="Connection",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AirPricingCommand:
    """A containter to identify individual pricing events. A pricing result will be
    returned for each pricing command according to its parameters.

    :ivar air_pricing_modifiers:
    :ivar air_segment_pricing_modifiers:
    :ivar command_key: An identifier to link the pricing responses to
                            the pricing commands. The value passed here will be returned in
                            the resulting AirPricingInfo(s) from this command.
    :ivar cabin_class: Specify the cabin type to price the entire
                            itinerary in. If segment level cabin selection is required, this
                            attribute should not be used.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element"
        )
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentPricingModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    command_key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CommandKey",
            type="Attribute",
            max_length=10
        )
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute"
        )
    )


@dataclass
class AlternateRouteList:
    """Identifies the alternate routes for the request.

    :ivar alternate_route:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    alternate_route: List[AlternateRoute] = field(
        default_factory=list,
        metadata=dict(
            name="AlternateRoute",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AutoPricingInfo:
    """Auto Pricing based on Segment and Traveler Association.

    :ivar air_segment_ref:
    :ivar booking_traveler_ref:
    :ivar air_pricing_modifiers:
    :ivar air_segment_pricing_modifiers:
    :ivar key:
    :ivar pricing_type: Indicates the Pricing Type used.
                            The possible values are TicketRecord, StoredFare, PricingInstruction.
    :ivar plating_carrier: The Plating Carrier for this journey
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=100
        )
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=100
        )
    )
    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element"
        )
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentPricingModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=100
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    pricing_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PricingType",
            type="Attribute",
            max_length=25
        )
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            length=2
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class BagDetails:
    """Information related to Bag details .

    :ivar baggage_restriction:
    :ivar available_discount:
    :ivar applicable_bags: Applicable baggage like Carry-On,1st Check-in,2nd Check -in etc.
    :ivar base_price:
    :ivar approximate_base_price:
    :ivar taxes:
    :ivar total_price:
    :ivar approximate_total_price:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    baggage_restriction: List[BaggageRestriction] = field(
        default_factory=list,
        metadata=dict(
            name="BaggageRestriction",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    available_discount: List[AvailableDiscount] = field(
        default_factory=list,
        metadata=dict(
            name="AvailableDiscount",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    applicable_bags: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApplicableBags",
            type="Attribute",
            required=True
        )
    )
    base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute"
        )
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateBasePrice",
            type="Attribute"
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute"
        )
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute"
        )
    )


@dataclass
class CarryOnAllowanceInfo(BaseBaggageAllowanceInfo):
    """Information related to Carry-On allowance like URL, pricing etc.

    :ivar carry_on_details: Information related to Carry-On Bag details .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    carry_on_details: List["CarryOnAllowanceInfo.CarryOnDetails"] = field(
        default_factory=list,
        metadata=dict(
            name="CarryOnDetails",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class CarryOnDetails:
        """
        :ivar baggage_restriction:
        :ivar applicable_carry_on_bags: Applicable Carry-On baggage "First", "Second", "Third" etc
        :ivar base_price:
        :ivar approximate_base_price:
        :ivar taxes:
        :ivar total_price:
        :ivar approximate_total_price:
        """
        baggage_restriction: List[BaggageRestriction] = field(
            default_factory=list,
            metadata=dict(
                name="BaggageRestriction",
                type="Element",
                min_occurs=0,
                max_occurs=99
            )
        )
        applicable_carry_on_bags: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ApplicableCarryOnBags",
                type="Attribute"
            )
        )
        base_price: Optional[str] = field(
            default=None,
            metadata=dict(
                name="BasePrice",
                type="Attribute"
            )
        )
        approximate_base_price: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ApproximateBasePrice",
                type="Attribute"
            )
        )
        taxes: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Taxes",
                type="Attribute"
            )
        )
        total_price: Optional[str] = field(
            default=None,
            metadata=dict(
                name="TotalPrice",
                type="Attribute"
            )
        )
        approximate_total_price: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ApproximateTotalPrice",
                type="Attribute"
            )
        )


@dataclass
class DefaultBrandDetail(TypeDefaultBrandDetail):
    """Applicable air segment."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class DocumentInfo:
    """Container for the document information summary line.

    :ivar ticket_info:
    :ivar mcoinfo:
    :ivar tcrinfo:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_info: List[TicketInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TicketInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    mcoinfo: List[Mcoinformation] = field(
        default_factory=list,
        metadata=dict(
            name="MCOInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrinfo: List[Tcrinfo] = field(
        default_factory=list,
        metadata=dict(
            name="TCRInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class Emdinfo:
    """This is the parent container to display EMD information. Occurrence of
    multiple unique EMDs inside this container indicate that those EMDs are
    conjunctive to each other. Supported providers are 1G/1V/1P/1J.

    :ivar emdtraveler_info: Basic information of the traveler associated with this EMDInfo.
    :ivar supplier_locator: List of Supplier Locator information that is associated with this document
    :ivar electronic_misc_document: Electronic miscellaneous documents.As an EMDInfo container displays all the EMDs which are in conjunction, there can be maximum 4 ElectronicMiscDocuments present in an EMDInfo
    :ivar payment: Payment charged for EMD isuance
    :ivar form_of_payment: FormOfPayment used for issuing these electronic miscellaneous documents
    :ivar emdpricing_info: Fare related information for these electronic miscellaneous documents
    :ivar emdendorsement:
    :ivar fare_calc: Infomration about the fare calculation
    :ivar emdcommission: Commission information applied during EMD issuance
    :ivar provider_code:
    :ivar provider_locator_code:
    :ivar key: System generated Key
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        name = "EMDInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdtraveler_info: Optional[EmdtravelerInfo] = field(
        default=None,
        metadata=dict(
            name="EMDTravelerInfo",
            type="Element",
            required=True
        )
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    electronic_misc_document: List[ElectronicMiscDocument] = field(
        default_factory=list,
        metadata=dict(
            name="ElectronicMiscDocument",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    payment: Optional[Payment] = field(
        default=None,
        metadata=dict(
            name="Payment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    emdpricing_info: Optional[EmdpricingInfo] = field(
        default=None,
        metadata=dict(
            name="EMDPricingInfo",
            type="Element"
        )
    )
    emdendorsement: List[Emdendorsement] = field(
        default_factory=list,
        metadata=dict(
            name="EMDEndorsement",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_calc: Optional[FareCalc] = field(
        default=None,
        metadata=dict(
            name="FareCalc",
            type="Element"
        )
    )
    emdcommission: Optional[Emdcommission] = field(
        default=None,
        metadata=dict(
            name="EMDCommission",
            type="Element"
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2,
            max_length=5
        )
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            required=True,
            max_length=15
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class EmdissuanceReq(BaseReq):
    """Electronic Miscellaneous Document issuance request.Supported providers are
    1V/1G/1P/1J.

    :ivar provider_reservation_detail: PNR information for which EMD is going to be issued.
    :ivar ticket_number: Ticket number for which EMD is going to be issued.Required for EMD-A issuance.
    :ivar issuance_modifiers: General modifiers related to EMD issuance.
    :ivar selection_modifiers: Modifiers related to selection of services during EMD issuance.
    :ivar universal_record_locator_code: Represents a valid Universal Record locator code.
    :ivar show_details: This attribute gives the control to request for complete information on Issued EMDs or minimal information.Requesting complete information leads to possible multiple supplier calls for fetching all the details.
    :ivar issue_all_open_svc: Issues EMDS to all SVC segments. If it is true, TicketNumber and SVC segment reference need not be provided. Supported provider 1P.
    """
    class Meta:
        name = "EMDIssuanceReq"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    provider_reservation_detail: Optional[ProviderReservationDetail] = field(
        default=None,
        metadata=dict(
            name="ProviderReservationDetail",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    ticket_number: Optional[TicketNumber] = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    issuance_modifiers: Optional[IssuanceModifiers] = field(
        default=None,
        metadata=dict(
            name="IssuanceModifiers",
            type="Element"
        )
    )
    selection_modifiers: Optional[SelectionModifiers] = field(
        default=None,
        metadata=dict(
            name="SelectionModifiers",
            type="Element"
        )
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            required=True,
            min_length=5,
            max_length=8
        )
    )
    show_details: bool = field(
        default=False,
        metadata=dict(
            name="ShowDetails",
            type="Attribute"
        )
    )
    issue_all_open_svc: bool = field(
        default=False,
        metadata=dict(
            name="IssueAllOpenSVC",
            type="Attribute"
        )
    )


@dataclass
class EmdsummaryInfo:
    """Container for EMD summary information. Supported providers are 1G/1V/1P/1J.

    :ivar emdsummary: Summary information for EMDs conjuncted to each other.
    :ivar emdtraveler_info: EMD traveler information.
    :ivar payment: Payment charged to issue EMD.
    :ivar provider_reservation_info_ref: A reference to the provider reservation with which the document is associated.Displayed when shown as part of UR.Not displayed in EMDRetrieveRsp
    :ivar key: System generated Key
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        name = "EMDSummaryInfo"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdsummary: List[Emdsummary] = field(
        default_factory=list,
        metadata=dict(
            name="EMDSummary",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    emdtraveler_info: Optional[EmdtravelerInfo] = field(
        default=None,
        metadata=dict(
            name="EMDTravelerInfo",
            type="Element",
            required=True
        )
    )
    payment: Optional[Payment] = field(
        default=None,
        metadata=dict(
            name="Payment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class ExpertSolutionList:
    """Identifies the Expert Solutions retrieved from the Knowledge Base.

    :ivar expert_solution:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    expert_solution: List[ExpertSolution] = field(
        default_factory=list,
        metadata=dict(
            name="ExpertSolution",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FareDisplayRule:
    """Fare Display Rule Container.

    :ivar rule_advanced_purchase:
    :ivar rule_length_of_stay:
    :ivar rule_charges:
    :ivar rule_number:
    :ivar source:
    :ivar tariff_number:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    rule_advanced_purchase: Optional[RuleAdvancedPurchase] = field(
        default=None,
        metadata=dict(
            name="RuleAdvancedPurchase",
            type="Element"
        )
    )
    rule_length_of_stay: Optional[RuleLengthOfStay] = field(
        default=None,
        metadata=dict(
            name="RuleLengthOfStay",
            type="Element"
        )
    )
    rule_charges: Optional[RuleCharges] = field(
        default=None,
        metadata=dict(
            name="RuleCharges",
            type="Element"
        )
    )
    rule_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RuleNumber",
            type="Attribute"
        )
    )
    source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute"
        )
    )
    tariff_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TariffNumber",
            type="Attribute"
        )
    )


@dataclass
class FaxDetailsInformation:
    """Container to send Fax details Information for ticketing.

    :ivar air_pricing_info_ref: Returns related air pricing infos.
    :ivar fax_details:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    fax_details: Optional[FaxDetails] = field(
        default=None,
        metadata=dict(
            name="FaxDetails",
            type="Element",
            required=True
        )
    )


@dataclass
class FlightDetails:
    """Specific details within a flight segment.

    :ivar connection:
    :ivar meals:
    :ivar in_flight_services:
    :ivar key:
    :ivar origin: The IATA location code for this origination of this entity.
    :ivar destination: The IATA location code for this destination of this entity.
    :ivar departure_time: The date and time at which this entity departs. Date and time are represented as Airport Local Time at the place of departure. The correct time zone offset is also included.
    :ivar arrival_time: The date and time at which this entity arrives at the destination. Date and time are represented as Airport Local Time at the place of arrival. The correct time zone offset is also included.
    :ivar flight_time: Time spent (minutes) traveling in flight, including airport taxi time.
    :ivar travel_time: Total time spent (minutes) traveling including flight time and ground time.
    :ivar distance: The distance traveled. Units are specified in the parent response element.
    :ivar equipment:
    :ivar on_time_performance: Represents flight on time performance
                            as a percentage from 0 to 100
    :ivar origin_terminal:
    :ivar destination_terminal:
    :ivar ground_time:
    :ivar automated_checkin: “True” indicates that the flight allows automated check-in. The default is “False”.
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    connection: Optional[Connection] = field(
        default=None,
        metadata=dict(
            name="Connection",
            type="Element"
        )
    )
    meals: List[Meals] = field(
        default_factory=list,
        metadata=dict(
            name="Meals",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    in_flight_services: List[InFlightServices] = field(
        default_factory=list,
        metadata=dict(
            name="InFlightServices",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute"
        )
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute"
        )
    )
    flight_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FlightTime",
            type="Attribute"
        )
    )
    travel_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute"
        )
    )
    distance: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Distance",
            type="Attribute"
        )
    )
    equipment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Equipment",
            type="Attribute",
            length=3
        )
    )
    on_time_performance: Optional[int] = field(
        default=None,
        metadata=dict(
            name="OnTimePerformance",
            type="Attribute"
        )
    )
    origin_terminal: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OriginTerminal",
            type="Attribute"
        )
    )
    destination_terminal: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DestinationTerminal",
            type="Attribute"
        )
    )
    ground_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="GroundTime",
            type="Attribute"
        )
    )
    automated_checkin: bool = field(
        default=False,
        metadata=dict(
            name="AutomatedCheckin",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class FlightInfo:
    """
    :ivar flight_info_detail:
    :ivar flight_info_error_message: Errors, Warnings and informational
                                messages for the Flight referenced above.
    :ivar criteria_key: An identifier to link the flightinfo responses
                            to the criteria in request. The value populated here is passed in
                            request.
    :ivar carrier: The carrier that is marketing this segment
    :ivar flight_number: The flight number under which the marketing
                            carrier is marketing this flight
    :ivar origin: The IATA location code for this origination of
                            this entity.
    :ivar destination: The IATA location code for this destination of
                            this entity.
    :ivar departure_date: The date at which this entity departs. This
                            does not include time zone information since it can be derived
                            from the origin location.
    :ivar class_of_service:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_info_detail: List[FlightInfoDetail] = field(
        default_factory=list,
        metadata=dict(
            name="FlightInfoDetail",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    flight_info_error_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata=dict(
            name="FlightInfoErrorMessage",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    criteria_key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CriteriaKey",
            type="Attribute",
            required=True
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            length=2
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            required=True,
            max_length=5
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    departure_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute",
            required=True
        )
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            min_length=1,
            max_length=2
        )
    )


@dataclass
class FlightTimeDetail:
    """Flight Time Table Response Details.

    :ivar days_of_operation:
    :ivar connection:
    :ivar key:
    :ivar vendor_code:
    :ivar flight_number:
    :ivar origin:
    :ivar destination:
    :ivar departure_time: Flight departure time
    :ivar arrival_time: Flight arrival time
    :ivar stop_count:
    :ivar equipment:
    :ivar schedule_start_date: Flight time table search start date
    :ivar schedule_end_date: Flight time table search end date
    :ivar display_option: Indicates if carrier has link (carrier specific) display option.
    :ivar on_time_performance: On time performance indicator in percentage.
    :ivar day_change: Indicates if flight arrives on same day as departure, previous day, or next day. Like values  00 means Same day ,  01 means next day, -1 mean Previous day etc.
    :ivar journey_time: Indicates total journey time in minutes.
    :ivar flight_time: Indicates total flight time in minutes.
    :ivar start_terminal: Flight start terminal code.
    :ivar end_terminal: Flight end terminal code.
    :ivar first_intermediate_stop: First intermediate stop after board point.
    :ivar last_intermediate_stop: Last intermediate stop before off point.
    :ivar inside_availability:
    :ivar secure_sell:
    :ivar availability_source:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    days_of_operation: Optional[TypeDaysOfOperation] = field(
        default=None,
        metadata=dict(
            name="DaysOfOperation",
            type="Element"
        )
    )
    connection: Optional[Connection] = field(
        default=None,
        metadata=dict(
            name="Connection",
            type="Element"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    vendor_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="VendorCode",
            type="Attribute"
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            max_length=5
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3
        )
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute"
        )
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute"
        )
    )
    stop_count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="StopCount",
            type="Attribute"
        )
    )
    equipment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Equipment",
            type="Attribute",
            length=3
        )
    )
    schedule_start_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ScheduleStartDate",
            type="Attribute"
        )
    )
    schedule_end_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ScheduleEndDate",
            type="Attribute"
        )
    )
    display_option: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="DisplayOption",
            type="Attribute"
        )
    )
    on_time_performance: Optional[int] = field(
        default=None,
        metadata=dict(
            name="OnTimePerformance",
            type="Attribute"
        )
    )
    day_change: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DayChange",
            type="Attribute"
        )
    )
    journey_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="JourneyTime",
            type="Attribute"
        )
    )
    flight_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FlightTime",
            type="Attribute"
        )
    )
    start_terminal: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StartTerminal",
            type="Attribute"
        )
    )
    end_terminal: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EndTerminal",
            type="Attribute"
        )
    )
    first_intermediate_stop: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FirstIntermediateStop",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    last_intermediate_stop: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LastIntermediateStop",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    inside_availability: Optional[str] = field(
        default=None,
        metadata=dict(
            name="InsideAvailability",
            type="Attribute",
            min_length=1,
            max_length=1
        )
    )
    secure_sell: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SecureSell",
            type="Attribute",
            min_length=0,
            max_length=2
        )
    )
    availability_source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AvailabilitySource",
            type="Attribute",
            max_length=1
        )
    )


@dataclass
class FlightTimeTableCriteria:
    """Flight Time Table Search Criteria.

    :ivar general_time_table:
    :ivar specific_time_table:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    general_time_table: Optional[GeneralTimeTable] = field(
        default=None,
        metadata=dict(
            name="GeneralTimeTable",
            type="Element"
        )
    )
    specific_time_table: Optional[SpecificTimeTable] = field(
        default=None,
        metadata=dict(
            name="SpecificTimeTable",
            type="Element"
        )
    )


@dataclass
class MerchandisingAvailabilityDetails:
    """Rich Content and Branding for an air segment.

    :ivar air_itinerary_details:
    :ivar account_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_itinerary_details: Optional[AirItineraryDetails] = field(
        default=None,
        metadata=dict(
            name="AirItineraryDetails",
            type="Element",
            required=True
        )
    )
    account_code: Optional[AccountCode] = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )


@dataclass
class MerchandisingDetails:
    """Rich Content and Branding for a fare brand.

    :ivar air_itinerary_details:
    :ivar account_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_itinerary_details: List[AirItineraryDetails] = field(
        default_factory=list,
        metadata=dict(
            name="AirItineraryDetails",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class Option:
    """List of segment and fare available for the search air leg.

    :ivar booking_info:
    :ivar connection:
    :ivar key:
    :ivar travel_time: Total traveling time that is difference between the departure time of the first segment and the arrival time of the last segments for that particular entire set of connection.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_info: List[BookingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="BookingInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata=dict(
            name="Connection",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    travel_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute"
        )
    )


@dataclass
class OptionalService:
    """
    :ivar service_data:
    :ivar service_info:
    :ivar remark: Information regarding any specific
                                for this service.
    :ivar tax_info:
    :ivar fee_info:
    :ivar emd:
    :ivar bundled_services:
    :ivar additional_info:
    :ivar fee_application: Specifies how the Optional Service fee is to be applied.  The choices are Per One Way, Per Round Trip, Per Item (Per Piece), Per Travel, Per Ticket, Per 1 Kilo, Per 5 Kilos.  Provider: 1G, 1V, 1P, 1J
    :ivar text:
    :ivar price_range:
    :ivar tour_code:
    :ivar branding_info:
    :ivar title:
    :ivar provider_code:
    :ivar supplier_code:
    :ivar optional_services_rule_ref: UniqueID to associate a rule to the
                            Optional Service
    :ivar type: Specify the type of service offered (e.g.
                            seats, baggage, etc.)
    :ivar confirmation: Confirmation number provided by the
                            supplier
    :ivar secondary_type: The secondary option code type required for
                            certain options
    :ivar purchase_window: Describes when the Service is available
                            for confirmation or purchase (e.g. Booking Only, Check-in Only,
                            Anytime, etc.)
    :ivar priority: Numeric value that represents the priority
                            order of the Service
    :ivar available: Boolean to describe whether the Service is
                            available for sale or not
    :ivar entitled: Boolean to describe whether the passenger
                            is entitled for the service without charge or not
    :ivar per_traveler: Boolean to describe whether the Amount on
                            the Service is charged per traveler.
    :ivar create_date: Timestamp when this service/offer got
                            created.
    :ivar payment_ref: Reference to a payment for merchandising
                            services.
    :ivar service_status: Specify the service status (e.g. active,
                            canceled, etc.)
    :ivar quantity: The number of units availed for each optional
                            service (e.g. 2 baggage availed will be specified as 2 in quantity
                            for optional service BAGGAGE)
    :ivar sequence_number: The sequence number associated with the
                            OptionalService
    :ivar service_sub_code: The service subcode associated with the
                            OptionalService
    :ivar ssrcode: The SSR Code associated with the
                            OptionalService
    :ivar issuance_reason: A one-letter code specifying the reason for
                            issuance of the OptionalService
    :ivar provider_defined_type: Original Type as sent by the provider
    :ivar total_price: The total price for this entity including base price and all taxes.
    :ivar base_price: Represents the base price for this entity. This does not include any taxes or surcharges.
    :ivar approximate_total_price: The Converted total price in Default Currency for this entity including base price and all taxes.
    :ivar approximate_base_price: The Converted base price in Default Currency for this entity. This does not include any taxes or surcharges.
    :ivar equivalent_base_price: Represents the base price in the related currency for this entity. This does not include any taxes or surcharges.
    :ivar taxes: The aggregated amount of all the taxes that are associated with this entity. See the associated TaxInfo array for a breakdown of the individual taxes.
    :ivar fees: The aggregated amount of all the fees that are associated with this entity. See the associated FeeInfo array for a breakdown of the individual fees.
    :ivar services: The total cost for all optional services.
    :ivar approximate_taxes: The Converted tax amount in Default Currency.
    :ivar approximate_fees: The Converted fee amount in Default Currency.
    :ivar key:
    :ivar assess_indicator: Indicates whether price is assessed by mileage or currency or both
    :ivar mileage: Indicates mileage fee/amount
    :ivar applicable_fflevel: Numerical value of the loyalty card level for which this service is available.
    :ivar private: Describes if service is private or not.
    :ivar ssrfree_text: Certain SSR types sent in OptionalService SSRCode require a free text message. For example, PETC Pet in Cabin.
    :ivar is_pricing_approximate: When set to True indicates that the pricing returned is approximate. Supported providers are MCH/ACH
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    :ivar chargeable: Indicates if the optional service is not offered, is available for a charge, or is included in the brand
    :ivar inclusive_of_tax: Identifies if the service was filed with a fee that is inclusive of tax.
    :ivar interline_settlement_allowed: Identifies if the interline settlement is allowed in service .
    :ivar geography_specification: Sector, Portion, Journey.
    :ivar excess_weight_rate: The cost of the bag per unit weight.
    :ivar source: The Source of the optional service. The source can be ACH, MCE, or MCH.
    :ivar viewable_only: Describes if the OptionalService is viewable only or not.
                               If viewable only then the service cannot be sold.
    :ivar display_text: Title of the Optional Service.  Provider: ACH
    :ivar weight_in_excess: The excess weight of a bag. Providers: 1G, 1V, 1P, 1J
    :ivar total_weight: The total weight of a bag. Providers: 1G, 1V, 1P, 1J
    :ivar baggage_unit_price: The per unit price of baggage. Providers: 1G, 1V, 1P, 1J
    :ivar first_piece: Indicates the minimum occurrence of excess baggage.Provider: 1G, 1V, 1P, 1J.
    :ivar last_piece: Indicates the maximum occurrence of excess baggage. Provider: 1G, 1V, 1P, 1J.
    :ivar restricted: When set to “true”, the Optional Service is restricted by an embargo. Provider: 1G, 1V, 1P, 1J
    :ivar is_reprice_required: When set to “true”, the Optional Service must be re-priced. Provider: 1G, 1V, 1P, 1J
    :ivar booked_quantity: Indicates the Optional Service quantity already booked. Provider: 1G, 1V, 1P, 1J
    :ivar group: Associates Optional Services with the same ServiceSub Code, Air Segment, Passenger, and EMD Associated Item. Provider:1G, 1V, 1P, 1J
    :ivar pseudo_city_code: The PCC or SID that booked the Optional Service.
    :ivar tag: Optional service group name.
    :ivar display_order: Optional service group display order.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    service_data: List[ServiceData] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceData",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    service_info: Optional[ServiceInfo] = field(
        default=None,
        metadata=dict(
            name="ServiceInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata=dict(
            name="Remark",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    emd: Optional[Emd] = field(
        default=None,
        metadata=dict(
            name="EMD",
            type="Element"
        )
    )
    bundled_services: Optional[BundledServices] = field(
        default=None,
        metadata=dict(
            name="BundledServices",
            type="Element"
        )
    )
    additional_info: List[AdditionalInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AdditionalInfo",
            type="Element",
            min_occurs=0,
            max_occurs=16
        )
    )
    fee_application: Optional[FeeApplication] = field(
        default=None,
        metadata=dict(
            name="FeeApplication",
            type="Element"
        )
    )
    text: List[Text] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=0,
            max_occurs=4
        )
    )
    price_range: List[PriceRange] = field(
        default_factory=list,
        metadata=dict(
            name="PriceRange",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    tour_code: Optional[TourCode] = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Element"
        )
    )
    branding_info: Optional[BrandingInfo] = field(
        default=None,
        metadata=dict(
            name="BrandingInfo",
            type="Element"
        )
    )
    title: List[Title] = field(
        default_factory=list,
        metadata=dict(
            name="Title",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            min_length=1,
            max_length=5
        )
    )
    optional_services_rule_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OptionalServicesRuleRef",
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True,
            min_length=1,
            max_length=128
        )
    )
    confirmation: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Confirmation",
            type="Attribute"
        )
    )
    secondary_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SecondaryType",
            type="Attribute"
        )
    )
    purchase_window: Optional[TypePurchaseWindow] = field(
        default=None,
        metadata=dict(
            name="PurchaseWindow",
            type="Attribute"
        )
    )
    priority: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Priority",
            type="Attribute"
        )
    )
    available: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Available",
            type="Attribute"
        )
    )
    entitled: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Entitled",
            type="Attribute"
        )
    )
    per_traveler: bool = field(
        default=True,
        metadata=dict(
            name="PerTraveler",
            type="Attribute"
        )
    )
    create_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CreateDate",
            type="Attribute"
        )
    )
    payment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PaymentRef",
            type="Attribute"
        )
    )
    service_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ServiceStatus",
            type="Attribute"
        )
    )
    quantity: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Quantity",
            type="Attribute"
        )
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SequenceNumber",
            type="Attribute"
        )
    )
    service_sub_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute",
            max_length=3
        )
    )
    ssrcode: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SSRCode",
            type="Attribute",
            min_length=4,
            max_length=4
        )
    )
    issuance_reason: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IssuanceReason",
            type="Attribute",
            min_length=1,
            max_length=1
        )
    )
    provider_defined_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderDefinedType",
            type="Attribute",
            min_length=1,
            max_length=16
        )
    )
    total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute"
        )
    )
    base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute"
        )
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute"
        )
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateBasePrice",
            type="Attribute"
        )
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EquivalentBasePrice",
            type="Attribute"
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Attribute"
        )
    )
    services: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Services",
            type="Attribute"
        )
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTaxes",
            type="Attribute"
        )
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateFees",
            type="Attribute"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    assess_indicator: Optional[TypeAssessIndicator] = field(
        default=None,
        metadata=dict(
            name="AssessIndicator",
            type="Attribute"
        )
    )
    mileage: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Mileage",
            type="Attribute"
        )
    )
    applicable_fflevel: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ApplicableFFLevel",
            type="Attribute",
            min_inclusive=0,
            max_inclusive=9
        )
    )
    private: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Private",
            type="Attribute"
        )
    )
    ssrfree_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SSRFreeText",
            type="Attribute"
        )
    )
    is_pricing_approximate: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IsPricingApproximate",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )
    chargeable: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Chargeable",
            type="Attribute"
        )
    )
    inclusive_of_tax: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="InclusiveOfTax",
            type="Attribute"
        )
    )
    interline_settlement_allowed: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="InterlineSettlementAllowed",
            type="Attribute"
        )
    )
    geography_specification: Optional[str] = field(
        default=None,
        metadata=dict(
            name="GeographySpecification",
            type="Attribute"
        )
    )
    excess_weight_rate: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ExcessWeightRate",
            type="Attribute"
        )
    )
    source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute"
        )
    )
    viewable_only: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ViewableOnly",
            type="Attribute"
        )
    )
    display_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DisplayText",
            type="Attribute"
        )
    )
    weight_in_excess: Optional[str] = field(
        default=None,
        metadata=dict(
            name="WeightInExcess",
            type="Attribute"
        )
    )
    total_weight: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalWeight",
            type="Attribute"
        )
    )
    baggage_unit_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BaggageUnitPrice",
            type="Attribute"
        )
    )
    first_piece: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FirstPiece",
            type="Attribute"
        )
    )
    last_piece: Optional[int] = field(
        default=None,
        metadata=dict(
            name="LastPiece",
            type="Attribute"
        )
    )
    restricted: bool = field(
        default=False,
        metadata=dict(
            name="Restricted",
            type="Attribute"
        )
    )
    is_reprice_required: bool = field(
        default=False,
        metadata=dict(
            name="IsRepriceRequired",
            type="Attribute"
        )
    )
    booked_quantity: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookedQuantity",
            type="Attribute"
        )
    )
    group: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Group",
            type="Attribute"
        )
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=2,
            max_length=10
        )
    )
    tag: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Tag",
            type="Attribute",
            min_length=1,
            max_length=256
        )
    )
    display_order: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DisplayOrder",
            type="Attribute",
            min_inclusive=0,
            max_inclusive=999
        )
    )


@dataclass
class PrePayAccount:
    """PrePay Account associated with the customer.

    :ivar credit_summary:
    :ivar pre_pay_price_info:
    :ivar program_title: Pre pay program title
    :ivar certificate_number:
    :ivar program_name: Pre pay program name
    :ivar effective_date: Effective date for the pre pay account
    :ivar expire_date: Expiry date for the pre pay account
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    credit_summary: Optional[CreditSummary] = field(
        default=None,
        metadata=dict(
            name="CreditSummary",
            type="Element"
        )
    )
    pre_pay_price_info: Optional[PrePayPriceInfo] = field(
        default=None,
        metadata=dict(
            name="PrePayPriceInfo",
            type="Element"
        )
    )
    program_title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProgramTitle",
            type="Attribute"
        )
    )
    certificate_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CertificateNumber",
            type="Attribute"
        )
    )
    program_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProgramName",
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


@dataclass
class RouteList:
    """Identifies the routes and sub-routes that were requested.

    :ivar route:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    route: List[Route] = field(
        default_factory=list,
        metadata=dict(
            name="Route",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class Row:
    """Identifies the row of in a seat map.

    :ivar facility:
    :ivar characteristic:
    :ivar number:
    :ivar search_traveler_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    facility: List[Facility] = field(
        default_factory=list,
        metadata=dict(
            name="Facility",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    characteristic: List[Characteristic] = field(
        default_factory=list,
        metadata=dict(
            name="Characteristic",
            type="Element",
            min_occurs=0,
            max_occurs=999
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
    search_traveler_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SearchTravelerRef",
            type="Attribute"
        )
    )


@dataclass
class SearchAirLeg:
    """Search version of AirLeg used to specify search criteria.

    :ivar search_origin:
    :ivar search_destination:
    :ivar search_dep_time:
    :ivar search_arv_time: Specifies the preferred time within the time range. For 1G, 1V, 1P, 1J, it is supported for AvailabilitySearchReq (TimeRange must also be specified) and not supported for LowFareSearchReq. ACH does not support search by arrival time.
    :ivar air_leg_modifiers:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    search_origin: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata=dict(
            name="SearchOrigin",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    search_destination: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata=dict(
            name="SearchDestination",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    search_dep_time: List[TypeFlexibleTimeSpec] = field(
        default_factory=list,
        metadata=dict(
            name="SearchDepTime",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    search_arv_time: List[TypeTimeSpec] = field(
        default_factory=list,
        metadata=dict(
            name="SearchArvTime",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_leg_modifiers: Optional[AirLegModifiers] = field(
        default=None,
        metadata=dict(
            name="AirLegModifiers",
            type="Element"
        )
    )


@dataclass
class SegmentModifiers:
    """To be used to modify the ticket modifiers for air segment.

    :ivar air_segment_ref:
    :ivar ticket_validity: To be used to pass the ticket validity dates
    :ivar baggage_allowance:
    :ivar ticket_designator:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: Optional[AirSegmentRef] = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            required=True
        )
    )
    ticket_validity: Optional[TicketValidity] = field(
        default=None,
        metadata=dict(
            name="TicketValidity",
            type="Element"
        )
    )
    baggage_allowance: Optional[BaggageAllowance] = field(
        default=None,
        metadata=dict(
            name="BaggageAllowance",
            type="Element"
        )
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketDesignator",
            type="Element",
            min_length=0,
            max_length=20
        )
    )


@dataclass
class StructuredFareRulesType:
    """
    :ivar fare_rule_category_type: For FareRulesType element
    """
    fare_rule_category_type: List[FareRuleCategoryTypes] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleCategoryType",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class AirMerchandisingDetailsReq(BaseReq):
    """Request to retrieve brand details and optional services included in the
    brand.

    :ivar merchandising_details:
    :ivar optional_service_modifiers:
    :ivar merchandising_availability_details:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    merchandising_details: Optional[MerchandisingDetails] = field(
        default=None,
        metadata=dict(
            name="MerchandisingDetails",
            type="Element"
        )
    )
    optional_service_modifiers: Optional[OptionalServiceModifiers] = field(
        default=None,
        metadata=dict(
            name="OptionalServiceModifiers",
            type="Element"
        )
    )
    merchandising_availability_details: Optional[MerchandisingAvailabilityDetails] = field(
        default=None,
        metadata=dict(
            name="MerchandisingAvailabilityDetails",
            type="Element"
        )
    )


@dataclass
class AirTicketingReq(AirBaseReq):
    """Request to ticket a previously stored reservation.

    :ivar air_reservation_locator_code: Provider: 1G,1V,1P,1J.
    :ivar air_pricing_info_ref: Provider: 1G,1V,1P,1J-Indicates air pricing infos to be ticketed.
    :ivar ticketing_modifiers_ref: Provider: 1P,1J-Reference to a shared list of Ticketing Modifiers. This is supported for Worldspan and JAL providers only. When AirPricingInfoRef is used along with TicketingModifiersRef means that particular TicketingModifiers will to be applied while ticketing the Stored fare corresponding to the AirPricingInfo. Absence of AirPricingInfoRef means that particular TicketingModifiers will be applied to all Stored fares which are requested to be ticketed.
    :ivar waiver_code:
    :ivar commission:
    :ivar detailed_billing_information: Provider: 1G,1V.
    :ivar fax_details_information: Provider: 1V.
    :ivar air_ticketing_modifiers: Provider: 1G,1V,1P,1J.
    :ivar air_segment_ticketing_modifiers: Provider: 1P,1J.
    :ivar return_info_on_fail:
    :ivar bulk_ticket: Provider: 1G,1V,1P,1J.
    :ivar validate_spanish_residency: Provider: 1G - If set as true, Spanish Residency will be validated for
                                                                            Provisioned Customers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[AirReservationLocatorCode] = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            required=True
        )
    )
    air_pricing_info_ref: List["AirTicketingReq.AirPricingInfoRef"] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticketing_modifiers_ref: List[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata=dict(
            name="TicketingModifiersRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element"
        )
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata=dict(
            name="Commission",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=18
        )
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fax_details_information: Optional[FaxDetailsInformation] = field(
        default=None,
        metadata=dict(
            name="FaxDetailsInformation",
            type="Element"
        )
    )
    air_ticketing_modifiers: List[AirTicketingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirTicketingModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_segment_ticketing_modifiers: List[AirSegmentTicketingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentTicketingModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    return_info_on_fail: bool = field(
        default=True,
        metadata=dict(
            name="ReturnInfoOnFail",
            type="Attribute"
        )
    )
    bulk_ticket: bool = field(
        default=False,
        metadata=dict(
            name="BulkTicket",
            type="Attribute"
        )
    )
    validate_spanish_residency: bool = field(
        default=False,
        metadata=dict(
            name="ValidateSpanishResidency",
            type="Attribute"
        )
    )

    @dataclass
    class AirPricingInfoRef:
        """
        :ivar booking_traveler_ref:
        :ivar key:
        """
        booking_traveler_ref: List[BookingTravelerRef] = field(
            default_factory=list,
            metadata=dict(
                name="BookingTravelerRef",
                type="Element",
                namespace="http://www.travelport.com/schema/common_v48_0",
                min_occurs=0,
                max_occurs=9
            )
        )
        key: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Key",
                type="Attribute",
                required=True
            )
        )


@dataclass
class BaggageAllowanceInfo(BaseBaggageAllowanceInfo):
    """Information related to Baggage allowance like URL,Height,Weight etc.

    :ivar bag_details:
    :ivar traveler_type:
    :ivar fare_info_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    bag_details: List[BagDetails] = field(
        default_factory=list,
        metadata=dict(
            name="BagDetails",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    traveler_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            min_length=3,
            max_length=5
        )
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute"
        )
    )


@dataclass
class EmdissuanceRsp(BaseRsp):
    """Electronic Miscellaneous Document issuance response.Supported providers are
    1V/1G/1P/1J.

    :ivar emdsummary_info: List of EMDSummaryInfo elements to show minimal information in issuance response. Appears for ShowDetails=false in the request.This is the default behaviour.
    :ivar emdinfo: List of EMDInfo elements to show detailoed information in issuance response. Appears for ShowDetails=true in the request.
    """
    class Meta:
        name = "EMDIssuanceRsp"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata=dict(
            name="EMDSummaryInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    emdinfo: List[Emdinfo] = field(
        default_factory=list,
        metadata=dict(
            name="EMDInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class EmdretrieveRsp(BaseRsp):
    """Electronic Miscellaneous Document list and detail retrieve
    response.Supported providers are 1G/1V/1P/1J.

    :ivar emdinfo: Provider: 1G/1V/1P/1J.
    :ivar emdsummary_info: Provider: 1G/1V/1P/1J.
    """
    class Meta:
        name = "EMDRetrieveRsp"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    emdinfo: Optional[Emdinfo] = field(
        default=None,
        metadata=dict(
            name="EMDInfo",
            type="Element"
        )
    )
    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata=dict(
            name="EMDSummaryInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class FareDisplay:
    """Fare/Tariff Display.

    :ivar fare_display_rule:
    :ivar fare_pricing:
    :ivar fare_restriction:
    :ivar fare_routing_information:
    :ivar fare_mileage_information:
    :ivar air_fare_display_rule_key:
    :ivar booking_code:
    :ivar account_code:
    :ivar addl_booking_code_information:
    :ivar fare_rule_failure_info: Returns fare rule failure info for Non
                                Valid fares.
    :ivar price_change: Indicates a price change is found in Fare Control Manager
    :ivar carrier:
    :ivar fare_basis:
    :ivar amount:
    :ivar trip_type:
    :ivar fare_type_code:
    :ivar special_fare:
    :ivar instant_purchase:
    :ivar eligibility_restricted:
    :ivar flight_restricted:
    :ivar stopovers_restricted:
    :ivar transfers_restricted:
    :ivar blackouts_exist:
    :ivar accompanied_travel:
    :ivar mile_or_route_based_fare:
    :ivar global_indicator:
    :ivar origin: Returns the origin airport or city code
                            for which this tariff is applicable.
    :ivar destination: Returns the destination airport or city
                            code for which this tariff is applicable.
    :ivar fare_ticketing_code: Returns the ticketing code for which this tariff is applicable.
    :ivar fare_ticketing_designator: Returns the ticketing designator for which this tariff is applicable.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_display_rule: Optional[FareDisplayRule] = field(
        default=None,
        metadata=dict(
            name="FareDisplayRule",
            type="Element",
            required=True
        )
    )
    fare_pricing: List[FarePricing] = field(
        default_factory=list,
        metadata=dict(
            name="FarePricing",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    fare_restriction: List[FareRestriction] = field(
        default_factory=list,
        metadata=dict(
            name="FareRestriction",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    fare_routing_information: Optional[FareRoutingInformation] = field(
        default=None,
        metadata=dict(
            name="FareRoutingInformation",
            type="Element"
        )
    )
    fare_mileage_information: Optional[FareMileageInformation] = field(
        default=None,
        metadata=dict(
            name="FareMileageInformation",
            type="Element"
        )
    )
    air_fare_display_rule_key: Optional[AirFareDisplayRuleKey] = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayRuleKey",
            type="Element"
        )
    )
    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata=dict(
            name="BookingCode",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    addl_booking_code_information: Optional[AddlBookingCodeInformation] = field(
        default=None,
        metadata=dict(
            name="AddlBookingCodeInformation",
            type="Element"
        )
    )
    fare_rule_failure_info: Optional[FareRuleFailureInfo] = field(
        default=None,
        metadata=dict(
            name="FareRuleFailureInfo",
            type="Element"
        )
    )
    price_change: List[PriceChangeType] = field(
        default_factory=list,
        metadata=dict(
            name="PriceChange",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            length=2
        )
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            required=True
        )
    )
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True
        )
    )
    trip_type: Optional[TypeFareTripType] = field(
        default=None,
        metadata=dict(
            name="TripType",
            type="Attribute"
        )
    )
    fare_type_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareTypeCode",
            type="Attribute",
            min_length=1,
            max_length=5
        )
    )
    special_fare: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="SpecialFare",
            type="Attribute"
        )
    )
    instant_purchase: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="InstantPurchase",
            type="Attribute"
        )
    )
    eligibility_restricted: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="EligibilityRestricted",
            type="Attribute"
        )
    )
    flight_restricted: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="FlightRestricted",
            type="Attribute"
        )
    )
    stopovers_restricted: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="StopoversRestricted",
            type="Attribute"
        )
    )
    transfers_restricted: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="TransfersRestricted",
            type="Attribute"
        )
    )
    blackouts_exist: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="BlackoutsExist",
            type="Attribute"
        )
    )
    accompanied_travel: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AccompaniedTravel",
            type="Attribute"
        )
    )
    mile_or_route_based_fare: Optional[TypeMileOrRouteBasedFare] = field(
        default=None,
        metadata=dict(
            name="MileOrRouteBasedFare",
            type="Attribute"
        )
    )
    global_indicator: Optional[TypeAtpcoglobalIndicator] = field(
        default=None,
        metadata=dict(
            name="GlobalIndicator",
            type="Attribute"
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    fare_ticketing_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareTicketingCode",
            type="Attribute"
        )
    )
    fare_ticketing_designator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareTicketingDesignator",
            type="Attribute",
            min_length=0,
            max_length=20
        )
    )


@dataclass
class FareRule:
    """Fare Rule Container.

    :ivar fare_rule_long:
    :ivar fare_rule_short:
    :ivar rule_advanced_purchase:
    :ivar rule_length_of_stay:
    :ivar rule_charges:
    :ivar fare_rule_result_message:
    :ivar structured_fare_rules:
    :ivar fare_info_ref:
    :ivar rule_number:
    :ivar source:
    :ivar tariff_number:
    :ivar provider_code:
    :ivar supplier_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_rule_long: List[FareRuleLong] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleLong",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_rule_short: List[FareRuleShort] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleShort",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    rule_advanced_purchase: Optional[RuleAdvancedPurchase] = field(
        default=None,
        metadata=dict(
            name="RuleAdvancedPurchase",
            type="Element"
        )
    )
    rule_length_of_stay: Optional[RuleLengthOfStay] = field(
        default=None,
        metadata=dict(
            name="RuleLengthOfStay",
            type="Element"
        )
    )
    rule_charges: Optional[RuleCharges] = field(
        default=None,
        metadata=dict(
            name="RuleCharges",
            type="Element"
        )
    )
    fare_rule_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleResultMessage",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    structured_fare_rules: Optional[StructuredFareRulesType] = field(
        default=None,
        metadata=dict(
            name="StructuredFareRules",
            type="Element"
        )
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
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
    source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute"
        )
    )
    tariff_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TariffNumber",
            type="Attribute"
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            min_length=1,
            max_length=5
        )
    )


@dataclass
class FlightDetailsList:
    """The shared object list of FlightDetails.

    :ivar flight_details:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_details: List[FlightDetails] = field(
        default_factory=list,
        metadata=dict(
            name="FlightDetails",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightInformationRsp(BaseRsp):
    """
    :ivar flight_info: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_info: List[FlightInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FlightInfo",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightOption:
    """List of Options available for any search air leg.

    :ivar option: List of BookingInfo available for the search air leg.
    :ivar leg_ref: Identifies the Leg Reference for this Flight Option.
    :ivar origin: The IATA location code for this origination of this entity.
    :ivar destination: The IATA location code for this destination of this entity.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    option: List[Option] = field(
        default_factory=list,
        metadata=dict(
            name="Option",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    leg_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LegRef",
            type="Attribute"
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )


@dataclass
class FlightTimeTableReq(BaseSearchReq):
    """Request for Flight Time Table.

    :ivar flight_time_table_criteria: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_time_table_criteria: Optional[FlightTimeTableCriteria] = field(
        default=None,
        metadata=dict(
            name="FlightTimeTableCriteria",
            type="Element",
            required=True
        )
    )


@dataclass
class FlightTimeTableRsp(BaseSearchRsp):
    """Response for Flight Time Table.

    :ivar flight_time_table_list: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_time_table_list: Optional["FlightTimeTableRsp.FlightTimeTableList"] = field(
        default=None,
        metadata=dict(
            name="FlightTimeTableList",
            type="Element"
        )
    )

    @dataclass
    class FlightTimeTableList:
        """
        :ivar flight_time_detail:
        """
        flight_time_detail: List[FlightTimeDetail] = field(
            default_factory=list,
            metadata=dict(
                name="FlightTimeDetail",
                type="Element",
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class OptionalServices:
    """A wrapper for all the information regarding each of the Optional services.

    :ivar optional_services_total: The total fares, fees and taxes associated
                                with the Optional Services
    :ivar optional_service:
    :ivar grouped_option_info: Details about an unselected or "other" option when optional services are grouped together.
    :ivar optional_service_rules: Holds the rules for selecting the optional
                                service in the itinerary
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    optional_services_total: Optional["OptionalServices.OptionalServicesTotal"] = field(
        default=None,
        metadata=dict(
            name="OptionalServicesTotal",
            type="Element"
        )
    )
    optional_service: List[OptionalService] = field(
        default_factory=list,
        metadata=dict(
            name="OptionalService",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    grouped_option_info: List[GroupedOptionInfo] = field(
        default_factory=list,
        metadata=dict(
            name="GroupedOptionInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_service_rules: List[ServiceRuleType] = field(
        default_factory=list,
        metadata=dict(
            name="OptionalServiceRules",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class OptionalServicesTotal:
        """
        :ivar tax_info:
        :ivar fee_info:
        :ivar total_price: The total price for this entity including base price and all taxes.
        :ivar base_price: Represents the base price for this entity. This does not include any taxes or surcharges.
        :ivar approximate_total_price: The Converted total price in Default Currency for this entity including base price and all taxes.
        :ivar approximate_base_price: The Converted base price in Default Currency for this entity. This does not include any taxes or surcharges.
        :ivar equivalent_base_price: Represents the base price in the related currency for this entity. This does not include any taxes or surcharges.
        :ivar taxes: The aggregated amount of all the taxes that are associated with this entity. See the associated TaxInfo array for a breakdown of the individual taxes.
        :ivar fees: The aggregated amount of all the fees that are associated with this entity. See the associated FeeInfo array for a breakdown of the individual fees.
        :ivar services: The total cost for all optional services.
        :ivar approximate_taxes: The Converted tax amount in Default Currency.
        :ivar approximate_fees: The Converted fee amount in Default Currency.
        """
        tax_info: List[TaxInfo] = field(
            default_factory=list,
            metadata=dict(
                name="TaxInfo",
                type="Element",
                min_occurs=0,
                max_occurs=999
            )
        )
        fee_info: List[FeeInfo] = field(
            default_factory=list,
            metadata=dict(
                name="FeeInfo",
                type="Element",
                min_occurs=0,
                max_occurs=999
            )
        )
        total_price: Optional[str] = field(
            default=None,
            metadata=dict(
                name="TotalPrice",
                type="Attribute"
            )
        )
        base_price: Optional[str] = field(
            default=None,
            metadata=dict(
                name="BasePrice",
                type="Attribute"
            )
        )
        approximate_total_price: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ApproximateTotalPrice",
                type="Attribute"
            )
        )
        approximate_base_price: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ApproximateBasePrice",
                type="Attribute"
            )
        )
        equivalent_base_price: Optional[str] = field(
            default=None,
            metadata=dict(
                name="EquivalentBasePrice",
                type="Attribute"
            )
        )
        taxes: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Taxes",
                type="Attribute"
            )
        )
        fees: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Fees",
                type="Attribute"
            )
        )
        services: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Services",
                type="Attribute"
            )
        )
        approximate_taxes: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ApproximateTaxes",
                type="Attribute"
            )
        )
        approximate_fees: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ApproximateFees",
                type="Attribute"
            )
        )


@dataclass
class PrePayProfileInfo:
    """PrePay Profile associated with the customer.

    :ivar pre_pay_id: Pre pay unique identifier detail.This information block is returned both in list and  detail retrieve transactions.Example flight pass number
    :ivar pre_pay_customer: Pre pay customer detail.This information block is returned both in list and  detail retrieve transactions.
    :ivar pre_pay_account: Pre pay account detail.This information block is returned both in list and  detail retrieve transactions.
    :ivar affiliations: Pre pay affiliations detail.This information block is returned only in detail retrieve transactions.
    :ivar account_related_rules: Pre pay account related rules.This information block is returned only in detail retrieve transactions.
    :ivar status_code: Customer pre pay profile status code(One of Marked for deletion,Lapsed,Terminated,Active,Inactive)
    :ivar creator_id: This is the loyalty card number of the person who originally purchased/setup the flight pass
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    pre_pay_id: Optional[PrePayId] = field(
        default=None,
        metadata=dict(
            name="PrePayId",
            type="Element",
            required=True
        )
    )
    pre_pay_customer: Optional[PrePayCustomer] = field(
        default=None,
        metadata=dict(
            name="PrePayCustomer",
            type="Element"
        )
    )
    pre_pay_account: Optional[PrePayAccount] = field(
        default=None,
        metadata=dict(
            name="PrePayAccount",
            type="Element"
        )
    )
    affiliations: Optional[Affiliations] = field(
        default=None,
        metadata=dict(
            name="Affiliations",
            type="Element"
        )
    )
    account_related_rules: Optional[AccountRelatedRules] = field(
        default=None,
        metadata=dict(
            name="AccountRelatedRules",
            type="Element"
        )
    )
    status_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StatusCode",
            type="Attribute"
        )
    )
    creator_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CreatorID",
            type="Attribute",
            min_length=1,
            max_length=36
        )
    )


@dataclass
class Rows:
    """A wrapper for all the information regarding each of the rows. Providers:
    ACH, 1G, 1V, 1P, 1J.

    :ivar row: Provider: 1G,1V,1P,1J,ACH,MCH.
    :ivar segment_ref: Specifies the AirSegment the seat map is for. Providers: ACH, 1G, 1V, 1P, 1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    row: List[Row] = field(
        default_factory=list,
        metadata=dict(
            name="Row",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute"
        )
    )


@dataclass
class TicketingModifiers:
    """A container to identify individual ticketing modifiers.

    :ivar booking_traveler_ref: Reference to a booking traveler for which ticketing modifier is applied.
    :ivar net_remit: Allows an agency to override the net
                         remittance amount - varies by BSP agreement
    :ivar net_fare: Net Fare amount for a ticketed fare
    :ivar actual_selling_fare: Allows an agency to report an Actual
                         Selling Fare as part of the net remittance BSP agreement
    :ivar invoice_fare: Allows an agency to report an Invoice Fare
                         as part of the net remittance BSP agreement
    :ivar corporate_discount: Allows an agency to add a corporate
                         discount to the itinerary to be ticketed
    :ivar accounting_info: Allows an agency to report Accounting
                         Information as part of the net remittance BSP agreement
    :ivar bulk_ticket: Allows an agency to update the fare as a
                         Bulk ticket - Optional SuppressOnFareCalc attribute will control
                         how fare calculation is printed on the ticket
    :ivar group_tour: Allows an agency to update the fare as a
                         Group Tour (inclusive tour) ticket - Optional SuppressOnFareCalc
                         attribute will control how fare calculation is printed on the
                         ticket
    :ivar commission: Allows an agency to update the commission
                         to a new or different commission rate which will be applied at
                         time of ticketing. The commission Modifier allows the user
                         specify how the commission change is to applied
    :ivar tour_code: Allows an agency to modify the tour code
                         information on the ticket
    :ivar ticket_endorsement: Allows an agency to add user defined
                         ticketing endorsements the ticket
    :ivar value_modifier: Allows an agency to modify value or
                         commission of the ticket. The modifier is generic and depends on
                         the specific GDS and BSP implementation
    :ivar document_select:
    :ivar document_options:
    :ivar segment_select:
    :ivar segment_modifiers:
    :ivar supplier_locator:
    :ivar destination_purpose_code:
    :ivar language_option:
    :ivar land_charges:
    :ivar print_blank_form_itinerary:
    :ivar exclude_ticketing:
    :ivar exempt_obfee:
    :ivar is_primary_di: Indicates if the DI is Primary DI. 1P only
    :ivar document_instruction_number: The Document Instruction line number. 1P only
    :ivar reference: Identifies if TicketingModifiers contains DI line information. 1P only.
    :ivar status: DI line status - ex:Ticketed
    :ivar free_text: DI line information shown as free text as in Host. 1P only
    :ivar name_number: Host Name Number
    :ivar ticket_record: Ticket Record Number
    :ivar plating_carrier: Allows an agency to specify the Plating
                      Carrier for ticketing
    :ivar exempt_vat: Allows an agency to update if VAT is
                      Exemtped on the fare.
    :ivar net_remit_applied: Indicator to the BSP net remittance
                      scheme applies to ticketed fare.
    :ivar free_ticket: Indicates free ticket.
    :ivar currency_override_code: This modifier allows an agency to specify the currency like L for Local, E for Euro, U for USD, C for CAD (Canadian dollars).
    :ivar key:
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    net_remit: Optional[TypeTicketModifierAmountType] = field(
        default=None,
        metadata=dict(
            name="NetRemit",
            type="Element"
        )
    )
    net_fare: Optional[TypeTicketModifierAmountType] = field(
        default=None,
        metadata=dict(
            name="NetFare",
            type="Element"
        )
    )
    actual_selling_fare: Optional[TypeTicketModifierAmountType] = field(
        default=None,
        metadata=dict(
            name="ActualSellingFare",
            type="Element"
        )
    )
    invoice_fare: Optional[TypeTicketModifierAccountingType] = field(
        default=None,
        metadata=dict(
            name="InvoiceFare",
            type="Element"
        )
    )
    corporate_discount: Optional[TypeTicketModifierAccountingType] = field(
        default=None,
        metadata=dict(
            name="CorporateDiscount",
            type="Element"
        )
    )
    accounting_info: Optional[TypeTicketModifierAccountingType] = field(
        default=None,
        metadata=dict(
            name="AccountingInfo",
            type="Element"
        )
    )
    bulk_ticket: Optional["TicketingModifiers.BulkTicket"] = field(
        default=None,
        metadata=dict(
            name="BulkTicket",
            type="Element"
        )
    )
    group_tour: Optional[TypeBulkTicketModifierType] = field(
        default=None,
        metadata=dict(
            name="GroupTour",
            type="Element"
        )
    )
    commission: Optional[Commission] = field(
        default=None,
        metadata=dict(
            name="Commission",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    tour_code: Optional[TourCode] = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Element"
        )
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata=dict(
            name="TicketEndorsement",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    value_modifier: Optional[TypeTicketModifierValueType] = field(
        default=None,
        metadata=dict(
            name="ValueModifier",
            type="Element"
        )
    )
    document_select: Optional[DocumentSelect] = field(
        default=None,
        metadata=dict(
            name="DocumentSelect",
            type="Element"
        )
    )
    document_options: Optional[DocumentOptions] = field(
        default=None,
        metadata=dict(
            name="DocumentOptions",
            type="Element"
        )
    )
    segment_select: Optional[SegmentSelect] = field(
        default=None,
        metadata=dict(
            name="SegmentSelect",
            type="Element"
        )
    )
    segment_modifiers: List[SegmentModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="SegmentModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    supplier_locator: Optional[SupplierLocator] = field(
        default=None,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    destination_purpose_code: Optional[DestinationPurposeCode] = field(
        default=None,
        metadata=dict(
            name="DestinationPurposeCode",
            type="Element"
        )
    )
    language_option: List[LanguageOption] = field(
        default_factory=list,
        metadata=dict(
            name="LanguageOption",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )
    land_charges: Optional[LandCharges] = field(
        default=None,
        metadata=dict(
            name="LandCharges",
            type="Element"
        )
    )
    print_blank_form_itinerary: Optional[PrintBlankFormItinerary] = field(
        default=None,
        metadata=dict(
            name="PrintBlankFormItinerary",
            type="Element"
        )
    )
    exclude_ticketing: Optional[ExcludeTicketing] = field(
        default=None,
        metadata=dict(
            name="ExcludeTicketing",
            type="Element"
        )
    )
    exempt_obfee: Optional[ExemptObfee] = field(
        default=None,
        metadata=dict(
            name="ExemptOBFee",
            type="Element"
        )
    )
    is_primary_di: bool = field(
        default=False,
        metadata=dict(
            name="IsPrimaryDI",
            type="Attribute"
        )
    )
    document_instruction_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocumentInstructionNumber",
            type="Attribute"
        )
    )
    reference: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Reference",
            type="Attribute",
            min_length=1,
            max_length=30
        )
    )
    status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            max_length=30
        )
    )
    free_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FreeText",
            type="Attribute",
            max_length=756
        )
    )
    name_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NameNumber",
            type="Attribute"
        )
    )
    ticket_record: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketRecord",
            type="Attribute"
        )
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            length=2
        )
    )
    exempt_vat: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ExemptVAT",
            type="Attribute"
        )
    )
    net_remit_applied: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NetRemitApplied",
            type="Attribute"
        )
    )
    free_ticket: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="FreeTicket",
            type="Attribute"
        )
    )
    currency_override_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyOverrideCode",
            type="Attribute",
            length=1
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )

    @dataclass
    class BulkTicket(TypeBulkTicketModifierType):
        """
        :ivar non_refundable: Indicates bulk ticket being
                                         non-refundable
        """
        non_refundable: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="NonRefundable",
                type="Attribute"
            )
        )


@dataclass
class TypeBaseAirSegment(Segment):
    """
    :ivar sponsored_flt_info:
    :ivar codeshare_info:
    :ivar air_avail_info:
    :ivar flight_details:
    :ivar flight_details_ref:
    :ivar alternate_location_distance_ref:
    :ivar connection:
    :ivar sell_message:
    :ivar rail_coach_details:
    :ivar open_segment: Indicates OpenSegment when True
    :ivar group: The Origin Destination Grouping of this
                                    segment.
    :ivar carrier: The carrier that is marketing this segment
    :ivar cabin_class: Specifies Cabin class for a group of
                                    class of services. Cabin class is not identified if it is not
                                    present.
    :ivar flight_number: The flight number under which the marketing
                                    carrier is marketing this flight
    :ivar origin: The IATA location code for this origination of this entity.
    :ivar destination: The IATA location code for this destination of this entity.
    :ivar departure_time: The date and time at which this entity departs. Date and time are represented as Airport Local Time at the place of departure. The correct time zone offset is also included.
    :ivar arrival_time: The date and time at which this entity arrives at the destination. Date and time are represented as Airport Local Time at the place of arrival. The correct time zone offset is also included.
    :ivar flight_time: Time spent (minutes) traveling in flight, including airport taxi time.
    :ivar travel_time: Total time spent (minutes) traveling including flight time and ground time.
    :ivar distance: The distance traveled. Units are specified in the parent response element.
    :ivar provider_code:
    :ivar supplier_code:
    :ivar participant_level: Type of sell agreement between host and link
                        carrier.
    :ivar link_availability: Indicates if carrier has link (carrier
                        specific) display option.
    :ivar polled_availability_option: Indicates if carrier has Inside
                        (polled)Availability option.
    :ivar availability_display_type: The type of availability from which the segment is sold.Possible Values (List):
                                        G - General
                                        S - Flight Specific
                                        L - Carrier Specific/Direct Access
                                        M - Manual Sell
                                        F - Fare Shop/Optimal Shop
                                        Q - Fare Specific Fare Quote unbooked
                                        R - Redemption Availability used to complete the sell. Supported Providers: 1G,1V.
    :ivar class_of_service:
    :ivar eticketability: Identifies if this particular segment
                                    is E-Ticketable
    :ivar equipment: Identifies the equipment that this
                                    segment is operating under.
    :ivar marriage_group: Identifies this segment as being a
                                    married segment. It is paired with other segments of the same
                                    value.
    :ivar number_of_stops: Identifies the number of stops for
                                    each within the segment.
    :ivar seamless: Identifies that this segment was sold
                                    via a direct access channel to the marketing carrier.
    :ivar change_of_plane: Indicates the traveler must change
                                    planes between flights.
    :ivar guaranteed_payment_carrier: Identifies that this segment has
                                    Guaranteed Payment Carrier.
    :ivar host_token_ref: Identifies that this segment has
                                    Guaranteed Payment Carrier.
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar passive_provider_reservation_info_ref: Provider reservation reference key.
    :ivar optional_services_indicator: Indicates true if flight provides
                                    optional services.
    :ivar availability_source: Indicates Availability source of
                                    AirSegment.
    :ivar apisrequirements_ref: Reference to the APIS Requirements for
                                    this AirSegment.
    :ivar black_listed: Indicates blacklisted carriers which are banned from servicing points to, from and within the European Community.
    :ivar operational_status: Refers to the flight operational status for the segment.
                                This attribute will only be returned in the AvailabilitySearchRsp and not used/returned in any other request/responses.
                                If this attribute is not returned back in the response, it means the flight is operational and not past scheduled departure.
    :ivar number_in_party: Number of person traveling in this air segment excluding the number of infants on lap.
    :ivar rail_coach_number: Coach number for which rail seatmap/coachmap is returned.
    :ivar booking_date: Used for rapid reprice. The date the booking was made.
                            Providers: 1G/1V/1P/1S/1A
    :ivar flown_segment: Used for rapid reprice. Tells whether or not the air segment has been flown.
                            Providers: 1G/1V/1P/1S/1A
    :ivar schedule_change: Used for rapid reprice. Tells whether or not the air segment had a
                            schedule change by the carrier. This tells rapid reprice that the change in the air
                            segment was involuntary and because of a schedule change, not because the user is
                            changing the segment. Providers: 1G/1V/1P/1S/1A
    :ivar brand_indicator: Value “B” specifies that the carrier supports Rich Content and Branding.  The Brand Indicator is only returned in the availability search response.  Provider: 1G, 1V, 1P, 1J, ACH
    """
    class Meta:
        name = "typeBaseAirSegment"

    sponsored_flt_info: Optional[SponsoredFltInfo] = field(
        default=None,
        metadata=dict(
            name="SponsoredFltInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    codeshare_info: Optional[CodeshareInfo] = field(
        default=None,
        metadata=dict(
            name="CodeshareInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    air_avail_info: List[AirAvailInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirAvailInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    flight_details: List[FlightDetails] = field(
        default_factory=list,
        metadata=dict(
            name="FlightDetails",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    flight_details_ref: List[FlightDetailsRef] = field(
        default_factory=list,
        metadata=dict(
            name="FlightDetailsRef",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    alternate_location_distance_ref: List[AlternateLocationDistanceRef] = field(
        default_factory=list,
        metadata=dict(
            name="AlternateLocationDistanceRef",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    connection: Optional[Connection] = field(
        default=None,
        metadata=dict(
            name="Connection",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    sell_message: List[SellMessage] = field(
        default_factory=list,
        metadata=dict(
            name="SellMessage",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_coach_details: List[RailCoachDetails] = field(
        default_factory=list,
        metadata=dict(
            name="RailCoachDetails",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    open_segment: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="OpenSegment",
            type="Attribute"
        )
    )
    group: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Group",
            type="Attribute",
            required=True
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            length=2
        )
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute"
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            max_length=5
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute"
        )
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute"
        )
    )
    flight_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FlightTime",
            type="Attribute"
        )
    )
    travel_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute"
        )
    )
    distance: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Distance",
            type="Attribute"
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            min_length=1,
            max_length=5
        )
    )
    participant_level: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ParticipantLevel",
            type="Attribute"
        )
    )
    link_availability: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="LinkAvailability",
            type="Attribute"
        )
    )
    polled_availability_option: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PolledAvailabilityOption",
            type="Attribute"
        )
    )
    availability_display_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AvailabilityDisplayType",
            type="Attribute"
        )
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            min_length=1,
            max_length=2
        )
    )
    eticketability: Optional[TypeEticketability] = field(
        default=None,
        metadata=dict(
            name="ETicketability",
            type="Attribute"
        )
    )
    equipment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Equipment",
            type="Attribute",
            length=3
        )
    )
    marriage_group: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MarriageGroup",
            type="Attribute"
        )
    )
    number_of_stops: Optional[int] = field(
        default=None,
        metadata=dict(
            name="NumberOfStops",
            type="Attribute"
        )
    )
    seamless: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Seamless",
            type="Attribute"
        )
    )
    change_of_plane: bool = field(
        default=False,
        metadata=dict(
            name="ChangeOfPlane",
            type="Attribute"
        )
    )
    guaranteed_payment_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="GuaranteedPaymentCarrier",
            type="Attribute"
        )
    )
    host_token_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="HostTokenRef",
            type="Attribute"
        )
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute"
        )
    )
    passive_provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PassiveProviderReservationInfoRef",
            type="Attribute"
        )
    )
    optional_services_indicator: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="OptionalServicesIndicator",
            type="Attribute"
        )
    )
    availability_source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AvailabilitySource",
            type="Attribute",
            max_length=1
        )
    )
    apisrequirements_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="APISRequirementsRef",
            type="Attribute"
        )
    )
    black_listed: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="BlackListed",
            type="Attribute"
        )
    )
    operational_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OperationalStatus",
            type="Attribute"
        )
    )
    number_in_party: Optional[int] = field(
        default=None,
        metadata=dict(
            name="NumberInParty",
            type="Attribute",
            min_inclusive=1,
            max_inclusive=99
        )
    )
    rail_coach_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RailCoachNumber",
            type="Attribute",
            max_length=4
        )
    )
    booking_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BookingDate",
            type="Attribute"
        )
    )
    flown_segment: bool = field(
        default=False,
        metadata=dict(
            name="FlownSegment",
            type="Attribute"
        )
    )
    schedule_change: bool = field(
        default=False,
        metadata=dict(
            name="ScheduleChange",
            type="Attribute"
        )
    )
    brand_indicator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandIndicator",
            type="Attribute"
        )
    )


@dataclass
class AirFareDisplayRsp(BaseRsp):
    """Response to an AirFareDisplayReq.

    :ivar fare_display: Provider: 1G,1V,1P,1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_display: List[FareDisplay] = field(
        default_factory=list,
        metadata=dict(
            name="FareDisplay",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirFareRulesRsp(BaseRsp):
    """Response to an AirFareRuleReq.

    :ivar fare_rule: Provider: 1G,1V,1P,1J,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirPrePayRsp(BaseRsp):
    """Flight Pass Response.

    :ivar pre_pay_profile_info: Provider: ACH.
    :ivar max_results: Provider: ACH-Max Number of Flight Passes being returned.
    :ivar more_indicator: Provider: ACH-Indicates if there are more flight passes to be offered
    :ivar more_data_start_index: Provider: ACH-Indicates start index of the next flight Passes
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    pre_pay_profile_info: List[PrePayProfileInfo] = field(
        default_factory=list,
        metadata=dict(
            name="PrePayProfileInfo",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    max_results: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MaxResults",
            type="Attribute",
            min_inclusive=1,
            max_inclusive=200
        )
    )
    more_indicator: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="MoreIndicator",
            type="Attribute"
        )
    )
    more_data_start_index: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MoreDataStartIndex",
            type="Attribute"
        )
    )


@dataclass
class AirPricingTicketingModifiers:
    """AirPricing TicketingModifier information.

                    - used to associate Ticketing Modifiers with one or more
                    AirPricingInfos/ProviderReservationInfo
    :ivar air_pricing_info_ref:
    :ivar ticketing_modifiers:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticketing_modifiers: Optional[TicketingModifiers] = field(
        default=None,
        metadata=dict(
            name="TicketingModifiers",
            type="Element",
            required=True
        )
    )


@dataclass
class AirSegment(TypeBaseAirSegment):
    """An Air marketable travel segment."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class BaggageAllowances:
    """Details of Baggage allowance.

    :ivar baggage_allowance_info:
    :ivar carry_on_allowance_info:
    :ivar embargo_info:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    baggage_allowance_info: List[BaggageAllowanceInfo] = field(
        default_factory=list,
        metadata=dict(
            name="BaggageAllowanceInfo",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    carry_on_allowance_info: List[CarryOnAllowanceInfo] = field(
        default_factory=list,
        metadata=dict(
            name="CarryOnAllowanceInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    embargo_info: List[EmbargoInfo] = field(
        default_factory=list,
        metadata=dict(
            name="EmbargoInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class Brand:
    """Commercially recognized product offered by an airline.

    :ivar title: The additional titles associated to the brand
    :ivar text: Text associated to the brand
    :ivar image_location: Images associated to the brand
    :ivar optional_services:
    :ivar rules: Brand rules
    :ivar service_associations: Service associated with this brand
    :ivar upsell_brand: The unique identifier of the Upsell brand
    :ivar applicable_segment:
    :ivar default_brand_detail: Default brand details.
    :ivar key: Brand Key
    :ivar brand_id: The unique identifier of the brand
    :ivar name: The Title of the brand
    :ivar air_itinerary_details_ref: AirItinerary associated with this brand
    :ivar up_sell_brand_id:
    :ivar brand_found: Indicates whether brand for the fare was found for carrier or not
    :ivar up_sell_brand_found: Indicates whether upsell brand for the fare was found for carrier or not
    :ivar branded_details_available: Indicates if full details of the brand is available
    :ivar carrier:
    :ivar brand_tier: Modifier to price by specific brand tier number.
    :ivar brand_maintained: Indicates whether the brand was maintained from the original ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    title: List[Title] = field(
        default_factory=list,
        metadata=dict(
            name="Title",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )
    text: List[Text] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata=dict(
            name="ImageLocation",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    rules: List[Rules] = field(
        default_factory=list,
        metadata=dict(
            name="Rules",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    service_associations: Optional[ServiceAssociations] = field(
        default=None,
        metadata=dict(
            name="ServiceAssociations",
            type="Element"
        )
    )
    upsell_brand: Optional[UpsellBrand] = field(
        default=None,
        metadata=dict(
            name="UpsellBrand",
            type="Element"
        )
    )
    applicable_segment: List[TypeApplicableSegment] = field(
        default_factory=list,
        metadata=dict(
            name="ApplicableSegment",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    default_brand_detail: List[DefaultBrandDetail] = field(
        default_factory=list,
        metadata=dict(
            name="DefaultBrandDetail",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandID",
            type="Attribute",
            min_length=1,
            max_length=19
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute"
        )
    )
    air_itinerary_details_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirItineraryDetailsRef",
            type="Attribute"
        )
    )
    up_sell_brand_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="UpSellBrandID",
            type="Attribute",
            min_length=1,
            max_length=19
        )
    )
    brand_found: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="BrandFound",
            type="Attribute"
        )
    )
    up_sell_brand_found: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="UpSellBrandFound",
            type="Attribute"
        )
    )
    branded_details_available: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="BrandedDetailsAvailable",
            type="Attribute"
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            length=2
        )
    )
    brand_tier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandTier",
            type="Attribute",
            min_length=1,
            max_length=10
        )
    )
    brand_maintained: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandMaintained",
            type="Attribute",
            min_length=1,
            max_length=99
        )
    )


@dataclass
class FlightOptionsList:
    """List of Flight Options for the itinerary.

    :ivar flight_option:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    flight_option: List[FlightOption] = field(
        default_factory=list,
        metadata=dict(
            name="FlightOption",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirItinerary:
    """A container for an Air only travel itinerary.

    :ivar air_segment:
    :ivar host_token:
    :ivar apisrequirements:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    apisrequirements: List[Apisrequirements] = field(
        default_factory=list,
        metadata=dict(
            name="APISRequirements",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirMerchandisingDetailsRsp(BaseRsp):
    """Response for retrieved brand details and optional services included in them.

    :ivar optional_services:
    :ivar brand:
    :ivar unassociated_booking_code_list: Lists classes of service by segment sent in the request which are not associated to a brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    brand: List[Brand] = field(
        default_factory=list,
        metadata=dict(
            name="Brand",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    unassociated_booking_code_list: Optional["AirMerchandisingDetailsRsp.UnassociatedBookingCodeList"] = field(
        default=None,
        metadata=dict(
            name="UnassociatedBookingCodeList",
            type="Element"
        )
    )

    @dataclass
    class UnassociatedBookingCodeList:
        """
        :ivar applicable_segment:
        """
        applicable_segment: List[TypeApplicableSegment] = field(
            default_factory=list,
            metadata=dict(
                name="ApplicableSegment",
                type="Element",
                min_occurs=0,
                max_occurs=99
            )
        )


@dataclass
class AirSegmentData:
    """The shared object list of AirsegmentData.

    :ivar air_segment_ref:
    :ivar baggage_allowance:
    :ivar brand:
    :ivar cabin_class: Specifies Cabin class for a group of class of services. Cabin class is not identified if it is not present.
    :ivar class_of_service:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    baggage_allowance: List[BaggageAllowance] = field(
        default_factory=list,
        metadata=dict(
            name="BaggageAllowance",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    brand: List[Brand] = field(
        default_factory=list,
        metadata=dict(
            name="Brand",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute"
        )
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            min_length=1,
            max_length=2
        )
    )


@dataclass
class AirSegmentError:
    """Container to return error messages corresponding to AirSegment.

    :ivar air_segment:
    :ivar error_message:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: Optional[AirSegment] = field(
        default=None,
        metadata=dict(
            name="AirSegment",
            type="Element",
            required=True
        )
    )
    error_message: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ErrorMessage",
            type="Element",
            required=True
        )
    )


@dataclass
class AirSegmentList:
    """The shared object list of AirSegments.

    :ivar air_segment:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirSolution:
    """Defines an air solution that is comprised of an itinerary (the segments)
    along with the passengers.

    :ivar search_traveler:
    :ivar air_segment:
    :ivar host_token:
    :ivar fare_basis:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="SearchTraveler",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=1,
            max_occurs=16
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=16
        )
    )
    fare_basis: List[FareBasis] = field(
        default_factory=list,
        metadata=dict(
            name="FareBasis",
            type="Element",
            min_occurs=0,
            max_occurs=16
        )
    )


@dataclass
class BrandList:
    """
    :ivar brand:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    brand: List[Brand] = field(
        default_factory=list,
        metadata=dict(
            name="Brand",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class ExchangeAirSegment:
    """A container to define segment and cabin class in order to process an
    exchange.

    :ivar air_segment:
    :ivar cabin_class:
    :ivar fare_basis_code: The fare basis code to be used for exchange of
                            this segment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: Optional[AirSegment] = field(
        default=None,
        metadata=dict(
            name="AirSegment",
            type="Element",
            required=True
        )
    )
    cabin_class: Optional[CabinClass] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    fare_basis_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareBasisCode",
            type="Attribute"
        )
    )


@dataclass
class FareInfo:
    """Information about this fare component.

    :ivar fare_ticket_designator:
    :ivar fare_surcharge:
    :ivar account_code:
    :ivar contract_code:
    :ivar endorsement:
    :ivar baggage_allowance:
    :ivar fare_rule_key:
    :ivar fare_rule_failure_info:
    :ivar fare_remark_ref:
    :ivar brand:
    :ivar commission: Specifies the Commission for Agency for a particular Fare component. Apllicable Providers are 1G and 1V.
    :ivar fare_attributes: Returns all fare attributes separated by pipe ‘|’. Attribute information is returned by comma separated values for each attribute. These information include attribute number, chargeable indicator and supplementary info. Attribute numbers: 1 - Checked Bag, 2 - Carry On, 3 - Rebooking, 4 - Refund, 5 - Seats, 6 - Meals, 7 - WiFi. Chargeable Indicator: Y - Chargeable, N - Not Chargeable. Supplementary Information that will be returned is : For 1 and 2 - Baggage weights. For 3 – Changeable Info. For 4 – Refundable Info. For 5 - Seat description. For 6 – Meal description. For 7 – WiFi description. Example: 1,Y,23|1,N,50|2,N,8|3,N,CHANGEABLE|4,Y,REFUNDABLE|5,N,SEATING|5,N,MIDDLE|6,Y,SOFT DRINK|6,N,ALCOHOLIC DRINK|6,Y,SNACK|7,X,WIFI
    :ivar change_penalty: The penalty (if any) to change the itinerary
    :ivar cancel_penalty: The penalty (if any) to cancel the fare
    :ivar fare_rules_filter:
    :ivar key:
    :ivar fare_basis: The fare basis code for this fare
    :ivar passenger_type_code: The PTC that is associated with this fare.
    :ivar origin: Returns the airport or city code that
                            defines the origin market for this fare.
    :ivar destination: Returns the airport or city code that
                            defines the destination market for this fare.
    :ivar effective_date: Returns the date on which this fare was
                            quoted
    :ivar travel_date: Returns the departure date of the first
                            segment that uses this fare.
    :ivar departure_date: Returns the departure date of the first
                            segment of the journey.
    :ivar amount:
    :ivar private_fare:
    :ivar negotiated_fare: Identifies the fare as a Negotiated
                            Fare.
    :ivar tour_code:
    :ivar waiver_code:
    :ivar not_valid_before: Fare not valid before this date.
    :ivar not_valid_after: Fare not valid after this date.
    :ivar pseudo_city_code: Provider PseudoCityCode associated with
                            private fare.
    :ivar fare_family: An alpha-numeric string which denotes fare
                            family. Some carriers may return this in lieu of or in addition to
                            the CabinClass.
    :ivar promotional_fare: Boolean to describe whether the Fare is Promotional fare or not.
    :ivar car_code:
    :ivar value_code:
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    :ivar bulk_ticket: Whether the ticket can be issued as bulk for this
                            fare. Providers supported: Worldspan and JAL
    :ivar inclusive_tour: Whether the ticket can be issued as part of
                            included package for this fare. Providers supported: Worldspan and
                            JAL
    :ivar value: Used in rapid reprice
    :ivar supplier_code: Code of the provider returning this fare info
    :ivar tax_amount: Currency code and value for the approximate tax amount for this fare component.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_ticket_designator: List[FareTicketDesignator] = field(
        default_factory=list,
        metadata=dict(
            name="FareTicketDesignator",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_surcharge: List[FareSurcharge] = field(
        default_factory=list,
        metadata=dict(
            name="FareSurcharge",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    contract_code: List[ContractCode] = field(
        default_factory=list,
        metadata=dict(
            name="ContractCode",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    endorsement: List[Endorsement] = field(
        default_factory=list,
        metadata=dict(
            name="Endorsement",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    baggage_allowance: Optional[BaggageAllowance] = field(
        default=None,
        metadata=dict(
            name="BaggageAllowance",
            type="Element"
        )
    )
    fare_rule_key: Optional[FareRuleKey] = field(
        default=None,
        metadata=dict(
            name="FareRuleKey",
            type="Element"
        )
    )
    fare_rule_failure_info: Optional[FareRuleFailureInfo] = field(
        default=None,
        metadata=dict(
            name="FareRuleFailureInfo",
            type="Element"
        )
    )
    fare_remark_ref: List[FareRemarkRef] = field(
        default_factory=list,
        metadata=dict(
            name="FareRemarkRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    brand: Optional[Brand] = field(
        default=None,
        metadata=dict(
            name="Brand",
            type="Element"
        )
    )
    commission: Optional[Commission] = field(
        default=None,
        metadata=dict(
            name="Commission",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    fare_attributes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareAttributes",
            type="Element"
        )
    )
    change_penalty: Optional[TypeFarePenalty] = field(
        default=None,
        metadata=dict(
            name="ChangePenalty",
            type="Element"
        )
    )
    cancel_penalty: Optional[TypeFarePenalty] = field(
        default=None,
        metadata=dict(
            name="CancelPenalty",
            type="Element"
        )
    )
    fare_rules_filter: Optional[FareRulesFilter] = field(
        default=None,
        metadata=dict(
            name="FareRulesFilter",
            type="Element"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            required=True
        )
    )
    passenger_type_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PassengerTypeCode",
            type="Attribute",
            required=True,
            min_length=3,
            max_length=5
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            required=True,
            length=3,
            white_space="collapse"
        )
    )
    effective_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EffectiveDate",
            type="Attribute",
            required=True
        )
    )
    travel_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelDate",
            type="Attribute"
        )
    )
    departure_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute"
        )
    )
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute"
        )
    )
    private_fare: Optional[TypePrivateFare] = field(
        default=None,
        metadata=dict(
            name="PrivateFare",
            type="Attribute"
        )
    )
    negotiated_fare: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NegotiatedFare",
            type="Attribute"
        )
    )
    tour_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Attribute",
            max_length=15
        )
    )
    waiver_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Attribute"
        )
    )
    not_valid_before: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NotValidBefore",
            type="Attribute"
        )
    )
    not_valid_after: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NotValidAfter",
            type="Attribute"
        )
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=2,
            max_length=10
        )
    )
    fare_family: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareFamily",
            type="Attribute",
            min_length=0,
            max_length=32
        )
    )
    promotional_fare: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="PromotionalFare",
            type="Attribute"
        )
    )
    car_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CarCode",
            type="Attribute",
            max_length=15
        )
    )
    value_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ValueCode",
            type="Attribute",
            max_length=15
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )
    bulk_ticket: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="BulkTicket",
            type="Attribute"
        )
    )
    inclusive_tour: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="InclusiveTour",
            type="Attribute"
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute"
        )
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            min_length=1,
            max_length=5
        )
    )
    tax_amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TaxAmount",
            type="Attribute"
        )
    )


@dataclass
class FlightDetailsReq(BaseReq):
    """Request for the Flight Details of segments.

    :ivar air_segment: Provider: 1G,1V,1P,1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightDetailsRsp(BaseRsp):
    """
    :ivar air_segment: Provider: 1G,1V,1P,1J.
    :ivar co2_emissions:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    co2_emissions: List[Co2Emissions] = field(
        default_factory=list,
        metadata=dict(
            name="CO2Emissions",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class JourneyData:
    """Performs journey aware air availability.

    :ivar air_segment:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class SeatMapReq(BaseReq):
    """Request a seat map for the give flight information.

    :ivar agency_sell_info: Provider: ACH-Required if the user requesting the seat map is not the same agent authenticated in the request.
    :ivar air_segment: Provider: 1G,1V,1P,1J,ACH,MCH.
    :ivar host_token: Provider: ACH-Required if the carrier has multiple adapters.
    :ivar search_traveler: Provider: 1G,1V,ACH,MCH.
    :ivar host_reservation: Provider: ACH,MCH-Required when seat price is requested.
    :ivar merchandising_pricing_modifiers: Used to provide additional pricing options. Provider:ACH.
    :ivar return_seat_pricing: Provider: 1G,1V,1P,1J,ACH-When set to true the price of the seat will be returned if it exists.
    :ivar return_branding_info: A value of true will return the BrandingInfo block in the response if applicable. A value of false will not return the BrandingInfo block in the response. Providers: 1G, 1V, 1P, 1J, ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    agency_sell_info: Optional[AgencySellInfo] = field(
        default=None,
        metadata=dict(
            name="AgencySellInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )
    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="SearchTraveler",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_reservation: Optional[HostReservation] = field(
        default=None,
        metadata=dict(
            name="HostReservation",
            type="Element"
        )
    )
    merchandising_pricing_modifiers: Optional[MerchandisingPricingModifiers] = field(
        default=None,
        metadata=dict(
            name="MerchandisingPricingModifiers",
            type="Element"
        )
    )
    return_seat_pricing: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ReturnSeatPricing",
            type="Attribute",
            required=True
        )
    )
    return_branding_info: bool = field(
        default=False,
        metadata=dict(
            name="ReturnBrandingInfo",
            type="Attribute"
        )
    )


@dataclass
class SeatMapRsp(BaseRsp):
    """
    :ivar host_token: Provider: ACH,MCH.
    :ivar cabin_class: Provider: 1G,1V,1P,1J,ACH,MCH.
    :ivar air_segment: Provider: ACH,MCH.
    :ivar search_traveler: Provider: ACH,MCH.
    :ivar optional_services: A wrapper for all the information regarding each of the Optional Services.
                                    	Provider: 1G,1V,1P,1J,ACH.
    :ivar remark: Provider: 1G,1V,1P,1J,ACH,MCH.
    :ivar rows:
    :ivar payment_restriction: Provider: MCH-Information regarding valid payment types, if restrictions apply(supplier specific)
    :ivar seat_information:
    :ivar copyright: Copyright text applicable for some seat content. Providers: 1G, 1V, 1P, 1J,ACH
    :ivar group_seat_price: Provider: 1G,1V-Seat price for the all passengers traveling together only when supplier provides group flat fee.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )
    cabin_class: Optional[CabinClass] = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="SearchTraveler",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    remark: Optional[Remark] = field(
        default=None,
        metadata=dict(
            name="Remark",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    rows: List[Rows] = field(
        default_factory=list,
        metadata=dict(
            name="Rows",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    payment_restriction: List[PaymentRestriction] = field(
        default_factory=list,
        metadata=dict(
            name="PaymentRestriction",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    seat_information: List[SeatInformation] = field(
        default_factory=list,
        metadata=dict(
            name="SeatInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    copyright: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Copyright",
            type="Element"
        )
    )
    group_seat_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="GroupSeatPrice",
            type="Attribute"
        )
    )


@dataclass
class TcrrefundBundle:
    """Bundle refund, pricing, and penalty information for a TCR reservation Used
    both in request and response.

    :ivar air_refund_info:
    :ivar waiver_code:
    :ivar air_segment:
    :ivar fee_info:
    :ivar tax_info: Itinerary level taxes
    :ivar host_token:
    :ivar tcrnumber: The identifying number for a Ticketless Air
                            Reservation.
    :ivar refund_type: Specifies whether this bundle was auto
                            or manually generated
    :ivar refund_access_code:
    """
    class Meta:
        name = "TCRRefundBundle"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_refund_info: Optional[AirRefundInfo] = field(
        default=None,
        metadata=dict(
            name="AirRefundInfo",
            type="Element",
            required=True
        )
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element"
        )
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Attribute",
            required=True
        )
    )
    refund_type: Optional["TcrrefundBundle.RefundType"] = field(
        default=None,
        metadata=dict(
            name="RefundType",
            type="Attribute",
            required=True
        )
    )
    refund_access_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RefundAccessCode",
            type="Attribute",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_length=1,
            max_length=32
        )
    )

    class RefundType(Enum):
        """
        :cvar AUTO:
        :cvar MANUAL:
        :cvar IGNORED:
        """
        AUTO = "Auto"
        MANUAL = "Manual"
        IGNORED = "Ignored"


@dataclass
class AirExchangeMultiQuoteOption:
    """The shared object list of AirExchangeMultiQuoteOptions.

    :ivar air_segment_data:
    :ivar air_exchange_bundle_total:
    :ivar air_exchange_bundle_list:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_data: List[AirSegmentData] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentData",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata=dict(
            name="AirExchangeBundleTotal",
            type="Element"
        )
    )
    air_exchange_bundle_list: List[AirExchangeBundleList] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundleList",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirMerchandisingOfferAvailabilityReq(BaseReq):
    """Check with the supplier whether or not the reservation or air solution
    supports any merchandising offerings.

    :ivar agency_sell_info: Provider: 1G,1V,1P,1J,ACH.
    :ivar air_solution: Provider: 1G,1V,1P,1J,ACH.
    :ivar host_reservation: Provider: 1G,1V,1P,1J,ACH.
    :ivar offer_availability_modifiers: Provider: 1G,1V,1P,1J,ACH.
    :ivar merchandising_pricing_modifiers: Used to provide additional pricing modifiers. Provider:ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    agency_sell_info: Optional[AgencySellInfo] = field(
        default=None,
        metadata=dict(
            name="AgencySellInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    air_solution: Optional[AirSolution] = field(
        default=None,
        metadata=dict(
            name="AirSolution",
            type="Element"
        )
    )
    host_reservation: List[HostReservation] = field(
        default_factory=list,
        metadata=dict(
            name="HostReservation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    offer_availability_modifiers: List[OfferAvailabilityModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="OfferAvailabilityModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    merchandising_pricing_modifiers: Optional[MerchandisingPricingModifiers] = field(
        default=None,
        metadata=dict(
            name="MerchandisingPricingModifiers",
            type="Element"
        )
    )


@dataclass
class AirMerchandisingOfferAvailabilityRsp(BaseRsp):
    """Contains the merchandising offerings for the given passenger and itinerary.

    :ivar air_solution: Provider: 1G,1V,1P,1J,ACH.
    :ivar remark: Provider: 1G,1V,1P,1J,ACH.
    :ivar optional_services:
    :ivar embargo_list:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_solution: Optional[AirSolution] = field(
        default=None,
        metadata=dict(
            name="AirSolution",
            type="Element",
            required=True
        )
    )
    remark: Optional[Remark] = field(
        default=None,
        metadata=dict(
            name="Remark",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    embargo_list: Optional[EmbargoList] = field(
        default=None,
        metadata=dict(
            name="EmbargoList",
            type="Element"
        )
    )


@dataclass
class AirPricingInfo:
    """Per traveler type pricing breakdown. This will reflect the pricing for all
    travelers of the specified type.

    :ivar fare_info:
    :ivar fare_status:
    :ivar fare_info_ref:
    :ivar booking_info:
    :ivar tax_info:
    :ivar fare_calc:
    :ivar passenger_type:
    :ivar booking_traveler_ref:
    :ivar waiver_code:
    :ivar payment_ref: The reference to the Payment if Air Pricing
                                is charged
    :ivar change_penalty: The penalty (if any) to change the itinerary
    :ivar cancel_penalty: The penalty (if any) to cancel the fare
    :ivar no_show_penalty: The NoShow penalty (if any)
    :ivar fee_info:
    :ivar adjustment:
    :ivar yield_value:
    :ivar air_pricing_modifiers:
    :ivar ticketing_modifiers_ref:
    :ivar air_segment_pricing_modifiers:
    :ivar flight_options_list:
    :ivar baggage_allowances:
    :ivar fare_rules_filter:
    :ivar policy_codes_list: A list of codes that indicate why an item was determined to be ‘out of policy’
    :ivar price_change: Indicates a price change is found in Fare Control Manager
    :ivar action_details:
    :ivar commission: Allows an agency to update the commission
                         to a new or different commission rate which will be applied at
                         time of ticketing. The commission Modifier allows the user
                         specify how the commission change is to applied
    :ivar origin: The IATA location code for this origination of this entity.
    :ivar destination: The IATA location code for this destination of this entity.
    :ivar key:
    :ivar command_key: The command identifier used when this is in
                            response to an AirPricingCommand. Not used in any request
                            processing.
    :ivar total_price: The total price for this entity including base price and all taxes.
    :ivar base_price: Represents the base price for this entity. This does not include any taxes or surcharges.
    :ivar approximate_total_price: The Converted total price in Default Currency for this entity including base price and all taxes.
    :ivar approximate_base_price: The Converted base price in Default Currency for this entity. This does not include any taxes or surcharges.
    :ivar equivalent_base_price: Represents the base price in the related currency for this entity. This does not include any taxes or surcharges.
    :ivar taxes: The aggregated amount of all the taxes that are associated with this entity. See the associated TaxInfo array for a breakdown of the individual taxes.
    :ivar fees: The aggregated amount of all the fees that are associated with this entity. See the associated FeeInfo array for a breakdown of the individual fees.
    :ivar services: The total cost for all optional services.
    :ivar approximate_taxes: The Converted tax amount in Default Currency.
    :ivar approximate_fees: The Converted fee amount in Default Currency.
    :ivar provider_code:
    :ivar supplier_code:
    :ivar amount_type: This field displays type of payment amount when it is non-monetary. Presently available/supported value is "Flight Pass Credits".
    :ivar includes_vat: Indicates whether the Base Price
                            includes VAT.
    :ivar exchange_amount: The amount to pay to cover the exchange of the
                            fare (includes penalties).
    :ivar forfeit_amount: The amount forfeited when the fare is
                            exchanged.
    :ivar refundable: Indicates whether the fare is refundable
    :ivar exchangeable: Indicates whether the fare is
                            exchangeable
    :ivar latest_ticketing_time: The latest date/time at which this pricing
                            information is valid
    :ivar pricing_method:
    :ivar checksum: A security value used to guarantee that the
                            pricing data sent in matches the pricing data previously returned
    :ivar eticketability: The E-Ticketability of this AirPricing
    :ivar plating_carrier: The Plating Carrier for this journey
    :ivar provider_reservation_info_ref: Provider reservation reference key.
    :ivar air_pricing_info_group: This attribute is added to support multiple
                            store fare in Host. All AirPricingInfo with same group number will
                            be stored together.
    :ivar total_net_price: The total price of a negotiated fare.
    :ivar ticketed: Indicates if the associated stored fare
                            is ticketed or not.
    :ivar pricing_type: Indicates the Pricing Type used.
                            The possible values are TicketRecord, StoredFare, PricingInstruction.
    :ivar true_last_date_to_ticket: This date indicates the true last date/time to ticket for the fare. This date comes from the filed fare . There is no guarantee the fare will still be available on that date or that the fare amount may change.
        It is merely the last date to purchase a ticket based on the carriers fare rules at the time the itinerary was quoted and stored
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    :ivar in_policy: This attribute will be used to indicate if a fare or rate has been determined to be ‘in policy’ based on the associated policy settings.
    :ivar preferred_option: This attribute is used to indicate if the vendors responsible for the fare or rate being returned have been determined to be ‘preferred’ based on the associated policy settings.
    :ivar fare_calculation_ind: Fare calculation that was used to price the itinerary.
    :ivar cat35_indicator: A true value indicates that the fare has a Cat35 rule.
                                    A false valud indicates that the fare does not have a Cat35 rule
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_info: List[FareInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FareInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_status: Optional[FareStatus] = field(
        default=None,
        metadata=dict(
            name="FareStatus",
            type="Element"
        )
    )
    fare_info_ref: List[FareInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="FareInfoRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_info: List[BookingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="BookingInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_calc: Optional[FareCalc] = field(
        default=None,
        metadata=dict(
            name="FareCalc",
            type="Element"
        )
    )
    passenger_type: List[PassengerType] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerType",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element"
        )
    )
    payment_ref: List[PaymentRef] = field(
        default_factory=list,
        metadata=dict(
            name="PaymentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    change_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata=dict(
            name="ChangePenalty",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    cancel_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata=dict(
            name="CancelPenalty",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    no_show_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata=dict(
            name="NoShowPenalty",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    adjustment: List[Adjustment] = field(
        default_factory=list,
        metadata=dict(
            name="Adjustment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    yield_value: List[YieldType] = field(
        default_factory=list,
        metadata=dict(
            name="Yield",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element"
        )
    )
    ticketing_modifiers_ref: List[TicketingModifiersRef] = field(
        default_factory=list,
        metadata=dict(
            name="TicketingModifiersRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentPricingModifiers",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    flight_options_list: Optional[FlightOptionsList] = field(
        default=None,
        metadata=dict(
            name="FlightOptionsList",
            type="Element"
        )
    )
    baggage_allowances: Optional[BaggageAllowances] = field(
        default=None,
        metadata=dict(
            name="BaggageAllowances",
            type="Element"
        )
    )
    fare_rules_filter: Optional[FareRulesFilter] = field(
        default=None,
        metadata=dict(
            name="FareRulesFilter",
            type="Element"
        )
    )
    policy_codes_list: Optional[PolicyCodesList] = field(
        default=None,
        metadata=dict(
            name="PolicyCodesList",
            type="Element"
        )
    )
    price_change: List[PriceChangeType] = field(
        default_factory=list,
        metadata=dict(
            name="PriceChange",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    action_details: Optional[ActionDetails] = field(
        default=None,
        metadata=dict(
            name="ActionDetails",
            type="Element"
        )
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata=dict(
            name="Commission",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    origin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    destination: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            length=3,
            white_space="collapse"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    command_key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CommandKey",
            type="Attribute",
            max_length=10
        )
    )
    total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute"
        )
    )
    base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute"
        )
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute"
        )
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateBasePrice",
            type="Attribute"
        )
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EquivalentBasePrice",
            type="Attribute"
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Attribute"
        )
    )
    services: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Services",
            type="Attribute"
        )
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTaxes",
            type="Attribute"
        )
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateFees",
            type="Attribute"
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            min_length=1,
            max_length=5
        )
    )
    amount_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AmountType",
            type="Attribute",
            min_length=1,
            max_length=32
        )
    )
    includes_vat: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IncludesVAT",
            type="Attribute"
        )
    )
    exchange_amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ExchangeAmount",
            type="Attribute"
        )
    )
    forfeit_amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ForfeitAmount",
            type="Attribute"
        )
    )
    refundable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute"
        )
    )
    exchangeable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Exchangeable",
            type="Attribute"
        )
    )
    latest_ticketing_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LatestTicketingTime",
            type="Attribute"
        )
    )
    pricing_method: Optional[TypePricingMethod] = field(
        default=None,
        metadata=dict(
            name="PricingMethod",
            type="Attribute",
            required=True
        )
    )
    checksum: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Checksum",
            type="Attribute"
        )
    )
    eticketability: Optional[TypeEticketability] = field(
        default=None,
        metadata=dict(
            name="ETicketability",
            type="Attribute"
        )
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            length=2
        )
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute"
        )
    )
    air_pricing_info_group: Optional[int] = field(
        default=None,
        metadata=dict(
            name="AirPricingInfoGroup",
            type="Attribute"
        )
    )
    total_net_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalNetPrice",
            type="Attribute"
        )
    )
    ticketed: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Ticketed",
            type="Attribute"
        )
    )
    pricing_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PricingType",
            type="Attribute",
            max_length=25
        )
    )
    true_last_date_to_ticket: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TrueLastDateToTicket",
            type="Attribute"
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )
    in_policy: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="InPolicy",
            type="Attribute"
        )
    )
    preferred_option: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="PreferredOption",
            type="Attribute"
        )
    )
    fare_calculation_ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareCalculationInd",
            type="Attribute",
            length=1
        )
    )
    cat35_indicator: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Cat35Indicator",
            type="Attribute"
        )
    )


@dataclass
class AirRefundQuoteRsp(BaseRsp):
    """
    :ivar air_refund_bundle:
    :ivar tcrrefund_bundle: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_refund_bundle: List[AirRefundBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirRefundBundle",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrrefund_bundle: List[TcrrefundBundle] = field(
        default_factory=list,
        metadata=dict(
            name="TCRRefundBundle",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirRefundReq(BaseReq):
    """Request to refund an itinerary for the amount previously quoted.

    :ivar air_refund_bundle: Provider: ACH.
    :ivar tcrrefund_bundle: Provider: ACH.
    :ivar air_refund_modifiers:
    :ivar commission: Provider: ACH.
    :ivar form_of_payment: Provider: ACH-Form of Payment for any Additional Collection charges for the Refund.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_refund_bundle: List[AirRefundBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirRefundBundle",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrrefund_bundle: List[TcrrefundBundle] = field(
        default_factory=list,
        metadata=dict(
            name="TCRRefundBundle",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_refund_modifiers: Optional[AirRefundModifiers] = field(
        default=None,
        metadata=dict(
            name="AirRefundModifiers",
            type="Element"
        )
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata=dict(
            name="Commission",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=9
        )
    )
    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )


@dataclass
class AirSearchReq(BaseSearchReq):
    """Base Request for Air Search.

    :ivar point_of_commencement:
    :ivar search_air_leg:
    :ivar search_specific_air_segment:
    :ivar air_search_modifiers:
    :ivar journey_data:
    """
    point_of_commencement: Optional[PointOfCommencement] = field(
        default=None,
        metadata=dict(
            name="PointOfCommencement",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    search_air_leg: List[SearchAirLeg] = field(
        default_factory=list,
        metadata=dict(
            name="SearchAirLeg",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=16
        )
    )
    search_specific_air_segment: List[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="SearchSpecificAirSegment",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_search_modifiers: Optional[AirSearchModifiers] = field(
        default=None,
        metadata=dict(
            name="AirSearchModifiers",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    journey_data: Optional[JourneyData] = field(
        default=None,
        metadata=dict(
            name="JourneyData",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )


@dataclass
class AirSegmentSellFailureInfo:
    """Container to return air segment sell failures.

    :ivar air_segment_error:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_error: List[AirSegmentError] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentError",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AvailabilityErrorInfo(TypeErrorInfo):
    """
    :ivar air_segment_error:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_error: List[AirSegmentError] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentError",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class BaseAirPriceReq(BaseCoreReq):
    """
    :ivar air_itinerary: Provider: 1G,1V,1P,1J,ACH.
    :ivar air_pricing_modifiers: Provider: 1G,1V,1P,1J,ACH.
    :ivar search_passenger: Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS 					passenger
    :ivar air_pricing_command: Provider: 1G,1V,1P,1J,ACH.
    :ivar air_reservation_locator_code: Provider: ACH,1P,1J
    :ivar optional_services: Provider: ACH.
    :ivar form_of_payment: Provider: 1G,1V,1P,1J,ACH.
    :ivar pcc:
    :ivar ssr: Special Service Request for GST tax details. Provider: ACH
    :ivar check_obfees: A flag to return fees for ticketing and for various forms of payment. The default is “TicketingOnly” and will return only ticketing fees.  The value “All” will return ticketing fees and the applicable form of payment fees for the form of payment information specified in the request.  “FOPOnly” will return the applicable form of payment fees for the form of payment information specified in the request. Form of payment fees are never included in the total unless specific card details are in the request.Provider notes:ACH - CheckOBFees is valid only for LowFareSearch.  The valid values are “All”, “TicketingOnly” and “None” and the default value is “None”. 1P/1J -The valid values are “All”, “None” and “TicketingOnly”.1G – All four values are supported.1V/RCH – CheckOBFees are not supported.”
    :ivar fare_rule_type: Provider: 1G,1V,1P,1J,ACH.
    :ivar supplier_code: Specifies the supplier/ vendor for vendor specific price requests
    :ivar ticket_date: YYYY-MM-DD Using a date in the past is a request for an historical fare
    :ivar check_flight_details: To Include FlightDetails in Response set to “true” the Default value is “false”.
    :ivar return_mm: If this attribute is set to “true”, Fare Control Manager processing will be invoked.
    :ivar nscc: 1 to 3 numeric that defines a Search Control Console filter.This attribute is used to override that filter.
    :ivar split_pricing: Indicates whether the AirSegments should be priced together or separately. Set ‘true’ for split pricing. Set ‘false’ for pricing together.SplitPricing is not supported with post book re-pricing.
    :ivar ignore_availability: Provides a method of pricing a book itinerary with the lowest fare regardless of the availability for the class of service. Only for providers 1P/1J.
    """
    air_itinerary: Optional[AirItinerary] = field(
        default=None,
        metadata=dict(
            name="AirItinerary",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            required=True
        )
    )
    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata=dict(
            name="SearchPassenger",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=18
        )
    )
    air_pricing_command: List[AirPricingCommand] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingCommand",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=1,
            max_occurs=16
        )
    )
    air_reservation_locator_code: Optional[AirReservationLocatorCode] = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    pcc: Optional[Pcc] = field(
        default=None,
        metadata=dict(
            name="PCC",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata=dict(
            name="SSR",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )
    check_obfees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CheckOBFees",
            type="Attribute"
        )
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE_VALUE,
        metadata=dict(
            name="FareRuleType",
            type="Attribute"
        )
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            min_length=1,
            max_length=5
        )
    )
    ticket_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketDate",
            type="Attribute"
        )
    )
    check_flight_details: bool = field(
        default=False,
        metadata=dict(
            name="CheckFlightDetails",
            type="Attribute"
        )
    )
    return_mm: bool = field(
        default=False,
        metadata=dict(
            name="ReturnMM",
            type="Attribute"
        )
    )
    nscc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            min_length=1,
            max_length=3
        )
    )
    split_pricing: bool = field(
        default=False,
        metadata=dict(
            name="SplitPricing",
            type="Attribute"
        )
    )
    ignore_availability: bool = field(
        default=False,
        metadata=dict(
            name="IgnoreAvailability",
            type="Attribute"
        )
    )


@dataclass
class BaseAirSearchReq(BaseCoreSearchReq):
    """Base Request for Low fare air Search.

    :ivar search_air_leg:
    :ivar search_specific_air_segment:
    :ivar air_search_modifiers:
    :ivar split_ticketing_search:
    :ivar journey_data:
    """
    search_air_leg: List[SearchAirLeg] = field(
        default_factory=list,
        metadata=dict(
            name="SearchAirLeg",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=9
        )
    )
    search_specific_air_segment: List[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="SearchSpecificAirSegment",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_search_modifiers: Optional[AirSearchModifiers] = field(
        default=None,
        metadata=dict(
            name="AirSearchModifiers",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    split_ticketing_search: Optional[SplitTicketingSearch] = field(
        default=None,
        metadata=dict(
            name="SplitTicketingSearch",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    journey_data: Optional[JourneyData] = field(
        default=None,
        metadata=dict(
            name="JourneyData",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )


@dataclass
class FareInfoList:
    """The shared object list of FareInfos.

    :ivar fare_info:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    fare_info: List[FareInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FareInfo",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeMulitQuoteList:
    """The shared object list of AirExchangeMultiQuotes.

    :ivar air_exchange_multi_quote_option:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_exchange_multi_quote_option: List[AirExchangeMultiQuoteOption] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeMultiQuoteOption",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirPricePoint:
    """The container which holds the Non Solutioned result.

    :ivar air_pricing_info:
    :ivar air_pricing_result_message:
    :ivar fee_info: Supported by ACH only
    :ivar fare_note:
    :ivar tax_info: Itinerary level taxes
    :ivar key:
    :ivar total_price: The total price for this entity including base price and all taxes.
    :ivar base_price: Represents the base price for this entity. This does not include any taxes or surcharges.
    :ivar approximate_total_price: The Converted total price in Default Currency for this entity including base price and all taxes.
    :ivar approximate_base_price: The Converted base price in Default Currency for this entity. This does not include any taxes or surcharges.
    :ivar equivalent_base_price: Represents the base price in the related currency for this entity. This does not include any taxes or surcharges.
    :ivar taxes: The aggregated amount of all the taxes that are associated with this entity. See the associated TaxInfo array for a breakdown of the individual taxes.
    :ivar fees: The aggregated amount of all the fees that are associated with this entity. See the associated FeeInfo array for a breakdown of the individual fees.
    :ivar services: The total cost for all optional services.
    :ivar approximate_taxes: The Converted tax amount in Default Currency.
    :ivar approximate_fees: The Converted fee amount in Default Currency.
    :ivar complete_itinerary: This attribute is used to return whether complete Itinerary is present in the AirPricePoint structure or not. If set to true means AirPricePoint contains the result for full requested itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingResultMessage",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata=dict(
            name="FareNote",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute"
        )
    )
    base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute"
        )
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute"
        )
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateBasePrice",
            type="Attribute"
        )
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EquivalentBasePrice",
            type="Attribute"
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Attribute"
        )
    )
    services: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Services",
            type="Attribute"
        )
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTaxes",
            type="Attribute"
        )
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateFees",
            type="Attribute"
        )
    )
    complete_itinerary: bool = field(
        default=True,
        metadata=dict(
            name="CompleteItinerary",
            type="Attribute"
        )
    )


@dataclass
class AirPriceReq(BaseAirPriceReq):
    """Request to price an itinerary in one to many ways.

    Pricing commands can be specified globally, or specifically per command.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AirPricingInfoList:
    """The shared object list of AirSegments.

    :ivar air_pricing_info:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirPricingSolution:
    """The pricing container for an air travel itinerary.

    :ivar air_segment:
    :ivar air_segment_ref:
    :ivar journey:
    :ivar leg_ref:
    :ivar air_pricing_info:
    :ivar fare_note:
    :ivar fare_note_ref:
    :ivar connection:
    :ivar meta_data:
    :ivar air_pricing_result_message:
    :ivar fee_info:
    :ivar tax_info: Itinerary level taxes
    :ivar air_itinerary_solution_ref:
    :ivar host_token:
    :ivar optional_services:
    :ivar available_ssr:
    :ivar pricing_details:
    :ivar key:
    :ivar complete_itinerary: This attribute is used to return whether complete Itinerary is present in the AirPricingSolution structure or not. If set to true means AirPricingSolution contains the result for full requested itinerary.
    :ivar quote_date: This date will be equal to the date of the transaction unless the request included a modified ticket date.
    :ivar total_price: The total price for this entity including base price and all taxes.
    :ivar base_price: Represents the base price for this entity. This does not include any taxes or surcharges.
    :ivar approximate_total_price: The Converted total price in Default Currency for this entity including base price and all taxes.
    :ivar approximate_base_price: The Converted base price in Default Currency for this entity. This does not include any taxes or surcharges.
    :ivar equivalent_base_price: Represents the base price in the related currency for this entity. This does not include any taxes or surcharges.
    :ivar taxes: The aggregated amount of all the taxes that are associated with this entity. See the associated TaxInfo array for a breakdown of the individual taxes.
    :ivar fees: The aggregated amount of all the fees that are associated with this entity. See the associated FeeInfo array for a breakdown of the individual fees.
    :ivar services: The total cost for all optional services.
    :ivar approximate_taxes: The Converted tax amount in Default Currency.
    :ivar approximate_fees: The Converted fee amount in Default Currency.
    :ivar itinerary: For an exchange request this tells if the itinerary is the original one or new one. A value of Original will only apply to 1G/1V/1P/1S/1A. A value of New will apply to 1G/1V/1P/1S/1A/ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    journey: List[Journey] = field(
        default_factory=list,
        metadata=dict(
            name="Journey",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    leg_ref: List[LegRef] = field(
        default_factory=list,
        metadata=dict(
            name="LegRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata=dict(
            name="FareNote",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_note_ref: List[FareNoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="FareNoteRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata=dict(
            name="Connection",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    meta_data: List[MetaData] = field(
        default_factory=list,
        metadata=dict(
            name="MetaData",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingResultMessage",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_itinerary_solution_ref: List[AirItinerarySolutionRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirItinerarySolutionRef",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    available_ssr: Optional[AvailableSsr] = field(
        default=None,
        metadata=dict(
            name="AvailableSSR",
            type="Element"
        )
    )
    pricing_details: Optional[PricingDetails] = field(
        default=None,
        metadata=dict(
            name="PricingDetails",
            type="Element"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            required=True
        )
    )
    complete_itinerary: bool = field(
        default=True,
        metadata=dict(
            name="CompleteItinerary",
            type="Attribute"
        )
    )
    quote_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="QuoteDate",
            type="Attribute"
        )
    )
    total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute"
        )
    )
    base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute"
        )
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute"
        )
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateBasePrice",
            type="Attribute"
        )
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EquivalentBasePrice",
            type="Attribute"
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Attribute"
        )
    )
    services: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Services",
            type="Attribute"
        )
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTaxes",
            type="Attribute"
        )
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateFees",
            type="Attribute"
        )
    )
    itinerary: Optional["AirPricingSolution.Itinerary"] = field(
        default=None,
        metadata=dict(
            name="Itinerary",
            type="Attribute"
        )
    )

    class Itinerary(Enum):
        """
        :cvar NEW:
        :cvar ORIGINAL:
        """
        NEW = "New"
        ORIGINAL = "Original"


@dataclass
class AvailabilitySearchReq(AirSearchReq):
    """Availability Search request.

    :ivar search_passenger: Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS                                                passenger
    :ivar point_of_sale: Provider: ACH.
    :ivar return_brand_indicator: When set to “true”, the Brand Indicator can be returned in the availability search response. Provider: 1G, 1V, 1P, 1J, ACH
    :ivar channel_id: A Channel ID is 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.
    :ivar nscc: Allows the agency to bypass/override the Search Control Console rule.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata=dict(
            name="SearchPassenger",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=18
        )
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=5
        )
    )
    return_brand_indicator: bool = field(
        default=False,
        metadata=dict(
            name="ReturnBrandIndicator",
            type="Attribute"
        )
    )
    channel_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ChannelId",
            type="Attribute",
            min_length=2,
            max_length=4
        )
    )
    nscc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            min_length=1,
            max_length=3
        )
    )


@dataclass
class BaseAvailabilitySearchRsp(BaseSearchRsp):
    """Availability Search response.

    :ivar flight_details_list:
    :ivar air_segment_list:
    :ivar fare_info_list:
    :ivar fare_remark_list:
    :ivar air_itinerary_solution:
    :ivar host_token_list:
    :ivar apisrequirements_list:
    :ivar distance_units:
    """
    flight_details_list: Optional[FlightDetailsList] = field(
        default=None,
        metadata=dict(
            name="FlightDetailsList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    air_segment_list: Optional[AirSegmentList] = field(
        default=None,
        metadata=dict(
            name="AirSegmentList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    fare_info_list: Optional[FareInfoList] = field(
        default=None,
        metadata=dict(
            name="FareInfoList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    fare_remark_list: Optional[FareRemarkList] = field(
        default=None,
        metadata=dict(
            name="FareRemarkList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    air_itinerary_solution: List[AirItinerarySolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirItinerarySolution",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token_list: Optional[HostTokenList] = field(
        default=None,
        metadata=dict(
            name="HostTokenList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    apisrequirements_list: Optional[ApisrequirementsList] = field(
        default=None,
        metadata=dict(
            name="APISRequirementsList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    distance_units: Optional[TypeDistance] = field(
        default=None,
        metadata=dict(
            name="DistanceUnits",
            type="Attribute"
        )
    )


@dataclass
class BaseLowFareSearchReq(BaseAirSearchReq):
    """Base Low Fare Search Request.

    :ivar search_passenger: Provider: 1G,1V,1P,1J,ACH-Maxinumber of passenger increased in to 18 to support 9 INF passenger along with 9 ADT,CHD,INS                                        passenger
    :ivar air_pricing_modifiers: Provider: 1G,1V,1P,1J,ACH.
    :ivar enumeration: Provider: 1G,1V,1P,1J,ACH.
    :ivar air_exchange_modifiers: Provider: ACH.
    :ivar flex_explore_modifiers: This is the container for a set of modifiers which allow the user to perform a special kind of low fare search, depicted as flex explore, based on different parameters like Area, Zone, Country, State, Specific locations, Distance around the actual destination of the itinerary. Applicable for providers 1G,1V,1P.
    :ivar pcc:
    :ivar fare_rules_filter_category:
    :ivar form_of_payment: Provider: 1P,1J
    :ivar enable_point_to_point_search: Provider: 1G,1V,1P,1J,ACH-Indicates that low cost providers should be queried for top connection options and the results returned with the search.
    :ivar enable_point_to_point_alternates: Provider: 1G,1V,1P,1J,ACH-Indicates that suggestions for alternate connection cities for low cost providers should be returned with the search.
    :ivar max_number_of_expert_solutions: Provider: 1G,1V,1P,1J,ACH-Indicates the Maximum Number of Expert Solutions to be returned from the Knowledge Base for the provided search criteria
    :ivar solution_result: Provider: 1G,1V,1P,1J,ACH-Indicates whether the response will contain Solution result (AirPricingSolution) or Non Solution Result (AirPricingPoints). The default value is false. This attribute cannot be combined with EnablePointToPointSearch, EnablePointToPointAlternates and MaxNumberOfExpertSolutions.
    :ivar prefer_complete_itinerary: Provider: ACH-This attribute is only supported for ACH .It works in conjunction with the @SolutionResult flag
    :ivar meta_option_identifier: Invoke Meta Search.  Valid values are 00 to 99, or D for the default meta search configuration.  When Meta Search not requested, normal LowFareSearch applies.  Supported Providers;  1g/1v/1p/1j
    :ivar return_upsell_fare: When set to “true”, Upsell information will be returned in the shop response. Provider supported : 1G, 1V, 1P, 1J
    :ivar include_fare_info_messages: Set to True to return FareInfoMessageList. Providers supported: 1G/1V/1P/1J
    :ivar return_branded_fares: When ReturnBrandedFares is set to “false”, Rich Content and Branding will not be returned in the shop response.  When ReturnBrandedFares it is set to “true” or is not sent, Rich Content and Branding will be returned in the shop response.  Provider: 1P/1J/ACH.
    :ivar multi_gdssearch: A "true" value indicates MultiGDSSearch. Specific provisioning is required.
    :ivar return_mm: If this attribute is set to “true”, Fare Control Manager processing will be invoked.
    :ivar check_obfees: A flag to return fees for ticketing and for various forms of payment. The default is “TicketingOnly” and will return only ticketing fees.  The value “All” will return ticketing fees and the applicable form of payment fees for the form of payment information specified in the request.  “FOPOnly” will return the applicable form of payment fees for the form of payment information specified in the request. Form of payment fees are never included in the total unless specific card details are in the request.Provider notes:ACH - CheckOBFees is valid only for LowFareSearch.  The valid values are “All”, “TicketingOnly” and “None” and the default value is “None”. 1P/1J -The valid values are “All”, “None” and “TicketingOnly”.1G – All four values are supported.1V/RCH – CheckOBFees are not supported.”
    :ivar nscc: 1 to 3 numeric that defines a Search Control Console filter.This attribute is used to override that filter.
    :ivar fare_info_rules: Returns ChangePenalty and CancelPenalty values at the FareInfo level. If FareRulesFilterCategory is sent FareRulesFilter will be returned at FareInfo level.  Provider: 1G/1V.
    """
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata=dict(
            name="SearchPassenger",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=18
        )
    )
    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    enumeration: Optional[Enumeration] = field(
        default=None,
        metadata=dict(
            name="Enumeration",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    air_exchange_modifiers: Optional[AirExchangeModifiers] = field(
        default=None,
        metadata=dict(
            name="AirExchangeModifiers",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    flex_explore_modifiers: Optional[FlexExploreModifiers] = field(
        default=None,
        metadata=dict(
            name="FlexExploreModifiers",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    pcc: Optional[Pcc] = field(
        default=None,
        metadata=dict(
            name="PCC",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    fare_rules_filter_category: Optional[FareRulesFilterCategory] = field(
        default=None,
        metadata=dict(
            name="FareRulesFilterCategory",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )
    enable_point_to_point_search: bool = field(
        default=False,
        metadata=dict(
            name="EnablePointToPointSearch",
            type="Attribute"
        )
    )
    enable_point_to_point_alternates: bool = field(
        default=False,
        metadata=dict(
            name="EnablePointToPointAlternates",
            type="Attribute"
        )
    )
    max_number_of_expert_solutions: int = field(
        default=0,
        metadata=dict(
            name="MaxNumberOfExpertSolutions",
            type="Attribute"
        )
    )
    solution_result: bool = field(
        default=False,
        metadata=dict(
            name="SolutionResult",
            type="Attribute"
        )
    )
    prefer_complete_itinerary: bool = field(
        default=True,
        metadata=dict(
            name="PreferCompleteItinerary",
            type="Attribute"
        )
    )
    meta_option_identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MetaOptionIdentifier",
            type="Attribute",
            min_length=1,
            max_length=2
        )
    )
    return_upsell_fare: bool = field(
        default=False,
        metadata=dict(
            name="ReturnUpsellFare",
            type="Attribute"
        )
    )
    include_fare_info_messages: bool = field(
        default=False,
        metadata=dict(
            name="IncludeFareInfoMessages",
            type="Attribute"
        )
    )
    return_branded_fares: bool = field(
        default=True,
        metadata=dict(
            name="ReturnBrandedFares",
            type="Attribute"
        )
    )
    multi_gdssearch: bool = field(
        default=False,
        metadata=dict(
            name="MultiGDSSearch",
            type="Attribute"
        )
    )
    return_mm: bool = field(
        default=False,
        metadata=dict(
            name="ReturnMM",
            type="Attribute"
        )
    )
    check_obfees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CheckOBFees",
            type="Attribute"
        )
    )
    nscc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NSCC",
            type="Attribute",
            min_length=1,
            max_length=3
        )
    )
    fare_info_rules: bool = field(
        default=False,
        metadata=dict(
            name="FareInfoRules",
            type="Attribute"
        )
    )


@dataclass
class Etr:
    """Result of ticketing request.

    :ivar air_reservation_locator_code:
    :ivar agency_info:
    :ivar booking_traveler:
    :ivar form_of_payment:
    :ivar payment:
    :ivar credit_card_auth: This is a container to display detail information of credit card auth. Providers supported: Worldspan and JAL.
    :ivar supplier_locator:
    :ivar fare_calc:
    :ivar ticket:
    :ivar commission:
    :ivar air_pricing_info:
    :ivar audit_data:
    :ivar restriction:
    :ivar waiver_code:
    :ivar baggage_allowances: Baggage Allowance Info after Ticketing
    :ivar key:
    :ivar total_price: The total price for this entity including base price and all taxes.
    :ivar base_price: Represents the base price for this entity. This does not include any taxes or surcharges.
    :ivar approximate_total_price: The Converted total price in Default Currency for this entity including base price and all taxes.
    :ivar approximate_base_price: The Converted base price in Default Currency for this entity. This does not include any taxes or surcharges.
    :ivar equivalent_base_price: Represents the base price in the related currency for this entity. This does not include any taxes or surcharges.
    :ivar taxes: The aggregated amount of all the taxes that are associated with this entity. See the associated TaxInfo array for a breakdown of the individual taxes.
    :ivar fees: The aggregated amount of all the fees that are associated with this entity. See the associated FeeInfo array for a breakdown of the individual fees.
    :ivar services: The total cost for all optional services.
    :ivar approximate_taxes: The Converted tax amount in Default Currency.
    :ivar approximate_fees: The Converted fee amount in Default Currency.
    :ivar refundable:
    :ivar exchangeable:
    :ivar tour_code:
    :ivar issued_date: Ticket issue date.
    :ivar bulk_ticket: Whether the ticket was issued as bulk.
    :ivar provider_code: Contains the Provider Code of the provider that houses this ETR.
    :ivar provider_locator_code: Contains the Locator Code of the Provider Reservation that houses this ETR.
    :ivar iatanumber: Contains the IATA Number of the agent initiating the request.
    :ivar pseudo_city_code: Contain Pseudo City, city/office number, branch ID, etc.
    :ivar country_code: Contains Ticketed PCC’s Country code.
    :ivar plating_carrier: Contains the Plating Carrier of this ETR.
    :ivar el_stat: This attribute is used to show the action results of an element.
                  Possible values are "A" (when elements have been added to the UR) and "M" (when existing elements have been modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding elements in some cases like URAdd, then instead of erroring out set this attribute to true.
    """
    class Meta:
        name = "ETR"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[AirReservationLocatorCode] = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element"
        )
    )
    agency_info: Optional[AgencyInfo] = field(
        default=None,
        metadata=dict(
            name="AgencyInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    booking_traveler: Optional[BookingTraveler] = field(
        default=None,
        metadata=dict(
            name="BookingTraveler",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            required=True
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata=dict(
            name="CreditCardAuth",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_calc: Optional[FareCalc] = field(
        default=None,
        metadata=dict(
            name="FareCalc",
            type="Element",
            required=True
        )
    )
    ticket: List[Ticket] = field(
        default_factory=list,
        metadata=dict(
            name="Ticket",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata=dict(
            name="Commission",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_info: Optional[AirPricingInfo] = field(
        default=None,
        metadata=dict(
            name="AirPricingInfo",
            type="Element"
        )
    )
    audit_data: Optional[AuditData] = field(
        default=None,
        metadata=dict(
            name="AuditData",
            type="Element"
        )
    )
    restriction: List[CommonRestriction] = field(
        default_factory=list,
        metadata=dict(
            name="Restriction",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element"
        )
    )
    baggage_allowances: Optional[BaggageAllowances] = field(
        default=None,
        metadata=dict(
            name="BaggageAllowances",
            type="Element"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute"
        )
    )
    total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute"
        )
    )
    base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute"
        )
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute"
        )
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateBasePrice",
            type="Attribute"
        )
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EquivalentBasePrice",
            type="Attribute"
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute"
        )
    )
    fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Attribute"
        )
    )
    services: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Services",
            type="Attribute"
        )
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateTaxes",
            type="Attribute"
        )
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ApproximateFees",
            type="Attribute"
        )
    )
    refundable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute"
        )
    )
    exchangeable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Exchangeable",
            type="Attribute"
        )
    )
    tour_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Attribute",
            max_length=15
        )
    )
    issued_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IssuedDate",
            type="Attribute",
            required=True
        )
    )
    bulk_ticket: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="BulkTicket",
            type="Attribute"
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            min_length=2,
            max_length=5
        )
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            max_length=15
        )
    )
    iatanumber: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IATANumber",
            type="Attribute",
            max_length=8
        )
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            min_length=2,
            max_length=10
        )
    )
    country_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Attribute",
            length=2
        )
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            length=2
        )
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata=dict(
            name="ElStat",
            type="Attribute"
        )
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="KeyOverride",
            type="Attribute"
        )
    )


@dataclass
class ScheduleSearchReq(AirSearchReq):
    """Schedule Search request."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class Tcr:
    """Information related to Ticketless carriers.

    :ivar form_of_payment:
    :ivar payment:
    :ivar booking_traveler:
    :ivar passenger_ticket_number:
    :ivar air_pricing_info:
    :ivar agency_info:
    :ivar air_reservation_locator_code:
    :ivar supplier_locator:
    :ivar refund_remark:
    :ivar tcrnumber: The identifying number for a Ticketless Air
                            Reservation.
    :ivar status: The current status of this TCR. Some status
                            values are not applicable by some Airlines.
    :ivar modified_date: The date at which the status was changed on
                            this TCR due to an action event (itemized from the booleans
                            below).
    :ivar confirmed_date: The date at which this TCR was confirmed (not
                            created). This mean the payment was approved and processed and
                            travel for this TCR is confirmed.
    :ivar base_price: The base price of this TCR as a whole as it
                            was when it was first booked.
    :ivar taxes: The taxes of this TCR as a whole as it was
                            when it was first booked.
    :ivar fees: The fees of this TCR as a whole as it was when
                            it was first booked.
    :ivar refundable: Is it possible to perform a Refund for this
                            TCR.
    :ivar exchangeable: Is it possible to perform an Exchange for this
                            TCR.
    :ivar voidable: Is it possible to perform a Void on this TCR.
    :ivar modifiable: Is it possible to modify this TCR (opposed to
                            Refund/Exchange/Void).
    :ivar provider_code:
    :ivar provider_locator_code:
    :ivar refund_access_code:
    :ivar refund_amount: Total Amount refunded to the customer.
    :ivar refund_fee: Charges incurred for processing refund.
    :ivar forfeit_amount: Amount forfeited as a result of refund.
    """
    class Meta:
        name = "TCR"
        namespace = "http://www.travelport.com/schema/air_v48_0"

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTraveler",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=1,
            max_occurs=999
        )
    )
    passenger_ticket_number: List[PassengerTicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerTicketNumber",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    agency_info: Optional[AgencyInfo] = field(
        default=None,
        metadata=dict(
            name="AgencyInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    air_reservation_locator_code: Optional[AirReservationLocatorCode] = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element"
        )
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    refund_remark: List[RefundRemark] = field(
        default_factory=list,
        metadata=dict(
            name="RefundRemark",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Attribute",
            required=True
        )
    )
    status: Optional[TypeTcrstatus] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            required=True
        )
    )
    modified_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ModifiedDate",
            type="Attribute",
            required=True
        )
    )
    confirmed_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ConfirmedDate",
            type="Attribute"
        )
    )
    base_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute",
            required=True
        )
    )
    taxes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute",
            required=True
        )
    )
    fees: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Attribute",
            required=True
        )
    )
    refundable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute",
            required=True
        )
    )
    exchangeable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Exchangeable",
            type="Attribute",
            required=True
        )
    )
    voidable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Voidable",
            type="Attribute",
            required=True
        )
    )
    modifiable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Modifiable",
            type="Attribute",
            required=True
        )
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            required=True,
            min_length=2,
            max_length=5
        )
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            required=True,
            max_length=15
        )
    )
    refund_access_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RefundAccessCode",
            type="Attribute",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_length=1,
            max_length=32
        )
    )
    refund_amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RefundAmount",
            type="Attribute"
        )
    )
    refund_fee: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RefundFee",
            type="Attribute"
        )
    )
    forfeit_amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ForfeitAmount",
            type="Attribute"
        )
    )


@dataclass
class TypeBaseAirReservation(BaseReservation):
    """Parent Container for Air Reservation.

    :ivar optional_services:
    :ivar supplier_locator:
    :ivar third_party_information:
    :ivar document_info:
    :ivar booking_traveler_ref:
    :ivar provider_reservation_info_ref:
    :ivar air_segment:
    :ivar svc_segment: Service segment added to collect additional fee. 1P only
    :ivar air_pricing_info:
    :ivar payment:
    :ivar credit_card_auth:
    :ivar fare_note:
    :ivar fee_info:
    :ivar tax_info: Itinerary level taxes
    :ivar ticketing_modifiers:
    :ivar associated_remark:
    :ivar pocket_itinerary_remark:
    :ivar air_exchange_bundle_total:
    :ivar air_exchange_bundle: Bundle exchange, pricing, and penalty information. Providers ACH/1G/1V/1P
    """
    class Meta:
        name = "typeBaseAirReservation"

    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    third_party_information: List[ThirdPartyInformation] = field(
        default_factory=list,
        metadata=dict(
            name="ThirdPartyInformation",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    document_info: Optional[DocumentInfo] = field(
        default=None,
        metadata=dict(
            name="DocumentInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    svc_segment: List[SvcSegment] = field(
        default_factory=list,
        metadata=dict(
            name="SvcSegment",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata=dict(
            name="CreditCardAuth",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata=dict(
            name="FareNote",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TypeTaxInfoWithPaymentRef] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticketing_modifiers: List[TicketingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="TicketingModifiers",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    associated_remark: List[AssociatedRemark] = field(
        default_factory=list,
        metadata=dict(
            name="AssociatedRemark",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    pocket_itinerary_remark: List[PocketItineraryRemark] = field(
        default_factory=list,
        metadata=dict(
            name="PocketItineraryRemark",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata=dict(
            name="AirExchangeBundleTotal",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundle",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeMultiQuoteRsp(BaseRsp):
    """
    :ivar air_segment_list:
    :ivar brand_list:
    :ivar air_exchange_mulit_quote_list:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_segment_list: List[AirSegmentList] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentList",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    brand_list: List[BrandList] = field(
        default_factory=list,
        metadata=dict(
            name="BrandList",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_exchange_mulit_quote_list: List[AirExchangeMulitQuoteList] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeMulitQuoteList",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeQuoteRsp(BaseRsp):
    """
    :ivar ticket_number:
    :ivar air_pricing_solution: Provider: 1G/1V/1P/1S/1A.
    :ivar air_exchange_bundle_total:
    :ivar air_exchange_bundle: Bundle exchange, pricing, and penalty information. Providers ACH/1G/1V/1P
    :ivar host_token: Encrypted data from the host. Required to send the HostToken from the AirExchangeQuoteRsp in the AirExchangeReq. Providers ACH/1G/1V/1P.
    :ivar optional_services: Provider: ACH.
    :ivar fare_rule: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata=dict(
            name="AirExchangeBundleTotal",
            type="Element"
        )
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundle",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeReq(BaseReq):
    """Request to exchange an itinerary.

    :ivar air_reservation_locator_code: Identifies the PNR locator code. Providers ACH/1G/1V/1P
    :ivar ticket_number:
    :ivar specific_seat_assignment: Identifies the standard seat. Providers ACH/1G/1V/1P
    :ivar air_pricing_solution: Providers ACH/1G/1V/1P.
    :ivar air_exchange_modifiers: Provider: ACH.
    :ivar air_exchange_bundle_total: Provider: 1G/1V/1P/1S/1A.
    :ivar air_exchange_bundle: Bundle exchange, pricing, and penalty information. Providers ACH/1G/1V/1P.
    :ivar host_token: Encrypted data from the host. Required to send the HostToken from the AirExchangeQuoteRsp in the AirExchangeReq. Providers ACH/1G/1V/1P
    :ivar optional_services: Provider: ACH.
    :ivar form_of_payment: Form of Payment for any additional collection charges for the Exchange. For ACH, most carriers will only allow refund amounts to the original form of payment. Providers ACH/1G/1V/1P
    :ivar form_of_payment_ref: Provider: ACH-Universal Record reference to Form of Payment for any Additional Collection charges or Refund due for the itinerary exchange
    :ivar ssrinfo: Providers ACH, 1G, 1V, 1P.
    :ivar add_svc: 1P - Add SVC segments to collect additional fee
    :ivar return_reservation: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[AirReservationLocatorCode] = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            required=True
        )
    )
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    specific_seat_assignment: List[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata=dict(
            name="SpecificSeatAssignment",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )
    air_exchange_modifiers: Optional[AirExchangeModifiers] = field(
        default=None,
        metadata=dict(
            name="AirExchangeModifiers",
            type="Element"
        )
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata=dict(
            name="AirExchangeBundleTotal",
            type="Element"
        )
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundle",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element"
        )
    )
    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    ssrinfo: List[Ssrinfo] = field(
        default_factory=list,
        metadata=dict(
            name="SSRInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    add_svc: Optional[AddSvc] = field(
        default=None,
        metadata=dict(
            name="AddSvc",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )
    return_reservation: bool = field(
        default=False,
        metadata=dict(
            name="ReturnReservation",
            type="Attribute"
        )
    )


@dataclass
class AirPricePointList:
    """Provides the list of AirPricePoint (Non Solutioned Result)

    :ivar air_price_point: The container which holds the Non Solutioned result. Different options for each search leg requested will be returned and one option for each search leg can be selected.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_price_point: List[AirPricePoint] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricePoint",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirPriceResult:
    """A solution will be returned if one exists. Otherwise an error will be
    present.

    :ivar air_pricing_solution:
    :ivar fare_rule:
    :ivar air_price_error:
    :ivar command_key: The command identifier used when this is in
                            response to an AirPricingCommand. Not used in any request
                            processing.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_price_error: Optional[TypeResultMessage] = field(
        default=None,
        metadata=dict(
            name="AirPriceError",
            type="Element"
        )
    )
    command_key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CommandKey",
            type="Attribute",
            max_length=10
        )
    )


@dataclass
class AirRefundRsp(BaseRsp):
    """
    :ivar etr: Provider: ACH.
    :ivar tcr: Provider: ACH.
    :ivar refund_failure_info: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    etr: List[Etr] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcr: List[Tcr] = field(
        default_factory=list,
        metadata=dict(
            name="TCR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    refund_failure_info: List[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata=dict(
            name="RefundFailureInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirRepriceReq(AirBaseReq):
    """Request to reprice a solution.

    :ivar air_reservation_locator_code:
    :ivar air_pricing_solution:
    :ivar fare_rule_type:
    :ivar ignore_availability:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_reservation_locator_code: Optional[AirReservationLocatorCode] = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element"
        )
    )
    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            required=True
        )
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE_VALUE,
        metadata=dict(
            name="FareRuleType",
            type="Attribute"
        )
    )
    ignore_availability: bool = field(
        default=False,
        metadata=dict(
            name="IgnoreAvailability",
            type="Attribute"
        )
    )


@dataclass
class AirRepriceRsp(BaseRsp):
    """
    :ivar air_pricing_solution:
    :ivar fare_rule:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            required=True
        )
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirReservation(TypeBaseAirReservation):
    """The parent container for all booking data."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AirRetrieveDocumentRsp(BaseRsp):
    """
    :ivar etr: Provider: 1G,1V,1P,1J.
    :ivar mco: Provider: 1G,1V,1P,1J.
    :ivar tcr: Provider: 1G,1V,1P,1J.
    :ivar document_failure_info: Provider: 1G,1V,1P,1J-Will be optionally returned if there are duplicate ticket numbers.
    :ivar service_fee_info: Provider: 1G,1V
    :ivar universal_record_locator_code: Provider: 1G,1V,1P,1J-Represents a valid Universal Record locator code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    etr: List[Etr] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    mco: List[Mco] = field(
        default_factory=list,
        metadata=dict(
            name="MCO",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcr: List[Tcr] = field(
        default_factory=list,
        metadata=dict(
            name="TCR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    document_failure_info: List[TypeFailureInfo] = field(
        default_factory=list,
        metadata=dict(
            name="DocumentFailureInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    service_fee_info: List[ServiceFeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceFeeInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            min_length=5,
            max_length=8
        )
    )


@dataclass
class AirScheduleChangedInfo:
    """Returned when the requested schedule does not match the host system schedule
    Contents will be a new AirPricingSolution that contains all the new schedule
    information as well as the pricing information.

    :ivar air_pricing_solution:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            required=True
        )
    )


@dataclass
class AirSolutionChangedInfo:
    """If RetainReservation is None, this will contain the new values returned from
    the provider. If RetainReservation is Price, Schedule, or Both and there is a
    price/schedule change, this will contain the new values that were returned from
    the provider. If RetainReservation is Price, Schedule, or Both and there isn’t
    a price/schedule change, this element will not be returned.

    :ivar air_pricing_solution:
    :ivar reason_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            required=True
        )
    )
    reason_code: Optional["AirSolutionChangedInfo.ReasonCode"] = field(
        default=None,
        metadata=dict(
            name="ReasonCode",
            type="Attribute",
            required=True
        )
    )

    class ReasonCode(Enum):
        """
        :cvar PRICE:
        :cvar SCHEDULE:
        :cvar BOTH:
        """
        PRICE = "Price"
        SCHEDULE = "Schedule"
        BOTH = "Both"


@dataclass
class AirVoidDocumentRsp(BaseRsp):
    """Result of void ticket request. Includes ticket number of voided tickets and
    air segments with updated status.

    :ivar etr: Provider: 1G,1V.
    :ivar void_result_info: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    etr: List[Etr] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    void_result_info: List[VoidResultInfo] = field(
        default_factory=list,
        metadata=dict(
            name="VoidResultInfo",
            type="Element",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AvailabilitySearchRsp(BaseAvailabilitySearchRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class BaseAirExchangeMultiQuoteReq(BaseCoreReq):
    """
    :ivar ticket_number:
    :ivar provider_reservation_info: Provider: 1P - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged
    :ivar air_pricing_solution:
    :ivar repricing_modifiers:
    :ivar original_itinerary_details:
    :ivar override_pcc:
    """
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info: Optional["BaseAirExchangeMultiQuoteReq.ProviderReservationInfo"] = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=2
        )
    )
    repricing_modifiers: Optional[RepricingModifiers] = field(
        default=None,
        metadata=dict(
            name="RepricingModifiers",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    original_itinerary_details: Optional[OriginalItineraryDetails] = field(
        default=None,
        metadata=dict(
            name="OriginalItineraryDetails",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    override_pcc: Optional[OverridePcc] = field(
        default=None,
        metadata=dict(
            name="OverridePCC",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0"
        )
    )

    @dataclass
    class ProviderReservationInfo:
        """
        :ivar provider_code:
        :ivar provider_locator_code:
        """
        provider_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ProviderCode",
                type="Attribute",
                required=True,
                min_length=2,
                max_length=5
            )
        )
        provider_locator_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ProviderLocatorCode",
                type="Attribute",
                required=True,
                max_length=15
            )
        )


@dataclass
class BaseAirExchangeQuoteReq(BaseCoreReq):
    """
    :ivar ticket_number:
    :ivar provider_reservation_info: Provider: 1G/1V/1P/ACH - Represents a valid Provider Reservation/PNR whose itinerary is to be exchanged
    :ivar air_pricing_solution:
    :ivar air_exchange_modifiers: Provider: ACH.
    :ivar host_token: Provider: ACH.
    :ivar optional_services: Provider: ACH.
    :ivar form_of_payment: Provider: ACH-This would allow a user to see the fees if they are changing from one Form Of Payment to other .
    :ivar repricing_modifiers:
    :ivar original_itinerary_details:
    :ivar pcc:
    :ivar fare_rule_type: Provider: ACH.
    """
    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info: Optional["BaseAirExchangeQuoteReq.ProviderReservationInfo"] = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfo",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=2
        )
    )
    air_exchange_modifiers: Optional[AirExchangeModifiers] = field(
        default=None,
        metadata=dict(
            name="AirExchangeModifiers",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    repricing_modifiers: Optional[RepricingModifiers] = field(
        default=None,
        metadata=dict(
            name="RepricingModifiers",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    original_itinerary_details: Optional[OriginalItineraryDetails] = field(
        default=None,
        metadata=dict(
            name="OriginalItineraryDetails",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    pcc: Optional[Pcc] = field(
        default=None,
        metadata=dict(
            name="PCC",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE_VALUE,
        metadata=dict(
            name="FareRuleType",
            type="Attribute"
        )
    )

    @dataclass
    class ProviderReservationInfo:
        """
        :ivar provider_code:
        :ivar provider_locator_code:
        """
        provider_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ProviderCode",
                type="Attribute",
                required=True,
                min_length=2,
                max_length=5
            )
        )
        provider_locator_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ProviderLocatorCode",
                type="Attribute",
                required=True,
                max_length=15
            )
        )


@dataclass
class LowFareSearchAsynchReq(BaseLowFareSearchReq):
    """Asynchronous Low Fare Search request.

    :ivar air_search_asynch_modifiers: Provider: 1G,1V,1P,1J,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_search_asynch_modifiers: Optional[AirSearchAsynchModifiers] = field(
        default=None,
        metadata=dict(
            name="AirSearchAsynchModifiers",
            type="Element"
        )
    )


@dataclass
class LowFareSearchReq(BaseLowFareSearchReq):
    """Low Fare Search request.

    :ivar policy_reference: This attribute will be used to pass in a value on the request which would be used to link to a ‘Policy Group’ in a policy engine external to UAPI.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    policy_reference: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PolicyReference",
            type="Attribute",
            min_length=1,
            max_length=20
        )
    )


@dataclass
class OptionalServicesInfo:
    """
    :ivar air_pricing_solution:
    :ivar form_of_payment:
    :ivar form_of_payment_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            required=True
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    form_of_payment_ref: List[FormOfPaymentRef] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class TypeAirReservationWithFop(TypeBaseAirReservation):
    """Air Reservation With Form Of Payment.

    :ivar form_of_payment:
    """
    class Meta:
        name = "typeAirReservationWithFOP"

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeMultiQuoteReq(BaseAirExchangeMultiQuoteReq):
    """Request multiple quotes for the exchange of an itinerary. 1P transactions
    only.

    :ivar type: Type choices are "Detail" or "Summary"  Default will be Summary
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    type: str = field(
        default="Summary",
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )


@dataclass
class AirExchangeQuoteReq(BaseAirExchangeQuoteReq):
    """Request to quote the exchange of an itinerary."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AirExchangeRsp(BaseRsp):
    """
    :ivar ticket_number:
    :ivar booking_traveler: Provider: ACH.
    :ivar air_reservation: Provider: ACH.
    :ivar exchange_failure_info: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    ticket_number: List[TicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTraveler",
            type="Element",
            namespace="http://www.travelport.com/schema/common_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_reservation: Optional[TypeAirReservationWithFop] = field(
        default=None,
        metadata=dict(
            name="AirReservation",
            type="Element"
        )
    )
    exchange_failure_info: List[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangeFailureInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeTicketingRsp(BaseRsp):
    """Response to reissue a ticket.

    :ivar air_solution_changed_info:
    :ivar etr: Provider 1G, 1V, 1P.
    :ivar ticket_failure_info: Provider 1G, 1V, 1P.
    :ivar detailed_billing_information: Providers 1G, 1V, 1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_solution_changed_info: Optional[AirSolutionChangedInfo] = field(
        default=None,
        metadata=dict(
            name="AirSolutionChangedInfo",
            type="Element"
        )
    )
    etr: Optional[Etr] = field(
        default=None,
        metadata=dict(
            name="ETR",
            type="Element"
        )
    )
    ticket_failure_info: Optional[TicketFailureInfo] = field(
        default=None,
        metadata=dict(
            name="TicketFailureInfo",
            type="Element"
        )
    )
    detailed_billing_information: Optional[DetailedBillingInformation] = field(
        default=None,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element"
        )
    )


@dataclass
class AirSearchRsp(BaseAvailabilitySearchRsp):
    """Base Response for Air Search.

    :ivar fare_note_list:
    :ivar expert_solution_list:
    :ivar route_list:
    :ivar alternate_route_list:
    :ivar alternate_location_distance_list:
    :ivar fare_info_message:
    :ivar air_pricing_solution:
    :ivar air_price_point_list:
    :ivar rail_segment_list:
    :ivar rail_journey_list:
    :ivar rail_fare_note_list:
    :ivar rail_fare_idlist:
    :ivar rail_fare_list:
    :ivar rail_pricing_solution:
    """
    fare_note_list: Optional[FareNoteList] = field(
        default=None,
        metadata=dict(
            name="FareNoteList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    expert_solution_list: Optional[ExpertSolutionList] = field(
        default=None,
        metadata=dict(
            name="ExpertSolutionList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    route_list: Optional[RouteList] = field(
        default=None,
        metadata=dict(
            name="RouteList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    alternate_route_list: Optional[AlternateRouteList] = field(
        default=None,
        metadata=dict(
            name="AlternateRouteList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    alternate_location_distance_list: Optional[AlternateLocationDistanceList] = field(
        default=None,
        metadata=dict(
            name="AlternateLocationDistanceList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    fare_info_message: List[FareInfoMessage] = field(
        default_factory=list,
        metadata=dict(
            name="FareInfoMessage",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=99
        )
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_price_point_list: Optional[AirPricePointList] = field(
        default=None,
        metadata=dict(
            name="AirPricePointList",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0"
        )
    )
    rail_segment_list: Optional[RailSegmentList] = field(
        default=None,
        metadata=dict(
            name="RailSegmentList",
            type="Element",
            namespace="http://www.travelport.com/schema/rail_v48_0"
        )
    )
    rail_journey_list: Optional[RailJourneyList] = field(
        default=None,
        metadata=dict(
            name="RailJourneyList",
            type="Element",
            namespace="http://www.travelport.com/schema/rail_v48_0"
        )
    )
    rail_fare_note_list: Optional[RailFareNoteList] = field(
        default=None,
        metadata=dict(
            name="RailFareNoteList",
            type="Element",
            namespace="http://www.travelport.com/schema/rail_v48_0"
        )
    )
    rail_fare_idlist: Optional[RailFareIdlist] = field(
        default=None,
        metadata=dict(
            name="RailFareIDList",
            type="Element",
            namespace="http://www.travelport.com/schema/rail_v48_0"
        )
    )
    rail_fare_list: Optional[RailFareList] = field(
        default=None,
        metadata=dict(
            name="RailFareList",
            type="Element",
            namespace="http://www.travelport.com/schema/rail_v48_0"
        )
    )
    rail_pricing_solution: List[RailPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="RailPricingSolution",
            type="Element",
            namespace="http://www.travelport.com/schema/rail_v48_0",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirTicketingRsp(BaseRsp):
    """Response to ticket a previously stored reservation.

    :ivar air_solution_changed_info:
    :ivar etr: Provider: 1G,1V,1P,1J.
    :ivar ticket_failure_info: Provider: 1G,1V,1P,1J.
    :ivar detailed_billing_information: Provider: 1G,1V,1P,1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_solution_changed_info: Optional[AirSolutionChangedInfo] = field(
        default=None,
        metadata=dict(
            name="AirSolutionChangedInfo",
            type="Element"
        )
    )
    etr: List[Etr] = field(
        default_factory=list,
        metadata=dict(
            name="ETR",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticket_failure_info: List[TicketFailureInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TicketFailureInfo",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata=dict(
            name="DetailedBillingInformation",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirUpsellSearchReq(AirBaseReq):
    """Request to search for Upsell Offers based on the Itinerary.

    :ivar air_itinerary: Provider: 1G,1V,1P,1J,ACH-AirItinerary of the pricing request.
    :ivar air_price_result: Provider: 1G,1V,1P,1J,ACH-Result of AirPrice request. Upsell uses this to search for new offer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    air_itinerary: Optional[AirItinerary] = field(
        default=None,
        metadata=dict(
            name="AirItinerary",
            type="Element",
            required=True
        )
    )
    air_price_result: List[AirPriceResult] = field(
        default_factory=list,
        metadata=dict(
            name="AirPriceResult",
            type="Element",
            min_occurs=1,
            max_occurs=16
        )
    )


@dataclass
class BaseAirPriceRsp(BaseRsp):
    """
    :ivar air_itinerary: Provider: 1G,1V,1P,1J,ACH.
    :ivar air_price_result: Provider: 1G,1V,1P,1J,ACH.
    """
    air_itinerary: Optional[AirItinerary] = field(
        default=None,
        metadata=dict(
            name="AirItinerary",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            required=True
        )
    )
    air_price_result: List[AirPriceResult] = field(
        default_factory=list,
        metadata=dict(
            name="AirPriceResult",
            type="Element",
            namespace="http://www.travelport.com/schema/air_v48_0",
            min_occurs=1,
            max_occurs=16
        )
    )


@dataclass
class AirPriceRsp(BaseAirPriceRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class AirUpsellSearchRsp(BaseAirPriceRsp):
    """Response of Upsell Offers search for the given Itinerary."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"


@dataclass
class LowFareSearchAsynchRsp(AirSearchRsp):
    """Asynchronous Low Fare Search Response contains only the 1st Provider
    response unless time out occurs.

    :ivar async_provider_specific_response: Provider: 1G,1V,1P,1J,ACH-Identifies pending responses from a specific provider using MoreResults attribute
    :ivar brand_list:
    :ivar search_id: Provider: 1G,1V,1P,1J,ACH-Indicates the Search Id of the LFS search
    :ivar currency_type: Provider: 1G,1V,1P,1J,ACH-Specifies the default Currency Type in the response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    async_provider_specific_response: List[AsyncProviderSpecificResponse] = field(
        default_factory=list,
        metadata=dict(
            name="AsyncProviderSpecificResponse",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    brand_list: Optional[BrandList] = field(
        default=None,
        metadata=dict(
            name="BrandList",
            type="Element"
        )
    )
    search_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SearchId",
            type="Attribute",
            required=True
        )
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            length=3
        )
    )


@dataclass
class LowFareSearchRsp(AirSearchRsp):
    """Low Fare Search Response.

    :ivar brand_list:
    :ivar currency_type: Provider: 1G,1V,1P,1J,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    brand_list: Optional[BrandList] = field(
        default=None,
        metadata=dict(
            name="BrandList",
            type="Element"
        )
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            required=True,
            length=3
        )
    )


@dataclass
class RetrieveLowFareSearchRsp(AirSearchRsp):
    """Low Fare Search Asynchronous Result response.

    :ivar async_provider_specific_response: Provider: 1G,1V,1P,1J,ACH-Identifies pending responses from a specific provider using MoreResults attribute
    :ivar brand_list:
    :ivar currency_type: Provider: 1G,1V,1P,1J,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"

    async_provider_specific_response: List[AsyncProviderSpecificResponse] = field(
        default_factory=list,
        metadata=dict(
            name="AsyncProviderSpecificResponse",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )
    brand_list: Optional[BrandList] = field(
        default=None,
        metadata=dict(
            name="BrandList",
            type="Element"
        )
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            length=3
        )
    )


@dataclass
class ScheduleSearchRsp(AirSearchRsp):
    """Schedule Search response."""
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v48_0"