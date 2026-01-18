from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/core-types/v1"
)


@dataclass(kw_only=True)
class TimeType:
    """
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Time.

    Type</ns1:DictionaryEntryName> <ns1:Version
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">2.00</ns1:Version>
    <ns1:Definition
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">A
    time.</ns1:Definition> <ns1:PrimitiveType
    xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Time</ns1:PrimitiveType>.
    """

    value: XmlTime = field(
        metadata={
            "required": True,
        }
    )
