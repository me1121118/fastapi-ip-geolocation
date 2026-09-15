# fastapi-ip-geolocation

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/fastapi-ip-geolocation/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

FastAPI dependency to extract client country code, city, and IP geolocation from Cloudflare, CloudFront, or reverse proxy CDN headers.

---

## 🚀 Features

- ⚡ **Zero Latency**: Extracts country info directly from edge proxy headers (`CF-IPCountry`, `CloudFront-Viewer-Country`, `X-Geo-Country`).
- 🌐 **Fallback Support**: Defaults to private/local network detection for local development.
- 🪶 **Zero Dependencies**: Pure standard library.

---

## 📦 Installation

```bash
pip install fastapi-ip-geolocation
```

---

## 🛠️ Quickstart

```python
from fastapi import FastAPI, Depends
from fastapi_ip_geolocation import get_geo_info, GeoInfo

app = FastAPI()

@app.get("/localize")
def localize(geo: GeoInfo = Depends(get_geo_info)):
    return {
        "client_ip": geo.ip,
        "country": geo.country_code,
        "is_eu": geo.is_eu
    }
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this library helped your geolocation detection, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [buymeacoffee.com/kcidi4148](https://buymeacoffee.com/kcidi4148)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
