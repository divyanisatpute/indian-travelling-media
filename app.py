from flask import Flask
import streamlit as st

app=Flask(__name__)

# Indian Destinations Database with Cost Metrics & Coordinates
DESTINATIONS = {
    "Goa": {
        "coords": [15.2993, 74.1240],
        "hotel_rate": "₹2,500 - ₹6,000 / night",
        "food_rate": "₹800 - ₹1,500 / day",
        "travel_rate": "₹500 - ₹1,200 / day (Scooter/Cabs)",
        "desc": "Sun-kissed beaches, vibrant nightlife, and Portuguese heritage."
    },
    "Manali": {
        "coords": [32.2432, 77.1892],
        "hotel_rate": "₹2,000 - ₹5,000 / night",
        "food_rate": "₹600 - ₹1,200 / day",
        "travel_rate": "₹1,000 - ₹2,500 / day (Local Cabs/Buses)",
        "desc": "Snow-capped mountains, adventure sports, and scenic valleys."
    },
    "Kerala": {
        "coords": [10.8505, 76.2711],
        "hotel_rate": "₹3,000 - ₹7,000 / night",
        "food_rate": "₹700 - ₹1,400 / day",
        "travel_rate": "₹800 - ₹2,000 / day (Houseboats/Cabs)",
        "desc": "Serene backwaters, lush green tea gardens, and Ayurveda resorts."
    },
    "Jaipur": {
        "coords": [26.9124, 75.7873],
        "hotel_rate": "₹1,800 - ₹4,500 / night",
        "food_rate": "₹500 - ₹1,000 / day",
        "travel_rate": "₹400 - ₹1,000 / day (Auto/Rickshaw)",
        "desc": "Majestic forts, royal palaces, and rich Rajasthani culture."
    }
}

@app.route('/')
def home():
    return render_template('index.html', destinations=DESTINATIONS)

@app.route('/api/generate-plan', methods=['POST'])
def generate_plan():
    data = request.json
    dest = data.get('destination', 'Goa')
    budget = int(data.get('budget', 15000))
    
    details = DESTINATIONS.get(dest, DESTINATIONS["Goa"])
    
    # Simple rule-based AI logic calculation
    response_data = {
        "destination": dest,
        "coordinates": details["coords"],
        "hotel_rate": details["hotel_rate"],
        "food_rate": details["food_rate"],
        "travel_rate": details["travel_rate"],
        "description": details["desc"],
        "optimized_itinerary": [
            f"Day 1: Arrival, check-in at recommended stay, evening leisure exploration.",
            f"Day 2: Core sightseeing of major cultural/natural landmarks.",
            f"Day 3: Local food trail, souvenir shopping, and departure."
        ],
        "budget_analysis": f"Optimized efficiently for your target budget of ₹{budget}."
    }
    return jsonify(response_data)

if __name__ == '__main__':
    pass
