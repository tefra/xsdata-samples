from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_key_element_1 import TypeKeyElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeCommissionReferenceHistory1(TypeKeyElement1):
    """
    Data refering to an external or internal Agent who recieves commission with
    relation to this profile.

    Parameters
    ----------
    agent_name
    agent_number
    priority_order
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """

    class Meta:
        name = "typeCommissionReferenceHistory"

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
