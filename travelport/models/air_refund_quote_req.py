from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_refund_modifiers import AirRefundModifiers
from travelport.models.base_req_1 import BaseReq1
from travelport.models.host_token_1 import HostToken1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirRefundQuoteReq(BaseReq1):
    """
    Request to quote a refund for an itinerary.

    Parameters
    ----------
    ticket_number
        Provider: ACH.
    tcrnumber
        Provider: ACH-The identifying number for a Ticketless Air
        Reservation
    air_refund_modifiers
        Provider: ACH.
    host_token
        Provider: ACH.
    provider_reservation_info
        Provider: 1P - Represents a valid Provider Reservation/PNR whose
        itinerary is to be requested
    ignore
        Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    ticket_number: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 13,
        }
    )
    tcrnumber: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TCRNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_refund_modifiers: None | AirRefundModifiers = field(
        default=None,
        metadata={
            "name": "AirRefundModifiers",
            "type": "Element",
        }
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    provider_reservation_info: list[AirRefundQuoteReq.ProviderReservationInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ignore: bool = field(
        default=False,
        metadata={
            "name": "Ignore",
            "type": "Attribute",
        }
    )

    @dataclass
    class ProviderReservationInfo:
        """
        Parameters
        ----------
        provider_code
        provider_locator_code
        supplier_code
            Represents Carrier Code for ACH PNR Retrieve.
        """
        provider_code: None | str = field(
            default=None,
            metadata={
                "name": "ProviderCode",
                "type": "Attribute",
                "required": True,
                "min_length": 2,
                "max_length": 5,
            }
        )
        provider_locator_code: None | str = field(
            default=None,
            metadata={
                "name": "ProviderLocatorCode",
                "type": "Attribute",
                "required": True,
                "max_length": 15,
            }
        )
        supplier_code: None | str = field(
            default=None,
            metadata={
                "name": "SupplierCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 5,
            }
        )
