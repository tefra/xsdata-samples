from dataclasses import dataclass, field
from typing import List, Union
from .cell_versioned_child_structure import (
    FareTable,
    FareTableInContext,
)
from .frame_containment_structure import FrameContainmentStructure
from .standard_fare_table import StandardFareTable

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareTablesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareTablesInFrame_RelStructure"

    standard_fare_table_or_fare_table_in_context_or_fare_table: List[Union[StandardFareTable, FareTableInContext, FareTable]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTable",
                    "type": StandardFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableInContext",
                    "type": FareTableInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTable",
                    "type": FareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
