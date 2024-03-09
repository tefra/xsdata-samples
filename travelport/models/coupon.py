from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.ticket_designator import TicketDesignator
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Coupon:
    """
    The flight coupon that resulted from the ticketing operation.

    Parameters
    ----------
    ticket_designator
    key
    coupon_number
        The sequential number of this coupon.
    operating_carrier
        The true carrier.
    operating_flight_number
        The true carrier's flight number.
    marketing_carrier
        If codeshare applies to this, this is the marketing carrier (as
        opposed to the operating carrier).
    marketing_flight_number
        If codeshare applies to this, this is the marketing flight number
        (as opposed to the operating flight number).
    origin
        Returns the airport or city code that defines the origin market for
        this fare.
    destination
        Returns the airport or city code that defines the destination market
        for this fare.
    departure_time
        The date and time at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location. In case of open segment this will not be returned.
    arrival_time
        The date and time at which this entity arrives at the destination.
        This does not include time zone information since it can be derived
        from the origin location.
    stopover_code
        Stopover code - indicator that stopover is allowed at Origin Airport
        or City.
    booking_class
        Booked fare class for coupon.
    fare_basis
        The fare basis code for this fare
    not_valid_before
        Fare not valid before this date.
    not_valid_after
        Fare not valid after this date.
    status
        The status of this coupon returend from host is mapped as follows
        Code="A" Status="Airport Controlled" Code="C" Status="Checked In"
        Code="F" Status="Flown/Used" Code="L" Status="Boarded/Lifted"
        Code="O" Status="Open" Code="P" Status="Printed" Code="R"
        Status="Refunded" Code="E" Status="Exchanged" Code="V" Status="Void"
        Code="Z" Status="Archived/Carrier Modified" Code="U"
        Status="Unavailable" Code="S" Status="Suspended" Code="I"
        Status="Irregular Ops" Code="D" Status="Deleted/Removed" Code="X"
        Status="Unknown"
    segment_group
        Indicates the grouping in which this segment resides based on
        Origin/Destination pairs in itinerary
    marriage_group
        Airline Marrraige group indicator
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
        namespace = "http://www.travelport.com/schema/air_v52_0"

    ticket_designator: list[TicketDesignator] = field(
        default_factory=list,
        metadata={
            "name": "TicketDesignator",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    coupon_number: None | int = field(
        default=None,
        metadata={
            "name": "CouponNumber",
            "type": "Attribute",
        },
    )
    operating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    operating_flight_number: None | str = field(
        default=None,
        metadata={
            "name": "OperatingFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        },
    )
    marketing_carrier: None | str = field(
        default=None,
        metadata={
            "name": "MarketingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    marketing_flight_number: None | str = field(
        default=None,
        metadata={
            "name": "MarketingFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    departure_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        },
    )
    arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        },
    )
    stopover_code: None | bool = field(
        default=None,
        metadata={
            "name": "StopoverCode",
            "type": "Attribute",
            "required": True,
        },
    )
    booking_class: None | str = field(
        default=None,
        metadata={
            "name": "BookingClass",
            "type": "Attribute",
            "required": True,
            "max_length": 2,
        },
    )
    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
        },
    )
    not_valid_before: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        },
    )
    not_valid_after: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
            "max_length": 1,
        },
    )
    segment_group: None | int = field(
        default=None,
        metadata={
            "name": "SegmentGroup",
            "type": "Attribute",
        },
    )
    marriage_group: None | int = field(
        default=None,
        metadata={
            "name": "MarriageGroup",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
