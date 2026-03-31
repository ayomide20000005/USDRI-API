import math


def normalize(value, min_val, max_val):
    if max_val == min_val:
        return 0
    return 25 * max(0, min(1, (value - min_val) / (max_val - min_val)))


def sighting_density_score(total_observations, bbox_area_km2):
    if bbox_area_km2 <= 0:
        return 0
    raw = total_observations / bbox_area_km2
    return 25 * min(raw / 1.0, 1)


def habitat_loss_score(forest_loss_percent):
    return 25 * max(0, min(forest_loss_percent, 100)) / 100


def urban_expansion_score(urban_feature_count):
    return 25 * min(urban_feature_count / 10, 1)


def urban_proximity_score(distance_km):
    return 25 * math.exp(-distance_km / 40)


def compute_usdri(sd_norm, hl_norm, ue_norm, up_norm):
    score = sd_norm + hl_norm + ue_norm + up_norm

    if score <= 25:
        band, indicator, action = "Low", "Green", "Routine monitoring"
    elif score <= 50:
        band, indicator, action = "Moderate", "Yellow", "Increased surveillance"
    elif score <= 75:
        band, indicator, action = "High", "Orange", "Targeted intervention"
    else:
        band, indicator, action = "Critical", "Red", "Emergency response"

    return {
        "usdri_score": round(score, 2),
        "band": band,
        "indicator": indicator,
        "recommended_action": action,
        "components": {
            "sighting_density": round(sd_norm, 2),
            "habitat_loss": round(hl_norm, 2),
            "urban_expansion": round(ue_norm, 2),
            "urban_proximity": round(up_norm, 2)
        }
    }