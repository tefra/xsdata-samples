from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_2 import BaseReq2
from travelport.models.meta_data_2 import MetaData2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class UimetaDataCreateReq(BaseReq2):
    """
    Service for Request to create the entry in action by Admin in Admin login view
    in Profile Settings.

    Parameters
    ----------
    meta_data
        An element created under the service which will store all settings
        for the selected profile.
    profile_id
        This attribute would pass the ID of the required profile
        selected(say, Agency or Account name) for which the change in
        setting will be done.
    description
        This optional attribute is for any description if the user wants to
        pass.
    """

    class Meta:
        name = "UIMetaDataCreateReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    meta_data: list[MetaData2] = field(
        default_factory=list,
        metadata={
            "name": "MetaData",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
