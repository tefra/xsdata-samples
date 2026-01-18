from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.traffic_status_enum import TrafficStatusEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TrafficStatusValue(DataValue):
    """
    A measured or calculated value of the status of traffic conditions on a
    section of road in a specified direction.

    :ivar traffic_status_value: A status value of traffic conditions on
        the identified section of road in the specified direction.
    :ivar traffic_status_value_extension:
    """

    traffic_status_value: TrafficStatusEnum | None = field(
        default=None,
        metadata={
            "name": "trafficStatusValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    traffic_status_value_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "trafficStatusValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
