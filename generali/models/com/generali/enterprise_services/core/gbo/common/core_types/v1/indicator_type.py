from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/core-types/v1"
)


@dataclass
class IndicatorType:
    """
    <ns1:UniqueID
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">UDT0000012</ns1:UniqueID>
    <ns1:Acronym
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">UDT</ns1:Acronym>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Indicator.

    Type</ns1:DictionaryEntryName> <ns1:Version
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">2.01</ns1:Version>
    <ns1:Definition
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">A
    list of two mutually exclusive Boolean values that express the only
    possible states of a Property.</ns1:Definition> <ns1:PrimitiveType
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">boolean</ns1:PrimitiveType>.
    """

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
