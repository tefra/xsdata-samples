from __future__ import annotations

from dataclasses import dataclass, field

from .tax_category_enumeration import TaxCategoryEnumeration
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPricingRuleVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfPricingRule_VersionStructure"

    tax_category: None | TaxCategoryEnumeration = field(
        default=None,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
