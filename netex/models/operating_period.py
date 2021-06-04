from dataclasses import dataclass
from netex.models.operating_period_version_structure import OperatingPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingPeriod(OperatingPeriodVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
