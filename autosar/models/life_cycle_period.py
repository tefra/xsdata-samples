from __future__ import annotations

from dataclasses import dataclass, field

from .date import Date
from .revision_label_string import RevisionLabelString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LifeCyclePeriod:
    """
    This meta class represents the ability to specify a point of time
    within a specified period, e.g. the starting or end point, in which a
    specific life cycle state is valid/applies to.

    :ivar date: Date within period.
    :ivar ar_release_version: Version of the AUTOSAR Release the element
        referred to is part of. The numbering contains three levels
        (major, minor, revision) which are defined by AUTOSAR.
    :ivar product_release: Version of the product within the period.
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
        name = "LIFE-CYCLE-PERIOD"

    date: Date | None = field(
        default=None,
        metadata={
            "name": "DATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ar_release_version: RevisionLabelString | None = field(
        default=None,
        metadata={
            "name": "AR-RELEASE-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    product_release: RevisionLabelString | None = field(
        default=None,
        metadata={
            "name": "PRODUCT-RELEASE",
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
