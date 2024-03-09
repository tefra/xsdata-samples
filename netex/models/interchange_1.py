from dataclasses import dataclass

from .interchange_version_structure import InterchangeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Interchange1(InterchangeVersionStructure):
    class Meta:
        name = "Interchange"
        namespace = "http://www.netex.org.uk/netex"
