from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/core-types/v1"
)


@dataclass
class NumberType:
    """
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Number.

    Type</ns1:DictionaryEntryName> <ns1:Version
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">2.00</ns1:Version>
    <ns1:Definition
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">A
    particular whole number.</ns1:Definition> <ns1:PrimitiveType
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Integer</ns1:PrimitiveType>.
    """

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
