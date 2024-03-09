from dataclasses import dataclass

from .fare_table_column_ref_structure import FareTableColumnRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareTableColumnRef(FareTableColumnRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
