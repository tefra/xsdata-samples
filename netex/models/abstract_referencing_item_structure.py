from dataclasses import dataclass, field
from typing import Optional
from .abstract_item_structure import AbstractItemStructure
from .item_ref_structure import ItemRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractReferencingItemStructure(AbstractItemStructure):
    item_ref: Optional[ItemRefStructure] = field(
        default=None,
        metadata={
            "name": "ItemRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
