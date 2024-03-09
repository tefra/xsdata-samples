from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

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
        },
    )
    state: None | PredictionStateEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publish_start: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        },
    )
    publish_stop: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        },
    )
