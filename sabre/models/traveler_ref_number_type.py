from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class TravelerRefNumberType:
    """
    A reference place holder used as a pointer to link back to the
    traveler.

    Attributes:
        rph: Reference place holder.
    """

    rph: None | str = field(
        default=None,
        metadata={
            "name": "RPH",
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}",
        },
    )
