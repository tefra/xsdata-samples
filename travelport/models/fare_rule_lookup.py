from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.account_code_1 import AccountCode1
from travelport.models.point_of_sale_1 import PointOfSale1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRuleLookup:
    """
    Parameters to use for a fare rule lookup that is not associated with an Air
    Reservation Locator Code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    account_code: None | AccountCode1 = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    point_of_sale: None | PointOfSale1 = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
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
    departure_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        }
    )
    ticketing_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TicketingDate",
            "type": "Attribute",
        }
    )
