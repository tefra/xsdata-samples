from dataclasses import dataclass

from .fare_table_row_ref_structure import FareTableRowRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareTableRowRef(FareTableRowRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
