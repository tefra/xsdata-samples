from __future__ import annotations

from dataclasses import dataclass, field

from ubl.models.common.ubl_xad_esv132_2_1 import (
    CertificateValues,
    RevocationValues,
    XadEstimeStampType,
)

__NAMESPACE__ = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(frozen=True, kw_only=True)
class ArchiveTimeStampV2(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(frozen=True, kw_only=True)
class ValidationDataType:
    certificate_values: None | CertificateValues = field(
        default=None,
        metadata={
            "name": "CertificateValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    revocation_values: None | RevocationValues = field(
        default=None,
        metadata={
            "name": "RevocationValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    ur: None | str = field(
        default=None,
        metadata={
            "name": "UR",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, kw_only=True)
class TimeStampValidationData(ValidationDataType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"
