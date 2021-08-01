from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class PortalRestrictionType:
    class Meta:
        name = "portalRestrictionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    portal_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "portalId",
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
