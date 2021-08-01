from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from npo.models.prediction_state_enum import PredictionStateEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class PredictionType:
    class Meta:
        name = "predictionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    state: Optional[PredictionStateEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publish_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
