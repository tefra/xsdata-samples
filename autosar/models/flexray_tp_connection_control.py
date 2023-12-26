from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .short_name_fragment import ShortNameFragment
from .time_value import TimeValue
from .tp_ack_type import TpAckType

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayTpConnectionControl:
    """
    Configuration parameters to control a FlexRay TP connection.

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
    :ivar ack_type: This parameter defines the type of acknowledgement
        which is used for the specific channel.
    :ivar max_ar: This parameter defines the maximum number of trying to
        send a frame when a TIMEOUT AR occurs (depending on whether
        retry is configured).
    :ivar max_as: This parameter defines the maximum number of trying to
        send a frame when a TIMEOUT AS occurs (depending on whether
        retry is configured)
    :ivar max_buffer_size: This attribute has the status "removed" and
        shall not be used any longer. Old description: This parameter is
        only relevant when having retry activated. It limits the maximal
        buffer size the FrTp can choose in order to limit the amount of
        Tx buffer that will be requested at the sender side in a
        segmented transfer. Unit: byte.
    :ivar max_fc_wait: This attribute defines the maximum number of
        FlowControl N-PDUs with FlowState "WAIT".
    :ivar max_fr_if: This parameter defines the maximum number of trying
        to send a frame when the FrIf returns an error
    :ivar max_number_of_npdu_per_cycle: This parameter limits the number
        of N-Pdus the sender is allowed to transmit within a FlexRay
        cycle.
    :ivar max_retries: This parameter defines the maximum number of
        retries (if retry is configured for the particular channel).
    :ivar separation_cycle_exponent: Exponent to calculate the minimum
        number of "Separation Cycles" the sender has to wait for the
        next transmission of an FrTp N-Pdu.
    :ivar time_br: Time (in seconds) until transmission of the next
        FlowControl N-PDU.
    :ivar time_buffer: This parameter defines the time of waiting for
        the next try to get a Tx or Rx buffer. This parameter is
        equivalent to the temporal distance between two FC.WT N-Pdus in
        case the buffer request returns busy. Specified in seconds.
    :ivar time_cs: Time (in seconds) until transmission of the next
        ConsecutiveFrame NPdu / LastFrame NPdu.
    :ivar time_fr_if: This parameter defines the time of waiting for the
        next try to send. Specified in seconds.
    :ivar timeout_ar: This parameter states the timeout between the PDU
        transmit request of the Transport Layer to the FlexRay Interface
        and the corresponding confirmation of the FlexRay Interface on
        the receiver side (for FC or AF). Specified in seconds.
    :ivar timeout_as: This attribute states the timeout between the PDU
        transmit request for the first PDU of the group used in the
        current connection of the Transport Layer to the FlexRay
        Interface and the corresponding confirmation of the FlexRay
        Interface (when having sent the last PDU of the group used in
        this connection) on the sender side (SF-x, FF-x, CF or FC (in
        case of Transmit Cancellation)). Specified in seconds.
    :ivar timeout_br: This attribute specifies the timeout in seconds
        between the Pdu receive indication of the Transport Layer to the
        FlexRay Interface and the corresponding Pdu transmission of the
        FlexRay Interface on the receiver side.
    :ivar timeout_bs: This parameter defines the timeout in seconds for
        waiting for an FC or AF on the sender side in a 1:1 connection.
    :ivar timeout_cr: This parameter defines the timeout value in
        seconds for waiting for a CF or FF-x (in case of retry) after
        receiving the last CF or after sending an FC or AF on the
        receiver side. Specified in seconds.
    :ivar timeout_cs: This attribute specifies the timeout in seconds to
        transmit the next ConsecutiveFrame NPdu or the last frame NPdu
        after receiving the flow control frame (CTS) from the sender
        side.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "FLEXRAY-TP-CONNECTION-CONTROL"

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
        "FlexrayTpConnectionControl.ShortNameFragments"
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
    annotations: Optional["FlexrayTpConnectionControl.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ack_type: Optional[TpAckType] = field(
        default=None,
        metadata={
            "name": "ACK-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_ar: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MAX-AR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_as: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MAX-AS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_buffer_size: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MAX-BUFFER-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_fc_wait: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MAX-FC-WAIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_fr_if: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MAX-FR-IF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_number_of_npdu_per_cycle: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MAX-NUMBER-OF-NPDU-PER-CYCLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_retries: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MAX-RETRIES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    separation_cycle_exponent: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SEPARATION-CYCLE-EXPONENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_br: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIME-BR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_buffer: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIME-BUFFER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_cs: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIME-CS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_fr_if: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIME-FR-IF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_ar: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-AR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_as: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-AS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_br: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-BR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_bs: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-BS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_cr: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-CR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_cs: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-CS",
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
