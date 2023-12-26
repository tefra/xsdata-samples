from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/passive_v52_0"


@dataclass
class PassiveRemark:
    """
    Parameters
    ----------
    text
    type_value
    passive_segment_ref
        The Passive Segment key that this remark refers to.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/passive_v52_0"

    text: None | str = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    passive_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Attribute",
            "required": True,
        },
    )
