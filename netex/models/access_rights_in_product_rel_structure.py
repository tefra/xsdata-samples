from dataclasses import dataclass, field
from typing import List, Union
from .access_right_in_product import AccessRightInProduct
from .access_right_in_product_ref import AccessRightInProductRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRightsInProductRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "accessRightsInProduct_RelStructure"

    access_right_in_product_ref_or_access_right_in_product: List[
        Union[AccessRightInProductRef, AccessRightInProduct]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessRightInProductRef",
                    "type": AccessRightInProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightInProduct",
                    "type": AccessRightInProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
