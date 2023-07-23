from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class Mcotext6:
    """All type of free format text messages related to MCO like - Command Text, Agent Entry, MCO Modifiers, Text Message

    Parameters
    ----------
    value
    type_value
        The type of text. Possible values: Command Text, Agent Entry, MCO
        Modifiers, Text Message
    """
    class Meta:
        name = "MCOText"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
