from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.hierarchy_level import HierarchyLevel

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileDeleteHierarchyLevelRsp(BaseRsp5):
    """
    Response with the updated hierarchy structure.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    hierarchy_level: list[HierarchyLevel] = field(
        default_factory=list,
        metadata={
            "name": "HierarchyLevel",
            "type": "Element",
            "max_occurs": 999,
        }
    )
