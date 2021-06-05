from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.array_impl_policy_enum import ArrayImplPolicyEnum
from autosar.models.array_size_handling_enum import ArraySizeHandlingEnum
from autosar.models.array_size_semantics_enum import ArraySizeSemanticsEnum
from autosar.models.boolean import Boolean
from autosar.models.category_string import CategoryString
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.positive_integer_value_variation_point import PositiveIntegerValueVariationPoint
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.sw_pointer_target_props import SwDataDefProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ImplementationDataTypeElement:
    """Declares a data object which is locally aggregated. Such an element can
    only be used within the scope where it is aggregated. This element either
    consists of further subElements or it is further defined via its
    swDataDefProps. There are several use cases within the system of
    ImplementationDataTypes fur such a local declaration:

    * It can represent the elements of an array, defining the element type and array size
    * It can represent an element of a struct, defining its type
    * It can be the local declaration of a debug element.

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
    :ivar array_impl_policy: This attribute controls the implementation
        of the payload of an array. It shall only be used if the
        enclosing ImplementationDataType constitutes an array.
    :ivar array_size: The existence of this attributes (if bigger than
        0) defines the size of an array and declares that this
        ImplementationDataTypeElement represents the type of each single
        array element.
    :ivar array_size_handling: The way how the size of the array is
        handled in case of a variable size array.
    :ivar array_size_semantics: This attribute controls the meaning of
        the value of the array size.
    :ivar is_optional: This attribute represents the ability to declare
        the enclosing ImplementationDataTypeElement as optional. This
        means that, at runtime, the ImplementationDataTypeElement may or
        may not have a valid value and shall therefore be ignored. The
        underlying runtime software provides means to set the
        CppImplementationDataTypeElement as not valid at the sending end
        of a communication and determine its validity at the receiving
        end.
    :ivar sub_elements: Element of an array, struct, or union in case of
        a nested declaration (i.e. without using "typedefs"). The
        aggregation of ImplementionDataTypeElement is subject to
        variability with the purpose to support the conditional
        existence of elements inside a ImplementationDataType
        representing a structure. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar sw_data_def_props: The properties of this
        ImplementationDataTypeElement.
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
        name = "IMPLEMENTATION-DATA-TYPE-ELEMENT"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["ImplementationDataTypeElement.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["ImplementationDataTypeElement.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    array_impl_policy: Optional[ArrayImplPolicyEnum] = field(
        default=None,
        metadata={
            "name": "ARRAY-IMPL-POLICY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    array_size: Optional[PositiveIntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "ARRAY-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    array_size_handling: Optional[ArraySizeHandlingEnum] = field(
        default=None,
        metadata={
            "name": "ARRAY-SIZE-HANDLING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    array_size_semantics: Optional[ArraySizeSemanticsEnum] = field(
        default=None,
        metadata={
            "name": "ARRAY-SIZE-SEMANTICS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    is_optional: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "IS-OPTIONAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sub_elements: Optional["ImplementationDataTypeElement.SubElements"] = field(
        default=None,
        metadata={
            "name": "SUB-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_data_def_props: Optional[SwDataDefProps] = field(
        default=None,
        metadata={
            "name": "SW-DATA-DEF-PROPS",
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
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        }
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
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
    class SubElements:
        implementation_data_type_element: List["ImplementationDataTypeElement"] = field(
            default_factory=list,
            metadata={
                "name": "IMPLEMENTATION-DATA-TYPE-ELEMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
