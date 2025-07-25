from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal, Optional, Protocol

from core.workflow.entities.workflow_node_execution import WorkflowNodeExecution


@dataclass
class OrderConfig:
    """Configuration for ordering NodeExecution instances."""

    order_by: list[str]
    order_direction: Optional[Literal["asc", "desc"]] = None


class WorkflowNodeExecutionRepository(Protocol):
    """
    Repository interface for NodeExecution.

    This interface defines the contract for accessing and manipulating
    NodeExecution data, regardless of the underlying storage mechanism.

    Note: Domain-specific concepts like multi-tenancy (tenant_id), application context (app_id),
    and trigger sources (triggered_from) should be handled at the implementation level, not in
    the core interface. This keeps the core domain model clean and independent of specific
    application domains or deployment scenarios.
    """

    def save(self, execution: WorkflowNodeExecution) -> None:
        """
        Save or update a NodeExecution instance.

        This method handles both creating new records and updating existing ones.
        The implementation should determine whether to create or update based on
        the execution's ID or other identifying fields.

        Args:
            execution: The NodeExecution instance to save or update
        """
        ...

    def get_by_workflow_run(
        self,
        workflow_run_id: str,
        order_config: Optional[OrderConfig] = None,
    ) -> Sequence[WorkflowNodeExecution]:
        """
        Retrieve all NodeExecution instances for a specific workflow run.

        Args:
            workflow_run_id: The workflow run ID
            order_config: Optional configuration for ordering results
                order_config.order_by: List of fields to order by (e.g., ["index", "created_at"])
                order_config.order_direction: Direction to order ("asc" or "desc")

        Returns:
            A list of NodeExecution instances
        """
        ...
