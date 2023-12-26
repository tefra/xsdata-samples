from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.meta_data_details import MetaDataDetails

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class MetaData2:
    """
    An element created under the service which will store all settings for the
    selected profile.

    Parameters
    ----------
    meta_data_details
    user_type
        This attribute will capture which view (say, Agency or Traveler) is
        called for.
    """

    class Meta:
        name = "MetaData"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    meta_data_details: list[MetaDataDetails] = field(
        default_factory=list,
        metadata={
            "name": "MetaDataDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )
    user_type: None | str = field(
        default=None,
        metadata={
            "name": "UserType",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        },
    )
