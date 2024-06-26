from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.commission_9 import Commission9

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class PassiveInfo5:
    """
    Used by CreateReservationReq for passing in elements normally found post-
    booking.
    """

    class Meta:
        name = "PassiveInfo"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    ticket_number: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    confirmation_number: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ConfirmationNumber",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    commission: None | Commission9 = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        },
    )
    supplier_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierLocatorCode",
            "type": "Attribute",
        },
    )
