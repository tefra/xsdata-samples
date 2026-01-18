from __future__ import annotations

from dataclasses import dataclass, field

from .control_centre_ref import ControlCentreRef
from .interchange_rule_parameter_structure import (
    InterchangeRuleParameterStructure,
)
from .interchange_rule_timings_rel_structure import (
    InterchangeRuleTimingsRelStructure,
)
from .interchange_version_structure import InterchangeVersionStructure
from .zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleVersionStructure(InterchangeVersionStructure):
    class Meta:
        name = "InterchangeRule_VersionStructure"

    connection_zone_ref: ZoneRefStructure | None = field(
        default=None,
        metadata={
            "name": "ConnectionZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    control_centre_ref: ControlCentreRef | None = field(
        default=None,
        metadata={
            "name": "ControlCentreRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    exclude: bool | None = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timings: InterchangeRuleTimingsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    feeder_filter: InterchangeRuleParameterStructure | None = field(
        default=None,
        metadata={
            "name": "FeederFilter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distributor_filter: InterchangeRuleParameterStructure | None = field(
        default=None,
        metadata={
            "name": "DistributorFilter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
