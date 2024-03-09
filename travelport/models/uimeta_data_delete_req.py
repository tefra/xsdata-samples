from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_2 import BaseReq2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class UimetaDataDeleteReq(BaseReq2):
    """
    Service for Request to delete any settings by user in Profile Settings.

    Parameters
    ----------
    profile_id
        This attribute would pass the ID of the required profile selected
        (say, Agency or Account name) for which the change in settings will
        be done.
    """

    class Meta:
        name = "UIMetaDataDeleteReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "required": True,
        },
    )
