from __future__ import annotations

from dataclasses import dataclass

from .boarding_position_ref_structure import BoardingPositionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPositionRef(BoardingPositionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
