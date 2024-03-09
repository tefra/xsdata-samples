from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .byte_order_enum import ByteOrderEnum
from .category_string import CategoryString
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_subtypes_enum import PduSubtypesEnum
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PduToFrameMapping:
    """
    A PduToFrameMapping defines the composition of Pdus in each frame.

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
    :ivar packing_byte_order: This attribute defines the order of the
        bytes of the Pdu and the packing into the Frame. Please consider
        that [constr_3246] and [constr_3222] are restricting the usage
        of this attribute.
    :ivar pdu_ref: Reference to a I-Pdu, N-Pdu or NmPdu that is
        transmitted in the Frame.
    :ivar start_position: This attribute describes the bitposition of a
        Pdu within a Frame. Please note that the absolute position of
        the Pdu in the Frame is determined by the definition of the
        packingByteOrder attribute. If Big Endian is specified, the
        start position indicates the bit position of the most
        significant bit in the Frame. If Little Endian is specified, the
        start position indicates the bit position of the least
        significant bit in the Frame. The bit counting in byte 0 starts
        with bit 0 (least significant bit). The most significant bit in
        byte 0 is bit 7. The Pdus are byte aligned in a Frame and only
        the values  0, 8, 16, 24,... (for little endian) and  7, 15, 23,
        ... (for big endian) are allowed.
    :ivar update_indication_bit_position: Indication to the receivers
        that the corresponding Pdu was updated by the sender. This
        attribute describes the position of the update bit in the frame
        that aggregates this PDUToFrameMapping. Length is always one
        bit. Note that the exact bit position of the
        updateIndicationBitPosition is linked to the value of the
        attribute packingByteOrder because the method of finding the bit
        position is different for the values mostSignificantByteFirst
        and mostSignificantByteLast. This means that if the value of
        packingByteOrder is changed while the value of
        updateIndicationBitPosition remains unchanged the exact bit
        position of updateIndicationBitPosition within the enclosing
        Frame still undergoes a change. This attribute denotes the least
        significant bit for "Little Endian" and the most significant bit
        for "Big Endian" packed signals within the IPdu (see the
        description of the packingByteOrder attribute). In AUTOSAR the
        bit counting is always set to "sawtooth" and the bit order is
        set to "Decreasing". The bit counting in byte 0 starts with bit
        0 (least significant bit). The most significant bit in byte 0 is
        bit 7.
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
        name = "PDU-TO-FRAME-MAPPING"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["PduToFrameMapping.ShortNameFragments"] = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    annotations: Optional["PduToFrameMapping.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    packing_byte_order: Optional[ByteOrderEnum] = field(
        default=None,
        metadata={
            "name": "PACKING-BYTE-ORDER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_ref: Optional["PduToFrameMapping.PduRef"] = field(
        default=None,
        metadata={
            "name": "PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    start_position: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "START-POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    update_indication_bit_position: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "UPDATE-INDICATION-BIT-POSITION",
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

    @dataclass
    class PduRef(Ref):
        dest: Optional[PduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
