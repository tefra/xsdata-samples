from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class SourceTypeEnum(Enum):
    """
    Type of sources from which situation information may be derived.

    :cvar AUTOMOBILE_CLUB_PATROL: A patrol of an automobile club.
    :cvar CAMERA_OBSERVATION: A camera observation (either still or
        video camera).
    :cvar FREIGHT_VEHICLE_OPERATOR: An operator of freight vehicles.
    :cvar INDUCTION_LOOP_MONITORING_STATION: A station dedicated to the
        monitoring of the road network by processing inductive loop
        information.
    :cvar INFRARED_MONITORING_STATION: A station dedicated to the
        monitoring of the road network by processing infrared image
        information.
    :cvar MICROWAVE_MONITORING_STATION: A station dedicated to the
        monitoring of the road network by processing microwave
        information.
    :cvar MOBILE_TELEPHONE_CALLER: A caller using a mobile telephone
        (who may or may not be on the road network).
    :cvar NON_POLICE_EMERGENCY_SERVICE_PATROL: Emergency service patrols
        other than police.
    :cvar OTHER_INFORMATION: Other sources of information.
    :cvar OTHER_OFFICIAL_VEHICLE: Personnel from a vehicle belonging to
        the road operator or authority or any emergency service,
        including authorised breakdown service organisations.
    :cvar POLICE_PATROL: A police patrol.
    :cvar PRIVATE_BREAKDOWN_SERVICE: A private breakdown service.
    :cvar PUBLIC_AND_PRIVATE_UTILITIES: A utility organisation, either
        public or private.
    :cvar REGISTERED_MOTORIST_OBSERVER: A motorist who is an officially
        registered observer.
    :cvar ROAD_AUTHORITIES: A road authority.
    :cvar ROAD_OPERATOR_PATROL: A patrol of the road operator or
        authority.
    :cvar ROADSIDE_TELEPHONE_CALLER: A caller who is using an emergency
        roadside telephone.
    :cvar SPOTTER_AIRCRAFT: A spotter aircraft of an organisation
        specifically assigned to the monitoring of the traffic network.
    :cvar TRAFFIC_MONITORING_STATION: A station, usually automatic,
        dedicated to the monitoring of the road network.
    :cvar TRANSIT_OPERATOR: An operator of a transit service, e.g. bus
        link operator.
    :cvar VEHICLE_PROBE_MEASUREMENT: A specially equipped vehicle used
        to provide measurements.
    :cvar VIDEO_PROCESSING_MONITORING_STATION: A station dedicated to
        the monitoring of the road network by processing video image
        information.
    """

    AUTOMOBILE_CLUB_PATROL = "automobileClubPatrol"
    CAMERA_OBSERVATION = "cameraObservation"
    FREIGHT_VEHICLE_OPERATOR = "freightVehicleOperator"
    INDUCTION_LOOP_MONITORING_STATION = "inductionLoopMonitoringStation"
    INFRARED_MONITORING_STATION = "infraredMonitoringStation"
    MICROWAVE_MONITORING_STATION = "microwaveMonitoringStation"
    MOBILE_TELEPHONE_CALLER = "mobileTelephoneCaller"
    NON_POLICE_EMERGENCY_SERVICE_PATROL = "nonPoliceEmergencyServicePatrol"
    OTHER_INFORMATION = "otherInformation"
    OTHER_OFFICIAL_VEHICLE = "otherOfficialVehicle"
    POLICE_PATROL = "policePatrol"
    PRIVATE_BREAKDOWN_SERVICE = "privateBreakdownService"
    PUBLIC_AND_PRIVATE_UTILITIES = "publicAndPrivateUtilities"
    REGISTERED_MOTORIST_OBSERVER = "registeredMotoristObserver"
    ROAD_AUTHORITIES = "roadAuthorities"
    ROAD_OPERATOR_PATROL = "roadOperatorPatrol"
    ROADSIDE_TELEPHONE_CALLER = "roadsideTelephoneCaller"
    SPOTTER_AIRCRAFT = "spotterAircraft"
    TRAFFIC_MONITORING_STATION = "trafficMonitoringStation"
    TRANSIT_OPERATOR = "transitOperator"
    VEHICLE_PROBE_MEASUREMENT = "vehicleProbeMeasurement"
    VIDEO_PROCESSING_MONITORING_STATION = "videoProcessingMonitoringStation"
