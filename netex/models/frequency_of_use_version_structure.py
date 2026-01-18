from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .discount_basis_enumeration import DiscountBasisEnumeration
from .frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from .time_interval_ref import TimeIntervalRef
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FrequencyOfUseVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "FrequencyOfUse_VersionStructure"

    frequency_of_use_type: FrequencyOfUseTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "FrequencyOfUseType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimal_frequency: int | None = field(
        default=None,
        metadata={
            "name": "MinimalFrequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximal_frequency: int | None = field(
        default=None,
        metadata={
            "name": "MaximalFrequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency_interval: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "FrequencyInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_interval_ref: TimeIntervalRef | None = field(
        default=None,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    discount_basis: DiscountBasisEnumeration | None = field(
        default=None,
        metadata={
            "name": "DiscountBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
