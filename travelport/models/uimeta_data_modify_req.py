from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_2 import BaseReq2
from travelport.models.meta_data_modify_cmd import MetaDataModifyCmd

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class UimetaDataModifyReq(BaseReq2):
    """
    Service for Request to modify the entry in action by Admin in Admin login view
    in Profile Settings.

    Parameters
    ----------
    meta_data_modify_cmd
    profile_id
        This attribute would pass the ID of the required profile
        selected(say, Agency or Account name) for which change in the
        settings will be done.
    meta_data_version
        This attribute updates the version of the change or any updates
        done.
    description
        This optional attribute is for any description if the user wants to
        pass.
    """
    class Meta:
        name = "UIMetaDataModifyReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    meta_data_modify_cmd: list[MetaDataModifyCmd] = field(
        default_factory=list,
        metadata={
            "name": "MetaDataModifyCmd",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    meta_data_version: None | int = field(
        default=None,
        metadata={
            "name": "MetaDataVersion",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
