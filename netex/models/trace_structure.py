from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .delta import Delta
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TraceStructure:
    object_ref: VersionOfObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "ObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    changed_at: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "ChangedAt",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    changed_by: str | None = field(
        default=None,
        metadata={
            "name": "ChangedBy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    delta: Delta | None = field(
        default=None,
        metadata={
            "name": "Delta",
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
    created: XmlDateTime | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
