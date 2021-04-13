from dataclasses import dataclass, field
from typing import Optional
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
    currency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BinaryObjectType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CodeType(CctsCctSchemaModule21CodeType):
    pass


@dataclass
class GraphicType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class IdentifierType(CctsCctSchemaModule21IdentifierType):
    pass


@dataclass
class MeasureType(CctsCctSchemaModule21MeasureType):
    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
            "required": True,
        }
    )


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
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class QuantityType(CctsCctSchemaModule21QuantityType):
    pass


@dataclass
class RateType(CctsCctSchemaModule21NumericType):
    pass


@dataclass
class SoundType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TextType(CctsCctSchemaModule21TextType):
    pass


@dataclass
class ValueType(CctsCctSchemaModule21NumericType):
    pass


@dataclass
class VideoType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )
