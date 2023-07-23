from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeProfileInfo2:
    """
    Base type for Profile Infos.

    Parameters
    ----------
    additional_identifier
        Additional identifier managed by an external system.
    description
    """
    class Meta:
        name = "typeProfileInfo"

    additional_identifier: None | str = field(
        default=None,
        metadata={
            "name": "AdditionalIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
