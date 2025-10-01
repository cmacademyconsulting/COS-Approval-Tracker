def is_valid_lat_lon(lat, lon) -> bool:
    try:
        lat = float(lat)
        lon = float(lon)
        return -90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0
    except Exception:
        return False
