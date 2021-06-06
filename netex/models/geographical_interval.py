from dataclasses import dataclass
from .geographical_interval_version_structure import GeographicalIntervalVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalInterval(GeographicalIntervalVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
