from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ...www.w3.org.pkg_2005.pkg_08.addressing.ws_addr import (
    EndpointReferenceType,
)

__NAMESPACE__ = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AcknowledgementType:
    message: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class AssigningAuthorityType:
    assigning_authority_id: str | None = field(
        default=None,
        metadata={
            "name": "assigningAuthorityId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class ConnectcustomHttpHeadersType:
    class Meta:
        name = "CONNECTCustomHttpHeadersType"

    header_name: str | None = field(
        default=None,
        metadata={
            "name": "headerName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    header_value: str | None = field(
        default=None,
        metadata={
            "name": "headerValue",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class CeType:
    code: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    code_system: str | None = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    code_system_name: str | None = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    code_system_version: str | None = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    display_name: str | None = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    original_text: str | None = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    translation: list[CeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class CreateEprrequestType:
    class Meta:
        name = "CreateEPRRequestType"

    endpoint_url: str | None = field(
        default=None,
        metadata={
            "name": "endpointURL",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    namespace_uri: str | None = field(
        default=None,
        metadata={
            "name": "namespaceURI",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    namespace_prefix: str | None = field(
        default=None,
        metadata={
            "name": "namespacePrefix",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    service_name: str | None = field(
        default=None,
        metadata={
            "name": "serviceName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    port_name: str | None = field(
        default=None,
        metadata={
            "name": "portName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class HomeCommunityType:
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    home_community_id: str | None = field(
        default=None,
        metadata={
            "name": "homeCommunityId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class QualifiedSubjectIdentifierType:
    subject_identifier: str | None = field(
        default=None,
        metadata={
            "name": "SubjectIdentifier",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    assigning_authority_identifier: str | None = field(
        default=None,
        metadata={
            "name": "AssigningAuthorityIdentifier",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class ResponseType:
    status: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    message: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class SamlAuthnStatementType:
    auth_instant: str | None = field(
        default=None,
        metadata={
            "name": "authInstant",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    session_index: str | None = field(
        default=None,
        metadata={
            "name": "sessionIndex",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    auth_context_class_ref: str | None = field(
        default=None,
        metadata={
            "name": "authContextClassRef",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    subject_locality_address: str | None = field(
        default=None,
        metadata={
            "name": "subjectLocalityAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    subject_locality_dnsname: str | None = field(
        default=None,
        metadata={
            "name": "subjectLocalityDNSName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class SamlAuthzDecisionStatementEvidenceConditionsType:
    not_before: str | None = field(
        default=None,
        metadata={
            "name": "notBefore",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    not_on_or_after: str | None = field(
        default=None,
        metadata={
            "name": "notOnOrAfter",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class SamlConditionsType:
    not_before: str | None = field(
        default=None,
        metadata={
            "name": "notBefore",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    not_on_or_after: str | None = field(
        default=None,
        metadata={
            "name": "notOnOrAfter",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class SamlIssuerType:
    issuer: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    issuer_format: str | None = field(
        default=None,
        metadata={
            "name": "issuerFormat",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class SamlSignatureKeyInfoType:
    rsa_key_value_modulus: bytes | None = field(
        default=None,
        metadata={
            "name": "rsaKeyValueModulus",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "format": "base64",
        },
    )
    rsa_key_value_exponent: bytes | None = field(
        default=None,
        metadata={
            "name": "rsaKeyValueExponent",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "format": "base64",
        },
    )


@dataclass
class TokenRetrieveInfoType:
    request: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class UrlInfoType:
    url: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class UrlSetType:
    url: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class Acknowledgement(AcknowledgementType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AddressType:
    address_type: CeType | None = field(
        default=None,
        metadata={
            "name": "addressType",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    city: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    country: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    state: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    street_address: str | None = field(
        default=None,
        metadata={
            "name": "streetAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    zip_code: str | None = field(
        default=None,
        metadata={
            "name": "zipCode",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class AssigningAuthoritiesType:
    assigning_authority: list[AssigningAuthorityType] = field(
        default_factory=list,
        metadata={
            "name": "assigningAuthority",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
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
    home_community: list[HomeCommunityType] = field(
        default_factory=list,
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class HomeCommunity(HomeCommunityType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class NhinTargetCommunityType:
    home_community: HomeCommunityType | None = field(
        default=None,
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    list_value: str | None = field(
        default=None,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    region: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class NhinTargetSystemType:
    epr: EndpointReferenceType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    home_community: HomeCommunityType | None = field(
        default=None,
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    url: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    exchange_name: str | None = field(
        default=None,
        metadata={
            "name": "exchangeName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    use_spec_version: str | None = field(
        default=None,
        metadata={
            "name": "useSpecVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class PersonNameType:
    family_name: str | None = field(
        default=None,
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    given_name: str | None = field(
        default=None,
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    name_type: CeType | None = field(
        default=None,
        metadata={
            "name": "nameType",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    second_name_or_initials: str | None = field(
        default=None,
        metadata={
            "name": "secondNameOrInitials",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    full_name: str | None = field(
        default=None,
        metadata={
            "name": "fullName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    prefix: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    suffix: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class PhoneType:
    area_code: str | None = field(
        default=None,
        metadata={
            "name": "areaCode",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    country_code: str | None = field(
        default=None,
        metadata={
            "name": "countryCode",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    extension: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    local_number: str | None = field(
        default=None,
        metadata={
            "name": "localNumber",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    phone_number_type: CeType | None = field(
        default=None,
        metadata={
            "name": "phoneNumberType",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class QualifiedSubjectIdentifier(QualifiedSubjectIdentifierType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class QualifiedSubjectIdentifiersType:
    qualified_subject_identifier: list[QualifiedSubjectIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "QualifiedSubjectIdentifier",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
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
    id: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    issue_instant: str | None = field(
        default=None,
        metadata={
            "name": "issueInstant",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    issuer: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    issuer_format: str | None = field(
        default=None,
        metadata={
            "name": "issuerFormat",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    subject: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    conditions: SamlAuthzDecisionStatementEvidenceConditionsType | None = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            },
        )
    )
    access_consent_policy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "accessConsentPolicy",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    instance_access_consent_policy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "instanceAccessConsentPolicy",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class SamlAuthzDecisionStatementEvidenceConditions(
    SamlAuthzDecisionStatementEvidenceConditionsType
):
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
    key_info: SamlSignatureKeyInfoType | None = field(
        default=None,
        metadata={
            "name": "keyInfo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    signature_value: bytes | None = field(
        default=None,
        metadata={
            "name": "signatureValue",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "format": "base64",
        },
    )


@dataclass
class SamlSubjectConfirmationType:
    method: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    subject_condition: SamlConditionsType | None = field(
        default=None,
        metadata={
            "name": "subjectCondition",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    recipient: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    in_response_to: str | None = field(
        default=None,
        metadata={
            "name": "inResponseTo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    address: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
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
    address: list[AddressType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "min_occurs": 1,
        },
    )


@dataclass
class HomeCommunities(HomeCommunitiesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class NhinTargetCommunitiesType:
    nhin_target_community: list[NhinTargetCommunityType] = field(
        default_factory=list,
        metadata={
            "name": "nhinTargetCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "min_occurs": 1,
        },
    )
    use_spec_version: str | None = field(
        default=None,
        metadata={
            "name": "useSpecVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    exchange_name: str | None = field(
        default=None,
        metadata={
            "name": "exchangeName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
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
class SamlAuthzDecisionStatementEvidenceAssertion(
    SamlAuthzDecisionStatementEvidenceAssertionType
):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementEvidenceType:
    assertion: SamlAuthzDecisionStatementEvidenceAssertionType | None = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            },
        )
    )


@dataclass
class SamlSignature(SamlSignatureType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class UserType:
    person_name: PersonNameType | None = field(
        default=None,
        metadata={
            "name": "personName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    user_name: str | None = field(
        default=None,
        metadata={
            "name": "userName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    org: HomeCommunityType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    role_coded: CeType | None = field(
        default=None,
        metadata={
            "name": "roleCoded",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
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
    user_info: UserType | None = field(
        default=None,
        metadata={
            "name": "userInfo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    config_instance: str | None = field(
        default=None,
        metadata={
            "name": "configInstance",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    auth_method: str | None = field(
        default=None,
        metadata={
            "name": "authMethod",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class NhinTargetCommunities(NhinTargetCommunitiesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementEvidence(
    SamlAuthzDecisionStatementEvidenceType
):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class SamlAuthzDecisionStatementType:
    decision: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    resource: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    action: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    evidence: SamlAuthzDecisionStatementEvidenceType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass
class User(UserType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass
class AssertionType:
    address: AddressType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    date_of_birth: str | None = field(
        default=None,
        metadata={
            "name": "dateOfBirth",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    explanation_non_claimant_signature: str | None = field(
        default=None,
        metadata={
            "name": "explanationNonClaimantSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    have_second_witness_signature: bool | None = field(
        default=None,
        metadata={
            "name": "haveSecondWitnessSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    have_signature: bool | None = field(
        default=None,
        metadata={
            "name": "haveSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    have_witness_signature: bool | None = field(
        default=None,
        metadata={
            "name": "haveWitnessSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    home_community: HomeCommunityType | None = field(
        default=None,
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    national_provider_id: str | None = field(
        default=None,
        metadata={
            "name": "nationalProviderId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    person_name: PersonNameType | None = field(
        default=None,
        metadata={
            "name": "personName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    phone_number: PhoneType | None = field(
        default=None,
        metadata={
            "name": "phoneNumber",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    second_witness_address: AddressType | None = field(
        default=None,
        metadata={
            "name": "secondWitnessAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    second_witness_name: PersonNameType | None = field(
        default=None,
        metadata={
            "name": "secondWitnessName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    second_witness_phone: PhoneType | None = field(
        default=None,
        metadata={
            "name": "secondWitnessPhone",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    ssn: str | None = field(
        default=None,
        metadata={
            "name": "SSN",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    unique_patient_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "uniquePatientId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    witness_address: AddressType | None = field(
        default=None,
        metadata={
            "name": "witnessAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    witness_name: PersonNameType | None = field(
        default=None,
        metadata={
            "name": "witnessName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    witness_phone: PhoneType | None = field(
        default=None,
        metadata={
            "name": "witnessPhone",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    user_info: UserType | None = field(
        default=None,
        metadata={
            "name": "userInfo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    authorized: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    purpose_of_disclosure_coded: CeType | None = field(
        default=None,
        metadata={
            "name": "purposeOfDisclosureCoded",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    acp_attribute: str | None = field(
        default=None,
        metadata={
            "name": "acpAttribute",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    instance_acp_attribute: str | None = field(
        default=None,
        metadata={
            "name": "instanceAcpAttribute",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    saml_conditions: SamlConditionsType | None = field(
        default=None,
        metadata={
            "name": "samlConditions",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    saml_authn_statement: SamlAuthnStatementType | None = field(
        default=None,
        metadata={
            "name": "samlAuthnStatement",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    saml_authz_decision_statement: SamlAuthzDecisionStatementType | None = (
        field(
            default=None,
            metadata={
                "name": "samlAuthzDecisionStatement",
                "type": "Element",
                "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            },
        )
    )
    saml_signature: SamlSignatureType | None = field(
        default=None,
        metadata={
            "name": "samlSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    saml_issuer: SamlIssuerType | None = field(
        default=None,
        metadata={
            "name": "samlIssuer",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    saml_subject_confirmations: list[SamlSubjectConfirmationType] = field(
        default_factory=list,
        metadata={
            "name": "samlSubjectConfirmations",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    message_id: str | None = field(
        default=None,
        metadata={
            "name": "messageId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    relates_to_list: list[str] = field(
        default_factory=list,
        metadata={
            "name": "relatesToList",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    implements_spec_version: str | None = field(
        default=None,
        metadata={
            "name": "implementsSpecVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    transaction_timeout: int | None = field(
        default=None,
        metadata={
            "name": "transactionTimeout",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    keep_alive: str | None = field(
        default=None,
        metadata={
            "name": "keepAlive",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    connectcustom_http_headers: list[ConnectcustomHttpHeadersType] = field(
        default_factory=list,
        metadata={
            "name": "CONNECTCustomHttpHeaders",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    signature_algorithm: str | None = field(
        default=None,
        metadata={
            "name": "signatureAlgorithm",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    digest_algorithm: str | None = field(
        default=None,
        metadata={
            "name": "digestAlgorithm",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
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
    assertion: AssertionType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    action_name: str | None = field(
        default=None,
        metadata={
            "name": "actionName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )
    resource_name: str | None = field(
        default=None,
        metadata={
            "name": "resourceName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "required": True,
        },
    )


@dataclass
class TokenCreationInfo(TokenCreationInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"
