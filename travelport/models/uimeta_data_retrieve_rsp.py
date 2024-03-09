from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_2 import BaseRsp2
from travelport.models.meta_data_2 import MetaData2
from travelport.models.type_profile_type_3 import TypeProfileType3

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class UimetaDataRetrieveRsp(BaseRsp2):
    """
    Service for Response to retrieve the settings by user in Profile Settings.

    Parameters
    ----------
    meta_data
        An element created under the service which will store all settings
        for the selected profile.
    profile_id
        This Profile Id would get the ID of the Agency/Account name for
        which the change is done. Hence all the applicable changes would be
        done for this particular agency/account.
    profile_type
        This will retrieve the type of the Profile for which the change is
        triggered, say Agency , Account, etc.
    meta_data_version
        This attribute updates the version of the change or any updates
        done.
    description
        This optional attribute is for any description if the user wants to
        pass.
    """

    class Meta:
        name = "UIMetaDataRetrieveRsp"
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
    profile_type: None | TypeProfileType3 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        },
    )
    meta_data_version: None | int = field(
        default=None,
        metadata={
            "name": "MetaDataVersion",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
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
