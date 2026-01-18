from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from npo.models.geo_restriction_enum import GeoRestrictionEnum
from npo.models.platform_type_enum import PlatformTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class GeoRestrictionType:
    class Meta:
        name = "geoRestrictionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    region_id: None | GeoRestrictionEnum = field(
        default=None,
        metadata={
            "name": "regionId",
            "type": "Attribute",
        },
    )
    start: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stop: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    platform: None | PlatformTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
