from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
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
from .ref import Ref
from .rpt_executable_entity_properties import RptExecutableEntityProperties
from .rpt_hook import RptHook
from .rpt_impl_policy import RptImplPolicy
from .rpt_profile_subtypes_enum import RptProfileSubtypesEnum
from .rpt_sw_prototyping_access import RptSwPrototypingAccess
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RptContainer:
    """This meta class defines a byPassPoint and the relation to a rptHook.

    Additionally it may contain further rptContainers if the byPassPoint
    is not atomic. For example a byPassPoint refereing to a
    RunnableEntity may contain rptContainers referring to the data
    access points of the RunnableEntity. The RptContainer structure on
    M1 shall follow the M1 structure of the Software Component
    Descriptions. The category attribute denotes which level of the
    Software Component Description is annotated.

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
    :ivar by_pass_point_irefs: byPassPoint desribes the required
        preparation of the host ECU. At a byPassPoint  the host ECU
        shall be capable to communicate with a RPT System in order to
        support the execution of the rapid prototyping algorithms with
        the original data calculated by the host system and to replace
        dedicated results of  the host system by the results of the
        rapid prototyping algorithm. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar explicit_rpt_profile_selection_refs: This attribute defines
        the applicable RptProfiles for the specific RptContainer. If not
        any references to a specific RptProfile is defined, all
        RptProfiles defined in the RapidPrototypingScenario are
        applicable.
    :ivar rpt_containers: Sub-level rptContainer definitions of this
        specific rapid prototyping scenario. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar rpt_executable_entity_properties: Describes the required code
        preparation for rapid prototyping at ExecutableEntity
        invocation.
    :ivar rpt_hooks: The rptHook describes the link between a
        byPassPoint and the rapid prototyping algorithm. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar rpt_impl_policy: Describes the required code preparation for
        rapid prototyping at data accesses.
    :ivar rpt_sw_prototyping_access: Describes the required
        accessibility of data and modes by the rapid prototyping
        tooling.
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
        name = "RPT-CONTAINER"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["RptContainer.ShortNameFragments"] = field(
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
    annotations: Optional["RptContainer.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    by_pass_point_irefs: Optional["RptContainer.ByPassPointIrefs"] = field(
        default=None,
        metadata={
            "name": "BY-PASS-POINT-IREFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    explicit_rpt_profile_selection_refs: Optional[
        "RptContainer.ExplicitRptProfileSelectionRefs"
    ] = field(
        default=None,
        metadata={
            "name": "EXPLICIT-RPT-PROFILE-SELECTION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_containers: Optional["RptContainer.RptContainers"] = field(
        default=None,
        metadata={
            "name": "RPT-CONTAINERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_executable_entity_properties: Optional[
        RptExecutableEntityProperties
    ] = field(
        default=None,
        metadata={
            "name": "RPT-EXECUTABLE-ENTITY-PROPERTIES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_hooks: Optional["RptContainer.RptHooks"] = field(
        default=None,
        metadata={
            "name": "RPT-HOOKS",
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
    rpt_sw_prototyping_access: Optional[RptSwPrototypingAccess] = field(
        default=None,
        metadata={
            "name": "RPT-SW-PROTOTYPING-ACCESS",
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
    class ByPassPointIrefs:
        by_pass_point_iref: List[AnyInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "BY-PASS-POINT-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ExplicitRptProfileSelectionRefs:
        explicit_rpt_profile_selection_ref: List[
            "RptContainer.ExplicitRptProfileSelectionRefs.ExplicitRptProfileSelectionRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "EXPLICIT-RPT-PROFILE-SELECTION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ExplicitRptProfileSelectionRef(Ref):
            dest: Optional[RptProfileSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class RptContainers:
        rpt_container: List["RptContainer"] = field(
            default_factory=list,
            metadata={
                "name": "RPT-CONTAINER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RptHooks:
        rpt_hook: List[RptHook] = field(
            default_factory=list,
            metadata={
                "name": "RPT-HOOK",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
