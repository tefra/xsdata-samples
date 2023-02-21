from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/core-types/v1"


@dataclass
class AmountType:
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreCo
    mponentsTechnicalSpecification:2">UNDT000001</ns1:UniqueID>

    <ns1:Acronym xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">CCT</ns1:Acronym>
    <ns1:DictionaryEntryName xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Amount. Type</ns1:DictionaryEntryName>
    <ns1:Version xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">2.01</ns1:Version>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">A number of monetary units specified in a currency where the unit of the currency is explicit or implied.</ns1:Definition>
    <ns1:PrimaryRepresentationTerm xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Amount</ns1:PrimaryRepresentationTerm>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">decimal</ns1:PrimitiveType>

    :ivar value:
    :ivar currency_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Amount.
        Currency. Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        currency of the amount.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar currency_code_list_version_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Amount
        Currency. Code List Version. Identifier</ns1:Name>
        <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        VersionID of the UN/ECE Rec9 code list.</ns1:Definition>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar unit_code: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Amount.
        Unit Code</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        unit of the amount.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    """
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    currency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyID",
            "type": "Attribute",
        }
    )
    currency_code_list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyCodeListVersionID",
            "type": "Attribute",
        }
    )
    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        }
    )
