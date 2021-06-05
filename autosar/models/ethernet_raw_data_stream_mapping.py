from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.category_string import CategoryString
from autosar.models.ethernet_communication_connector_subtypes_enum import EthernetCommunicationConnectorSubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.positive_integer import PositiveInteger
from autosar.models.process_subtypes_enum import ProcessSubtypesEnum
from autosar.models.r_port_prototype_in_executable_instance_ref import RPortPrototypeInExecutableInstanceRef
from autosar.models.raw_data_stream_deployment_subtypes_enum import RawDataStreamDeploymentSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.string import String
from autosar.models.tls_secure_com_props import TlsSecureComProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EthernetRawDataStreamMapping:
    """
    This meta-class represents the ability to map a PortPrototype to a
    Ethernet-based communication channel.

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
    :ivar deployment_ref: This reference identifies the applicable
        RawDataStreamDeployment.
    :ivar port_prototype_iref: Reference to a specific PortPrototype
        that represents the raw data stream to the application.
    :ivar process_ref: Reference to the Process in which the Executable
        that contains the SoftwareComponent and the referenced
        PortPrototype is executed.
    :ivar communication_connector_ref: This attribute represents the
        CommunicationConnector taken for socket-based data
        communication.
    :ivar multicast_udp_port: This attribute describes the UDP Port used
        for multicast raw data stream transmission.
    :ivar socket_options:
    :ivar tcp_port: This attribute describes the TCP port used for the
        raw data streaming.
    :ivar tls_secure_com_props: This aggregation provides the ability to
        define TLS-related properties for the enclosing
        SocketRawDataStreamMapping.
    :ivar udp_port: This attribute describes the UDP Port used for the
        raw data streaming.
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
        name = "ETHERNET-RAW-DATA-STREAM-MAPPING"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["EthernetRawDataStreamMapping.ShortNameFragments"] = field(
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
    annotations: Optional["EthernetRawDataStreamMapping.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    deployment_ref: Optional["EthernetRawDataStreamMapping.DeploymentRef"] = field(
        default=None,
        metadata={
            "name": "DEPLOYMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    port_prototype_iref: Optional[RPortPrototypeInExecutableInstanceRef] = field(
        default=None,
        metadata={
            "name": "PORT-PROTOTYPE-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    process_ref: Optional["EthernetRawDataStreamMapping.ProcessRef"] = field(
        default=None,
        metadata={
            "name": "PROCESS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    communication_connector_ref: Optional["EthernetRawDataStreamMapping.CommunicationConnectorRef"] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-CONNECTOR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    multicast_udp_port: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MULTICAST-UDP-PORT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    socket_options: Optional["EthernetRawDataStreamMapping.SocketOptions"] = field(
        default=None,
        metadata={
            "name": "SOCKET-OPTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_port: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-PORT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tls_secure_com_props: Optional[TlsSecureComProps] = field(
        default=None,
        metadata={
            "name": "TLS-SECURE-COM-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    udp_port: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "UDP-PORT",
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

    @dataclass
    class DeploymentRef(Ref):
        dest: Optional[RawDataStreamDeploymentSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ProcessRef(Ref):
        dest: Optional[ProcessSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class CommunicationConnectorRef(Ref):
        dest: Optional[EthernetCommunicationConnectorSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SocketOptions:
        """
        :ivar socket_option: This attribute represents the ability to
            specify non-formal socket options that might only be valid
            for specific platforms. AUTOSAR does not define a
            standardized meaning for the possible values of this
            attribute.
        """
        socket_option: List[String] = field(
            default_factory=list,
            metadata={
                "name": "SOCKET-OPTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
