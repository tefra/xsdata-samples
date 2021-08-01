from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RoadOperatorServiceDisruptionTypeEnum(Enum):
    """
    Types of disruption to road operator services relevant to road users.

    :cvar EMERGENCY_TELEPHONE_NUMBER_OUT_OF_SERVICE: Emergency telephone
        number for use by public to report incidents is out of service.
    :cvar INFORMATION_SERVICE_TELEPHONE_NUMBER_OUT_OF_SERVICE: Road
        information service telephone number is out of service.
    :cvar NO_TRAFFIC_OFFICER_PATROL_SERVICE: No traffic officer patrol
        service is operating.
    """
    EMERGENCY_TELEPHONE_NUMBER_OUT_OF_SERVICE = "emergencyTelephoneNumberOutOfService"
    INFORMATION_SERVICE_TELEPHONE_NUMBER_OUT_OF_SERVICE = "informationServiceTelephoneNumberOutOfService"
    NO_TRAFFIC_OFFICER_PATROL_SERVICE = "noTrafficOfficerPatrolService"
