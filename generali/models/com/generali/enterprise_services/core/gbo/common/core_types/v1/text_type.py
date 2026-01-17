from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/core-types/v1"
)


@dataclass
class TextType:
    """
    <ns1:UniqueID
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">UNDT000010</ns1:UniqueID>
    <ns1:Acronym
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">CCT</ns1:Acronym>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Text.

    Type</ns1:DictionaryEntryName> <ns1:Version
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">2.01</ns1:Version>
    <ns1:Definition
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">A
    character string (i.e. a finite set of characters) generally in the
    form of words of a language.</ns1:Definition>
    <ns1:PrimaryRepresentationTerm
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Text</ns1:PrimaryRepresentationTerm>
    <ns1:PrimitiveType
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>.

    :ivar value:
    :ivar language_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Language.
        Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        identifier of the language used in the content
        component.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar language_locale_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Language
        Locale. Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        identification of the locale of the language.</ns1:Definition>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    """

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
