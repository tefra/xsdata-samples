from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


class UsageType(StrEnum):
    """
    An enumeration of optional | mandatory to indicate the usage of an
    attribute or measure.
    """

    MANDATORY = "mandatory"
    OPTIONAL = "optional"
