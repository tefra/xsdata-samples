from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_5 import BaseReq5
from travelport.models.modify_tag_2 import ModifyTag2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileModifyTagsReq2(BaseReq5):
    """
    Request to modify tags for an agency.
    """
    class Meta:
        name = "ProfileModifyTagsReq"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    modify_tag: list[ModifyTag2] = field(
        default_factory=list,
        metadata={
            "name": "ModifyTag",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        }
    )
