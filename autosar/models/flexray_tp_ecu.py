from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import VariationPoint
from autosar.models.boolean import Boolean
from autosar.models.ecu_instance_subtypes_enum import EcuInstanceSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayTpEcu:
    """ECU specific TP configuration parameters.

    Each TpEcu element has a reference to exactly one ECUInstance in the
    topology.

    :ivar cancellation: With this switch Tx and Rx Cancellation can be
        turned on or off.
    :ivar cycle_time_main_function: The period between successive calls
        to the Main Function of the AUTOSAR TP. Specified in seconds.
    :ivar ecu_instance_ref: Connection to the ECUInstance in the
        Topology
    :ivar full_duplex_enabled: The full duplex mechanisms is enabled if
        this attribute is set to true. Otherwise half duplex is enabled.
    :ivar transmit_cancellation: This attribute states whether Transmit
        Cancellation is supported on this ECU.  Please note that this
        attribute is deprecated and will be removed in future.
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
        name = "FLEXRAY-TP-ECU"

    cancellation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CANCELLATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    cycle_time_main_function: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "CYCLE-TIME-MAIN-FUNCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ecu_instance_ref: Optional["FlexrayTpEcu.EcuInstanceRef"] = field(
        default=None,
        metadata={
            "name": "ECU-INSTANCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    full_duplex_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "FULL-DUPLEX-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    transmit_cancellation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TRANSMIT-CANCELLATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class EcuInstanceRef(Ref):
        dest: Optional[EcuInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
