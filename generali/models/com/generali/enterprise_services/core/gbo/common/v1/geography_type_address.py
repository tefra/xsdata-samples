from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.address_type import (
    AddressType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geo_coded_address_type import (
    GeoCodedAddressType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class GeographyTypeAddress:
    class Meta:
        global_type = False

    address: AddressType | None = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_address: GeoCodedAddressType | None = field(
        default=None,
        metadata={
            "name": "GeocodedAddress",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
