from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDuration
from npo.models.range_facet_result_item import RangeFacetResultItem

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DurationFacetResultItemType(RangeFacetResultItem):
    class Meta:
        name = "durationFacetResultItemType"

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
