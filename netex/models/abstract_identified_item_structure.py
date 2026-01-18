from __future__ import annotations

from dataclasses import dataclass, field

from .abstract_item_structure import AbstractItemStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractIdentifiedItemStructure(AbstractItemStructure):
    item_identifier: None | str = field(
        default=None,
        metadata={
            "name": "ItemIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
