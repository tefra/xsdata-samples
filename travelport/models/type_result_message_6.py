from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_result_message_type_6 import TypeResultMessageType6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class TypeResultMessage6:
    """
    Used to identify the results of a requests.

    Parameters
    ----------
    value
    code
    type_value
        Indicates the type of message (Warning, Error, Info)
    """
    class Meta:
        name = "typeResultMessage"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code: None | int = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | TypeResultMessageType6 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
