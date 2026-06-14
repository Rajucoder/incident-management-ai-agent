from agent.workflow import (
    intent_node,
    execute_node
)

state = {
    "user_input": "Show Incident 1"
}

state = intent_node(state)

print(state)

state = execute_node(state)

print(state)