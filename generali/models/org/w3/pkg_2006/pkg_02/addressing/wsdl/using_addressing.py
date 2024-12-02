from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/2006/02/addressing/wsdl"


@dataclass
class UsingAddressing:
    class Meta:
        namespace = "http://www.w3.org/2006/02/addressing/wsdl"

    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
