from dataclasses import dataclass, field
from typing import Optional
from autosar.models.application_rule_based_value_specification import ApplicationRuleBasedValueSpecification
from autosar.models.application_value_specification import ApplicationValueSpecification
from autosar.models.constant_reference import ConstantReference
from autosar.models.not_available_value_specification import NotAvailableValueSpecification
from autosar.models.numerical_rule_based_value_specification import NumericalRuleBasedValueSpecification
from autosar.models.numerical_value_specification import NumericalValueSpecification
from autosar.models.persistency_data_element_subtypes_enum import PersistencyDataElementSubtypesEnum
from autosar.models.record_value_specification import (
    ApplicationAssocMapValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueSpecification,
    RecordValueSpecification,
)
from autosar.models.ref import Ref
from autosar.models.reference_value_specification import ReferenceValueSpecification
from autosar.models.text_value_specification import TextValueSpecification

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PersistencyDataRequiredComSpec:
    """
    This meta-class represents the ability to define port-specific attributes
    for supporting use cases of data persistency on the required side.

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

    data_element_ref: Optional["PersistencyDataRequiredComSpec.DataElementRef"] = field(
        default=None,
        metadata={
            "name": "DATA-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    init_value: Optional["PersistencyDataRequiredComSpec.InitValue"] = field(
        default=None,
        metadata={
            "name": "INIT-VALUE",
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
    class DataElementRef(Ref):
        dest: Optional[PersistencyDataElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class InitValue:
        application_assoc_map_value_specification: Optional[ApplicationAssocMapValueSpecification] = field(
            default=None,
            metadata={
                "name": "APPLICATION-ASSOC-MAP-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        application_rule_based_value_specification: Optional[ApplicationRuleBasedValueSpecification] = field(
            default=None,
            metadata={
                "name": "APPLICATION-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        application_value_specification: Optional[ApplicationValueSpecification] = field(
            default=None,
            metadata={
                "name": "APPLICATION-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        array_value_specification: Optional[ArrayValueSpecification] = field(
            default=None,
            metadata={
                "name": "ARRAY-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        composite_rule_based_value_specification: Optional[CompositeRuleBasedValueSpecification] = field(
            default=None,
            metadata={
                "name": "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        constant_reference: Optional[ConstantReference] = field(
            default=None,
            metadata={
                "name": "CONSTANT-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        not_available_value_specification: Optional[NotAvailableValueSpecification] = field(
            default=None,
            metadata={
                "name": "NOT-AVAILABLE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        numerical_rule_based_value_specification: Optional[NumericalRuleBasedValueSpecification] = field(
            default=None,
            metadata={
                "name": "NUMERICAL-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        numerical_value_specification: Optional[NumericalValueSpecification] = field(
            default=None,
            metadata={
                "name": "NUMERICAL-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        record_value_specification: Optional[RecordValueSpecification] = field(
            default=None,
            metadata={
                "name": "RECORD-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        reference_value_specification: Optional[ReferenceValueSpecification] = field(
            default=None,
            metadata={
                "name": "REFERENCE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        text_value_specification: Optional[TextValueSpecification] = field(
            default=None,
            metadata={
                "name": "TEXT-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
