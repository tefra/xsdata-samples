from __future__ import annotations

from dataclasses import dataclass

from .boarding_position_version_structure import (
    BoardingPositionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPosition(BoardingPositionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
