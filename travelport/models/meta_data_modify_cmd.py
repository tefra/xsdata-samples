from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.meta_data_add import MetaDataAdd
from travelport.models.meta_data_delete import MetaDataDelete
from travelport.models.meta_data_update import MetaDataUpdate

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class MetaDataModifyCmd:
    """
    Wrapper for a set of modification commands to be applied to this profile.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    meta_data_add: None | MetaDataAdd = field(
        default=None,
        metadata={
            "name": "MetaDataAdd",
            "type": "Element",
        }
    )
    meta_data_update: None | MetaDataUpdate = field(
        default=None,
        metadata={
            "name": "MetaDataUpdate",
            "type": "Element",
        }
    )
    meta_data_delete: None | MetaDataDelete = field(
        default=None,
        metadata={
            "name": "MetaDataDelete",
            "type": "Element",
        }
    )
