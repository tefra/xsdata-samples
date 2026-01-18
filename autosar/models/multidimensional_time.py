from __future__ import annotations

from dataclasses import dataclass, field

from .cse_code_type_string import CseCodeTypeString
from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MultidimensionalTime:
    """
    This is used to specify a multidimensional time value based on ASAM CSE
    codes.

    It is specified by a code which defined the basis of the time and a
    scaling factor which finally determines the time value. If for example
    the cseCode is 100 and the cseCodeFactor is 360, it represents 360
    angular degrees. If the cseCode is 0 and the cseCodeFactor is 50 it
    represents 50 microseconds.

    :ivar cse_code: Specifies the time base by means of CSE codes.
    :ivar cse_code_factor: The scaling factor for the time value based
        on the specified CSE code.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "MULTIDIMENSIONAL-TIME"

    cse_code: None | CseCodeTypeString = field(
        default=None,
        metadata={
            "name": "CSE-CODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    cse_code_factor: None | Integer = field(
        default=None,
        metadata={
            "name": "CSE-CODE-FACTOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
