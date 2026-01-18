from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.type_result_message_1 import TypeResultMessage1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class ProviderReservationStatus:
    """
    Status of the cancellation for this provider reservation.

    Parameters
    ----------
    cancel_info
        If the provider reservation was not successfully cancelled or
        cancelled with warnings the provider system might provides some
        textual information describing the reason.
    create_date
        The date and time that this reservation was created.
    modified_date
        The date and time that this reservation was last modified for any
        reason.
    provider_code
        Contains the Provider Code of the entity housing the actual
        reservation in the event this is a passive one.
    locator_code
        Contains the Locator Code of the actual reservation in the event
        this is a passive reservation.
    cancelled
        Will be true if the reservation was successfuly cancelled on the
        provider system.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    cancel_info: None | TypeResultMessage1 = field(
        default=None,
        metadata={
            "name": "CancelInfo",
            "type": "Element",
        },
    )
    create_date: XmlDateTime = field(
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
            "required": True,
        }
    )
    modified_date: XmlDateTime = field(
        metadata={
            "name": "ModifiedDate",
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
    cancelled: bool = field(
        metadata={
            "name": "Cancelled",
            "type": "Attribute",
            "required": True,
        }
    )
