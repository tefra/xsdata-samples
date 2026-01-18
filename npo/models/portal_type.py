from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.section_type import SectionType

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass(kw_only=True)
class PortalType:
    class Meta:
        name = "portalType"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "required": True,
        }
    )
    section: None | SectionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    url: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
