from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_result_message_type_2 import TypeResultMessageType2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class TypeResultMessage2:
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
        },
    )
    code: int = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | TypeResultMessageType2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
