from dataclasses import dataclass
from netex.models.uic_operating_period_version_structure import UicOperatingPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UicOperatingPeriod(UicOperatingPeriodVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
