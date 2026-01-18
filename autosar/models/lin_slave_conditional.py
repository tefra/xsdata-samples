from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .boolean import Boolean
from .integer import Integer
from .lin_error_response import LinErrorResponse
from .positive_integer import PositiveInteger
from .string import String
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LinSlaveConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar wake_up_by_controller_supported: Defines whether the ECU shall
        be woken up by this CommunicationController. TRUE: wake up is
        possible FALSE: wake up is not supported Note: If
        wakeUpByControllerSupported is set to TRUE the feature shall be
        supported by both hardware and basic software.
    :ivar protocol_version: Version specifier for a communication
        protocol.
    :ivar assign_nad: This attribute has the ability to control whether
        the node configuration command 'Assign NAD' is supported.
    :ivar configured_nad: To distinguish LIN slaves that are used twice
        or more within the same cluster.
    :ivar function_id: LIN function ID
    :ivar initial_nad: This attribute represents the initial NAD.
    :ivar lin_error_response: Each slave node shall publish one response
        error in one of its transmitted unconditional frames.
    :ivar nas_timeout: Value of the N_AS timeout. Unit: seconds.
    :ivar save_configuration: This attribute has the ability to decide
        whether the node configuration command 'Save Configuration' is
        supported.
    :ivar supplier_id: LIN Supplier ID
    :ivar variant_id: Specifies the Variant ID
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
        name = "LIN-SLAVE-CONDITIONAL"

    wake_up_by_controller_supported: Boolean | None = field(
        default=None,
        metadata={
            "name": "WAKE-UP-BY-CONTROLLER-SUPPORTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    protocol_version: String | None = field(
        default=None,
        metadata={
            "name": "PROTOCOL-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    assign_nad: Boolean | None = field(
        default=None,
        metadata={
            "name": "ASSIGN-NAD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    configured_nad: Integer | None = field(
        default=None,
        metadata={
            "name": "CONFIGURED-NAD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    function_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "FUNCTION-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    initial_nad: Integer | None = field(
        default=None,
        metadata={
            "name": "INITIAL-NAD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    lin_error_response: LinErrorResponse | None = field(
        default=None,
        metadata={
            "name": "LIN-ERROR-RESPONSE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nas_timeout: TimeValue | None = field(
        default=None,
        metadata={
            "name": "NAS-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    save_configuration: Boolean | None = field(
        default=None,
        metadata={
            "name": "SAVE-CONFIGURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    supplier_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "SUPPLIER-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variant_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "VARIANT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
