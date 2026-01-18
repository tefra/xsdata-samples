from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.description import Description

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ComputationType(AnnotableType):
    """
    ComputationType describes a computation in a process.

    :ivar description: Description describe the computation in any form
        desired by the user (these are informational rather than
        machine-actionable), and so may be supplied in multiple,
        parallel-language versions,
    :ivar local_id: The localID attribute is an optional identification
        for the computation within the process.
    :ivar software_package: The softwarePackage attribute holds the name
        of the software package that is used to perform the computation.
    :ivar software_language: The softwareLanguage attribute holds the
        coding language that the software package used to perform the
        computation is written in.
    :ivar software_version: The softwareVersion attribute hold the
        version of the software package that is used to perform that
        computation.
    """

    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
            "min_occurs": 1,
        },
    )
    local_id: None | str = field(
        default=None,
        metadata={
            "name": "localID",
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    software_package: None | str = field(
        default=None,
        metadata={
            "name": "softwarePackage",
            "type": "Attribute",
        },
    )
    software_language: None | str = field(
        default=None,
        metadata={
            "name": "softwareLanguage",
            "type": "Attribute",
        },
    )
    software_version: None | str = field(
        default=None,
        metadata={
            "name": "softwareVersion",
            "type": "Attribute",
        },
    )
