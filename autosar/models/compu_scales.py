from __future__ import annotations

from dataclasses import dataclass, field

from .compu_scale import CompuScale

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CompuScales:
    """
    This meta-class represents the ability to stepwise express a
    computation method.

    :ivar compu_scales: This represents one scale within the compu
        method. Note that it contains a Variationpoint in order to
        support blueprints of enumerations. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
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
        name = "COMPU-SCALES"

    compu_scales: None | CompuScales.CompuScalesInner = field(
        default=None,
        metadata={
            "name": "COMPU-SCALES",
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

    @dataclass
    class CompuScalesInner:
        compu_scale: list[CompuScale] = field(
            default_factory=list,
            metadata={
                "name": "COMPU-SCALE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
