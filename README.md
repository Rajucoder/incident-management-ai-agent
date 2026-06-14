# Incident Management AI Agent

An enterprise-style incident management AI agent built with Python, PostgreSQL, LangChain, and LangGraph.

## Features

- Retrieve incident details
- Update incident priority
- Assign incidents
- Resolve incidents
- Create audit logs
- Route user requests to incident tools
- Extract incident IDs dynamically from user input

## Project Structure

```text
agent/
  incident_tools.py
  router.py
  state.py
  workflow.py

db/
  connection.py
  incident_repository.py

tests/
  test_incident_repository.py
  test_workflow.py

evaluation/
mlflow/
main.py
pyproject.toml
```

## Prerequisites

- Python 3.11 or later
- PostgreSQL
- uv

## Installation

Install the project dependencies:

```bash
uv sync
```

To include future evaluation dependencies:

```bash
uv sync --extra evaluation
```

## Database Configuration

Update the PostgreSQL connection settings in `db/connection.py`:

```python
psycopg2.connect(
    host="localhost",
    database="incident_agent_db",
    user="postgres",
    password="",
)
```

The project expects these tables:

- `incidents`
- `knowledge_base`
- `audit_logs`

## Running the Agent

```bash
uv run python main.py
```

Example input:

```text
Show Incident 15
```

The workflow extracts `incident_id = 15` and retrieves the matching incident from PostgreSQL.

## Running Tests

```bash
uv run pytest
```

## Current Workflow

```mermaid
flowchart TD
    A[User Input] --> B[intent_node]
    B --> C[Detect Intent]
    C --> D[Extract Incident ID]
    D --> E[route_user_request]
    E --> F[Incident Tool]
    F --> G[Repository Function]
    G --> H[(PostgreSQL)]
    H --> I[Store Result in AgentState]
    I --> J[Return Result]
```

## Current Progress

- PostgreSQL database layer
- Incident repository operations
- Repository unit tests
- Agent state
- Intent detection
- Tool routing
- Incident tools
- Dynamic incident ID extraction
- Workflow tests

## Roadmap

1. Extract parameters for assignment, priority updates, and resolution
2. Execute all incident actions through the workflow
3. Create audit logs for incident changes
4. Build the workflow with LangGraph
5. Add knowledge-base retrieval and RAG
6. Evaluate with DeepEval and RAGAS
7. Track experiments with MLflow
