from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.source_type import SourceType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class PosType:
    """
    Point of Sale (POS) is the details identifying the party or connection
    channel making the request.

    Attributes:
        source: This holds details regarding the requestor. It may be
            repeated to also accommodate the delivery systems.
    """

    class Meta:
        name = "POS_Type"

    source: list[SourceType] = field(
        default_factory=list,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
