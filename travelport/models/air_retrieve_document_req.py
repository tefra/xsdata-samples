from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirRetrieveDocumentReq(BaseReq1):
    """Retrieve the post booking information for a PNR.

    ETRs will be returned for standard carriers. TCRs will be returned
    for Ticketless carriers. If the locator is send on a standard
    carrier, all ETRs will be retrieved.

    Parameters
    ----------
    air_reservation_locator_code
        Provider: 1G,1V,1P.
    ticket_number
        Provider: 1G,1V,1P.
    tcrnumber
        Provider: 1G,1V,1P-The identifying number for a Ticketless Air
        Reservation.
    return_restrictions
        Will return a response which includes a set of restrictions
        associated with the document.
    return_pricing
        Provider: 1G,1V,1P-Will return a response which includes the pricing
        associated with the ETR.
    retrieve_mco
        When true, returns MCO Information. The default value is false.
    universal_record_locator_code
        Contains the Locator Code of the Universal Record that houses this
        reservation.
    provider_code
        Contains the Provider Code of the provider that houses this
        reservation.
    provider_locator_code
        Contains the Locator Code of the Provider Reservation that houses
        this reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
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
    return_restrictions: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnRestrictions",
            "type": "Attribute",
        }
    )
    return_pricing: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnPricing",
            "type": "Attribute",
        }
    )
    retrieve_mco: None | bool = field(
        default=None,
        metadata={
            "name": "RetrieveMCO",
            "type": "Attribute",
        }
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
