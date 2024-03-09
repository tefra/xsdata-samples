from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .flat_instance_descriptor_subtypes_enum import (
    FlatInstanceDescriptorSubtypesEnum,
)
from .identifier import Identifier
from .implementation_element_in_parameter_instance_ref import (
    ImplementationElementInParameterInstanceRef,
)
from .mc_data_access_details import McDataAccessDetails
from .mcd_identifier import McdIdentifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .role_based_mc_data_assignment import RoleBasedMcDataAssignment
from .rpt_impl_policy import RptImplPolicy
from .rpt_sw_prototyping_access import RptSwPrototypingAccess
from .short_name_fragment import ShortNameFragment
from .sw_data_def_props import SwDataDefProps
from .symbol_string import SymbolString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class McDataInstance:
    """Describes the specific properties of one data instance in order to support
    measurement and/or calibration of this data instance.

    The most important attributes are:
    * Its shortName is copied from the ECU Flat map (if applicable) and will be used as identifier and for display by the MC system.
    * The category is copied from the corresponding data type (ApplicationDataType if defined, otherwise ImplementationDataType) as far as applicable.
    * The symbol is the one used in the programming language. It will be used to find out the actual memory address by the final generation tool with the help of linker generated information.
    It is assumed that in the M1 model this part and all the aggregated and referred elements (with the exception of the Flat Map and the references from ImplementationElementInParameterInstanceRef and McAccessDetails) are completely generated from "upstream" information. This means, that even if an element like e.g. a CompuMethod is only used via reference here, it will be copied into the M1 artifact which holds the complete McSupportData for a given Implementation.

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
    :ivar array_size: The existence of this attribute turns the data
        instance into an array of data. The attribute determines the
        size of the array in terms of number of elements.
    :ivar display_identifier: An optional attribute to be used to set
        the ASAM ASAP2 DISPLAY_IDENTIFIER attribute.
    :ivar flat_map_entry_ref: Reference to the corresponding entry in
        the ECU Flat Map. This allows to trace back to the original
        specification of the generated data instance. This link shall be
        added by the RTE generator mainly for documentation purposes.
        The reference is optional because * The McDataInstance may
        represent an array or struct in which only the subElements
        correspond to FlatMap entries. * The McDataInstance may
        represent a task local buffer for rapid prototyping access which
        is different from the "main instance" used for measurement
        access.
    :ivar instance_in_memory: Reference to the corresponding data
        instance in the description of calibration data structures
        published by the RTE generator. This is used to support
        emulation methods inside the ECU, it is not required for A2L
        generation.
    :ivar mc_data_access_details: Refers to "upstream" information on
        how the RTE uses this data instance. Use Case: Rapid Prototyping
    :ivar mc_data_assignments: An assignment between McDataInstances.
        This supports the indication of related McDataElement
        implementing the of „RP global buffer", „RP global measurement
        buffer", „RP enabler flag".
    :ivar resulting_properties: These are the generated properties
        resulting from decisions taken by the RTE  generator for the
        actually implemented data instance. Only those properties are
        relevant here, which are needed for the measurement and
        calibration system.
    :ivar resulting_rpt_sw_prototyping_access: Describes the implemented
        accessibility of data and modes by the rapid prototyping
        tooling.
    :ivar role: An optional attribute to be used for additional
        information on the role of this data instance, for example in
        the context of rapid prototyping.
    :ivar rpt_impl_policy: Describes the implemented code preparation
        for rapid prototyping at data accesses for a hook based
        bypassing.
    :ivar sub_elements: This relation indicates, that the target element
        is part of a "struct" which is given by the source element. This
        information will be used by the final generator to set up the
        correct addressing scheme. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar symbol: This String is used to determine the memory address
        during final generation of the MC configuration data (e.g. "A2L"
        file) . It shall be the name of the element in the programming
        language such that it can be identified in linker generated
        information. In case the McDataInstance is part of composite
        data in the programming language, the symbol String may include
        parts denoting the element context, unless the context is given
        by the symbol attribute of an enclosing McDataInstance. This
        means in particular for the C language that the "." character
        shall be used as a separator between the name of a "struct"
        variable the name of one of its elements. The symbol can differ
        from the shortName in case of generated C data declarations. It
        is an optional attribute since it may be missing in case the
        instance represents an element (e.g. a single array element)
        which has no name in the linker map.
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
        name = "MC-DATA-INSTANCE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["McDataInstance.ShortNameFragments"] = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    annotations: Optional["McDataInstance.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    array_size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "ARRAY-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    display_identifier: Optional[McdIdentifier] = field(
        default=None,
        metadata={
            "name": "DISPLAY-IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    flat_map_entry_ref: Optional["McDataInstance.FlatMapEntryRef"] = field(
        default=None,
        metadata={
            "name": "FLAT-MAP-ENTRY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    instance_in_memory: Optional[
        ImplementationElementInParameterInstanceRef
    ] = field(
        default=None,
        metadata={
            "name": "INSTANCE-IN-MEMORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mc_data_access_details: Optional[McDataAccessDetails] = field(
        default=None,
        metadata={
            "name": "MC-DATA-ACCESS-DETAILS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mc_data_assignments: Optional["McDataInstance.McDataAssignments"] = field(
        default=None,
        metadata={
            "name": "MC-DATA-ASSIGNMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    resulting_properties: Optional[SwDataDefProps] = field(
        default=None,
        metadata={
            "name": "RESULTING-PROPERTIES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    resulting_rpt_sw_prototyping_access: Optional[RptSwPrototypingAccess] = (
        field(
            default=None,
            metadata={
                "name": "RESULTING-RPT-SW-PROTOTYPING-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    role: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_impl_policy: Optional[RptImplPolicy] = field(
        default=None,
        metadata={
            "name": "RPT-IMPL-POLICY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sub_elements: Optional["McDataInstance.SubElements"] = field(
        default=None,
        metadata={
            "name": "SUB-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    symbol: Optional[SymbolString] = field(
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
    class FlatMapEntryRef(Ref):
        dest: Optional[FlatInstanceDescriptorSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class McDataAssignments:
        role_based_mc_data_assignment: List[RoleBasedMcDataAssignment] = field(
            default_factory=list,
            metadata={
                "name": "ROLE-BASED-MC-DATA-ASSIGNMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SubElements:
        mc_data_instance: List["McDataInstance"] = field(
            default_factory=list,
            metadata={
                "name": "MC-DATA-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
