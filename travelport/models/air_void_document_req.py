from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_reservation_locator_code import (
    AirReservationLocatorCode,
)
from travelport.models.base_req_1 import BaseReq1
from travelport.models.void_document_info import VoidDocumentInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirVoidDocumentReq(BaseReq1):
    """
    Request to void all previously issued tickets for the PNR.

    Parameters
    ----------
    air_reservation_locator_code
        Provider: 1G,1V.
    void_document_info
        Provider: 1G,1V-All tickets that belong to this PNR must be
        enumerated here. Voiding only some tickets of a multi-ticket PNR not
        currently supported.
    show_etr
        Provider: 1G,1V-If set as true, response will display the detailed
        ETR for successfully voided E-Tickets.
    provider_code
        Provider: 1G,1V-Provider code of a specific host.
    provider_locator_code
        Provider: 1G,1V-Contains the locator of the host reservation.
    validate_spanish_residency
        Provider: 1G - If set as true, Spanish Residency will be validated
        for Provisioned Customers.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: None | AirReservationLocatorCode = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
        },
    )
    void_document_info: list[VoidDocumentInfo] = field(
        default_factory=list,
        metadata={
            "name": "VoidDocumentInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    show_etr: bool = field(
        default=False,
        metadata={
            "name": "ShowETR",
            "type": "Attribute",
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
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
        },
    )
    validate_spanish_residency: bool = field(
        default=False,
        metadata={
            "name": "ValidateSpanishResidency",
            "type": "Attribute",
        },
    )
