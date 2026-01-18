from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.cause import Cause
from datexii.models.eu.datexii.v2.cause_type_enum import CauseTypeEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class NonManagedCause(Cause):
    """
    A cause of this situation record which is not managed by the
    publication creator, i.e. one which is not represented by another
    situation record produced by the same publication creator.

    :ivar cause_description: Description of a cause which is not managed
        by the publication creator (e.g. an off network cause).
    :ivar cause_type: Indicates an external influence that may be the
        causation of components of a situation.
    :ivar non_managed_cause_extension:
    """

    cause_description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "causeDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    cause_type: None | CauseTypeEnum = field(
        default=None,
        metadata={
            "name": "causeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    non_managed_cause_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "nonManagedCauseExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
