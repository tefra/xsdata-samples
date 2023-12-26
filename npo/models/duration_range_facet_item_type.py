from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DurationRangeFacetItemType:
    class Meta:
        name = "durationRangeFacetItemType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    begin: None | XmlDuration = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    end: None | XmlDuration = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
