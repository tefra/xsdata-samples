from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from npo.models.range_facet_result_item import RangeFacetResultItem

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DurationFacetResultItemType(RangeFacetResultItem):
    class Meta:
        name = "durationFacetResultItemType"

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
