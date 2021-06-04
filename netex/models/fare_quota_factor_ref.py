from dataclasses import dataclass
from netex.models.fare_quota_factor_ref_structure import FareQuotaFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareQuotaFactorRef(FareQuotaFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
