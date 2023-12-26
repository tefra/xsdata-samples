from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.alert_cdirection_enum import (
    AlertCDirectionEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCDirection:
    """
    The direction of traffic flow along the road to which the information relates.

    :ivar alert_cdirection_coded: The direction of traffic flow to which
        the situation, traffic data or information is related. Positive
        is in the direction of coding of the road.
    :ivar alert_cdirection_named: ALERT-C name of a direction e.g.
        Brussels -&gt; Lille.
    :ivar alert_cdirection_sense: Indicates for circular routes (i.e.
        valid only for ring roads) the sense in which navigation should
        be made from the primary location to the secondary location, to
        avoid ambiguity. TRUE indicates positive RDS direction, i.e.
        direction of coding of road.
    :ivar alert_cdirection_extension:
    """

    alert_cdirection_coded: Optional[AlertCDirectionEnum] = field(
        default=None,
        metadata={
            "name": "alertCDirectionCoded",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_cdirection_named: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "alertCDirectionNamed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    alert_cdirection_sense: Optional[bool] = field(
        default=None,
        metadata={
            "name": "alertCDirectionSense",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    alert_cdirection_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCDirectionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
