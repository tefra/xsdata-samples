from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
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
