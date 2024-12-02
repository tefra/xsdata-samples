from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .deterministic_client_subtypes_enum import DeterministicClientSubtypesEnum
from .executable_subtypes_enum import ExecutableSubtypesEnum
from .identifier import Identifier
from .mode_declaration_group_prototype import ModeDeclarationGroupPrototype
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .process_design_subtypes_enum import ProcessDesignSubtypesEnum
from .ref import Ref
from .security_event_definition_subtypes_enum import (
    SecurityEventDefinitionSubtypesEnum,
)
from .short_name_fragment import ShortNameFragment
from .state_dependent_startup_config import StateDependentStartupConfig
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Process:
    """
    This meta-class provides information required to execute the referenced
    executable.

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
    :ivar design_ref: This reference represents the identification of
        the design-time representation for the Process that owns the
        reference.
    :ivar deterministic_client_ref: This reference adds further
        execution characteristics for deterministic clients.
    :ivar executable_ref: Reference to executable that is executed in
        the process.
    :ivar function_cluster_affiliation: This attribute specifies which
        functional cluster the process is affiliated with.
    :ivar number_of_restart_attempts: This attribute defines how often a
        process shall be restarted if the start fails.
        numberOfRestartAttempts = "0" OR Attribute not existing, start
        once numberOfRestartAttempts = "1",  start a second time
    :ivar pre_mapping: This attribute describes whether the executable
        is preloaded into the memory.
    :ivar process_state_machine: Set of Process States that are defined
        for the process.
    :ivar security_event_refs: The reference identifies the collection
        of SecurityEvents that can be reported by the enclosing
        SoftwareCluster.
    :ivar state_dependent_startup_configs: Applicable startup
        configurations.
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
        name = "PROCESS"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["Process.ShortNameFragments"] = field(
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
    annotations: Optional["Process.Annotations"] = field(
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
    design_ref: Optional["Process.DesignRef"] = field(
        default=None,
        metadata={
            "name": "DESIGN-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    deterministic_client_ref: Optional["Process.DeterministicClientRef"] = (
        field(
            default=None,
            metadata={
                "name": "DETERMINISTIC-CLIENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    executable_ref: Optional["Process.ExecutableRef"] = field(
        default=None,
        metadata={
            "name": "EXECUTABLE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    function_cluster_affiliation: Optional[String] = field(
        default=None,
        metadata={
            "name": "FUNCTION-CLUSTER-AFFILIATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    number_of_restart_attempts: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "NUMBER-OF-RESTART-ATTEMPTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pre_mapping: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "PRE-MAPPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    process_state_machine: Optional[ModeDeclarationGroupPrototype] = field(
        default=None,
        metadata={
            "name": "PROCESS-STATE-MACHINE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    security_event_refs: Optional["Process.SecurityEventRefs"] = field(
        default=None,
        metadata={
            "name": "SECURITY-EVENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    state_dependent_startup_configs: Optional[
        "Process.StateDependentStartupConfigs"
    ] = field(
        default=None,
        metadata={
            "name": "STATE-DEPENDENT-STARTUP-CONFIGS",
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
    class DesignRef(Ref):
        dest: Optional[ProcessDesignSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DeterministicClientRef(Ref):
        dest: Optional[DeterministicClientSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ExecutableRef(Ref):
        dest: Optional[ExecutableSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SecurityEventRefs:
        security_event_ref: list[
            "Process.SecurityEventRefs.SecurityEventRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class SecurityEventRef(Ref):
            dest: Optional[SecurityEventDefinitionSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class StateDependentStartupConfigs:
        state_dependent_startup_config: list[StateDependentStartupConfig] = (
            field(
                default_factory=list,
                metadata={
                    "name": "STATE-DEPENDENT-STARTUP-CONFIG",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
