from dataclasses import dataclass, field

from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class GlobalTimeCouplingPortProps:
    """
    Defines properties for the usage of the CouplingPort in the scope of
    Global Time Sync.

    :ivar propagation_delay: If cyclic propagation delay measurement is
        enabled, this parameter represents the default value of the
        propagation delay until the first actually measured propagation
        delay is available. If cyclic propagation delay measurement is
        disabled, this parameter defines a fixed value for the
        propagation delay.
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
        name = "GLOBAL-TIME-COUPLING-PORT-PROPS"

    propagation_delay: TimeValue | None = field(
        default=None,
        metadata={
            "name": "PROPAGATION-DELAY",
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
