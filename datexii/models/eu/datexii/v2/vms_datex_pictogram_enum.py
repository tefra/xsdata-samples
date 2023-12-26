from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VmsDatexPictogramEnum(Enum):
    """
    Types of main pictograms.

    :cvar ACCIDENT: Accident.
    :cvar ADVISORY_SPEED: Advisory speed limit.
    :cvar ANIMALS_ON_ROAD: Animal(s) on the road.
    :cvar BLANK_VOID: Blank or void.
    :cvar BRIDGE_CLOSED: Bridge closed.
    :cvar BRIDGE_SWING_IN_OPERATION: Bridge swing in operation.
    :cvar CAR_PARK_FULL: Car park full.
    :cvar CAR_PARK_SPACES_AVAILABLE: Spaces available in car park.
    :cvar CARRIAGEWAY_NARROWS: The carriageway narrows ahead.
    :cvar CARRIAGEWAY_NARROWS_ON_THE_LEFT: The carriageway narrows ahead
        from the left.
    :cvar CARRIAGEWAY_NARROWS_ON_THE_RIGHT: The carriageway narrows
        ahead from the right.
    :cvar CARRIAGEWAY_REDUCED_TO_ONE_LANE: Carriageway reduced to one
        lane.
    :cvar CARRIAGEWAY_REDUCED_TO_TWO_LANES: Carriageway reduced to two
        lanes.
    :cvar CARRIAGEWAY_REDUCED_TO_THREE_LANES: Carriageway reduced to
        three lanes.
    :cvar CHAINS_OR_SNOW_TYRES_RECOMMENDED: Chains or snow tyres are
        recommended.
    :cvar COMPULSORY_MINIMUM_SPEED: Mandatory minimum speed limit.
    :cvar CROSS_WIND: Cross wind.
    :cvar DANGER_OF_FIRE: Danger of fire.
    :cvar DRIVING_OF_VEHICLES_LESS_THAN_XMETRES_APART_PROHIBITED: The
        driving of vehicles less than X metres apart is prohibited.
    :cvar END_OF_ADVISORY_SPEED: End of advisory speed.
    :cvar END_OF_COMPULSORY_MINIMUM_SPEED: End of compulsory minimum
        speed limit.
    :cvar END_OF_PROHIBITION_OF_OVERTAKING: End of prohibition of
        overtaking.
    :cvar END_OF_PROHIBITION_OF_OVERTAKING_FOR_GOODS_VEHICLES: End of
        prohibition of overtaking for goods vehicles.
    :cvar END_OF_SPEED_LIMIT: End of mandatory speed limit.
    :cvar EXIT_CLOSED: Exit closed.
    :cvar FALLING_ROCKS: Danger of rock fall or landslide.
    :cvar FASTEN_CHILDRENS_SEAT_BELTS: Fasten the seat belts of
        children.
    :cvar FASTEN_YOUR_SEAT_BELT: Fasten your seat belt.
    :cvar FIRE: Fire.
    :cvar FLOODING_OR_FLASH_FLOODS: Flooding or flash floods.
    :cvar FOG: Fog.
    :cvar FOOTBALL_MATCH: Football match (current or anticipated
        disruption due to football match).
    :cvar HARD_SHOULDER_NOT_RUNNING: Hard shoulder running is in
        operation.
    :cvar HARD_SHOULDER_RUNNING: Hard shoulder running is not in
        operation.
    :cvar KEEP_ASAFE_DISTANCE: Keep a safe distance.
    :cvar KEEP_LEFT: Keep left.
    :cvar KEEP_RIGHT: Keep right.
    :cvar LANE1_CLOSED_OF2: Lane 1 closed on a 2 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANE2_CLOSED_OF2: Lane 2 closed on a 2 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANE1_CLOSED_OF3: Lane 1 closed on a 3 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANE3_CLOSED_OF3: Lane 3 closed on a 3 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANES1_AND2_CLOSED_OF3: Lanes 1 and 2 closed on a 3 lane
        carriageway. Lanes numbered from nearside (next to hard shoulder
        on motorway) to central median.
    :cvar LANES2_AND3_CLOSED_OF3: Lanes 2 and 3 closed on a 3 lane
        carriageway. Lanes numbered from nearside (next to hard shoulder
        on motorway) to central median.
    :cvar LANE1_CLOSED_OF4: Lane 1 closed on a 4 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANE4_CLOSED_OF4: Lane 4 closed on a 4 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANES1_AND2_CLOSED_OF4: Lanes 1 and 2 closed on a 4 lane
        carriageway. Lanes numbered from nearside (next to hard shoulder
        on motorway) to central median.
    :cvar LANES3_AND4_CLOSED_OF4: Lanes 3 and 4 closed on a 4 lane
        carriageway. Lanes numbered from nearside (next to hard shoulder
        on motorway) to central median.
    :cvar LANES1_AND2_AND3_CLOSED_OF4: Lanes 1, 2 and 3 closed on a 4
        lane carriageway. Lanes numbered from nearside (next to hard
        shoulder on motorway) to central median.
    :cvar LANES2_AND3_AND4_CLOSED_OF4: Lanes 2, 3 and 4 closed on a 4
        lane carriageway. Lanes numbered from nearside (next to hard
        shoulder on motorway) to central median.
    :cvar LANE_CLOSED: Lane closed.
    :cvar LANE_DEVIATION_TO_LEFT: Lane deviates to the left.
    :cvar LANE_DEVIATION_TO_RIGHT: Lane deviates to the right.
    :cvar LANE_OPEN: Lane open.
    :cvar LEFT_HAND_LANE_CLOSED: Left hand lane closed ahead.
    :cvar LIGHT_SIGNALS: Traffic light signals ahead.
    :cvar LOOSE_GRAVEL: Loose gravel.
    :cvar MAINTENANCE_VEHICLE_IN_ACTION: Maintenance vehicles in action.
    :cvar MAXIMUM_SPEED_LIMITED_TO_THE_FIGURE_INDICATED: Mandatory
        maximum speed limit, displayed as speed limit indside a red
        circle.
    :cvar NARROW_LANES_AEAD: Narrow lanes ahead.
    :cvar NO_ENTRY: No entry.
    :cvar NO_ENTRY_FOR_ANY_POWER_DRIVEN_VEHICLE_DRAWING_ATRAILER: No
        entry for any power driven vehicle drawing a trailer
    :cvar
        NO_ENTRY_FOR_ANY_POWER_DRIVEN_VEHICLE_DRAWING_ATRAILER_OTHER_THAN_ASEMI_TRAILER_OR_ASINGLE_AXLE_TRAILER:
        No entry to any power driven vehicle drawing a trailer other
        than a semi-trailer or a single axle trailer. A semi-trailer is
        one designed to be coupled to a motor vehicle so that part of
        its weight and that of its load is borne by the motor vehicle.
    :cvar NO_ENTRY_FOR_GOODS_VEHICLES: No entry for goods vehicles.
    :cvar NO_ENTRY_FOR_VEHICLES_EXCEEDING_XTONNES_LADEN_MASS: No entry
        for vehicles exceeding X tonnes laden mass.
    :cvar
        NO_ENTRY_FOR_VEHICLES_HAVING_AMASS_EXCEEDING_XTONNES_ON_ONE_AXLE:
        No entry for vehicles having a mass exceeding X tonnes on a
        single axle.
    :cvar
        NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_HEIGHT_EXCEEDING_XMETRES:
        No entry for vehicles having an overall height exceeding X
        metres.
    :cvar
        NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_LENGTH_EXCEEDING_XMETRES:
        No entry for vehicles having an overall length exceeding X
        metres.
    :cvar
        NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_WIDTH_EXCEEDING_XMETRES:
        No entry for vehicles having an overall width exceeding X
        metres.
    :cvar NO_ENTRY_FOR_VEHICLES_CARRYING_DANGEROUS_GOODS: No entry for
        vehicles carrying dangerous goods.
    :cvar OTHER_DANGERS: Danger ahead of an unspecified nature.
    :cvar OVERTAKING_BY_GOODS_VEHICLES_PROHIBITED: Overtaking prohibited
        for goods vehicles.
    :cvar OVERTAKING_PROHIBITED: Overtaking prohibited.
    :cvar POLLUTION_OR_SMOG_ALERT: Pollution or smog alert.
    :cvar QUEUE: Queue ahead.
    :cvar RAIN: Rain.
    :cvar RIGHT_HAND_LANE_CLOSED: Right hand lane closed ahead.
    :cvar ROAD_CLOSED_AHEAD: Road closed ahead.
    :cvar ROADWORKS: Roadworks.
    :cvar SLIPPERY_ROAD: Slippery road.
    :cvar SMOKE: Smoke.
    :cvar SNOW: Snow.
    :cvar SNOW_CHAINS_COMPULSORY: The use of snow chains is compulsory.
    :cvar SNOW_TYRES_COMPULSORY: The use of snow tyres is compulsory.
    :cvar SNOW_PLOUGH_IN_ACTION: Snow plough(s) in action.
    :cvar SPEED_CAMERAS_IN_ACTION: Speed cameras in action.
    :cvar TRAFFIC_CONGESTION: Traffic congestion and possible queues.
    :cvar TRAFFIC_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD: All traffic is
        diverted to the opposite carriageway ahead in a contraflow
        layout.
    :cvar TRAFFIC_PARTIALLY_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD:
        Traffic is partially diverted to the opposite carriageway ahead
        in a contraflow layout.
    :cvar TUNNEL_CLOSED: Tunnel closed.
    :cvar TURN_LEFT: Mandatory turn left.
    :cvar TURN_RIGHT: Mandatory turn right.
    :cvar TWO_WAY_TRAFFIC: Two way traffic (on a single carriageway).
    :cvar UNEVEN_ROAD: Uneven road surface.
    :cvar VEHICLE_FIRE: Vehicle fire.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    ACCIDENT = "accident"
    ADVISORY_SPEED = "advisorySpeed"
    ANIMALS_ON_ROAD = "animalsOnRoad"
    BLANK_VOID = "blankVoid"
    BRIDGE_CLOSED = "bridgeClosed"
    BRIDGE_SWING_IN_OPERATION = "bridgeSwingInOperation"
    CAR_PARK_FULL = "carParkFull"
    CAR_PARK_SPACES_AVAILABLE = "carParkSpacesAvailable"
    CARRIAGEWAY_NARROWS = "carriagewayNarrows"
    CARRIAGEWAY_NARROWS_ON_THE_LEFT = "carriagewayNarrowsOnTheLeft"
    CARRIAGEWAY_NARROWS_ON_THE_RIGHT = "carriagewayNarrowsOnTheRight"
    CARRIAGEWAY_REDUCED_TO_ONE_LANE = "carriagewayReducedToOneLane"
    CARRIAGEWAY_REDUCED_TO_TWO_LANES = "carriagewayReducedToTwoLanes"
    CARRIAGEWAY_REDUCED_TO_THREE_LANES = "carriagewayReducedToThreeLanes"
    CHAINS_OR_SNOW_TYRES_RECOMMENDED = "chainsOrSnowTyresRecommended"
    COMPULSORY_MINIMUM_SPEED = "compulsoryMinimumSpeed"
    CROSS_WIND = "crossWind"
    DANGER_OF_FIRE = "dangerOfFire"
    DRIVING_OF_VEHICLES_LESS_THAN_XMETRES_APART_PROHIBITED = (
        "drivingOfVehiclesLessThanXMetresApartProhibited"
    )
    END_OF_ADVISORY_SPEED = "endOfAdvisorySpeed"
    END_OF_COMPULSORY_MINIMUM_SPEED = "endOfCompulsoryMinimumSpeed"
    END_OF_PROHIBITION_OF_OVERTAKING = "endOfProhibitionOfOvertaking"
    END_OF_PROHIBITION_OF_OVERTAKING_FOR_GOODS_VEHICLES = (
        "endOfProhibitionOfOvertakingForGoodsVehicles"
    )
    END_OF_SPEED_LIMIT = "endOfSpeedLimit"
    EXIT_CLOSED = "exitClosed"
    FALLING_ROCKS = "fallingRocks"
    FASTEN_CHILDRENS_SEAT_BELTS = "fastenChildrensSeatBelts"
    FASTEN_YOUR_SEAT_BELT = "fastenYourSeatBelt"
    FIRE = "fire"
    FLOODING_OR_FLASH_FLOODS = "floodingOrFlashFloods"
    FOG = "fog"
    FOOTBALL_MATCH = "footballMatch"
    HARD_SHOULDER_NOT_RUNNING = "hardShoulderNotRunning"
    HARD_SHOULDER_RUNNING = "hardShoulderRunning"
    KEEP_ASAFE_DISTANCE = "keepASafeDistance"
    KEEP_LEFT = "keepLeft"
    KEEP_RIGHT = "keepRight"
    LANE1_CLOSED_OF2 = "lane1ClosedOf2"
    LANE2_CLOSED_OF2 = "lane2ClosedOf2"
    LANE1_CLOSED_OF3 = "lane1ClosedOf3"
    LANE3_CLOSED_OF3 = "lane3ClosedOf3"
    LANES1_AND2_CLOSED_OF3 = "lanes1And2ClosedOf3"
    LANES2_AND3_CLOSED_OF3 = "lanes2And3ClosedOf3"
    LANE1_CLOSED_OF4 = "lane1ClosedOf4"
    LANE4_CLOSED_OF4 = "lane4ClosedOf4"
    LANES1_AND2_CLOSED_OF4 = "lanes1And2ClosedOf4"
    LANES3_AND4_CLOSED_OF4 = "lanes3And4ClosedOf4"
    LANES1_AND2_AND3_CLOSED_OF4 = "lanes1And2And3ClosedOf4"
    LANES2_AND3_AND4_CLOSED_OF4 = "lanes2And3And4ClosedOf4"
    LANE_CLOSED = "laneClosed"
    LANE_DEVIATION_TO_LEFT = "laneDeviationToLeft"
    LANE_DEVIATION_TO_RIGHT = "laneDeviationToRight"
    LANE_OPEN = "laneOpen"
    LEFT_HAND_LANE_CLOSED = "leftHandLaneClosed"
    LIGHT_SIGNALS = "lightSignals"
    LOOSE_GRAVEL = "looseGravel"
    MAINTENANCE_VEHICLE_IN_ACTION = "maintenanceVehicleInAction"
    MAXIMUM_SPEED_LIMITED_TO_THE_FIGURE_INDICATED = (
        "maximumSpeedLimitedToTheFigureIndicated"
    )
    NARROW_LANES_AEAD = "narrowLanesAead"
    NO_ENTRY = "noEntry"
    NO_ENTRY_FOR_ANY_POWER_DRIVEN_VEHICLE_DRAWING_ATRAILER = (
        "noEntryForAnyPowerDrivenVehicleDrawingATrailer"
    )
    NO_ENTRY_FOR_ANY_POWER_DRIVEN_VEHICLE_DRAWING_ATRAILER_OTHER_THAN_ASEMI_TRAILER_OR_ASINGLE_AXLE_TRAILER = "noEntryForAnyPowerDrivenVehicleDrawingATrailerOtherThanASemiTrailerOrASingleAxleTrailer"
    NO_ENTRY_FOR_GOODS_VEHICLES = "noEntryForGoodsVehicles"
    NO_ENTRY_FOR_VEHICLES_EXCEEDING_XTONNES_LADEN_MASS = (
        "noEntryForVehiclesExceedingXTonnesLadenMass"
    )
    NO_ENTRY_FOR_VEHICLES_HAVING_AMASS_EXCEEDING_XTONNES_ON_ONE_AXLE = (
        "noEntryForVehiclesHavingAMassExceedingXTonnesOnOneAxle"
    )
    NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_HEIGHT_EXCEEDING_XMETRES = (
        "noEntryForVehiclesHavingAnOverallHeightExceedingXMetres"
    )
    NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_LENGTH_EXCEEDING_XMETRES = (
        "noEntryForVehiclesHavingAnOverallLengthExceedingXMetres"
    )
    NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_WIDTH_EXCEEDING_XMETRES = (
        "noEntryForVehiclesHavingAnOverallWidthExceedingXMetres"
    )
    NO_ENTRY_FOR_VEHICLES_CARRYING_DANGEROUS_GOODS = (
        "noEntryForVehiclesCarryingDangerousGoods"
    )
    OTHER_DANGERS = "otherDangers"
    OVERTAKING_BY_GOODS_VEHICLES_PROHIBITED = (
        "overtakingByGoodsVehiclesProhibited"
    )
    OVERTAKING_PROHIBITED = "overtakingProhibited"
    POLLUTION_OR_SMOG_ALERT = "pollutionOrSmogAlert"
    QUEUE = "queue"
    RAIN = "rain"
    RIGHT_HAND_LANE_CLOSED = "rightHandLaneClosed"
    ROAD_CLOSED_AHEAD = "roadClosedAhead"
    ROADWORKS = "roadworks"
    SLIPPERY_ROAD = "slipperyRoad"
    SMOKE = "smoke"
    SNOW = "snow"
    SNOW_CHAINS_COMPULSORY = "snowChainsCompulsory"
    SNOW_TYRES_COMPULSORY = "snowTyresCompulsory"
    SNOW_PLOUGH_IN_ACTION = "snowPloughInAction"
    SPEED_CAMERAS_IN_ACTION = "speedCamerasInAction"
    TRAFFIC_CONGESTION = "trafficCongestion"
    TRAFFIC_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD = (
        "trafficDeviatedToOppositeCarriagewayAhead"
    )
    TRAFFIC_PARTIALLY_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD = (
        "trafficPartiallyDeviatedToOppositeCarriagewayAhead"
    )
    TUNNEL_CLOSED = "tunnelClosed"
    TURN_LEFT = "turnLeft"
    TURN_RIGHT = "turnRight"
    TWO_WAY_TRAFFIC = "twoWayTraffic"
    UNEVEN_ROAD = "unevenRoad"
    VEHICLE_FIRE = "vehicleFire"
    OTHER = "other"
