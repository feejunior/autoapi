import requests

BASE_URL = "https://hel.kore.kontrl.tech/health-check"
HEADERS = {
"Content-Type": "application/json",
"x-kore-drone-uid":"drone:87c0976259b402a4160bff6db091e14bfcb9d0ea3f1e3425ef073ad146e2b13e",
"x-kore-drone-sign": ""
}

def test_healthcheck_all_modules_ok():
    payload = {"modules": "all"}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS, timeout=10)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict), "A resposta deve ser um JSON com módulos"
    for module, status in data.items():
        if module == "version": continue
        assert status.lower() == "ok", f"Módulo {module} não está saudável (status: {status})"

def test_healthcheck_some_modules():
    payload = {"modules": ["drone"]}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS, timeout=10)
    assert response.status_code == 200

    data = response.json()
    assert "drone" in data
    assert data["drone"].lower() in ("ok", "nok")