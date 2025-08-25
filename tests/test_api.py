import requests

BASE_URL = "https://man.kontrl.tech/kore/rest/healthcheck/"
HEADERS = {"Content-Type": "application/json"}

def test_healthcheck_all_modules_ok():
    payload = {"modules": "all"}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS, timeout=10)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict), "A resposta deve ser um JSON com módulos"
    for module, status in data.items():
        assert status.lower() == "ok", f"Módulo {module} não está saudável (status: {status})"

def test_healthcheck_some_module_nok():
    # Exemplo opcional: testa um módulo específico, que pode estar NOK
    payload = {"modules": ["drone"]}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS, timeout=10)
    assert response.status_code in (200, 504)

    data = response.json()
    assert "drone" in data
    assert data["drone"].lower() in ("ok", "nok")

def test_healthcheck_timeout():
    # Simula um módulo não saudável para retornar 504
    payload = {"modules": ["drone"]}  # supomos que 'drone' pode falhar
    response = requests.post(BASE_URL, json=payload, headers=HEADERS, timeout=5)
    assert response.status_code in (200, 504)
