from dataclasses import dataclass, field
from typing import List, Optional
from ubl.models.common.ubl_common_basic_components_2_1 import (
    Id,
    Name,
)
from ubl.models.common.ubl_extension_content_data_type_2_1 import ExtensionContentType
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    CodeType,
    IdentifierType,
    TextType,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionAgencyIdtype(IdentifierType):
    class Meta:
        name = "ExtensionAgencyIDType"


@dataclass
class ExtensionAgencyNameType(TextType):
    pass


@dataclass
class ExtensionAgencyUritype(IdentifierType):
    class Meta:
        name = "ExtensionAgencyURIType"


@dataclass
class ExtensionContent(ExtensionContentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionReasonCodeType(CodeType):
    pass


@dataclass
class ExtensionReasonType(TextType):
    pass


@dataclass
class ExtensionUritype(IdentifierType):
    class Meta:
        name = "ExtensionURIType"


@dataclass
class ExtensionVersionIdtype(IdentifierType):
    class Meta:
        name = "ExtensionVersionIDType"


@dataclass
class ExtensionAgencyId(ExtensionAgencyIdtype):
    class Meta:
        name = "ExtensionAgencyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionAgencyName(ExtensionAgencyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionAgencyUri(ExtensionAgencyUritype):
    class Meta:
        name = "ExtensionAgencyURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionReason(ExtensionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionReasonCode(ExtensionReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionUri(ExtensionUritype):
    class Meta:
        name = "ExtensionURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionVersionId(ExtensionVersionIdtype):
    class Meta:
        name = "ExtensionVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class UblextensionType:
    class Meta:
        name = "UBLExtensionType"

    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    extension_agency_id: Optional[ExtensionAgencyId] = field(
        default=None,
        metadata={
            "name": "ExtensionAgencyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        }
    )
    extension_agency_name: Optional[ExtensionAgencyName] = field(
        default=None,
        metadata={
            "name": "ExtensionAgencyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        }
    )
    extension_version_id: Optional[ExtensionVersionId] = field(
        default=None,
        metadata={
            "name": "ExtensionVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        }
    )
    extension_agency_uri: Optional[ExtensionAgencyUri] = field(
        default=None,
        metadata={
            "name": "ExtensionAgencyURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        }
    )
    extension_uri: Optional[ExtensionUri] = field(
        default=None,
        metadata={
            "name": "ExtensionURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        }
    )
    extension_reason_code: Optional[ExtensionReasonCode] = field(
        default=None,
        metadata={
            "name": "ExtensionReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        }
    )
    extension_reason: Optional[ExtensionReason] = field(
        default=None,
        metadata={
            "name": "ExtensionReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        }
    )
    extension_content: Optional[ExtensionContent] = field(
        default=None,
        metadata={
            "name": "ExtensionContent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "required": True,
        }
    )


@dataclass
class Ublextension(UblextensionType):
    class Meta:
        name = "UBLExtension"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class UblextensionsType:
    class Meta:
        name = "UBLExtensionsType"

    ublextension: List[Ublextension] = field(
        default_factory=list,
        metadata={
            "name": "UBLExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class Ublextensions(UblextensionsType):
    class Meta:
        name = "UBLExtensions"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
