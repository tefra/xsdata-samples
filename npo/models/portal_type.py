from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.section_type import SectionType

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class PortalType:
    class Meta:
        name = "portalType"

    name: None | str = field(
        default=None,
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
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    url: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
