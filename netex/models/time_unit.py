from dataclasses import dataclass
from netex.models.time_unit_version_structure import TimeUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeUnit(TimeUnitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
