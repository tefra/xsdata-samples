from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from ubl.models.common.ccts_cct_schema_module_2_1 import (
    AmountType as CctsCctSchemaModule21AmountType,
)
from ubl.models.common.ccts_cct_schema_module_2_1 import (
    BinaryObjectType as CctsCctSchemaModule21BinaryObjectType,
)
from ubl.models.common.ccts_cct_schema_module_2_1 import (
    CodeType as CctsCctSchemaModule21CodeType,
)
from ubl.models.common.ccts_cct_schema_module_2_1 import (
    IdentifierType as CctsCctSchemaModule21IdentifierType,
)
from ubl.models.common.ccts_cct_schema_module_2_1 import (
    MeasureType as CctsCctSchemaModule21MeasureType,
)
from ubl.models.common.ccts_cct_schema_module_2_1 import (
    NumericType as CctsCctSchemaModule21NumericType,
)
from ubl.models.common.ccts_cct_schema_module_2_1 import (
    QuantityType as CctsCctSchemaModule21QuantityType,
)
from ubl.models.common.ccts_cct_schema_module_2_1 import (
    TextType as CctsCctSchemaModule21TextType,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2"
)


@dataclass(frozen=True, kw_only=True)
class DateTimeType:
    value: XmlDateTime = field(
        metadata={
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class DateType:
    value: XmlDate = field(
        metadata={
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class IndicatorType:
    value: bool = field(
        metadata={
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class TimeType:
    value: XmlTime = field(
        metadata={
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class AmountType(CctsCctSchemaModule21AmountType):
    currency_id: str = field(
        metadata={
            "name": "currencyID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class BinaryObjectType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: str = field(
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class CodeType(CctsCctSchemaModule21CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class GraphicType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: str = field(
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class IdentifierType(CctsCctSchemaModule21IdentifierType):
    pass


@dataclass(frozen=True, kw_only=True)
class MeasureType(CctsCctSchemaModule21MeasureType):
    unit_code: str = field(
        metadata={
            "name": "unitCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class NameType(CctsCctSchemaModule21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class NumericType(CctsCctSchemaModule21NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class PercentType(CctsCctSchemaModule21NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class PictureType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: str = field(
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class QuantityType(CctsCctSchemaModule21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class RateType(CctsCctSchemaModule21NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class SoundType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: str = field(
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class TextType(CctsCctSchemaModule21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValueType(CctsCctSchemaModule21NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class VideoType(CctsCctSchemaModule21BinaryObjectType):
    mime_code: str = field(
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )
