from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .alignment_type import AlignmentType
from .c_identifier import CIdentifier
from .category_string import CategoryString
from .executable_entity_subtypes_enum import ExecutableEntitySubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .section_name_prefix_subtypes_enum import SectionNamePrefixSubtypesEnum
from .short_name_fragment import ShortNameFragment
from .sw_addr_method_subtypes_enum import SwAddrMethodSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MemorySection:
    """
    Provides a description of an abstract memory section used in the
    Implementation for code or data.

    It shall be declared by the Implementation Description of the module or
    component, which actually allocates the memory in its code. This means
    in case of data prototypes which are allocated by the RTE, that the
    generated Implementation Description of the RTE shall contain the
    corresponding MemorySections. The attribute "symbol" (if symbol is
    missing: "shortName") defines the module or component specific section
    name used in the code. For details see the document "Specification of
    Memory Mapping". Typically the section name is build according the
    pattern: &lt;SwAddrMethod shortName&gt;[_&lt;further specialization
    nominator&gt;][_&lt;alignment&gt;] where * '''[&lt;SwAddrMethod
    shortName&gt;]''' is the shortName of the referenced SwAddrMethod *
    '''[_&lt;further specialization nominator&gt;]''' is an optional infix
    to indicate the specialization in the case that several MemorySections
    for different purpose of the same Implementation Description referring
    to the same or equally named SwAddrMethods. *
    '''[_&lt;alignment&gt;]''' is the alignment attributes value and is
    only applicable in the case that the memoryAllocationKeywordPolicy
    value of the referenced SwAddrMethod is set to
    addrMethodShortNameAndAlignment MemorySection used to Implement the
    code of RunnableEntitys and BswSchedulableEntitys shall have a symbol
    (if missing: shortName) identical to the referred SwAddrMethod to
    conform to the generated RTE header files. In addition to the section
    name described above, a prefix is used in the corresponding macro code
    in order to define a name space. This prefix is by default given by the
    shortName of the BswModuleDescription resp. the SwComponentType. It can
    be superseded by the prefix attribute.

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
    :ivar alignment: The attribute describes the alignment of objects
        within this memory section.
    :ivar executable_entity_refs: Reference to the ExecutableEntitites
        located in this section. This allows to locate different
        ExecutableEntitities in different sections even if the
        associated SwAddrmethod is the same. This is applicable to code
        sections only.
    :ivar mem_class_symbol: Defines a specific  symbol in order to
        generate the compiler abstraction  "memclass" code for this
        MemorySection. The existence of this attribute supersedes the
        usage of swAddrmethod.shortName for this purpose. The complete
        name of the  "memclass" preprocessor symbol is constructed as
        &lt;prefix&gt;_&lt;memClassSymbol&gt; where prefix is defined in
        the same way as for the enclosing MemorySection. See also
        AUTOSAR_SWS_CompilerAbstraction SWS_COMPILER_00040.
    :ivar options:
    :ivar prefix_ref: The prefix used to set the memory section's
        namespace in the code. The existence of a prefix element
        supersedes rules for a default prefix (such as the
        BswModuleDescription's shortName). This allows the user to
        define several name spaces for memory sections within the scope
        of one module, cluster or SWC.
    :ivar size: The size in bytes of the section.
    :ivar sw_addrmethod_ref: This association indicates that this module
        specific (abstract) memory section is part of an overall
        SwAddrMethod, referred by the upstream declarations (e.g.
        calibration parameters, data element prototypes, code entities)
        which share a common addressing strategy. This can be evaluated
        for the ECU configuration of the build support. This association
        shall always be declared by the Implementation description of
        the module or component, which allocates the memory in its code.
        This means in case of data prototypes which are allocated by the
        RTE, that the software components only declare the grouping of
        its data prototypes to SwAddrMethods, and the generated
        Implementation Description of the RTE actually sets up this
        association.
    :ivar symbol: Defines the section name as explained in the main
        description. By using this attribute for code generation
        (instead of the shortName) it is possible to define several
        different MemorySections having the same name - e.g. symbol =
        CODE - but using different sectionNamePrefixes.
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
        name = "MEMORY-SECTION"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["MemorySection.ShortNameFragments"] = field(
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
    annotations: Optional["MemorySection.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    alignment: Optional[AlignmentType] = field(
        default=None,
        metadata={
            "name": "ALIGNMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    executable_entity_refs: Optional["MemorySection.ExecutableEntityRefs"] = (
        field(
            default=None,
            metadata={
                "name": "EXECUTABLE-ENTITY-REFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    mem_class_symbol: Optional[CIdentifier] = field(
        default=None,
        metadata={
            "name": "MEM-CLASS-SYMBOL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    options: Optional["MemorySection.Options"] = field(
        default=None,
        metadata={
            "name": "OPTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    prefix_ref: Optional["MemorySection.PrefixRef"] = field(
        default=None,
        metadata={
            "name": "PREFIX-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_addrmethod_ref: Optional["MemorySection.SwAddrmethodRef"] = field(
        default=None,
        metadata={
            "name": "SW-ADDRMETHOD-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    symbol: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SYMBOL",
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
    class ExecutableEntityRefs:
        executable_entity_ref: list[
            "MemorySection.ExecutableEntityRefs.ExecutableEntityRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTABLE-ENTITY-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ExecutableEntityRef(Ref):
            dest: Optional[ExecutableEntitySubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class Options:
        """
        :ivar option: This attribute introduces the ability to specify
            further intended properties of this MemorySection. The
            following two values are standardized (to be used for code
            sections only and exclusively to each other): * INLINE - The
            code section is declared with the compiler abstraction macro
            INLINE. * LOCAL_INLINE  - The code section is declared with
            the compiler abstraction macro LOCAL_INLINE In both cases
            (INLINE and LOCAL_INLINE) the inline expansion depends on
            the compiler specific implementation of these macros.
            Depending on this, the code section either corresponds to an
            actual section in memory or is put into the section of the
            caller. See AUTOSAR_SWS_CompilerAbstraction for more
            details.
        """

        option: list[Identifier] = field(
            default_factory=list,
            metadata={
                "name": "OPTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PrefixRef(Ref):
        dest: Optional[SectionNamePrefixSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SwAddrmethodRef(Ref):
        dest: Optional[SwAddrMethodSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
