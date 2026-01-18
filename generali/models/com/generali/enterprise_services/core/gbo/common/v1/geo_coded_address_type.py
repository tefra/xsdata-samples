from __future__ import annotations

from dataclasses import dataclass, field

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
    geocoded_addres_line1: None | str = field(
        default=None,
        metadata={
            "name": "GeocodedAddresLine1",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_addres_line2: None | str = field(
        default=None,
        metadata={
            "name": "GeocodedAddresLine2",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_state: None | str = field(
        default=None,
        metadata={
            "name": "GeocodedState",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_town: None | str = field(
        default=None,
        metadata={
            "name": "GeocodedTown",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_zip_code: None | str = field(
        default=None,
        metadata={
            "name": "GeocodedZipCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_country: None | CountryGbotype = field(
        default=None,
        metadata={
            "name": "GeocodedCountry",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    geocoded_accuracy: None | GeocodedAccuracyEnum = field(
        default=None,
        metadata={
            "name": "GeocodedAccuracy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    global_position_address: None | GeographicLocationType = field(
        default=None,
        metadata={
            "name": "GlobalPositionAddress",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    cresta_zone: None | CrestaZoneType = field(
        default=None,
        metadata={
            "name": "CrestaZone",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    accuracy_level: None | str = field(
        default=None,
        metadata={
            "name": "AccuracyLevel",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
