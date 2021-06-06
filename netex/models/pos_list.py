from dataclasses import dataclass
from .direct_position_list_type import DirectPositionListType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PosList(DirectPositionListType):
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml/3.2"
