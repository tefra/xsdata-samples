from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.headers.v1.base_header_type import (
    BaseHeaderType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
)


@dataclass
class BaseSystemTraceabilityType(BaseHeaderType):
    """
    <description xmlns="">The base type for the source and destination
    system information in the header.</description>.

    :ivar country_code: <description xmlns="">The ISO3166-2 country
        code.</description>
    :ivar country_name: <description xmlns="">The name of the country in
        which the system resides.</description>
    :ivar language_code: <description xmlns="">The ISO639-1 language
        code.</description>
    :ivar operator_name: <description xmlns="">The organisation that
        operates the system.</description>
    :ivar system_id: <description xmlns="">The logical identifier of the
        system.</description>
    :ivar system_name: <description xmlns="">The logical name of the
        system.</description>
    """

    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
            "pattern": r"[A-Z][A-Z]",
        },
    )
    country_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
        },
    )
    language_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
        },
    )
    operator_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
        },
    )
    system_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
        },
    )
    system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
        },
    )
