from __future__ import annotations
from dataclasses import dataclass, field
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
    owner: None | OwnerTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    role: None | GeoRoleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    gtaa_uri: None | str = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    match: None | Match = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
