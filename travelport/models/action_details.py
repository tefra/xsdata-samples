from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlTime

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ActionDetails:
    """
    Information related to the storing of the fare: Agent, Date and Action
    for Provider: 1P.

    Parameters
    ----------
    pseudo_city_code
        PCC in the host of the agent who stored the fare for Provider: 1P
    agent_sine
        The sign in of the user who stored the fare for Provider: 1P
    event_date
        Date at which the fare was stored for Provider: 1P
    event_time
        Time at which the fare was stored for Provider: 1P
    text
        The type of action the agent performed for Provider: 1P
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
    agent_sine: None | str = field(
        default=None,
        metadata={
            "name": "AgentSine",
            "type": "Attribute",
        },
    )
    event_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EventDate",
            "type": "Attribute",
        },
    )
    event_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "EventTime",
            "type": "Attribute",
        },
    )
    text: None | str = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        },
    )
