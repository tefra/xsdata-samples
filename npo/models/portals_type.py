from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.organization_type import OrganizationType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class PortalsType:
    class Meta:
        name = "portalsType"

    portal: list[OrganizationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
