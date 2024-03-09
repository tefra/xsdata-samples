from dataclasses import dataclass

from .boarding_position_ref_structure import BoardingPositionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BoardingPositionRef(BoardingPositionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
