from dataclasses import dataclass
from netex.models.type_of_fare_table_ref_structure import TypeOfFareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFareTableRef(TypeOfFareTableRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
