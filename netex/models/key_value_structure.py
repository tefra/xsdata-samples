from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class KeyValueStructure:
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    value: str = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    type_of_key: None | str = field(
        default=None,
        metadata={
            "name": "typeOfKey",
            "type": "Attribute",
        },
    )
