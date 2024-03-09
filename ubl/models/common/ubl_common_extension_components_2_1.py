from dataclasses import dataclass, field
from typing import Optional, Tuple

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


@dataclass(frozen=True)
class ExtensionAgencyIdtype(IdentifierType):
    class Meta:
        name = "ExtensionAgencyIDType"


@dataclass(frozen=True)
class ExtensionAgencyNameType(TextType):
    pass


@dataclass(frozen=True)
class ExtensionAgencyUritype(IdentifierType):
    class Meta:
        name = "ExtensionAgencyURIType"


@dataclass(frozen=True)
class ExtensionContent(ExtensionContentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True)
class ExtensionReasonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ExtensionReasonType(TextType):
    pass


@dataclass(frozen=True)
class ExtensionUritype(IdentifierType):
    class Meta:
        name = "ExtensionURIType"


@dataclass(frozen=True)
class ExtensionVersionIdtype(IdentifierType):
    class Meta:
        name = "ExtensionVersionIDType"


@dataclass(frozen=True)
class ExtensionAgencyId(ExtensionAgencyIdtype):
    class Meta:
        name = "ExtensionAgencyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True)
class ExtensionAgencyName(ExtensionAgencyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True)
class ExtensionAgencyUri(ExtensionAgencyUritype):
    class Meta:
        name = "ExtensionAgencyURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True)
class ExtensionReason(ExtensionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True)
class ExtensionReasonCode(ExtensionReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True)
class ExtensionUri(ExtensionUritype):
    class Meta:
        name = "ExtensionURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True)
class ExtensionVersionId(ExtensionVersionIdtype):
    class Meta:
        name = "ExtensionVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True)
class UblextensionType:
    class Meta:
        name = "UBLExtensionType"

    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    extension_agency_id: Optional[ExtensionAgencyId] = field(
        default=None,
        metadata={
            "name": "ExtensionAgencyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_agency_name: Optional[ExtensionAgencyName] = field(
        default=None,
        metadata={
            "name": "ExtensionAgencyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_version_id: Optional[ExtensionVersionId] = field(
        default=None,
        metadata={
            "name": "ExtensionVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_agency_uri: Optional[ExtensionAgencyUri] = field(
        default=None,
        metadata={
            "name": "ExtensionAgencyURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_uri: Optional[ExtensionUri] = field(
        default=None,
        metadata={
            "name": "ExtensionURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_reason_code: Optional[ExtensionReasonCode] = field(
        default=None,
        metadata={
            "name": "ExtensionReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_reason: Optional[ExtensionReason] = field(
        default=None,
        metadata={
            "name": "ExtensionReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    extension_content: Optional[ExtensionContent] = field(
        default=None,
        metadata={
            "name": "ExtensionContent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class Ublextension(UblextensionType):
    class Meta:
        name = "UBLExtension"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass(frozen=True)
class UblextensionsType:
    class Meta:
        name = "UBLExtensionsType"

    ublextension: Tuple[Ublextension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "UBLExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class Ublextensions(UblextensionsType):
    class Meta:
        name = "UBLExtensions"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
