from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.meta_data_2 import MetaData2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class MetaDataUpdate:
    """
    Command to update profile data information.
    """

    class Meta:
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
