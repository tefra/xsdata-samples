from dataclasses import dataclass

from .direct_position_type import DirectPositionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class VectorType(DirectPositionType):
    pass
