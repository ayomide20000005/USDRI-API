USDRI API
A deployed API that computes composite displacement risk scores from environmental variables using the Urban Snake Displacement Risk Index methodology, introduced in the paper Urban Snake Displacement Risk Index (USDRI): A Quantitative Framework for Measuring Displacement Pressure in Urbanizing Regions (Shuaib Alameen, 2026).
The methodology aggregates four environmental variables into a single score from 0 to 100, classified into four risk bands. Although the framework was originally developed for urban snake displacement research, the scoring logic is general enough to apply to any displacement risk context where the same four mechanisms are relevant.

Live API
https://usdri-api.onrender.com/docs
Note: the API runs on Render's free tier, so the first request after a period of inactivity may take up to 50 seconds to respond. Subsequent requests are fast

Endpoints
POST /score/raw
Pass in your raw environmental measurements. The API handles normalization internally.
POST /score/normalized
Pass in already-normalized values between 0 and 25 per component if you have handled normalization on your end

How to use it
Using Python:

import requests

response = requests.post(
    "https://usdri-api.onrender.com/score/raw",
    json={
        "total_observations": 45,
        "bbox_area_km2": 200,
        "forest_loss_percent": 74,
        "urban_feature_count": 7,
        "distance_to_urban_center_km": 12
    }
)

print(response.json())


Using JavaScript:

const res = await fetch("https://usdri-api.onrender.com/score/raw", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        total_observations: 45,
        bbox_area_km2: 200,
        forest_loss_percent: 74,
        urban_feature_count: 7,
        distance_to_urban_center_km: 12
    })
});

console.log(await res.json());

