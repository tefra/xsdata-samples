from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DateRangeFacetItemType:
    class Meta:
        name = "dateRangeFacetItemType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    begin: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    end: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
