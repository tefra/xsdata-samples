from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2"


@dataclass
class TreeBelowType:
    """
    :ivar assigned_turnover_tree_below: Turnover value assigned by
        D&amp;B to this legal entity and all entities below in the in
        the corporate tree. Only available for legal entities that are
        part of a corporate family, blank for all standalone or unlinked
        entities
    :ivar assigned_number_of_employees_tree_below: Number of employees
        assigned by D&amp;B to this legal entity and all entities below
        in the corporate tree.
    :ivar tree_below_sites:
    :ivar tree_below_sites_excluding_branch:
    """

    assigned_turnover_tree_below: None | AmountType = field(
        default=None,
        metadata={
            "name": "AssignedTurnoverTreeBelow",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "nillable": True,
        },
    )
    assigned_number_of_employees_tree_below: None | Decimal = field(
        default=None,
        metadata={
            "name": "AssignedNumberOfEmployeesTreeBelow",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    tree_below_sites: None | Decimal = field(
        default=None,
        metadata={
            "name": "TreeBelowSites",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    tree_below_sites_excluding_branch: None | Decimal = field(
        default=None,
        metadata={
            "name": "TreeBelowSitesExcludingBranch",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
