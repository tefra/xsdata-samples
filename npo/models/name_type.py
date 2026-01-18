from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.gtaa_status_type import GtaaStatusType
from npo.models.role_type import RoleType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class NameType:
    class Meta:
        name = "nameType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    scope_note: list[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    role: RoleType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    gtaa_uri: None | str = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        },
    )
    gtaa_status: None | GtaaStatusType = field(
        default=None,
        metadata={
            "name": "gtaaStatus",
            "type": "Attribute",
        },
    )
