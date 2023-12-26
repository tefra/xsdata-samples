from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class Name5:
    """
    Complete name fields.

    Parameters
    ----------
    prefix
        Name prefix. Size can be up to 20 characters
    first
        First Name. Size can be up to 256 characters
    middle
        Midle name. Size can be up to 256 characters
    last
        Last Name. Size can be up to 256 characters
    suffix
        Name suffix. Size can be up to 256 characters
    traveler_profile_id
        Traveler Applied Profile ID.
    """

    class Meta:
        name = "Name"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    prefix: None | str = field(
        default=None,
        metadata={
            "name": "Prefix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        },
    )
    first: None | str = field(
        default=None,
        metadata={
            "name": "First",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    middle: None | str = field(
        default=None,
        metadata={
            "name": "Middle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        },
    )
    last: None | str = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    suffix: None | str = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        },
    )
    traveler_profile_id: None | int = field(
        default=None,
        metadata={
            "name": "TravelerProfileId",
            "type": "Attribute",
        },
    )
