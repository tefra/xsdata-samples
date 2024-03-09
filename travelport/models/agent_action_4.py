from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

from travelport.models.agent_action_action_type_4 import AgentActionActionType4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class AgentAction4:
    """
    Depending on context, this will represent information about which agent perform
    different actions.

    Parameters
    ----------
    action_type
        The type of action the agent performed.
    agent_code
        The AgenctCode who performed the action.
    branch_code
        The BranchCode of the branch (working branch, branchcode used for
        the request. If nothing specified, branchcode for the agent) who
        performed the action.
    agency_code
        The AgencyCode of the agent who performed the action.
    agent_sine
        The sign in user name of the agent logged into the terminal.
        PROVIDER SUPPORTED: ACH
    event_time
        Date and time at which this event took place.
    agent_override
        AgentSine value that was used during PNR creation or End Transact.
    """

    class Meta:
        name = "AgentAction"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    action_type: None | AgentActionActionType4 = field(
        default=None,
        metadata={
            "name": "ActionType",
            "type": "Attribute",
            "required": True,
        },
    )
    agent_code: None | str = field(
        default=None,
        metadata={
            "name": "AgentCode",
            "type": "Attribute",
            "required": True,
        },
    )
    branch_code: None | str = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )
    agency_code: None | str = field(
        default=None,
        metadata={
            "name": "AgencyCode",
            "type": "Attribute",
            "required": True,
        },
    )
    agent_sine: None | str = field(
        default=None,
        metadata={
            "name": "AgentSine",
            "type": "Attribute",
        },
    )
    event_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "EventTime",
            "type": "Attribute",
            "required": True,
        },
    )
    agent_override: None | str = field(
        default=None,
        metadata={
            "name": "AgentOverride",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
