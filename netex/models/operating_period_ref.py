from dataclasses import dataclass
from netex.models.operating_period_ref_structure import OperatingPeriodRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingPeriodRef(OperatingPeriodRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
