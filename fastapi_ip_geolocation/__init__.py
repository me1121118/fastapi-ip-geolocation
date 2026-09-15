from dataclasses import dataclass
from typing import Optional
from fastapi import Request

EU_COUNTRIES = {
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR",
    "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL",
    "PL", "PT", "RO", "SK", "SI", "ES", "SE"
}

@dataclass(frozen=True)
class GeoInfo:
    ip: str
    country_code: str
    is_eu: bool
    is_local: bool

def extract_client_ip(request: Request) -> str:
    cf_connecting_ip = request.headers.get("cf-connecting-ip")
    if cf_connecting_ip:
        return cf_connecting_ip.strip()

    x_forwarded_for = request.headers.get("x-forwarded-for")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()

    return request.client.host if request.client else "127.0.0.1"

def get_geo_info(request: Request) -> GeoInfo:
    """FastAPI dependency to inspect edge proxy geolocation headers."""
    ip = extract_client_ip(request)
    
    # Check headers from Cloudflare, CloudFront, Fly.io, etc.
    country = (
        request.headers.get("cf-ipcountry") or
        request.headers.get("cloudfront-viewer-country") or
        request.headers.get("x-country-code") or
        request.headers.get("x-geo-country") or
        "XX"
    ).upper().strip()

    is_local = ip in ("127.0.0.1", "::1", "localhost") or ip.startswith(("192.168.", "10."))
    is_eu = country in EU_COUNTRIES

    return GeoInfo(ip=ip, country_code=country, is_eu=is_eu, is_local=is_local)
