from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class RoleInfo5:
    """
    Container to specify the role of the agent.

    Parameters
    ----------
    id
        Unique identifier of the role.
    name
        Agent's role name
    source
        Role inheritance level. Needed in the response, not in the request
    description
        Description of role
    """

    class Meta:
        name = "RoleInfo"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
            "max_length": 19,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "max_length": 128,
        }
    )
    source: None | str = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "max_length": 1024,
        },
    )
