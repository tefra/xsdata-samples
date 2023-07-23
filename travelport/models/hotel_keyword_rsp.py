from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.keyword_1 import Keyword1
from travelport.models.marketing_information_1 import MarketingInformation1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelKeywordRsp(BaseRsp1):
    """
    Response showing keyword details of a given hotel chain or property.

    Parameters
    ----------
    marketing_information
    keyword
        A word that a vendor uses to describe corporate policy/information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    marketing_information: None | MarketingInformation1 = field(
        default=None,
        metadata={
            "name": "MarketingInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    keyword: list[Keyword1] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
