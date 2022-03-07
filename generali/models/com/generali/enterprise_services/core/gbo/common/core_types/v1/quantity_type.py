from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/core-types/v1"


@dataclass
class QuantityType:
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:standard:Co
    reComponentsTechnicalSpecification:2">UNDT000009</ns1:UniqueID>

    <ns1:Acronym xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">CCT</ns1:Acronym>
    <ns1:DictionaryEntryName xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Quantity. Type</ns1:DictionaryEntryName>
    <ns1:Version xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">2.01</ns1:Version>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">A counted number of non-monetary units possibly including fractions.</ns1:Definition>
    <ns1:PrimaryRepresentationTerm xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Quantity</ns1:PrimaryRepresentationTerm>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">decimal</ns1:PrimitiveType>

    :ivar value:
    :ivar unit_code: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Quantity.
        Unit. Code</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        unit of the quantity</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar unit_code_list_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Quantity
        Unit. Code List. Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        quantity unit code list.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar unit_code_list_agency_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Quantity
        Unit. Code List Agency. Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        identification of the agency that maintains the quantity unit
        code list</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar unit_code_list_agency_name: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Quantity
        Unit. Code List Agency. Name</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        name of the agency which maintains the quantity unit code
        list.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    """
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        }
    )
    unit_code_list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListID",
            "type": "Attribute",
        }
    )
    unit_code_list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListAgencyID",
            "type": "Attribute",
        }
    )
    unit_code_list_agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListAgencyName",
            "type": "Attribute",
        }
    )
