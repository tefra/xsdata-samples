from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.pre_pay_profile_info import PrePayProfileInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPrePayRsp(BaseRsp1):
    """
    Flight Pass Response.

    Parameters
    ----------
    pre_pay_profile_info
        Provider: ACH.
    max_results
        Provider: ACH-Max Number of Flight Passes being returned.
    more_indicator
        Provider: ACH-Indicates if there are more flight passes to be
        offered
    more_data_start_index
        Provider: ACH-Indicates start index of the next flight Passes
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    pre_pay_profile_info: list[PrePayProfileInfo] = field(
        default_factory=list,
        metadata={
            "name": "PrePayProfileInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    max_results: None | int = field(
        default=None,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 200,
        },
    )
    more_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "MoreIndicator",
            "type": "Attribute",
        },
    )
    more_data_start_index: None | str = field(
        default=None,
        metadata={
            "name": "MoreDataStartIndex",
            "type": "Attribute",
        },
    )
