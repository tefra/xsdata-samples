from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.amount_type import AmountType
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/passive_v52_0"


@dataclass
class PassiveSegment:
    """
    Parameters
    ----------
    amount
    supplier_code
        Vendor Code. This could have values outside what is defined as a
        carrier. (eg:ZZ as in case for vendor in case of Due paid)
    status
    start_date
    end_date
    origin
        Origin for Air, but City for all other Types.
    destination
        This optional, except when Type is Air, then it is required.
    availability_source
        Indicates Availability source of AirSegment.
    polled_availability_option
        Indicates if carrier has inside(polled) availability option.
    availability_display_type
        The type of availability from which the segment is sold. E.g.,
        General, Carrier Specific/Direct Access, Fare Shop/Optimal Shop,
        etc.
    flight_number
    class_of_service
    number_of_items
    segment_type
        The Type of Passive segment being entered (
        Car,Hotel,Tour,Air,Surface,Bus,Rail,Cruise,Helicopter,Limousine,Transfers,Miscellaneous,ProcessingFee,Insurance,
        AirTaxi,Currency,Fees,Forms,Group,Include,Leisure,Land,Other,Package,RailRoad,SeaPlane,Software,Supply,Service,
        Theater,Ticket,Transfer,Taxi,Charter,CorporatePlane,UnitedPassive,AccountingInfo,BookingFee,ServiceCharge,ServiceFee,TicketFees
        ,TelexCharge)
    key
        The Key of Passive Segment.
    vehicle_type
        The Type of Vehicle in Passive Segment.
    passive_provider_reservation_info_ref
        Passive Provider Reservation reference key.
    group
        Unique Identifier used for grouping together identical segments.
    travel_order
        To identify the appropriate travel sequence for
        Air/Car/Hotel/Passive segments/reservations based on travel dates.
        This ordering is applicable across the UR not provider or traveler
        specific
    provider_segment_order
        To identify the appropriate travel sequence for Air/Car/Hotel/Rail
        segments/reservations in the provider reservation.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    passive_group
        Used for grouping 2 sets of identical passive segments with
        different remark information.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/passive_v52_0"

    amount: None | PassiveSegment.Amount = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 20,
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        },
    )
    start_date: None | str = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        },
    )
    end_date: None | str = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    availability_source: None | str = field(
        default=None,
        metadata={
            "name": "AvailabilitySource",
            "type": "Attribute",
        },
    )
    polled_availability_option: None | str = field(
        default=None,
        metadata={
            "name": "PolledAvailabilityOption",
            "type": "Attribute",
        },
    )
    availability_display_type: None | str = field(
        default=None,
        metadata={
            "name": "AvailabilityDisplayType",
            "type": "Attribute",
        },
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
        },
    )
    class_of_service: None | str = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
        },
    )
    number_of_items: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfItems",
            "type": "Attribute",
        },
    )
    segment_type: None | str = field(
        default=None,
        metadata={
            "name": "SegmentType",
            "type": "Attribute",
            "required": True,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    vehicle_type: None | str = field(
        default=None,
        metadata={
            "name": "VehicleType",
            "type": "Attribute",
        },
    )
    passive_provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    group: None | int = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Attribute",
        },
    )
    travel_order: None | int = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        },
    )
    provider_segment_order: None | int = field(
        default=None,
        metadata={
            "name": "ProviderSegmentOrder",
            "type": "Attribute",
            "max_inclusive": 999,
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
    passive_group: None | str = field(
        default=None,
        metadata={
            "name": "PassiveGroup",
            "type": "Attribute",
        },
    )

    @dataclass
    class Amount:
        type_value: None | AmountType = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            },
        )
        amount_due_paid: None | str = field(
            default=None,
            metadata={
                "name": "AmountDuePaid",
                "type": "Attribute",
            },
        )
