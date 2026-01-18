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
from .constant_reference import ConstantReference
from .not_available_value_specification import NotAvailableValueSpecification
from .numerical_rule_based_value_specification import (
    NumericalRuleBasedValueSpecification,
)
from .numerical_value_specification import NumericalValueSpecification
from .persistency_data_element_subtypes_enum import (
    PersistencyDataElementSubtypesEnum,
)
from .ref import Ref
from .reference_value_specification import ReferenceValueSpecification
from .text_value_specification import TextValueSpecification

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PersistencyDataRequiredComSpec:
    """
    This meta-class represents the ability to define port-specific
    attributes for supporting use cases of data persistency on the required
    side.

    :ivar data_element_ref: This refrence represents the
        PersistencyDataElement for which the
        PersistencyDataRequiredComSpec applies.
    :ivar init_value: This aggregation represents the definition of an
        initial value for the PersistencyDataElement referenced by the
        enclosing PersistencyDataRequiredComSpec
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
        name = "PERSISTENCY-DATA-REQUIRED-COM-SPEC"

    data_element_ref: PersistencyDataRequiredComSpec.DataElementRef | None = field(
        default=None,
        metadata={
            "name": "DATA-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    init_value: PersistencyDataRequiredComSpec.InitValue | None = field(
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
    class DataElementRef(Ref):
        dest: PersistencyDataElementSubtypesEnum | None = field(
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
