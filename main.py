from fastapi import FastAPI
from models import RawInputRequest, NormalizedInputRequest, USDRIResponse
from calculator import (
    sighting_density_score,
    habitat_loss_score,
    urban_expansion_score,
    urban_proximity_score,
    compute_usdri
)

app = FastAPI(
    title="USDRI API",
    description="Displacement Risk Index calculator. Pass in raw or pre-normalized environmental variables, get back a 0–100 composite risk score.",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/score/raw", response_model=USDRIResponse)
def score_from_raw(data: RawInputRequest):
    sd = sighting_density_score(data.total_observations, data.bbox_area_km2)
    hl = habitat_loss_score(data.forest_loss_percent)
    ue = urban_expansion_score(data.urban_feature_count)
    up = urban_proximity_score(data.distance_to_urban_center_km)
    return compute_usdri(sd, hl, ue, up)


@app.post("/score/normalized", response_model=USDRIResponse)
def score_from_normalized(data: NormalizedInputRequest):
    return compute_usdri(
        data.sighting_density,
        data.habitat_loss,
        data.urban_expansion,
        data.urban_proximity
    )