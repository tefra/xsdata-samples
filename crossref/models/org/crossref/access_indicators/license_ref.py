from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from crossref.models.org.crossref.access_indicators.license_ref_applies_to import (
    LicenseRefAppliesTo,
)

__NAMESPACE__ = "http://www.crossref.org/AccessIndicators.xsd"


@dataclass
class LicenseRef:
    class Meta:
        name = "license_ref"
        namespace = "http://www.crossref.org/AccessIndicators.xsd"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 10,
            "pattern": r"([hH][tT][tT][pP]|[hH][tT][tT][pP][sS]|[fF][tT][pP])://.*",
        },
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    applies_to: Optional[LicenseRefAppliesTo] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
