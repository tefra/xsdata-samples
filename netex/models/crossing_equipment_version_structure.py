from dataclasses import dataclass, field
from typing import Optional

from .access_equipment_version_structure import AccessEquipmentVersionStructure
from .bollard_crossing_enumeration import BollardCrossingEnumeration
from .crossing_type_enumeration import CrossingTypeEnumeration
from .marking_status_enumeration import MarkingStatusEnumeration
from .tactile_warning_strip_enumeration import TactileWarningStripEnumeration
from .visual_obstacle_enumeration import VisualObstacleEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CrossingEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "CrossingEquipment_VersionStructure"

    crossing_type: Optional[CrossingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "CrossingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    zebra_crossing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ZebraCrossing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pedestrian_lights: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PedestrianLights",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    acoustic_device_sensors: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcousticDeviceSensors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    acoustic_crossing_aids: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcousticCrossingAids",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_guidance_strips: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileGuidanceStrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_warning_strip: Optional[TactileWarningStripEnumeration] = field(
        default=None,
        metadata={
            "name": "TactileWarningStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    visual_guidance_bands: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisualGuidanceBands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dropped_kerb: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DroppedKerb",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suitable_for_cycles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    marking_status: Optional[MarkingStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "MarkingStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vibrating_crossing_aids: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VibratingCrossingAids",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bump_crossing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BumpCrossing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    visual_obstacle: Optional[VisualObstacleEnumeration] = field(
        default=None,
        metadata={
            "name": "VisualObstacle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bollard_crossing: Optional[BollardCrossingEnumeration] = field(
        default=None,
        metadata={
            "name": "BollardCrossing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
