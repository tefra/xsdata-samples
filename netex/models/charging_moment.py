from dataclasses import dataclass
from netex.models.charging_moment_value_structure import ChargingMomentValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ChargingMoment(ChargingMomentValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
