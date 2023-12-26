from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.reference_data_item import ReferenceDataItem

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class ReferenceDataRetrieveRsp(BaseRsp1):
    """
    Response to retrieve code, name and description for a specific reference data
    type.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    reference_data_item: list[ReferenceDataItem] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceDataItem",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    more_results: None | bool = field(
        default=None,
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        },
    )
