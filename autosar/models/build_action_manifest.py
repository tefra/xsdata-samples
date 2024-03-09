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
from .build_action import BuildAction
from .build_action_environment import BuildActionEnvironment
from .build_action_subtypes_enum import BuildActionSubtypesEnum
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BuildActionManifest:
    """This meta-class represents the ability to specify a manifest for processing
    artifacts.

    An example use case is the processing of ECUC parameter values.

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
    :ivar start_action_refs: This specifies the list of actions to be
        performed at the beginning of the process.
    :ivar tear_down_action_refs: This specifies the set of action which
        shall be performed after all other actions in the manifest were
        performed.
    :ivar build_actions: This represents a particular action in the
        build chain. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar build_action_environments: This represents a build action
        environment. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar dynamic_action_refs: This denots an Action which is to be
        executed as part of the dynamic action set.
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
        name = "BUILD-ACTION-MANIFEST"

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
        "BuildActionManifest.ShortNameFragments"
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
    annotations: Optional["BuildActionManifest.Annotations"] = field(
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
    blueprint_policys: Optional["BuildActionManifest.BlueprintPolicys"] = (
        field(
            default=None,
            metadata={
                "name": "BLUEPRINT-POLICYS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    short_name_pattern: Optional[String] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    start_action_refs: Optional["BuildActionManifest.StartActionRefs"] = field(
        default=None,
        metadata={
            "name": "START-ACTION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tear_down_action_refs: Optional[
        "BuildActionManifest.TearDownActionRefs"
    ] = field(
        default=None,
        metadata={
            "name": "TEAR-DOWN-ACTION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    build_actions: Optional["BuildActionManifest.BuildActions"] = field(
        default=None,
        metadata={
            "name": "BUILD-ACTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    build_action_environments: Optional[
        "BuildActionManifest.BuildActionEnvironments"
    ] = field(
        default=None,
        metadata={
            "name": "BUILD-ACTION-ENVIRONMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dynamic_action_refs: Optional["BuildActionManifest.DynamicActionRefs"] = (
        field(
            default=None,
            metadata={
                "name": "DYNAMIC-ACTION-REFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    class StartActionRefs:
        start_action_ref: List[
            "BuildActionManifest.StartActionRefs.StartActionRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "START-ACTION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class StartActionRef(Ref):
            dest: Optional[BuildActionSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class TearDownActionRefs:
        tear_down_action_ref: List[
            "BuildActionManifest.TearDownActionRefs.TearDownActionRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "TEAR-DOWN-ACTION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class TearDownActionRef(Ref):
            dest: Optional[BuildActionSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class BuildActions:
        build_action: List[BuildAction] = field(
            default_factory=list,
            metadata={
                "name": "BUILD-ACTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class BuildActionEnvironments:
        build_action_environment: List[BuildActionEnvironment] = field(
            default_factory=list,
            metadata={
                "name": "BUILD-ACTION-ENVIRONMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DynamicActionRefs:
        dynamic_action_ref: List[
            "BuildActionManifest.DynamicActionRefs.DynamicActionRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "DYNAMIC-ACTION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DynamicActionRef(Ref):
            dest: Optional[BuildActionSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
