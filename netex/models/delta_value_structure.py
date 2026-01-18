from __future__ import annotations

from dataclasses import dataclass, field

from .modification_enumeration import ModificationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeltaValueStructure:
    delta_ref: None | str = field(
        default=None,
        metadata={
            "name": "DeltaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    modification: None | ModificationEnumeration = field(
        default=None,
        metadata={
            "name": "Modification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    value_name: None | str = field(
        default=None,
        metadata={
            "name": "ValueName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    old_value: None | object = field(
        default=None,
        metadata={
            "name": "OldValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    new_value: None | object = field(
        default=None,
        metadata={
            "name": "NewValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
