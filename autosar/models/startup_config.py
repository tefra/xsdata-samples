from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .category_string import CategoryString
from .enter_exit_timeout import EnterExitTimeout
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .process_argument import ProcessArgument
from .process_execution_error_subtypes_enum import (
    ProcessExecutionErrorSubtypesEnum,
)
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .string import String
from .tag_with_optional_value import TagWithOptionalValue
from .termination_behavior_enum import TerminationBehaviorEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class StartupConfig:
    """
    This meta-class represents a reusable startup configuration for processes..

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
    :ivar environment_variables: This aggregation represents the
        collection of environment variables that shall be added to the
        respective Process's environment prior to launch.
    :ivar execution_error_ref: this reference is used to identify the
        applicable execution error
    :ivar process_arguments: This aggregation represents the collection
        of command-line arguments applicable to the enclosing
        StartupConfig.
    :ivar scheduling_policy: This attribute represents the ability to
        define the scheduling policy for the initial thread of the
        application.
    :ivar scheduling_priority: This is the scheduling priority requested
        by the application itself.
    :ivar termination_behavior: This attribute defines the termination
        behavior of the Process.
    :ivar timeout: This aggregation can be used to specify the timeouts
        for launching and terminating the process depending on the
        StartupConfig.
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
        name = "STARTUP-CONFIG"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["StartupConfig.ShortNameFragments"] = field(
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
    annotations: Optional["StartupConfig.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    environment_variables: Optional["StartupConfig.EnvironmentVariables"] = (
        field(
            default=None,
            metadata={
                "name": "ENVIRONMENT-VARIABLES",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    execution_error_ref: Optional["StartupConfig.ExecutionErrorRef"] = field(
        default=None,
        metadata={
            "name": "EXECUTION-ERROR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    process_arguments: Optional["StartupConfig.ProcessArguments"] = field(
        default=None,
        metadata={
            "name": "PROCESS-ARGUMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    scheduling_policy: Optional[String] = field(
        default=None,
        metadata={
            "name": "SCHEDULING-POLICY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    scheduling_priority: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SCHEDULING-PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    termination_behavior: Optional[TerminationBehaviorEnum] = field(
        default=None,
        metadata={
            "name": "TERMINATION-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout: Optional[EnterExitTimeout] = field(
        default=None,
        metadata={
            "name": "TIMEOUT",
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
    class EnvironmentVariables:
        tag_with_optional_value: List[TagWithOptionalValue] = field(
            default_factory=list,
            metadata={
                "name": "TAG-WITH-OPTIONAL-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ExecutionErrorRef(Ref):
        dest: Optional[ProcessExecutionErrorSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ProcessArguments:
        process_argument: List[ProcessArgument] = field(
            default_factory=list,
            metadata={
                "name": "PROCESS-ARGUMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
