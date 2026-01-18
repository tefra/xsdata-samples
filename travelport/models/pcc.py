from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.override_pcc_1 import OverridePcc1
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.ticket_agency import TicketAgency

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Pcc:
    """
    Specify pseudo City.
    """

    class Meta:
        name = "PCC"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    override_pcc: None | OverridePcc1 = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    point_of_sale: list[PointOfSale1] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        },
    )
    ticket_agency: None | TicketAgency = field(
        default=None,
        metadata={
            "name": "TicketAgency",
            "type": "Element",
        },
    )
