from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


class StandardToVtlMappingMethodType(Enum):
    """
    A simple type enumerating the standard mapping methods when converting
    from data structures from SDMX to VLT.

    :cvar BASIC: The default mapping method. See Section 6 SDMX
        Standards ("SDMX Technical Notes"), 10.3.3.1 ("Basic Mapping").
    :cvar PIVOT: Method for mapping multi-measure data. See Section 6
        SDMX Standards ("SDMX Technical Notes"), 10.3.3.2 ("Pivot
        Mapping").
    :cvar BASIC_A2_M: The basic mapping method, using attributes to
        measures. See Section 6 SDMX Standards ("SDMX Technical Notes"),
        10.3.3.3 ("From SDMX DataAttributes to VTL Measures").
    :cvar PIVOT_A2_M: The pivot mapping method, using attributes to
        measures. See Section 6 SDMX Standards ("SDMX Technical Notes"),
        10.3.3.3 ("From SDMX DataAttributes to VTL Measures").
    """

    BASIC = "Basic"
    PIVOT = "Pivot"
    BASIC_A2_M = "Basic-A2M"
    PIVOT_A2_M = "Pivot-A2M"
