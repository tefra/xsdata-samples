from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class AgentIdoverride6:
    """
    Vendor specific agent identifier overrides to be used to access vendor systems.

    Parameters
    ----------
    supplier_code
        Supplier code to determine which vendor this AgentId belongs to.
    provider_code
        Provider code to route the AgentId to proper provider.
    agent_id
        The Agent ID for the applicable supplier/vendor
    """
    class Meta:
        name = "AgentIDOverride"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    agent_id: None | str = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        }
    )
