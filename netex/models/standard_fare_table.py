from dataclasses import dataclass
from netex.models.standard_fare_table_version_structure import StandardFareTableVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StandardFareTable(StandardFareTableVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
