from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_5 import BaseReq5
from travelport.models.tag_ref_2 import TagRef2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileDeleteTagReq2(BaseReq5):
    """
    Request to delete tags.

    Parameters
    ----------
    tag_ref
        The tag to be deleted
    override
        Indicator to override the delete when the tag is "in use" by
        profiles in the agency.
    """

    class Meta:
        name = "ProfileDeleteTagReq"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    tag_ref: None | TagRef2 = field(
        default=None,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "required": True,
        },
    )
    override: bool = field(
        default=False,
        metadata={
            "name": "Override",
            "type": "Attribute",
        },
    )
