from dataclasses import dataclass

from .charging_moment_ref_structure import ChargingMomentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ChargingMomentRef(ChargingMomentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
