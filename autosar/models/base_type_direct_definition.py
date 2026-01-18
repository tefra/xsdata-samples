from dataclasses import dataclass, field

from .base_type_encoding_string import BaseTypeEncodingString
from .byte_order_enum import ByteOrderEnum
from .native_declaration_string import NativeDeclarationString
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BaseTypeDirectDefinition:
    """
    This BaseType is defined directly (as opposite to a derived BaseType).

    :ivar base_type_size: Describes the length of the data type
        specified in the container in bits.
    :ivar max_base_type_size: Describes the maximum length of the
        BaseType in bits.
    :ivar base_type_encoding: This specifies, how an object of the
        current BaseType is encoded, e.g. in an ECU within a message
        sequence.
    :ivar mem_alignment: This attribute describes the alignment of the
        memory object in bits. E.g. "8" specifies, that the object in
        question is aligned to a byte while "32" specifies that it is
        aligned four byte. If the value is set to "0" the meaning shall
        be interpreted as "unspecified".
    :ivar byte_order: This attribute specifies the byte order of the
        base type.
    :ivar native_declaration: This attribute describes the declaration
        of such a base type in the native programming language,
        primarily in the Programming language C. This can then be used
        by a code generator to include the necessary declarations into a
        header file. For example BaseType with shortName:
        "MyUnsignedInt" nativeDeclaration: "unsigned short" Results in
        typedef unsigned short MyUnsignedInt; If the attribute is not
        defined the referring ImplementationDataTypes will not be
        generated as a typedef by RTE. If a nativeDeclaration type is
        given it shall fulfill the characteristic given by
        basetypeEncoding and baseTypeSize. This is required to ensure
        the consistent handling and interpretation by software
        components, RTE, COM and MCM systems.
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
    """

    class Meta:
        name = "BASE-TYPE-DIRECT-DEFINITION"

    base_type_size: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "BASE-TYPE-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_base_type_size: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MAX-BASE-TYPE-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    base_type_encoding: BaseTypeEncodingString | None = field(
        default=None,
        metadata={
            "name": "BASE-TYPE-ENCODING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mem_alignment: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MEM-ALIGNMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    byte_order: ByteOrderEnum | None = field(
        default=None,
        metadata={
            "name": "BYTE-ORDER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    native_declaration: NativeDeclarationString | None = field(
        default=None,
        metadata={
            "name": "NATIVE-DECLARATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
