from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from xsdata.models.datatype import XmlDate, XmlDateTime
from travelport.models.common import (
    BaseReservation,
    BookingTravelerRef,
    ConnectionPoint,
    DiscountCard,
    HostToken,
    Payment,
    Remark,
    Segment,
    SupplierLocator,
    TypeElementStatus,
    TypeFlexibleTimeSpec,
    TypePassengerType,
    TypeSearchLocation,
    TypeTimeSpec,
)

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v48_0"


@dataclass
class FareValidity:
    """
    Associates fare validity dates with journeys.

    Parameters
    ----------
    rail_journey_ref
        Reference to a journey to which this fare validity refers.
    not_valid_before
        Fare not valid before this date.
    not_valid_after
        Fare not valid after this date.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_journey_ref: None | str = field(
        default=None,
        metadata={
            "name": "RailJourneyRef",
            "type": "Attribute",
            "required": True,
        }
    )
    not_valid_before: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        }
    )
    not_valid_after: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        }
    )


@dataclass
class FulFillmentType:
    """Fulfillment options for this segment.

    the options will be one of "Ticket on Departure", "Ticketless",
    "Ticket By Email", "Travel Agency"
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 255,
        }
    )


@dataclass
class JourneyRemark:
    """
    A Remark for a Journey.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )


@dataclass
class OperatingCompany:
    """
    A textual remark identifying the OperatingCompany/Train Service other than BN
    orTL.

    Parameters
    ----------
    value
    code
        Company Short Text
    name
        Name Identifying the Train Service other than BN orTL
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailAutoSeatAssignment:
    """
    Request object used to request seats automatically by seat type.

    Parameters
    ----------
    seat_type
        Indicates codeset of values such as Seat Type like Place,Position,
        Smoking Choice, Place Arrangement, Place Direction, Compartment.
    seat_value
        Indicates the value specific to the selected type.
    rail_segment_ref
        The rail segment that this assignment belongs to
    booking_traveler_ref
        The booking traveler that this seat assignment is for. If not
        entered, this applies to the primary booking traveler and other
        passengers are adjacent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    seat_type: None | str = field(
        default=None,
        metadata={
            "name": "SeatType",
            "type": "Attribute",
            "required": True,
            "min_length": 0,
            "max_length": 255,
        }
    )
    seat_value: None | str = field(
        default=None,
        metadata={
            "name": "SeatValue",
            "type": "Attribute",
            "required": True,
            "min_length": 0,
            "max_length": 255,
        }
    )
    rail_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class RailAvailInfo:
    """
    Parameters
    ----------
    class_code
        A booking code or fare basis code or fare class.
    quantity
        Available fare basis code or fare class quantity.
    cabin_class
        The fare basis code or fare class for this fare.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    class_code: None | str = field(
        default=None,
        metadata={
            "name": "ClassCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    quantity: None | int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        }
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class RailBookingInfo:
    """
    Links journeys and fares together.

    Parameters
    ----------
    rail_fare_ref
        Reference to a fare that applies to the journey below.
    rail_journey_ref
        Reference to a journeys on which the above fare applies.
    optional_service
        Indicate the OfferFareItem elements  will be Optional or not.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_fare_ref: None | str = field(
        default=None,
        metadata={
            "name": "RailFareRef",
            "type": "Attribute",
            "required": True,
        }
    )
    rail_journey_ref: None | str = field(
        default=None,
        metadata={
            "name": "RailJourneyRef",
            "type": "Attribute",
            "required": True,
        }
    )
    optional_service: bool = field(
        default=False,
        metadata={
            "name": "OptionalService",
            "type": "Attribute",
        }
    )


@dataclass
class RailExchangeInfo:
    """
    Exchange information for the rail booking.

    Parameters
    ----------
    refund_amount
    cancellation_fee
    exchange_amount
    approximate_refund_amount
    approximate_cancellation_fee
    approximate_exchange_amount
        The Converted total price in Default Currency for this entity
        including base price and all taxes.
    retain_amount
        Amount retained by a rail vendor for future use at the vendor’s
        site.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    refund_amount: None | str = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
        }
    )
    cancellation_fee: None | str = field(
        default=None,
        metadata={
            "name": "CancellationFee",
            "type": "Attribute",
        }
    )
    exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
        }
    )
    approximate_refund_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateRefundAmount",
            "type": "Attribute",
        }
    )
    approximate_cancellation_fee: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateCancellationFee",
            "type": "Attribute",
        }
    )
    approximate_exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateExchangeAmount",
            "type": "Attribute",
        }
    )
    retain_amount: None | str = field(
        default=None,
        metadata={
            "name": "RetainAmount",
            "type": "Attribute",
        }
    )


@dataclass
class RailFareIdref:
    """
    Reference to a complete FareID from a shared list.
    """
    class Meta:
        name = "RailFareIDRef"
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailFareNoteRef:
    """A reference to a fare note from a shared list.

    Used to minimize xml results.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailFareRef:
    """
    Reference to a complete FareInfo from a shared list.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailInfo:
    """
    Container for rail-related information required for retrieving a rail seat
    map/coach map.

    Parameters
    ----------
    origin
        The IATA location code for this origination of this entity.
    rail_loc_origin
        RCH specific origin code (a.k.a UCodes) which uniquely identifies a
        train station.
    destination
        The IATA location code for this destination of this entity.
    rail_loc_destination
        RCH specific destination code (a.k.a UCodes) which uniquely
        identifies a train station.
    departure_time
        The date and time at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location.
    arrival_time
        The date and time at which this entity arrives at the destination.
        This does not include time zone information since it can be derived
        from the origin location.
    train_number
    provider_code
    supplier_code
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    rail_loc_origin: None | str = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    rail_loc_destination: None | str = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    departure_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    train_number: None | str = field(
        default=None,
        metadata={
            "name": "TrainNumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: None | str = field(
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
class RailJourneyRef:
    """
    Reference to a RailJourney.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailRefundInfo:
    """
    Information about refund.

    Parameters
    ----------
    refund_amount
        Amount refunded back to customer.
    cancellation_fee
        Cancellation penalty imposed by the distributor.
    refund
        Indicates whether vendor offers refund on rail reservation.
    retain
        Indicates whether vendor retains the amount to be used later.
    retain_amount
        Amount retained by rail vendor for futute exchange/rail book at rail
        vendor site.
    net_amount
        Net total amount to be refunded or retained by the vendor.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    refund_amount: None | str = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
        }
    )
    cancellation_fee: None | str = field(
        default=None,
        metadata={
            "name": "CancellationFee",
            "type": "Attribute",
        }
    )
    refund: None | bool = field(
        default=None,
        metadata={
            "name": "Refund",
            "type": "Attribute",
        }
    )
    retain: None | bool = field(
        default=None,
        metadata={
            "name": "Retain",
            "type": "Attribute",
        }
    )
    retain_amount: None | str = field(
        default=None,
        metadata={
            "name": "RetainAmount",
            "type": "Attribute",
        }
    )
    net_amount: None | str = field(
        default=None,
        metadata={
            "name": "NetAmount",
            "type": "Attribute",
        }
    )


@dataclass
class RailSegmentRef:
    """
    Reference to a RaiLSegment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class RailSolutionChangedInfoReasonCode(Enum):
    PRICE = "Price"
    SCHEDULE = "Schedule"
    BOTH = "Both"


@dataclass
class RailSpecificSeatAssignment:
    """
    Request object used to request a specific coach and seat number or a seat near-
    to a specific seat number.

    Parameters
    ----------
    coach_label
        The coach number of the train being requested.
    place_label
        The actual seat number or the close-to seat number based on the
        Assignment.
    assignment
        Defines how the PlaceLabel should be applied.  The values are
        6.STP for actual seat or 2.STP for close-to seat. Default is
        2.STP.
    rail_segment_ref
        The rail segment to which this assignment belongs.
    booking_traveler_ref
        The BookingTraveler for this seat assignment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    coach_label: None | str = field(
        default=None,
        metadata={
            "name": "CoachLabel",
            "type": "Attribute",
            "required": True,
        }
    )
    place_label: None | str = field(
        default=None,
        metadata={
            "name": "PlaceLabel",
            "type": "Attribute",
            "required": True,
        }
    )
    assignment: None | str = field(
        default=None,
        metadata={
            "name": "Assignment",
            "type": "Attribute",
            "required": True,
        }
    )
    rail_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
            "type": "Attribute",
            "required": True,
        }
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailSupplier:
    """
    Parameters
    ----------
    code
        2 character Rail distributor code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    code: None | str = field(
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
class TicketAdvisory:
    """
    Additional ticket information.

    Parameters
    ----------
    value
    key
    language_code
        ISO 639 two-character language codes are used to retrieve specific
        information in the requested language. For Rich Content and
        Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS
        (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese
        Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE,
        DECH can also be used. Only certain services support this attribute.
        Providers: ACH, RCH, 1G, 1V, 1P, 1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 500,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    language_code: None | str = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Attribute",
        }
    )


class TypeCoachClassType(Enum):
    """
    Values for accommodation class.
    """
    FIRST_CLASS = "First Class"
    STANDARD_CLASS = "Standard Class"
    FIRST_AND_STANDARD_CLASS = "First and Standard Class"
    OTHER = "Other"


class TypeJourneyDirection(Enum):
    """
    Outbound and Return directions.
    """
    OUTWARD = "Outward"
    RETURN = "Return"


class TypeRailDirection(Enum):
    """
    The direction of travel.
    """
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"
    BOTH = "Both"


class TypeRailSegmentInfo(Enum):
    """
    Extra for ExtraSegmentInfo and Vendor for VendorMessages.
    """
    EXTRA = "Extra"
    VENDOR = "Vendor"
    SERVICES = "Services"


class TypeTransportMode(Enum):
    """
    Enumeration of all Train Transport Modes.
    """
    BICYCLE = "Bicycle"
    BOAT = "Boat"
    BUS = "Bus"
    CABLE_CAR = "Cable Car"
    CAR = "Car"
    CARRIAGE = "Carriage"
    COURTESY_CAR = "Courtesy car"
    HELICOPTER = "Helicopter"
    LIMOUSINE = "Limousine"
    METRO = "Metro"
    MONORAIL = "Monorail"
    MOTORBIKE = "Motorbike"
    PACK_ANIMAL = "Pack Animal"
    PLANE = "Plane"
    RENTAL_CAR = "Rental Car"
    RICKSHAW = "Rickshaw"
    SHUTTLE = "Shuttle"
    SUBWAY = "Subway"
    SEDAN_CHAIR = "Sedan Chair"
    TAXI = "Taxi"
    TRAIN = "Train"
    TROLLEY = "Trolley"
    TUBE = "Tube"
    WALK = "Walk"
    WATER_TAXI = "Water Taxi"
    OTHER = "Other"
    CAR_RUSH_HOUR = "Car/Rush hour"
    TAXI_RUSH_HOUR = "Taxi/Rush hour"
    NO_TRANSPORTATION = "No Transportation"
    EXPRESS_TRAIN = "Express Train"
    PUBLIC = "Public"
    SHIP_FERRY = "Ship/Ferry"
    UNDERGROUND = "Underground"
    TRAM_LIGHT_RAIL = "Tram/light rail"
    SHARED_TAXI = "Shared Taxi"


@dataclass
class Characteristic:
    """
    Defines coach characteristics such as accommodation class, smoking choice, etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    smoking: bool = field(
        default=False,
        metadata={
            "name": "Smoking",
            "type": "Attribute",
        }
    )
    class_value: None | TypeCoachClassType = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
        }
    )


@dataclass
class RailFareComponent:
    """
    Contains fare and discount information for each passenger type.

    Parameters
    ----------
    discount
        Discount information specific to the fare component
    key
    amount
        FareComponent amount
    age
    passenger_type_code
        The three character passenger code
    supplier_passenger_type
        Supplier passenger type code
    quantity
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    discount: list[RailFareComponent.Discount] = field(
        default_factory=list,
        metadata={
            "name": "Discount",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    age: None | int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        }
    )
    passenger_type_code: None | str = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    supplier_passenger_type: None | str = field(
        default=None,
        metadata={
            "name": "SupplierPassengerType",
            "type": "Attribute",
        }
    )
    quantity: None | int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        }
    )

    @dataclass
    class Discount:
        discount_card: list[DiscountCard] = field(
            default_factory=list,
            metadata={
                "name": "DiscountCard",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 9,
            }
        )
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
            }
        )


@dataclass
class RailFareId:
    """
    Parameters
    ----------
    value
    key
    category
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """
    class Meta:
        name = "RailFareID"
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    el_stat: None | TypeElementStatus = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class RailFareNote:
    """A simple textual fare note.

    Used within several other objects.

    Parameters
    ----------
    value
    key
    note_name
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    note_name: None | str = field(
        default=None,
        metadata={
            "name": "NoteName",
            "type": "Attribute",
            "required": True,
        }
    )
    el_stat: None | TypeElementStatus = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class RailLegModifiers:
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    permitted_connection_points: None | RailLegModifiers.PermittedConnectionPoints = field(
        default=None,
        metadata={
            "name": "PermittedConnectionPoints",
            "type": "Element",
        }
    )
    prohibited_connection_points: None | RailLegModifiers.ProhibitedConnectionPoints = field(
        default=None,
        metadata={
            "name": "ProhibitedConnectionPoints",
            "type": "Element",
        }
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
        }
    )

    @dataclass
    class PermittedConnectionPoints:
        connection_point: list[ConnectionPoint] = field(
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
        connection_point: list[ConnectionPoint] = field(
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
class RailPricingModifiers:
    """
    Search flexibiity criteria .

    Parameters
    ----------
    discount_card
        Discount request for rail.
    prohibit_non_refundable_fares
        Indicates whether it prohibits NonRefundable Fares.
    prohibit_non_exchangeable_fares
        Indicates whether it prohibits NonExchangeable Fares .
    currency_type
        3 Letter Currency Code
    rail_search_type
        RailSearchType options are "All Fares"  "Fastest"  "Lowest Fare"
        "One Fare Per Class" "Seasons".  Supported by NTV/VF only for "All
        Fares" "Lowest Fare" and "One Fare Per Class". Provider : RCH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    discount_card: list[DiscountCard] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 9,
        }
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonRefundableFares",
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
    currency_type: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        }
    )
    rail_search_type: None | str = field(
        default=None,
        metadata={
            "name": "RailSearchType",
            "type": "Attribute",
        }
    )


@dataclass
class RailSearchModifiers:
    """
    Controls and switches for the Rail Availability Search request.

    Parameters
    ----------
    preferred_suppliers
    max_changes
        The maximum number of stops within a connection.
    direction
        The direction of travel.
    class_value
    max_solutions
        The maximum number of solutions to return. Decreasing this number
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    preferred_suppliers: None | RailSearchModifiers.PreferredSuppliers = field(
        default=None,
        metadata={
            "name": "PreferredSuppliers",
            "type": "Element",
        }
    )
    max_changes: int = field(
        default=2,
        metadata={
            "name": "MaxChanges",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 3,
        }
    )
    direction: None | TypeRailDirection = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
        }
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
        }
    )
    max_solutions: int = field(
        default=300,
        metadata={
            "name": "MaxSolutions",
            "type": "Attribute",
        }
    )

    @dataclass
    class PreferredSuppliers:
        rail_supplier: list[RailSupplier] = field(
            default_factory=list,
            metadata={
                "name": "RailSupplier",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class RailSegmentInfo:
    """A textual remark container to hold any printable text.

    (max 512 chars) Holds the ExtraSegmentInfo and VendorMessages from
    RCH response.

    Parameters
    ----------
    value
    category
        Supplier specific category.
    type_value
        Either Extra for ExtraSegmentInfo or Vendor for VendorMessages.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    type_value: None | TypeRailSegmentInfo = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailTicketInfo:
    """
    Parameters
    ----------
    rail_journey_ref
    ticket_advisory
    number
        Ticket number.
    issue_location
        Issue location is internal distributor code associated with the PCC.
    ticket_status
        Status of Ticket.
    ticket_form_type
        FormType of Ticket.
    traffic_type
        Type of traffic.
    issued_date
        Ticket issue date.
    ticket_type
        Type of ticket. Paper, eTicket etc.
    booking_traveler_ref
        Reference to a BookingTraveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_journey_ref: list[RailJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "RailJourneyRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ticket_advisory: list[TicketAdvisory] = field(
        default_factory=list,
        metadata={
            "name": "TicketAdvisory",
            "type": "Element",
            "max_occurs": 10,
        }
    )
    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 19,
        }
    )
    issue_location: None | str = field(
        default=None,
        metadata={
            "name": "IssueLocation",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 128,
        }
    )
    ticket_status: None | str = field(
        default=None,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    ticket_form_type: None | str = field(
        default=None,
        metadata={
            "name": "TicketFormType",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        }
    )
    traffic_type: None | str = field(
        default=None,
        metadata={
            "name": "TrafficType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    issued_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "IssuedDate",
            "type": "Attribute",
        }
    )
    ticket_type: None | str = field(
        default=None,
        metadata={
            "name": "TicketType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class Coach:
    """
    Captures rail seat map/coach map information.

    Parameters
    ----------
    characteristic
    remark
    coach_number
        Coach number for which seat map/coach map is returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    characteristic: None | Characteristic = field(
        default=None,
        metadata={
            "name": "Characteristic",
            "type": "Element",
        }
    )
    remark: list[Remark] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    coach_number: None | str = field(
        default=None,
        metadata={
            "name": "CoachNumber",
            "type": "Attribute",
        }
    )


@dataclass
class RailFare:
    """
    Information about this fare component.

    Parameters
    ----------
    rail_fare_note_ref
        Key reference to RailFareNote present in RailFareNotList
    rail_fare_id
    rail_fare_idref
    fare_validity
    host_token
    ful_fillment_type
    rail_fare_component
    key
    fare_basis
        The fare basis code  or fare description for this fare
    cabin_class
        The fare basis code or fare class for this fare
    passenger_type_code
        The PTC that is associated with this fare. Default to ADT
    origin
        Returns the airport or city code that defines the origin market for
        this fare.
    destination
        Returns the airport or city code that defines the destination market
        for this fare.
    effective_date
        Returns the date on which this fare was quoted. Set as current date
    amount
    route_description
        Describes the route of the train fare.
    ticket_type_code
        Describes the main identifier code of the fare.
    fare_reference
        Unique reference for the fare that is required in RailExchangeQuote
        request.
    cross_city_fare
        Set to 'true' if the fare is valid across a Metropolitan Area, eg.
        Cross-London travel via the London Underground.
    origin_station_name
        The origin station name for the Rail Fare.
    destination_station_name
        The destination station name for the Rail Fare.
    reservation_required
        Set to true if a seat reservation is required while booking.
    journey_direction
        The direction of the Journey (Outward or Return) associated with the
        Rail fare.
    rail_loc_origin
        RCH specific origin code (a.k.a UCodes) which uniquely identifies a
        train station.
    rail_loc_destination
        RCH specific destination code (a.k.a UCodes) which uniquely
        identifies a train station.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_fare_note_ref: list[RailFareNoteRef] = field(
        default_factory=list,
        metadata={
            "name": "RailFareNoteRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_fare_id: list[RailFareId] = field(
        default_factory=list,
        metadata={
            "name": "RailFareID",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_fare_idref: list[RailFareIdref] = field(
        default_factory=list,
        metadata={
            "name": "RailFareIDRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_validity: list[FareValidity] = field(
        default_factory=list,
        metadata={
            "name": "FareValidity",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_token: None | HostToken = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    ful_fillment_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "FulFillmentType",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 0,
            "max_length": 255,
        }
    )
    rail_fare_component: list[RailFareComponent] = field(
        default_factory=list,
        metadata={
            "name": "RailFareComponent",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
        }
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    passenger_type_code: None | str = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    effective_date: None | str = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    route_description: None | str = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Attribute",
        }
    )
    ticket_type_code: None | str = field(
        default=None,
        metadata={
            "name": "TicketTypeCode",
            "type": "Attribute",
        }
    )
    fare_reference: None | str = field(
        default=None,
        metadata={
            "name": "FareReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    cross_city_fare: bool = field(
        default=False,
        metadata={
            "name": "CrossCityFare",
            "type": "Attribute",
        }
    )
    origin_station_name: None | str = field(
        default=None,
        metadata={
            "name": "OriginStationName",
            "type": "Attribute",
        }
    )
    destination_station_name: None | str = field(
        default=None,
        metadata={
            "name": "DestinationStationName",
            "type": "Attribute",
        }
    )
    reservation_required: None | bool = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Attribute",
        }
    )
    journey_direction: None | TypeJourneyDirection = field(
        default=None,
        metadata={
            "name": "JourneyDirection",
            "type": "Attribute",
        }
    )
    rail_loc_origin: None | str = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    rail_loc_destination: None | str = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    el_stat: None | TypeElementStatus = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class RailFareIdlist:
    """
    The shared object list of FareIDs.
    """
    class Meta:
        name = "RailFareIDList"
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_fare_id: list[RailFareId] = field(
        default_factory=list,
        metadata={
            "name": "RailFareID",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class RailFareNoteList:
    """
    The shared object list of Notes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_fare_note: list[RailFareNote] = field(
        default_factory=list,
        metadata={
            "name": "RailFareNote",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class RailSegment(Segment):
    """
    Rail Segment.

    Parameters
    ----------
    rail_segment_info
    operating_company
    rail_avail_info
    ful_fillment_type
    train_number
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    departure_time
        The date and time at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location.
    arrival_time
        The date and time at which this entity arrives at the destination.
        This does not include time zone information since it can be derived
        from the origin location.
    origin_station_name
        The origin station name for the Journey.
    destination_station_name
        The destination station name for the Journey.
    rail_loc_origin
        RCH specific origin code (a.k.a UCodes) which uniquely identifies a
        train station.
    rail_loc_destination
        RCH specific destination code (a.k.a UCodes) which uniquely
        identifies a train station.
    train_type
        Type of train used. Same as TrainServiceType.
    train_type_code
        Code for type of train used. Same as TrainServiceType.
    transport_mode
        Type of Transport Mode used.
    seat_assignable
        Set to true if there exists seats to be booked
    transport_code
        Supplier specific train code
    reservation_required
        Set to true if a reservation is required for booking.
    travel_time
        Total time spent (minutes) traveling
    host_token_ref
        The reference key for the host token. From the HostTokenList
        Providers RCH.
    cabin_class
        Rail Cabin class specification. The valid values are Economy,
        Business, First and Other
    class_code
        A booking code or fare basis code or fare class.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_segment_info: list[RailSegmentInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailSegmentInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    operating_company: None | OperatingCompany = field(
        default=None,
        metadata={
            "name": "OperatingCompany",
            "type": "Element",
        }
    )
    rail_avail_info: list[RailAvailInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailAvailInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ful_fillment_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "FulFillmentType",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 0,
            "max_length": 255,
        }
    )
    train_number: None | str = field(
        default=None,
        metadata={
            "name": "TrainNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    origin_station_name: None | str = field(
        default=None,
        metadata={
            "name": "OriginStationName",
            "type": "Attribute",
        }
    )
    destination_station_name: None | str = field(
        default=None,
        metadata={
            "name": "DestinationStationName",
            "type": "Attribute",
        }
    )
    rail_loc_origin: None | str = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    rail_loc_destination: None | str = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    train_type: None | str = field(
        default=None,
        metadata={
            "name": "TrainType",
            "type": "Attribute",
        }
    )
    train_type_code: None | str = field(
        default=None,
        metadata={
            "name": "TrainTypeCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    transport_mode: None | TypeTransportMode = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Attribute",
        }
    )
    seat_assignable: None | bool = field(
        default=None,
        metadata={
            "name": "SeatAssignable",
            "type": "Attribute",
        }
    )
    transport_code: None | str = field(
        default=None,
        metadata={
            "name": "TransportCode",
            "type": "Attribute",
        }
    )
    reservation_required: None | bool = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Attribute",
        }
    )
    travel_time: None | int = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        }
    )
    host_token_ref: None | str = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        }
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    class_code: None | str = field(
        default=None,
        metadata={
            "name": "ClassCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )


@dataclass
class RailFareList:
    """
    The shared object list of FareInfos.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_fare: list[RailFare] = field(
        default_factory=list,
        metadata={
            "name": "RailFare",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class RailJourney:
    """
    Captures all journey-related data.

    Parameters
    ----------
    rail_segment
    rail_segment_ref
    journey_remark
    host_token
    key
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    departure_time
        The date and time at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location.
    arrival_time
        The date and time at which this entity arrives at the destination.
        This does not include time zone information since it can be derived
        from the origin location.
    origin_station_name
        The origin station name for the Journey.
    destination_station_name
        The destination station name for the Journey.
    rail_loc_origin
        RCH specific origin code (a.k.a UCodes) which uniquely identifies a
        train station.
    rail_loc_destination
        RCH specific destination code (a.k.a UCodes) which uniquely
        identifies a train station.
    route_description
        The description of the route.
    journey_direction
        The direction of the Journey (Outward or Return).
    journey_duration
        The duration of the entire Journey in minutes
    total_price
        The total price for this entity including base price and all taxes.
    base_price
        Represents the base price for this entity. This does not include any
        taxes or surcharges.
    approximate_total_price
        The Converted total price in Default Currency for this entity
        including base price and all taxes.
    approximate_base_price
        The Converted base price in Default Currency for this entity. This
        does not include any taxes or surcharges.
    equivalent_base_price
        Represents the base price in the related currency for this entity.
        This does not include any taxes or surcharges.
    taxes
        The aggregated amount of all the taxes that are associated with this
        entity. See the associated TaxInfo array for a breakdown of the
        individual taxes.
    fees
        The aggregated amount of all the fees that are associated with this
        entity. See the associated FeeInfo array for a breakdown of the
        individual fees.
    services
        The total cost for all optional services.
    approximate_taxes
        The Converted tax amount in Default Currency.
    approximate_fees
        The Converted fee amount in Default Currency.
    provider_code
    supplier_code
    status
        Status of this Journey.
    provider_reservation_info_ref
        Provider reservation reference key.
    passive_provider_reservation_info_ref
        Passive provider reservation reference key.
    travel_order
        To identify the appropriate travel sequence for Air/Car/Hotel/Rail
        segments/reservations/Journeys based on travel dates. This ordering
        is applicable across the UR not provider or traveler specific
    route_reference
        RouteReference is required in seat assignment purpose
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    operation
        "Type of exchange. Add - Add new Journey. Update - Modify existing
        Journey. Delete - Remove existing Journey"
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_segment: list[RailSegment] = field(
        default_factory=list,
        metadata={
            "name": "RailSegment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_segment_ref: list[RailSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "RailSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    journey_remark: list[JourneyRemark] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRemark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_token: list[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    origin_station_name: None | str = field(
        default=None,
        metadata={
            "name": "OriginStationName",
            "type": "Attribute",
        }
    )
    destination_station_name: None | str = field(
        default=None,
        metadata={
            "name": "DestinationStationName",
            "type": "Attribute",
        }
    )
    rail_loc_origin: None | str = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    rail_loc_destination: None | str = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    route_description: None | str = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Attribute",
            "max_length": 255,
        }
    )
    journey_direction: None | TypeJourneyDirection = field(
        default=None,
        metadata={
            "name": "JourneyDirection",
            "type": "Attribute",
        }
    )
    journey_duration: None | int = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
            "type": "Attribute",
        }
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: None | str = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: None | str = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: None | str = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    passive_provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    travel_order: None | int = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        }
    )
    route_reference: None | str = field(
        default=None,
        metadata={
            "name": "RouteReference",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        }
    )
    el_stat: None | TypeElementStatus = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    operation: None | str = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Attribute",
        }
    )


@dataclass
class RailPricingInfo:
    """
    Per traveler type pricing breakdown.

    Parameters
    ----------
    rail_fare
    rail_fare_ref
    rail_booking_info
    passenger_type
    booking_traveler_ref
    key
    exchange_amount
        The amount to pay to cover the exchange of the fare (includes
        penalties).
    approximate_exchange_amount
    total_price
        The total price for this entity including base price and all taxes.
    base_price
        Represents the base price for this entity. This does not include any
        taxes or surcharges.
    approximate_total_price
        The Converted total price in Default Currency for this entity
        including base price and all taxes.
    approximate_base_price
        The Converted base price in Default Currency for this entity. This
        does not include any taxes or surcharges.
    equivalent_base_price
        Represents the base price in the related currency for this entity.
        This does not include any taxes or surcharges.
    taxes
        The aggregated amount of all the taxes that are associated with this
        entity. See the associated TaxInfo array for a breakdown of the
        individual taxes.
    fees
        The aggregated amount of all the fees that are associated with this
        entity. See the associated FeeInfo array for a breakdown of the
        individual fees.
    services
        The total cost for all optional services.
    approximate_taxes
        The Converted tax amount in Default Currency.
    approximate_fees
        The Converted fee amount in Default Currency.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_fare: list[RailFare] = field(
        default_factory=list,
        metadata={
            "name": "RailFare",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_fare_ref: list[RailFareRef] = field(
        default_factory=list,
        metadata={
            "name": "RailFareRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_booking_info: list[RailBookingInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailBookingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    passenger_type: list[TypePassengerType] = field(
        default_factory=list,
        metadata={
            "name": "PassengerType",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    booking_traveler_ref: list[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
        }
    )
    approximate_exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateExchangeAmount",
            "type": "Attribute",
        }
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: None | str = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: None | str = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: None | str = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    el_stat: None | TypeElementStatus = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class RailSegmentList:
    """
    List of Rail Segments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_segment: list[RailSegment] = field(
        default_factory=list,
        metadata={
            "name": "RailSegment",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class RailJourneyList:
    """
    List of Rail Journeys.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_journey: list[RailJourney] = field(
        default_factory=list,
        metadata={
            "name": "RailJourney",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class RailReservation(BaseReservation):
    """
    The parent container for all Rail booking data.

    Parameters
    ----------
    booking_traveler_ref
    rail_journey
    rail_pricing_info
    payment
    rail_ticket_info
    rail_fare_note_list
        List of RailFareNote(s) that is referenced by key in RailFare.
    supplier_locator
    booking_status
        The Current Status of the rail booking.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    booking_traveler_ref: list[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 9,
        }
    )
    rail_journey: list[RailJourney] = field(
        default_factory=list,
        metadata={
            "name": "RailJourney",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    rail_pricing_info: list[RailPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    payment: list[Payment] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    rail_ticket_info: list[RailTicketInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailTicketInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_fare_note_list: None | RailFareNoteList = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
        }
    )
    supplier_locator: list[SupplierLocator] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    booking_status: None | str = field(
        default=None,
        metadata={
            "name": "BookingStatus",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SearchRailLeg:
    """
    Holds Origin, Destination, and Departure times for a Rail Leg to search for.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    search_origin: list[TypeSearchLocation] = field(
        default_factory=list,
        metadata={
            "name": "SearchOrigin",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    search_destination: list[TypeSearchLocation] = field(
        default_factory=list,
        metadata={
            "name": "SearchDestination",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    rail_segment_list: None | RailSegmentList = field(
        default=None,
        metadata={
            "name": "RailSegmentList",
            "type": "Element",
        }
    )
    search_dep_time: list[TypeFlexibleTimeSpec] = field(
        default_factory=list,
        metadata={
            "name": "SearchDepTime",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    search_arv_time: list[TypeTimeSpec] = field(
        default_factory=list,
        metadata={
            "name": "SearchArvTime",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_leg_modifiers: None | RailLegModifiers = field(
        default=None,
        metadata={
            "name": "RailLegModifiers",
            "type": "Element",
        }
    )


@dataclass
class TypeRailPricingSolution:
    """
    Common RailPricingSolution container.

    Parameters
    ----------
    rail_journey
    rail_journey_ref
    rail_pricing_info
    key
    offer_id
        OfferID must be included if the RailCreateReq contains a price.  If
        the RailCreateReq is used for the Direct Book function, the OfferID
        is not included.
    total_price
        The total price for this entity including base price and all taxes.
    base_price
        Represents the base price for this entity. This does not include any
        taxes or surcharges.
    approximate_total_price
        The Converted total price in Default Currency for this entity
        including base price and all taxes.
    approximate_base_price
        The Converted base price in Default Currency for this entity. This
        does not include any taxes or surcharges.
    equivalent_base_price
        Represents the base price in the related currency for this entity.
        This does not include any taxes or surcharges.
    taxes
        The aggregated amount of all the taxes that are associated with this
        entity. See the associated TaxInfo array for a breakdown of the
        individual taxes.
    fees
        The aggregated amount of all the fees that are associated with this
        entity. See the associated FeeInfo array for a breakdown of the
        individual fees.
    services
        The total cost for all optional services.
    approximate_taxes
        The Converted tax amount in Default Currency.
    approximate_fees
        The Converted fee amount in Default Currency.
    provider_code
    supplier_code
    host_token_ref
        HostTokenRef will reference the value in HostTokenList/HostToken @
        Key
    reference
        Offer Reference required for Booking(eg.TL).
    """
    class Meta:
        name = "typeRailPricingSolution"

    rail_journey: list[RailJourney] = field(
        default_factory=list,
        metadata={
            "name": "RailJourney",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v48_0",
            "max_occurs": 999,
        }
    )
    rail_journey_ref: list[RailJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "RailJourneyRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v48_0",
            "max_occurs": 999,
        }
    )
    rail_pricing_info: list[RailPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v48_0",
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    offer_id: None | int = field(
        default=None,
        metadata={
            "name": "OfferId",
            "type": "Attribute",
        }
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: None | str = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: None | str = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: None | str = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
    host_token_ref: None | str = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        }
    )
    reference: None | str = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Attribute",
        }
    )


@dataclass
class RailExchangeSolution(TypeRailPricingSolution):
    """
    Contains the fares and segments for a particular offer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_exchange_info: None | RailExchangeInfo = field(
        default=None,
        metadata={
            "name": "RailExchangeInfo",
            "type": "Element",
        }
    )


@dataclass
class RailPricingSolution(TypeRailPricingSolution):
    """
    Contains the fares and segments for a particular offer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"


@dataclass
class RailSolutionChangedInfo:
    """If RetainReservation is None, this will contain the new values returned from
    the provider.

    If RetainReservation is Price, Schedule, or Both and there is a
    price/schedule change, this will contain the new values that were
    returned from the provider.  If RetainReservation is Price,
    Schedule, or Both and there isn’t a price/schedule change, this
    element will not be returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v48_0"

    rail_pricing_solution: None | RailPricingSolution = field(
        default=None,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    reason_code: None | RailSolutionChangedInfoReasonCode = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Attribute",
            "required": True,
        }
    )
