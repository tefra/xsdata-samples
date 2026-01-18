from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.crossref.org/AccessIndicators.xsd"


@dataclass(kw_only=True)
class FreeToRead:
    class Meta:
        name = "free_to_read"
        namespace = "http://www.crossref.org/AccessIndicators.xsd"

    end_date: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
