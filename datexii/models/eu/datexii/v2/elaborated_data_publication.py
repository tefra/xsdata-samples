from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.elaborated_data import ElaboratedData
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.header_information import HeaderInformation
from datexii.models.eu.datexii.v2.payload_publication import PayloadPublication
from datexii.models.eu.datexii.v2.reference_settings import ReferenceSettings

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ElaboratedDataPublication(PayloadPublication):
    """
    A publication containing one or more elaborated data sets.

    :ivar forecast_default: The default value for the publication of
        whether the elaborated data is a forecast (true = forecast).
    :ivar period_default: The default value for the publication of the
        time elapsed between the beginning and the end of the sampling
        or measurement period. This item may differ from the unit
        attribute; e.g. an hourly flow can be estimated from a 5-minute
        measurement period.
    :ivar time_default: The default for the publication of the time at
        which the values have been computed/derived.
    :ivar header_information:
    :ivar reference_settings:
    :ivar elaborated_data:
    :ivar elaborated_data_publication_extension:
    """

    forecast_default: None | bool = field(
        default=None,
        metadata={
            "name": "forecastDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    period_default: None | float = field(
        default=None,
        metadata={
            "name": "periodDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    time_default: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "timeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    header_information: None | HeaderInformation = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    reference_settings: None | ReferenceSettings = field(
        default=None,
        metadata={
            "name": "referenceSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    elaborated_data: list[ElaboratedData] = field(
        default_factory=list,
        metadata={
            "name": "elaboratedData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    elaborated_data_publication_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "elaboratedDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
