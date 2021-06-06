from dataclasses import dataclass, field
from typing import Optional
from .control_centre_ref import ControlCentreRef
from .interchange_rule_parameter_structure import InterchangeRuleParameterStructure
from .interchange_rule_timings_rel_structure import InterchangeRuleTimingsRelStructure
from .interchange_version_structure import InterchangeVersionStructure
from .zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleVersionStructure(InterchangeVersionStructure):
    class Meta:
        name = "InterchangeRule_VersionStructure"

    connection_zone_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ConnectionZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centre_ref: Optional[ControlCentreRef] = field(
        default=None,
        metadata={
            "name": "ControlCentreRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timings: Optional[InterchangeRuleTimingsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    feeder_filter: Optional[InterchangeRuleParameterStructure] = field(
        default=None,
        metadata={
            "name": "FeederFilter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distributor_filter: Optional[InterchangeRuleParameterStructure] = field(
        default=None,
        metadata={
            "name": "DistributorFilter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
