**USDRI API**

A deployed API that computes composite displacement risk scores from environmental variables using the Urban Snake Displacement Risk Index methodology, introduced in the paper Urban Snake Displacement Risk Index (USDRI): A Quantitative Framework for Measuring Displacement Pressure in Urbanizing Regions (Shuaib Alameen, 2026).

The methodology aggregates four environmental variables into a single score from 0 to 100, classified into four risk bands. Although the framework was originally developed for urban snake displacement research, the scoring logic is general enough to apply to any displacement risk context where the same four mechanisms are relevant.

**Live API**
https://usdri-api.onrender.com/docs

**Note:** the API runs on Render's free tier, so the first request after a period of inactivity may take up to 50 seconds to respond. Subsequent requests are fast.

**Endpoints**
POST /score/raw
Pass in your raw environmental measurements. The API handles normalization internally.
POST /score/normalized
Pass in already-normalized values between 0 and 25 per component if you have handled normalization on your end.

**How to use it**
Using Python:

![python](https://github.com/user-attachments/assets/26df03fd-85c9-453d-90ac-cb90c6ff9d3f)
