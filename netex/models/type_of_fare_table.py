from dataclasses import dataclass

from .type_of_fare_table_version_structure import (
    TypeOfFareTableVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFareTable(TypeOfFareTableVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
