from dataclasses import dataclass, field

from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from .series_constraint_ref import SeriesConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "SeriesConstraintPrice_VersionedChildStructure"

    series_constraint_ref: SeriesConstraintRef | None = field(
        default=None,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
