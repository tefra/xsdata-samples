from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.abstract_implementation_data_type_subtypes_enum import AbstractImplementationDataTypeSubtypesEnum
from autosar.models.alignment_type import AlignmentType
from autosar.models.annotation import (
    Annotation,
    VariationPoint,
)
from autosar.models.application_primitive_data_type_subtypes_enum import ApplicationPrimitiveDataTypeSubtypesEnum
from autosar.models.application_rule_based_value_specification import ApplicationRuleBasedValueSpecification
from autosar.models.application_value_specification import ApplicationValueSpecification
from autosar.models.autosar_variable_ref import AutosarVariableRef
from autosar.models.boolean import Boolean
from autosar.models.bsw_module_entry_subtypes_enum import BswModuleEntrySubtypesEnum
from autosar.models.compu_method_subtypes_enum import CompuMethodSubtypesEnum
from autosar.models.constant_reference import ConstantReference
from autosar.models.data_constr_subtypes_enum import DataConstrSubtypesEnum
from autosar.models.display_format_string import DisplayFormatString
from autosar.models.display_presentation_enum import DisplayPresentationEnum
from autosar.models.float_mod import FloatType
from autosar.models.identifier import Identifier
from autosar.models.mc_data_instance_subtypes_enum import McDataInstanceSubtypesEnum
from autosar.models.multidimensional_time import MultidimensionalTime
from autosar.models.native_declaration_string import NativeDeclarationString
from autosar.models.not_available_value_specification import NotAvailableValueSpecification
from autosar.models.numerical_rule_based_value_specification import NumericalRuleBasedValueSpecification
from autosar.models.numerical_value import NumericalValue
from autosar.models.numerical_value_specification import NumericalValueSpecification
from autosar.models.numerical_value_variation_point import NumericalValueVariationPoint
from autosar.models.record_value_specification import (
    ApplicationAssocMapValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueSpecification,
    RecordValueSpecification,
)
from autosar.models.ref import Ref
from autosar.models.reference_value_specification import ReferenceValueSpecification
from autosar.models.sw_addr_method_subtypes_enum import SwAddrMethodSubtypesEnum
from autosar.models.sw_base_type_subtypes_enum import SwBaseTypeSubtypesEnum
from autosar.models.sw_bit_representation import SwBitRepresentation
from autosar.models.sw_calibration_access_enum import SwCalibrationAccessEnum
from autosar.models.sw_calprm_axis_set import SwCalprmAxisSet
from autosar.models.sw_data_dependency import SwDataDependency
from autosar.models.sw_impl_policy_enum import SwImplPolicyEnum
from autosar.models.sw_record_layout_subtypes_enum import SwRecordLayoutSubtypesEnum
from autosar.models.sw_text_props import SwTextProps
from autosar.models.sw_variable_ref_proxy import SwVariableRefProxy
from autosar.models.text_value_specification import TextValueSpecification
from autosar.models.unit_subtypes_enum import UnitSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwPointerTargetProps:
    """This element defines, that the data object (which is specified by the
    aggregating element) contains a reference to another data object or to a
    function in the CPU code.

    This corresponds to a pointer in the C-language. The attributes of
    this element describe the category and the detailed properties of
    the target which is either a data description or a function
    signature.

    :ivar target_category: This specifies the category of the target: *
        In case of a data pointer, it shall specify the category of the
        referenced data. * In case of a function pointer, it could be
        used to denote the category of the referenced BswModuleEntry.
        Since currently no categories for BswModuleEntry are defined it
        will be empty.
    :ivar sw_data_def_props: The properties of the target data type.
    :ivar function_pointer_signature_ref: The referenced BswModuleEntry
        serves as the signature of a function pointer definition.
        Primary use case: function pointer passed as argument to other
        function.
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
        name = "SW-POINTER-TARGET-PROPS"

    target_category: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "TARGET-CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_data_def_props: Optional["SwDataDefProps"] = field(
        default=None,
        metadata={
            "name": "SW-DATA-DEF-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    function_pointer_signature_ref: Optional["SwPointerTargetProps.FunctionPointerSignatureRef"] = field(
        default=None,
        metadata={
            "name": "FUNCTION-POINTER-SIGNATURE-REF",
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
    class FunctionPointerSignatureRef(Ref):
        dest: Optional[BswModuleEntrySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class SwDataDefPropsConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar display_presentation: This attribute controls the presentation
        of the related data for measurement and calibration tools.
    :ivar step_size: This attribute can be used to define a value which
        is added to or subtracted from the value of a DataPrototype when
        using up/down keys while calibrating.
    :ivar sw_value_block_size_mults: This attribute is used to specify
        the dimensions of a value block (VAL_BLK) for the case that that
        value block has more than one dimension. The dimensions given in
        this attribute are ordered such that the first entry represents
        the first dimension, the second entry represents the second
        dimension, and so on. For one-dimensional value blocks the
        attribute swValueBlockSize shall be used and this attribute
        shall not exist.
    :ivar annotations: This aggregation allows to add annotations
        (yellow pads ...) related to the current data object.
    :ivar sw_addr_method_ref: Addressing method related to this data
        object. Via an association to the same SwAddrMethod it can be
        specified that several DataPrototypes shall be located in the
        same memory without already specifying the memory section
        itself.
    :ivar sw_alignment: The attribute describes the intended alignment
        of the DataPrototype. If the attribute is not defined the
        alignment is determined by the swBaseType size and the
        memoryAllocationKeywordPolicy of the referenced SwAddrMethod.
    :ivar base_type_ref: Base type associated with the containing data
        object.
    :ivar sw_bit_representation: Description of the binary
        representation in case of a bit variable.
    :ivar sw_calibration_access: Specifies the read or write access by
        MCD tools for this data object.
    :ivar sw_value_block_size: This represents the size of a Value Block
    :ivar sw_calprm_axis_set: This specifies the properties of the axes
        in case of a curve or map etc. This is mainly applicable to
        calibration parameters.
    :ivar sw_text_props: the specific properties if the data object is a
        text object.
    :ivar sw_comparison_variables: Variables used for comparison in an
        MCD process.
    :ivar compu_method_ref: Computation method associated with the
        semantics of this data object.
    :ivar data_constr_ref: Data constraint for this data object.
    :ivar sw_data_dependency: Describes how the value of the data object
        has to be calculated from the value of another data object (by
        the MCD system).
    :ivar display_format: This property describes how a number is to be
        rendered e.g. in documents or in a measurement and calibration
        system.
    :ivar implementation_data_type_ref: This association denotes the
        ImplementationDataType of a data declaration via its aggregated
        SwDataDefProps. It is used whenever a data declaration is not
        directly referring to a base type. Especially * redefinition of
        an ImplementationDataType via a "typedef" to another
        ImplementationDatatype * the target type of a pointer (see
        SwPointerTargetProps), if it does not refer to a base type
        directly * the data type of an array or record element within an
        ImplementationDataType, if it does not refer to a base type
        directly * the data type of an SwServiceArg, if it does not
        refer to a base type directly
    :ivar sw_host_variable: Contains a reference to a variable which
        serves as a host-variable for a bit variable. Only applicable to
        bit objects.
    :ivar sw_impl_policy: Implementation policy for this data object.
    :ivar additional_native_type_qualifier: This attribute is used to
        declare native qualifiers of the programming language which can
        neither be deduced from the baseType (e.g. because the data
        object describes a pointer) nor from other more abstract
        attributes. Examples are qualifiers like "volatile", "strict" or
        "enum" of the C-language. All such declarations have to be put
        into one string.
    :ivar sw_intended_resolution: The purpose of this element is to
        describe the requested quantization of data objects early on in
        the design process. The resolution ultimately occurs via the
        conversion formula present (compuMethod), which specifies the
        transition from the physical world to the standardized world
        (and vice-versa) (here, "the slope per bit" is present
        implicitly in the conversion formula). In the case of a
        development phase without a fixed conversion formula, a pre-
        specification can occur through swIntendedResolution. The
        resolution is specified in the physical domain according to the
        property "unit".
    :ivar sw_interpolation_method: This is a keyword identifying the
        mathematical method to be applied for interpolation. The keyword
        needs to be related to the interpolation routine which needs to
        be invoked.
    :ivar invalid_value: Optional value to express invalidity of the
        actual data element.
    :ivar mc_function: Specifies the name of a "Function" (in the sense
        of the MC system) to which this data object belongs. This
        corresponds to the Function in ASAM MCD 2MC /ASAP2 which defines
        the characteristic resp. which provides the measurement as
        output. The function name is only used for support of MC
        systems. It can be predefined on the level of software component
        design. If it  is not  predefined, it could be filled out with a
        reasonable name, e.g. the component  prototype name, from the
        ECU extract. Note: This attribute is deprecated because an
        explicit model of MC functions can be set up by using the meta-
        class McFunction.
    :ivar sw_is_virtual: This element distinguishes virtual objects.
        Virtual objects do not appear in the memory, their derivation is
        much more dependent on other objects and hence they shall have a
        swDataDependency .
    :ivar sw_pointer_target_props: Specifies that the containing data
        object is a pointer to another data object.
    :ivar sw_record_layout_ref: Record layout for this data object.
    :ivar sw_refresh_timing: This element specifies the frequency in
        which the object involved shall be or is called or calculated.
        This timing can be collected from the task in which write access
        processes to the variable run. But this cannot be done by the
        MCD system. So this attribute can be used in an early phase to
        express the desired refresh timing and later on to specify the
        real refresh timing.
    :ivar unit_ref: Physical unit associated with the semantics of this
        data object. This attribute applies if no compuMethod is
        specified. If both units (this as well as via compuMethod) are
        specified the units shall be compatible.
    :ivar value_axis_data_type_ref: The referenced
        ApplicationPrimitiveDataType represents the primitive data type
        of the value axis within a compound primitive (e.g. curve, map).
        It supersedes CompuMethod, Unit, and BaseType.
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
        name = "SW-DATA-DEF-PROPS-CONDITIONAL"

    display_presentation: Optional[DisplayPresentationEnum] = field(
        default=None,
        metadata={
            "name": "DISPLAY-PRESENTATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    step_size: Optional[FloatType] = field(
        default=None,
        metadata={
            "name": "STEP-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_value_block_size_mults: Optional["SwDataDefPropsConditional.SwValueBlockSizeMults"] = field(
        default=None,
        metadata={
            "name": "SW-VALUE-BLOCK-SIZE-MULTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["SwDataDefPropsConditional.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_addr_method_ref: Optional["SwDataDefPropsConditional.SwAddrMethodRef"] = field(
        default=None,
        metadata={
            "name": "SW-ADDR-METHOD-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_alignment: Optional[AlignmentType] = field(
        default=None,
        metadata={
            "name": "SW-ALIGNMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    base_type_ref: Optional["SwDataDefPropsConditional.BaseTypeRef"] = field(
        default=None,
        metadata={
            "name": "BASE-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_bit_representation: Optional[SwBitRepresentation] = field(
        default=None,
        metadata={
            "name": "SW-BIT-REPRESENTATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_calibration_access: Optional[SwCalibrationAccessEnum] = field(
        default=None,
        metadata={
            "name": "SW-CALIBRATION-ACCESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_value_block_size: Optional[NumericalValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "SW-VALUE-BLOCK-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_calprm_axis_set: Optional[SwCalprmAxisSet] = field(
        default=None,
        metadata={
            "name": "SW-CALPRM-AXIS-SET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_text_props: Optional[SwTextProps] = field(
        default=None,
        metadata={
            "name": "SW-TEXT-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_comparison_variables: Optional["SwDataDefPropsConditional.SwComparisonVariables"] = field(
        default=None,
        metadata={
            "name": "SW-COMPARISON-VARIABLES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    compu_method_ref: Optional["SwDataDefPropsConditional.CompuMethodRef"] = field(
        default=None,
        metadata={
            "name": "COMPU-METHOD-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_constr_ref: Optional["SwDataDefPropsConditional.DataConstrRef"] = field(
        default=None,
        metadata={
            "name": "DATA-CONSTR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_data_dependency: Optional[SwDataDependency] = field(
        default=None,
        metadata={
            "name": "SW-DATA-DEPENDENCY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    display_format: Optional[DisplayFormatString] = field(
        default=None,
        metadata={
            "name": "DISPLAY-FORMAT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    implementation_data_type_ref: Optional["SwDataDefPropsConditional.ImplementationDataTypeRef"] = field(
        default=None,
        metadata={
            "name": "IMPLEMENTATION-DATA-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_host_variable: Optional[SwVariableRefProxy] = field(
        default=None,
        metadata={
            "name": "SW-HOST-VARIABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_impl_policy: Optional[SwImplPolicyEnum] = field(
        default=None,
        metadata={
            "name": "SW-IMPL-POLICY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    additional_native_type_qualifier: Optional[NativeDeclarationString] = field(
        default=None,
        metadata={
            "name": "ADDITIONAL-NATIVE-TYPE-QUALIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_intended_resolution: Optional[NumericalValue] = field(
        default=None,
        metadata={
            "name": "SW-INTENDED-RESOLUTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_interpolation_method: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SW-INTERPOLATION-METHOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    invalid_value: Optional["SwDataDefPropsConditional.InvalidValue"] = field(
        default=None,
        metadata={
            "name": "INVALID-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mc_function: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "MC-FUNCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_is_virtual: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "SW-IS-VIRTUAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_pointer_target_props: Optional[SwPointerTargetProps] = field(
        default=None,
        metadata={
            "name": "SW-POINTER-TARGET-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_record_layout_ref: Optional["SwDataDefPropsConditional.SwRecordLayoutRef"] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_refresh_timing: Optional[MultidimensionalTime] = field(
        default=None,
        metadata={
            "name": "SW-REFRESH-TIMING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    unit_ref: Optional["SwDataDefPropsConditional.UnitRef"] = field(
        default=None,
        metadata={
            "name": "UNIT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    value_axis_data_type_ref: Optional["SwDataDefPropsConditional.ValueAxisDataTypeRef"] = field(
        default=None,
        metadata={
            "name": "VALUE-AXIS-DATA-TYPE-REF",
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
    class SwValueBlockSizeMults:
        numerical_value_variation_point: List[NumericalValueVariationPoint] = field(
            default_factory=list,
            metadata={
                "name": "NUMERICAL-VALUE-VARIATION-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class SwAddrMethodRef(Ref):
        dest: Optional[SwAddrMethodSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class BaseTypeRef(Ref):
        dest: Optional[SwBaseTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SwComparisonVariables:
        """
        :ivar autosar_variable: This represents the reference to a
            Variable in an Autosar system. Note that the target of the
            reference within AutosarVariableRef shall be typed by a
            primitive data type
        :ivar mc_data_instance_var_ref: This reference is used in the
            McSupport file to express the final instance of input values
            etc. It is not allowed to use this outside of an
            McDataInstance. The referenced mcDataInstance shall be
            originated from a VariableDataPrototype.
        """
        autosar_variable: List[AutosarVariableRef] = field(
            default_factory=list,
            metadata={
                "name": "AUTOSAR-VARIABLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        mc_data_instance_var_ref: List["SwDataDefPropsConditional.SwComparisonVariables.McDataInstanceVarRef"] = field(
            default_factory=list,
            metadata={
                "name": "MC-DATA-INSTANCE-VAR-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class McDataInstanceVarRef(Ref):
            dest: Optional[McDataInstanceSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class CompuMethodRef(Ref):
        dest: Optional[CompuMethodSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class DataConstrRef(Ref):
        dest: Optional[DataConstrSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ImplementationDataTypeRef(Ref):
        dest: Optional[AbstractImplementationDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class InvalidValue:
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
    class SwRecordLayoutRef(Ref):
        dest: Optional[SwRecordLayoutSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class UnitRef(Ref):
        dest: Optional[UnitSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ValueAxisDataTypeRef(Ref):
        dest: Optional[ApplicationPrimitiveDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class SwDataDefProps:
    """This class is a collection of properties relevant for data objects under
    various aspects. One could consider this class as a "pattern of inheritance
    by aggregation". The properties can be applied to all objects of all
    classes in which SwDataDefProps is aggregated.

    @RESTRICT_TO_STANDARD:CP:AP!
    Note that not all of the attributes or associated elements are useful all of the time. Hence, the process definition (e.g. expressed with an OCL or a Document Control Instance MSR-DCI) has the task of implementing limitations.
    SwDataDefProps covers various aspects:
    * Structure of the data element for calibration use cases: is it a single value, a curve, or a map, but also the recordLayouts which specify how such elements are mapped/converted to the DataTypes in the programming language (or in AUTOSAR). This is mainly expressed by properties like swRecordLayout and swCalprmAxisSet
    * Implementation aspects, mainly expressed by swImplPolicy, swVariableAccessImplPolicy, swAddrMethod, swPointerTagetProps, baseType, implementationDataType and additionalNativeTypeQualifier
    * Access policy for the MCD system, mainly expressed by swCalibrationAccess
    * Semantics of the data element, mainly expressed by compuMethod and/or unit, dataConstr, invalidValue
    * Code generation policy provided by swRecordLayout
    @END_RESTRICT_TO_STANDARD!

    :ivar sw_data_def_props_variants: This element was
        generated/modified due to an atpVariation stereotype.
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
        name = "SW-DATA-DEF-PROPS"

    sw_data_def_props_variants: Optional["SwDataDefProps.SwDataDefPropsVariants"] = field(
        default=None,
        metadata={
            "name": "SW-DATA-DEF-PROPS-VARIANTS",
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
    class SwDataDefPropsVariants:
        sw_data_def_props_conditional: List[SwDataDefPropsConditional] = field(
            default_factory=list,
            metadata={
                "name": "SW-DATA-DEF-PROPS-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
