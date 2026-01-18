from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.clock_driver import ClockDriver
from ipxact.models.default_value import DefaultValue
from ipxact.models.range import Range
from ipxact.models.single_shot_driver import SingleShotDriver

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class DriverType:
    """
    Wire port driver type.

    :ivar range:
    :ivar view_ref: A reference to a view in the file for which this
        type applies.
    :ivar default_value:
    :ivar clock_driver:
    :ivar single_shot_driver:
    :ivar id:
    """

    class Meta:
        name = "driverType"

    range: Range | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    view_ref: list[DriverType.ViewRef] = field(
        default_factory=list,
        metadata={
            "name": "viewRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    default_value: DefaultValue | None = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    clock_driver: ClockDriver | None = field(
        default=None,
        metadata={
            "name": "clockDriver",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    single_shot_driver: SingleShotDriver | None = field(
        default=None,
        metadata={
            "name": "singleShotDriver",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class ViewRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
