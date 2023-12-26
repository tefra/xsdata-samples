from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDuration
from npo.models.range_matcher_type import RangeMatcherType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DurationRangeMatcherType(RangeMatcherType):
    class Meta:
        name = "durationRangeMatcherType"

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
