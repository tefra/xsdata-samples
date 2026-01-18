from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class ProgramReqAppDataType:
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
