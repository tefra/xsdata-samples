from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.elaborated_data import ElaboratedData
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.operator_action import OperatorAction
from datexii.models.eu.datexii.v2.traffic_element import TrafficElement
from datexii.models.eu.datexii.v2.url_link import UrlLink

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TrafficViewRecord:
    """An identifiable instance of a single record within a traffic view which shall comprise at most one instance of each of the following: OperatorAction, TrafficElement, ElaboratedData and CCTVImages.

    :ivar record_sequence_number: A number identifying the sequence of
        the record within the set of records which comprise the traffic
        view.
    :ivar traffic_element:
    :ivar operator_action:
    :ivar elaborated_data:
    :ivar url_link:
    :ivar traffic_view_record_extension:
    :ivar id:
    """

    record_sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "recordSequenceNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    traffic_element: Optional[TrafficElement] = field(
        default=None,
        metadata={
            "name": "trafficElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    operator_action: Optional[OperatorAction] = field(
        default=None,
        metadata={
            "name": "operatorAction",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    elaborated_data: Optional[ElaboratedData] = field(
        default=None,
        metadata={
            "name": "elaboratedData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    url_link: List[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    traffic_view_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
