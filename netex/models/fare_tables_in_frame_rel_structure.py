from dataclasses import dataclass, field
from typing import List, Union
from .frame_containment_structure import FrameContainmentStructure
from .priceable_object_version_structure import (
    FareTableInContext,
    FareTable1,
)
from .standard_fare_table import StandardFareTable

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareTablesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareTablesInFrame_RelStructure"

    fare_table: List[
        Union[StandardFareTable, FareTableInContext, FareTable1]
    ] = field(
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
                    "type": FareTable1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
