from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import VariationPoint
from autosar.models.application_rule_based_value_specification import ApplicationRuleBasedValueSpecification
from autosar.models.application_value_specification import ApplicationValueSpecification
from autosar.models.constant_reference import ConstantReference
from autosar.models.flat_instance_descriptor_subtypes_enum import FlatInstanceDescriptorSubtypesEnum
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
class CalibrationParameterValue:
    """Specifies instance specific calibration parameter values used to
    initialize the memory objects implementing calibration parameters in the
    generated RTE code.

    RTE generator will use the implInitValue to override the initial values specified for the DataPrototypes of a component type.

    The applInitValue is used to exchange init values with the component vendor not publishing the transformation algorithm between ApplicationDataTypes and ImplementationDataTypes or defining an instance specific initialization of components which are only defined with ApplicationDataTypes.

    Note: If both representations of init values are available these need to represent the same content.

    Note further that in this case an explicit mapping of ValueSpecification is not implemented because calibration parameters are delivered back after the calibration phase.

    :ivar appl_init_value: This is the initial value specification
        structured according to the ApplicationDataType
    :ivar impl_init_value: This is the initial value specification
        structured according to the ImplementationDataType
    :ivar initialized_parameter_ref: This represents the parameter that
        is initialized by the CalibrationParameterValue.
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
        name = "CALIBRATION-PARAMETER-VALUE"

    appl_init_value: Optional["CalibrationParameterValue.ApplInitValue"] = field(
        default=None,
        metadata={
            "name": "APPL-INIT-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    impl_init_value: Optional["CalibrationParameterValue.ImplInitValue"] = field(
        default=None,
        metadata={
            "name": "IMPL-INIT-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    initialized_parameter_ref: Optional["CalibrationParameterValue.InitializedParameterRef"] = field(
        default=None,
        metadata={
            "name": "INITIALIZED-PARAMETER-REF",
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
    class ApplInitValue:
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
    class ImplInitValue:
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
    class InitializedParameterRef(Ref):
        dest: Optional[FlatInstanceDescriptorSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
