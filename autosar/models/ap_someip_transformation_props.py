from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .base_type_encoding_string import BaseTypeEncodingString
from .boolean import Boolean
from .byte_order_enum import ByteOrderEnum
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .short_name_fragment import ShortNameFragment
from .someip_transformer_session_handling_enum import (
    SomeipTransformerSessionHandlingEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ApSomeipTransformationProps:
    """
    SOME/IP serialization properties.

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
    :ivar alignment: Defines the padding for alignment purposes that
        will be added by the SOME/IP transformer after the serialized
        data of the variable data length data element. The alignment
        shall be specified in Bits.
    :ivar byte_order: Specifies the byte order of data in the serialized
        data stream.
    :ivar implements_legacy_string_serialization: This attribute
        indicates that Strings in the SOME/IP message shall NOT be
        serialized according to the SOME/IP specification for Strings.
        If this attribute is set to true, BOM and null-termination shall
        NOT be added in the serialization for Strings in the payload. If
        this attribute is set to false (or not set)  BOM and null-
        termination shall be added in the serialization for Strings in
        the payload according to the SOME/IP specification for Strings.
        NOTE! This attribute is not future safe, and will be removed in
        an upcoming AUTOSAR release!
    :ivar is_dynamic_length_field_size: This attribute represents the
        ability to control the setting of the wire type for TLV
        encoding. If the attribute is set to True then wire type 5-7
        shall be used. If the attribute does not exist or is set to
        False then wire type 4 shall be used.
    :ivar session_handling: Defines whether the SOME/IP transformer
        shall use session handling for Sender/Receiver communication.
    :ivar size_of_array_length_field: Configures the SOME/IP
        serialization for the referenced dataPrototype in case of a
        variable size Array (Vector), fixed-size Array or an
        Associative_Map. It describes the size of the length field (in
        Bytes) that will be put in front of the Array or Associative_Map
        in the SOME/IP message.
    :ivar size_of_string_length_field: Configures the SOME/IP
        serialization for the referenced dataPrototype in case of a
        String. It describes the size of the length field (in Bytes)
        that will be put in front of the String in the SOME/IP message.
    :ivar size_of_struct_length_field: Configures the SOME/IP
        serialization for the referenced dataPrototype in case of an
        Struct. It describes the size of the length field (in Bytes)
        that will be put in front of the Struct in the SOME/IP message.
    :ivar size_of_union_length_field: Configures the SOME/IP
        serialization for the referenced dataPrototype in case of a
        Union. It describes the size of the length field (in Bytes) that
        will be put in front of the Union in the SOME/IP message.
    :ivar size_of_union_type_selector_field: Configures the SOME/IP
        serialization for the referenced dataPrototype in case of a
        Union. It describes the size of the type selector field (in
        Bytes) that will be put in front of the Union in the SOME/IP
        message.
    :ivar string_encoding: Configures the encoding for SOME/IP
        serialization for the referenced dataPrototype in case of an
        String.
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
        name = "AP-SOMEIP-TRANSFORMATION-PROPS"

    short_name: None | Identifier = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: (
        None | ApSomeipTransformationProps.ShortNameFragments
    ) = field(
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
    annotations: None | ApSomeipTransformationProps.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    alignment: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "ALIGNMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    byte_order: None | ByteOrderEnum = field(
        default=None,
        metadata={
            "name": "BYTE-ORDER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implements_legacy_string_serialization: None | Boolean = field(
        default=None,
        metadata={
            "name": "IMPLEMENTS-LEGACY-STRING-SERIALIZATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_dynamic_length_field_size: None | Boolean = field(
        default=None,
        metadata={
            "name": "IS-DYNAMIC-LENGTH-FIELD-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    session_handling: None | SomeipTransformerSessionHandlingEnum = field(
        default=None,
        metadata={
            "name": "SESSION-HANDLING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size_of_array_length_field: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SIZE-OF-ARRAY-LENGTH-FIELD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size_of_string_length_field: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SIZE-OF-STRING-LENGTH-FIELD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size_of_struct_length_field: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SIZE-OF-STRUCT-LENGTH-FIELD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size_of_union_length_field: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SIZE-OF-UNION-LENGTH-FIELD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size_of_union_type_selector_field: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SIZE-OF-UNION-TYPE-SELECTOR-FIELD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    string_encoding: None | BaseTypeEncodingString = field(
        default=None,
        metadata={
            "name": "STRING-ENCODING",
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

    @dataclass
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
