from __future__ import annotations

from dataclasses import dataclass, field

from .activation_point_ref_structure import ActivationPointRefStructure
from .link_version_structure import LinkVersionStructure
from .type_of_activation_ref import TypeOfActivationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationLinkVersionStructure(LinkVersionStructure):
    class Meta:
        name = "ActivationLink_VersionStructure"

    type_of_activation_ref: None | TypeOfActivationRef = field(
        default=None,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_point_ref: None | ActivationPointRefStructure = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to_point_ref: None | ActivationPointRefStructure = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
