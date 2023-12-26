from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .boolean import Boolean
from .category_string import CategoryString
from .dlt_log_channel_design_subtypes_enum import (
    DltLogChannelDesignSubtypesEnum,
)
from .dlt_message_subtypes_enum import DltMessageSubtypesEnum
from .identifier import Identifier
from .log_trace_default_log_level_enum import LogTraceDefaultLogLevelEnum
from .log_trace_log_mode_enum import LogTraceLogModeEnum
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from .platform_module_ethernet_endpoint_configuration_subtypes_enum import (
    PlatformModuleEthernetEndpointConfigurationSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref
from .service_instance_to_port_prototype_mapping_subtypes_enum import (
    ServiceInstanceToPortPrototypeMappingSubtypesEnum,
)
from .short_name_fragment import ShortNameFragment
from .string import String
from .uri_string import UriString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DltLogChannel:
    """
    This element contains the settings for the log/trace message output for a tuple
    of ApplicationId and ContextId (verbose mode) or a SessionId (non-verbose
    mode).

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
    :ivar application_description: This attribute can be used to
        describe the applicationId that is used in the log and trace
        message in more detail.
    :ivar application_id: This attribute identifies the SW-C/BSW module
        in the log and trace message.
    :ivar context_description: This attribute can be used to describe
        the contextId that is used in the log and trace message in more
        detail.
    :ivar context_id: This attribute is used to group log and trace
        messages produced by a SW-C/BSW modules to distinguish
        functionality (representing e.g. a library of the adaptive
        foundation linked into the application).
    :ivar dlt_log_channel_design_ref: This reference represents the
        identification of the design-time representation for the
        DltLogChannel that owns the reference.
    :ivar dlt_message_refs: Reference to DltMessages that can be
        transported over the DltLogChannel in the DltPdu.
    :ivar endpoint_configuration_ref: Network configuration (Protocol,
        Port, IP Address) for transmission of  dlt messages on a
        specific VLAN.
    :ivar log_trace_default_log_level: This attribute allows to set the
        initial log reporting level for a logTraceProcessId
        (ApplicationId).
    :ivar log_trace_file_path: This attribute defines the destination
        file to which the logging information is passed.
    :ivar log_trace_log_modes:
    :ivar non_verbose_mode: This attribute defines whether this channel
        supports non-Verbose Dlt messages. If disabled only verbose mode
        messages  shall be used.
    :ivar rx_pdu_triggering_ref: Reference to DltPdu that is received by
        the DltLogChannel
    :ivar service_instance_to_port_prototype_mapping_ref: Optional
        reference to a PortPrototype of the monitored Application in
        case that the communication over this port is monitored and
        defines the ContextId.
    :ivar session_id: This attribute allows distinguishing log/trace
        messages from different instances of the same SW-C. It is
        required if sessionIdSupport of the aggregating DltConfig is
        True.
    :ivar tx_pdu_triggering_ref: Reference to DltPdu that is transmitted
        by the DltLogChannel.
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
        name = "DLT-LOG-CHANNEL"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["DltLogChannel.ShortNameFragments"] = field(
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
    annotations: Optional["DltLogChannel.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    application_description: Optional[String] = field(
        default=None,
        metadata={
            "name": "APPLICATION-DESCRIPTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    application_id: Optional[String] = field(
        default=None,
        metadata={
            "name": "APPLICATION-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_description: Optional[String] = field(
        default=None,
        metadata={
            "name": "CONTEXT-DESCRIPTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_id: Optional[String] = field(
        default=None,
        metadata={
            "name": "CONTEXT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dlt_log_channel_design_ref: Optional[
        "DltLogChannel.DltLogChannelDesignRef"
    ] = field(
        default=None,
        metadata={
            "name": "DLT-LOG-CHANNEL-DESIGN-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dlt_message_refs: Optional["DltLogChannel.DltMessageRefs"] = field(
        default=None,
        metadata={
            "name": "DLT-MESSAGE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    endpoint_configuration_ref: Optional[
        "DltLogChannel.EndpointConfigurationRef"
    ] = field(
        default=None,
        metadata={
            "name": "ENDPOINT-CONFIGURATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    log_trace_default_log_level: Optional[LogTraceDefaultLogLevelEnum] = field(
        default=None,
        metadata={
            "name": "LOG-TRACE-DEFAULT-LOG-LEVEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    log_trace_file_path: Optional[UriString] = field(
        default=None,
        metadata={
            "name": "LOG-TRACE-FILE-PATH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    log_trace_log_modes: Optional["DltLogChannel.LogTraceLogModes"] = field(
        default=None,
        metadata={
            "name": "LOG-TRACE-LOG-MODES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    non_verbose_mode: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NON-VERBOSE-MODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rx_pdu_triggering_ref: Optional[
        "DltLogChannel.RxPduTriggeringRef"
    ] = field(
        default=None,
        metadata={
            "name": "RX-PDU-TRIGGERING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_instance_to_port_prototype_mapping_ref: Optional[
        "DltLogChannel.ServiceInstanceToPortPrototypeMappingRef"
    ] = field(
        default=None,
        metadata={
            "name": "SERVICE-INSTANCE-TO-PORT-PROTOTYPE-MAPPING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    session_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SESSION-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tx_pdu_triggering_ref: Optional[
        "DltLogChannel.TxPduTriggeringRef"
    ] = field(
        default=None,
        metadata={
            "name": "TX-PDU-TRIGGERING-REF",
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
    class DltLogChannelDesignRef(Ref):
        dest: Optional[DltLogChannelDesignSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DltMessageRefs:
        dlt_message_ref: List[
            "DltLogChannel.DltMessageRefs.DltMessageRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "DLT-MESSAGE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DltMessageRef(Ref):
            dest: Optional[DltMessageSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class EndpointConfigurationRef(Ref):
        dest: Optional[
            PlatformModuleEthernetEndpointConfigurationSubtypesEnum
        ] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class LogTraceLogModes:
        """
        :ivar log_trace_log_mode: This attribute defines the destination
            of log messages provided by the process.
        """

        log_trace_log_mode: List[LogTraceLogModeEnum] = field(
            default_factory=list,
            metadata={
                "name": "LOG-TRACE-LOG-MODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RxPduTriggeringRef(Ref):
        dest: Optional[PduTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ServiceInstanceToPortPrototypeMappingRef(Ref):
        dest: Optional[
            ServiceInstanceToPortPrototypeMappingSubtypesEnum
        ] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TxPduTriggeringRef(Ref):
        dest: Optional[PduTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
