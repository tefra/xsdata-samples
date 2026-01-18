from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.number_type import (
    NumberType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.aircraft_type_aircarft_type import (
    AircraftTypeAircarftType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.vehicle_type import (
    VehicleType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class AircraftType(VehicleType):
    crew_seat_count: NumberType | None = field(
        default=None,
        metadata={
            "name": "CrewSeatCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    pilot_seat_count: NumberType | None = field(
        default=None,
        metadata={
            "name": "PilotSeatCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    primary_hangar: TextType | None = field(
        default=None,
        metadata={
            "name": "PrimaryHangar",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    seat_capacity: NumberType | None = field(
        default=None,
        metadata={
            "name": "SeatCapacity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    aircarft_type: AircraftTypeAircarftType | None = field(
        default=None,
        metadata={
            "name": "AircarftType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
