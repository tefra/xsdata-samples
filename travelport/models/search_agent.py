from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SearchAgent:
    """
    Search restriction by Agent.

    Parameters
    ----------
    branch_id
    created_by_agent
        The Agent ID that created a PNR.
    modified_by_agent
        The Agent ID that modified a PNR last.
    ticketed_by_agent
        The Agent ID that ticketed a PNR.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    branch_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BranchId",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    created_by_agent: None | str = field(
        default=None,
        metadata={
            "name": "CreatedByAgent",
            "type": "Attribute",
        }
    )
    modified_by_agent: None | str = field(
        default=None,
        metadata={
            "name": "ModifiedByAgent",
            "type": "Attribute",
        }
    )
    ticketed_by_agent: None | str = field(
        default=None,
        metadata={
            "name": "TicketedByAgent",
            "type": "Attribute",
        }
    )
