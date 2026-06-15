# Incident Management AI Agent

An enterprise-style incident management AI agent built with Python, PostgreSQL, LangChain, and LangGraph.

## Features

- Retrieve incident details
- Update incident priority
- Assign incidents
- Resolve incidents
- Create audit logs
- Route user requests to incident tools
- Extract incident IDs, assignees, priorities, and resolutions dynamically
- Preserve capitalization in extracted parameter values

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

## Supported Commands

```text
Show Incident 15
Assign Incident 15 to Alice Smith
Update Priority of Incident 8 to Critical
Resolve Incident 12 with resolution Server restarted
```

The workflow detects the intent, extracts the required parameters, routes the request to the matching tool, and returns the result.

## Running Tests

```bash
uv run pytest
```

The test suite currently contains 16 tests. Workflow tools and database connections are mocked, so unit tests do not access PostgreSQL.

## Current Workflow

```mermaid
flowchart TD
    A[User Input] --> B[intent_node]
    B --> C[Detect Intent]
    C --> D[Extract Action Parameters]
    D --> E[route_user_request]
    E --> F[Incident Tool]
    F --> G[Repository Function]
    G --> H[(PostgreSQL)]
    H --> I[Store Result in AgentState]
    I --> J[Return Result]
```

## Planned Project Architecture

```mermaid
flowchart TD
    U[User Request] --> LG[LangGraph Workflow]

    subgraph Agent Layer
        LG --> IN[Intent Detection]
        IN --> PE[Parameter Extraction]
        PE --> RT[Request Router]
        RT --> TL[Incident Tools]
    end

    subgraph Service Operations
        TL --> GET[Retrieve Incident]
        TL --> PRI[Update Priority]
        TL --> ASN[Assign Incident]
        TL --> RES[Resolve Incident]
        TL --> AUD[Create Audit Log]
    end

    subgraph Data Layer
        GET --> REPO[Incident Repository]
        PRI --> REPO
        ASN --> REPO
        RES --> REPO
        AUD --> REPO
        REPO --> PG[(PostgreSQL)]

        PG --> INC[incidents]
        PG --> KB[knowledge_base]
        PG --> LOG[audit_logs]
    end

    subgraph RAG Layer
        LG --> RET[Knowledge Retrieval]
        RET --> KB
        RET --> LLM[LLM Response Generation]
    end

    subgraph Evaluation Layer
        LG --> DE[DeepEval]
        LG --> RG[RAGAS]
        DE --> MF[MLflow]
        RG --> MF
    end

    REPO --> LG
    LLM --> LG
    LG --> OUT[Structured Response]
```

### Layer Responsibilities

1. **User Interface**: Starts with `main.py` and can later become a REST API or web interface.
2. **Agent and Workflow Layer**: Uses shared state, intent detection, parameter extraction, routing, and LangGraph workflow execution.
3. **Tool Layer**: Exposes incident operations while keeping agent logic separate from database logic.
4. **Repository Layer**: Contains PostgreSQL queries for retrieval, creation, assignment, priority updates, resolution, and auditing.
5. **Database Layer**: Stores operational incidents, troubleshooting knowledge, and audit history.
6. **RAG Layer**: Retrieves knowledge-base context and supplies it to an LLM for resolution recommendations.
7. **Evaluation Layer**: Uses DeepEval and RAGAS for quality evaluation, with MLflow tracking experiments and metrics.

### Planned Request Flow

```text
User request
→ LangGraph workflow
→ Detect intent
→ Extract parameters
→ Validate parameters
→ Route to tool
→ Execute repository operation
→ Create audit log
→ Return structured result
→ Record evaluation and tracing data
```

## Current Progress

- PostgreSQL database layer
- Incident repository operations
- Repository unit tests
- Agent state
- Intent detection
- Tool routing
- Incident tools
- Dynamic extraction of incident IDs, assignees, priorities, and resolutions
- Execution of retrieve, assign, priority-update, and resolve workflows
- Mock-only workflow and repository unit tests
- 16 passing tests

## Roadmap

1. Create audit logs for incident changes
2. Validate that target incidents exist and report unsuccessful updates
3. Build the workflow with LangGraph
4. Add knowledge-base retrieval and RAG
5. Evaluate with DeepEval and RAGAS
6. Track experiments with MLflow
