from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.action_status_type_4 import ActionStatusType4
from travelport.models.remark_5 import Remark5
from travelport.models.type_element_status_5 import TypeElementStatus5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class ActionStatus4:
    """Status of the action that will happen or has happened to the air
    reservation.

    One Action status for each provider reservation

    Parameters
    ----------
    remark
    type_value
        Identifies the type of action (if any) to take on this air
        reservation. Only TTL, TAU, TAX and TAW can be set by the user.
    ticket_date
        Identifies when the action type will happen, or has happened
        according to the type.
    key
        Identifies when the action type will happen, or has happened
        according to the type.
    provider_reservation_info_ref
        Provider reservation reference key.
    queue_category
        Add Category placement to ticketing queue (required in 1P - default
        is 00)
    airport_code
        Used with Time Limit to specify the airport location where the
        ticket is to be issued.
    provider_code
    supplier_code
    pseudo_city_code
        The Branch PCC in the host system where PNR can be queued for
        ticketing. When used with TAU it will auto queue to Q10. When used
        with TAW agent performs manual move to Q.
    account_code
        Used with TAW. Used to specify a corporate or in house account code
        to the PNR as part of ticketing arrangement field.
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
        name = "ActionStatus"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    remark: None | Remark5 = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
        },
    )
    type_value: None | ActionStatusType4 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    ticket_date: None | str = field(
        default=None,
        metadata={
            "name": "TicketDate",
            "type": "Attribute",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    queue_category: None | str = field(
        default=None,
        metadata={
            "name": "QueueCategory",
            "type": "Attribute",
            "min_length": 1,
            "white_space": "collapse",
        },
    )
    airport_code: None | str = field(
        default=None,
        metadata={
            "name": "AirportCode",
            "type": "Attribute",
            "length": 3,
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
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
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
    account_code: None | str = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus5 = field(
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
