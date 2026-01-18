from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from npo.models.redirect_entry import RedirectEntry

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class RedirectList:
    class Meta:
        name = "redirectList"

    entry: list[RedirectEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    last_update: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "lastUpdate",
            "type": "Attribute",
        },
    )
