from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import Idtype

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
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
    latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )
    longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )
    wgscode: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "WGSCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )
