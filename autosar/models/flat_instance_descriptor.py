from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .any_instance_ref import AnyInstanceRef
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .rte_plugin_props import RtePluginProps
from .short_name_fragment import ShortNameFragment
from .sw_pointer_target_props import SwDataDefProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlatInstanceDescriptor:
    """Represents exactly one node (e.g. a component instance or data element) of
    the instance tree of a software system.

    The purpose of this element is to map the various nested representations of this instance to a flat representation and assign a unique name (shortName) to it.
    Use cases:
    * Specify unique names of measurable data to be used by MCD tools
    * Specify unique names of calibration data to be used by MCD tool
    * Specify a unique name for an instance of a component prototype in the ECU extract of the system description
    Note that in addition it is possible to assign alias names via AliasNameAssignment.

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
    :ivar role: The role denotes the particular role of the downstream
        memory location described by this FlatInstanceDescriptor. It
        applies to use case where one upstream object results in
        multiple downstream objects, e.g. ModeDeclarationGroupPrototypes
        which are measurable. In this case the RTE will provide
        locations for current mode, previous mode and next mode.
    :ivar rte_plugin_props: The properties of a communication graph with
        respect to the utilization of RTE Implementation Plug-in.
    :ivar sw_data_def_props: The properties of this
        FlatInstanceDescriptor.
    :ivar upstream_reference_iref: Refers to the instance in the context
        of an "upstream" descriptions, wich could be the system or
        system extract description, the basic software module
        description or (if a flat map is used in preliminary context) a
        description of an atomic component or composition. This
        reference is optional in case the flat map is used in ECU
        context. The reference shall be such that it uniquely defines
        the object instance in the given context. For example, if a data
        prototype is declared as a role within an SwcInternalBehavior,
        it is not enough to state the SwcInternalBehavior as context and
        the aggregated data prototype as target. In addition, the
        reference shall also include the complete path identifying the
        instance of the component prototype that contains the particular
        instance of SwcInternalBehavior.
    :ivar ecu_extract_reference_iref: Refers to the instance in the ECU
        extract. This is valid only, if the FlatMap is used in the
        context of an ECU extract. The reference shall be such that it
        uniquely defines the object instance. For example, if a data
        prototype is declared as a role within an SwcInternalBehavior,
        it is not enough to state the SwcInternalBehavior as context and
        the aggregated data prototype as target. In addition, the
        reference shall also include the complete path identifying
        instance of the component prototype and the
        AtomicSoftwareComponentType, which is refered by the particular
        SwcInternalBehavior.
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
        name = "FLAT-INSTANCE-DESCRIPTOR"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["FlatInstanceDescriptor.ShortNameFragments"] = field(
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
    annotations: Optional["FlatInstanceDescriptor.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    role: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rte_plugin_props: Optional[RtePluginProps] = field(
        default=None,
        metadata={
            "name": "RTE-PLUGIN-PROPS",
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
    upstream_reference_iref: Optional[AnyInstanceRef] = field(
        default=None,
        metadata={
            "name": "UPSTREAM-REFERENCE-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ecu_extract_reference_iref: Optional[AnyInstanceRef] = field(
        default=None,
        metadata={
            "name": "ECU-EXTRACT-REFERENCE-IREF",
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
