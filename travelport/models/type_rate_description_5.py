from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TypeRateDescription5:
    """
    Parameters
    ----------
    text
    name
        Optional context name of the text block being returned i.e. Room
        details
    """

    class Meta:
        name = "typeRateDescription"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
