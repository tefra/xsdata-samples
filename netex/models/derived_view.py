from dataclasses import dataclass
from netex.models.derived_view_structure import DerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DerivedView(DerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
