from dataclasses import dataclass
from .quay_version_structure import QuayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Quay1(QuayVersionStructure):
    class Meta:
        name = "Quay"
        namespace = "http://www.netex.org.uk/netex"
