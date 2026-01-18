from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.address_type import (
    AddressType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.country_gbotype import (
    CountryGbotype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.cresta_zone_type import (
    CrestaZoneType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geocoded_accuracy_enum import (
    GeocodedAccuracyEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geographic_location_type import (
    GeographicLocationType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class GeoCodedAddressType(AddressType):
    geocoded_addres_line1: str | None = field(
        default=None,
        metadata={
            "name": "GeocodedAddresLine1",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_addres_line2: str | None = field(
        default=None,
        metadata={
            "name": "GeocodedAddresLine2",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_state: str | None = field(
        default=None,
        metadata={
            "name": "GeocodedState",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_town: str | None = field(
        default=None,
        metadata={
            "name": "GeocodedTown",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_zip_code: str | None = field(
        default=None,
        metadata={
            "name": "GeocodedZipCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_country: CountryGbotype | None = field(
        default=None,
        metadata={
            "name": "GeocodedCountry",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_accuracy: GeocodedAccuracyEnum | None = field(
        default=None,
        metadata={
            "name": "GeocodedAccuracy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    global_position_address: GeographicLocationType | None = field(
        default=None,
        metadata={
            "name": "GlobalPositionAddress",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    cresta_zone: CrestaZoneType | None = field(
        default=None,
        metadata={
            "name": "CrestaZone",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    accuracy_level: str | None = field(
        default=None,
        metadata={
            "name": "AccuracyLevel",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
