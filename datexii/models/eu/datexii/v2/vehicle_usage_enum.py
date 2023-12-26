from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VehicleUsageEnum(Enum):
    """
    Types of usage of a vehicle.

    :cvar AGRICULTURAL: Vehicle used for agricultural purposes.
    :cvar COMMERCIAL: Vehicle which is limited to non-private usage or
        public transport usage.
    :cvar EMERGENCY_SERVICES: Vehicle used by the emergency services.
    :cvar MILITARY: Vehicle used by the military.
    :cvar NON_COMMERCIAL: Vehicle used for non-commercial or private
        purposes.
    :cvar PATROL: Vehicle used as part of a patrol service, e.g. road
        operator or automobile association patrol vehicle.
    :cvar RECOVERY_SERVICES: Vehicle used to provide a recovery service.
    :cvar ROAD_MAINTENANCE_OR_CONSTRUCTION: Vehicle used for road
        maintenance or construction work purposes.
    :cvar ROAD_OPERATOR: Vehicle used by the road operator.
    :cvar TAXI: Vehicle used to provide an authorised taxi service.
    """

    AGRICULTURAL = "agricultural"
    COMMERCIAL = "commercial"
    EMERGENCY_SERVICES = "emergencyServices"
    MILITARY = "military"
    NON_COMMERCIAL = "nonCommercial"
    PATROL = "patrol"
    RECOVERY_SERVICES = "recoveryServices"
    ROAD_MAINTENANCE_OR_CONSTRUCTION = "roadMaintenanceOrConstruction"
    ROAD_OPERATOR = "roadOperator"
    TAXI = "taxi"
