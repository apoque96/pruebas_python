import pytest
from flow import full_flow

def test_full_flow_success():
    assert "10" in full_flow(3, 7)

def test_full_flow_failure():
    with pytest.raises(ValueError):
        full_flow(-1, 5)