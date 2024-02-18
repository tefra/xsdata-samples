from dataclasses import dataclass
from .operating_period_version_structure import OperatingPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingPeriod1(OperatingPeriodVersionStructure):
    class Meta:
        name = "OperatingPeriod"
        namespace = "http://www.netex.org.uk/netex"
