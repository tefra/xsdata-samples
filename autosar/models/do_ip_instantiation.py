from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from autosar.models.boolean import Boolean
from autosar.models.category_string import CategoryString
from autosar.models.do_ip_network_configuration import DoIpNetworkConfiguration
from autosar.models.do_ip_request_configuration import DoIpRequestConfiguration
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.positive_integer import PositiveInteger
from autosar.models.positive_unlimited_integer import PositiveUnlimitedInteger
from autosar.models.short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DoIpInstantiation:
    """
    This meta-class defines the attributes for the DoIP configuration on a
    specific machine.

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
    :ivar eid: Configured EID (Entity ID) used for
        VehicleIdentificationRequest. If configured, take this value, if
        not configured use MAC address.
    :ivar entity_status_max_byte_field_use: This attribute is used to
        distinguish the optional support of the Max data size element of
        a diagnostic entity status response.
    :ivar gid: Configured GID (Group ID) used for
        VehicleIdentificationRequest. If configured, take this value
        (and set "Further action required" byte to 0x00="No further
        action required"), if not configured use ServiceInterface
        DoIPGroupIdentification to retrieve GID and 'further action
        required' values.
    :ivar gid_invalidity_pattern: Specifies the Byte pattern that is
        used for response messages if no valid GID could be retrieved.
        Only the value '0' or '255' is allowed.
    :ivar logical_address: Describes the logical address of the DoIP
        entity, which is used for VehicleAnnouncement and
        RoutingActivation responses.
    :ivar max_request_bytes: Specifies the maximum allowed bytes of a
        DoIP message request without the DoIP header.
    :ivar network_interfaces: Network interface specific DoIP
        properties.
    :ivar request_configurations: Request configuration that is used to
        determine whether an incoming DiagnosticMessage request needs to
        be interpreted as PHYSICAL or FUNCTIONAL. Any request with
        target address not within the configured target address range
        will be rejected.
    :ivar vin_invalidity_pattern: Specifies the Byte pattern that is
        used for response messages if no valid VIN could be retrieved.
        Only the value '0' or '255' is allowed.
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
        name = "DO-IP-INSTANTIATION"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["DoIpInstantiation.ShortNameFragments"] = field(
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
    annotations: Optional["DoIpInstantiation.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    eid: Optional[PositiveUnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "EID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    entity_status_max_byte_field_use: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ENTITY-STATUS-MAX-BYTE-FIELD-USE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    gid: Optional[PositiveUnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "GID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    gid_invalidity_pattern: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "GID-INVALIDITY-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    logical_address: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LOGICAL-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_request_bytes: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-REQUEST-BYTES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    network_interfaces: Optional["DoIpInstantiation.NetworkInterfaces"] = field(
        default=None,
        metadata={
            "name": "NETWORK-INTERFACES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    request_configurations: Optional["DoIpInstantiation.RequestConfigurations"] = field(
        default=None,
        metadata={
            "name": "REQUEST-CONFIGURATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    vin_invalidity_pattern: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "VIN-INVALIDITY-PATTERN",
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
    class NetworkInterfaces:
        do_ip_network_configuration: List[DoIpNetworkConfiguration] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-NETWORK-CONFIGURATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class RequestConfigurations:
        do_ip_request_configuration: List[DoIpRequestConfiguration] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-REQUEST-CONFIGURATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
