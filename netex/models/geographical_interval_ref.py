from dataclasses import dataclass
from .geographical_interval_ref_structure import (
    GeographicalIntervalRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalIntervalRef(GeographicalIntervalRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
