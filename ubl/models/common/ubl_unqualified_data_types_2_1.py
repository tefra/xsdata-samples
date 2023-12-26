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

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2"
)


@dataclass(frozen=True)
class AmountType(CctsCctSchemaModule21AmountType):
    currency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyID",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True)
class BinaryObjectType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True)
class CodeType(CctsCctSchemaModule21CodeType):
    pass


@dataclass(frozen=True)
class GraphicType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True)
class IdentifierType(CctsCctSchemaModule21IdentifierType):
    pass


@dataclass(frozen=True)
class MeasureType(CctsCctSchemaModule21MeasureType):
    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True)
class NameType(CctsCctSchemaModule21TextType):
    pass


@dataclass(frozen=True)
class NumericType(CctsCctSchemaModule21NumericType):
    pass


@dataclass(frozen=True)
class PercentType(CctsCctSchemaModule21NumericType):
    pass


@dataclass(frozen=True)
class PictureType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True)
class QuantityType(CctsCctSchemaModule21QuantityType):
    pass


@dataclass(frozen=True)
class RateType(CctsCctSchemaModule21NumericType):
    pass


@dataclass(frozen=True)
class SoundType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True)
class TextType(CctsCctSchemaModule21TextType):
    pass


@dataclass(frozen=True)
class ValueType(CctsCctSchemaModule21NumericType):
    pass


@dataclass(frozen=True)
class VideoType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        },
    )
