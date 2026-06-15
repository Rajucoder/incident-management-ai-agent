from unittest.mock import Mock, patch

import pytest

from agent.workflow import (
    execute_node,
    extract_assignment,
    extract_incident_id,
    extract_priority_update,
    extract_resolution,
    intent_node,
)


@pytest.mark.parametrize(
    ("user_input", "expected_id"),
    [
        ("Show Incident 2", 2),
        ("Show Incident 15", 15),
        ("show incident #27", 27),
    ],
)
def test_extract_incident_id(user_input, expected_id):
    assert extract_incident_id(user_input) == expected_id


def test_intent_node_extracts_incident_id():
    state = {"user_input": "Show Incident 15"}

    result = intent_node(state)

    assert result["intent"] == "get_incident"
    assert result["incident_id"] == 15


def test_intent_node_rejects_get_request_without_incident_id():
    with pytest.raises(ValueError, match="No incident ID found"):
        intent_node({"user_input": "Show Incident"})


def test_extract_assignment_preserves_assignee_name():
    assert extract_assignment(
        "Assign Incident 15 to Alice Smith"
    ) == (15, "Alice Smith")


def test_extract_priority_update_preserves_priority():
    assert extract_priority_update(
        "Update Priority of Incident 8 to Critical"
    ) == (8, "Critical")


def test_extract_resolution_preserves_resolution_text():
    assert extract_resolution(
        "Resolve Incident 12 with resolution Server restarted"
    ) == (12, "Server restarted")


@pytest.mark.parametrize(
    ("extractor", "user_input", "error_message"),
    [
        (
            extract_assignment,
            "Assign Incident 15",
            "No incident ID or assignee found",
        ),
        (
            extract_priority_update,
            "Update Priority of Incident 8",
            "No incident ID or priority found",
        ),
        (
            extract_resolution,
            "Resolve Incident 12",
            "No incident ID or resolution found",
        ),
    ],
)
def test_extractors_reject_missing_parameters(
    extractor,
    user_input,
    error_message,
):
    with pytest.raises(ValueError, match=error_message):
        extractor(user_input)


@patch("agent.workflow.route_user_request")
def test_execute_node_uses_extracted_incident_id(mock_route_user_request):
    tool = Mock(return_value=[("incident", 15)])
    mock_route_user_request.return_value = tool
    state = intent_node({"user_input": "Show Incident 15"})

    result = execute_node(state)

    tool.assert_called_once_with(15)
    assert result["result"] == [("incident", 15)]


@pytest.mark.parametrize(
    ("user_input", "expected_arguments", "tool_result"),
    [
        (
            "Assign Incident 15 to Alice Smith",
            (15, "Alice Smith"),
            "Incident assigned to Alice Smith",
        ),
        (
            "Update Priority of Incident 8 to Critical",
            (8, "Critical"),
            "Priority updated to Critical",
        ),
        (
            "Resolve Incident 12 with resolution Server restarted",
            (12, "Server restarted"),
            "Incident resolved",
        ),
    ],
)
@patch("agent.workflow.route_user_request")
def test_execute_node_uses_extracted_action_parameters(
    mock_route_user_request,
    user_input,
    expected_arguments,
    tool_result,
):
    tool = Mock(return_value=tool_result)
    mock_route_user_request.return_value = tool
    state = intent_node({"user_input": user_input})

    result = execute_node(state)

    tool.assert_called_once_with(*expected_arguments)
    assert result["result"] == tool_result
