from __future__ import annotations

from dataclasses import dataclass, field

from .infrastructure_link_version_structure import (
    InfrastructureLinkVersionStructure,
)
from .wire_point_ref_structure import WirePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireElementVersionStructure(InfrastructureLinkVersionStructure):
    class Meta:
        name = "WireElement_VersionStructure"

    from_point_ref: WirePointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: WirePointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
