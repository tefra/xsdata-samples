from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.reference_data_search_item import (
    ReferenceDataSearchItem,
)
from travelport.models.reference_data_search_modifiers import (
    ReferenceDataSearchModifiers,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class ReferenceDataSearchReq(BaseReq1):
    """
    Request to lookup a specific reference data item.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    reference_data_search_modifiers: None | ReferenceDataSearchModifiers = (
        field(
            default=None,
            metadata={
                "name": "ReferenceDataSearchModifiers",
                "type": "Element",
            },
        )
    )
    reference_data_search_item: list[ReferenceDataSearchItem] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceDataSearchItem",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
