from __future__ import annotations

from dataclasses import dataclass, field

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
from .boolean import Boolean
from .boolean_value_variation_point import BooleanValueVariationPoint
from .composite_network_representation import CompositeNetworkRepresentation
from .constant_reference import ConstantReference
from .data_filter import DataFilter
from .end_to_end_transformation_com_spec_props import (
    EndToEndTransformationComSpecProps,
)
from .handle_out_of_range_enum import HandleOutOfRangeEnum
from .handle_out_of_range_status_enum import HandleOutOfRangeStatusEnum
from .handle_timeout_enum import HandleTimeoutEnum
from .not_available_value_specification import NotAvailableValueSpecification
from .numerical_rule_based_value_specification import (
    NumericalRuleBasedValueSpecification,
)
from .numerical_value_specification import NumericalValueSpecification
from .positive_integer import PositiveInteger
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .receiver_intent_enum import ReceiverIntentEnum
from .reception_com_spec_props import ReceptionComSpecProps
from .ref import Ref
from .reference_value_specification import ReferenceValueSpecification
from .sw_data_def_props import SwDataDefProps
from .text_value_specification import TextValueSpecification
from .time_value import TimeValue
from .user_defined_transformation_com_spec_props import (
    UserDefinedTransformationComSpecProps,
)
from .variable_access import VariableAccess

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NonqueuedReceiverComSpec:
    """
    Communication attributes specific to non-queued receiving.

    :ivar composite_network_representations: This represents a
        CompositeNetworkRepresentation defined in the context of a
        ReceiverComSpec. The purpose of this aggregation is to be able
        to specify the network representation of leaf elements of
        ApplicationCompositeDataTypes.
    :ivar data_element_ref: Data element these attributes belong to.
    :ivar data_update_period: This attribute defines the period in which
        the application shall check for updated data. This attribute is
        used for the configuration of the E2E protection, but may also
        indicate a general data reception period.
    :ivar external_replacement_ref: This reference is used to reference
        the AutosarDataPrototype to be taken for sourcing an external
        replacement in the out-of-range handling.
    :ivar handle_out_of_range: This attribute controls how values that
        are out of the specified range are handled according to the
        values of HandleOutOfRangeEnum.
    :ivar handle_out_of_range_status: Control the way how return values
        are created in case of an out-of-range situation.
    :ivar max_delta_counter_init: Initial maximum allowed gap between
        two counter values of two consecutively received valid Data,
        i.e. how many subsequent lost data is accepted. For example, if
        the receiver gets Data with counter 1 and MaxDeltaCounterInit is
        1, then at the next reception the receiver can accept Counters
        with values 2 and 3, but not 4. Note that if the receiver does
        not receive new Data at a consecutive read, then the receiver
        increments the tolerance by 1. Caveat: The E2E wrapper approach
        involves technologies that are not subjected to the AUTOSAR
        standard and is superseded by the superior E2E transformer
        approach (which is fully standardized by AUTOSAR). Hence, new
        projects (without legacy constraints due to carry-over parts)
        shall use the fully standardized E2E transformer approach.
    :ivar max_no_new_or_repeated_data: The maximum amount of missing or
        repeated Data which the receiver does not expect to exceed under
        normal communication conditions. Caveat: The E2E wrapper
        approach involves technologies that are not subjected to the
        AUTOSAR standard and is superseded by the superior E2E
        transformer approach (which is fully standardized by AUTOSAR).
        Hence, new projects (without legacy constraints due to carry-
        over parts) shall use the fully standardized E2E transformer
        approach.
    :ivar network_representation: A networkRepresentation is used to
        define how the dataElement is mapped to a communication bus.
    :ivar receiver_intent: This attribute represents the expressed
        intent of the receiver. The receiver may decide to claim that
        existing resources of a ServiceInterface are expressly not used
        by this specific receiver. The conceptual background of this
        claim may be driven by security, safety, etc.
    :ivar reception_props: "This aggregation represents the definition
        transmission props in the context of the enclosing
        ReceiverComSpec.
    :ivar replace_with: This aggregation is used to identify the
        AutosarDataPrototype to be taken for sourcing an external
        replacement in the out-of-range handling.
    :ivar sync_counter_init: Number of Data required for validating the
        consistency of the counter that shall be received with a valid
        counter (i.e. counter within the allowed lock-in range) after
        the detection of an unexpected behavior of a received counter.
        Caveat: The E2E wrapper approach involves technologies that are
        not subjected to the AUTOSAR standard and is superseded by the
        superior E2E transformer approach (which is fully standardized
        by AUTOSAR). Hence, new projects (without legacy constraints due
        to carry-over parts) shall use the fully standardized E2E
        transformer approach.
    :ivar transformation_com_spec_propss: This references the
        TransformationComSpecProps which define  port-specific
        configuration for data transformation.
    :ivar uses_end_to_end_protection: This indicates whether the
        corresponding dataElement shall be transmitted using end-to-end
        protection. Caveat: The E2E wrapper approach involves
        technologies that are not subjected to the AUTOSAR standard and
        is superseded by the superior E2E transformer approach (which is
        fully standardized by AUTOSAR). Hence, new projects (without
        legacy constraints due to carry-over parts) shall use the fully
        standardized E2E transformer approach.
    :ivar alive_timeout: Specify the amount of time (in seconds) after
        which the software component (via the RTE)  needs to be notified
        if the corresponding data item have not been received according
        to the specified timing description. If the aliveTimeout
        attribute is 0 no timeout monitoring shall be performed.
    :ivar enable_update: This attribute controls whether application
        code is entitled to check whether the value of the corresponding
        VariableDataPrototype has been updated.
    :ivar filter: The applicable filter algorithm for filtering the
        value of the corresponding dataElement.
    :ivar handle_data_status: If this attribute is set to true than the
        Rte_IStatus API shall exist. If the attribute does not exist or
        is set to false then the Rte_IStatus API may still exist in
        response to the existence of further conditions.
    :ivar handle_never_received: This attribute specifies whether for
        the corresponding VariableDataPrototype the "never received"
        flag is available. If yes, the RTE is supposed to assume that
        initially the VariableDataPrototype has not been received
        before. After the first reception of the corresponding
        VariableDataPrototype the flag is cleared. * If the value of
        this attribute is set to "true" the flag is required. * If set
        to "false", the RTE shall not support the "never received"
        functionality for the corresponding VariableDataPrototype.
    :ivar handle_timeout_type: This attribute controls the behavior with
        respect to the handling of timeouts.
    :ivar init_value: Initial value to be used in case the sending
        component is not yet initialized. If the sender also specifies
        an initial value the receiver's value will be used.
    :ivar timeout_substitution_value: This attribute represents the
        substitution value applicable in the case of a timeout.
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
        name = "NONQUEUED-RECEIVER-COM-SPEC"

    composite_network_representations: (
        NonqueuedReceiverComSpec.CompositeNetworkRepresentations | None
    ) = field(
        default=None,
        metadata={
            "name": "COMPOSITE-NETWORK-REPRESENTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_element_ref: NonqueuedReceiverComSpec.DataElementRef | None = field(
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
    external_replacement_ref: (
        NonqueuedReceiverComSpec.ExternalReplacementRef | None
    ) = field(
        default=None,
        metadata={
            "name": "EXTERNAL-REPLACEMENT-REF",
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
    handle_out_of_range_status: HandleOutOfRangeStatusEnum | None = field(
        default=None,
        metadata={
            "name": "HANDLE-OUT-OF-RANGE-STATUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_delta_counter_init: PositiveIntegerValueVariationPoint | None = field(
        default=None,
        metadata={
            "name": "MAX-DELTA-COUNTER-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_no_new_or_repeated_data: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MAX-NO-NEW-OR-REPEATED-DATA",
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
    receiver_intent: ReceiverIntentEnum | None = field(
        default=None,
        metadata={
            "name": "RECEIVER-INTENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    reception_props: ReceptionComSpecProps | None = field(
        default=None,
        metadata={
            "name": "RECEPTION-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    replace_with: VariableAccess | None = field(
        default=None,
        metadata={
            "name": "REPLACE-WITH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sync_counter_init: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "SYNC-COUNTER-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformation_com_spec_propss: (
        NonqueuedReceiverComSpec.TransformationComSpecPropss | None
    ) = field(
        default=None,
        metadata={
            "name": "TRANSFORMATION-COM-SPEC-PROPSS",
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
    alive_timeout: TimeValue | None = field(
        default=None,
        metadata={
            "name": "ALIVE-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    enable_update: Boolean | None = field(
        default=None,
        metadata={
            "name": "ENABLE-UPDATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    filter: DataFilter | None = field(
        default=None,
        metadata={
            "name": "FILTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    handle_data_status: Boolean | None = field(
        default=None,
        metadata={
            "name": "HANDLE-DATA-STATUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    handle_never_received: Boolean | None = field(
        default=None,
        metadata={
            "name": "HANDLE-NEVER-RECEIVED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    handle_timeout_type: HandleTimeoutEnum | None = field(
        default=None,
        metadata={
            "name": "HANDLE-TIMEOUT-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    init_value: NonqueuedReceiverComSpec.InitValue | None = field(
        default=None,
        metadata={
            "name": "INIT-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_substitution_value: (
        NonqueuedReceiverComSpec.TimeoutSubstitutionValue | None
    ) = field(
        default=None,
        metadata={
            "name": "TIMEOUT-SUBSTITUTION-VALUE",
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
    class ExternalReplacementRef(Ref):
        dest: AutosarDataPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TransformationComSpecPropss:
        end_to_end_transformation_com_spec_props: list[
            EndToEndTransformationComSpecProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_transformation_com_spec_props: list[
            UserDefinedTransformationComSpecProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class InitValue:
        application_assoc_map_value_specification: (
            ApplicationAssocMapValueSpecification | None
        ) = field(
            default=None,
            metadata={
                "name": "APPLICATION-ASSOC-MAP-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_rule_based_value_specification: (
            ApplicationRuleBasedValueSpecification | None
        ) = field(
            default=None,
            metadata={
                "name": "APPLICATION-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_value_specification: (
            ApplicationValueSpecification | None
        ) = field(
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
        composite_rule_based_value_specification: (
            CompositeRuleBasedValueSpecification | None
        ) = field(
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
        not_available_value_specification: (
            NotAvailableValueSpecification | None
        ) = field(
            default=None,
            metadata={
                "name": "NOT-AVAILABLE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_rule_based_value_specification: (
            NumericalRuleBasedValueSpecification | None
        ) = field(
            default=None,
            metadata={
                "name": "NUMERICAL-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_value_specification: NumericalValueSpecification | None = (
            field(
                default=None,
                metadata={
                    "name": "NUMERICAL-VALUE-SPECIFICATION",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        record_value_specification: RecordValueSpecification | None = field(
            default=None,
            metadata={
                "name": "RECORD-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        reference_value_specification: ReferenceValueSpecification | None = (
            field(
                default=None,
                metadata={
                    "name": "REFERENCE-VALUE-SPECIFICATION",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        text_value_specification: TextValueSpecification | None = field(
            default=None,
            metadata={
                "name": "TEXT-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TimeoutSubstitutionValue:
        application_assoc_map_value_specification: (
            ApplicationAssocMapValueSpecification | None
        ) = field(
            default=None,
            metadata={
                "name": "APPLICATION-ASSOC-MAP-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_rule_based_value_specification: (
            ApplicationRuleBasedValueSpecification | None
        ) = field(
            default=None,
            metadata={
                "name": "APPLICATION-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_value_specification: (
            ApplicationValueSpecification | None
        ) = field(
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
        composite_rule_based_value_specification: (
            CompositeRuleBasedValueSpecification | None
        ) = field(
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
        not_available_value_specification: (
            NotAvailableValueSpecification | None
        ) = field(
            default=None,
            metadata={
                "name": "NOT-AVAILABLE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_rule_based_value_specification: (
            NumericalRuleBasedValueSpecification | None
        ) = field(
            default=None,
            metadata={
                "name": "NUMERICAL-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_value_specification: NumericalValueSpecification | None = (
            field(
                default=None,
                metadata={
                    "name": "NUMERICAL-VALUE-SPECIFICATION",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        record_value_specification: RecordValueSpecification | None = field(
            default=None,
            metadata={
                "name": "RECORD-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        reference_value_specification: ReferenceValueSpecification | None = (
            field(
                default=None,
                metadata={
                    "name": "REFERENCE-VALUE-SPECIFICATION",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        text_value_specification: TextValueSpecification | None = field(
            default=None,
            metadata={
                "name": "TEXT-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
