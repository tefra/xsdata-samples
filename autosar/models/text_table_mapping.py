from dataclasses import dataclass, field
from typing import List, Optional
from .boolean import Boolean
from .mapping_direction_enum import MappingDirectionEnum
from .positive_integer_value_variation_point import PositiveIntegerValueVariationPoint
from .text_table_value_pair import TextTableValuePair

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TextTableMapping:
    """
    Defines the mapping of two DataPrototypes typed by AutosarDataTypes that refer
    to CompuMethods of category TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or
    BITFIELD_TEXTTABLE.

    :ivar bitfield_text_table_mask_first: This attribute can be used to
        support the mapping of bit field to bit field, boolean values to
        bit fields, and vice versa. The attribute defines the bit mask
        for the first element of the TextTableMapping.
    :ivar bitfield_text_table_mask_second: This attribute can be used to
        support the mapping of bit field to bit field, boolean values to
        bit fields, and vice versa. The attribute defines the bit mask
        for the second element of the TextTableMapping.
    :ivar identical_mapping: If identicalMapping is set == true the
        values of the two referenced DataPrototypes do not need any
        conversion of the values.
    :ivar mapping_direction: Specifies the conversion direction for
        which the TextTableMapping is applicable.
    :ivar value_pairs: Defines a pair of values which are translated
        into each other.
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
        name = "TEXT-TABLE-MAPPING"

    bitfield_text_table_mask_first: Optional[PositiveIntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "BITFIELD-TEXT-TABLE-MASK-FIRST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    bitfield_text_table_mask_second: Optional[PositiveIntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "BITFIELD-TEXT-TABLE-MASK-SECOND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    identical_mapping: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "IDENTICAL-MAPPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mapping_direction: Optional[MappingDirectionEnum] = field(
        default=None,
        metadata={
            "name": "MAPPING-DIRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    value_pairs: Optional["TextTableMapping.ValuePairs"] = field(
        default=None,
        metadata={
            "name": "VALUE-PAIRS",
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

    @dataclass
    class ValuePairs:
        text_table_value_pair: List[TextTableValuePair] = field(
            default_factory=list,
            metadata={
                "name": "TEXT-TABLE-VALUE-PAIR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
