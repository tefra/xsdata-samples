from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .delta_values_rel_structure import DeltaValuesRelStructure
from .modification_enumeration import ModificationEnumeration
from .simple_object_ref import SimpleObjectRef
from .simple_object_ref_structure import SimpleObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeltaStructure:
    simple_object_ref: None | SimpleObjectRef = field(
        default=None,
        metadata={
            "name": "SimpleObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_version_ref: None | SimpleObjectRefStructure = field(
        default=None,
        metadata={
            "name": "FromVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_version_ref: None | SimpleObjectRefStructure = field(
        default=None,
        metadata={
            "name": "ToVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
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
    delta_values: None | DeltaValuesRelStructure = field(
        default=None,
        metadata={
            "name": "deltaValues",
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
    created: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
