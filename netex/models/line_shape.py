from __future__ import annotations

from dataclasses import dataclass

from .line_shape_structure_2 import LineShapeStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineShape(LineShapeStructure2):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
