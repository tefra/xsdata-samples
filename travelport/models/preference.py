from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.preference_owner import PreferenceOwner

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class Preference:
    """
    Preferences of the segment related to the profile (Agent, Branch, etc.).
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    owner: None | PreferenceOwner = field(
        default=None,
        metadata={
            "name": "Owner",
            "type": "Attribute",
            "required": True,
        },
    )
