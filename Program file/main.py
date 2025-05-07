import requests

API_KEY = "1305a3d5074e398d143807afff9362e6"  # Free API key from Numverify
numbers = [
    "12523733215", "12523733845", "12523734875",
    "12622639954", "12692639923", "12692853922",
    "12785934129"
]

for number in numbers:
    response = requests.get(
        "http://apilayer.net/api/validate",
        params={
            "access_key": API_KEY,
            "number": number,
            "country_code": "US",
            "format": 1
        }
    )
    data = response.json()
    valid = data.get("valid", False)
    line_type = data.get("line_type", "Unknown")
    carrier = data.get("carrier", "Unknown")

    # Determine status based on validity
    status = "Positive" if valid else "Negative"
    allowed = "Allowed" if valid else "Not Allowed"

    print(f"Number: {number}")
    print(f"  Valid: {valid}")
    print(f"  Status: {status}")
    print(f"  Access: {allowed}")
    print(f"  Line Type: {line_type}")
    print(f"  Carrier: {carrier}")
    print("-" * 40)
