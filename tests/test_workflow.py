from unittest.mock import Mock, patch

import pytest

from agent.workflow import execute_node, extract_incident_id, intent_node


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


@patch("agent.workflow.route_user_request")
def test_execute_node_uses_extracted_incident_id(mock_route_user_request):
    tool = Mock(return_value=[("incident", 15)])
    mock_route_user_request.return_value = tool
    state = intent_node({"user_input": "Show Incident 15"})

    result = execute_node(state)

    tool.assert_called_once_with(15)
    assert result["result"] == [("incident", 15)]
