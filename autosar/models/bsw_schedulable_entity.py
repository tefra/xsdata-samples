from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .bsw_asynchronous_server_call_point import BswAsynchronousServerCallPoint
from .bsw_asynchronous_server_call_result_point import (
    BswAsynchronousServerCallResultPoint,
)
from .bsw_direct_call_point import BswDirectCallPoint
from .bsw_internal_triggering_point_ref_conditional import (
    BswInternalTriggeringPointRefConditional,
)
from .bsw_module_entry_ref_conditional import BswModuleEntryRefConditional
from .bsw_module_entry_subtypes_enum import BswModuleEntrySubtypesEnum
from .bsw_scheduler_name_prefix_subtypes_enum import (
    BswSchedulerNamePrefixSubtypesEnum,
)
from .bsw_synchronous_server_call_point import BswSynchronousServerCallPoint
from .bsw_variable_access import BswVariableAccess
from .category_string import CategoryString
from .exclusive_area_nesting_order_subtypes_enum import (
    ExclusiveAreaNestingOrderSubtypesEnum,
)
from .exclusive_area_subtypes_enum import ExclusiveAreaSubtypesEnum
from .executable_entity_activation_reason import (
    ExecutableEntityActivationReason,
)
from .identifier import Identifier
from .mode_declaration_group_prototype_ref_conditional import (
    ModeDeclarationGroupPrototypeRefConditional,
)
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .reentrancy_level_enum import ReentrancyLevelEnum
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .sw_addr_method_subtypes_enum import SwAddrMethodSubtypesEnum
from .time_value import TimeValue
from .trigger_ref_conditional import TriggerRefConditional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswSchedulableEntity:
    """BSW module entity, which is designed for control by the BSW Scheduler.

    It may for example implement a so-called "main" function.

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
    :ivar activation_reasons: If the ExecutableEntity provides at least
        one activationReason element the RTE resp. BSW Scheduler shall
        provide means to read the activation vector of this executable
        entity execution. If no activationReason element is provided the
        feature of being able to determine the activating RTEEvent is
        disabled for this ExecutableEntity.
    :ivar can_enter_exclusive_area_refs: This means that the executable
        entity can enter/leave the referenced exclusive area through
        explicit API calls.
    :ivar exclusive_area_nesting_order_refs: This represents the set of
        ExclusiveAreaNestingOrders recognized by this ExecutableEntity.
    :ivar minimum_start_interval: Specifies the time in seconds by which
        two consecutive starts of an ExecutableEntity are guaranteed to
        be separated.
    :ivar reentrancy_level: The reentrancy level of this
        ExecutableEntity. See the documentation of the enumeration type
        ReentrancyLevelEnum for details. Please note that nonReentrant
        interfaces can have also reentrant or multicoreReentrant
        implementations, and reentrant interfaces can also have
        multicoreReentrant implementations.
    :ivar runs_inside_exclusive_area_refs: The executable entity runs
        completely inside the referenced exclusive area.
    :ivar sw_addr_method_ref: Addressing method related to this code
        entity. Via an association to the same SwAddrMethod, it can be
        specified that several code entities (even of different modules
        or components)  shall be located in the same memory without
        already specifying the memory section itself.
    :ivar accessed_mode_groups: A mode group which is accessed via API
        call by this entity. It shall be a ModeDeclarationGroupPrototype
        required by this module or cluster. This property was modified
        due to atpVariation (DirectedAssociationPattern).
    :ivar activation_points: Activation point used by the module entity
        to activate one or more internal triggers. This property was
        modified due to atpVariation (DirectedAssociationPattern).
    :ivar call_points: A call point used in the code of this entitiy.
        The variablity of this association is especially targeted at
        debug scenarios: It is possible to have one variant calling into
        the AUTOSAR debug module and another one which doesn't. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar called_entrys: The entry of another (or the same) BSW module
        which is called by this entry (usually via C function call).
        This information allows to set up a model of call chains. The
        variablity of this association is especially targeted at debug
        scenarios: It is possible to have one variant calling into the
        AUTOSAR debug module and another one which doesn't. Note that
        this relation has been merked as obsolete, since the more
        powerful definition of a callPoint should be used. This property
        was modified due to atpVariation (DirectedAssociationPattern).
    :ivar data_receive_points: The data is received via the BSW
        Scheduler. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar data_send_points: The data is sent via the BSW Scheduler. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar implemented_entry_ref: The entry which is implemented by this
        module entity.
    :ivar issued_triggers: A trigger issued by this entity via BSW
        Scheduler API call. It shall be a BswTrigger released (i.e.
        owned) by this module or cluster. This property was modified due
        to atpVariation (DirectedAssociationPattern).
    :ivar managed_mode_groups: A mode group which is managed by this
        entity. It shall be a ModeDeclarationGroupPrototype provided by
        this module or cluster. This property was modified due to
        atpVariation (DirectedAssociationPattern).
    :ivar scheduler_name_prefix_ref: A prefix to be used in generated
        names for the BswModuleScheduler in the context of this
        BswModuleEntity, for example entry point prototypes, macros for
        dealing with exclusive areas, header file names. Details are
        defined in the SWS RTE. The prefix supersedes default rules for
        the prefix of those names.
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
        name = "BSW-SCHEDULABLE-ENTITY"

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
        "BswSchedulableEntity.ShortNameFragments"
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
    annotations: Optional["BswSchedulableEntity.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    activation_reasons: Optional["BswSchedulableEntity.ActivationReasons"] = (
        field(
            default=None,
            metadata={
                "name": "ACTIVATION-REASONS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    can_enter_exclusive_area_refs: Optional[
        "BswSchedulableEntity.CanEnterExclusiveAreaRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CAN-ENTER-EXCLUSIVE-AREA-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exclusive_area_nesting_order_refs: Optional[
        "BswSchedulableEntity.ExclusiveAreaNestingOrderRefs"
    ] = field(
        default=None,
        metadata={
            "name": "EXCLUSIVE-AREA-NESTING-ORDER-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minimum_start_interval: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "MINIMUM-START-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    reentrancy_level: Optional[ReentrancyLevelEnum] = field(
        default=None,
        metadata={
            "name": "REENTRANCY-LEVEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    runs_inside_exclusive_area_refs: Optional[
        "BswSchedulableEntity.RunsInsideExclusiveAreaRefs"
    ] = field(
        default=None,
        metadata={
            "name": "RUNS-INSIDE-EXCLUSIVE-AREA-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_addr_method_ref: Optional["BswSchedulableEntity.SwAddrMethodRef"] = (
        field(
            default=None,
            metadata={
                "name": "SW-ADDR-METHOD-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    accessed_mode_groups: Optional[
        "BswSchedulableEntity.AccessedModeGroups"
    ] = field(
        default=None,
        metadata={
            "name": "ACCESSED-MODE-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    activation_points: Optional["BswSchedulableEntity.ActivationPoints"] = (
        field(
            default=None,
            metadata={
                "name": "ACTIVATION-POINTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    call_points: Optional["BswSchedulableEntity.CallPoints"] = field(
        default=None,
        metadata={
            "name": "CALL-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    called_entrys: Optional["BswSchedulableEntity.CalledEntrys"] = field(
        default=None,
        metadata={
            "name": "CALLED-ENTRYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_receive_points: Optional["BswSchedulableEntity.DataReceivePoints"] = (
        field(
            default=None,
            metadata={
                "name": "DATA-RECEIVE-POINTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    data_send_points: Optional["BswSchedulableEntity.DataSendPoints"] = field(
        default=None,
        metadata={
            "name": "DATA-SEND-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implemented_entry_ref: Optional[
        "BswSchedulableEntity.ImplementedEntryRef"
    ] = field(
        default=None,
        metadata={
            "name": "IMPLEMENTED-ENTRY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    issued_triggers: Optional["BswSchedulableEntity.IssuedTriggers"] = field(
        default=None,
        metadata={
            "name": "ISSUED-TRIGGERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    managed_mode_groups: Optional["BswSchedulableEntity.ManagedModeGroups"] = (
        field(
            default=None,
            metadata={
                "name": "MANAGED-MODE-GROUPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    scheduler_name_prefix_ref: Optional[
        "BswSchedulableEntity.SchedulerNamePrefixRef"
    ] = field(
        default=None,
        metadata={
            "name": "SCHEDULER-NAME-PREFIX-REF",
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
    class ActivationReasons:
        executable_entity_activation_reason: List[
            ExecutableEntityActivationReason
        ] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTABLE-ENTITY-ACTIVATION-REASON",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CanEnterExclusiveAreaRefs:
        can_enter_exclusive_area_ref: List[
            "BswSchedulableEntity.CanEnterExclusiveAreaRefs.CanEnterExclusiveAreaRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CAN-ENTER-EXCLUSIVE-AREA-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class CanEnterExclusiveAreaRef(Ref):
            dest: Optional[ExclusiveAreaSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ExclusiveAreaNestingOrderRefs:
        exclusive_area_nesting_order_ref: List[
            "BswSchedulableEntity.ExclusiveAreaNestingOrderRefs.ExclusiveAreaNestingOrderRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "EXCLUSIVE-AREA-NESTING-ORDER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ExclusiveAreaNestingOrderRef(Ref):
            dest: Optional[ExclusiveAreaNestingOrderSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class RunsInsideExclusiveAreaRefs:
        runs_inside_exclusive_area_ref: List[
            "BswSchedulableEntity.RunsInsideExclusiveAreaRefs.RunsInsideExclusiveAreaRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "RUNS-INSIDE-EXCLUSIVE-AREA-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class RunsInsideExclusiveAreaRef(Ref):
            dest: Optional[ExclusiveAreaSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class SwAddrMethodRef(Ref):
        dest: Optional[SwAddrMethodSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class AccessedModeGroups:
        mode_declaration_group_prototype_ref_conditional: List[
            ModeDeclarationGroupPrototypeRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ActivationPoints:
        bsw_internal_triggering_point_ref_conditional: List[
            BswInternalTriggeringPointRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CallPoints:
        bsw_asynchronous_server_call_point: List[
            BswAsynchronousServerCallPoint
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-ASYNCHRONOUS-SERVER-CALL-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_asynchronous_server_call_result_point: List[
            BswAsynchronousServerCallResultPoint
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-ASYNCHRONOUS-SERVER-CALL-RESULT-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_direct_call_point: List[BswDirectCallPoint] = field(
            default_factory=list,
            metadata={
                "name": "BSW-DIRECT-CALL-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_synchronous_server_call_point: List[
            BswSynchronousServerCallPoint
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-SYNCHRONOUS-SERVER-CALL-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CalledEntrys:
        bsw_module_entry_ref_conditional: List[
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
    class DataReceivePoints:
        bsw_variable_access: List[BswVariableAccess] = field(
            default_factory=list,
            metadata={
                "name": "BSW-VARIABLE-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DataSendPoints:
        bsw_variable_access: List[BswVariableAccess] = field(
            default_factory=list,
            metadata={
                "name": "BSW-VARIABLE-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ImplementedEntryRef(Ref):
        dest: Optional[BswModuleEntrySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class IssuedTriggers:
        trigger_ref_conditional: List[TriggerRefConditional] = field(
            default_factory=list,
            metadata={
                "name": "TRIGGER-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ManagedModeGroups:
        mode_declaration_group_prototype_ref_conditional: List[
            ModeDeclarationGroupPrototypeRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SchedulerNamePrefixRef(Ref):
        dest: Optional[BswSchedulerNamePrefixSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
