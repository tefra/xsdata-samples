from dataclasses import dataclass
from netex.models.time_structure_factor_ref_structure import TimeStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeStructureFactorRef(TimeStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
