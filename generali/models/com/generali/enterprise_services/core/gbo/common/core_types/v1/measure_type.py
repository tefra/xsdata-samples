from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/core-types/v1"


@dataclass
class MeasureType:
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreCo
    mponentsTechnicalSpecification:2">UNDT000007</ns1:UniqueID>

    <ns1:Acronym xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">CCT</ns1:Acronym>
    <ns1:DictionaryEntryName xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Measure. Type</ns1:DictionaryEntryName>
    <ns1:Version xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">2.01</ns1:Version>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">A numeric value determined by measuring an object along with the specified unit of measure.</ns1:Definition>
    <ns1:PrimaryRepresentationTerm xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Measure</ns1:PrimaryRepresentationTerm>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">decimal</ns1:PrimitiveType>

    :ivar value:
    :ivar unit_code: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Measure.
        Unit. Code</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        type of unit of measure.</ns1:Definition> <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    :ivar unit_code_list_version_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Measure
        Unit. Code List Version. Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        version of the measure unit code list.</ns1:Definition>
        <ns1:PrimitiveType
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
    unit_code_list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListVersionID",
            "type": "Attribute",
        }
    )
