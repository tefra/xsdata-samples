from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.hierarchy_level import HierarchyLevel

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileRetrieveHierarchyRsp(BaseRsp5):
    """
    Response with the requested hierarchy structure.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    hierarchy_level: list[HierarchyLevel] = field(
        default_factory=list,
        metadata={
            "name": "HierarchyLevel",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
