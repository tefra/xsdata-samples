from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .delta import Delta
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TraceStructure:
    object_ref: None | VersionOfObjectRefStructure = field(
        default=None,
        metadata={
            "name": "ObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    changed_at: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ChangedAt",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    changed_by: None | str = field(
        default=None,
        metadata={
            "name": "ChangedBy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    delta: None | Delta = field(
        default=None,
        metadata={
            "name": "Delta",
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
