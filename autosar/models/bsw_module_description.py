from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .blueprint_policy_list import BlueprintPolicyList
from .blueprint_policy_not_modifiable import BlueprintPolicyNotModifiable
from .blueprint_policy_single import BlueprintPolicySingle
from .bsw_internal_behavior import BswInternalBehavior
from .bsw_module_client_server_entry import BswModuleClientServerEntry
from .bsw_module_dependency import BswModuleDependency
from .bsw_module_entry_ref_conditional import BswModuleEntryRefConditional
from .category_string import CategoryString
from .identifier import Identifier
from .mode_declaration_group_prototype import ModeDeclarationGroupPrototype
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .short_name_fragment import ShortNameFragment
from .string import String
from .sw_component_documentation import SwComponentDocumentation
from .trigger import Trigger
from .variable_data_prototype import VariableDataPrototype

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswModuleDescription:
    """Root element for the description of a single BSW module or BSW cluster.

    In case it describes a BSW module, the short name of this element
    equals the name of the BSW module.

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
    :ivar expected_entrys: Indicates an entry which is required by this
        module. Replacement of outgoingCallback / requiredEntry. This
        property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar implemented_entrys: Specifies an entry provided by this module
        which can be called by other modules. This includes "main"
        functions, interrupt routines, and callbacks. Replacement of
        providedEntry / expectedCallback. This property was modified due
        to atpVariation (DirectedAssociationPattern).
    :ivar module_id: Refers to the BSW Module Identifier defined by the
        AUTOSAR standard. For non-standardized modules, a proprietary
        identifier can be optionally chosen.
    :ivar bsw_module_documentations: This adds a documentation to the
        BSW module. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar provided_entrys: Specifies an entry provided by this module
        which can be called by other modules. This includes "main"
        functions and interrupt routines, but not callbacks (because the
        signature of a callback is defined by the caller). This property
        was modified due to atpVariation (DirectedAssociationPattern).
    :ivar outgoing_callbacks: Specifies a callback, which will be called
        from this module if required by another module. This property
        was modified due to atpVariation (DirectedAssociationPattern).
    :ivar bsw_module_dependencys: Describes the dependency to another
        BSW module. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar provided_mode_groups: A set of modes which is owned and
        provided by this module or cluster. It can be connected to the
        requiredModeGroups of other modules or clusters via the
        configuration of the BswScheduler. It can also be synchronized
        with modes provided via ports by an associated
        ServiceSwComponentType, EcuAbstractionSwComponentType or
        ComplexDeviceDriverSwComponentType. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar required_mode_groups: Specifies that this module or cluster
        depends on a certain mode group. The requiredModeGroup is local
        to  this context and will be connected to the providedModeGroup
        of another module or cluster via the configuration of the
        BswScheduler. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar released_triggers: A Trigger released by this module or
        cluster. It can be connected to the requiredTriggers of other
        modules or clusters via the configuration of the BswScheduler.
        It can also be synchronized with Triggers provided via ports by
        an associated ServiceSwComponentType,
        EcuAbstractionSwComponentType or
        ComplexDeviceDriverSwComponentType. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar required_triggers: Specifies that this module or cluster
        reacts upon an external trigger.This requiredTrigger is declared
        locally to this context and will be connected to the
        providedTrigger of another module or cluster via the
        configuration of the BswScheduler. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar provided_client_server_entrys: Specifies that this module
        provides a client server entry which can be called from another
        parition or core.This entry is declared locally to this context
        and will be connected to the requiredClientServerEntry of
        another or the same module via the configuration of the BSW
        Scheduler. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar required_client_server_entrys: Specifies that this module
        requires a client server entry which can be implemented on
        another parition or core.This entry is declared locally to this
        context and will be connected to the providedClientServerEntry
        of another or the same module via the configuration of the BSW
        Scheduler. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar provided_datas: Specifies a data prototype provided by this
        module in order to be read  from another partition or core.The
        providedData is declared locally to this context and will be
        connected to the requiredData of another or the same module via
        the configuration of the BSW Scheduler. The upper multiplicity
        of this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar required_datas: Specifies a data prototype required by this
        module in oder to be provided from another partition or core.The
        requiredData is declared locally to this context and will be
        connected to the providedData of another or the same module via
        the configuration of the BswScheduler. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar internal_behaviors: The various BswInternalBehaviors
        associated with a BswModuleDescription can be distributed over
        several physical files. Therefore the aggregation is
        &lt;&lt;atpSplitable&gt;&gt;.
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
        name = "BSW-MODULE-DESCRIPTION"

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
        "BswModuleDescription.ShortNameFragments"
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
    annotations: Optional["BswModuleDescription.Annotations"] = field(
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
    blueprint_policys: Optional["BswModuleDescription.BlueprintPolicys"] = (
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
    expected_entrys: Optional["BswModuleDescription.ExpectedEntrys"] = field(
        default=None,
        metadata={
            "name": "EXPECTED-ENTRYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implemented_entrys: Optional["BswModuleDescription.ImplementedEntrys"] = (
        field(
            default=None,
            metadata={
                "name": "IMPLEMENTED-ENTRYS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    module_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MODULE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bsw_module_documentations: Optional[
        "BswModuleDescription.BswModuleDocumentations"
    ] = field(
        default=None,
        metadata={
            "name": "BSW-MODULE-DOCUMENTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    provided_entrys: Optional["BswModuleDescription.ProvidedEntrys"] = field(
        default=None,
        metadata={
            "name": "PROVIDED-ENTRYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    outgoing_callbacks: Optional["BswModuleDescription.OutgoingCallbacks"] = (
        field(
            default=None,
            metadata={
                "name": "OUTGOING-CALLBACKS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    bsw_module_dependencys: Optional[
        "BswModuleDescription.BswModuleDependencys"
    ] = field(
        default=None,
        metadata={
            "name": "BSW-MODULE-DEPENDENCYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    provided_mode_groups: Optional[
        "BswModuleDescription.ProvidedModeGroups"
    ] = field(
        default=None,
        metadata={
            "name": "PROVIDED-MODE-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_mode_groups: Optional[
        "BswModuleDescription.RequiredModeGroups"
    ] = field(
        default=None,
        metadata={
            "name": "REQUIRED-MODE-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    released_triggers: Optional["BswModuleDescription.ReleasedTriggers"] = (
        field(
            default=None,
            metadata={
                "name": "RELEASED-TRIGGERS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    required_triggers: Optional["BswModuleDescription.RequiredTriggers"] = (
        field(
            default=None,
            metadata={
                "name": "REQUIRED-TRIGGERS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    provided_client_server_entrys: Optional[
        "BswModuleDescription.ProvidedClientServerEntrys"
    ] = field(
        default=None,
        metadata={
            "name": "PROVIDED-CLIENT-SERVER-ENTRYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_client_server_entrys: Optional[
        "BswModuleDescription.RequiredClientServerEntrys"
    ] = field(
        default=None,
        metadata={
            "name": "REQUIRED-CLIENT-SERVER-ENTRYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    provided_datas: Optional["BswModuleDescription.ProvidedDatas"] = field(
        default=None,
        metadata={
            "name": "PROVIDED-DATAS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_datas: Optional["BswModuleDescription.RequiredDatas"] = field(
        default=None,
        metadata={
            "name": "REQUIRED-DATAS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    internal_behaviors: Optional["BswModuleDescription.InternalBehaviors"] = (
        field(
            default=None,
            metadata={
                "name": "INTERNAL-BEHAVIORS",
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
    class BlueprintPolicys:
        blueprint_policy_list: list[BlueprintPolicyList] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        blueprint_policy_not_modifiable: list[BlueprintPolicyNotModifiable] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BLUEPRINT-POLICY-NOT-MODIFIABLE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        blueprint_policy_single: list[BlueprintPolicySingle] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-SINGLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ExpectedEntrys:
        bsw_module_entry_ref_conditional: list[
            BswModuleEntryRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-ENTRY-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ImplementedEntrys:
        bsw_module_entry_ref_conditional: list[
            BswModuleEntryRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-ENTRY-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class BswModuleDocumentations:
        sw_component_documentation: list[SwComponentDocumentation] = field(
            default_factory=list,
            metadata={
                "name": "SW-COMPONENT-DOCUMENTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ProvidedEntrys:
        bsw_module_entry_ref_conditional: list[
            BswModuleEntryRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-ENTRY-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class OutgoingCallbacks:
        bsw_module_entry_ref_conditional: list[
            BswModuleEntryRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-ENTRY-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class BswModuleDependencys:
        bsw_module_dependency: list[BswModuleDependency] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODULE-DEPENDENCY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ProvidedModeGroups:
        mode_declaration_group_prototype: list[
            ModeDeclarationGroupPrototype
        ] = field(
            default_factory=list,
            metadata={
                "name": "MODE-DECLARATION-GROUP-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RequiredModeGroups:
        mode_declaration_group_prototype: list[
            ModeDeclarationGroupPrototype
        ] = field(
            default_factory=list,
            metadata={
                "name": "MODE-DECLARATION-GROUP-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ReleasedTriggers:
        trigger: list[Trigger] = field(
            default_factory=list,
            metadata={
                "name": "TRIGGER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RequiredTriggers:
        trigger: list[Trigger] = field(
            default_factory=list,
            metadata={
                "name": "TRIGGER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ProvidedClientServerEntrys:
        bsw_module_client_server_entry: list[BswModuleClientServerEntry] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BSW-MODULE-CLIENT-SERVER-ENTRY",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class RequiredClientServerEntrys:
        bsw_module_client_server_entry: list[BswModuleClientServerEntry] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BSW-MODULE-CLIENT-SERVER-ENTRY",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class ProvidedDatas:
        variable_data_prototype: list[VariableDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RequiredDatas:
        variable_data_prototype: list[VariableDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class InternalBehaviors:
        bsw_internal_behavior: list[BswInternalBehavior] = field(
            default_factory=list,
            metadata={
                "name": "BSW-INTERNAL-BEHAVIOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
