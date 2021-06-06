from dataclasses import dataclass, field
from typing import List, Optional
from ...www.w3.org.pkg_2005.pkg_08.addressing.ws_addr import EndpointReferenceType

__NAMESPACE__ = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AcknowledgementType:
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class AssigningAuthorityType:
    assigning_authority_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigningAuthorityId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class ConnectcustomHttpHeadersType:
    class Meta:
        name = "CONNECTCustomHttpHeadersType"

    header_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "headerName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    header_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "headerValue",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class CeType:
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    original_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    translation: List["CeType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class CreateEprrequestType:
    class Meta:
        name = "CreateEPRRequestType"

    endpoint_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "endpointURL",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    namespace_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "namespaceURI",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    namespace_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "namespacePrefix",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    port_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "portName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class HomeCommunityType:
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    home_community_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "homeCommunityId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class QualifiedSubjectIdentifierType:
    subject_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubjectIdentifier",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    assigning_authority_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssigningAuthorityIdentifier",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class ResponseType:
    status: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class SamlAuthnStatementType:
    auth_instant: Optional[str] = field(
        default=None,
        metadata={
            "name": "authInstant",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    session_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "sessionIndex",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    auth_context_class_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "authContextClassRef",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    subject_locality_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "subjectLocalityAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    subject_locality_dnsname: Optional[str] = field(
        default=None,
        metadata={
            "name": "subjectLocalityDNSName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class SamlAuthzDecisionStatementEvidenceConditionsType:
    not_before: Optional[str] = field(
        default=None,
        metadata={
            "name": "notBefore",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    not_on_or_after: Optional[str] = field(
        default=None,
        metadata={
            "name": "notOnOrAfter",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class SamlConditionsType:
    not_before: Optional[str] = field(
        default=None,
        metadata={
            "name": "notBefore",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    not_on_or_after: Optional[str] = field(
        default=None,
        metadata={
            "name": "notOnOrAfter",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class SamlIssuerType:
    issuer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    issuer_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerFormat",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class SamlSignatureKeyInfoType:
    rsa_key_value_modulus: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "rsaKeyValueModulus",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "format": "base64",
        }
    )
    rsa_key_value_exponent: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "rsaKeyValueExponent",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "format": "base64",
        }
    )


@dataclass
class TokenRetrieveInfoType:
    request: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class UrlInfoType:
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class UrlSetType:
    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class Acknowledgement(AcknowledgementType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AddressType:
    address_type: Optional[CeType] = field(
        default=None,
        metadata={
            "name": "addressType",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    street_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "streetAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    zip_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "zipCode",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class AssigningAuthoritiesType:
    assigning_authority: List[AssigningAuthorityType] = field(
        default_factory=list,
        metadata={
            "name": "assigningAuthority",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class AssigningAuthority(AssigningAuthorityType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class ConnectcustomHttpHeaders(ConnectcustomHttpHeadersType):
    class Meta:
        name = "CONNECTCustomHttpHeaders"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Ce(CeType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class CreateEprrequest(CreateEprrequestType):
    class Meta:
        name = "CreateEPRRequest"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Epr(EndpointReferenceType):
    class Meta:
        name = "EPR"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class HomeCommunitiesType:
    home_community: List[HomeCommunityType] = field(
        default_factory=list,
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class HomeCommunity(HomeCommunityType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class NhinTargetCommunityType:
    home_community: Optional[HomeCommunityType] = field(
        default=None,
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    list_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class NhinTargetSystemType:
    epr: Optional[EndpointReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    home_community: Optional[HomeCommunityType] = field(
        default=None,
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    exchange_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "exchangeName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    use_spec_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "useSpecVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class PersonNameType:
    family_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    name_type: Optional[CeType] = field(
        default=None,
        metadata={
            "name": "nameType",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    second_name_or_initials: Optional[str] = field(
        default=None,
        metadata={
            "name": "secondNameOrInitials",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fullName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class PhoneType:
    area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "areaCode",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "countryCode",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    local_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "localNumber",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    phone_number_type: Optional[CeType] = field(
        default=None,
        metadata={
            "name": "phoneNumberType",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class QualifiedSubjectIdentifier(QualifiedSubjectIdentifierType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class QualifiedSubjectIdentifiersType:
    qualified_subject_identifier: List[QualifiedSubjectIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "QualifiedSubjectIdentifier",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class Response(ResponseType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthnStatement(SamlAuthnStatementType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementEvidenceAssertionType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    issue_instant: Optional[str] = field(
        default=None,
        metadata={
            "name": "issueInstant",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    issuer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    issuer_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerFormat",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    subject: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    conditions: Optional[SamlAuthzDecisionStatementEvidenceConditionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    access_consent_policy: List[str] = field(
        default_factory=list,
        metadata={
            "name": "accessConsentPolicy",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    instance_access_consent_policy: List[str] = field(
        default_factory=list,
        metadata={
            "name": "instanceAccessConsentPolicy",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class SamlAuthzDecisionStatementEvidenceConditions(SamlAuthzDecisionStatementEvidenceConditionsType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlConditions(SamlConditionsType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlIssuer(SamlIssuerType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlSignatureKeyInfo(SamlSignatureKeyInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlSignatureType:
    key_info: Optional[SamlSignatureKeyInfoType] = field(
        default=None,
        metadata={
            "name": "keyInfo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    signature_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "signatureValue",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "format": "base64",
        }
    )


@dataclass
class SamlSubjectConfirmationType:
    method: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    subject_condition: Optional[SamlConditionsType] = field(
        default=None,
        metadata={
            "name": "subjectCondition",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    recipient: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    in_response_to: Optional[str] = field(
        default=None,
        metadata={
            "name": "inResponseTo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class TokenRetrieveInfo(TokenRetrieveInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class UrlInfo(UrlInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class UrlSet(UrlSetType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Address(AddressType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AddressesType:
    address: List[AddressType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "min_occurs": 1,
        }
    )


@dataclass
class HomeCommunities(HomeCommunitiesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class NhinTargetCommunitiesType:
    nhin_target_community: List[NhinTargetCommunityType] = field(
        default_factory=list,
        metadata={
            "name": "nhinTargetCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "min_occurs": 1,
        }
    )
    use_spec_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "useSpecVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    exchange_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "exchangeName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class NhinTargetCommunity(NhinTargetCommunityType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class NhinTargetSystem(NhinTargetSystemType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class PersonName(PersonNameType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Phone(PhoneType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class QualifiedSubjectIdentifiers(QualifiedSubjectIdentifiersType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementEvidenceAssertion(SamlAuthzDecisionStatementEvidenceAssertionType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementEvidenceType:
    assertion: Optional[SamlAuthzDecisionStatementEvidenceAssertionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class SamlSignature(SamlSignatureType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class UserType:
    person_name: Optional[PersonNameType] = field(
        default=None,
        metadata={
            "name": "personName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "userName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    org: Optional[HomeCommunityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    role_coded: Optional[CeType] = field(
        default=None,
        metadata={
            "name": "roleCoded",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class AssigningAuthorites(AssigningAuthoritiesType):
    class Meta:
        name = "assigningAuthorites"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Addresses(AddressesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class ConfigAssertionType:
    user_info: Optional[UserType] = field(
        default=None,
        metadata={
            "name": "userInfo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    config_instance: Optional[str] = field(
        default=None,
        metadata={
            "name": "configInstance",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    auth_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "authMethod",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class NhinTargetCommunities(NhinTargetCommunitiesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementEvidence(SamlAuthzDecisionStatementEvidenceType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementType:
    decision: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    resource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    action: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    evidence: Optional[SamlAuthzDecisionStatementEvidenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class User(UserType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AssertionType:
    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    date_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "dateOfBirth",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    explanation_non_claimant_signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "explanationNonClaimantSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    have_second_witness_signature: Optional[bool] = field(
        default=None,
        metadata={
            "name": "haveSecondWitnessSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    have_signature: Optional[bool] = field(
        default=None,
        metadata={
            "name": "haveSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    have_witness_signature: Optional[bool] = field(
        default=None,
        metadata={
            "name": "haveWitnessSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    home_community: Optional[HomeCommunityType] = field(
        default=None,
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    national_provider_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "nationalProviderId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    person_name: Optional[PersonNameType] = field(
        default=None,
        metadata={
            "name": "personName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    phone_number: Optional[PhoneType] = field(
        default=None,
        metadata={
            "name": "phoneNumber",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    second_witness_address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "secondWitnessAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    second_witness_name: Optional[PersonNameType] = field(
        default=None,
        metadata={
            "name": "secondWitnessName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    second_witness_phone: Optional[PhoneType] = field(
        default=None,
        metadata={
            "name": "secondWitnessPhone",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    ssn: Optional[str] = field(
        default=None,
        metadata={
            "name": "SSN",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    unique_patient_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uniquePatientId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    witness_address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "witnessAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    witness_name: Optional[PersonNameType] = field(
        default=None,
        metadata={
            "name": "witnessName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    witness_phone: Optional[PhoneType] = field(
        default=None,
        metadata={
            "name": "witnessPhone",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    user_info: Optional[UserType] = field(
        default=None,
        metadata={
            "name": "userInfo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    authorized: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    purpose_of_disclosure_coded: Optional[CeType] = field(
        default=None,
        metadata={
            "name": "purposeOfDisclosureCoded",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    acp_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "acpAttribute",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    instance_acp_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "instanceAcpAttribute",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    saml_conditions: Optional[SamlConditionsType] = field(
        default=None,
        metadata={
            "name": "samlConditions",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    saml_authn_statement: Optional[SamlAuthnStatementType] = field(
        default=None,
        metadata={
            "name": "samlAuthnStatement",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    saml_authz_decision_statement: Optional[SamlAuthzDecisionStatementType] = field(
        default=None,
        metadata={
            "name": "samlAuthzDecisionStatement",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    saml_signature: Optional[SamlSignatureType] = field(
        default=None,
        metadata={
            "name": "samlSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    saml_issuer: Optional[SamlIssuerType] = field(
        default=None,
        metadata={
            "name": "samlIssuer",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    saml_subject_confirmations: List[SamlSubjectConfirmationType] = field(
        default_factory=list,
        metadata={
            "name": "samlSubjectConfirmations",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    message_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "messageId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    relates_to_list: List[str] = field(
        default_factory=list,
        metadata={
            "name": "relatesToList",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    implements_spec_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "implementsSpecVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    transaction_timeout: Optional[int] = field(
        default=None,
        metadata={
            "name": "transactionTimeout",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    keep_alive: Optional[str] = field(
        default=None,
        metadata={
            "name": "keepAlive",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    connectcustom_http_headers: List[ConnectcustomHttpHeadersType] = field(
        default_factory=list,
        metadata={
            "name": "CONNECTCustomHttpHeaders",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    signature_algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "signatureAlgorithm",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    digest_algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "digestAlgorithm",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass
class ConfigAssertion(ConfigAssertionType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatement(SamlAuthzDecisionStatementType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class Assertion(AssertionType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class TokenCreationInfoType:
    assertion: Optional[AssertionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    action_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "actionName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )
    resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "resourceName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        }
    )


@dataclass
class TokenCreationInfo(TokenCreationInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"
