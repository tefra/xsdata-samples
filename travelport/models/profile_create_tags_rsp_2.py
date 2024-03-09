from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.tag_2 import Tag2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileCreateTagsRsp2(BaseRsp5):
    """
    Response with all the tags for the agency.

    Parameters
    ----------
    tag
        A tag that belongs to the agency.
    """

    class Meta:
        name = "ProfileCreateTagsRsp"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    tag: list[Tag2] = field(
        default_factory=list,
        metadata={
            "name": "Tag",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        },
    )
