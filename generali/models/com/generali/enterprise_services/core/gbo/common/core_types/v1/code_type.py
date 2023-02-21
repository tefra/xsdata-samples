from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/core-types/v1"


@dataclass
class CodeType:
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreCo
    mponentsTechnicalSpecification:2">UNDT000003</ns1:UniqueID>

    <ns1:Acronym xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">CCT</ns1:Acronym>
    <ns1:DictionaryEntryName xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Code. Type</ns1:DictionaryEntryName>
    <ns1:Version xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">2.01</ns1:Version>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">A character string (letters, figures, or symbols) that for brevity and/or languange independence may be used to represent or replace a definitive value or text of an attribute together with relevant supplementary information.
    </ns1:Definition>
    <ns1:PrimaryRepresentationTerm xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Code</ns1:PrimaryRepresentationTerm>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    <ns1:UsageRule xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Should not be used if the character string identifies an instance of an object class or an object in the real world, in which case the Identifier. Type should be used.
    </ns1:UsageRule>

    :ivar value:
    :ivar list_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Code
        List. Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        identification of a list of codes.</ns1:Definition>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar list_agency_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Code
        List. Agency. Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">An
        agency that maintains one or more lists of
        codes.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar list_agency_name: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Code
        List. Agency Name. Text</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        name of the agency that maintains the list of
        codes.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar list_name: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Code
        List. Name. Text</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        name of a list of codes.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar list_version_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Code
        List. Version. Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        version of the list of codes.</ns1:Definition>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar name: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Code.
        Name. Text</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        textual equivalent of the code content
        component.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar language_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Language.
        Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        identifier of the language used in the code
        name.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar list_uri: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Code
        List. Uniform Resource. Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        Uniform Resource Identifier that identifies where the code list
        is located.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar list_scheme_uri: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Code
        List Scheme. Uniform Resource. Identifier</ns1:Name>
        <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        Uniform Resource Identifier that identifies where the code list
        scheme is located.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        }
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        }
    )
    list_agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyName",
            "type": "Attribute",
        }
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        }
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    language_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "languageID",
            "type": "Attribute",
        }
    )
    list_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "listURI",
            "type": "Attribute",
        }
    )
    list_scheme_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "listSchemeURI",
            "type": "Attribute",
        }
    )
