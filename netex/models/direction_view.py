from dataclasses import dataclass
from netex.models.direction_derived_view_structure import DirectionDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DirectionView(DirectionDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
