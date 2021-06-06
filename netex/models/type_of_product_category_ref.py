from dataclasses import dataclass
from .type_of_product_category_ref_structure import TypeOfProductCategoryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfProductCategoryRef(TypeOfProductCategoryRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
