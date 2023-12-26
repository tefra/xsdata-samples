from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.basic_data import BasicData
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location_characteristics_override import (
    LocationCharacteristicsOverride,
)
from datexii.models.eu.datexii.v2.measurement_equipment_fault import (
    MeasurementEquipmentFault,
)
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MeasuredValue:
    """
    Contains optional characteristics for the specific measured value (indexed to
    correspond with the defined characteristics of the measurement at the
    referenced measurement site) which override the static characteristics defined
    in the MeasurementSiteTable.

    :ivar measurement_equipment_type_used: The type of equipment used to
        gather the raw information from which the data values are
        determined, e.g. 'loop', 'ANPR' (automatic number plate
        recognition) or 'urban traffic management system' (such as
        SCOOT).
    :ivar location_characteristics_override:
    :ivar measurement_equipment_fault:
    :ivar basic_data:
    :ivar measured_value_extension:
    """

    measurement_equipment_type_used: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentTypeUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    location_characteristics_override: Optional[
        LocationCharacteristicsOverride
    ] = field(
        default=None,
        metadata={
            "name": "locationCharacteristicsOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_equipment_fault: List[MeasurementEquipmentFault] = field(
        default_factory=list,
        metadata={
            "name": "measurementEquipmentFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    basic_data: Optional[BasicData] = field(
        default=None,
        metadata={
            "name": "basicData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measured_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measuredValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
