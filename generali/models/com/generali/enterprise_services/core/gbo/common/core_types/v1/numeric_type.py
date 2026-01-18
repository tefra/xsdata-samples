from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/core-types/v1"
)


@dataclass(kw_only=True)
class NumericType:
    """
    <ns1:UniqueID
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">UNDT000008</ns1:UniqueID>
    <ns1:Acronym
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">CCT</ns1:Acronym>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Numeric.

    Type</ns1:DictionaryEntryName> <ns1:Version
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">2.01</ns1:Version>
    <ns1:Definition
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Numeric
    information that is assigned or is determined by calculation, counting,
    or sequencing. It does not require a unit of quantity or unit of
    measure. </ns1:Definition> <ns1:PrimaryRepresentationTerm
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Numeric</ns1:PrimaryRepresentationTerm>
    <ns1:PrimitiveType
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">decimal</ns1:PrimitiveType>.
    """

    value: Decimal = field(
        metadata={
            "required": True,
        }
    )
