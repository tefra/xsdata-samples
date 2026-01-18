from __future__ import annotations

from dataclasses import dataclass, field

from .fare_product_version_structure import FareProductVersionStructure
from .general_group_of_entities import GeneralGroupOfEntities
from .general_group_of_entities_ref import GeneralGroupOfEntitiesRef
from .sale_discount_right_enumeration import SaleDiscountRightEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SaleDiscountRightVersionStructure(FareProductVersionStructure):
    class Meta:
        name = "SaleDiscountRight_VersionStructure"

    product_type: None | SaleDiscountRightEnumeration = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    general_group_of_entities_ref_or_general_group_of_entities: (
        None | GeneralGroupOfEntitiesRef | GeneralGroupOfEntities
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeneralGroupOfEntitiesRef",
                    "type": GeneralGroupOfEntitiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralGroupOfEntities",
                    "type": GeneralGroupOfEntities,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
