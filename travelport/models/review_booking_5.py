from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

from travelport.models.type_element_status_6 import TypeElementStatus6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class ReviewBooking5:
    """Review Booking or Queue Minders is to add the reminders in the Provider
    Reservation along with the date time and Queue details.

    On the date time defined in reminders, the message along with the
    PNR goes to the desired Queue.

    Parameters
    ----------
    key
        Returned in response. Use it for update of saved review booking.
    queue
        Queue number, Must be numeric and less than 100.
    queue_category
        Queue Category, 2 Character Alpha or Numeric.
    date_time
        Date and Time to place message on designated Queue, Should be prior
        to the last segment date in the PNR.
    pseudo_city_code
        Input PCC optional value for placing the PNR into Queue. If not
        passed, will add as default PNR's Pseudo.
    provider_code
        The code of the Provider (e.g 1G,1V).
    provider_reservation_info_ref
        Provider Reservation reference. Returned in the response. Use it for
        update of saved Review Booking.
    remarks
        Remark or reminder message. It can be truncated depending on the
        provider.
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
        name = "ReviewBooking"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    queue: None | int = field(
        default=None,
        metadata={
            "name": "Queue",
            "type": "Attribute",
            "required": True,
            "max_inclusive": 99,
        },
    )
    queue_category: None | str = field(
        default=None,
        metadata={
            "name": "QueueCategory",
            "type": "Attribute",
            "max_length": 2,
        },
    )
    date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Attribute",
            "required": True,
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    remarks: None | str = field(
        default=None,
        metadata={
            "name": "Remarks",
            "type": "Attribute",
            "required": True,
            "max_length": 300,
        },
    )
    el_stat: None | TypeElementStatus6 = field(
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
