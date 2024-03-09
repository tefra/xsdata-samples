from dataclasses import dataclass

from .railway_element_version_structure import RailwayElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RailwayElement(RailwayElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
