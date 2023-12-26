from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_key_element_2 import TypeKeyElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CommissionReference2(TypeKeyElement2):
    """Data refering to an external or internal Agent who receives commission with
    relation to this profile.

    Agent Name or Number is required.

    Parameters
    ----------
    agent_name
        Name of the agent.
    agent_number
        Number or code identifying the agent.
    priority_order
        Priority of this commission reference item.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """

    class Meta:
        name = "CommissionReference"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agent_name: None | str = field(
        default=None,
        metadata={
            "name": "AgentName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    agent_number: None | str = field(
        default=None,
        metadata={
            "name": "AgentNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        },
    )
