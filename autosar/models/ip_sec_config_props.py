from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .i_psec_dpd_action_enum import IPsecDpdActionEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .short_name_fragment import ShortNameFragment
from .string import String
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IpSecConfigProps:
    """
    This element holds all the attributes for configuration of IPsec that are
    independent of specific IPsec rules.

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
    :ivar ah_cipher_suite_names:
    :ivar dpd_action: This attribute defines what to do if the peer is
        considered dead. If not configured "restart" shall be assumed.
    :ivar dpd_delay: This attribute describes the interval to check the
        liveness of a peer actively using IKEv2 INFORMATIONAL exchanges.
        Active DPD checking is only enforced if no IKE or ESP/AH packet
        has been received for the configured DPD delay. In not
        configured the value "5 minutes" shall be assumed.
    :ivar esp_cipher_suite_names:
    :ivar ike_cipher_suite_name: IKE encryption/authentication
        algorithms to be used for the connection.
    :ivar ike_over_time: This attribute describes the hard deadline when
        an SA becomes invalid in percentage. Example: ikeOverTime of
        max(ikeReauthTime, ikeRekeyTime). Default: 10 %
    :ivar ike_rand_time: This attribute defines in percentage by how
        long before the expiration of ikeReauthTime and ikeRekeyTime
        will be rekeyed/reauthenticated. Default: 10%
    :ivar ike_reauth_time: This attribute defines the absolute time
        after which an IKE SA will be reauthenticated. 0 means
        reauthentication is disabled.
    :ivar ike_rekey_time: This attribute defines the absolute time after
        which an IKE SA will be rekeyed. 0 means rekey is disabled.
    :ivar sa_over_time: This attribute describes the hard deadline when
        an IPsec SA becomes invalid in percentage. Example: saOverTime *
        saRekeyTime. Default: 110%
    :ivar sa_rand_time: This attribute defines by how long before the
        expiration of saRekeyTime will be rekeyed.
    :ivar sa_rekey_time: This attribute defines the absolute time after
        which an IPsec SA will be rekeyed. 0 means rekey is disabled.
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
        name = "IP-SEC-CONFIG-PROPS"

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
        "IpSecConfigProps.ShortNameFragments"
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
    annotations: Optional["IpSecConfigProps.Annotations"] = field(
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
    ah_cipher_suite_names: Optional[
        "IpSecConfigProps.AhCipherSuiteNames"
    ] = field(
        default=None,
        metadata={
            "name": "AH-CIPHER-SUITE-NAMES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dpd_action: Optional[IPsecDpdActionEnum] = field(
        default=None,
        metadata={
            "name": "DPD-ACTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dpd_delay: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "DPD-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    esp_cipher_suite_names: Optional[
        "IpSecConfigProps.EspCipherSuiteNames"
    ] = field(
        default=None,
        metadata={
            "name": "ESP-CIPHER-SUITE-NAMES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ike_cipher_suite_name: Optional[String] = field(
        default=None,
        metadata={
            "name": "IKE-CIPHER-SUITE-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ike_over_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "IKE-OVER-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ike_rand_time: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "IKE-RAND-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ike_reauth_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "IKE-REAUTH-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ike_rekey_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "IKE-REKEY-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sa_over_time: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SA-OVER-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sa_rand_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "SA-RAND-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sa_rekey_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "SA-REKEY-TIME",
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
    class AhCipherSuiteNames:
        """
        :ivar ah_cipher_suite_name: AH (Authentication Header) algorithm
            to be used for the connection, e.g. HMAC/SHA2-256
        """

        ah_cipher_suite_name: List[String] = field(
            default_factory=list,
            metadata={
                "name": "AH-CIPHER-SUITE-NAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class EspCipherSuiteNames:
        """
        :ivar esp_cipher_suite_name: ESP (Encapsulating Security
            Payload) algorithm that provides encryption and optional
            authentication for the connection, e.g. AES-128+SHA2-256.
        """

        esp_cipher_suite_name: List[String] = field(
            default_factory=list,
            metadata={
                "name": "ESP-CIPHER-SUITE-NAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
