from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_2 import BaseRsp2
from travelport.models.tag_1 import Tag1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileCreateTagsRsp1(BaseRsp2):
    """
    Response with all the tags for the agency.

    Parameters
    ----------
    tag
        A tag that belongs to the agency.
    """

    class Meta:
        name = "ProfileCreateTagsRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    tag: list[Tag1] = field(
        default_factory=list,
        metadata={
            "name": "Tag",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        },
    )
