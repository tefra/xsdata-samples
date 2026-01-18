from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass(kw_only=True)
class GlobalPositionAddressType:
    """
    :ivar latitude:
    :ivar longitude:
    :ivar wgscode: The World Geodetic System (WGS) is a standard for use
        in cartography, geodesy, and navigation including by GPS. It
        comprises a standard coordinate system for the Earth, a standard
        spheroidal reference surface (the datum or reference ellipsoid)
        for raw altitude data, and a gravitational equipotential surface
        (the geoid) that defines the nominal sea level.
    """

    latitude: NumericType = field(
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )
    longitude: NumericType = field(
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )
    wgscode: Idtype = field(
        metadata={
            "name": "WGSCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )
