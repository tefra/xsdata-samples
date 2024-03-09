from dataclasses import dataclass

from .fare_price_ref_structure import FarePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintPriceRefStructure(FarePriceRefStructure):
    pass
