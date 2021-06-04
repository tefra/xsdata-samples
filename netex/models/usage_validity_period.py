from dataclasses import dataclass
from netex.models.usage_validity_period_version_structure import UsageValidityPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageValidityPeriod(UsageValidityPeriodVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
