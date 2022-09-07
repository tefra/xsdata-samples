from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlPeriod
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_alt_as_published_value import StdAltAsPublishedValue
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_designator_t import StdDesignatorT

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StdAltAsPublished(StdDesignatorT):
    class Meta:
        name = "std_alt_as_published"
        namespace = "http://www.crossref.org/schema/5.3.1"

    reason: List[StdAltAsPublishedValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )
    approved_month: Optional[int] = field(
        default=None,
        metadata={
            "name": "approvedMonth",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 12,
            "total_digits": 2,
        }
    )
    approved_year: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "approvedYear",
            "type": "Attribute",
            "required": True,
        }
    )
