from dataclasses import dataclass, field
from typing import Optional
from netex.models.external_object_ref_structure import ExternalObjectRefStructure
from netex.models.type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfProductCategoryStructure(TypeOfEntityVersionStructure):
    external_product_category_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
