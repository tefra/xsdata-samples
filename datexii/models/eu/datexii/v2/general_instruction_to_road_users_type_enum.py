from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class GeneralInstructionToRoadUsersTypeEnum(Enum):
    """
    General instructions that may be issued to road users (specifically drivers and
    sometimes passengers) by an operator or operational system in support of
    network management activities or emergency situations.

    :cvar ALLOW_EMERGENCY_VEHICLES_TO_PASS: Allow emergency vehicles to
        pass.
    :cvar APPROACH_WITH_CARE: Approach with care.
    :cvar AVOID_THE_AREA: Drivers are to avoid the area.
    :cvar CLOSE_ALL_WINDOWS_TURN_OFF_HEATER_AND_VENTS: Close all windows
        and turn off heater and vents.
    :cvar CROSS_JUNCTION_WITH_CARE: Cross junction with care.
    :cvar DO_NOT_ALLOW_UNNECESSARY_GAPS: Do not allow unnecessary gaps.
    :cvar DO_NOT_LEAVE_YOUR_VEHICLE: Do not leave your vehicle.
    :cvar DO_NOT_THROW_OUT_ANY_BURNING_OBJECTS: Do not throw out any
        burning objects.
    :cvar DO_NOT_USE_NAVIGATION_SYSTEMS: Do not use navigation systems
        to determine routing.
    :cvar DRIVE_CAREFULLY: Drive carefully.
    :cvar DRIVE_WITH_EXTREME_CAUTION: Drive with extreme caution.
    :cvar FLASH_YOUR_LIGHTS: Flash your lights to warn oncoming traffic
        of hazard ahead.
    :cvar FOLLOW_THE_VEHICLE_IN_FRONT_SMOOTHLY: Follow the vehicle in
        front, smoothly.
    :cvar INCREASE_NORMAL_FOLLOWING_DISTANCE: Increase normal following
        distance.
    :cvar IN_EMERGENCY_WAIT_FOR_PATROL_SERVICE: In emergency, wait for
        patrol service (either road operator or police patrol service).
    :cvar KEEP_YOUR_DISTANCE: Keep your distance.
    :cvar LEAVE_YOUR_VEHICLE_PROCEED_TO_NEXT_SAFE_PLACE: Leave your
        vehicle and proceed to next safe place.
    :cvar NO_NAKED_FLAMES: No naked flames.
    :cvar NO_OVERTAKING: No overtaking on the specified section of road.
    :cvar NO_SMOKING: No smoking.
    :cvar NO_STOPPING: No stopping.
    :cvar NO_UTURNS: No U-turns.
    :cvar OBSERVE_AMBER_ALERT: Observe current amber alert (an emergency
        alert issued for a missing or abducted child).
    :cvar OBSERVE_SIGNALS: Observe signals.
    :cvar OBSERVE_SIGNS: Observe signs.
    :cvar ONLY_TRAVEL_IF_ABSOLUTELY_NECESSARY: Only travel if absolutely
        necessary.
    :cvar OVERTAKE_WITH_CARE: Overtake with care.
    :cvar PULL_OVER_TO_THE_EDGE_OF_THE_ROADWAY: Pull over to the edge of
        the roadway.
    :cvar STOP_AT_NEXT_SAFE_PLACE: Stop at next safe place.
    :cvar STOP_AT_NEXT_SERVICE_AREA: Stop at next rest service area or
        car park.
    :cvar SWITCH_OFF_ENGINE: Switch off engine.
    :cvar SWITCH_OFF_MOBILE_PHONES_AND_TWO_WAY_RADIOS: Switch off mobile
        phones and two-way radios.
    :cvar TEST_YOUR_BRAKES: Test your brakes.
    :cvar USE_BUS_SERVICE: Use bus service.
    :cvar USE_FOG_LIGHTS: Use fog lights.
    :cvar USE_HAZARD_WARNING_LIGHTS: Use hazard warning lights.
    :cvar USE_HEADLIGHTS: Use headlights.
    :cvar USE_RAIL_SERVICE: Use rail service.
    :cvar USE_TRAM_SERVICE: Use tram service.
    :cvar USE_UNDERGROUND_SERVICE: Use underground service.
    :cvar WAIT_FOR_ESCORT_VEHICLE: Wait for escort vehicle.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ALLOW_EMERGENCY_VEHICLES_TO_PASS = "allowEmergencyVehiclesToPass"
    APPROACH_WITH_CARE = "approachWithCare"
    AVOID_THE_AREA = "avoidTheArea"
    CLOSE_ALL_WINDOWS_TURN_OFF_HEATER_AND_VENTS = "closeAllWindowsTurnOffHeaterAndVents"
    CROSS_JUNCTION_WITH_CARE = "crossJunctionWithCare"
    DO_NOT_ALLOW_UNNECESSARY_GAPS = "doNotAllowUnnecessaryGaps"
    DO_NOT_LEAVE_YOUR_VEHICLE = "doNotLeaveYourVehicle"
    DO_NOT_THROW_OUT_ANY_BURNING_OBJECTS = "doNotThrowOutAnyBurningObjects"
    DO_NOT_USE_NAVIGATION_SYSTEMS = "doNotUseNavigationSystems"
    DRIVE_CAREFULLY = "driveCarefully"
    DRIVE_WITH_EXTREME_CAUTION = "driveWithExtremeCaution"
    FLASH_YOUR_LIGHTS = "flashYourLights"
    FOLLOW_THE_VEHICLE_IN_FRONT_SMOOTHLY = "followTheVehicleInFrontSmoothly"
    INCREASE_NORMAL_FOLLOWING_DISTANCE = "increaseNormalFollowingDistance"
    IN_EMERGENCY_WAIT_FOR_PATROL_SERVICE = "inEmergencyWaitForPatrolService"
    KEEP_YOUR_DISTANCE = "keepYourDistance"
    LEAVE_YOUR_VEHICLE_PROCEED_TO_NEXT_SAFE_PLACE = "leaveYourVehicleProceedToNextSafePlace"
    NO_NAKED_FLAMES = "noNakedFlames"
    NO_OVERTAKING = "noOvertaking"
    NO_SMOKING = "noSmoking"
    NO_STOPPING = "noStopping"
    NO_UTURNS = "noUturns"
    OBSERVE_AMBER_ALERT = "observeAmberAlert"
    OBSERVE_SIGNALS = "observeSignals"
    OBSERVE_SIGNS = "observeSigns"
    ONLY_TRAVEL_IF_ABSOLUTELY_NECESSARY = "onlyTravelIfAbsolutelyNecessary"
    OVERTAKE_WITH_CARE = "overtakeWithCare"
    PULL_OVER_TO_THE_EDGE_OF_THE_ROADWAY = "pullOverToTheEdgeOfTheRoadway"
    STOP_AT_NEXT_SAFE_PLACE = "stopAtNextSafePlace"
    STOP_AT_NEXT_SERVICE_AREA = "stopAtNextServiceArea"
    SWITCH_OFF_ENGINE = "switchOffEngine"
    SWITCH_OFF_MOBILE_PHONES_AND_TWO_WAY_RADIOS = "switchOffMobilePhonesAndTwoWayRadios"
    TEST_YOUR_BRAKES = "testYourBrakes"
    USE_BUS_SERVICE = "useBusService"
    USE_FOG_LIGHTS = "useFogLights"
    USE_HAZARD_WARNING_LIGHTS = "useHazardWarningLights"
    USE_HEADLIGHTS = "useHeadlights"
    USE_RAIL_SERVICE = "useRailService"
    USE_TRAM_SERVICE = "useTramService"
    USE_UNDERGROUND_SERVICE = "useUndergroundService"
    WAIT_FOR_ESCORT_VEHICLE = "waitForEscortVehicle"
    OTHER = "other"
