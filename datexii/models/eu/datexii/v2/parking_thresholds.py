from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.parking_status_colour_mapping import ParkingStatusColourMapping

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingThresholds:
    """Configuration parameters of the parking site, used among others for the
    dynamic attribute 'parkingStatus'.

    This component or all elements of it can be overridden in the
    dynamic model.

    :ivar almost_full_decreasing: The number of available spaces above
        which the state of the parking site is considered to change from
        'almost full' to 'spaces available' as the parking site's
        occupancy decreases. Must be greater than 'almostFullIncreasing'
        value.
    :ivar almost_full_increasing: The number of available spaces below
        which the state of the site is considered to change from 'spaces
        available' to 'almost full' as the site's occupancy increases.
        Must be lower or equal to 'almostFullDecreasing' and greater
        'fullDecreasing'.
    :ivar entrance_full: The number of available spaces below which the
        parking site is considered to be 'full' at its entrance (e.g.
        full sign is displayed at entrance or on managing VMS).
    :ivar full_decreasing: The number of available spaces above which
        the state of the parking site is considered to change from
        'full' to 'almost full' as the site's occupancy decreases. Must
        be greater or equal to 'fullIncreasing' value and lower than
        'almostFullIncreasing'.
    :ivar full_increasing: The number of available spaces below which
        the state of the parking site is considered to change from
        'almost full' to 'full' as the site's occupancy increases. Must
        be lower than or equal to 'fullDecreasing' value.
    :ivar overcrowding: The number of vehicles on the parking above
        which the overcrowding state of the parking site is considered
        to change to 'overcrowding'.  Can be used as an alternative to
        the overcrowding level attributes.
    :ivar overcrowding_level1: The number of vehicles on the parking
        site above which the overcrowding state of the parking site is
        considered to change from 'noOvercrowding' to
        'overcrowdingLevel1'. Must be lower than the
        'overcrowdingLevel2' value.
    :ivar overcrowding_level2: The number of vehicles on the parking
        site above which the overcrowding state of the parking site is
        considered to change from 'overcrowdingLevel1' to
        'overcrowdingLevel2'. Must be greater than the
        'overcrowdingLevel1' value.
    :ivar parking_last_maximum_occupancy: The last known occupancy
        (number of parking vehicles on the site) under safe conditions.
    :ivar parking_status_colour_mapping:
    :ivar parking_thresholds_extension:
    """
    almost_full_decreasing: Optional[int] = field(
        default=None,
        metadata={
            "name": "almostFullDecreasing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    almost_full_increasing: Optional[int] = field(
        default=None,
        metadata={
            "name": "almostFullIncreasing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    entrance_full: Optional[int] = field(
        default=None,
        metadata={
            "name": "entranceFull",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    full_decreasing: Optional[int] = field(
        default=None,
        metadata={
            "name": "fullDecreasing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    full_increasing: Optional[int] = field(
        default=None,
        metadata={
            "name": "fullIncreasing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    overcrowding: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    overcrowding_level1: Optional[int] = field(
        default=None,
        metadata={
            "name": "overcrowdingLevel1",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    overcrowding_level2: Optional[int] = field(
        default=None,
        metadata={
            "name": "overcrowdingLevel2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_last_maximum_occupancy: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingLastMaximumOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_status_colour_mapping: List[ParkingStatusColourMapping] = field(
        default_factory=list,
        metadata={
            "name": "parkingStatusColourMapping",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_thresholds_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingThresholdsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
