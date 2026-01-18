from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/wsrf/bf-2"


@dataclass
class BaseFaultTypeFaultCause:
    class Meta:
        global_type = False

    other_element: object | None = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
