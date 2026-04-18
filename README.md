**USDRI API**

A deployed API that computes composite displacement risk scores from environmental variables using the Urban Snake Displacement Risk Index methodology, introduced in the paper Urban Snake Displacement Risk Index (USDRI): A Quantitative Framework for Measuring Displacement Pressure in Urbanizing Regions (Shuaib Alameen 2026)

The methodology aggregates four environmental variables into a single score from 0 to 100, classified into four risk bands. Although the framework was originally developed for urban snake displacement research, the scoring logic is general enough to apply to any displacement risk context where the same four mechanisms are relevant

**Live API**
https://usdri-api.onrender.com/docs

**Note:** the API runs on Render's free tier, so the first request after a period of inactivity may take up to 50 seconds to respond Subsequent requests are fast.

**Endpoints**
POST /score/raw
Pass in your raw environmental measurements. The API handles normalization internally.
POST /score/normalized
Pass in already-normalized values between 0 and 25 per component if you have handled normalization on your end

**How to use it**
Using Python:

![python](https://github.com/user-attachments/assets/26df03fd-85c9-453d-90ac-cb90c6ff9d3f)


Using JavaScript:

![js](https://github.com/user-attachments/assets/503c96b8-a82c-4849-bbe9-bd5d0441ae60)


**Input Fields Explained**
For the /score/raw endpoint:

total_observations — total number of recorded sightings in the area
bbox_area_km2 — the bounding box area of your query region in square kilometres
forest_loss_percent — percentage of forest cover lost in the region, from 0 to 100
urban_feature_count — number of urban infrastructure features intersecting the region
distance_to_urban_center_km — straight-line distance from the sighting cluster centroid to the nearest urban center in kilometres


**Response Structure**

![r](https://github.com/user-attachments/assets/ef6b43b3-bf8b-4a2a-aac3-bd96b4c0385c)

**Risk Bands**

0 to 25 — Low — Routine monitoring
26 to 50 — Moderate — Increased surveillance
51 to 75 — High — Targeted intervention
76 to 100 — Critical — Emergency response


**Paper**
The full methodology is documented in the original paper published on Zenodo.
DOI: [10.5281/zenodo.19245787](https://doi.org/10.5281/zenodo.19245787)

Author
Shuaib Alameen — Independent Researcher, Lagos, Nigeria
