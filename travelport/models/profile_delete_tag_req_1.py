from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_2 import BaseReq2
from travelport.models.tag_ref_1 import TagRef1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileDeleteTagReq1(BaseReq2):
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    tag_ref: None | TagRef1 = field(
        default=None,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "required": True,
        }
    )
    override: bool = field(
        default=False,
        metadata={
            "name": "Override",
            "type": "Attribute",
        }
    )
