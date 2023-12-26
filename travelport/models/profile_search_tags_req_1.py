from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_2 import BaseReq2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileSearchTagsReq1(BaseReq2):
    """
    Request to retrieve tags for an agency.

    Parameters
    ----------
    agency_id
        The ID of the agency that the tags belong to.
    """

    class Meta:
        name = "ProfileSearchTagsReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    agency_id: None | int = field(
        default=None,
        metadata={
            "name": "AgencyID",
            "type": "Attribute",
            "required": True,
        },
    )
