from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_product_category_ref import TypeOfProductCategoryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfProductCategoryRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfProductCategoryRefs_RelStructure"

    type_of_product_category_ref: List[TypeOfProductCategoryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
