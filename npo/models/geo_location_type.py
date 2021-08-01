from dataclasses import dataclass, field
from typing import List, Optional
from npo.models.geo_role_type import GeoRoleType
from npo.models.gtaa_status_type import GtaaStatusType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GeoLocationType:
    class Meta:
        name = "geoLocationType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    role: Optional[GeoRoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    gtaa_status: Optional[GtaaStatusType] = field(
        default=None,
        metadata={
            "name": "gtaaStatus",
            "type": "Attribute",
        }
    )
