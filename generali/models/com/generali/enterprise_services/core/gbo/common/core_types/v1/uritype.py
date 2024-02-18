from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/core-types/v1"
)


@dataclass
class Uritype:
    """<ns1:DictionaryEntryName xmlns:ns1="urn:un:unece:uncefact:documentation:stan
    dard:CoreComponentsTechnicalSpecification:2">URI.

    Type</ns1:DictionaryEntryName>
    <ns1:Version xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">2.00</ns1:Version>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">A particular URI conforming to RFC3689.</ns1:Definition>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">URI</ns1:PrimitiveType>
    """

    class Meta:
        name = "URIType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
