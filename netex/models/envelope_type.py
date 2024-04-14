from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .direct_position_type import DirectPositionType
from .pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EnvelopeType:
    lower_corner_or_upper_corner_or_pos: List[
        Union["EnvelopeType.LowerCorner", "EnvelopeType.UpperCorner", Pos]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "lowerCorner",
                    "type": ForwardRef("EnvelopeType.LowerCorner"),
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "upperCorner",
                    "type": ForwardRef("EnvelopeType.UpperCorner"),
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "pos",
                    "type": Pos,
                    "namespace": "http://www.opengis.net/gml/3.2",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )

    @dataclass
    class LowerCorner(DirectPositionType):
        pass

    @dataclass
    class UpperCorner(DirectPositionType):
        pass
