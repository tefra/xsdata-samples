from dataclasses import dataclass

from .destination_display_ref_structure import DestinationDisplayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DestinationDisplayRef(DestinationDisplayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
