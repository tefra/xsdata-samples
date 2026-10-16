from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeRateGuarantee(StrEnum):
    """
    The guarantee for this rate.
    """

    RATE_GUARANTEED = "Rate Guaranteed"
    RATE_QUOTED = "Rate Quoted"
    AGENT_ENTERED = "Agent Entered"
