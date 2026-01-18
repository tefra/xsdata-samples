from dataclasses import dataclass, field

from .modification_enumeration import ModificationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeltaValueStructure:
    delta_ref: str | None = field(
        default=None,
        metadata={
            "name": "DeltaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    modification: ModificationEnumeration | None = field(
        default=None,
        metadata={
            "name": "Modification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    value_name: str | None = field(
        default=None,
        metadata={
            "name": "ValueName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    old_value: object | None = field(
        default=None,
        metadata={
            "name": "OldValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    new_value: object | None = field(
        default=None,
        metadata={
            "name": "NewValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
