from dataclasses import dataclass, field
from typing import List, Optional

from .compu_const import CompuConst
from .compu_scale import CompuScale

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Compu:
    """
    This meta-class represents the ability to express one particular computation.

    :ivar compu_scales: This represents one scale within the compu
        method. Note that it contains a Variationpoint in order to
        support blueprints of enumerations. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar compu_default_value: This property can be used to specify an
        output value for a conversion formula, if the value to be
        converted lies outside the plausibility limit. Although this is
        possible for all conversion formulae, it is especially valid for
        variables with tabular conversion formulae.
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
        name = "COMPU"

    compu_scales: Optional["Compu.CompuScales"] = field(
        default=None,
        metadata={
            "name": "COMPU-SCALES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    compu_default_value: Optional[CompuConst] = field(
        default=None,
        metadata={
            "name": "COMPU-DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class CompuScales:
        compu_scale: List[CompuScale] = field(
            default_factory=list,
            metadata={
                "name": "COMPU-SCALE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
