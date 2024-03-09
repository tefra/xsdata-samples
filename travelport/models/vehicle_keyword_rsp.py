from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.keyword_1 import Keyword1

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleKeywordRsp(BaseRsp1):
    """
    Used to respond with a list of keywords or specific keyword information.

    Parameters
    ----------
    text
        Information for this vendor not related to a keyword.
    keyword
        A word that a vendor uses to describe corporate policy/information.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    keyword: list[Keyword1] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
