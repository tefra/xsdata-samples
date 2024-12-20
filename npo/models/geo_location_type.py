from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.geo_role_type import GeoRoleType
from npo.models.gtaa_status_type import GtaaStatusType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GeoLocationType:
    class Meta:
        name = "geoLocationType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
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
    role: None | GeoRoleType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
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
