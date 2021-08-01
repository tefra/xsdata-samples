from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from npo.models.geo_restriction_enum import GeoRestrictionEnum
from npo.models.platform_type_enum import PlatformTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GeoRestrictionType:
    class Meta:
        name = "geoRestrictionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    region_id: Optional[GeoRestrictionEnum] = field(
        default=None,
        metadata={
            "name": "regionId",
            "type": "Attribute",
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
