from dataclasses import dataclass
from netex.models.flexible_area_ref_structure import FlexibleAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleAreaRef(FlexibleAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
