USDRI API
A deployed API that computes composite displacement risk scores from environmental variables using the Urban Snake Displacement Risk Index methodology, introduced in the paper Urban Snake Displacement Risk Index (USDRI): A Quantitative Framework for Measuring Displacement Pressure in Urbanizing Regions (Shuaib Alameen, 2026).
The methodology aggregates four environmental variables into a single score from 0 to 100, classified into four risk bands. Although the framework was originally developed for urban snake displacement research, the scoring logic is general enough to apply to any displacement risk context where the same four mechanisms are relevant.

Live API
https://usdri-api.onrender.com/docs


The API runs on Render's free tier, so the first request after a period of inactivity may take up to 50 seconds to respond. Subsequent requests are fast.
Endpoints
POST /score/raw — pass in your raw environmental measurements and the API handles normalization internally.
POST /score/normalized — pass in already-normalized values between 0 and 25 per component if you have handled normalization on your end.
Input Fields
total_observations — total number of recorded sightings in the area.
bbox_area_km2 — the bounding box area of your query region in square kilometres.
forest_loss_percent — percentage of forest cover lost in the region, from 0 to 100.
urban_feature_count — number of urban infrastructure features intersecting the region.
distance_to_urban_center_km — straight-line distance from the sighting cluster centroid to the nearest urban center in kilometres.
Response Structure
The API returns a usdri_score between 0 and 100, a risk band, an indicator color, a recommended action, and a breakdown of each component score.
Risk Bands
0 to 25 is Low — routine monitoring.
26 to 50 is Moderate — increased surveillance.
51 to 75 is High — targeted intervention.
76 to 100 is Critical — emergency response.
How to Use It
You can call the API from any language that supports HTTP requests. Send a POST request to the /score/raw endpoint with your values as a JSON body and you will get the score back immediately. Full interactive documentation with a built-in request tester is available at the live API link above.
Paper
The full methodology is documented in the original paper published on Zenodo. DOI: 10.5281/zenodo.19245787
Author
Shuaib Alameen — Independent Researcher, Lagos, Nigeria
