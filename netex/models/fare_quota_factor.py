from dataclasses import dataclass
from netex.models.fare_quota_factor_version_structure import FareQuotaFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareQuotaFactor(FareQuotaFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
