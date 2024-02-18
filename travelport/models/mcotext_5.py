from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_free_form_text_5 import TypeFreeFormText5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class Mcotext5(TypeFreeFormText5):
    """All type of free format text messages related to MCO like - Command Text, Agent Entry, MCO Modifiers, Text Message

    Parameters
    ----------
    type_value
        The type of text. Possible values: Command Text, Agent Entry, MCO
        Modifiers, Text Message
    """

    class Meta:
        name = "MCOText"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
