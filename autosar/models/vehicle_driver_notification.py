from dataclasses import dataclass, field

from .boolean import Boolean
from .vehicle_driver_notification_enum import VehicleDriverNotificationEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class VehicleDriverNotification:
    """
    This meta-class provides the ability to configure a notification of the
    vehicle driver with respect to the update of vehicle software.

    :ivar approval_required: This attribute controls whether approval is
        required for the driver notification.
    :ivar notification_state: This attribute is used to configure the
        notification state.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "VEHICLE-DRIVER-NOTIFICATION"

    approval_required: Boolean | None = field(
        default=None,
        metadata={
            "name": "APPROVAL-REQUIRED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    notification_state: VehicleDriverNotificationEnum | None = field(
        default=None,
        metadata={
            "name": "NOTIFICATION-STATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
