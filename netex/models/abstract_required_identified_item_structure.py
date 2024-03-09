from dataclasses import dataclass, field
from typing import Optional

from .abstract_item_structure import AbstractItemStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractRequiredIdentifiedItemStructure(AbstractItemStructure):
    item_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
