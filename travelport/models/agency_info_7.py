from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.agent_action_5 import AgentAction5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class AgencyInfo7:
    """
    Tracks the various agent/agency information.
    """

    class Meta:
        name = "AgencyInfo"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    agent_action: list[AgentAction5] = field(
        default_factory=list,
        metadata={
            "name": "AgentAction",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
