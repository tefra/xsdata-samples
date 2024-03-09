from dataclasses import dataclass

from .interchanging_version_structure import InterchangingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Interchanging(InterchangingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
