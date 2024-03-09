from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeBillingDetailsName(Enum):
    PERSONAL_ID = "PersonalId"
    COST_ACCOUNT_NUMBER = "CostAccountNumber"
    ACCOUNT_NUMBER = "AccountNumber"
    PROJECT_NUMBER = "ProjectNumber"
    ACTION_CODE = "ActionCode"
    DEPARTMENT_CODE = "DepartmentCode"
    ACCOUNTING_UNIT = "AccountingUnit"
    ORDER_NUMBER = "OrderNumber"
    DESTINATION = "Destination"
    FILE_DATE = "FileDate"
