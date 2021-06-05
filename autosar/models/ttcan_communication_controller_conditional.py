from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import VariationPoint
from autosar.models.boolean import Boolean
from autosar.models.can_controller_configuration import CanControllerConfiguration
from autosar.models.can_controller_configuration_requirements import CanControllerConfigurationRequirements
from autosar.models.integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TtcanCommunicationControllerConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar wake_up_by_controller_supported: Defines whether the ECU shall
        be woken up by this CommunicationController. TRUE: wake up is
        possible FALSE: wake up is not supported Note: If
        wakeUpByControllerSupported is set to TRUE the feature shall be
        supported by both hardware and basic software.
    :ivar can_controller_attributes: CAN Bit Timing configuration
    :ivar appl_watchdog_limit: The Appl_Watchdog_Limit shall be an 8-bit
        value specifying the period for the application watchdog in
        Appl_Watchdog_Limit times 256 NTUs.
    :ivar expected_tx_trigger: The Expected_Tx_Trigger shall be an eight
        (8) bit value which limits the number of messages the FSE may
        try to transmit in one matrix cycle.
    :ivar external_clock_synchronisation: One bit shall be used to
        configure whether or not external clock synchronisation will be
        allowed during runtime (only Level 2).
    :ivar initial_ref_offset: The Initial_Ref_Offset shall be an eight
        (8) bit value for the initialisation of Ref_Trigger_Offset.
    :ivar master: One bit shall be used to distinguish between
        (potential) time masters and time slaves. This can be derived
        from the frame-triggering's triggers.
    :ivar time_master_priority: The time master priority shall contain a
        three bit value for the priority of the current time master (the
        last three bits of the identifier of the reference message).
        This can be derived from the frame-triggering's triggers.
    :ivar time_triggered_can_level: One bit shall be used to distinguish
        between Level 1 and Level 2.
    :ivar tx_enable_window_length: The length of the Tx_Enable window
        shall be a four (4) bit value specifying the length of the time
        period (1-16 nominal CAN bit times) in which a transmission may
        be started.
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
        name = "TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL"

    wake_up_by_controller_supported: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "WAKE-UP-BY-CONTROLLER-SUPPORTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    can_controller_attributes: Optional["TtcanCommunicationControllerConditional.CanControllerAttributes"] = field(
        default=None,
        metadata={
            "name": "CAN-CONTROLLER-ATTRIBUTES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    appl_watchdog_limit: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "APPL-WATCHDOG-LIMIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    expected_tx_trigger: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "EXPECTED-TX-TRIGGER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    external_clock_synchronisation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "EXTERNAL-CLOCK-SYNCHRONISATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    initial_ref_offset: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "INITIAL-REF-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    master: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "MASTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    time_master_priority: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "TIME-MASTER-PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    time_triggered_can_level: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "TIME-TRIGGERED-CAN-LEVEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tx_enable_window_length: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "TX-ENABLE-WINDOW-LENGTH",
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
    class CanControllerAttributes:
        can_controller_configuration: Optional[CanControllerConfiguration] = field(
            default=None,
            metadata={
                "name": "CAN-CONTROLLER-CONFIGURATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        can_controller_configuration_requirements: Optional[CanControllerConfigurationRequirements] = field(
            default=None,
            metadata={
                "name": "CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
