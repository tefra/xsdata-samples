from __future__ import annotations

from dataclasses import dataclass, field

from ubl.models.common.ubl_common_basic_components_2_1 import (
    Id,
    Name,
)
from ubl.models.common.ubl_extension_content_data_type_2_1 import (
    ExtensionContentType,
)
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    CodeType,
    IdentifierType,
    TextType,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
)


@dataclass(frozen=True, kw_only=True)
class ExtensionAgencyIdtype(IdentifierType):
    class Meta:
        name = "ExtensionAgencyIDType"


@dataclass(frozen=True, kw_only=True)
class ExtensionAgencyNameType(TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExtensionAgencyUritype(IdentifierType):
    class Meta:
        name = "ExtensionAgencyURIType"


@dataclass(frozen=True, kw_only=True)
class ExtensionContent(ExtensionContentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExtensionReasonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExtensionReasonType(TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExtensionUritype(IdentifierType):
    class Meta:
        name = "ExtensionURIType"


@dataclass(frozen=True, kw_only=True)
class ExtensionVersionIdtype(IdentifierType):
    class Meta:
        name = "ExtensionVersionIDType"


@dataclass(frozen=True, kw_only=True)
class ExtensionAgencyId(ExtensionAgencyIdtype):
    class Meta:
        name = "ExtensionAgencyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExtensionAgencyName(ExtensionAgencyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExtensionAgencyUri(ExtensionAgencyUritype):
    class Meta:
        name = "ExtensionAgencyURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExtensionReason(ExtensionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExtensionReasonCode(ExtensionReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExtensionUri(ExtensionUritype):
    class Meta:
        name = "ExtensionURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExtensionVersionId(ExtensionVersionIdtype):
    class Meta:
        name = "ExtensionVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True, kw_only=True)
class UblextensionType:
    class Meta:
        name = "UBLExtensionType"

    id: None | Id = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: None | Name = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    extension_agency_id: None | ExtensionAgencyId = field(
        default=None,
        metadata={
            "name": "ExtensionAgencyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_agency_name: None | ExtensionAgencyName = field(
        default=None,
        metadata={
            "name": "ExtensionAgencyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_version_id: None | ExtensionVersionId = field(
        default=None,
        metadata={
            "name": "ExtensionVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_agency_uri: None | ExtensionAgencyUri = field(
        default=None,
        metadata={
            "name": "ExtensionAgencyURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_uri: None | ExtensionUri = field(
        default=None,
        metadata={
            "name": "ExtensionURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_reason_code: None | ExtensionReasonCode = field(
        default=None,
        metadata={
            "name": "ExtensionReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_reason: None | ExtensionReason = field(
        default=None,
        metadata={
            "name": "ExtensionReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_content: ExtensionContent = field(
        metadata={
            "name": "ExtensionContent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class Ublextension(UblextensionType):
    class Meta:
        name = "UBLExtension"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True, kw_only=True)
class UblextensionsType:
    class Meta:
        name = "UBLExtensionsType"

    ublextension: tuple[Ublextension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "UBLExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True, kw_only=True)
class Ublextensions(UblextensionsType):
    class Meta:
        name = "UBLExtensions"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
