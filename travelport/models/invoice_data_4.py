from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.booking_traveler_information_4 import (
    BookingTravelerInformation4,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class InvoiceData4:
    """
    List of invoices only for 1G/1V.

    Parameters
    ----------
    booking_traveler_information
    key
    invoice_number
        Invoice number
    issue_date
        Invoice issue date
    provider_reservation_info_ref
        Provider reservation reference key.
    """

    class Meta:
        name = "InvoiceData"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    booking_traveler_information: list[BookingTravelerInformation4] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerInformation",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    invoice_number: None | str = field(
        default=None,
        metadata={
            "name": "InvoiceNumber",
            "type": "Attribute",
            "required": True,
        },
    )
    issue_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Attribute",
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
            "required": True,
        },
    )
