from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import VariationPoint
from autosar.models.boolean import Boolean
from autosar.models.can_controller_configuration import CanControllerConfiguration
from autosar.models.can_controller_configuration_requirements import CanControllerConfigurationRequirements

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanCommunicationControllerConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar wake_up_by_controller_supported: Defines whether the ECU shall
        be woken up by this CommunicationController.  TRUE: wake up is
        possible  FALSE: wake up is not supported  Note: If
        wakeUpByControllerSupported is set to TRUE the feature shall be
        supported by both hardware and basic software.
    :ivar can_controller_attributes: CAN Bit Timing configuration
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
        name = "CAN-COMMUNICATION-CONTROLLER-CONDITIONAL"

    wake_up_by_controller_supported: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "WAKE-UP-BY-CONTROLLER-SUPPORTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    can_controller_attributes: Optional["CanCommunicationControllerConditional.CanControllerAttributes"] = field(
        default=None,
        metadata={
            "name": "CAN-CONTROLLER-ATTRIBUTES",
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
