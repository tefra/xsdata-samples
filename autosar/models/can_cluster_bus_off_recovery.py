from dataclasses import dataclass, field
from typing import Optional

from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanClusterBusOffRecovery:
    """
    This element contains the attributes that are used to configure the CAN bus off
    monitoring / recovery at system level.

    :ivar bor_counter_l_1_to_l_2: This threshold defines the count of
        bus-offs until the bus-off recovery switches from level 1 (short
        recovery time) to level 2 (long recovery time).
    :ivar bor_time_l_1: This attribute defines the duration of the bus-
        off recovery time in level 1 (short recovery time) in seconds.
    :ivar bor_time_l_2: This attribute defines the duration of the bus-
        off recovery time in level 2 (long recovery time) in seconds.
    :ivar bor_time_tx_ensured: This attribute defines the duration of
        the bus-off event check in seconds.
    :ivar main_function_period: This attribute defines the cycle time of
        the function CanSM_MainFunction in seconds.
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
        name = "CAN-CLUSTER-BUS-OFF-RECOVERY"

    bor_counter_l_1_to_l_2: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "BOR-COUNTER-L-1-TO-L-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bor_time_l_1: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "BOR-TIME-L-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bor_time_l_2: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "BOR-TIME-L-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bor_time_tx_ensured: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "BOR-TIME-TX-ENSURED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    main_function_period: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "MAIN-FUNCTION-PERIOD",
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
