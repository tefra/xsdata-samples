from dataclasses import dataclass, field
from typing import List
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_right_in_product_ref import AccessRightInProductRef
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRightsInProductRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "accessRightsInProduct_RelStructure"

    access_right_in_product_ref: List[AccessRightInProductRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightInProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_right_in_product: List[AccessRightInProduct] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightInProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
