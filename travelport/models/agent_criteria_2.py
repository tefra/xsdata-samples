from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_search_criteria_2 import TypeProfileSearchCriteria2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class AgentCriteria2(TypeProfileSearchCriteria2):
    """
    Agent search modifiers.

    Parameters
    ----------
    username
        Username wild card
    given_name
        Given name wild card
    surname
        Surname wild card
    alternate_agent_id
    """
    class Meta:
        name = "AgentCriteria"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    username: None | str = field(
        default=None,
        metadata={
            "name": "Username",
            "type": "Attribute",
        }
    )
    given_name: None | str = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
        }
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
        }
    )
    alternate_agent_id: None | str = field(
        default=None,
        metadata={
            "name": "AlternateAgentID",
            "type": "Attribute",
            "max_length": 128,
        }
    )
