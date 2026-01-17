from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


class StandardFromVtlMappingMethodType(Enum):
    """
    A simple type enumerating the standard mapping methods when converting
    from data structures from VTL to SDMX.

    :cvar BASIC: The default mapping method, applicable only when the
        VLT data structure has just one measure component. See Section 6
        SDMX Standards ("SDMX Technical Notes"), 10.3.4.1 ("Basic
        Mapping").
    :cvar UNPIVOT: The mapping method to be used when the VTL data
        structure has more than one measure component. See Section 6
        SDMX Standards ("SDMX Technical Notes"), 10.3.4.2 ("Unpivot
        Mapping").
    :cvar M2_A: Mapping of multi-measure VTL where on measure is mapped
        to the SDMX primary measure and the remaining measures are
        mapped as data attributes. See Section 6 SDMX Standards ("SDMX
        Technical Notes"), 10.3.4.3 ("From VTL Measures to SDMX
        DataAttributes").
    """

    BASIC = "Basic"
    UNPIVOT = "Unpivot"
    M2_A = "M2A"
