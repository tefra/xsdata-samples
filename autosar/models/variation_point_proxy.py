from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .boolean_value_variation_point import BooleanValueVariationPoint
from .category_string import CategoryString
from .condition_by_formula import ConditionByFormula
from .diagnostic_debounce_behavior_enum_value_variation_point import (
    DiagnosticDebounceBehaviorEnumValueVariationPoint,
)
from .diagnostic_indicator_type_enum_value_variation_point import (
    DiagnosticIndicatorTypeEnumValueVariationPoint,
)
from .diagnostic_test_result_update_enum_value_variation_point import (
    DiagnosticTestResultUpdateEnumValueVariationPoint,
)
from .diagnostic_wwh_obd_dtc_class_enum_value_variation_point import (
    DiagnosticWwhObdDtcClassEnumValueVariationPoint,
)
from .float_value_variation_point import FloatValueVariationPoint
from .identifier import Identifier
from .implementation_data_type_subtypes_enum import (
    ImplementationDataTypeSubtypesEnum,
)
from .integer_value_variation_point import IntegerValueVariationPoint
from .limit import Limit
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .name_token_value_variation_point import NameTokenValueVariationPoint
from .numerical_value_variation_point import NumericalValueVariationPoint
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .post_build_variant_condition import PostBuildVariantCondition
from .post_build_variant_criterion_subtypes_enum import (
    PostBuildVariantCriterionSubtypesEnum,
)
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .time_value_value_variation_point import TimeValueValueVariationPoint
from .unlimited_integer_value_variation_point import (
    UnlimitedIntegerValueVariationPoint,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class VariationPointProxy:
    """
    The VariationPointProxy represents variation points of the C/C++
    implementation.

    In case of bindingTime = compileTime the RTE provides defines which can
    be used for Pre Processor directives to implement compileTime
    variability.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar condition_access: This condition acts as Binding Function for
        the VariationPoint.
    :ivar implementation_data_type_ref: This association to
        ImplementationDataType shall be taken as an implementation hint
        by the RTE generator.
    :ivar post_build_value_access_ref: This represents the applicable
        PostBuildVariantCriterion in the context of a
        VariationPointProxy. Note that the technical details how to
        access the particular postBuildValueAccess are still considered
        internal to the RTE and are consequently not standardized.
    :ivar post_build_variant_conditions: This represents that applicable
        PostBuoldVariantCondition in the context of
        aVariationPointProxy.
    :ivar value_access: This value acts as Binding Function for the
        VariationPoint.
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
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "VARIATION-POINT-PROXY"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional[
        "VariationPointProxy.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["VariationPointProxy.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    condition_access: Optional[ConditionByFormula] = field(
        default=None,
        metadata={
            "name": "CONDITION-ACCESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implementation_data_type_ref: Optional[
        "VariationPointProxy.ImplementationDataTypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "IMPLEMENTATION-DATA-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    post_build_value_access_ref: Optional[
        "VariationPointProxy.PostBuildValueAccessRef"
    ] = field(
        default=None,
        metadata={
            "name": "POST-BUILD-VALUE-ACCESS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    post_build_variant_conditions: Optional[
        "VariationPointProxy.PostBuildVariantConditions"
    ] = field(
        default=None,
        metadata={
            "name": "POST-BUILD-VARIANT-CONDITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    value_access: Optional["VariationPointProxy.ValueAccess"] = field(
        default=None,
        metadata={
            "name": "VALUE-ACCESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ImplementationDataTypeRef(Ref):
        dest: Optional[ImplementationDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class PostBuildValueAccessRef(Ref):
        dest: Optional[PostBuildVariantCriterionSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class PostBuildVariantConditions:
        post_build_variant_condition: list[PostBuildVariantCondition] = field(
            default_factory=list,
            metadata={
                "name": "POST-BUILD-VARIANT-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ValueAccess:
        boolean_value_variation_point: Optional[BooleanValueVariationPoint] = (
            field(
                default=None,
                metadata={
                    "name": "BOOLEAN-VALUE-VARIATION-POINT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_debounce_behavior_enum_value_variation_point: Optional[
            DiagnosticDebounceBehaviorEnumValueVariationPoint
        ] = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-DEBOUNCE-BEHAVIOR-ENUM-VALUE-VARIATION-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_indicator_type_enum_value_variation_point: Optional[
            DiagnosticIndicatorTypeEnumValueVariationPoint
        ] = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-INDICATOR-TYPE-ENUM-VALUE-VARIATION-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_test_result_update_enum_value_variation_point: Optional[
            DiagnosticTestResultUpdateEnumValueVariationPoint
        ] = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-TEST-RESULT-UPDATE-ENUM-VALUE-VARIATION-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_wwh_obd_dtc_class_enum_value_variation_point: Optional[
            DiagnosticWwhObdDtcClassEnumValueVariationPoint
        ] = field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-WWH-OBD-DTC-CLASS-ENUM-VALUE-VARIATION-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        float_value_variation_point: Optional[FloatValueVariationPoint] = (
            field(
                default=None,
                metadata={
                    "name": "FLOAT-VALUE-VARIATION-POINT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        integer_value_variation_point: Optional[IntegerValueVariationPoint] = (
            field(
                default=None,
                metadata={
                    "name": "INTEGER-VALUE-VARIATION-POINT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        limit: Optional[Limit] = field(
            default=None,
            metadata={
                "name": "LIMIT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        name_token_value_variation_point: Optional[
            NameTokenValueVariationPoint
        ] = field(
            default=None,
            metadata={
                "name": "NAME-TOKEN-VALUE-VARIATION-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_value_variation_point: Optional[
            NumericalValueVariationPoint
        ] = field(
            default=None,
            metadata={
                "name": "NUMERICAL-VALUE-VARIATION-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        positive_integer_value_variation_point: Optional[
            PositiveIntegerValueVariationPoint
        ] = field(
            default=None,
            metadata={
                "name": "POSITIVE-INTEGER-VALUE-VARIATION-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        time_value_value_variation_point: Optional[
            TimeValueValueVariationPoint
        ] = field(
            default=None,
            metadata={
                "name": "TIME-VALUE-VALUE-VARIATION-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        unlimited_integer_value_variation_point: Optional[
            UnlimitedIntegerValueVariationPoint
        ] = field(
            default=None,
            metadata={
                "name": "UNLIMITED-INTEGER-VALUE-VARIATION-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
