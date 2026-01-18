from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/passive_v52_0"


@dataclass(kw_only=True)
class PassiveSegmentRef:
    """
    Parameters
    ----------
    key
        The Key of Passive Segment.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/passive_v52_0"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
