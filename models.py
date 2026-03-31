from pydantic import BaseModel, Field


class RawInputRequest(BaseModel):
    total_observations: float = Field(..., ge=0, description="Total snake sightings in the area")
    bbox_area_km2: float = Field(..., gt=0, description="Bounding box area in square kilometres")
    forest_loss_percent: float = Field(..., ge=0, le=100, description="Percentage of forest cover lost")
    urban_feature_count: float = Field(..., ge=0, description="Number of urban infrastructure features")
    distance_to_urban_center_km: float = Field(..., ge=0, description="Haversine distance to nearest urban center in km")


class NormalizedInputRequest(BaseModel):
    sighting_density: float = Field(..., ge=0, le=25)
    habitat_loss: float = Field(..., ge=0, le=25)
    urban_expansion: float = Field(..., ge=0, le=25)
    urban_proximity: float = Field(..., ge=0, le=25)


class USDRIResponse(BaseModel):
    usdri_score: float
    band: str
    indicator: str
    recommended_action: str
    components: dict