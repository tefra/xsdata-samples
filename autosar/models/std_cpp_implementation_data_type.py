from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .blueprint_policy_list import BlueprintPolicyList
from .blueprint_policy_not_modifiable import BlueprintPolicyNotModifiable
from .blueprint_policy_single import BlueprintPolicySingle
from .category_string import CategoryString
from .cpp_implementation_data_type_element import (
    CppImplementationDataTypeElement,
)
from .cpp_implementation_data_type_subtypes_enum import (
    CppImplementationDataTypeSubtypesEnum,
)
from .cpp_template_argument import CppTemplateArgument
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nmtoken_string import NmtokenString
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .string import String
from .sw_data_def_props import SwDataDefProps
from .symbol_props import SymbolProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class StdCppImplementationDataType:
    """
    This meta-class represents the way to specify a data type definition that is
    taken as the basis for a C++ language binding to a C++ Standard Library
    feature.

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
    :ivar blueprint_policys: This role indicates whether the
        blueprintable element will be modifiable or not motifiable.
    :ivar short_name_pattern: This attribute represents the pattern
        which shall be used to build the shortName of the derived
        elements. As of now it is modeled as a String.  In general it
        should follow the pattern: pattern = (placeholder | namePart)*
        placeholder = "{" namePart "}" namePart = identifier | "_" This
        is subject to be refined in subsequent versions. Note that this
        is marked as obsolete. Use the xml attribute namePattern instead
        as it applies to Identifier and CIdentifier (shortName, symbol
        etc.)
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar sw_data_def_props: The properties of this AutosarDataType.
    :ivar array_size: This attribute can be used to specify the array
        size if the enclosing CppImplementationDataType has array
        semantics.
    :ivar header_file: Configuration of the Header File with the custom
        class declaration.
    :ivar namespaces: This aggregation allows for the definition an own
        namespace for the enclosing CppImplementationDataType.
    :ivar sub_elements: This represents the collection of sub-elements
        of the enclosing CppImplementationDataType
    :ivar template_arguments: This aggreation allows for the
        specification of properties of template arguments
    :ivar type_emitter: This attribute can be taken to control how the
        respective CppImplementationDataType is contributed to the
        language binding.
    :ivar type_reference_ref: This reference shall be defined to define
        a type reference (a.k.a. typedef).
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
        name = "STD-CPP-IMPLEMENTATION-DATA-TYPE"

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
        "StdCppImplementationDataType.ShortNameFragments"
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
    annotations: Optional["StdCppImplementationDataType.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    blueprint_policys: Optional[
        "StdCppImplementationDataType.BlueprintPolicys"
    ] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    short_name_pattern: Optional[String] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-PATTERN",
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
    sw_data_def_props: Optional[SwDataDefProps] = field(
        default=None,
        metadata={
            "name": "SW-DATA-DEF-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    array_size: Optional[PositiveIntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "ARRAY-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    header_file: Optional[String] = field(
        default=None,
        metadata={
            "name": "HEADER-FILE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    namespaces: Optional["StdCppImplementationDataType.Namespaces"] = field(
        default=None,
        metadata={
            "name": "NAMESPACES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sub_elements: Optional["StdCppImplementationDataType.SubElements"] = field(
        default=None,
        metadata={
            "name": "SUB-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    template_arguments: Optional[
        "StdCppImplementationDataType.TemplateArguments"
    ] = field(
        default=None,
        metadata={
            "name": "TEMPLATE-ARGUMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    type_emitter: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "TYPE-EMITTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    type_reference_ref: Optional[
        "StdCppImplementationDataType.TypeReferenceRef"
    ] = field(
        default=None,
        metadata={
            "name": "TYPE-REFERENCE-REF",
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
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class BlueprintPolicys:
        blueprint_policy_list: List[BlueprintPolicyList] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        blueprint_policy_not_modifiable: List[BlueprintPolicyNotModifiable] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BLUEPRINT-POLICY-NOT-MODIFIABLE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        blueprint_policy_single: List[BlueprintPolicySingle] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-SINGLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Namespaces:
        symbol_props: List[SymbolProps] = field(
            default_factory=list,
            metadata={
                "name": "SYMBOL-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SubElements:
        cpp_implementation_data_type_element: List[
            CppImplementationDataTypeElement
        ] = field(
            default_factory=list,
            metadata={
                "name": "CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TemplateArguments:
        cpp_template_argument: List[CppTemplateArgument] = field(
            default_factory=list,
            metadata={
                "name": "CPP-TEMPLATE-ARGUMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TypeReferenceRef(Ref):
        dest: Optional[CppImplementationDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
