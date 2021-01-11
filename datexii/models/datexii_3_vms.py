from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from datexii.models.datexii_3_common import (
    Fault,
    HeaderInformation,
    InternationalIdentifier,
    MultilingualString,
    PayloadPublication,
    UrlLink,
    VersionedReference,
    ExtensionType,
)
from datexii.models.datexii_3_location_referencing import (
    Lane,
    Location,
)

__NAMESPACE__ = "http://datex2.eu/schema/3/vms"


class ColourEnum1(Enum):
    """
    Colours.

    :cvar AMBER: The colour amber.
    :cvar BLUE: The colour blue.
    :cvar GREEN: The colour green.
    :cvar RED: The colour red.
    :cvar WHITE: The colour white.
    :cvar WHITE_YELLOW: The colour white-yellow.
    :cvar EXTENDED:
    """
    AMBER = "amber"
    BLUE = "blue"
    GREEN = "green"
    RED = "red"
    WHITE = "white"
    WHITE_YELLOW = "whiteYellow"
    EXTENDED = "_extended"


class CompositePictogramEnum1(Enum):
    """
    Identifies a pictogram used only for building a composite pictogram.

    :cvar CONDITION_ON_CURRENT_SECTION_AFTER_NEXT_EXIT: Deals with
        condition on current section after next exit.
    :cvar CONDITION_AT_NEXT_EXIT: Deals with condition at next exit.
    :cvar CONDITION_ON_CURRENT_SECTION_AFTER_SECONDT_EXIT: Deals with
        condition on current section after second exit.
    :cvar CONDITION_AT_SECOND_EXIT: Deals with condition on current
        section at second exit.
    :cvar RESTRICTION_ON_CURRENT_SECTION_AFTER_NEXT_EXIT: Deals with
        restriction on current section after next exit.
    :cvar RESTRICTION_AT_NEXT_EXIT: Deals with restriction at next exit.
    :cvar RESTRICTION_ON_CURRENT_SECTION_AFTER_SECOND_EXIT: Deals with
        restriction on current section after second exit.
    :cvar RESTRICTION_AT_SECONDT_EXIT: Deals with restriction after
        second exit.
    :cvar EXTENDED:
    """
    CONDITION_ON_CURRENT_SECTION_AFTER_NEXT_EXIT = "conditionOnCurrentSectionAfterNextExit"
    CONDITION_AT_NEXT_EXIT = "conditionAtNextExit"
    CONDITION_ON_CURRENT_SECTION_AFTER_SECONDT_EXIT = "conditionOnCurrentSectionAfterSecondtExit"
    CONDITION_AT_SECOND_EXIT = "conditionAtSecondExit"
    RESTRICTION_ON_CURRENT_SECTION_AFTER_NEXT_EXIT = "restrictionOnCurrentSectionAfterNextExit"
    RESTRICTION_AT_NEXT_EXIT = "restrictionAtNextExit"
    RESTRICTION_ON_CURRENT_SECTION_AFTER_SECOND_EXIT = "restrictionOnCurrentSectionAfterSecondExit"
    RESTRICTION_AT_SECONDT_EXIT = "restrictionAtSecondtExit"
    EXTENDED = "_extended"


class DedicatedUsageEnum1(Enum):
    """
    Type of usage for which a VMS is dedicated.

    :cvar ENERGY_INFORMATION: Dedicated to displaying energy information
    :cvar INSPECTION_AREA: Dedicated to an inspection area
    :cvar LANE_CONTROL_SYSTEM: Dedicated to the purpose of lane control
    :cvar PARKING_INFORMATION: Dedicated to displaying parking
        information
    :cvar RAMP_METERING: Dedicated to ramp metering
    :cvar TUNNEL_MANAGEMENT: Dedicated to tunnel management
    :cvar OTHER: Other dedicated usage
    :cvar EXTENDED:
    """
    ENERGY_INFORMATION = "energyInformation"
    INSPECTION_AREA = "inspectionArea"
    LANE_CONTROL_SYSTEM = "laneControlSystem"
    PARKING_INFORMATION = "parkingInformation"
    RAMP_METERING = "rampMetering"
    TUNNEL_MANAGEMENT = "tunnelManagement"
    OTHER = "other"
    EXTENDED = "_extended"


class DisplayedNumericalInformationTypeEnum1(Enum):
    """
    Type of numerical information displayed.

    :cvar DISTANCE: A distance
    :cvar HEIGHT: A height e.g. for a vehicle height restriction
    :cvar LENGTH: A length e.g. for a vehicle length restriction
    :cvar RATE_OF_INCLINE: A rate of incline
    :cvar SECTION_LENGTH: A road section length
    :cvar SPEED: A speed e.g. for a vehicle speed limit
    :cvar WEIGHT: A weight e.g. for a vehicle weight restriction
    :cvar WEIGHT_PER_AXLE: An axle weight e.g. for an axle weight
        restriction
    :cvar WIDTH: A width e.g. for a vehicle width restriction
    :cvar EXTENDED:
    """
    DISTANCE = "distance"
    HEIGHT = "height"
    LENGTH = "length"
    RATE_OF_INCLINE = "rateOfIncline"
    SECTION_LENGTH = "sectionLength"
    SPEED = "speed"
    WEIGHT = "weight"
    WEIGHT_PER_AXLE = "weightPerAxle"
    WIDTH = "width"
    EXTENDED = "_extended"


class GddServiceCategoryEnum1(Enum):
    """
    Type of service offered by the pictogram, as defined in ISO 14823 Graphic
    Data Dictionary (GDD)

    :cvar DANGER_WARNING: Danger warning sign information (GDD service
        category 11).
    :cvar REGULATORY: Informing of special obligations, restrictions or
        prohibitions (GDD service category 12).
    :cvar INFORMATIVE: Informative, advisory, or guiding (GDD service
        category 13).
    :cvar PUBLIC_FACILITIES: Informing of a certain public facility and
        its service (GDD service category 21).
    :cvar AMBIENT_CONDITIONS: Notifying of road-related ambient
        conditions and events on route (GDD service category 31).
    :cvar ROAD_CONDITIONS: Notifying of road-related conditions and
        events on route (GDD service category 32).
    :cvar EXTENDED:
    """
    DANGER_WARNING = "dangerWarning"
    REGULATORY = "regulatory"
    INFORMATIVE = "informative"
    PUBLIC_FACILITIES = "publicFacilities"
    AMBIENT_CONDITIONS = "ambientConditions"
    ROAD_CONDITIONS = "roadConditions"
    EXTENDED = "_extended"


class ImageFormatEnum1(Enum):
    """
    Identifies an image format.

    :cvar BMP: The bmp image format
    :cvar GIF: The gif image format
    :cvar JPEG: The jpeg image format
    :cvar PNG: The png image format
    :cvar TIFF: The TIFF image format
    :cvar EXTENDED:
    """
    BMP = "bmp"
    GIF = "gif"
    JPEG = "jpeg"
    PNG = "png"
    TIFF = "tiff"
    EXTENDED = "_extended"


class InformationTypeEnum1(Enum):
    """
    Type of text characterisation.

    :cvar SITUATION_INFORMATION: Information about the situation
    :cvar WARNING: The information is a warning
    :cvar PROHIBITION: The information is a prohibition
    :cvar OBLIGATION: The information is an obligation
    :cvar DESTINATION: The information is a destination
    :cvar TRAVEL_TIME: The information is travel time
    :cvar DELAY: Delay information
    :cvar LOCATION: Location information
    :cvar VEHICLE_TYPE: The information is about vehicle type
    :cvar GENERAL_INFORMATION: General information
    :cvar BLANK: There is no information content
    :cvar OTHER: Other kind of information
    :cvar EXTENDED:
    """
    SITUATION_INFORMATION = "situationInformation"
    WARNING = "warning"
    PROHIBITION = "prohibition"
    OBLIGATION = "obligation"
    DESTINATION = "destination"
    TRAVEL_TIME = "travelTime"
    DELAY = "delay"
    LOCATION = "location"
    VEHICLE_TYPE = "vehicleType"
    GENERAL_INFORMATION = "generalInformation"
    BLANK = "blank"
    OTHER = "other"
    EXTENDED = "_extended"


class MessageInformationTypeEnum1(Enum):
    """
    Types of information displayable on a VMS.

    :cvar CAMPAIGN_MESSAGE: Campaign type information which is non time
        specific that may request certain actions (e.g. "do not drink
        and drive") or which is intended to influence drivers'
        behaviour.
    :cvar DATE_TIME: Current date and/or time information.
    :cvar FUTURE_INFORMATION: Information which informs road users about
        future situations which can potentially cause congestion or
        influence future travel plans (e.g. future roadworks, closures,
        sporting events, public concerts, suspension of train or ferry
        services).
    :cvar INSTRUCTION_OR_MESSAGE: Instructions or messages to road users
        which are relevant at the current time, (e.g. "do not throw out
        any burning objects" or an Amber alert message).
    :cvar SITUATION_WARNING: Information warning of a current situation
        likely to affect traffic on the road ahead.
    :cvar TEMPERATURE: Temperature information.
    :cvar TRAFFIC_MANAGEMENT: Information comprising traffic management
        instructions.
    :cvar TRAVEL_TIME: Travel time information.
    :cvar EXTENDED:
    """
    CAMPAIGN_MESSAGE = "campaignMessage"
    DATE_TIME = "dateTime"
    FUTURE_INFORMATION = "futureInformation"
    INSTRUCTION_OR_MESSAGE = "instructionOrMessage"
    SITUATION_WARNING = "situationWarning"
    TEMPERATURE = "temperature"
    TRAFFIC_MANAGEMENT = "trafficManagement"
    TRAVEL_TIME = "travelTime"
    EXTENDED = "_extended"


class PhysicalSupportEnum1(Enum):
    """
    The ways in which equipments such as VMS are mounted or deployed on the
    road.

    :cvar CENTRAL_RESERVATION_MOUNTED: Equipment mounted in the central
        reservation.
    :cvar GANTRY_MOUNTED: Equipment mounted on an overhead gantry across
        the carriageway.
    :cvar OVERHEAD_BRIDGE_MOUNTED: Equipment mounted overhead on a
        bridge structure.
    :cvar ROADSIDE_CANTILEVER_MOUNTED: Equipment mounted on a cantilever
        from the roadside.
    :cvar ROADSIDE_MOUNTED: Equipment mounted at the roadside.
    :cvar TRAILER_MOUNTED: Equipment mounted on a movable trailer.
    :cvar TUNNEL_ENTRANCE_MOUNTED: Equipment mounted on the entrance to
        a tunnel.
    :cvar VEHICLE_MOUNTED: Equipment mounted on a vehicle.
    :cvar EXTENDED:
    """
    CENTRAL_RESERVATION_MOUNTED = "centralReservationMounted"
    GANTRY_MOUNTED = "gantryMounted"
    OVERHEAD_BRIDGE_MOUNTED = "overheadBridgeMounted"
    ROADSIDE_CANTILEVER_MOUNTED = "roadsideCantileverMounted"
    ROADSIDE_MOUNTED = "roadsideMounted"
    TRAILER_MOUNTED = "trailerMounted"
    TUNNEL_ENTRANCE_MOUNTED = "tunnelEntranceMounted"
    VEHICLE_MOUNTED = "vehicleMounted"
    EXTENDED = "_extended"


class PictogramEnum1(Enum):
    """
    Types of pictogram not currently covered by ISO 14823 Graphic Data
    Dictionary.

    :cvar BLANK_VOID: Blank or void.
    :cvar BRIDGE_CLOSED: Bridge closed.
    :cvar CAR_PARK_FULL: Car park full.
    :cvar CAR_PARK_SPACES_AVAILABLE: Spaces available in car park.
    :cvar CORRIDOR_FOR_EMERGENCY_VEHICLE_ACCESS: Corridor for emergency
        vehicle access
    :cvar CURVE_ARROW_TO_LEFT: Single curve arrow to the leftt
        corresponding to an exit (without fork).
    :cvar CURVE_ARROW_TO_RIGHT: Single curve arrow to the right
        corresponding to an exit (without fork).
    :cvar DANGER_OF_FIRE: Danger of fire.
    :cvar DOUBLE_EXIT_TO_LEFT: Triple arrow corresponding to two
        sequential exits to the left.
    :cvar DOUBLE_EXIT_TO_RIGHT: Triple arrow corresponding to two
        sequential exits to the right.
    :cvar END_OF_ADVISORY_SPEED: End of advisory speed.
    :cvar FASTEN_CHILDRENS_SEAT_BELTS: Fasten the seat belts of
        children.
    :cvar FASTEN_YOUR_SEAT_BELT: Fasten your seat belt.
    :cvar FIRE: Fire.
    :cvar FOOTBALL_MATCH: Football match (current or anticipated
        disruption due to football match).
    :cvar HARD_SHOULDER_NOT_RUNNING: Hard shoulder running is in
        operation.
    :cvar HARD_SHOULDER_RUNNING: Hard shoulder running is not in
        operation.
    :cvar HORIZONTAL_DIVERSION_TO_LEFT: Correspond to the horizontal
        orange (to the left) sign for diversion
    :cvar HORIZONTAL_DIVERSION_TO_RIGHT: Correspond to the horizontal
        orange (to the right) sign for diversion
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
    :cvar LEFT_HAND_LANE_CLOSED: Left-hand lane closed ahead.
    :cvar NARROW_LANES_AHEAD: Narrow lanes ahead.
    :cvar OBLIQUE_ARROW_TO_LEFT: Single oblique straight arrow to the
        left corresponding to an exit (without fork).
    :cvar OBLIQUE_ARROW_TO_RIGHT: Single oblique straight arrow to the
        right corresponding to an exit (without fork).
    :cvar POLLUTION_OR_SMOG_ALERT: Pollution or smog alert.
    :cvar RIGHT_HAND_LANE_CLOSED: Right-hand lane closed ahead.
    :cvar SINGLE_EXIT_TO_LEFT: Double arrow corresponding to a single
        exit to the left.
    :cvar SINGLE_EXIT_TO_RIGHT: Double arrow corresponding to a single
        exit to the right.
    :cvar SMOKE: Smoke.
    :cvar SNOW_PLOUGH_IN_ACTION: Snow plough(s) in action.
    :cvar SPEED_CAMERAS_IN_ACTION: Speed cameras in action.
    :cvar STRAIGHT_VERTICAL_ARROW: Straight vertical arrow (towards
        top).
    :cvar TRAFFIC_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD: All traffic is
        diverted to the opposite carriageway ahead in a contraflow
        layout.
    :cvar TRAFFIC_PARTIALLY_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD:
        Traffic is partially diverted to the opposite carriageway ahead
        in a contraflow layout.
    :cvar TUNNEL_CLOSED: Tunnel closed.
    :cvar VERTICAL_DIVERSION: Correspond to the vertical orange sign for
        diversion.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    BLANK_VOID = "blankVoid"
    BRIDGE_CLOSED = "bridgeClosed"
    CAR_PARK_FULL = "carParkFull"
    CAR_PARK_SPACES_AVAILABLE = "carParkSpacesAvailable"
    CORRIDOR_FOR_EMERGENCY_VEHICLE_ACCESS = "corridorForEmergencyVehicleAccess"
    CURVE_ARROW_TO_LEFT = "curveArrowToLeft"
    CURVE_ARROW_TO_RIGHT = "curveArrowToRight"
    DANGER_OF_FIRE = "dangerOfFire"
    DOUBLE_EXIT_TO_LEFT = "doubleExitToLeft"
    DOUBLE_EXIT_TO_RIGHT = "doubleExitToRight"
    END_OF_ADVISORY_SPEED = "endOfAdvisorySpeed"
    FASTEN_CHILDRENS_SEAT_BELTS = "fastenChildrensSeatBelts"
    FASTEN_YOUR_SEAT_BELT = "fastenYourSeatBelt"
    FIRE = "fire"
    FOOTBALL_MATCH = "footballMatch"
    HARD_SHOULDER_NOT_RUNNING = "hardShoulderNotRunning"
    HARD_SHOULDER_RUNNING = "hardShoulderRunning"
    HORIZONTAL_DIVERSION_TO_LEFT = "horizontalDiversionToLeft"
    HORIZONTAL_DIVERSION_TO_RIGHT = "horizontalDiversionToRight"
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
    LEFT_HAND_LANE_CLOSED = "leftHandLaneClosed"
    NARROW_LANES_AHEAD = "narrowLanesAhead"
    OBLIQUE_ARROW_TO_LEFT = "obliqueArrowToLeft"
    OBLIQUE_ARROW_TO_RIGHT = "obliqueArrowToRight"
    POLLUTION_OR_SMOG_ALERT = "pollutionOrSmogAlert"
    RIGHT_HAND_LANE_CLOSED = "rightHandLaneClosed"
    SINGLE_EXIT_TO_LEFT = "singleExitToLeft"
    SINGLE_EXIT_TO_RIGHT = "singleExitToRight"
    SMOKE = "smoke"
    SNOW_PLOUGH_IN_ACTION = "snowPloughInAction"
    SPEED_CAMERAS_IN_ACTION = "speedCamerasInAction"
    STRAIGHT_VERTICAL_ARROW = "straightVerticalArrow"
    TRAFFIC_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD = "trafficDeviatedToOppositeCarriagewayAhead"
    TRAFFIC_PARTIALLY_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD = "trafficPartiallyDeviatedToOppositeCarriagewayAhead"
    TUNNEL_CLOSED = "tunnelClosed"
    VERTICAL_DIVERSION = "verticalDiversion"
    OTHER = "other"
    EXTENDED = "_extended"


class PositionXAbsoluteEnum1(Enum):
    """
    Absolute horizontal positions of an item within an assigned space.

    :cvar ON_LEFT: On the left of the assigned space.
    :cvar IN_THE_MIDDLE: In the middle of the assigned space.
    :cvar ON_RIGHT: On the right of the assigned space.
    :cvar EXTENDED:
    """
    ON_LEFT = "onLeft"
    IN_THE_MIDDLE = "inTheMiddle"
    ON_RIGHT = "onRight"
    EXTENDED = "_extended"


class PositionXRelativeEnum1(Enum):
    """
    Relative horizontal positions of one item to another.

    :cvar TO_THE_LEFT: Positioned to the left of relative item.
    :cvar ALIGNED_ON_THE_LEFT_SIDE: The left side of the area is aligned
        on the left side of the relative area.
    :cvar CENTRED: The area is vertically centred on the relative area.
    :cvar ALIGNED_ON_THE_RIGHT_SIDE: The right side of the area is
        aligned on the right side of the relative area.
    :cvar TO_THE_RIGHT: Positioned to the right of relative item.
    :cvar EXTENDED:
    """
    TO_THE_LEFT = "toTheLeft"
    ALIGNED_ON_THE_LEFT_SIDE = "alignedOnTheLeftSide"
    CENTRED = "centred"
    ALIGNED_ON_THE_RIGHT_SIDE = "alignedOnTheRightSide"
    TO_THE_RIGHT = "toTheRight"
    EXTENDED = "_extended"


class PositionYAbsoluteEnum1(Enum):
    """
    Absolute verticals positions of an item within an assigned space.

    :cvar AT_TOP: At the top of the assigned space.
    :cvar IN_THE_MIDDLE: In the middle of the assigned space.
    :cvar AT_BOTTOM: At the bottom of the assigned space.
    :cvar EXTENDED:
    """
    AT_TOP = "atTop"
    IN_THE_MIDDLE = "inTheMiddle"
    AT_BOTTOM = "atBottom"
    EXTENDED = "_extended"


class PositionYRelativeEnum1(Enum):
    """
    Relative vertical positions of one item to another.

    :cvar ABOVE: Positioned above relative item.
    :cvar ALIGNED_ON_THE_TOP_SIDE: The top side of the area is aligned
        on the top side of the relative area.
    :cvar CENTRED: The area is horizontally centred on the relative
        area.
    :cvar ALIGNED_ON_THE_BOTTOM_SIDE: The bottom side of the area is
        aligned on the bottom side of the relative area.
    :cvar BELOW: Positioned below relative item.
    :cvar EXTENDED:
    """
    ABOVE = "above"
    ALIGNED_ON_THE_TOP_SIDE = "alignedOnTheTopSide"
    CENTRED = "centred"
    ALIGNED_ON_THE_BOTTOM_SIDE = "alignedOnTheBottomSide"
    BELOW = "below"
    EXTENDED = "_extended"


class SettingReasonEnum1(Enum):
    """
    Coded reasons why a message has been selected for display on the sign.

    :cvar SITUATION: Message selected as the result of a situation
        occuring either on or off the road which might affect road
        users.
    :cvar OPERATOR_CREATED: Message selected by operator as the result
        of an unmanaged event or situation.
    :cvar TRAFFIC_MANAGEMENT: Message selected as part of the
        implementation of a traffic management action. This can be part
        of a specific traffic management or diversion plan.
    :cvar TRAVEL_TIME: The VMS is currently selected to display travel
        times.
    :cvar CAMPAIGN: The VMS is currently selected to display a campaign
        message.
    :cvar DEFAULT: The VMS is currently selected to display default
        information (e.g. time, date, temperature).
    :cvar EXTENDED:
    """
    SITUATION = "situation"
    OPERATOR_CREATED = "operatorCreated"
    TRAFFIC_MANAGEMENT = "trafficManagement"
    TRAVEL_TIME = "travelTime"
    CAMPAIGN = "campaign"
    DEFAULT = "default"
    EXTENDED = "_extended"


class SupplementalPictogramEnum1(Enum):
    """
    Types of pictograms displayable in supplementary panels (normally below the
    main pictogram display which it qualifies).

    :cvar DISTANCE_TO_THE_BEGINNING_OF_THE_APPLICATION_ZONE: Distance to
        the beginning of the application zone.
    :cvar EXCEPT_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER: Except any
        power-driven vehicle drawing a trailer.
    :cvar EXCEPT_BUS: Except for buses.
    :cvar EXCEPT_GOODS_VEHICLES: Except for goods vehicles.
    :cvar EXCEPT_SEMITRAILER: Except for semitrailers (i.e. any trailer
        designed to be coupled to a motor vehicle in such a way that
        part of its weight and that of its load is borne by the motor
        vehicle).
    :cvar EXCEPT_VEHICLES_CARRYING_DANGEROUS_GOODS: Except for vehicles
        carrying dangerous goods (i.e. for which special sign plating is
        prescribed).
    :cvar IN_CASE_OF_ICE_OR_SNOW: In case of ice or snow.
    :cvar LENGTH_OF_THE_APPLICATION_ZONE: Length of the applicable zone.
    :cvar RESTRICTED_TO_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER:
        Restricted to any power driven vehicle drawing a trailer.
    :cvar RESTRICTED_TO_BUS: Restricted to buses.
    :cvar RESTRICTED_TO_GOODS_VEHICLES: Restricted to goods vehicles.
    :cvar RESTRICTED_TO_SEMI_TRAILER: Restricted to semi trailers (i.e.
        any trailer designed to be coupled to a motor vehicle in such a
        way that part of its weight and that of its load is borne by the
        motor vehicle).
    :cvar RESTRICTED_TO_VEHICLES_CARRYING_DANGEROUS_GOODS: Restricted to
        vehicles carrying dangerous goods (i.e. for which special sign
        plating is prescribed).
    :cvar MAINTENANCE_VEHICLES: Maintenance vehicles.
    :cvar SNOW_PLOUGHS: Snow ploughs.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    DISTANCE_TO_THE_BEGINNING_OF_THE_APPLICATION_ZONE = "distanceToTheBeginningOfTheApplicationZone"
    EXCEPT_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER = "exceptAnyPowerDrivenVehicleDrawingTrailer"
    EXCEPT_BUS = "exceptBus"
    EXCEPT_GOODS_VEHICLES = "exceptGoodsVehicles"
    EXCEPT_SEMITRAILER = "exceptSemitrailer"
    EXCEPT_VEHICLES_CARRYING_DANGEROUS_GOODS = "exceptVehiclesCarryingDangerousGoods"
    IN_CASE_OF_ICE_OR_SNOW = "inCaseOfIceOrSnow"
    LENGTH_OF_THE_APPLICATION_ZONE = "lengthOfTheApplicationZone"
    RESTRICTED_TO_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER = "restrictedToAnyPowerDrivenVehicleDrawingTrailer"
    RESTRICTED_TO_BUS = "restrictedToBus"
    RESTRICTED_TO_GOODS_VEHICLES = "restrictedToGoodsVehicles"
    RESTRICTED_TO_SEMI_TRAILER = "restrictedToSemiTrailer"
    RESTRICTED_TO_VEHICLES_CARRYING_DANGEROUS_GOODS = "restrictedToVehiclesCarryingDangerousGoods"
    MAINTENANCE_VEHICLES = "maintenanceVehicles"
    SNOW_PLOUGHS = "snowPloughs"
    OTHER = "other"
    EXTENDED = "_extended"


class UnitOfMeasureEnum1(Enum):
    """
    Identifies a unit of measure for a physical quantity.

    :cvar FEET: The imperial unit feet
    :cvar FEET_AND_INCHES: The imperial units feet and inches
    :cvar KILOMETRES: The metric unit kilometres
    :cvar KILOMETRES_PER_HOUR: The unit kilometres per hour
    :cvar METRES: The metric unit metres
    :cvar MILES: The imperial unit miles
    :cvar MILES_PER_HOUR: The unit miles per hour
    :cvar PERCENTAGE: A percentage
    :cvar TONNES: The metric unit tonnes
    :cvar YARDS: The imperial unit yards
    :cvar EXTENDED:
    """
    FEET = "feet"
    FEET_AND_INCHES = "feetAndInches"
    KILOMETRES = "kilometres"
    KILOMETRES_PER_HOUR = "kilometresPerHour"
    METRES = "metres"
    MILES = "miles"
    MILES_PER_HOUR = "milesPerHour"
    PERCENTAGE = "percentage"
    TONNES = "tonnes"
    YARDS = "yards"
    EXTENDED = "_extended"


class VmsControllerFaultEnum1(Enum):
    """
    Types of variable message sign controller faults.

    :cvar COMMUNICATIONS_FAILURE: Comunications failure affecting VMS
        controller
    :cvar POWER_FAILURE: Power to VMS controller has failed.
    :cvar UNKNOWN: unknown
    :cvar OTHER: unknown
    :cvar EXTENDED:
    """
    COMMUNICATIONS_FAILURE = "communicationsFailure"
    POWER_FAILURE = "powerFailure"
    UNKNOWN = "unknown"
    OTHER = "other"
    EXTENDED = "_extended"


class VmsFaultEnum1(Enum):
    """
    Types of variable message sign faults.

    :cvar INCORRECT_MESSAGE_DISPLAYED: Incorrect message is being
        displayed.
    :cvar INCORRECT_PICTOGRAM_DISPLAYED: Incorrect pictogram is being
        displayed.
    :cvar OUT_OF_SERVICE: Not currently in service (e.g. intentionally
        disconnected or switched off during roadworks).
    :cvar UNABLE_TO_CLEAR_DOWN: Unable to clear down information
        displayed on VMS.
    :cvar UNKNOWN: Unknown VMS fault.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    INCORRECT_MESSAGE_DISPLAYED = "incorrectMessageDisplayed"
    INCORRECT_PICTOGRAM_DISPLAYED = "incorrectPictogramDisplayed"
    OUT_OF_SERVICE = "outOfService"
    UNABLE_TO_CLEAR_DOWN = "unableToClearDown"
    UNKNOWN = "unknown"
    OTHER = "other"
    EXTENDED = "_extended"


class VmsTypeEnum1(Enum):
    """
    Type of variable message sign.

    :cvar COLOUR_GRAPHIC: A colour graphic display.
    :cvar ROTATING_PRISM_SIGN: A sign implementing fixed messages which
        are made visible to drivers by electromechanical means e.g. a
        fixed sign parallel to traffic flow and therefore not legible is
        rotated to be orthogonal to traffic flow and becomes legible.
    :cvar MONOCHROME_GRAPHIC: A monochrome graphic display.
    :cvar SIMPLE_MATRIX_SIGN: Simple display made up of a fixed matrix
        of pixels (e.g. sets of LEDs or lights) capable of showing a
        limited set of aspects (or matrix images). The display area is
        regarded as a pictogram area in DATEX II.
    :cvar FULL_MATRIX_SIGN: A full-matrix sign.
    :cvar ROLLER_BLIND_SIGN: Continuous sign using a roller blind.
    :cvar VIRTUAL_VMS: Not a physical VMS but a conceptual one used in
        the electronic distribution of information
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    COLOUR_GRAPHIC = "colourGraphic"
    ROTATING_PRISM_SIGN = "rotatingPrismSign"
    MONOCHROME_GRAPHIC = "monochromeGraphic"
    SIMPLE_MATRIX_SIGN = "simpleMatrixSign"
    FULL_MATRIX_SIGN = "fullMatrixSign"
    ROLLER_BLIND_SIGN = "rollerBlindSign"
    VIRTUAL_VMS = "virtualVms"
    OTHER = "other"
    EXTENDED = "_extended"


class WorkingStatusEnum1(Enum):
    """
    Identifies the working status of a VMS.

    :cvar BLANK: The VMS is blank
    :cvar COVERED: The VMS is physically covered so no messages can be
        seen.
    :cvar NOT_WORKING: The VMS is not working
    :cvar WORKING: The VMS is working
    :cvar EXTENDED:
    """
    BLANK = "blank"
    COVERED = "covered"
    NOT_WORKING = "notWorking"
    WORKING = "working"
    EXTENDED = "_extended"


@dataclass
class DisplayAreaSettings:
    """
    A display of pictograms or text on one area on a VMS.

    :ivar is_blank: Identifies whether this display area is blank. The
        absense of this attribute has no semantics.
    :ivar legally_binding: The semantics of this display are legally
        binding for road users
    :ivar legal_basis: Identies any legal basis for the elements
        displayed
    :ivar display_area_settings_extension:
    """
    is_blank: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isBlank",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    legally_binding: Optional[bool] = field(
        default=None,
        metadata={
            "name": "legallyBinding",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    legal_basis: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "legalBasis",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_area_settings_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_displayAreaSettingsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class DisplayGeometry:
    """
    Characteristics of the geometry of a display.

    :ivar pixels_across: Number of pixels horizontally across the
        display area.
    :ivar pixels_down: Number of pixels vertically down the display
        area.
    :ivar display_height: The vertical height measured in metres of the
        display area.
    :ivar display_width: The horizontal width measured in metres of the
        display area.
    :ivar position_x: The X-coordinate (horizontal) position of this
        specific display area measured from the top left of the sign's
        overall display area to the top left of this specific display
        area
    :ivar position_y: The Y-coordinate (vertical) position of this
        specific display area measured from the top left of the sign's
        overall display area to the top left of this specific display
        area
    :ivar display_geometry_extension:
    """
    pixels_across: Optional[int] = field(
        default=None,
        metadata={
            "name": "pixelsAcross",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pixels_down: Optional[int] = field(
        default=None,
        metadata={
            "name": "pixelsDown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "displayHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "displayWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    position_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "positionX",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    position_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "positionY",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_geometry_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_displayGeometryExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class GddPictogramAttributes:
    """
    ISO 14823 Graphic Data Dictionary attributes with textual or numeric data
    to supplement a pictogram identification.

    :ivar attributes: ISO 14823 "attributes" data frame which augments
        the basic identification of the type of pictogram with further
        textual or numeric data. The encoding shall follow unaligned
        packed encoding rules (UPER) [ISO/IEC 8825-2:2015]
    :ivar gdd_pictogram_attributes_extension:
    """
    attributes: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
            "format": "base64",
        }
    )
    gdd_pictogram_attributes_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_gddPictogramAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class ManagedLogicalLocation:
    """
    The logical location (e.g. a car park, a section of road, a junction etc.)
    which a VMS contributes to the management of.

    :ivar managed_logical_location: Identification of the logical
        location (e.g. a car park, a section of road , a junction etc.)
        which this sign contributes to the management of.
    :ivar distance_from_logical_location: Distance in metres of the VMS
        from the logical location which this sign contributes to the
        management of.
    :ivar managed_location: The location which is managed by the
        variable message sign, such as the location of a junction or a
        car park.
    :ivar managed_logical_location_extension:
    """
    managed_logical_location: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "managedLogicalLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    distance_from_logical_location: Optional[int] = field(
        default=None,
        metadata={
            "name": "distanceFromLogicalLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    managed_location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "managedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    managed_logical_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_managedLogicalLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class ColourEnum2:
    class Meta:
        name = "_ColourEnum"

    value: Optional[ColourEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class CompositePictogramEnum2:
    class Meta:
        name = "_CompositePictogramEnum"

    value: Optional[CompositePictogramEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class DedicatedUsageEnum2:
    class Meta:
        name = "_DedicatedUsageEnum"

    value: Optional[DedicatedUsageEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class DisplayedNumericalInformationTypeEnum2:
    class Meta:
        name = "_DisplayedNumericalInformationTypeEnum"

    value: Optional[DisplayedNumericalInformationTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class GddServiceCategoryEnum2:
    class Meta:
        name = "_GddServiceCategoryEnum"

    value: Optional[GddServiceCategoryEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class ImageFormatEnum2:
    class Meta:
        name = "_ImageFormatEnum"

    value: Optional[ImageFormatEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class InformationTypeEnum2:
    class Meta:
        name = "_InformationTypeEnum"

    value: Optional[InformationTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class MessageInformationTypeEnum2:
    class Meta:
        name = "_MessageInformationTypeEnum"

    value: Optional[MessageInformationTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PhysicalSupportEnum2:
    class Meta:
        name = "_PhysicalSupportEnum"

    value: Optional[PhysicalSupportEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PictogramEnum2:
    class Meta:
        name = "_PictogramEnum"

    value: Optional[PictogramEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PositionXAbsoluteEnum2:
    class Meta:
        name = "_PositionXAbsoluteEnum"

    value: Optional[PositionXAbsoluteEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PositionXRelativeEnum2:
    class Meta:
        name = "_PositionXRelativeEnum"

    value: Optional[PositionXRelativeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PositionYAbsoluteEnum2:
    class Meta:
        name = "_PositionYAbsoluteEnum"

    value: Optional[PositionYAbsoluteEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PositionYRelativeEnum2:
    class Meta:
        name = "_PositionYRelativeEnum"

    value: Optional[PositionYRelativeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class SettingReasonEnum2:
    class Meta:
        name = "_SettingReasonEnum"

    value: Optional[SettingReasonEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class SituationRecordVersionedReference(VersionedReference):
    class Meta:
        name = "_SituationRecordVersionedReference"

    target_class: str = field(
        init=False,
        default="sit:SituationRecord",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SituationVersionedReference(VersionedReference):
    class Meta:
        name = "_SituationVersionedReference"

    target_class: str = field(
        init=False,
        default="sit:Situation",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SupplementalPictogramEnum2:
    class Meta:
        name = "_SupplementalPictogramEnum"

    value: Optional[SupplementalPictogramEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class UnitOfMeasureEnum2:
    class Meta:
        name = "_UnitOfMeasureEnum"

    value: Optional[UnitOfMeasureEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class VmsControllerFaultEnum2:
    class Meta:
        name = "_VmsControllerFaultEnum"

    value: Optional[VmsControllerFaultEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class VmsControllerTableVersionedReference(VersionedReference):
    class Meta:
        name = "_VmsControllerTableVersionedReference"

    target_class: str = field(
        init=False,
        default="vms:VmsControllerTable",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsControllerVersionedReference(VersionedReference):
    class Meta:
        name = "_VmsControllerVersionedReference"

    target_class: str = field(
        init=False,
        default="vms:VmsController",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsFaultEnum2:
    class Meta:
        name = "_VmsFaultEnum"

    value: Optional[VmsFaultEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class VmsTypeEnum2:
    class Meta:
        name = "_VmsTypeEnum"

    value: Optional[VmsTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class WorkingStatusEnum2:
    class Meta:
        name = "_WorkingStatusEnum"

    value: Optional[WorkingStatusEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class DisplayArea:
    """
    Configuration (static or dynamic) of a display area.

    :ivar sequencing_capable: Indicates whether the display area on the
        VMS is capable of sequencing through multiple pages. True =
        capable.
    :ivar max_number_of_sequential_pages: Maximum number of pages which
        the VMS is capable of scrolling through sequentially (2 to n).
    :ivar position_xabsolute: The horizontal position of the area in
        which the pictogram is displayed, i.e. at the left, or right of
        the VMS display.
    :ivar position_xrelative_to_previous: The horizontal position of the
        area in which the pictogram is displayed relative to the
        previous display in the collection (e.g. to the left, to the
        right ....).
    :ivar position_yabsolute: The vertical position of the area in which
        the area is displayed, i.e. at the top or bottom of the VMS
        display.
    :ivar position_yrelative_to_previous: The horizontal position of the
        area in which the pictogram is displayed relative to the
        previous display area in the collection (i.e.above or below).
    :ivar display_geometry:
    :ivar overridden_lane_association: The display area is associated
        with these lanes, which refine any location specified for the
        VMS
    :ivar display_area_extension:
    """
    sequencing_capable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "sequencingCapable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    max_number_of_sequential_pages: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxNumberOfSequentialPages",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    position_xabsolute: Optional[PositionXAbsoluteEnum2] = field(
        default=None,
        metadata={
            "name": "positionXAbsolute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    position_xrelative_to_previous: Optional[PositionXRelativeEnum2] = field(
        default=None,
        metadata={
            "name": "positionXRelativeToPrevious",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    position_yabsolute: Optional[PositionYAbsoluteEnum2] = field(
        default=None,
        metadata={
            "name": "positionYAbsolute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    position_yrelative_to_previous: Optional[PositionYRelativeEnum2] = field(
        default=None,
        metadata={
            "name": "positionYRelativeToPrevious",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_geometry: Optional[DisplayGeometry] = field(
        default=None,
        metadata={
            "name": "displayGeometry",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    overridden_lane_association: List[Lane] = field(
        default_factory=list,
        metadata={
            "name": "overriddenLaneAssociation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_displayAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class DisplayedNumericalInformation:
    """
    Numerical information displayed on a sign.

    :ivar numerical_information_type: Type of numerical information
        displayed
    :ivar numeric_value: The value displayed. In the special case where
        the unit of measure is feet and inches, the part of the number
        after the decimal separator is the number of inches.
    :ivar unit_of_measure: The unit of measure for the numeric value.
        This may be displayed or predefined for a type of sign.
    :ivar displayed_numerical_information_extension:
    """
    numerical_information_type: Optional[DisplayedNumericalInformationTypeEnum2] = field(
        default=None,
        metadata={
            "name": "numericalInformationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    numeric_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "numericValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    unit_of_measure: Optional[UnitOfMeasureEnum2] = field(
        default=None,
        metadata={
            "name": "unitOfMeasure",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    displayed_numerical_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_displayedNumericalInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class GddPictogramIdentification:
    """
    Group of codes that uniquely identifies a kind of pictogram, according to
    the ISO 14823 Graphic Data Dictionary.

    :ivar country: Country code used to either allow associating a
        country-specific rendering with the coded pictogram or
        distinguish nationally-defined pictogram codes.
    :ivar service_category: Category used to group pictograms for a
        given usage
    :ivar pictogram_category_code: Code that identifies a pictogram for
        a given country and service category.
    :ivar gdd_pictogram_identification_extension:
    """
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
            "max_length": 2,
        }
    )
    service_category: Optional[GddServiceCategoryEnum2] = field(
        default=None,
        metadata={
            "name": "serviceCategory",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    pictogram_category_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramCategoryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    gdd_pictogram_identification_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_gddPictogramIdentificationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class Image:
    """
    An image, with encoded data and identification of format.

    :ivar image_data: Encoded image data
    :ivar image_format: Identifies the image format of the associated
        image data
    :ivar image_extension:
    """
    image_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "imageData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
            "format": "base64",
        }
    )
    image_format: Optional[ImageFormatEnum2] = field(
        default=None,
        metadata={
            "name": "imageFormat",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    image_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_imageExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class SupplementaryInformationDisplay(DisplayAreaSettings):
    """
    A display of information or a regulatory instruction which is supplemental
    to the associated pictogram, comprising either an additional line of text
    or a pictogram or both.
    """
    supplementary_information_display_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_supplementaryInformationDisplayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class TextLine:
    """A single line of text displayed on a text display area or supplementary
    panel or corresponding to a displayed text.

    It may correspond to the entire text in the case that text
    segmentation in lines is not available.

    :ivar text_line: A free-text string that is displayed on a single
        line on the text display area. It may correspond to the entire
        text in the case that text segmentation in lines is not
        available.
    :ivar line_colour: The colour of the displayed text.
    :ivar line_flashing: Indication of whether the displayed text is
        flashing.
    :ivar line_html: The displayed line of text defined by an HTML
        string showing text formatting tags.
    :ivar is_exact_text_on_sign: Confirms whether the specified text is
        exactly as displayed, or whether it is just a semantic
        equivalent.
    :ivar text_information_type: Allows characterising the type of of
        displayed information
    :ivar text_line_extension:
    :ivar line_language: The language of the displayed text, specified
        by an ISO 639-1 language code.
    """
    text_line: Optional[str] = field(
        default=None,
        metadata={
            "name": "textLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
            "max_length": 1024,
        }
    )
    line_colour: Optional[ColourEnum2] = field(
        default=None,
        metadata={
            "name": "lineColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    line_flashing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "lineFlashing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    line_html: Optional[str] = field(
        default=None,
        metadata={
            "name": "lineHtml",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    is_exact_text_on_sign: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isExactTextOnSign",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    text_information_type: List[InformationTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "textInformationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    text_line_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_textLineExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    line_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "lineLanguage",
            "type": "Attribute",
        }
    )


@dataclass
class VmsControllerFault(Fault):
    """
    Details of the fault which is being reported for the specified variable
    message sign control unit.

    :ivar vms_controller_fault: The type of fault which is being
        reported for the VMS unit.
    :ivar vms_controller_fault_extension:
    """
    vms_controller_fault: Optional[VmsControllerFaultEnum2] = field(
        default=None,
        metadata={
            "name": "vmsControllerFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    vms_controller_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsControllerFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class VmsFault(Fault):
    """
    Details of the fault which is being reported for the specified variable
    message sign panel.

    :ivar vms_fault: The type of fault which is being reported for the
        specified variable message sign panel.
    :ivar vms_fault_extension:
    """
    vms_fault: Optional[VmsFaultEnum2] = field(
        default=None,
        metadata={
            "name": "vmsFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    vms_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class MultiPageDisplayPageNumberDisplayAreaSettings:
    class Meta:
        name = "_MultiPageDisplayPageNumberDisplayAreaSettings"

    display_area_settings: Optional[DisplayAreaSettings] = field(
        default=None,
        metadata={
            "name": "displayAreaSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    page_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "pageNumber",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsMessageDisplayAreaIndexDisplayAreaSettings:
    class Meta:
        name = "_VmsMessageDisplayAreaIndexDisplayAreaSettings"

    display_area_settings: Optional[DisplayAreaSettings] = field(
        default=None,
        metadata={
            "name": "displayAreaSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    display_area_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "displayAreaIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class GddStructure:
    """
    Graphic Data Dictionary structure, to identify a pictogram by code and
    optional supplementary attributes.
    """
    gdd_pictogram_identification: Optional[GddPictogramIdentification] = field(
        default=None,
        metadata={
            "name": "gddPictogramIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    gdd_pictogram_attributes: Optional[GddPictogramAttributes] = field(
        default=None,
        metadata={
            "name": "gddPictogramAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    gdd_structure_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_gddStructureExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class MultiPageDisplay(DisplayAreaSettings):
    """
    A display of multiple pages, sequentially displayed in order of their
    "pageNumber".

    :ivar sequence_group_number: Where MultiPageDisplay instances have
        the same sequenceGroupNumber, the timed progression through
        their pages is synchronised.
    :ivar display_area_settings:
    :ivar multi_page_display_extension:
    """
    sequence_group_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceGroupNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_area_settings: List[MultiPageDisplayPageNumberDisplayAreaSettings] = field(
        default_factory=list,
        metadata={
            "name": "displayAreaSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    multi_page_display_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_multiPageDisplayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class PictogramDisplayArea(DisplayArea):
    """
    Characteristics specific to a pictogram display area on the VMS.

    :ivar pictogram_code_list_identifier: Indicates which pictogram code
        list is referenced. This may be ISO 14823 or a custom list.
    :ivar pictogram_number_of_colours: The number of colours the
        pictogram display area is capable of rendering.
    :ivar pictogram_display_area_extension:
    """
    pictogram_code_list_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictogramCodeListIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    pictogram_number_of_colours: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramNumberOfColours",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram_display_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pictogramDisplayAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class SupplementaryPanelArea(DisplayArea):
    """
    Characteristics of a panel which can display details (sometimes regulatory
    in nature) that are supplementary to one pictogram, comprising an
    additional line of text or another pictogram.

    :ivar supplementary_pictogram_code_list_identifier: Indicates which
        supplementary pictogram code list is referenced. This may be ISO
        14823 or a custom list.
    :ivar related_pictogram_area: The displayAreaIndex associated with
        the pictogram display area that this supplementary display area
        is designed to supplement.
    :ivar supplementary_panel_area_extension:
    """
    supplementary_pictogram_code_list_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "supplementaryPictogramCodeListIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    related_pictogram_area: Optional[int] = field(
        default=None,
        metadata={
            "name": "relatedPictogramArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    supplementary_panel_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_supplementaryPanelAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class SupplementaryPictogram(SupplementaryInformationDisplay):
    """
    An additional pictogram that is displayed in the panel which is
    supplemental to the associated pictogram display.

    :ivar pictogram_description: Description of the displayed
        supplementary pictogram.
    :ivar pictogram_code: The code of the supplementary pictogram from
        the supplementary pictogram code list referenced in the
        corresponding SupplementaryPanelArea.
    :ivar pictogram_url: Reference to a URL from where an image of the
        displayed supplementary pictogram can be be obtained.
    :ivar additional_description: Additional free text description of
        the supplementary pictogram.
    :ivar pictogram_flashing: Indication of whether the pictogram is
        flashing.
    :ivar pictogram_information_type: Allows characterising the type of
        of displayed information
    :ivar supplementary_pictogram_extension:
    """
    pictogram_description: Optional[SupplementalPictogramEnum2] = field(
        default=None,
        metadata={
            "name": "pictogramDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictogramCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    pictogram_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictogramUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    additional_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "additionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram_flashing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramFlashing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram_information_type: Optional[InformationTypeEnum2] = field(
        default=None,
        metadata={
            "name": "pictogramInformationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    supplementary_pictogram_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_supplementaryPictogramExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class SupplementaryText(SupplementaryInformationDisplay):
    """
    Text used in a supplementary display associated with a pictogram.

    :ivar text_line: One line of text displayed in the panel which is
        supplemental to the pictogram display.
    :ivar supplementary_text_extension:
    """
    text_line: Optional[TextLine] = field(
        default=None,
        metadata={
            "name": "textLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    supplementary_text_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_supplementaryTextExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class TextDisplayArea(DisplayArea):
    """
    Characteristics specific to the textual display area on the VMS.

    :ivar proportional_font: Whether the VMS supports proportional fonts
    :ivar max_number_of_characters: Maximum number of displayable
        characters on a single line in the textual display area of the
        VMS.
    :ivar max_number_of_rows: Maximum number of rows of displayable
        characters in the textual display area of the VMS.
    :ivar text_code_list_identifier: Indicates which textual message
        code list is referenced. This may be specific to the VMS type
        defined by vmsTypeCode.
    :ivar max_font_height: Maximum font height in pixels.
    :ivar min_font_height: Minimum font height in pixels.
    :ivar max_font_width: Maximum font width in pixels.
    :ivar min_font_width: Minimum font width in pixels.
    :ivar max_font_spacing: Maximum font spacing in pixels.
    :ivar min_font_spacing: Minimum font spacing in pixels.
    :ivar text_display_area_extension:
    """
    proportional_font: Optional[bool] = field(
        default=None,
        metadata={
            "name": "proportionalFont",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    max_number_of_characters: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxNumberOfCharacters",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    max_number_of_rows: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxNumberOfRows",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    text_code_list_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "textCodeListIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    max_font_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxFontHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    min_font_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "minFontHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    max_font_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxFontWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    min_font_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "minFontWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    max_font_spacing: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxFontSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    min_font_spacing: Optional[int] = field(
        default=None,
        metadata={
            "name": "minFontSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    text_display_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_textDisplayAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class VmsMessage:
    """
    A message displayed on a VMS which can comprise one or more sequentially
    displayed text pages and/or pictograms with supplementary details.

    :ivar associated_traffic_management_plan: The identification of the
        traffic management plan or diversion plan with which the message
        is associated.
    :ivar message_set_by: The organisation or authority which set the
        message currently being displayed.
    :ivar set_by_system: Indicates whether the message has been set
        automatically by a system. True =  automatically set.
    :ivar reason_for_setting: The reason why the sign has been set.
    :ivar coded_reason_for_setting: The reason, in terms of a high-level
        coded classification, why the sign has been set.
    :ivar message_information_type: Type of information being displayed.
    :ivar primary_setting: Identifies whether the message setting is
        primary (explicitly requested) or is secondary (derived
        according to an algorithm as the result of setting other signs).
        True = a primary setting.
    :ivar mare_nostrum_compliant: Indication that the displayed message
        (text and pictogram) conforms with the formulation recommended
        by the Mare Nostrum project.
    :ivar time_last_set: The date/time at which the sign was last set.
    :ivar requested_by: The authority, organisation or system which
        requested the setting of the message. This may be different from
        the authority or system which actually set the message on behalf
        of the requestor.
    :ivar related_situation: A reference to the managed situation to
        which the set message relates.
    :ivar related_situation_record: A reference to the situation record
        within a managed situation to which the set message relates.
    :ivar distance_from_closest_situation_record: Distance of the VMS
        from the location of the closest situation record. If the VMS is
        located within the extent of the situation record this should be
        set to zero.
    :ivar sequencing_interval: The time duration that each text page or
        pictogram within a message is displayed for before the VMS
        displays the next text page and/or pictogram in the message.
    :ivar display_area_settings:
    :ivar image:
    :ivar vms_message_extension:
    """
    associated_traffic_management_plan: Optional[str] = field(
        default=None,
        metadata={
            "name": "associatedTrafficManagementPlan",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    message_set_by: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "messageSetBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    set_by_system: Optional[bool] = field(
        default=None,
        metadata={
            "name": "setBySystem",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    reason_for_setting: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reasonForSetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    coded_reason_for_setting: Optional[SettingReasonEnum2] = field(
        default=None,
        metadata={
            "name": "codedReasonForSetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    message_information_type: List[MessageInformationTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "messageInformationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    primary_setting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "primarySetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    mare_nostrum_compliant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "mareNostrumCompliant",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    time_last_set: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeLastSet",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    requested_by: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "requestedBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    related_situation: List[SituationVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "relatedSituation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    related_situation_record: List[SituationRecordVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "relatedSituationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    distance_from_closest_situation_record: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceFromClosestSituationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    sequencing_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "sequencingInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_area_settings: List[VmsMessageDisplayAreaIndexDisplayAreaSettings] = field(
        default_factory=list,
        metadata={
            "name": "displayAreaSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    image: Optional[Image] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_message_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsMessageExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class TextDisplayLineIndexTextLine:
    class Meta:
        name = "_TextDisplayLineIndexTextLine"

    text_line: Optional[TextLine] = field(
        default=None,
        metadata={
            "name": "textLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    line_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsConfigurationDisplayAreaIndexDisplayArea:
    class Meta:
        name = "_VmsConfigurationDisplayAreaIndexDisplayArea"

    display_area: Optional[DisplayArea] = field(
        default=None,
        metadata={
            "name": "displayArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    display_area_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "displayAreaIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Pictogram:
    """A main pictogram displayable on the VMS panel.

    Note a main pictogram may have an associated supplementary panel
    which may itself contain a further pictogram and line of text.

    :ivar custom_pictogram_code: If a custom code list (not based on
        GDD) is being used, this is the code of the pictogram using the
        pictogram code list identified in the corresponding
        PictogramDisplayArea object
    :ivar additional_description: Additional description of the
        pictogram.
    :ivar pictogram_flashing: Indication of whether the pictogram is
        flashing.
    :ivar pictogram_in_inverse_colour: The pictogram is displayed in
        inverse colour (i.e. the colours are the inverse of normal).
    :ivar vienna_convention_compliant: Indicates that the displayed
        pictogram conforms with the Vienna Convention defined pictogram
        list as modified by "UNECE Consolidated Resolution on Road Signs
        and Signals".
    :ivar pictogram_information_type: Allows characterising the type of
        of displayed information
    :ivar gdd_structure:
    :ivar pictogram_extension:
    """
    custom_pictogram_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "customPictogramCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    additional_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "additionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram_flashing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramFlashing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram_in_inverse_colour: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramInInverseColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vienna_convention_compliant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "viennaConventionCompliant",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram_information_type: Optional[InformationTypeEnum2] = field(
        default=None,
        metadata={
            "name": "pictogramInformationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    gdd_structure: Optional[GddStructure] = field(
        default=None,
        metadata={
            "name": "gddStructure",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pictogramExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class TextDisplay(DisplayAreaSettings):
    """
    A page of text (comprising one or more ordered lines) that are displayed
    simultaneously on the VMS.

    :ivar text_code: The code of the specific text, from the defined
        code list.
    :ivar text_image_url: Reference to a URL from where an image of the
        displayed text can be be obtained.
    :ivar text_line:
    :ivar text_display_extension:
    """
    text_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "textCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    text_image_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "textImageUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    text_line: List[TextDisplayLineIndexTextLine] = field(
        default_factory=list,
        metadata={
            "name": "textLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    text_display_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_textDisplayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class VmsConfiguration:
    """
    Describes the current configuration and characteristics of a VMS, whether
    it is statically or dynamically configured.

    :ivar number_of_display_areas: Number of display areas which the VMS
        contains.
    :ivar display_area:
    :ivar vms_configuration_extension:
    """
    number_of_display_areas: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfDisplayAreas",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_area: List[VmsConfigurationDisplayAreaIndexDisplayArea] = field(
        default_factory=list,
        metadata={
            "name": "displayArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_configuration_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsConfigurationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class VmsStatusMessageIndexVmsMessage:
    class Meta:
        name = "_VmsStatusMessageIndexVmsMessage"

    vms_message: Optional[VmsMessage] = field(
        default=None,
        metadata={
            "name": "vmsMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    message_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "messageIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PictogramDisplay(DisplayAreaSettings):
    """
    A display of a pictogram on one area on a VMS, potentially with associated
    supplemental information or instructions.

    :ivar is_primary_pictogram: Indicates if the given pictogram display
        area is considered as the primary pictogram (= True) or not (=
        False).
    :ivar pictogram_display_url: Reference to a URL from where an image
        of the displayed pictogram can be be obtained.
    :ivar pictogram:
    :ivar supplementary_information_display:
    :ivar image:
    :ivar pictogram_display_extension:
    """
    is_primary_pictogram: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPrimaryPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram_display_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram: Optional[Pictogram] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    supplementary_information_display: Optional[SupplementaryInformationDisplay] = field(
        default=None,
        metadata={
            "name": "supplementaryInformationDisplay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    image: Optional[Image] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    pictogram_display_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pictogramDisplayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class RegularPictogram(Pictogram):
    """
    A regular pictogram displayable on a VMS panel.

    :ivar pictogram_description: Description of the pictogram.
    :ivar presence_of_red_triangle: Indication of the presence of a red
        triangle around the pictogram, often used to indicate imminence,
        typically within 2 km, of signed danger.
    :ivar displayed_numerical_information:
    :ivar regular_pictogram_extension:
    """
    pictogram_description: List[PictogramEnum2] = field(
        default_factory=list,
        metadata={
            "name": "pictogramDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    presence_of_red_triangle: Optional[bool] = field(
        default=None,
        metadata={
            "name": "presenceOfRedTriangle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    displayed_numerical_information: List[DisplayedNumericalInformation] = field(
        default_factory=list,
        metadata={
            "name": "displayedNumericalInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_occurs": 2,
        }
    )
    regular_pictogram_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_regularPictogramExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class Vms:
    """Variable message sign - a display panel used to display one or more messages (text, symbols, pictograms or combinations) that can be changed or switched on or off as required

    :ivar lanterns_present: Indicates whether the VMS is equipped with
        flashing lanterns outside the text or pictogram display areas
    :ivar description: The description of the VMS (possibly giving a
        description of its location or its normal use).
    :ivar owner: Owner (authority or organisation) of the VMS. This may
        not be the same as the authority or organisation which is
        currently controlling the VMS.
    :ivar physical_support: Description of how the VMS is physically
        mounted or deployed on the road.
    :ivar vms_type: Broad classification of the type of variable message
        sign.
    :ivar vms_type_code: Specification of the type of VMS defined by a
        code, normally country or even manufacturer specific (e.g. MS4).
    :ivar dynamically_configurable: Identifies (when True) that the VMS
        has a display area that may be dynamically configured to display
        different combinations of text and pictogram areas. The current
        configuration will normally be given with each published current
        VMS setting.
    :ivar display_height: Height in metres of the sign's overall display
        area.
    :ivar display_width: Width in metres of the sign's overall display
        area.
    :ivar height_above_carriageway: Height in metres of the mounted sign
        above the carriageway, measured to the bottom of the display
        area.
    :ivar dedicated_usage: Type of usage to which this VMS is dedicated
    :ivar vms_configuration:
    :ivar vms_location: The physical point location at which the
        variable message sign is situated. For mobile VMS which are
        regularly moved this need not be provided. Instead the VMS
        location should be provided in the VmsPublication along with
        current settings.
    :ivar managed_logical_location: The logical location managed by the
        VMS
    :ivar image_link: A URL reference from where an image of the VMS can
        be obtained.
    :ivar vms_extension:
    """
    lanterns_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "lanternsPresent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    owner: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    physical_support: Optional[PhysicalSupportEnum2] = field(
        default=None,
        metadata={
            "name": "physicalSupport",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_type: Optional[VmsTypeEnum2] = field(
        default=None,
        metadata={
            "name": "vmsType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsTypeCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    dynamically_configurable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "dynamicallyConfigurable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "displayHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    display_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "displayWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    height_above_carriageway: Optional[float] = field(
        default=None,
        metadata={
            "name": "heightAboveCarriageway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    dedicated_usage: Optional[DedicatedUsageEnum2] = field(
        default=None,
        metadata={
            "name": "dedicatedUsage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_configuration: Optional[VmsConfiguration] = field(
        default=None,
        metadata={
            "name": "vmsConfiguration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    vms_location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "vmsLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    managed_logical_location: Optional[ManagedLogicalLocation] = field(
        default=None,
        metadata={
            "name": "managedLogicalLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    image_link: Optional[UrlLink] = field(
        default=None,
        metadata={
            "name": "imageLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class VmsStatus:
    """
    Provides the current status and settings of the VMS and the currently
    displayed information.

    :ivar flashing_lights_on: Indicates if lights outside display areas
        (called lanterns in some countries) are turned on.
    :ivar remaining_power_capacity: The estimated length of time for
        which the VMS will have power to continue operating
    :ivar status_update_time: Time at which this VMS status was updated
    :ivar sequencing_interval: The time duration that each message is
        displayed for before the VMS displays the next message in the
        sequence.
    :ivar working_status: Indicates whether the VMS is usable. Note it
        can still be usable with minor faults.
    :ivar vms_dynamic_configuration:
    :ivar vms_message:
    :ivar vms_location_override: The current physical point location at
        which the VMS is situated. This overrides any physical location
        stated in the corresponding Vms object. Typically it is used for
        giving the updated physical location of a mobile VMS which has
        recently been moved.
    :ivar managed_logical_location_override: The current logical
        location that is being managed by the VMS which overrides any
        stated in the corresponding Vms object. Typically it is used for
        giving the updated managed location of a mobile VMS which has
        recently been moved.
    :ivar vms_fault:
    :ivar vms_status_extension:
    """
    flashing_lights_on: Optional[bool] = field(
        default=None,
        metadata={
            "name": "flashingLightsOn",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    remaining_power_capacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "remainingPowerCapacity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    status_update_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "statusUpdateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    sequencing_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "sequencingInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    working_status: Optional[WorkingStatusEnum2] = field(
        default=None,
        metadata={
            "name": "workingStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_dynamic_configuration: Optional[VmsConfiguration] = field(
        default=None,
        metadata={
            "name": "vmsDynamicConfiguration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_message: List[VmsStatusMessageIndexVmsMessage] = field(
        default_factory=list,
        metadata={
            "name": "vmsMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_location_override: Optional[Location] = field(
        default=None,
        metadata={
            "name": "vmsLocationOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    managed_logical_location_override: Optional[ManagedLogicalLocation] = field(
        default=None,
        metadata={
            "name": "managedLogicalLocationOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_fault: List[VmsFault] = field(
        default_factory=list,
        metadata={
            "name": "vmsFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class CompositePictogram(Pictogram):
    """
    A composite pictogram representing a diagrammatic schema in association
    with an embedded regular sign.

    :ivar pictogram_description: Description of the  displayed composed
        pictogram.
    :ivar regular_pictogram:
    :ivar composite_pictogram_extension:
    """
    pictogram_description: Optional[CompositePictogramEnum2] = field(
        default=None,
        metadata={
            "name": "pictogramDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    regular_pictogram: Optional[RegularPictogram] = field(
        default=None,
        metadata={
            "name": "regularPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    composite_pictogram_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_compositePictogramExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class VmsControllerStatusVmsIndexVmsStatus:
    class Meta:
        name = "_VmsControllerStatusVmsIndexVmsStatus"

    vms_status: Optional[VmsStatus] = field(
        default=None,
        metadata={
            "name": "vmsStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    vms_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "vmsIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsControllerVmsIndexVms:
    class Meta:
        name = "_VmsControllerVmsIndexVms"

    vms: Optional[Vms] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    vms_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "vmsIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsController:
    """
    A roadside unit which can control one or more variable message signs on a
    single gantry or mounting or on closely associated gantries or mountings.

    :ivar number_of_vms: Number of variable message signs controlled by
        the unit.
    :ivar external_identifier: Identification of a VMS controller unit
        used by the supplier or consumer systems.
    :ivar ip_address: IP network address of the VMS controller unit.
    :ivar electronic_address: Electronic address of the VMS controller
        unit (if not IP addressable).
    :ivar vms:
    :ivar vms_controller_extension:
    :ivar id:
    :ivar version:
    """
    number_of_vms: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVms",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    external_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    ip_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    electronic_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "electronicAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    vms: List[VmsControllerVmsIndexVms] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_controller_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsControllerExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsControllerStatus:
    """
    Status of a VMS controller unit.

    :ivar vms_controller_table_reference: A reference to a versioned VMS
        controller unit table.
    :ivar vms_controller_reference: A reference to a versioned VMS
        controller record in a VMS controller table which defines the
        characteristics of the VMS controller unit.
    :ivar status_update_time: Time at which this VMS controller unit
        status was updated
    :ivar information_manager_override: Organisation that manages the
        information content (is responsible for updates of this
        information) typically the organisation that first made the
        DATEX II publication of this content. This value overrides any
        value specified at a more general level.
    :ivar vms_status:
    :ivar vms_controller_fault:
    :ivar vms_controller_status_extension:
    """
    vms_controller_table_reference: Optional[VmsControllerTableVersionedReference] = field(
        default=None,
        metadata={
            "name": "vmsControllerTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    vms_controller_reference: Optional[VmsControllerVersionedReference] = field(
        default=None,
        metadata={
            "name": "vmsControllerReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    status_update_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "statusUpdateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    information_manager_override: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "informationManagerOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_status: List[VmsControllerStatusVmsIndexVmsStatus] = field(
        default_factory=list,
        metadata={
            "name": "vmsStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_controller_fault: List[VmsControllerFault] = field(
        default_factory=list,
        metadata={
            "name": "vmsControllerFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_controller_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsControllerStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class VmsControllerTable:
    """
    A versioned VMS controller unit table comprising a number of data records,
    each record defining the characteristics of a specific deployed variable
    message sign controller unit.

    :ivar vms_controller_table_identification: An alphanumeric
        identification for the VMS controller unit table, possibly human
        readable.
    :ivar information_manager: Organisation that manages the information
        content (is responsible for updates of this information)
        typically the organisation that first made the DATEX II
        publication of this content.
    :ivar vms_controller:
    :ivar vms_controller_table_extension:
    :ivar id:
    :ivar version:
    """
    vms_controller_table_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsControllerTableIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "max_length": 1024,
        }
    )
    information_manager: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "informationManager",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    vms_controller: List[VmsController] = field(
        default_factory=list,
        metadata={
            "name": "vmsController",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "min_occurs": 1,
        }
    )
    vms_controller_table_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsControllerTableExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsPublication(PayloadPublication):
    """
    A publication containing the current status and settings of one or more VMS
    controller units, each unit controlling one or more individual variable
    message signs.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    vms_controller_status: List[VmsControllerStatus] = field(
        default_factory=list,
        metadata={
            "name": "vmsControllerStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "min_occurs": 1,
        }
    )
    vms_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )


@dataclass
class VmsTablePublication(PayloadPublication):
    """
    A publication containing one or more VMS controller unit tables each
    comprising a set of records which hold details of VMS controller units.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "required": True,
        }
    )
    vms_controller_table: List[VmsControllerTable] = field(
        default_factory=list,
        metadata={
            "name": "vmsControllerTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
            "min_occurs": 1,
        }
    )
    vms_table_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vmsTablePublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/vms",
        }
    )
