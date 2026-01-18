from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from npo.models.range_matcher_type import RangeMatcherType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DateRangeMatcherType(RangeMatcherType):
    class Meta:
        name = "dateRangeMatcherType"

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
