from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .contained_i_pdu_props import ContainedIPduProps
from .container_i_pdu_header_type_enum import ContainerIPduHeaderTypeEnum
from .container_i_pdu_trigger_enum import ContainerIPduTriggerEnum
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .rx_accept_contained_i_pdu_enum import RxAcceptContainedIPduEnum
from .short_name_fragment import ShortNameFragment
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ContainerIPdu:
    """
    Allows to collect several IPdus in one ContainerIPdu based on the
    headerType.

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
    :ivar has_dynamic_length: This attribute defines whether the Pdu has
        dynamic length (true) or not (false). Please note that the usage
        of this attribute is restricted by [constr_3448].
    :ivar length: Pdu length in bytes. In case of dynamic length IPdus
        (containing a dynamical length signal), this value indicates the
        maximum data length. It should be noted that in former AUTOSAR
        releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this
        parameter was defined in bits. The Pdu length of zero bytes is
        allowed.
    :ivar meta_data_length: Number of additional bytes of MetaData in
        the PDU data field. The MetaData contains auxiliary information
        for the PDU, e.g. the CAN ID.
    :ivar contained_i_pdu_props: Defines whether this IPdu may be
        collected inside a ContainerIPdu.
    :ivar contained_pdu_triggering_refs: This PduTriggering shall be
        collected inside the ContainerIPdu.
    :ivar container_timeout: When this timeout expires the ContainerIPdu
        is sent out. The respective timer is started when the first Ipdu
        is put into the ContainerIPdu. This attribute is ignored on
        receiver side.
    :ivar container_trigger: Defines if the transmission of the
        ContainerIPdu shall be requested right after the first
        ContainedIPdu was put into it. This attribute shall be ignored
        on receiver side.
    :ivar header_type: Defines whether and which header type is used
        (header id and length).
    :ivar minimum_rx_container_queue_size: This attribute defines the
        minimum queue size for received containers.
    :ivar minimum_tx_container_queue_size: This attribute defines the
        minimum queue size for transmitted containers.
    :ivar rx_accept_contained_i_pdu: Defines whether this ContainerIPdu
        has a fixed set of containedIPdus assigned for reception.
    :ivar threshold_size: Defines the size threshold which, when
        exceeded, triggers the sending of the ContainerIPdu although the
        maxium Pdu size has not been reached yet. Unit: byte.
    :ivar unused_bit_pattern: IPduM fills not updated areas of the
        ContainerPdu with this byte-pattern.
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
        name = "CONTAINER-I-PDU"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: None | ContainerIPdu.ShortNameFragments = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: None | MultilanguageLongName = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: None | MultiLanguageOverviewParagraph = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: None | ContainerIPdu.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    has_dynamic_length: None | Boolean = field(
        default=None,
        metadata={
            "name": "HAS-DYNAMIC-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    length: None | Integer = field(
        default=None,
        metadata={
            "name": "LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    meta_data_length: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "META-DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    contained_i_pdu_props: None | ContainedIPduProps = field(
        default=None,
        metadata={
            "name": "CONTAINED-I-PDU-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    contained_pdu_triggering_refs: (
        None | ContainerIPdu.ContainedPduTriggeringRefs
    ) = field(
        default=None,
        metadata={
            "name": "CONTAINED-PDU-TRIGGERING-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    container_timeout: None | TimeValue = field(
        default=None,
        metadata={
            "name": "CONTAINER-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    container_trigger: None | ContainerIPduTriggerEnum = field(
        default=None,
        metadata={
            "name": "CONTAINER-TRIGGER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    header_type: None | ContainerIPduHeaderTypeEnum = field(
        default=None,
        metadata={
            "name": "HEADER-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minimum_rx_container_queue_size: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MINIMUM-RX-CONTAINER-QUEUE-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minimum_tx_container_queue_size: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MINIMUM-TX-CONTAINER-QUEUE-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rx_accept_contained_i_pdu: None | RxAcceptContainedIPduEnum = field(
        default=None,
        metadata={
            "name": "RX-ACCEPT-CONTAINED-I-PDU",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    threshold_size: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "THRESHOLD-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    unused_bit_pattern: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "UNUSED-BIT-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: None | str = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ContainedPduTriggeringRefs:
        contained_pdu_triggering_ref: list[
            ContainerIPdu.ContainedPduTriggeringRefs.ContainedPduTriggeringRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTAINED-PDU-TRIGGERING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class ContainedPduTriggeringRef(Ref):
            dest: PduTriggeringSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
