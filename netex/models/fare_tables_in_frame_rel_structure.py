from dataclasses import dataclass, field
from typing import List
from .cell_versioned_child_structure import (
    FareTableInContext,
    FareTable1,
)
from .fare_table_2 import FareTable2
from .frame_containment_structure import FrameContainmentStructure
from .standard_fare_table import StandardFareTable

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareTablesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareTablesInFrame_RelStructure"

    standard_fare_table: List[StandardFareTable] = field(
        default_factory=list,
        metadata={
            "name": "StandardFareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_table_in_context: List[FareTableInContext] = field(
        default_factory=list,
        metadata={
            "name": "FareTableInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_table: List[FareTable1] = field(
        default_factory=list,
        metadata={
            "name": "FareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_fare_table: List[FareTable2] = field(
        default_factory=list,
        metadata={
            "name": "FareTable_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
