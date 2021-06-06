from dataclasses import dataclass
from .onward_timing_link_derived_view_structure import OnwardTimingLinkDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnwardTimingLinkView(OnwardTimingLinkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
