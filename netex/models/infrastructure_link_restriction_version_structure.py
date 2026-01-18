from dataclasses import dataclass, field
from typing import Optional

from .link_ref_structure import LinkRefStructure
from .network_restriction_version_structure import (
    NetworkRestrictionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureLinkRestrictionVersionStructure(
    NetworkRestrictionVersionStructure
):
    class Meta:
        name = "InfrastructureLinkRestriction_VersionStructure"

    from_link_ref: LinkRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to_link_ref: LinkRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
