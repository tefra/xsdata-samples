from dataclasses import dataclass
from netex.models.series_constraint_price_versioned_child_structure import SeriesConstraintPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintPrice(SeriesConstraintPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
