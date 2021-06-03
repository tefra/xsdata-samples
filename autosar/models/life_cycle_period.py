from dataclasses import dataclass, field
from typing import Optional
from autosar.models.date import Date
from autosar.models.revision_label_string import RevisionLabelString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LifeCyclePeriod:
    """
    This meta class represents the ability to specify a point of time within a
    specified period, e.g. the starting or end point, in which a specific life
    cycle state is valid/applies to.

    :ivar date: Date within period.
    :ivar ar_release_version: Version of the AUTOSAR Release the element
        referred to is part of.    The numbering contains three levels
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

    date: Optional[Date] = field(
        default=None,
        metadata={
            "name": "DATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ar_release_version: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "AR-RELEASE-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    product_release: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "PRODUCT-RELEASE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
