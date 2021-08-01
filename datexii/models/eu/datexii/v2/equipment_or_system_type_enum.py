from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class EquipmentOrSystemTypeEnum(Enum):
    """
    Types of equipment and systems used to support the operation of the road
    network.

    :cvar ANPR_CAMERAS: Automatic number plate recognition cameras.
    :cvar AUTOMATED_TOLL_SYSTEM: Automated toll system.
    :cvar CCTV_CAMERAS: Closed-circuit television cameras.
    :cvar EMERGENCY_ROADSIDE_TELEPHONES: Emergency roadside telephones.
    :cvar GALLERY_LIGHTS: Gallery lights.
    :cvar LANE_CONTROL_SIGNS: Signs used to control lane usage (e.g. in
        tidal flow systems or hard shoulder running).
    :cvar LEVEL_CROSSING: Level crossing (barriers and signals).
    :cvar MATRIX_SIGNS: Matrix signs. These normally comprise a symbol
        display area surrounded by four lights (usually amber) which
        flash when a symbol is displayed.
    :cvar RAMP_CONTROLS: Ramp control equipment.
    :cvar ROADSIDE_COMMUNICATIONS_SYSTEM: Roadside communications system
        which is used by one or more roadside equipments or systems.
    :cvar ROADSIDE_POWER_SYSTEM: Roadside power system which is used by
        one or more roadside equipments or systems.
    :cvar SPEED_CONTROL_SIGNS: Signs used to control traffic speed.
    :cvar STREET_LIGHTING: Street or road lighting.
    :cvar TEMPORARY_TRAFFIC_LIGHTS: Temporary traffic lights.
    :cvar TOLL_GATES: Toll gates.
    :cvar TRAFFIC_LIGHT_SETS: Sets of traffic lights.
    :cvar TRAFFIC_SIGNALS: Traffic signals.
    :cvar TUNNEL_LIGHTS: Tunnel lights.
    :cvar TUNNEL_VENTILATION: Tunnel ventilation system.
    :cvar VARIABLE_MESSAGE_SIGNS: Variable message signs.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ANPR_CAMERAS = "anprCameras"
    AUTOMATED_TOLL_SYSTEM = "automatedTollSystem"
    CCTV_CAMERAS = "cctvCameras"
    EMERGENCY_ROADSIDE_TELEPHONES = "emergencyRoadsideTelephones"
    GALLERY_LIGHTS = "galleryLights"
    LANE_CONTROL_SIGNS = "laneControlSigns"
    LEVEL_CROSSING = "levelCrossing"
    MATRIX_SIGNS = "matrixSigns"
    RAMP_CONTROLS = "rampControls"
    ROADSIDE_COMMUNICATIONS_SYSTEM = "roadsideCommunicationsSystem"
    ROADSIDE_POWER_SYSTEM = "roadsidePowerSystem"
    SPEED_CONTROL_SIGNS = "speedControlSigns"
    STREET_LIGHTING = "streetLighting"
    TEMPORARY_TRAFFIC_LIGHTS = "temporaryTrafficLights"
    TOLL_GATES = "tollGates"
    TRAFFIC_LIGHT_SETS = "trafficLightSets"
    TRAFFIC_SIGNALS = "trafficSignals"
    TUNNEL_LIGHTS = "tunnelLights"
    TUNNEL_VENTILATION = "tunnelVentilation"
    VARIABLE_MESSAGE_SIGNS = "variableMessageSigns"
    OTHER = "other"
