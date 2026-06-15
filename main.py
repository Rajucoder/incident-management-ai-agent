from agent.workflow import (
    intent_node,
    execute_node
)

state = {
    #"user_input": "Show Incident 1"
    #"user_input": "Assign Incident 1 to Alice"
    #"user_input": "Update priority of Incident 1 to High"
    "user_input": "Resolve Incident 1 with resolution Server restarted"
}

state = intent_node(state)

print(state)

state = execute_node(state)

print(state)