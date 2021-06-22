from dataclasses import dataclass
from ubl.models.common.ccts_cct_schema_module_2_1 import (
    AmountType as CctsCctSchemaModule21AmountType,
    BinaryObjectType as CctsCctSchemaModule21BinaryObjectType,
    CodeType as CctsCctSchemaModule21CodeType,
    IdentifierType as CctsCctSchemaModule21IdentifierType,
    MeasureType as CctsCctSchemaModule21MeasureType,
    NumericType as CctsCctSchemaModule21NumericType,
    QuantityType as CctsCctSchemaModule21QuantityType,
    TextType as CctsCctSchemaModule21TextType,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2"


@dataclass
class AmountType(CctsCctSchemaModule21AmountType):
    pass


@dataclass
class BinaryObjectType(CctsCctSchemaModule21BinaryObjectType):
    pass


@dataclass
class CodeType(CctsCctSchemaModule21CodeType):
    pass


@dataclass
class GraphicType(CctsCctSchemaModule21BinaryObjectType):
    pass


@dataclass
class IdentifierType(CctsCctSchemaModule21IdentifierType):
    pass


@dataclass
class MeasureType(CctsCctSchemaModule21MeasureType):
    pass


@dataclass
class NameType(CctsCctSchemaModule21TextType):
    pass


@dataclass
class NumericType(CctsCctSchemaModule21NumericType):
    pass


@dataclass
class PercentType(CctsCctSchemaModule21NumericType):
    pass


@dataclass
class PictureType(CctsCctSchemaModule21BinaryObjectType):
    pass


@dataclass
class QuantityType(CctsCctSchemaModule21QuantityType):
    pass


@dataclass
class RateType(CctsCctSchemaModule21NumericType):
    pass


@dataclass
class SoundType(CctsCctSchemaModule21BinaryObjectType):
    pass


@dataclass
class TextType(CctsCctSchemaModule21TextType):
    pass


@dataclass
class ValueType(CctsCctSchemaModule21NumericType):
    pass


@dataclass
class VideoType(CctsCctSchemaModule21BinaryObjectType):
    pass
