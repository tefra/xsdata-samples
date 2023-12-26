from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate, XmlDateTime
from npo.models.range_facet_result_item import RangeFacetResultItem

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DateFacetResultItemType(RangeFacetResultItem):
    class Meta:
        name = "dateFacetResultItemType"

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
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
