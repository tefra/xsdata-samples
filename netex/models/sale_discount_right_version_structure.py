from dataclasses import dataclass, field
from typing import List, Optional
from .fare_product_version_structure import FareProductVersionStructure
from .general_group_of_entities import GeneralGroupOfEntities
from .general_group_of_entities_ref import GeneralGroupOfEntitiesRef
from .sale_discount_right_enumeration import SaleDiscountRightEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SaleDiscountRightVersionStructure(FareProductVersionStructure):
    class Meta:
        name = "SaleDiscountRight_VersionStructure"

    product_type: Optional[SaleDiscountRightEnumeration] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_group_of_entities_ref_or_general_group_of_entities: List[object] = field(
        default_factory=list,
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
            "max_occurs": 2,
        }
    )
