from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.display_details import DisplayDetails

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class ProviderReservationDisplayDetailsRsp(BaseRsp1):
    """
    Response to display the addtional details of provider reservation
    information .
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    display_details: list[DisplayDetails] = field(
        default_factory=list,
        metadata={
            "name": "DisplayDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
