from dataclasses import dataclass
from netex.models.interchanging_version_structure import InterchangingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Interchanging(InterchangingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
