from collections.abc import Iterable
from dataclasses import dataclass, field

from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AmountOfPriceUnitRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "amountOfPriceUnitRefs_RelStructure"

    amount_of_price_unit_product_ref: Iterable[AmountOfPriceUnitProductRef] = (
        field(
            default_factory=list,
            metadata={
                "name": "AmountOfPriceUnitProductRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
