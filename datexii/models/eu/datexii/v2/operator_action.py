from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.operator_action_origin_enum import (
    OperatorActionOriginEnum,
)
from datexii.models.eu.datexii.v2.operator_action_status_enum import (
    OperatorActionStatusEnum,
)
from datexii.models.eu.datexii.v2.situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OperatorAction(SituationRecord):
    """
    Actions that a traffic operator can decide to implement to prevent or
    help correct dangerous or poor driving conditions, including
    maintenance of the road infrastructure.

    :ivar action_origin: Indicates whether the actions to be undertaken
        by the operator are the result of an internal operation or
        external influence.
    :ivar action_plan_identifier: The identifier of the traffic
        management action plan to which this action relates.
    :ivar operator_action_status: The status of the defined operator
        action.
    :ivar operator_action_extension:
    """

    action_origin: OperatorActionOriginEnum | None = field(
        default=None,
        metadata={
            "name": "actionOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    action_plan_identifier: str | None = field(
        default=None,
        metadata={
            "name": "actionPlanIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    operator_action_status: OperatorActionStatusEnum | None = field(
        default=None,
        metadata={
            "name": "operatorActionStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    operator_action_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "operatorActionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
