from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ActionSummary:
    """
    Action Summary.

    Parameters
    ----------
    id
        Action Unique ID.
    name
        Action Name.
    description
        Action Description.
    consuming_system
        Action Consuming System (Universal Desktop, 3rd party system).
    target_service
        Action Target Service (Web Service name or page name that the data
        will be utilized).
    profile_action_code
        Profile Action Code description.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: int = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    consuming_system: str = field(
        metadata={
            "name": "ConsumingSystem",
            "type": "Attribute",
            "required": True,
        }
    )
    target_service: str = field(
        metadata={
            "name": "TargetService",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_action_code: str = field(
        metadata={
            "name": "ProfileActionCode",
            "type": "Attribute",
            "required": True,
        }
    )
