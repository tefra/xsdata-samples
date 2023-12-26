from dataclasses import dataclass
from .flexible_line_derived_view_structure import (
    FlexibleLineDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleLineView(FlexibleLineDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
