from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import VariationPoint
from .boolean import Boolean
from .lin_slave_config import LinSlaveConfig
from .string import String
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LinMasterConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar wake_up_by_controller_supported: Defines whether the ECU shall
        be woken up by this CommunicationController. TRUE: wake up is
        possible FALSE: wake up is not supported Note: If
        wakeUpByControllerSupported is set to TRUE the feature shall be
        supported by both hardware and basic software.
    :ivar protocol_version: Version specifier for a communication
        protocol.
    :ivar lin_slaves: LinSlaves that are handled by the LinMaster.
    :ivar time_base: Time base is mandatory for the master. It is not
        used for slaves. LIN 2.0 Spec states: "The time_base value
        specifies the used time base in the master node to generate the
        maximum allowed frame transfer time." The time base shall be
        specified AUTOSAR conform in seconds.
    :ivar time_base_jitter: The attribute timeBaseJitter is a mandatory
        attribute for the master and not used for slaves. LIN 2.0 Spec
        states: "The jitter value specifies the differences between the
        maximum and minimum delay from time base start point to the
        frame header sending start point (falling edge of BREAK
        signal)." The jitter shall be specified AUTOSAR conform in
        seconds.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "LIN-MASTER-CONDITIONAL"

    wake_up_by_controller_supported: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "WAKE-UP-BY-CONTROLLER-SUPPORTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    protocol_version: Optional[String] = field(
        default=None,
        metadata={
            "name": "PROTOCOL-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    lin_slaves: Optional["LinMasterConditional.LinSlaves"] = field(
        default=None,
        metadata={
            "name": "LIN-SLAVES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_base: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIME-BASE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_base_jitter: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIME-BASE-JITTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class LinSlaves:
        lin_slave_config: List[LinSlaveConfig] = field(
            default_factory=list,
            metadata={
                "name": "LIN-SLAVE-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
