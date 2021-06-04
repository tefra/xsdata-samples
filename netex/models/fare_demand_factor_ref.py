from dataclasses import dataclass
from netex.models.fare_demand_factor_ref_structure import FareDemandFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareDemandFactorRef(FareDemandFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
