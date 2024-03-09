from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.proprietary_data_proprietary_data_type_1 import (
    ProprietaryDataProprietaryDataType1,
)
from travelport.models.type_key_element_1 import TypeKeyElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProprietaryData1(TypeKeyElement1):
    """
    ProprietaryData for a Traveler which can be overridden for immediate parent
    like BranchGroup,Branch,Account and TravelerGroup.

    Parameters
    ----------
    proprietary_data_type
        The type of ProprietaryData being overridden for a TravelerProfile.
    value
        The value of ProprietaryData.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """

    class Meta:
        name = "ProprietaryData"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    proprietary_data_type: None | ProprietaryDataProprietaryDataType1 = field(
        default=None,
        metadata={
            "name": "ProprietaryDataType",
            "type": "Attribute",
            "required": True,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
            "required": True,
        },
    )
