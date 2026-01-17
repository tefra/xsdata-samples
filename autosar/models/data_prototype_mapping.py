from dataclasses import dataclass, field
from typing import Optional

from .autosar_data_prototype_subtypes_enum import (
    AutosarDataPrototypeSubtypesEnum,
)
from .data_transformation_subtypes_enum import DataTransformationSubtypesEnum
from .ref import Ref
from .sub_element_mapping import SubElementMapping
from .text_table_mapping import TextTableMapping

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DataPrototypeMapping:
    """
    Defines the mapping of two particular VariableDataPrototypes,
    ParameterDataPrototypes or ArgumentDataPrototypes with unequal names
    and/or unequal semantic (resolution or range) in context of two
    different SenderReceiverInterface, NvDataInterface or
    ParameterInterface or Operations.

    If the semantic is unequal following rules apply: The textTableMapping
    is only applicable if the referred DataPrototypes are typed by
    AutosarDataType referring to CompuMethods of category TEXTTABLE,
    SCALE_LINEAR_AND_TEXTTABLE or BITFIELD_TEXTTABLE. In the case that the
    DataPrototypes are typed by AutosarDataType either referring to
    CompuMethods of category LINEAR, IDENTICAL or referring to no
    CompuMethod (which is similar as IDENTICAL) the linear conversion
    factor is calculated out of the factorSiToUnit and offsetSiToUnit
    attributes of the referred Units and the CompuRationalCoeffs of a
    compuInternalToPhys of the referred CompuMethods.

    :ivar first_data_prototype_ref: First to be mapped DataPrototype in
        context of a  SenderReceiverInterface, NvDataInterface,
        ParameterInterface or Operation.
    :ivar first_to_second_data_transformation_ref: This reference
        defines the need to execute the DataTransformation
        &lt;Mip&gt;_&lt;transformerId&gt; functions of the
        transformation chain when communicating from the
        DataPrototypeMapping.firstDataPrototype to the
        DataPrototypeMapping.secondDataPrototype. This reference also
        specifies the reverse DataTransformation
        &lt;Mip&gt;_Inv_&lt;transformerId&gt; functions of the
        transformation chain (i.e. from the
        DataPrototypeMapping.secondDataPrototype to the
        DataPrototypeMapping.firstDataPrototype) if the referenced
        DataTransformation is symmetric, i.e. attribute
        DataTransformation.dataTransformationKind is set to symmetric.
    :ivar second_data_prototype_ref: Second to be mapped DataPrototype
        in context of a  SenderReceiverInterface, NvDataInterface,
        ParameterInterface or Operation.
    :ivar second_to_first_data_transformation_ref: This defines the need
        to execute the reverse DataTransformation
        &lt;Mip&gt;_Inv_&lt;transformerId&gt; functions of the
        transformation chain when communicating from the
        DataPrototypeMapping.secondDataPrototype to the
        DataPrototypeMapping.firstDataPrototype.
    :ivar sub_element_mappings: This represents the owned
        SubelementMapping.
    :ivar text_table_mappings: Applied TextTableMapping(s)
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
        name = "DATA-PROTOTYPE-MAPPING"

    first_data_prototype_ref: Optional[
        "DataPrototypeMapping.FirstDataPrototypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "FIRST-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    first_to_second_data_transformation_ref: Optional[
        "DataPrototypeMapping.FirstToSecondDataTransformationRef"
    ] = field(
        default=None,
        metadata={
            "name": "FIRST-TO-SECOND-DATA-TRANSFORMATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    second_data_prototype_ref: Optional[
        "DataPrototypeMapping.SecondDataPrototypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "SECOND-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    second_to_first_data_transformation_ref: Optional[
        "DataPrototypeMapping.SecondToFirstDataTransformationRef"
    ] = field(
        default=None,
        metadata={
            "name": "SECOND-TO-FIRST-DATA-TRANSFORMATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sub_element_mappings: Optional[
        "DataPrototypeMapping.SubElementMappings"
    ] = field(
        default=None,
        metadata={
            "name": "SUB-ELEMENT-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    text_table_mappings: Optional["DataPrototypeMapping.TextTableMappings"] = (
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
    class FirstDataPrototypeRef(Ref):
        dest: Optional[AutosarDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class FirstToSecondDataTransformationRef(Ref):
        dest: Optional[DataTransformationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SecondDataPrototypeRef(Ref):
        dest: Optional[AutosarDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SecondToFirstDataTransformationRef(Ref):
        dest: Optional[DataTransformationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SubElementMappings:
        sub_element_mapping: list[SubElementMapping] = field(
            default_factory=list,
            metadata={
                "name": "SUB-ELEMENT-MAPPING",
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
