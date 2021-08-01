from dataclasses import dataclass, field
from typing import Optional
from npo.models.geo_role_type import GeoRoleType
from npo.models.match import Match
from npo.models.owner_type_enum import OwnerTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class GeoLocationSearchType:
    class Meta:
        name = "geoLocationSearchType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    role: Optional[GeoRoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
