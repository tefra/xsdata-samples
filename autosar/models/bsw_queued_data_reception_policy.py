from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .boolean import Boolean
from .positive_integer import PositiveInteger
from .ref import Ref
from .variable_data_prototype_subtypes_enum import (
    VariableDataPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class BswQueuedDataReceptionPolicy:
    """
    Reception policy attributes specific for queued receiving.

    :ivar enable_take_address: If set to true, the BSW Module is able to
        use the API reference for deriving a pointer to an object
    :ivar received_data_ref: The data received over the BSW Scheduler
        using this policy.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar queue_length: Length of queue for received events.
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
        name = "BSW-QUEUED-DATA-RECEPTION-POLICY"

    enable_take_address: None | Boolean = field(
        default=None,
        metadata={
            "name": "ENABLE-TAKE-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    received_data_ref: None | BswQueuedDataReceptionPolicy.ReceivedDataRef = (
        field(
            default=None,
            metadata={
                "name": "RECEIVED-DATA-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    queue_length: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "QUEUE-LENGTH",
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

    @dataclass(kw_only=True)
    class ReceivedDataRef(Ref):
        dest: VariableDataPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
