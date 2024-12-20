from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional

from xsdata.models.datatype import XmlDateTime

from ubl.models.common.ubl_xmldsig_core_schema_2_1 import (
    CanonicalizationMethod,
    DigestMethod,
    DigestValue,
    Signature,
    Transforms,
    X509IssuerSerialType,
)

__NAMESPACE__ = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class AnyType:
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(frozen=True)
class CrlidentifierType:
    class Meta:
        name = "CRLIdentifierType"

    issuer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issuer",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    issue_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class DocumentationReferencesType:
    documentation_reference: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentationReference",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class EncapsulatedPkidataType:
    class Meta:
        name = "EncapsulatedPKIDataType"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class IncludeType:
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        },
    )
    referenced_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "referencedData",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class IntegerListType:
    int_value: tuple[int, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "int",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


class QualifierType(Enum):
    OIDAS_URI = "OIDAsURI"
    OIDAS_URN = "OIDAsURN"


@dataclass(frozen=True)
class QualifyingPropertiesReferenceType:
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class ResponderIdtype:
    class Meta:
        name = "ResponderIDType"

    by_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ByName",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    by_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ByKey",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "format": "base64",
        },
    )


@dataclass(frozen=True)
class Spuri:
    class Meta:
        name = "SPURI"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(frozen=True)
class SignatureProductionPlaceType:
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    state_or_province: Optional[str] = field(
        default=None,
        metadata={
            "name": "StateOrProvince",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    country_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(frozen=True)
class SigningTime:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass(frozen=True)
class AnyModel(AnyType):
    class Meta:
        name = "Any"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class CrlvaluesType:
    class Meta:
        name = "CRLValuesType"

    encapsulated_crlvalue: tuple[EncapsulatedPkidataType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EncapsulatedCRLValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class CertificateValuesType:
    encapsulated_x509_certificate: tuple[EncapsulatedPkidataType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EncapsulatedX509Certificate",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    other_certificate: tuple[AnyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OtherCertificate",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class CertifiedRolesListType:
    certified_role: tuple[EncapsulatedPkidataType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CertifiedRole",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class ClaimedRolesListType:
    claimed_role: tuple[AnyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ClaimedRole",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class CommitmentTypeQualifiersListType:
    commitment_type_qualifier: tuple[AnyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CommitmentTypeQualifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(frozen=True)
class CounterSignatureType:
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass(frozen=True)
class DigestAlgAndValueType:
    digest_method: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )
    digest_value: Optional[DigestValue] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass(frozen=True)
class EncapsulatedPkidata(EncapsulatedPkidataType):
    class Meta:
        name = "EncapsulatedPKIData"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class IdentifierType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    qualifier: Optional[QualifierType] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class Include(IncludeType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class NoticeReferenceType:
    organization: Optional[str] = field(
        default=None,
        metadata={
            "name": "Organization",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    notice_numbers: Optional[IntegerListType] = field(
        default=None,
        metadata={
            "name": "NoticeNumbers",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )


@dataclass(frozen=True)
class OcspidentifierType:
    class Meta:
        name = "OCSPIdentifierType"

    responder_id: Optional[ResponderIdtype] = field(
        default=None,
        metadata={
            "name": "ResponderID",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    produced_at: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ProducedAt",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class OcspvaluesType:
    class Meta:
        name = "OCSPValuesType"

    encapsulated_ocspvalue: tuple[EncapsulatedPkidataType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EncapsulatedOCSPValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class OtherCertStatusRefsType:
    other_ref: tuple[AnyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OtherRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class OtherCertStatusValuesType:
    other_value: tuple[AnyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OtherValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class QualifyingPropertiesReference(QualifyingPropertiesReferenceType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class ReferenceInfoType:
    digest_method: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )
    digest_value: Optional[DigestValue] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class SigPolicyQualifiersListType:
    sig_policy_qualifier: tuple[AnyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SigPolicyQualifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class SignatureProductionPlace(SignatureProductionPlaceType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class UnsignedDataObjectPropertiesType:
    unsigned_data_object_property: tuple[AnyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "UnsignedDataObjectProperty",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class AttrAuthoritiesCertValues(CertificateValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class CrlrefType:
    class Meta:
        name = "CRLRefType"

    digest_alg_and_value: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "name": "DigestAlgAndValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    crlidentifier: Optional[CrlidentifierType] = field(
        default=None,
        metadata={
            "name": "CRLIdentifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(frozen=True)
class CertIdtype:
    class Meta:
        name = "CertIDType"

    cert_digest: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "name": "CertDigest",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    issuer_serial: Optional[X509IssuerSerialType] = field(
        default=None,
        metadata={
            "name": "IssuerSerial",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class CertificateValues(CertificateValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class CounterSignature(CounterSignatureType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class OcsprefType:
    class Meta:
        name = "OCSPRefType"

    ocspidentifier: Optional[OcspidentifierType] = field(
        default=None,
        metadata={
            "name": "OCSPIdentifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    digest_alg_and_value: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "name": "DigestAlgAndValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(frozen=True)
class ObjectIdentifierType:
    identifier: Optional[IdentifierType] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    documentation_references: Optional[DocumentationReferencesType] = field(
        default=None,
        metadata={
            "name": "DocumentationReferences",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(frozen=True)
class ReferenceInfo(ReferenceInfoType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class RevocationValuesType:
    crlvalues: Optional[CrlvaluesType] = field(
        default=None,
        metadata={
            "name": "CRLValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    ocspvalues: Optional[OcspvaluesType] = field(
        default=None,
        metadata={
            "name": "OCSPValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    other_values: Optional[OtherCertStatusValuesType] = field(
        default=None,
        metadata={
            "name": "OtherValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class SpuserNoticeType:
    class Meta:
        name = "SPUserNoticeType"

    notice_ref: Optional[NoticeReferenceType] = field(
        default=None,
        metadata={
            "name": "NoticeRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    explicit_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExplicitText",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(frozen=True)
class SignerRoleType:
    claimed_roles: Optional[ClaimedRolesListType] = field(
        default=None,
        metadata={
            "name": "ClaimedRoles",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    certified_roles: Optional[CertifiedRolesListType] = field(
        default=None,
        metadata={
            "name": "CertifiedRoles",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(frozen=True)
class UnsignedDataObjectProperties(UnsignedDataObjectPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class AttributeRevocationValues(RevocationValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class CrlrefsType:
    class Meta:
        name = "CRLRefsType"

    crlref: tuple[CrlrefType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CRLRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class CertIdlistType:
    class Meta:
        name = "CertIDListType"

    cert: tuple[CertIdtype, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class CommitmentTypeIndicationType:
    commitment_type_id: Optional[ObjectIdentifierType] = field(
        default=None,
        metadata={
            "name": "CommitmentTypeId",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    object_reference: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ObjectReference",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    all_signed_data_objects: Optional[object] = field(
        default=None,
        metadata={
            "name": "AllSignedDataObjects",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    commitment_type_qualifiers: Optional[CommitmentTypeQualifiersListType] = (
        field(
            default=None,
            metadata={
                "name": "CommitmentTypeQualifiers",
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )


@dataclass(frozen=True)
class DataObjectFormatType:
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    object_identifier: Optional[ObjectIdentifierType] = field(
        default=None,
        metadata={
            "name": "ObjectIdentifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    object_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ObjectReference",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True)
class GenericTimeStampType:
    include: tuple[Include, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Include",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    reference_info: tuple[ReferenceInfo, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReferenceInfo",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    canonicalization_method: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    encapsulated_time_stamp: tuple[EncapsulatedPkidataType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EncapsulatedTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    xmltime_stamp: tuple[AnyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "XMLTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class OcsprefsType:
    class Meta:
        name = "OCSPRefsType"

    ocspref: tuple[OcsprefType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OCSPRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class ObjectIdentifier(ObjectIdentifierType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class RevocationValues(RevocationValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class SpuserNotice(SpuserNoticeType):
    class Meta:
        name = "SPUserNotice"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class SignaturePolicyIdType:
    sig_policy_id: Optional[ObjectIdentifierType] = field(
        default=None,
        metadata={
            "name": "SigPolicyId",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    sig_policy_hash: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "name": "SigPolicyHash",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    sig_policy_qualifiers: Optional[SigPolicyQualifiersListType] = field(
        default=None,
        metadata={
            "name": "SigPolicyQualifiers",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(frozen=True)
class SignerRole(SignerRoleType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class CommitmentTypeIndication(CommitmentTypeIndicationType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class CompleteCertificateRefsType:
    cert_refs: Optional[CertIdlistType] = field(
        default=None,
        metadata={
            "name": "CertRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class CompleteRevocationRefsType:
    crlrefs: Optional[CrlrefsType] = field(
        default=None,
        metadata={
            "name": "CRLRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    ocsprefs: Optional[OcsprefsType] = field(
        default=None,
        metadata={
            "name": "OCSPRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    other_refs: Optional[OtherCertStatusRefsType] = field(
        default=None,
        metadata={
            "name": "OtherRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class DataObjectFormat(DataObjectFormatType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class OtherTimeStampType(GenericTimeStampType):
    include: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    reference_info: tuple[ReferenceInfo, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReferenceInfo",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class SignaturePolicyIdentifierType:
    signature_policy_id: Optional[SignaturePolicyIdType] = field(
        default=None,
        metadata={
            "name": "SignaturePolicyId",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signature_policy_implied: Optional[object] = field(
        default=None,
        metadata={
            "name": "SignaturePolicyImplied",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(frozen=True)
class SigningCertificate(CertIdlistType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class XadEstimeStampType(GenericTimeStampType):
    class Meta:
        name = "XAdESTimeStampType"

    reference_info: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True)
class AllDataObjectsTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class ArchiveTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class AttributeCertificateRefs(CompleteCertificateRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class AttributeRevocationRefs(CompleteRevocationRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class CompleteCertificateRefs(CompleteCertificateRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class CompleteRevocationRefs(CompleteRevocationRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class IndividualDataObjectsTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class OtherTimeStamp(OtherTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class RefsOnlyTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class SigAndRefsTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class SignaturePolicyIdentifier(SignaturePolicyIdentifierType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class SignatureTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class SignedDataObjectPropertiesType:
    data_object_format: tuple[DataObjectFormatType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DataObjectFormat",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    commitment_type_indication: tuple[CommitmentTypeIndicationType, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "CommitmentTypeIndication",
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )
    all_data_objects_time_stamp: tuple[XadEstimeStampType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllDataObjectsTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    individual_data_objects_time_stamp: tuple[XadEstimeStampType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "IndividualDataObjectsTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class SignedSignaturePropertiesType:
    signing_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SigningTime",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signing_certificate: Optional[CertIdlistType] = field(
        default=None,
        metadata={
            "name": "SigningCertificate",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signature_policy_identifier: Optional[SignaturePolicyIdentifierType] = (
        field(
            default=None,
            metadata={
                "name": "SignaturePolicyIdentifier",
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )
    signature_production_place: Optional[SignatureProductionPlaceType] = field(
        default=None,
        metadata={
            "name": "SignatureProductionPlace",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signer_role: Optional[SignerRoleType] = field(
        default=None,
        metadata={
            "name": "SignerRole",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class UnsignedSignaturePropertiesType:
    counter_signature: tuple[CounterSignatureType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CounterSignature",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signature_time_stamp: tuple[XadEstimeStampType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SignatureTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    complete_certificate_refs: tuple[CompleteCertificateRefsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CompleteCertificateRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    complete_revocation_refs: tuple[CompleteRevocationRefsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CompleteRevocationRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    attribute_certificate_refs: tuple[CompleteCertificateRefsType, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "AttributeCertificateRefs",
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )
    attribute_revocation_refs: tuple[CompleteRevocationRefsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AttributeRevocationRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    sig_and_refs_time_stamp: tuple[XadEstimeStampType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SigAndRefsTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    refs_only_time_stamp: tuple[XadEstimeStampType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RefsOnlyTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    certificate_values: tuple[CertificateValuesType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CertificateValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    revocation_values: tuple[RevocationValuesType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RevocationValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    attr_authorities_cert_values: tuple[CertificateValuesType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AttrAuthoritiesCertValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    attribute_revocation_values: tuple[RevocationValuesType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AttributeRevocationValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    archive_time_stamp: tuple[XadEstimeStampType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ArchiveTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    other_element: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class XadEstimeStamp(XadEstimeStampType):
    class Meta:
        name = "XAdESTimeStamp"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class SignedDataObjectProperties(SignedDataObjectPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class SignedPropertiesType:
    signed_signature_properties: Optional[SignedSignaturePropertiesType] = (
        field(
            default=None,
            metadata={
                "name": "SignedSignatureProperties",
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )
    signed_data_object_properties: Optional[SignedDataObjectPropertiesType] = (
        field(
            default=None,
            metadata={
                "name": "SignedDataObjectProperties",
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class SignedSignatureProperties(SignedSignaturePropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class UnsignedPropertiesType:
    unsigned_signature_properties: Optional[
        UnsignedSignaturePropertiesType
    ] = field(
        default=None,
        metadata={
            "name": "UnsignedSignatureProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    unsigned_data_object_properties: Optional[
        UnsignedDataObjectPropertiesType
    ] = field(
        default=None,
        metadata={
            "name": "UnsignedDataObjectProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class UnsignedSignatureProperties(UnsignedSignaturePropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class QualifyingPropertiesType:
    signed_properties: Optional[SignedPropertiesType] = field(
        default=None,
        metadata={
            "name": "SignedProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    unsigned_properties: Optional[UnsignedPropertiesType] = field(
        default=None,
        metadata={
            "name": "UnsignedProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    target: Optional[str] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class SignedProperties(SignedPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class UnsignedProperties(UnsignedPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(frozen=True)
class QualifyingProperties(QualifyingPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"
