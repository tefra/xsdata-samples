from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .category_string import CategoryString
from .communication_direction_type import CommunicationDirectionType
from .crypto_service_certificate_subtypes_enum import CryptoServiceCertificateSubtypesEnum
from .crypto_service_key_subtypes_enum import CryptoServiceKeySubtypesEnum
from .i_psec_header_type_enum import IPsecHeaderTypeEnum
from .i_psec_ip_protocol_enum import IPsecIpProtocolEnum
from .i_psec_mode_enum import IPsecModeEnum
from .i_psec_policy_enum import IPsecPolicyEnum
from .identifier import Identifier
from .ike_authentication_method_enum import IkeAuthenticationMethodEnum
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .network_endpoint_subtypes_enum import NetworkEndpointSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IpSecRule:
    """
    This element defines an IPsec rule that describes communication traffic that is
    monitored, protected and filtered.

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
    :ivar direction: This attribute defines the direction in which the
        traffic is monitored. If this attribute is not set a
        bidirectional traffic monitoring is assumed.
    :ivar header_type: Header type specifying the IPsec security
        mechanism.
    :ivar ike_authentication_method: This attribute defines the IKE
        authentication method that is used locally and is expected on
        the remote side.
    :ivar ip_protocol: This attribute defines the relevant IP protocol
        used in the Security Policy Database (SPD) entry.
    :ivar local_certificate_refs: This reference identifies the
        applicable certificate used for a local authentication.
    :ivar local_id: This attribute defines how the local participant
        should be identified for authentication.
    :ivar local_port_range_end: This attribute restricts the traffic
        monitoring and defines an end value for the local port range. If
        this attribute is not set then this rule shall be effective for
        all local ports. Please note that port ranges are currently not
        supported in the AUTOSAR AP's operating system backend. If AP
        systems are involved, each IPsec rule may only contain a single
        port.
    :ivar local_port_range_start: This attribute restricts the traffic
        monitoring and defines a start value for the local port range.
        If this attribute is not set then this rule shall be effective
        for all local ports. Please note that port ranges are currently
        not supported in the AUTOSAR AP's operating system backend. If
        AP systems are involved, each IPsec rule may only contain a
        single port.
    :ivar mode: This attribute defines the type of the connection.
    :ivar policy: An IPsec policy defines the rules that determine which
        type of IP traffic needs to be secured using IPsec and how that
        traffic is secured.
    :ivar pre_shared_key_ref: This reference identifies the applicable
        cryptograhic key used for authentication.
    :ivar priority: This attribute defines the priority of the IPSecRule
        (SPD entry). The processing of entries is based on priority,
        starting with the highest priority "0".
    :ivar remote_certificate_refs: This reference identifies the
        applicable certificate used for a remote authentication.
    :ivar remote_id: This attribute defines how the remote participant
        should be identified for authentication.
    :ivar remote_ip_address_refs: Definition of the remote
        NetworkEndpoint. With this reference the connection between the
        local NetworkEndpoint and the remote NetworkEndpoint is
        described on which the traffic is monitored.
    :ivar remote_port_range_end: This attribute restricts the traffic
        monitoring and defines an end value for the remote port range.
        If this attribute is not set then this rule shall be effective
        for all local ports. Please note that port ranges are currently
        not supported in the AUTOSAR AP's operating system backend. If
        AP systems are involved, each IPsec rule may only contain a
        single port.
    :ivar remote_port_range_start: This attribute restricts the traffic
        monitoring and defines a start value for the remote port range.
        If this attribute is not set then this rule shall be effective
        for all local ports. Please note that port ranges are currently
        not supported in the AUTOSAR AP's operating system backend. If
        AP systems are involved, each IPsec rule may only contain a
        single port.
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
        name = "IP-SEC-RULE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["IpSecRule.ShortNameFragments"] = field(
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
    annotations: Optional["IpSecRule.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    direction: Optional[CommunicationDirectionType] = field(
        default=None,
        metadata={
            "name": "DIRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    header_type: Optional[IPsecHeaderTypeEnum] = field(
        default=None,
        metadata={
            "name": "HEADER-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ike_authentication_method: Optional[IkeAuthenticationMethodEnum] = field(
        default=None,
        metadata={
            "name": "IKE-AUTHENTICATION-METHOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ip_protocol: Optional[IPsecIpProtocolEnum] = field(
        default=None,
        metadata={
            "name": "IP-PROTOCOL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    local_certificate_refs: Optional["IpSecRule.LocalCertificateRefs"] = field(
        default=None,
        metadata={
            "name": "LOCAL-CERTIFICATE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    local_id: Optional[String] = field(
        default=None,
        metadata={
            "name": "LOCAL-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    local_port_range_end: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LOCAL-PORT-RANGE-END",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    local_port_range_start: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LOCAL-PORT-RANGE-START",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mode: Optional[IPsecModeEnum] = field(
        default=None,
        metadata={
            "name": "MODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    policy: Optional[IPsecPolicyEnum] = field(
        default=None,
        metadata={
            "name": "POLICY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pre_shared_key_ref: Optional["IpSecRule.PreSharedKeyRef"] = field(
        default=None,
        metadata={
            "name": "PRE-SHARED-KEY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    priority: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    remote_certificate_refs: Optional["IpSecRule.RemoteCertificateRefs"] = field(
        default=None,
        metadata={
            "name": "REMOTE-CERTIFICATE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    remote_id: Optional[String] = field(
        default=None,
        metadata={
            "name": "REMOTE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    remote_ip_address_refs: Optional["IpSecRule.RemoteIpAddressRefs"] = field(
        default=None,
        metadata={
            "name": "REMOTE-IP-ADDRESS-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    remote_port_range_end: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "REMOTE-PORT-RANGE-END",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    remote_port_range_start: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "REMOTE-PORT-RANGE-START",
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
    class LocalCertificateRefs:
        local_certificate_ref: List["IpSecRule.LocalCertificateRefs.LocalCertificateRef"] = field(
            default_factory=list,
            metadata={
                "name": "LOCAL-CERTIFICATE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class LocalCertificateRef(Ref):
            dest: Optional[CryptoServiceCertificateSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class PreSharedKeyRef(Ref):
        dest: Optional[CryptoServiceKeySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class RemoteCertificateRefs:
        remote_certificate_ref: List["IpSecRule.RemoteCertificateRefs.RemoteCertificateRef"] = field(
            default_factory=list,
            metadata={
                "name": "REMOTE-CERTIFICATE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class RemoteCertificateRef(Ref):
            dest: Optional[CryptoServiceCertificateSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class RemoteIpAddressRefs:
        remote_ip_address_ref: List["IpSecRule.RemoteIpAddressRefs.RemoteIpAddressRef"] = field(
            default_factory=list,
            metadata={
                "name": "REMOTE-IP-ADDRESS-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class RemoteIpAddressRef(Ref):
            dest: Optional[NetworkEndpointSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
