from __future__ import annotations

from dataclasses import dataclass, field

from ...www.w3.org.pkg_2005.pkg_08.addressing.ws_addr import (
    EndpointReferenceType,
)

__NAMESPACE__ = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class AcknowledgementType:
    message: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class AssigningAuthorityType:
    assigning_authority_id: str = field(
        metadata={
            "name": "assigningAuthorityId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class ConnectcustomHttpHeadersType:
    class Meta:
        name = "CONNECTCustomHttpHeadersType"

    header_name: str = field(
        metadata={
            "name": "headerName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    header_value: str = field(
        metadata={
            "name": "headerValue",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class CeType:
    code: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    code_system: None | str = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    code_system_name: None | str = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    code_system_version: str = field(
        metadata={
            "name": "codeSystemVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    display_name: str = field(
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    original_text: str = field(
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    translation: list[CeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class CreateEprrequestType:
    class Meta:
        name = "CreateEPRRequestType"

    endpoint_url: str = field(
        metadata={
            "name": "endpointURL",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    namespace_uri: str = field(
        metadata={
            "name": "namespaceURI",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    namespace_prefix: str = field(
        metadata={
            "name": "namespacePrefix",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    service_name: str = field(
        metadata={
            "name": "serviceName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    port_name: str = field(
        metadata={
            "name": "portName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class HomeCommunityType:
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    home_community_id: str = field(
        metadata={
            "name": "homeCommunityId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class QualifiedSubjectIdentifierType:
    subject_identifier: str = field(
        metadata={
            "name": "SubjectIdentifier",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    assigning_authority_identifier: str = field(
        metadata={
            "name": "AssigningAuthorityIdentifier",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class ResponseType:
    status: bool = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    message: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class SamlAuthnStatementType:
    auth_instant: str = field(
        metadata={
            "name": "authInstant",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    session_index: None | str = field(
        default=None,
        metadata={
            "name": "sessionIndex",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    auth_context_class_ref: str = field(
        metadata={
            "name": "authContextClassRef",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    subject_locality_address: None | str = field(
        default=None,
        metadata={
            "name": "subjectLocalityAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    subject_locality_dnsname: None | str = field(
        default=None,
        metadata={
            "name": "subjectLocalityDNSName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class SamlAuthzDecisionStatementEvidenceConditionsType:
    not_before: None | str = field(
        default=None,
        metadata={
            "name": "notBefore",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    not_on_or_after: None | str = field(
        default=None,
        metadata={
            "name": "notOnOrAfter",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class SamlConditionsType:
    not_before: str = field(
        metadata={
            "name": "notBefore",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    not_on_or_after: str = field(
        metadata={
            "name": "notOnOrAfter",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class SamlIssuerType:
    issuer: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    issuer_format: None | str = field(
        default=None,
        metadata={
            "name": "issuerFormat",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class SamlSignatureKeyInfoType:
    rsa_key_value_modulus: None | bytes = field(
        default=None,
        metadata={
            "name": "rsaKeyValueModulus",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "format": "base64",
        },
    )
    rsa_key_value_exponent: None | bytes = field(
        default=None,
        metadata={
            "name": "rsaKeyValueExponent",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "format": "base64",
        },
    )


@dataclass(kw_only=True)
class TokenRetrieveInfoType:
    request: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class UrlInfoType:
    url: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class UrlSetType:
    url: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class Acknowledgement(AcknowledgementType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class AddressType:
    address_type: CeType = field(
        metadata={
            "name": "addressType",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    city: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    country: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    state: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    street_address: str = field(
        metadata={
            "name": "streetAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    zip_code: str = field(
        metadata={
            "name": "zipCode",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class AssigningAuthoritiesType:
    assigning_authority: list[AssigningAuthorityType] = field(
        default_factory=list,
        metadata={
            "name": "assigningAuthority",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class AssigningAuthority(AssigningAuthorityType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class ConnectcustomHttpHeaders(ConnectcustomHttpHeadersType):
    class Meta:
        name = "CONNECTCustomHttpHeaders"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class Ce(CeType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class CreateEprrequest(CreateEprrequestType):
    class Meta:
        name = "CreateEPRRequest"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class Epr(EndpointReferenceType):
    class Meta:
        name = "EPR"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class HomeCommunitiesType:
    home_community: list[HomeCommunityType] = field(
        default_factory=list,
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class HomeCommunity(HomeCommunityType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class NhinTargetCommunityType:
    home_community: HomeCommunityType = field(
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    list_value: None | str = field(
        default=None,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    region: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class NhinTargetSystemType:
    epr: None | EndpointReferenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    home_community: None | HomeCommunityType = field(
        default=None,
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    url: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    exchange_name: None | str = field(
        default=None,
        metadata={
            "name": "exchangeName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    use_spec_version: None | str = field(
        default=None,
        metadata={
            "name": "useSpecVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class PersonNameType:
    family_name: str = field(
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    given_name: str = field(
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    name_type: CeType = field(
        metadata={
            "name": "nameType",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    second_name_or_initials: str = field(
        metadata={
            "name": "secondNameOrInitials",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    full_name: str = field(
        metadata={
            "name": "fullName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    prefix: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    suffix: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class PhoneType:
    area_code: str = field(
        metadata={
            "name": "areaCode",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    country_code: str = field(
        metadata={
            "name": "countryCode",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    extension: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    local_number: str = field(
        metadata={
            "name": "localNumber",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    phone_number_type: CeType = field(
        metadata={
            "name": "phoneNumberType",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class QualifiedSubjectIdentifier(QualifiedSubjectIdentifierType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class QualifiedSubjectIdentifiersType:
    qualified_subject_identifier: list[QualifiedSubjectIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "QualifiedSubjectIdentifier",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class Response(ResponseType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlAuthnStatement(SamlAuthnStatementType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlAuthzDecisionStatementEvidenceAssertionType:
    id: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    issue_instant: None | str = field(
        default=None,
        metadata={
            "name": "issueInstant",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    version: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    issuer: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    issuer_format: None | str = field(
        default=None,
        metadata={
            "name": "issuerFormat",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    subject: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    conditions: None | SamlAuthzDecisionStatementEvidenceConditionsType = (
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


@dataclass(kw_only=True)
class SamlAuthzDecisionStatementEvidenceConditions(
    SamlAuthzDecisionStatementEvidenceConditionsType
):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlConditions(SamlConditionsType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlIssuer(SamlIssuerType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlSignatureKeyInfo(SamlSignatureKeyInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlSignatureType:
    key_info: None | SamlSignatureKeyInfoType = field(
        default=None,
        metadata={
            "name": "keyInfo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    signature_value: None | bytes = field(
        default=None,
        metadata={
            "name": "signatureValue",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "format": "base64",
        },
    )


@dataclass(kw_only=True)
class SamlSubjectConfirmationType:
    method: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    subject_condition: None | SamlConditionsType = field(
        default=None,
        metadata={
            "name": "subjectCondition",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    recipient: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    in_response_to: None | str = field(
        default=None,
        metadata={
            "name": "inResponseTo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    address: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class TokenRetrieveInfo(TokenRetrieveInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class UrlInfo(UrlInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class UrlSet(UrlSetType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class Address(AddressType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class AddressesType:
    address: list[AddressType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class HomeCommunities(HomeCommunitiesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
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
    use_spec_version: None | str = field(
        default=None,
        metadata={
            "name": "useSpecVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    exchange_name: None | str = field(
        default=None,
        metadata={
            "name": "exchangeName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class NhinTargetCommunity(NhinTargetCommunityType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class NhinTargetSystem(NhinTargetSystemType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class PersonName(PersonNameType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class Phone(PhoneType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class QualifiedSubjectIdentifiers(QualifiedSubjectIdentifiersType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlAuthzDecisionStatementEvidenceAssertion(
    SamlAuthzDecisionStatementEvidenceAssertionType
):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlAuthzDecisionStatementEvidenceType:
    assertion: None | SamlAuthzDecisionStatementEvidenceAssertionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class SamlSignature(SamlSignatureType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class UserType:
    person_name: PersonNameType = field(
        metadata={
            "name": "personName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    user_name: str = field(
        metadata={
            "name": "userName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    org: HomeCommunityType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    role_coded: CeType = field(
        metadata={
            "name": "roleCoded",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class AssigningAuthorites(AssigningAuthoritiesType):
    class Meta:
        name = "assigningAuthorites"
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class Addresses(AddressesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class ConfigAssertionType:
    user_info: UserType = field(
        metadata={
            "name": "userInfo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    config_instance: str = field(
        metadata={
            "name": "configInstance",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    auth_method: str = field(
        metadata={
            "name": "authMethod",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class NhinTargetCommunities(NhinTargetCommunitiesType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlAuthzDecisionStatementEvidence(
    SamlAuthzDecisionStatementEvidenceType
):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlAuthzDecisionStatementType:
    decision: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    resource: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    action: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    evidence: None | SamlAuthzDecisionStatementEvidenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class User(UserType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class AssertionType:
    address: None | AddressType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    date_of_birth: None | str = field(
        default=None,
        metadata={
            "name": "dateOfBirth",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    explanation_non_claimant_signature: None | str = field(
        default=None,
        metadata={
            "name": "explanationNonClaimantSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    have_second_witness_signature: None | bool = field(
        default=None,
        metadata={
            "name": "haveSecondWitnessSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    have_signature: None | bool = field(
        default=None,
        metadata={
            "name": "haveSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    have_witness_signature: None | bool = field(
        default=None,
        metadata={
            "name": "haveWitnessSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    home_community: HomeCommunityType = field(
        metadata={
            "name": "homeCommunity",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    national_provider_id: None | str = field(
        default=None,
        metadata={
            "name": "nationalProviderId",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    person_name: None | PersonNameType = field(
        default=None,
        metadata={
            "name": "personName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    phone_number: None | PhoneType = field(
        default=None,
        metadata={
            "name": "phoneNumber",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    second_witness_address: None | AddressType = field(
        default=None,
        metadata={
            "name": "secondWitnessAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    second_witness_name: None | PersonNameType = field(
        default=None,
        metadata={
            "name": "secondWitnessName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    second_witness_phone: None | PhoneType = field(
        default=None,
        metadata={
            "name": "secondWitnessPhone",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    ssn: None | str = field(
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
    witness_address: None | AddressType = field(
        default=None,
        metadata={
            "name": "witnessAddress",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    witness_name: None | PersonNameType = field(
        default=None,
        metadata={
            "name": "witnessName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    witness_phone: None | PhoneType = field(
        default=None,
        metadata={
            "name": "witnessPhone",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    user_info: UserType = field(
        metadata={
            "name": "userInfo",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    authorized: bool = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    purpose_of_disclosure_coded: CeType = field(
        metadata={
            "name": "purposeOfDisclosureCoded",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    acp_attribute: None | str = field(
        default=None,
        metadata={
            "name": "acpAttribute",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    instance_acp_attribute: None | str = field(
        default=None,
        metadata={
            "name": "instanceAcpAttribute",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    saml_conditions: None | SamlConditionsType = field(
        default=None,
        metadata={
            "name": "samlConditions",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    saml_authn_statement: None | SamlAuthnStatementType = field(
        default=None,
        metadata={
            "name": "samlAuthnStatement",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    saml_authz_decision_statement: None | SamlAuthzDecisionStatementType = (
        field(
            default=None,
            metadata={
                "name": "samlAuthzDecisionStatement",
                "type": "Element",
                "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
            },
        )
    )
    saml_signature: None | SamlSignatureType = field(
        default=None,
        metadata={
            "name": "samlSignature",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    saml_issuer: None | SamlIssuerType = field(
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
    message_id: None | str = field(
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
    implements_spec_version: None | str = field(
        default=None,
        metadata={
            "name": "implementsSpecVersion",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    transaction_timeout: None | int = field(
        default=None,
        metadata={
            "name": "transactionTimeout",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    keep_alive: None | str = field(
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
    signature_algorithm: None | str = field(
        default=None,
        metadata={
            "name": "signatureAlgorithm",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )
    digest_algorithm: None | str = field(
        default=None,
        metadata={
            "name": "digestAlgorithm",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        },
    )


@dataclass(kw_only=True)
class ConfigAssertion(ConfigAssertionType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class SamlAuthzDecisionStatement(SamlAuthzDecisionStatementType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class Assertion(AssertionType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"


@dataclass(kw_only=True)
class TokenCreationInfoType:
    assertion: AssertionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    action_name: str = field(
        metadata={
            "name": "actionName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )
    resource_name: str = field(
        metadata={
            "name": "resourceName",
            "type": "Element",
            "namespace": "urn:gov:hhs:fha:nhinc:common:nhinccommon",
        }
    )


@dataclass(kw_only=True)
class TokenCreationInfo(TokenCreationInfoType):
    class Meta:
        namespace = "urn:gov:hhs:fha:nhinc:common:nhinccommon"
