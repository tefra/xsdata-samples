from __future__ import annotations

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
from .boolean import Boolean
from .bsw_call_type import BswCallType
from .bsw_entry_kind_enum import BswEntryKindEnum
from .bsw_execution_context import BswExecutionContext
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nmtoken_string import NmtokenString
from .positive_integer import PositiveInteger
from .short_name_fragment import ShortNameFragment
from .string import String
from .sw_service_arg import SwServiceArg
from .sw_service_impl_policy_enum import SwServiceImplPolicyEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswModuleEntry:
    """
    This class represents a single API entry (C-function prototype) into
    the BSW module or cluster.

    The name of the C-function is equal to the short name of this element
    with one exception: In case of multiple instances of a module on the
    same CPU, special rules for "infixes" apply, see description of class
    BswImplementation.

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
    :ivar function_prototype_emitter: This attribute is used to control
        the generation of function prototypes. If set to "RTE", the RTE
        generates the  function prototypes in the Module Interlink
        Header File.
    :ivar service_id: Refers to the service identifier of the
        Standardized Interfaces of AUTOSAR basic software. For non-
        standardized interfaces, it can optionally be used for
        proprietary identification.
    :ivar role: Specifies the role of the entry in the given context. It
        shall be equal to the standardized name of the service call,
        especially in cases where no ServiceIdentifier is specified,
        e.g. for callbacks. Note that the ShortName is not always
        sufficient because it maybe vendor specific (e.g. for callbacks
        which can have more than one instance).
    :ivar is_reentrant: Reentrancy from the viewpoint of function
        callers: * True: Enables the service to be invoked again, before
        the service has finished. * False: It is prohibited to invoke
        the service again before is has finished.
    :ivar is_synchronous: Synchronicity from the viewpoint of function
        callers: * True: This calls a synchronous service, i.e. the
        service is completed when the call returns. * False: The service
        (on semantical level) may not be complete when the call returns.
    :ivar call_type: The type of call associated with this service.
    :ivar execution_context: Specifies the execution context which is
        required (in case of entries into this module) or guaranteed (in
        case of entries called from this module) for this service.
    :ivar sw_service_impl_policy: Denotes the implementation policy as a
        standard function call, inline function or macro. This has to be
        specified on interface level because it determines the signature
        of the call.
    :ivar bsw_entry_kind: This describes whether the entry is concrete
        or abstract. If the attribute is missing the entry is considered
        as concrete.
    :ivar return_type: The return type belonging to this bswModuleEntry.
    :ivar arguments: An argument belonging to this BswModuleEntry. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
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
        name = "BSW-MODULE-ENTRY"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: BswModuleEntry.ShortNameFragments | None = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    long_name: MultilanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: MultiLanguageOverviewParagraph | None = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: CategoryString | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: AdminData | None = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: DocumentationBlock | None = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: BswModuleEntry.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    blueprint_policys: BswModuleEntry.BlueprintPolicys | None = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    short_name_pattern: String | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    function_prototype_emitter: NmtokenString | None = field(
        default=None,
        metadata={
            "name": "FUNCTION-PROTOTYPE-EMITTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "SERVICE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    role: Identifier | None = field(
        default=None,
        metadata={
            "name": "ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_reentrant: Boolean | None = field(
        default=None,
        metadata={
            "name": "IS-REENTRANT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_synchronous: Boolean | None = field(
        default=None,
        metadata={
            "name": "IS-SYNCHRONOUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    call_type: BswCallType | None = field(
        default=None,
        metadata={
            "name": "CALL-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    execution_context: BswExecutionContext | None = field(
        default=None,
        metadata={
            "name": "EXECUTION-CONTEXT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_service_impl_policy: SwServiceImplPolicyEnum | None = field(
        default=None,
        metadata={
            "name": "SW-SERVICE-IMPL-POLICY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bsw_entry_kind: BswEntryKindEnum | None = field(
        default=None,
        metadata={
            "name": "BSW-ENTRY-KIND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    return_type: SwServiceArg | None = field(
        default=None,
        metadata={
            "name": "RETURN-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    arguments: BswModuleEntry.Arguments | None = field(
        default=None,
        metadata={
            "name": "ARGUMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: str | None = field(
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
    class Arguments:
        sw_service_arg: list[SwServiceArg] = field(
            default_factory=list,
            metadata={
                "name": "SW-SERVICE-ARG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
