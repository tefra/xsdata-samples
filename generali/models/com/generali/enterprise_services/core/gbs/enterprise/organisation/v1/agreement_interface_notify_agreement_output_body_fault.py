from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


@dataclass
class AgreementInterfaceNotifyAgreementOutputBodyFault:
    class Meta:
        global_type = False

    faultcode: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    faultstring: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    faultactor: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    detail: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
