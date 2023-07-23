from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.delivery_info_5 import DeliveryInfo5
from travelport.models.phone_number_6 import PhoneNumber6
from travelport.models.type_element_status_6 import TypeElementStatus6
from travelport.models.type_structured_address_6 import TypeStructuredAddress6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class Group5:
    """Represents a traveler group for Group booking and all their accompanying
    data.

    SUPPORTED PROVIDER: Worldspan and JAL.

    Parameters
    ----------
    name
        Name of the group in group booking.
    delivery_info
    phone_number
    ssrref
        Reference Element for SSR.
    address
    booking_traveler_ref
        Reference Element for Booking Traveler.
    key
    traveler_type
        Defines the type of traveler used for booking which could be a non-
        defining type (Companion, Web-fare, etc), or a standard type (Adult,
        Child, etc).
    group_size
        Represents size of the group
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
        name = "Group"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    delivery_info: None | DeliveryInfo5 = field(
        default=None,
        metadata={
            "name": "DeliveryInfo",
            "type": "Element",
        }
    )
    phone_number: list[PhoneNumber6] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ssrref: list[Group5.Ssrref] = field(
        default_factory=list,
        metadata={
            "name": "SSRRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    address: None | TypeStructuredAddress6 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    booking_traveler_ref: list[Group5.BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    traveler_type: None | str = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    group_size: None | int = field(
        default=None,
        metadata={
            "name": "GroupSize",
            "type": "Attribute",
            "required": True,
        }
    )
    el_stat: None | TypeElementStatus6 = field(
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
    class Ssrref:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class BookingTravelerRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )
