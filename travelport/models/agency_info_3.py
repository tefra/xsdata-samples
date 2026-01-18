from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.agent_action_2 import AgentAction2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class AgencyInfo3:
    """
    Tracks the various agent/agency information.
    """

    class Meta:
        name = "AgencyInfo"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    agent_action: list[AgentAction2] = field(
        default_factory=list,
        metadata={
            "name": "AgentAction",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
