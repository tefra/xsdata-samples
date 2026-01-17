from dataclasses import dataclass, field
from typing import Optional

from .array_size_semantics_enum import ArraySizeSemanticsEnum
from .integer import Integer
from .integer_value_variation_point import IntegerValueVariationPoint
from .ref import Ref
from .sw_base_type_subtypes_enum import SwBaseTypeSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwTextProps:
    """
    This meta-class expresses particular properties applicable to strings
    in variables or calibration parameters.

    :ivar array_size_semantics: This attribute controls the semantics of
        the arraysize for the array representing the string in an
        ImplementationDataType. It is there to support a safe conversion
        between ApplicationDatatype and ImplementationDatatype, even for
        variable length strings as required e.g. for Support of SAE
        J1939.
    :ivar sw_max_text_size: Specifies the maximum text size in
        characters. Note the size in bytes depends on the encoding in
        the corresponding baseType.
    :ivar base_type_ref: This is the base type of one character in the
        string. In particular this baseType denotes the intended
        encoding of the characters in the string  on level of
        ApplicationDataType.
    :ivar sw_fill_character: Filler character for text parameter to pad
        up to the maximum length swMaxTextSize. The value will be
        interpreted according to the encoding specified in the
        associated base type of the data object, e.g. 0x30 (hex)
        represents the ASCII character zero as filler character and 0
        (dec) represents an end of string as filler character. The usage
        of the fill character depends on the arraySizeSemantics.
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
        name = "SW-TEXT-PROPS"

    array_size_semantics: Optional[ArraySizeSemanticsEnum] = field(
        default=None,
        metadata={
            "name": "ARRAY-SIZE-SEMANTICS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_max_text_size: Optional[IntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "SW-MAX-TEXT-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    base_type_ref: Optional["SwTextProps.BaseTypeRef"] = field(
        default=None,
        metadata={
            "name": "BASE-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_fill_character: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SW-FILL-CHARACTER",
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

    @dataclass
    class BaseTypeRef(Ref):
        dest: Optional[SwBaseTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
