from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .application_assoc_map_element_value_specification import (
    ApplicationAssocMapValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueSpecification,
    RecordValueSpecification,
)
from .application_rule_based_value_specification import (
    ApplicationRuleBasedValueSpecification,
)
from .application_value_specification import ApplicationValueSpecification
from .autosar_data_prototype_subtypes_enum import (
    AutosarDataPrototypeSubtypesEnum,
)
from .boolean_value_variation_point import BooleanValueVariationPoint
from .composite_network_representation import CompositeNetworkRepresentation
from .constant_reference import ConstantReference
from .handle_out_of_range_enum import HandleOutOfRangeEnum
from .not_available_value_specification import NotAvailableValueSpecification
from .numerical_rule_based_value_specification import (
    NumericalRuleBasedValueSpecification,
)
from .numerical_value_specification import NumericalValueSpecification
from .ref import Ref
from .reference_value_specification import ReferenceValueSpecification
from .sender_intent_enum import SenderIntentEnum
from .sw_data_def_props import SwDataDefProps
from .text_value_specification import TextValueSpecification
from .time_value import TimeValue
from .transmission_acknowledgement_request import (
    TransmissionAcknowledgementRequest,
)
from .transmission_com_spec_props import TransmissionComSpecProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FieldSenderComSpec:
    """
    Port specific communication attributes for a Field that is defined in a
    ServiceInterface.

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
    :ivar init_value: Initial value for a Field that is set before the
        ServiceInterface is offered.
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
        name = "FIELD-SENDER-COM-SPEC"

    composite_network_representations: FieldSenderComSpec.CompositeNetworkRepresentations | None = field(
        default=None,
        metadata={
            "name": "COMPOSITE-NETWORK-REPRESENTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_element_ref: FieldSenderComSpec.DataElementRef | None = field(
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
    init_value: FieldSenderComSpec.InitValue | None = field(
        default=None,
        metadata={
            "name": "INIT-VALUE",
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

    @dataclass
    class InitValue:
        application_assoc_map_value_specification: ApplicationAssocMapValueSpecification | None = field(
            default=None,
            metadata={
                "name": "APPLICATION-ASSOC-MAP-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_rule_based_value_specification: ApplicationRuleBasedValueSpecification | None = field(
            default=None,
            metadata={
                "name": "APPLICATION-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_value_specification: ApplicationValueSpecification | None = field(
            default=None,
            metadata={
                "name": "APPLICATION-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        array_value_specification: ArrayValueSpecification | None = field(
            default=None,
            metadata={
                "name": "ARRAY-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        composite_rule_based_value_specification: CompositeRuleBasedValueSpecification | None = field(
            default=None,
            metadata={
                "name": "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        constant_reference: ConstantReference | None = field(
            default=None,
            metadata={
                "name": "CONSTANT-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        not_available_value_specification: NotAvailableValueSpecification | None = field(
            default=None,
            metadata={
                "name": "NOT-AVAILABLE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_rule_based_value_specification: NumericalRuleBasedValueSpecification | None = field(
            default=None,
            metadata={
                "name": "NUMERICAL-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_value_specification: NumericalValueSpecification | None = field(
            default=None,
            metadata={
                "name": "NUMERICAL-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        record_value_specification: RecordValueSpecification | None = field(
            default=None,
            metadata={
                "name": "RECORD-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        reference_value_specification: ReferenceValueSpecification | None = field(
            default=None,
            metadata={
                "name": "REFERENCE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        text_value_specification: TextValueSpecification | None = field(
            default=None,
            metadata={
                "name": "TEXT-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
