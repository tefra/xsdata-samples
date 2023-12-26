from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.keyword_1 import Keyword1
from travelport.models.permitted_providers_1 import PermittedProviders1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelKeywordReq(BaseReq1):
    """
    Request to retrieve the hotel keyword details of a hotel chain or property.

    Parameters
    ----------
    keyword
        Used to request specific keyword details.
    permitted_providers
    hotel_chain
    hotel_code
    checkin_date
    return_keyword_list
        When true, a list of keyword names should be returned. If false then
        list of keyword details should be returned
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    keyword: list[Keyword1] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 15,
        },
    )
    permitted_providers: None | PermittedProviders1 = field(
        default=None,
        metadata={
            "name": "PermittedProviders",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    hotel_chain: None | str = field(
        default=None,
        metadata={
            "name": "HotelChain",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
    hotel_code: None | str = field(
        default=None,
        metadata={
            "name": "HotelCode",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    checkin_date: None | str = field(
        default=None,
        metadata={
            "name": "CheckinDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        },
    )
    return_keyword_list: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnKeywordList",
            "type": "Attribute",
        },
    )
