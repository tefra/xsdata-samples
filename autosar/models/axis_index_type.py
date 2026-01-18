from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AxisIndexType:
    """
    This meta-class specifies an axis in a curve/map data object.

    The index satisfies the following convention: * 0 output "axis" * 1
    input axis 1 (X input axis e.g. of a CURVE) * 2 input axis 2 (Y input
    axis e.g. of a MAP) * 3 input axis 3 (Z input axis e.g. of a CUBOID) *
    4 input axis 3 (Z4 input axis e.g. of a CUBE_4) * 5 input axis 3 (Z5
    input axis e.g. of a CUBE_5) * 6..9 etc. The output "axis" provides
    access to the output value of the parameter. Note that this access is
    usually performed via an index according to the input axis. In addition
    to this, the Values STRING and ARRAY support specific iterations.

    :ivar value:
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
        name = "AXIS-INDEX-TYPE"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]+|STRING|ARRAY",
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
