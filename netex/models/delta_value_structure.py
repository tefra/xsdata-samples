from dataclasses import dataclass, field
from typing import Optional
from .modification_enumeration import ModificationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeltaValueStructure:
    delta_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeltaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    modification: Optional[ModificationEnumeration] = field(
        default=None,
        metadata={
            "name": "Modification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    value_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValueName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    old_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "OldValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    new_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "NewValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
