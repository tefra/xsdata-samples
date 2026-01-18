from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.country_gbotype import (
    CountryGbotype,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class AddressType:
    address_line1: str | None = field(
        default=None,
        metadata={
            "name": "AddressLine1",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        },
    )
    address_line2: str | None = field(
        default=None,
        metadata={
            "name": "AddressLine2",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    state: str | None = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    city: str | None = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    zip_code: str | None = field(
        default=None,
        metadata={
            "name": "ZipCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    country: CountryGbotype | None = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        },
    )
