import pytest
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from fastapi_ip_geolocation import get_geo_info, GeoInfo

def test_ip_geolocation():
    app = FastAPI()

    @app.get("/geo")
    def geo_endpoint(geo: GeoInfo = Depends(get_geo_info)):
        return {
            "ip": geo.ip,
            "country": geo.country_code,
            "is_eu": geo.is_eu,
            "is_local": geo.is_local
        }

    client = TestClient(app)

    # Cloudflare header
    res = client.get("/geo", headers={"CF-Connecting-IP": "203.0.113.195", "CF-IPCountry": "TH"})
    assert res.status_code == 200
    data = res.json()
    assert data["ip"] == "203.0.113.195"
    assert data["country"] == "TH"
    assert data["is_eu"] is False

    # EU Country (DE)
    res_de = client.get("/geo", headers={"CloudFront-Viewer-Country": "DE"})
    assert res_de.json()["country"] == "DE"
    assert res_de.json()["is_eu"] is True
