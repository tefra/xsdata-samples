from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class DocumentModifiers:
    """
    Parameters
    ----------
    generate_itinerary_invoice
        Generate itinerary/invoice documents along with ticket
    generate_accounting_interface
        Generate interface message along with ticket
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    generate_itinerary_invoice: bool = field(
        default=False,
        metadata={
            "name": "GenerateItineraryInvoice",
            "type": "Attribute",
        },
    )
    generate_accounting_interface: bool = field(
        default=False,
        metadata={
            "name": "GenerateAccountingInterface",
            "type": "Attribute",
        },
    )
