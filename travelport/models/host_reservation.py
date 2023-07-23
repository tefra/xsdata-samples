from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class HostReservation:
    """
    Defines a reservation that already exists in the host system (e.g an agent
    using Galileo Desktop already booked a reservation on Midwest in Sabre host
    system).

    Parameters
    ----------
    carrier
        The carrier code (e.g. YX, UA, ...) that is providing the
        merchandising
    carrier_locator_code
        The locator code in the supplier system (also could be defined as
        locator in the carrier host system).
    provider_code
        Contains the GDS or other provider code of the entity actually
        housing the reservation. This is optional when used on Merchandising
        Availability but required on MerchandisingFulfillment.
    provider_locator_code
        Contains the locator of the reservation actually housed in the
        provider.
    universal_locator_code
        The locator of the Universal Record, if one exists.
    eticket
        An flag to indicate if ticket has been issued for the PNR.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    carrier_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "CarrierLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
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
    universal_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    eticket: bool = field(
        default=False,
        metadata={
            "name": "ETicket",
            "type": "Attribute",
        }
    )
