from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.basic_data import BasicData
from datexii.models.eu.datexii.v2.elaborated_data_fault import (
    ElaboratedDataFault,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.source import Source
from datexii.models.eu.datexii.v2.validity import Validity

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ElaboratedData:
    """
    An instance of data which is derived/computed from one or more
    measurements over a period of time.

    It may be a current value or a forecast value predicted from historical
    measurements.

    :ivar forecast: Indication of whether this elaborated data is a
        forecast (true = forecast).
    :ivar source:
    :ivar validity:
    :ivar elaborated_data_fault:
    :ivar basic_data:
    :ivar elaborated_data_extension:
    """

    forecast: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    source: None | Source = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    validity: None | Validity = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    elaborated_data_fault: list[ElaboratedDataFault] = field(
        default_factory=list,
        metadata={
            "name": "elaboratedDataFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    basic_data: None | BasicData = field(
        default=None,
        metadata={
            "name": "basicData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    elaborated_data_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "elaboratedDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
