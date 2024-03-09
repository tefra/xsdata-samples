from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class PortalRestrictionType:
    class Meta:
        name = "portalRestrictionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    portal_id: None | str = field(
        default=None,
        metadata={
            "name": "portalId",
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
