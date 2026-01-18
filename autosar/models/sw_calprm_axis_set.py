from dataclasses import dataclass, field
from typing import Optional

from .sw_calprm_axis import SwCalprmAxis

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwCalprmAxisSet:
    """
    This element specifies the input parameter axes (abscissas) of
    parameters (and variables, if these are used adaptively).

    :ivar sw_calprm_axis: One axis belonging to this SwCalprmAxisSet
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
        name = "SW-CALPRM-AXIS-SET"

    sw_calprm_axis: list[SwCalprmAxis] = field(
        default_factory=list,
        metadata={
            "name": "SW-CALPRM-AXIS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
