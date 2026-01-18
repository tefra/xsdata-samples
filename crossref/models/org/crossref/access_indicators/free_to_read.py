from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.crossref.org/AccessIndicators.xsd"


@dataclass
class FreeToRead:
    class Meta:
        name = "free_to_read"
        namespace = "http://www.crossref.org/AccessIndicators.xsd"

    end_date: XmlDate | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    start_date: XmlDate | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
