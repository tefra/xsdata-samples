from dataclasses import dataclass, field
from typing import Optional

from .application_composite_data_type_sub_element_ref import (
    ApplicationCompositeDataTypeSubElementRef,
)
from .implementation_data_type_sub_element_ref import (
    ImplementationDataTypeSubElementRef,
)
from .text_table_mapping import TextTableMapping

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SubElementMapping:
    """
    This meta-class allows for the definition of mappings of elements of a
    composite data type.

    :ivar first_elements: This represents the first element referenced
        in the scope of the mapping. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was 1.
    :ivar second_elements: This represents the second element referenced
        in the scope of the mapping. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was 1.
    :ivar text_table_mappings: This allows for the text-table
        translation of individual elements of a composite data type.
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
        name = "SUB-ELEMENT-MAPPING"

    first_elements: Optional["SubElementMapping.FirstElements"] = field(
        default=None,
        metadata={
            "name": "FIRST-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    second_elements: Optional["SubElementMapping.SecondElements"] = field(
        default=None,
        metadata={
            "name": "SECOND-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    text_table_mappings: Optional["SubElementMapping.TextTableMappings"] = (
        field(
            default=None,
            metadata={
                "name": "TEXT-TABLE-MAPPINGS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    class FirstElements:
        application_composite_data_type_sub_element_ref: list[
            ApplicationCompositeDataTypeSubElementRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        implementation_data_type_sub_element_ref: list[
            ImplementationDataTypeSubElementRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "IMPLEMENTATION-DATA-TYPE-SUB-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SecondElements:
        application_composite_data_type_sub_element_ref: list[
            ApplicationCompositeDataTypeSubElementRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        implementation_data_type_sub_element_ref: list[
            ImplementationDataTypeSubElementRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "IMPLEMENTATION-DATA-TYPE-SUB-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TextTableMappings:
        text_table_mapping: list[TextTableMapping] = field(
            default_factory=list,
            metadata={
                "name": "TEXT-TABLE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 2,
            },
        )
