from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.direct_position_type import DirectPositionType
from netex.models.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EnvelopeType:
    lower_corner: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "name": "lowerCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    upper_corner: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "name": "upperCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "max_occurs": 2,
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )
