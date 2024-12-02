from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .crypto_module_instantiation import CryptoModuleInstantiation
from .do_ip_instantiation import DoIpInstantiation
from .enter_exit_timeout import EnterExitTimeout
from .generic_module_instantiation import GenericModuleInstantiation
from .iam_module_instantiation import IamModuleInstantiation
from .identifier import Identifier
from .idsm_module_instantiation import IdsmModuleInstantiation
from .log_and_trace_instantiation import LogAndTraceInstantiation
from .machine_design_subtypes_enum import MachineDesignSubtypesEnum
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nm_instantiation import NmInstantiation
from .os_module_instantiation import OsModuleInstantiation
from .processor import Processor
from .ref import Ref
from .sec_oc_deployment import SecOcDeployment
from .short_name_fragment import ShortNameFragment
from .tag_with_optional_value import TagWithOptionalValue
from .time_sync_module_instantiation import TimeSyncModuleInstantiation
from .tls_deployment import TlsDeployment
from .trusted_platform_executable_launch_behavior_enum import (
    TrustedPlatformExecutableLaunchBehaviorEnum,
)
from .ucm_module_instantiation import UcmModuleInstantiation

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Machine:
    """
    Machine that represents an Adaptive Autosar Software Stack.

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
    :ivar default_application_timeout: This aggration defines a default
        timeout in the context of a given Machine with respect to the
        launching and termination of applications.
    :ivar environment_variables: This aggregation represents the
        collection of environment variables that shall be added to the
        environment defined on the level of the enclosing Machine.
    :ivar machine_design_ref: Reference to the MachineDesign this
        Machine is implementing.
    :ivar module_instantiations: Configuration of Adaptive Autosar
        module instances that are running on the machine.
    :ivar processors: This represents the collection of processors owned
        by the enclosing machine.
    :ivar secure_communication_deployments: Deployment of secure
        communication protocol configuration settings to crypto module
        entities.
    :ivar trusted_platform_executable_launch_behavior: This attribute
        controls the behavior of how authentication affects the ability
        to launch for each Executable.
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
        name = "MACHINE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["Machine.ShortNameFragments"] = field(
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
    annotations: Optional["Machine.Annotations"] = field(
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
    default_application_timeout: Optional[EnterExitTimeout] = field(
        default=None,
        metadata={
            "name": "DEFAULT-APPLICATION-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    environment_variables: Optional["Machine.EnvironmentVariables"] = field(
        default=None,
        metadata={
            "name": "ENVIRONMENT-VARIABLES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    machine_design_ref: Optional["Machine.MachineDesignRef"] = field(
        default=None,
        metadata={
            "name": "MACHINE-DESIGN-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    module_instantiations: Optional["Machine.ModuleInstantiations"] = field(
        default=None,
        metadata={
            "name": "MODULE-INSTANTIATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    processors: Optional["Machine.Processors"] = field(
        default=None,
        metadata={
            "name": "PROCESSORS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    secure_communication_deployments: Optional[
        "Machine.SecureCommunicationDeployments"
    ] = field(
        default=None,
        metadata={
            "name": "SECURE-COMMUNICATION-DEPLOYMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trusted_platform_executable_launch_behavior: Optional[
        TrustedPlatformExecutableLaunchBehaviorEnum
    ] = field(
        default=None,
        metadata={
            "name": "TRUSTED-PLATFORM-EXECUTABLE-LAUNCH-BEHAVIOR",
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
    class EnvironmentVariables:
        tag_with_optional_value: list[TagWithOptionalValue] = field(
            default_factory=list,
            metadata={
                "name": "TAG-WITH-OPTIONAL-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class MachineDesignRef(Ref):
        dest: Optional[MachineDesignSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ModuleInstantiations:
        crypto_module_instantiation: list[CryptoModuleInstantiation] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-MODULE-INSTANTIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        do_ip_instantiation: list[DoIpInstantiation] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-INSTANTIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        generic_module_instantiation: list[GenericModuleInstantiation] = field(
            default_factory=list,
            metadata={
                "name": "GENERIC-MODULE-INSTANTIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        iam_module_instantiation: list[IamModuleInstantiation] = field(
            default_factory=list,
            metadata={
                "name": "IAM-MODULE-INSTANTIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        idsm_module_instantiation: list[IdsmModuleInstantiation] = field(
            default_factory=list,
            metadata={
                "name": "IDSM-MODULE-INSTANTIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        log_and_trace_instantiation: list[LogAndTraceInstantiation] = field(
            default_factory=list,
            metadata={
                "name": "LOG-AND-TRACE-INSTANTIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        nm_instantiation: list[NmInstantiation] = field(
            default_factory=list,
            metadata={
                "name": "NM-INSTANTIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        os_module_instantiation: list[OsModuleInstantiation] = field(
            default_factory=list,
            metadata={
                "name": "OS-MODULE-INSTANTIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        time_sync_module_instantiation: list[TimeSyncModuleInstantiation] = (
            field(
                default_factory=list,
                metadata={
                    "name": "TIME-SYNC-MODULE-INSTANTIATION",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        ucm_module_instantiation: list[UcmModuleInstantiation] = field(
            default_factory=list,
            metadata={
                "name": "UCM-MODULE-INSTANTIATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Processors:
        processor: list[Processor] = field(
            default_factory=list,
            metadata={
                "name": "PROCESSOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SecureCommunicationDeployments:
        sec_oc_deployment: list[SecOcDeployment] = field(
            default_factory=list,
            metadata={
                "name": "SEC-OC-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        tls_deployment: list[TlsDeployment] = field(
            default_factory=list,
            metadata={
                "name": "TLS-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
