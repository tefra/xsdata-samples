from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .autosar_data_prototype_subtypes_enum import (
    AutosarDataPrototypeSubtypesEnum,
)
from .boolean_value_variation_point import BooleanValueVariationPoint
from .composite_network_representation import CompositeNetworkRepresentation
from .end_to_end_transformation_com_spec_props import (
    EndToEndTransformationComSpecProps,
)
from .handle_out_of_range_enum import HandleOutOfRangeEnum
from .handle_out_of_range_status_enum import HandleOutOfRangeStatusEnum
from .positive_integer import PositiveInteger
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .receiver_intent_enum import ReceiverIntentEnum
from .reception_com_spec_props import ReceptionComSpecProps
from .ref import Ref
from .sw_data_def_props import SwDataDefProps
from .time_value import TimeValue
from .user_defined_transformation_com_spec_props import (
    UserDefinedTransformationComSpecProps,
)
from .variable_access import VariableAccess

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class QueuedReceiverComSpec:
    """
    Communication attributes specific to queued receiving.

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
        name = "QUEUED-RECEIVER-COM-SPEC"

    composite_network_representations: QueuedReceiverComSpec.CompositeNetworkRepresentations | None = field(
        default=None,
        metadata={
            "name": "COMPOSITE-NETWORK-REPRESENTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_element_ref: QueuedReceiverComSpec.DataElementRef | None = field(
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
    external_replacement_ref: QueuedReceiverComSpec.ExternalReplacementRef | None = field(
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
    max_delta_counter_init: PositiveIntegerValueVariationPoint | None = (
        field(
            default=None,
            metadata={
                "name": "MAX-DELTA-COUNTER-INIT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    transformation_com_spec_propss: QueuedReceiverComSpec.TransformationComSpecPropss | None = field(
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
    queue_length: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "QUEUE-LENGTH",
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
