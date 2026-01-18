from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/technical/v1"


@dataclass
class PayloadType:
    any_element: object | None = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
