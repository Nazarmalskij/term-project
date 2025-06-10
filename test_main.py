import pytest
from src.main import app, calculate_tax

# -------------------------
# Тести для calculate_tax
# -------------------------

def test_calculate_tax_normal():
    assert calculate_tax(1000, 0.2) == 200.0

def test_calculate_tax_zero_income():
    assert calculate_tax(0, 0.2) == 0.0

def test_calculate_tax_invalid_income():
    with pytest.raises(ValueError, match="Income cannot be negative"):
        calculate_tax(-500, 0.1)

def test_calculate_tax_invalid_rate_high():
    with pytest.raises(ValueError, match="Tax rate must be between 0 and 1"):
        calculate_tax(1000, 1.5)

def test_calculate_tax_invalid_rate_low():
    with pytest.raises(ValueError, match="Tax rate must be between 0 and 1"):
        calculate_tax(1000, -0.1)

# -------------------------
# Тести для Flask /tax
# -------------------------

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_tax_endpoint_valid(client):
    response = client.get('/tax?income=1000&rate=0.2')
    assert response.status_code == 200
    assert response.json["tax"] == 200.0

def test_tax_endpoint_missing_param(client):
    response = client.get('/tax?income=1000')  # відсутній параметр rate
    assert response.status_code == 400
    assert "error" in response.json

def test_tax_endpoint_invalid_param(client):
    response = client.get('/tax?income=abc&rate=0.2')
    assert response.status_code == 400
    assert "error" in response.json

def test_tax_endpoint_invalid_logic(client):
    response = client.get('/tax?income=-100&rate=0.2')
    assert response.status_code == 400
    assert "error" in response.json
