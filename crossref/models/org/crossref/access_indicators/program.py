from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.access_indicators.free_to_read import (
    FreeToRead,
)
from crossref.models.org.crossref.access_indicators.license_ref import (
    LicenseRef,
)

__NAMESPACE__ = "http://www.crossref.org/AccessIndicators.xsd"


@dataclass
class Program:
    """
    Accommodates deposit of license metadata.

    The license_ref value will be a URL. Values for the "applies_to"
    attribute are vor (version of record),am (accepted manuscript), tdm
    (text and data mining), and stm-asf (STM Article Sharing Framework
    license).
    """

    class Meta:
        name = "program"
        namespace = "http://www.crossref.org/AccessIndicators.xsd"

    free_to_read: FreeToRead | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    license_ref: list[LicenseRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    name: str = field(
        init=False,
        default="AccessIndicators",
        metadata={
            "type": "Attribute",
        },
    )
