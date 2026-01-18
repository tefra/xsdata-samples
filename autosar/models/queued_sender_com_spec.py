from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .autosar_data_prototype_subtypes_enum import (
    AutosarDataPrototypeSubtypesEnum,
)
from .boolean_value_variation_point import BooleanValueVariationPoint
from .composite_network_representation import CompositeNetworkRepresentation
from .handle_out_of_range_enum import HandleOutOfRangeEnum
from .ref import Ref
from .sender_intent_enum import SenderIntentEnum
from .sw_data_def_props import SwDataDefProps
from .time_value import TimeValue
from .transmission_acknowledgement_request import (
    TransmissionAcknowledgementRequest,
)
from .transmission_com_spec_props import TransmissionComSpecProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class QueuedSenderComSpec:
    """
    Communication attributes specific to distribution of events
    (PPortPrototype, SenderReceiverInterface and dataElement carries an
    "event").

    :ivar composite_network_representations: This represents a
        CompositeNetworkRepresentation defined in the context of a
        SenderComSpec.
    :ivar data_element_ref: Data element these quality of service
        attributes apply to.
    :ivar data_update_period: This attribute describes the period in
        which the applications are assumed to transmit the respective
        data.
    :ivar handle_out_of_range: This attribute controls how out-of-range
        values shall be dealt with.
    :ivar network_representation: A networkRepresentation is used to
        define how the dataElement is mapped to a communication bus.
    :ivar sender_intent: This attribute represents the expressed intent
        of the client. The client may decide to claim that existing
        resources of a ServiceInterface are expressly not used by this
        specific client. The conceptual background of this claim may be
        driven by security, safety, etc.
    :ivar transmission_acknowledge: Requested transmission
        acknowledgement for data element.
    :ivar transmission_props: This aggregation represents the definition
        transmission props in the context of the enclosing
        SenderComSpec.
    :ivar uses_end_to_end_protection: This indicates whether the
        corresponding dataElement shall be transmitted using end-to-end
        protection.
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
        name = "QUEUED-SENDER-COM-SPEC"

    composite_network_representations: QueuedSenderComSpec.CompositeNetworkRepresentations | None = field(
        default=None,
        metadata={
            "name": "COMPOSITE-NETWORK-REPRESENTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_element_ref: QueuedSenderComSpec.DataElementRef | None = field(
        default=None,
        metadata={
            "name": "DATA-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_update_period: TimeValue | None = field(
        default=None,
        metadata={
            "name": "DATA-UPDATE-PERIOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    handle_out_of_range: HandleOutOfRangeEnum | None = field(
        default=None,
        metadata={
            "name": "HANDLE-OUT-OF-RANGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_representation: SwDataDefProps | None = field(
        default=None,
        metadata={
            "name": "NETWORK-REPRESENTATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sender_intent: SenderIntentEnum | None = field(
        default=None,
        metadata={
            "name": "SENDER-INTENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmission_acknowledge: TransmissionAcknowledgementRequest | None = (
        field(
            default=None,
            metadata={
                "name": "TRANSMISSION-ACKNOWLEDGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    transmission_props: TransmissionComSpecProps | None = field(
        default=None,
        metadata={
            "name": "TRANSMISSION-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    uses_end_to_end_protection: BooleanValueVariationPoint | None = field(
        default=None,
        metadata={
            "name": "USES-END-TO-END-PROTECTION",
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

    @dataclass
    class CompositeNetworkRepresentations:
        composite_network_representation: list[
            CompositeNetworkRepresentation
        ] = field(
            default_factory=list,
            metadata={
                "name": "COMPOSITE-NETWORK-REPRESENTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DataElementRef(Ref):
        dest: AutosarDataPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
