from dataclasses import dataclass

from .journey_version_structure import JourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Journey1(JourneyVersionStructure):
    class Meta:
        name = "Journey"
        namespace = "http://www.netex.org.uk/netex"
