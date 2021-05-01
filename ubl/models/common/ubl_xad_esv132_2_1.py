from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional
from xsdata.models.datatype import XmlDateTime
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import (
    CanonicalizationMethod,
    DigestMethod,
    Signature,
    Transforms,
    X509IssuerSerialType,
)

__NAMESPACE__ = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class AnyType:
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
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
        }
    )
    issue_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )


@dataclass
class DocumentationReferencesType:
    documentation_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DocumentationReference",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class EncapsulatedPkidataType:
    class Meta:
        name = "EncapsulatedPKIDataType"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Attribute",
        }
    )


@dataclass
class IncludeType:
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        }
    )
    referenced_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "referencedData",
            "type": "Attribute",
        }
    )


@dataclass
class IntegerListType:
    int_value: List[int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


class QualifierType(Enum):
    OIDAS_URI = "OIDAsURI"
    OIDAS_URN = "OIDAsURN"


@dataclass
class QualifyingPropertiesReferenceType:
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class ResponderIdtype:
    class Meta:
        name = "ResponderIDType"

    by_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ByName",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    by_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ByKey",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "format": "base64",
        }
    )


@dataclass
class Spuri:
    class Meta:
        name = "SPURI"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SignatureProductionPlaceType:
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    state_or_province: Optional[str] = field(
        default=None,
        metadata={
            "name": "StateOrProvince",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    country_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
class SigningTime:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Any(AnyType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CrlvaluesType:
    class Meta:
        name = "CRLValuesType"

    encapsulated_crlvalue: List[EncapsulatedPkidataType] = field(
        default_factory=list,
        metadata={
            "name": "EncapsulatedCRLValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class CertificateValuesType:
    encapsulated_x509_certificate: List[EncapsulatedPkidataType] = field(
        default_factory=list,
        metadata={
            "name": "EncapsulatedX509Certificate",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    other_certificate: List[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "OtherCertificate",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class CertifiedRolesListType:
    certified_role: List[EncapsulatedPkidataType] = field(
        default_factory=list,
        metadata={
            "name": "CertifiedRole",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class ClaimedRolesListType:
    claimed_role: List[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "ClaimedRole",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class CommitmentTypeQualifiersListType:
    commitment_type_qualifier: List[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "CommitmentTypeQualifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
class CounterSignatureType:
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class DigestAlgAndValueType:
    digest_method: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class EncapsulatedPkidata(EncapsulatedPkidataType):
    class Meta:
        name = "EncapsulatedPKIData"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class IdentifierType:
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    qualifier: Optional[QualifierType] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Attribute",
        }
    )


@dataclass
class Include(IncludeType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class NoticeReferenceType:
    organization: Optional[str] = field(
        default=None,
        metadata={
            "name": "Organization",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        }
    )
    notice_numbers: Optional[IntegerListType] = field(
        default=None,
        metadata={
            "name": "NoticeNumbers",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        }
    )


@dataclass
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
        }
    )
    produced_at: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ProducedAt",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )


@dataclass
class OcspvaluesType:
    class Meta:
        name = "OCSPValuesType"

    encapsulated_ocspvalue: List[EncapsulatedPkidataType] = field(
        default_factory=list,
        metadata={
            "name": "EncapsulatedOCSPValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class OtherCertStatusRefsType:
    other_ref: List[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "OtherRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class OtherCertStatusValuesType:
    other_value: List[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "OtherValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class QualifyingPropertiesReference(QualifyingPropertiesReferenceType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class ReferenceInfoType:
    digest_method: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )


@dataclass
class SigPolicyQualifiersListType:
    sig_policy_qualifier: List[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "SigPolicyQualifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class SignatureProductionPlace(SignatureProductionPlaceType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class UnsignedDataObjectPropertiesType:
    unsigned_data_object_property: List[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "UnsignedDataObjectProperty",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class AttrAuthoritiesCertValues(CertificateValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
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
        }
    )
    crlidentifier: Optional[CrlidentifierType] = field(
        default=None,
        metadata={
            "name": "CRLIdentifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
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
        }
    )
    issuer_serial: Optional[X509IssuerSerialType] = field(
        default=None,
        metadata={
            "name": "IssuerSerial",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )


@dataclass
class CertificateValues(CertificateValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CounterSignature(CounterSignatureType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
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
        }
    )
    digest_alg_and_value: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "name": "DigestAlgAndValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
class ObjectIdentifierType:
    identifier: Optional[IdentifierType] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    documentation_references: Optional[DocumentationReferencesType] = field(
        default=None,
        metadata={
            "name": "DocumentationReferences",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
class ReferenceInfo(ReferenceInfoType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class RevocationValuesType:
    crlvalues: Optional[CrlvaluesType] = field(
        default=None,
        metadata={
            "name": "CRLValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    ocspvalues: Optional[OcspvaluesType] = field(
        default=None,
        metadata={
            "name": "OCSPValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    other_values: Optional[OtherCertStatusValuesType] = field(
        default=None,
        metadata={
            "name": "OtherValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class SpuserNoticeType:
    class Meta:
        name = "SPUserNoticeType"

    notice_ref: Optional[NoticeReferenceType] = field(
        default=None,
        metadata={
            "name": "NoticeRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    explicit_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExplicitText",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
class SignerRoleType:
    claimed_roles: Optional[ClaimedRolesListType] = field(
        default=None,
        metadata={
            "name": "ClaimedRoles",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    certified_roles: Optional[CertifiedRolesListType] = field(
        default=None,
        metadata={
            "name": "CertifiedRoles",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
class UnsignedDataObjectProperties(UnsignedDataObjectPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class AttributeRevocationValues(RevocationValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CrlrefsType:
    class Meta:
        name = "CRLRefsType"

    crlref: List[CrlrefType] = field(
        default_factory=list,
        metadata={
            "name": "CRLRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class CertIdlistType:
    class Meta:
        name = "CertIDListType"

    cert: List[CertIdtype] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class CommitmentTypeIndicationType:
    commitment_type_id: Optional[ObjectIdentifierType] = field(
        default=None,
        metadata={
            "name": "CommitmentTypeId",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        }
    )
    object_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ObjectReference",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    all_signed_data_objects: Optional[object] = field(
        default=None,
        metadata={
            "name": "AllSignedDataObjects",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    commitment_type_qualifiers: Optional[CommitmentTypeQualifiersListType] = field(
        default=None,
        metadata={
            "name": "CommitmentTypeQualifiers",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
class DataObjectFormatType:
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    object_identifier: Optional[ObjectIdentifierType] = field(
        default=None,
        metadata={
            "name": "ObjectIdentifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    object_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ObjectReference",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class GenericTimeStampType:
    include: List[Include] = field(
        default_factory=list,
        metadata={
            "name": "Include",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    reference_info: List[ReferenceInfo] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceInfo",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    canonicalization_method: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    encapsulated_time_stamp: List[EncapsulatedPkidataType] = field(
        default_factory=list,
        metadata={
            "name": "EncapsulatedTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "sequential": True,
        }
    )
    xmltime_stamp: List[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "XMLTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class OcsprefsType:
    class Meta:
        name = "OCSPRefsType"

    ocspref: List[OcsprefType] = field(
        default_factory=list,
        metadata={
            "name": "OCSPRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )


@dataclass
class ObjectIdentifier(ObjectIdentifierType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class RevocationValues(RevocationValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SpuserNotice(SpuserNoticeType):
    class Meta:
        name = "SPUserNotice"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignaturePolicyIdType:
    sig_policy_id: Optional[ObjectIdentifierType] = field(
        default=None,
        metadata={
            "name": "SigPolicyId",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        }
    )
    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    sig_policy_hash: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "name": "SigPolicyHash",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        }
    )
    sig_policy_qualifiers: Optional[SigPolicyQualifiersListType] = field(
        default=None,
        metadata={
            "name": "SigPolicyQualifiers",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
class SignerRole(SignerRoleType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CommitmentTypeIndication(CommitmentTypeIndicationType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CompleteCertificateRefsType:
    cert_refs: Optional[CertIdlistType] = field(
        default=None,
        metadata={
            "name": "CertRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class CompleteRevocationRefsType:
    crlrefs: Optional[CrlrefsType] = field(
        default=None,
        metadata={
            "name": "CRLRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    ocsprefs: Optional[OcsprefsType] = field(
        default=None,
        metadata={
            "name": "OCSPRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    other_refs: Optional[OtherCertStatusRefsType] = field(
        default=None,
        metadata={
            "name": "OtherRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class DataObjectFormat(DataObjectFormatType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class OtherTimeStampType(GenericTimeStampType):
    reference_info: List[ReferenceInfo] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceInfo",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        }
    )
    encapsulated_time_stamp: Optional[EncapsulatedPkidataType] = field(
        default=None,
        metadata={
            "name": "EncapsulatedTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    xmltime_stamp: Optional[AnyType] = field(
        default=None,
        metadata={
            "name": "XMLTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
class SignaturePolicyIdentifierType:
    signature_policy_id: Optional[SignaturePolicyIdType] = field(
        default=None,
        metadata={
            "name": "SignaturePolicyId",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    signature_policy_implied: Optional[object] = field(
        default=None,
        metadata={
            "name": "SignaturePolicyImplied",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass
class SigningCertificate(CertIdlistType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class XadEstimeStampType(GenericTimeStampType):
    class Meta:
        name = "XAdESTimeStampType"


@dataclass
class AllDataObjectsTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class ArchiveTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class AttributeCertificateRefs(CompleteCertificateRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class AttributeRevocationRefs(CompleteRevocationRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CompleteCertificateRefs(CompleteCertificateRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CompleteRevocationRefs(CompleteRevocationRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class IndividualDataObjectsTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class OtherTimeStamp(OtherTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class RefsOnlyTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SigAndRefsTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignaturePolicyIdentifier(SignaturePolicyIdentifierType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignatureTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignedDataObjectPropertiesType:
    data_object_format: List[DataObjectFormatType] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectFormat",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    commitment_type_indication: List[CommitmentTypeIndicationType] = field(
        default_factory=list,
        metadata={
            "name": "CommitmentTypeIndication",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    all_data_objects_time_stamp: List[XadEstimeStampType] = field(
        default_factory=list,
        metadata={
            "name": "AllDataObjectsTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    individual_data_objects_time_stamp: List[XadEstimeStampType] = field(
        default_factory=list,
        metadata={
            "name": "IndividualDataObjectsTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class SignedSignaturePropertiesType:
    signing_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SigningTime",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    signing_certificate: Optional[CertIdlistType] = field(
        default=None,
        metadata={
            "name": "SigningCertificate",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    signature_policy_identifier: Optional[SignaturePolicyIdentifierType] = field(
        default=None,
        metadata={
            "name": "SignaturePolicyIdentifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    signature_production_place: Optional[SignatureProductionPlaceType] = field(
        default=None,
        metadata={
            "name": "SignatureProductionPlace",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    signer_role: Optional[SignerRoleType] = field(
        default=None,
        metadata={
            "name": "SignerRole",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class UnsignedSignaturePropertiesType:
    counter_signature: List[CounterSignatureType] = field(
        default_factory=list,
        metadata={
            "name": "CounterSignature",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    signature_time_stamp: List[XadEstimeStampType] = field(
        default_factory=list,
        metadata={
            "name": "SignatureTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    complete_certificate_refs: List[CompleteCertificateRefsType] = field(
        default_factory=list,
        metadata={
            "name": "CompleteCertificateRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    complete_revocation_refs: List[CompleteRevocationRefsType] = field(
        default_factory=list,
        metadata={
            "name": "CompleteRevocationRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    attribute_certificate_refs: List[CompleteCertificateRefsType] = field(
        default_factory=list,
        metadata={
            "name": "AttributeCertificateRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    attribute_revocation_refs: List[CompleteRevocationRefsType] = field(
        default_factory=list,
        metadata={
            "name": "AttributeRevocationRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    sig_and_refs_time_stamp: List[XadEstimeStampType] = field(
        default_factory=list,
        metadata={
            "name": "SigAndRefsTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    refs_only_time_stamp: List[XadEstimeStampType] = field(
        default_factory=list,
        metadata={
            "name": "RefsOnlyTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    certificate_values: List[CertificateValuesType] = field(
        default_factory=list,
        metadata={
            "name": "CertificateValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    revocation_values: List[RevocationValuesType] = field(
        default_factory=list,
        metadata={
            "name": "RevocationValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    attr_authorities_cert_values: List[CertificateValuesType] = field(
        default_factory=list,
        metadata={
            "name": "AttrAuthoritiesCertValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    attribute_revocation_values: List[RevocationValuesType] = field(
        default_factory=list,
        metadata={
            "name": "AttributeRevocationValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    archive_time_stamp: List[XadEstimeStampType] = field(
        default_factory=list,
        metadata={
            "name": "ArchiveTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class XadEstimeStamp(XadEstimeStampType):
    class Meta:
        name = "XAdESTimeStamp"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignedDataObjectProperties(SignedDataObjectPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignedPropertiesType:
    signed_signature_properties: Optional[SignedSignaturePropertiesType] = field(
        default=None,
        metadata={
            "name": "SignedSignatureProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    signed_data_object_properties: Optional[SignedDataObjectPropertiesType] = field(
        default=None,
        metadata={
            "name": "SignedDataObjectProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class SignedSignatureProperties(SignedSignaturePropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class UnsignedPropertiesType:
    unsigned_signature_properties: Optional[UnsignedSignaturePropertiesType] = field(
        default=None,
        metadata={
            "name": "UnsignedSignatureProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    unsigned_data_object_properties: Optional[UnsignedDataObjectPropertiesType] = field(
        default=None,
        metadata={
            "name": "UnsignedDataObjectProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class UnsignedSignatureProperties(UnsignedSignaturePropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class QualifyingPropertiesType:
    signed_properties: Optional[SignedPropertiesType] = field(
        default=None,
        metadata={
            "name": "SignedProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    unsigned_properties: Optional[UnsignedPropertiesType] = field(
        default=None,
        metadata={
            "name": "UnsignedProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    target: Optional[str] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class SignedProperties(SignedPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class UnsignedProperties(UnsignedPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class QualifyingProperties(QualifyingPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"
