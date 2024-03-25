from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ReleaseCalendarType:
    """ReleaseCalendarType describes information about the timing of releases of
    the constrained data.

    All of these values use the standard "P7D" - style format.

    :ivar periodicity: Periodicity is the period between releases of the
        data set.
    :ivar offset: Offset is the interval between January first and the
        first release of data within the year.
    :ivar tolerance: Tolerance is the period after which the release of
        data may be deemed late.
    """

    periodicity: Optional[str] = field(
        default=None,
        metadata={
            "name": "Periodicity",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
    tolerance: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tolerance",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
