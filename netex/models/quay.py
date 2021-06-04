from dataclasses import dataclass
from netex.models.quay_version_structure import QuayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Quay(QuayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
