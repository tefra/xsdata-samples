from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2"
)


@dataclass(frozen=True)
class AmountType:
    value: Decimal | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    currency_id: str | None = field(
        default=None,
        metadata={
            "name": "currencyID",
            "type": "Attribute",
        },
    )
    currency_code_list_version_id: str | None = field(
        default=None,
        metadata={
            "name": "currencyCodeListVersionID",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class BinaryObjectType:
    value: bytes | None = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        },
    )
    format: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mime_code: str | None = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
        },
    )
    encoding_code: str | None = field(
        default=None,
        metadata={
            "name": "encodingCode",
            "type": "Attribute",
        },
    )
    character_set_code: str | None = field(
        default=None,
        metadata={
            "name": "characterSetCode",
            "type": "Attribute",
        },
    )
    uri: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    filename: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class CodeType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    list_id: str | None = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: str | None = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_agency_name: str | None = field(
        default=None,
        metadata={
            "name": "listAgencyName",
            "type": "Attribute",
        },
    )
    list_name: str | None = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: str | None = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    language_id: str | None = field(
        default=None,
        metadata={
            "name": "languageID",
            "type": "Attribute",
        },
    )
    list_uri: str | None = field(
        default=None,
        metadata={
            "name": "listURI",
            "type": "Attribute",
        },
    )
    list_scheme_uri: str | None = field(
        default=None,
        metadata={
            "name": "listSchemeURI",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class DateTimeType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    format: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class IdentifierType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    scheme_id: str | None = field(
        default=None,
        metadata={
            "name": "schemeID",
            "type": "Attribute",
        },
    )
    scheme_name: str | None = field(
        default=None,
        metadata={
            "name": "schemeName",
            "type": "Attribute",
        },
    )
    scheme_agency_id: str | None = field(
        default=None,
        metadata={
            "name": "schemeAgencyID",
            "type": "Attribute",
        },
    )
    scheme_agency_name: str | None = field(
        default=None,
        metadata={
            "name": "schemeAgencyName",
            "type": "Attribute",
        },
    )
    scheme_version_id: str | None = field(
        default=None,
        metadata={
            "name": "schemeVersionID",
            "type": "Attribute",
        },
    )
    scheme_data_uri: str | None = field(
        default=None,
        metadata={
            "name": "schemeDataURI",
            "type": "Attribute",
        },
    )
    scheme_uri: str | None = field(
        default=None,
        metadata={
            "name": "schemeURI",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class IndicatorType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    format: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class MeasureType:
    value: Decimal | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    unit_code: str | None = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        },
    )
    unit_code_list_version_id: str | None = field(
        default=None,
        metadata={
            "name": "unitCodeListVersionID",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class NumericType:
    value: Decimal | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    format: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class QuantityType:
    value: Decimal | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    unit_code: str | None = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        },
    )
    unit_code_list_id: str | None = field(
        default=None,
        metadata={
            "name": "unitCodeListID",
            "type": "Attribute",
        },
    )
    unit_code_list_agency_id: str | None = field(
        default=None,
        metadata={
            "name": "unitCodeListAgencyID",
            "type": "Attribute",
        },
    )
    unit_code_list_agency_name: str | None = field(
        default=None,
        metadata={
            "name": "unitCodeListAgencyName",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class TextType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    language_id: str | None = field(
        default=None,
        metadata={
            "name": "languageID",
            "type": "Attribute",
        },
    )
    language_locale_id: str | None = field(
        default=None,
        metadata={
            "name": "languageLocaleID",
            "type": "Attribute",
        },
    )
