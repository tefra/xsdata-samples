from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
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
from .category_string import CategoryString
from .constant_reference import ConstantReference
from .data_transformation_ref_conditional import (
    DataTransformationRefConditional,
)
from .data_type_policy_enum import DataTypePolicyEnum
from .end_to_end_transformation_i_signal_props import (
    EndToEndTransformationISignalProps,
)
from .i_signal_props import ISignalProps
from .i_signal_type_enum import ISignalTypeEnum
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .not_available_value_specification import NotAvailableValueSpecification
from .numerical_rule_based_value_specification import (
    NumericalRuleBasedValueSpecification,
)
from .numerical_value_specification import NumericalValueSpecification
from .ref import Ref
from .reference_value_specification import ReferenceValueSpecification
from .short_name_fragment import ShortNameFragment
from .someip_transformation_i_signal_props import (
    SomeipTransformationISignalProps,
)
from .sw_data_def_props import SwDataDefProps
from .system_signal_subtypes_enum import SystemSignalSubtypesEnum
from .text_value_specification import TextValueSpecification
from .user_defined_transformation_i_signal_props import (
    UserDefinedTransformationISignalProps,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ISignal:
    """Signal of the Interaction Layer.

    The RTE supports a "signal fan-out" where the same System Signal is
    sent in different SignalIPdus to multiple receivers. To support the
    RTE "signal fan-out" each SignalIPdu  contains ISignals. If the same
    System Signal is to be mapped into several SignalIPdus there is one
    ISignal needed for each ISignalToIPduMapping. ISignals describe the
    Interface between the Precompile configured RTE and the potentially
    Postbuild configured Com Stack (see ECUC Parameter Mapping). In case
    of the SystemSignalGroup an ISignal shall be created for each
    SystemSignal contained in the SystemSignalGroup.

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
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar data_transformations: This property was modified due to
        atpVariation (DirectedAssociationPattern).
    :ivar data_type_policy: With the aggregation of SwDataDefProps an
        ISignal specifies how it is represented on the network. This
        representation follows a particular policy. Note that this
        causes some redundancy which is intended and can be used to
        support flexible development methodology as well as subsequent
        integrity checks. If the policy
        "networkRepresentationFromComSpec" is chosen the network
        representation from the ComSpec that is aggregated by the
        PortPrototype shall be used. If the "override" policy is chosen
        the requirements specified in the PortInterface and in the
        ComSpec are not fulfilled by the networkRepresentationProps. In
        case the System Description doesn't use a complete Software
        Component Description (VFB View) the "legacy" policy can be
        chosen.
    :ivar i_signal_props: Additional optional ISignal properties that
        may be stored in different files.
    :ivar i_signal_type: This attribute defines whether this iSignal is
        an array that results in a UINT8_N / UINT8_DYN ComSignalType in
        the COM configuration or a primitive type.
    :ivar init_value: Optional definition of a ISignal's initValue in
        case the System Description doesn't use a complete Software
        Component Description (VFB View). This supports the inclusion of
        legacy system signals. This value can be used to configure the
        Signal's "InitValue". If a full DataMapping exist for the
        SystemSignal this information may be available from a configured
        SenderComSpec and ReceiverComSpec. In this case the initvalues
        in SenderComSpec and/or ReceiverComSpec override this optional
        value specification. Further restrictions apply from the RTE
        specification.
    :ivar length: Size of the signal in bits. The size needs to be
        derived from the mapped VariableDataPrototype according to the
        mapping of primitive DataTypes to BaseTypes as used in the RTE.
        Indicates maximum size for dynamic length signals. The ISignal
        length of zero bits is allowed.
    :ivar network_representation_props: Specification of the actual
        network representation. The usage of SwDataDefProps for this
        purpose is restricted to the attributes compuMethod and
        baseType. The optional baseType attributes "memAllignment" and
        "byteOrder" shall not be used. The attribute "dataTypePolicy" in
        the SystemTemplate element defines whether this network
        representation shall be ignored and the information shall be
        taken over from  the network representation of the ComSpec. If
        "override" is chosen by the system integrator the network
        representation can violate against the requirements defined in
        the PortInterface and in the network representation of the
        ComSpec. In case that the System Description doesn't use a
        complete Software Component Description (VFB View) this element
        is used to configure "ComSignalDataInvalidValue" and the Data
        Semantics.
    :ivar system_signal_ref: Reference to the System Signal that is
        supposed to be transmitted in the ISignal.
    :ivar timeout_substitution_value: Defines and enables the
        ComTimeoutSubstituition for this ISignal.
    :ivar transformation_i_signal_propss: A transformer chain consists
        of an ordered list of transformers. The ISignal specific
        configuration properties for each transformer are defined in the
        TransformationISignalProps class. The transformer configuration
        properties that are common for all ISignals are described in the
        TransformationTechnology class.
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
        name = "I-SIGNAL"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["ISignal.ShortNameFragments"] = field(
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
    annotations: Optional["ISignal.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_transformations: Optional["ISignal.DataTransformations"] = field(
        default=None,
        metadata={
            "name": "DATA-TRANSFORMATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_type_policy: Optional[DataTypePolicyEnum] = field(
        default=None,
        metadata={
            "name": "DATA-TYPE-POLICY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_signal_props: Optional[ISignalProps] = field(
        default=None,
        metadata={
            "name": "I-SIGNAL-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_signal_type: Optional[ISignalTypeEnum] = field(
        default=None,
        metadata={
            "name": "I-SIGNAL-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    init_value: Optional["ISignal.InitValue"] = field(
        default=None,
        metadata={
            "name": "INIT-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    length: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_representation_props: Optional[SwDataDefProps] = field(
        default=None,
        metadata={
            "name": "NETWORK-REPRESENTATION-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    system_signal_ref: Optional["ISignal.SystemSignalRef"] = field(
        default=None,
        metadata={
            "name": "SYSTEM-SIGNAL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_substitution_value: Optional[
        "ISignal.TimeoutSubstitutionValue"
    ] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-SUBSTITUTION-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformation_i_signal_propss: Optional[
        "ISignal.TransformationISignalPropss"
    ] = field(
        default=None,
        metadata={
            "name": "TRANSFORMATION-I-SIGNAL-PROPSS",
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
    class DataTransformations:
        data_transformation_ref_conditional: list[
            DataTransformationRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "DATA-TRANSFORMATION-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class InitValue:
        application_assoc_map_value_specification: Optional[
            ApplicationAssocMapValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "APPLICATION-ASSOC-MAP-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_rule_based_value_specification: Optional[
            ApplicationRuleBasedValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "APPLICATION-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_value_specification: Optional[
            ApplicationValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "APPLICATION-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        array_value_specification: Optional[ArrayValueSpecification] = field(
            default=None,
            metadata={
                "name": "ARRAY-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        composite_rule_based_value_specification: Optional[
            CompositeRuleBasedValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        constant_reference: Optional[ConstantReference] = field(
            default=None,
            metadata={
                "name": "CONSTANT-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        not_available_value_specification: Optional[
            NotAvailableValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "NOT-AVAILABLE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_rule_based_value_specification: Optional[
            NumericalRuleBasedValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "NUMERICAL-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_value_specification: Optional[
            NumericalValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "NUMERICAL-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        record_value_specification: Optional[RecordValueSpecification] = field(
            default=None,
            metadata={
                "name": "RECORD-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        reference_value_specification: Optional[
            ReferenceValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "REFERENCE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        text_value_specification: Optional[TextValueSpecification] = field(
            default=None,
            metadata={
                "name": "TEXT-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SystemSignalRef(Ref):
        dest: Optional[SystemSignalSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TimeoutSubstitutionValue:
        application_assoc_map_value_specification: Optional[
            ApplicationAssocMapValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "APPLICATION-ASSOC-MAP-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_rule_based_value_specification: Optional[
            ApplicationRuleBasedValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "APPLICATION-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_value_specification: Optional[
            ApplicationValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "APPLICATION-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        array_value_specification: Optional[ArrayValueSpecification] = field(
            default=None,
            metadata={
                "name": "ARRAY-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        composite_rule_based_value_specification: Optional[
            CompositeRuleBasedValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        constant_reference: Optional[ConstantReference] = field(
            default=None,
            metadata={
                "name": "CONSTANT-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        not_available_value_specification: Optional[
            NotAvailableValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "NOT-AVAILABLE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_rule_based_value_specification: Optional[
            NumericalRuleBasedValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "NUMERICAL-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_value_specification: Optional[
            NumericalValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "NUMERICAL-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        record_value_specification: Optional[RecordValueSpecification] = field(
            default=None,
            metadata={
                "name": "RECORD-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        reference_value_specification: Optional[
            ReferenceValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "REFERENCE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        text_value_specification: Optional[TextValueSpecification] = field(
            default=None,
            metadata={
                "name": "TEXT-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TransformationISignalPropss:
        end_to_end_transformation_i_signal_props: list[
            EndToEndTransformationISignalProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_transformation_i_signal_props: list[
            SomeipTransformationISignalProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_transformation_i_signal_props: list[
            UserDefinedTransformationISignalProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
