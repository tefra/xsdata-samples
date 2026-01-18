from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from travelport.models.provider_reservation_details import (
    ProviderReservationDetails,
)
from travelport.models.provider_reservation_display_details_list import (
    ProviderReservationDisplayDetailsList,
)
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class ProviderReservationInfo:
    """
    Provider Reservation informations.

    Parameters
    ----------
    provider_reservation_details
    provider_reservation_display_details_list
    key
        Key value of the provider reservation
    provider_code
        Contains the Provider Code of the entity housing the actual
        reservation in the event this is a passive one.
    locator_code
        Contains the Locator Code of the actual reservation in the event
        this is a passive reservation.
    create_date
        The date and time that this reservation was created.
    host_create_date
        The date that this reservation was created in the host system.
    host_create_time
        The Time that this reservation was created in the host system for
        1P.
    modified_date
        The date and time that this reservation was last modified for any
        reason.
    imported
        Identifies a reservation that was originally created elsewhere and
        imported into a Universal Record.
    ticketing_modifiers_ref
        Reference to a Ticketing Modifers which is attached to this PNR.
        Ticketing Modifers referred  by this Key is a Primary Ticketing
        Modifers. Worldspan Primary DI line will be supported using this
        feature.
    in_queue_mode
        Identifies whether the gds pnr is being processed from the GDS
        queue.
    group_ref
        Represents a traveler group for Group booking and all their
        accompanying data. SUPPORTED PROVIDER: Worldspan.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    owning_pcc
        Indentifies the owning PCC of the PNR. PROVIDER SUPPORTED:
        Worldspan,Galileo and Apollo
    agent_override
        AgentSine value that was used during PNR creation or End Transact.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    provider_reservation_details: None | ProviderReservationDetails = field(
        default=None,
        metadata={
            "name": "ProviderReservationDetails",
            "type": "Element",
        },
    )
    provider_reservation_display_details_list: (
        None | ProviderReservationDisplayDetailsList
    ) = field(
        default=None,
        metadata={
            "name": "ProviderReservationDisplayDetailsList",
            "type": "Element",
        },
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    locator_code: str = field(
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    create_date: XmlDateTime = field(
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
            "required": True,
        }
    )
    host_create_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "HostCreateDate",
            "type": "Attribute",
        },
    )
    host_create_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "HostCreateTime",
            "type": "Attribute",
        },
    )
    modified_date: XmlDateTime = field(
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        }
    )
    imported: None | bool = field(
        default=None,
        metadata={
            "name": "Imported",
            "type": "Attribute",
        },
    )
    ticketing_modifiers_ref: None | str = field(
        default=None,
        metadata={
            "name": "TicketingModifiersRef",
            "type": "Attribute",
        },
    )
    in_queue_mode: None | bool = field(
        default=None,
        metadata={
            "name": "InQueueMode",
            "type": "Attribute",
        },
    )
    group_ref: None | str = field(
        default=None,
        metadata={
            "name": "GroupRef",
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
    owning_pcc: None | str = field(
        default=None,
        metadata={
            "name": "OwningPCC",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
    agent_override: None | str = field(
        default=None,
        metadata={
            "name": "AgentOverride",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
