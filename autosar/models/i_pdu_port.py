from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.boolean import Boolean
from autosar.models.category_string import CategoryString
from autosar.models.communication_direction_type import CommunicationDirectionType
from autosar.models.i_pdu_signal_processing_enum import IPduSignalProcessingEnum
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.positive_integer import PositiveInteger
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IPduPort:
    """
    Connectors reception or send port on the referenced channel referenced by a
    PduTriggering.

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
    :ivar communication_direction: Communication Direction of the
        Connector Port (input or output Port).
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar i_pdu_signal_processing: Definition of the two signal
        processing modes Immediate and Deferred for both Tx and Rx
        IPdus.
    :ivar key_id: This attribute specifies the local Key identifier of
        the stored Key used to generate or verify a MAC. The keyId shall
        be unique per Ecu.
    :ivar rx_security_verification: This attribute defines the bypassing
        of signature authentication or MAC verification in the receiving
        ECU. If not defined or set to true the signature authentication
        or MAC verification shall be performed for the SecuredIPdu. If
        set to false the signature authentication or MAC verification
        shall not be performed for the SecuredIPdu.
    :ivar timestamp_rx_acceptance_window: This attribute is used to
        define the maximum allowed deviation in seconds from the
        expected timestamp for which a SecuredIPdu is still deemed
        authentic. Please note that this attribute is for documentation
        only to allow the configuration of required freshness value
        manager and no upstream mapping is defined for it.
    :ivar use_auth_data_freshness: This attribute describes whether a
        part of AuthenticPdu contained in a SecuredIPdu shall be passed
        on to the SWC that verifies and generates the Freshness. The
        part of the Authentic-PDU is defined by the
        authDataFreshnessStartPosition and authDataFreshnessLength.
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
        name = "I-PDU-PORT"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["IPduPort.ShortNameFragments"] = field(
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
    annotations: Optional["IPduPort.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    communication_direction: Optional[CommunicationDirectionType] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-DIRECTION",
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
    i_pdu_signal_processing: Optional[IPduSignalProcessingEnum] = field(
        default=None,
        metadata={
            "name": "I-PDU-SIGNAL-PROCESSING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    key_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "KEY-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rx_security_verification: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "RX-SECURITY-VERIFICATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timestamp_rx_acceptance_window: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMESTAMP-RX-ACCEPTANCE-WINDOW",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    use_auth_data_freshness: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "USE-AUTH-DATA-FRESHNESS",
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
