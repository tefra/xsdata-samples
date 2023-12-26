from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_2 import BaseReq2
from travelport.models.modify_tag_1 import ModifyTag1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileModifyTagsReq1(BaseReq2):
    """
    Request to modify tags for an agency.
    """

    class Meta:
        name = "ProfileModifyTagsReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    modify_tag: list[ModifyTag1] = field(
        default_factory=list,
        metadata={
            "name": "ModifyTag",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        },
    )
