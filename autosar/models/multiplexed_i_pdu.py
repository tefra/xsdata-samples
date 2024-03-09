from dataclasses import dataclass, field
from typing import List, Optional
from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .byte_order_enum import ByteOrderEnum
from .category_string import CategoryString
from .contained_i_pdu_props import ContainedIPduProps
from .dynamic_part import DynamicPart
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .short_name_fragment import ShortNameFragment
from .static_part import StaticPart
from .trigger_mode import TriggerMode

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MultiplexedIPdu:
    """A MultiplexedPdu (i.e. NOT a COM I-PDU) contains a DynamicPart, an optional
    StaticPart and a selectorField.

    In case of multiplexing this IPdu is routed between the Pdu
    Multiplexer and the Interface Layer. A multiplexer is used to define
    variable parts within an IPdu that may carry different signals. The
    receivers of such a IPdu can determine which signalPdus are
    transmitted by evaluating the selector field, which carries a unique
    selector code for each sub-part.

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
    :ivar dynamic_parts: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar selector_field_byte_order: This attribute defines the order of
        the bytes of the selectorField and the packing into the
        MultiplexedIPdu. Please consider that [constr_3247] and
        [constr_3223] are restricting the usage of this attribute. In a
        complete System Description this attribute is mandatory. If a
        MultiplexedPdu is received by a Pdu Gateway and is not delivered
        to the IPduM but routed directly to a bus interface then the
        content of the MulitplexedPdu doesn't need to be described in
        the System Extract/Ecu Extract. To support this use case the
        multiplicity is set to 0..1.
    :ivar selector_field_length: The size in bits of the selector field
        shall be configurable in a range of 1-16 bits. In a complete
        System Description this attribute is mandatory. If a
        MultiplexedPdu is received by a Pdu Gateway and is not delivered
        to the IPduM but routed directly to a bus interface then the
        content of the MulitplexedPdu doesn't need to be described in
        the System Extract/Ecu Extract. To support this use case the
        multiplicity is set to 0..1.
    :ivar selector_field_start_position: This parameter is necessary to
        describe the position of the selector field within the IPdu.
        Note that the absolute position of the selectorField in the
        MultiplexedIPdu is determined by the definition of the
        selectorFieldByteOrder attribute of the Multiplexed Pdu. If Big
        Endian is specified, the start position indicates the bit
        position of the most significant bit in the IPdu. If Little
        Endian is specified, the start position indicates the bit
        position of the least significant bit in the IPdu. In AUTOSAR
        the bit counting is always set to "sawtooth" and the bit order
        is set to "Decreasing". The bit counting in byte 0 starts with
        bit 0 (least significant bit). The most significant bit in byte
        0 is bit 7. In a complete System Description this attribute is
        mandatory. If a MultiplexedPdu is received by a Pdu Gateway and
        is not delivered to the IPduM but routed directly to a bus
        interface then the content of the MulitplexedPdu doesn't need to
        be described in the System Extract/Ecu Extract. To support this
        use case the multiplicity is set to 0..1.
    :ivar static_parts: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar trigger_mode: IPduM can be configured to send a transmission
        request for the new multiplexed IPdu to the PDU-Router because
        of the trigger conditions/ modes that are described in the
        TriggerMode enumeration. In a complete System Description this
        attribute is mandatory. If a MultiplexedPdu is received by a Pdu
        Gateway and is not delivered to the IPduM but routed directly to
        a bus interface then the content of the MulitplexedPdu doesn't
        need to be described in the System Extract/Ecu Extract. To
        support this use case the multiplicity is set to 0..1.
    :ivar unused_bit_pattern: AUTOSAR COM and AUTOSAR IPDUM are filling
        not used areas of an IPdu with this bit-pattern. This attribute
        is mandatory to avoid undefined behavior. This byte-pattern will
        be repeated throughout the IPdu. In a complete System
        Description this attribute is mandatory. If a MultiplexedPdu is
        received by a Pdu Gateway and is not delivered to the IPduM but
        routed directly to a bus interface then the content of the
        MulitplexedPdu doesn't need to be described in the System
        Extract/Ecu Extract. To support this use case the multiplicity
        is set to 0..1.
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
        name = "MULTIPLEXED-I-PDU"

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
        "MultiplexedIPdu.ShortNameFragments"
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
    annotations: Optional["MultiplexedIPdu.Annotations"] = field(
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
    has_dynamic_length: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "HAS-DYNAMIC-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    length: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    meta_data_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "META-DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    contained_i_pdu_props: Optional[ContainedIPduProps] = field(
        default=None,
        metadata={
            "name": "CONTAINED-I-PDU-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dynamic_parts: Optional["MultiplexedIPdu.DynamicParts"] = field(
        default=None,
        metadata={
            "name": "DYNAMIC-PARTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    selector_field_byte_order: Optional[ByteOrderEnum] = field(
        default=None,
        metadata={
            "name": "SELECTOR-FIELD-BYTE-ORDER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    selector_field_length: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SELECTOR-FIELD-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    selector_field_start_position: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SELECTOR-FIELD-START-POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    static_parts: Optional["MultiplexedIPdu.StaticParts"] = field(
        default=None,
        metadata={
            "name": "STATIC-PARTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trigger_mode: Optional[TriggerMode] = field(
        default=None,
        metadata={
            "name": "TRIGGER-MODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    unused_bit_pattern: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "UNUSED-BIT-PATTERN",
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
    class DynamicParts:
        dynamic_part: List[DynamicPart] = field(
            default_factory=list,
            metadata={
                "name": "DYNAMIC-PART",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class StaticParts:
        static_part: List[StaticPart] = field(
            default_factory=list,
            metadata={
                "name": "STATIC-PART",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
