from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SwImplPolicyEnumSimple(Enum):
    """
    :cvar CONST: forced implementation such that the  running software
        within the ECU  shall not modify it. For example implemented
        with the "const" modifier in C.  This can be applied for
        parameters (not for those in NVRAM) as well as argument  data
        prototypes.
    :cvar FIXED: This data element is fixed. In particular this
        indicates, that it  might also be implemented  e.g. as in place
        data, (#DEFINE).
    :cvar MEASUREMENT_POINT: The data element is created for measurement
        purposes only.  The data element is never read directly within
        the ECU software. In contrast to  a "standard" data element in
        an unconnected provide port is, this unconnection  is guaranteed
        for  measurementPoint data elements.
    :cvar QUEUED: The content of the data element is queued and the data
        element has 'event' semantics, i.e. data elements are stored in
        a queue and all data  elements are processed in 'first in first
        out' order.  The queuing is intended to be implemented by RTE
        Generator. This value is not applicable for parameters.
    :cvar STANDARD: This is applicable for all kinds of data elements.
        For variable  data prototypes the 'last is best' semantics
        applies. For parameter there is no  specific implementation
        directive.
    """
    CONST = "CONST"
    FIXED = "FIXED"
    MEASUREMENT_POINT = "MEASUREMENT-POINT"
    QUEUED = "QUEUED"
    STANDARD = "STANDARD"
