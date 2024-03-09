from dataclasses import dataclass

from .series_constraint_price_ref_structure import (
    SeriesConstraintPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintPriceRef(SeriesConstraintPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
