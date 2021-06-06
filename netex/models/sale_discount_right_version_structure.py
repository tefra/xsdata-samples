from dataclasses import dataclass, field
from typing import Optional
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
    general_group_of_entities_ref: Optional[GeneralGroupOfEntitiesRef] = field(
        default=None,
        metadata={
            "name": "GeneralGroupOfEntitiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_group_of_entities: Optional[GeneralGroupOfEntities] = field(
        default=None,
        metadata={
            "name": "GeneralGroupOfEntities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
