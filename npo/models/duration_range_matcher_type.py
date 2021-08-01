from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from npo.models.range_matcher_type import RangeMatcherType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DurationRangeMatcherType(RangeMatcherType):
    class Meta:
        name = "durationRangeMatcherType"

    begin: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
