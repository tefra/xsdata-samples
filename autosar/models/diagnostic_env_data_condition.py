from dataclasses import dataclass, field
from typing import Optional
from autosar.models.application_rule_based_value_specification import ApplicationRuleBasedValueSpecification
from autosar.models.application_value_specification import ApplicationValueSpecification
from autosar.models.constant_reference import ConstantReference
from autosar.models.diagnostic_compare_type_enum import DiagnosticCompareTypeEnum
from autosar.models.diagnostic_data_element_subtypes_enum import DiagnosticDataElementSubtypesEnum
from autosar.models.not_available_value_specification import NotAvailableValueSpecification
from autosar.models.numerical_rule_based_value_specification import NumericalRuleBasedValueSpecification
from autosar.models.numerical_value_specification import NumericalValueSpecification
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
class DiagnosticEnvDataCondition:
    """A DiagnosticEnvDataCondition is an atomic condition that compares the
    current value of the referenced DiagnosticDataElement with a constant value
    defined by the ValueSpecification.

    All compareTypes are supported.

    :ivar compare_type: This attributes represents the concrete type of
        the comparison.
    :ivar compare_value: This attribute represents a fixed compare value
        taken to evaluate the compare condition.
    :ivar data_element_ref: This reference represents the related
        diagnostic data element.
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
        name = "DIAGNOSTIC-ENV-DATA-CONDITION"

    compare_type: Optional[DiagnosticCompareTypeEnum] = field(
        default=None,
        metadata={
            "name": "COMPARE-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    compare_value: Optional["DiagnosticEnvDataCondition.CompareValue"] = field(
        default=None,
        metadata={
            "name": "COMPARE-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_element_ref: Optional["DiagnosticEnvDataCondition.DataElementRef"] = field(
        default=None,
        metadata={
            "name": "DATA-ELEMENT-REF",
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
    class CompareValue:
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

    @dataclass
    class DataElementRef(Ref):
        dest: Optional[DiagnosticDataElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
