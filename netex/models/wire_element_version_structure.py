from dataclasses import dataclass, field
from typing import Optional
from .infrastructure_link_version_structure import InfrastructureLinkVersionStructure
from .wire_point_ref_structure import WirePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WireElementVersionStructure(InfrastructureLinkVersionStructure):
    class Meta:
        name = "WireElement_VersionStructure"

    from_point_ref: Optional[WirePointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: Optional[WirePointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
