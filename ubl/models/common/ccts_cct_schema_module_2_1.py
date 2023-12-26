from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2"
)


@dataclass(frozen=True)
class AmountType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    currency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyID",
            "type": "Attribute",
        },
    )
    currency_code_list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyCodeListVersionID",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class BinaryObjectType:
    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
        },
    )
    encoding_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "encodingCode",
            "type": "Attribute",
        },
    )
    character_set_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "characterSetCode",
            "type": "Attribute",
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    filename: Optional[str] = field(
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
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyName",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    language_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "languageID",
            "type": "Attribute",
        },
    )
    list_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "listURI",
            "type": "Attribute",
        },
    )
    list_scheme_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "listSchemeURI",
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
    scheme_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeID",
            "type": "Attribute",
        },
    )
    scheme_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeName",
            "type": "Attribute",
        },
    )
    scheme_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeAgencyID",
            "type": "Attribute",
        },
    )
    scheme_agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeAgencyName",
            "type": "Attribute",
        },
    )
    scheme_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeVersionID",
            "type": "Attribute",
        },
    )
    scheme_data_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeDataURI",
            "type": "Attribute",
        },
    )
    scheme_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeURI",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class MeasureType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        },
    )
    unit_code_list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListVersionID",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class NumericType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class QuantityType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        },
    )
    unit_code_list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListID",
            "type": "Attribute",
        },
    )
    unit_code_list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListAgencyID",
            "type": "Attribute",
        },
    )
    unit_code_list_agency_name: Optional[str] = field(
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
    language_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "languageID",
            "type": "Attribute",
        },
    )
    language_locale_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "languageLocaleID",
            "type": "Attribute",
        },
    )
