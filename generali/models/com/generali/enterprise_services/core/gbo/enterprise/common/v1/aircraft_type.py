from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.aircraft_type_aircarft_type import AircraftTypeAircarftType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.vehicle_type import VehicleType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


@dataclass
class AircraftType(VehicleType):
    crew_seat_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "CrewSeatCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    pilot_seat_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PilotSeatCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    primary_hangar: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "PrimaryHangar",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    seat_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeatCapacity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    aircarft_type: Optional[AircraftTypeAircarftType] = field(
        default=None,
        metadata={
            "name": "AircarftType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
