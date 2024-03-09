from dataclasses import dataclass

from .journey_ref_structure import JourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyRef(JourneyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
