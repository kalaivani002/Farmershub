import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import requests

# ------------------ Page Config ------------------
st.set_page_config(layout="wide", page_title="FarmersHub", page_icon="🌾")

# ------------------ Language Dictionary ------------------
languages = {
    "English": {
        "title": "FarmersHub - Empower Your Farming Journey",
        "weather": "Local Weather Updates",
        "crop_advisor": "Insightful Crop Recommendations",
        "market_prices": "Current Market Prices",
        "marketplace": "Digital Marketplace",
        "schemes": "Government Scheme Updates",
        "select_language": "Select Language",
        "select_state": "Select State",
        "select_village": "Select Village/Town",
        "showing_data": "Showing data for",
        "temperature": "Temperature",
        "humidity": "Humidity",
        "forecast": "Forecast",
        "village_input": "Village / Town",
        "soil_type": "Soil Type",
        "ph_level": "pH Level",
        "nitrogen": "Nitrogen (kg/ha)",
        "phosphorus": "Phosphorus (kg/ha)",
        "potassium": "Potassium (kg/ha)",
        "recommend": "Get Crop Recommendations",
        "recommended_crops": "Recommended Crops",
        "crop": "Crop",
        "price": "Price (₹/kg)",
        "product_name": "Product Name",
        "price_kg": "Price per kg",
        "quantity": "Quantity (kg)",
        "contact_info": "Contact Info",
        "post_listing": "Post Listing",
        "product_success": "Product listed successfully!",
        "scheme_1": "PM-KISAN: ₹6000 yearly income support to all farmers.",
        "scheme_2": "PMFBY: Crop insurance at low premium.",
        "scheme_3": "eNAM: Digital platform for buying and selling.",
        "scheme_4": "Soil Health Card: Free testing & crop advice."
    },
    "தமிழ்": {
        "title": "விவசாயி மையம் - உங்கள் விவசாய பயணத்தை மேம்படுத்துங்கள்",
        "weather": "மூல்நிலை வானிலை புதுப்பிப்புகள்",
        "crop_advisor": "பயனுள்ள பயிர் பரிந்துரைகள்",
        "market_prices": "தற்போதைய சந்தை விலைகள்",
        "marketplace": "டிஜிட்டல் சந்தை",
        "schemes": "அரசுத் திட்டங்கள்",
        "select_language": "மொழியை தேர்ந்தெடுங்கள்",
        "select_state": "மாநிலத்தை தேர்ந்தெடுக்கவும்",
        "select_village": "கிராமம் / நகரம் தேர்ந்தெடுக்கவும்",
        "showing_data": "தரவு காண்பிக்கப்படுகிறது:",
        "temperature": "வெப்பநிலை",
        "humidity": "ஈரப்பதம்",
        "forecast": "வானிலை கணிப்பு",
        "village_input": "கிராமம் / நகரம்",
        "soil_type": "மண் வகை",
        "ph_level": "pH நிலை",
        "nitrogen": "நைட்ரஜன் (kg/ha)",
        "phosphorus": "பாஸ்பரஸ் (kg/ha)",
        "potassium": "பொட்டாசியம் (kg/ha)",
        "recommend": "பயிர் பரிந்துரை பெறுங்கள்",
        "recommended_crops": "பரிந்துரைக்கப்பட்ட பயிர்கள்",
        "crop": "பயிர்",
        "price": "விலை (₹/kg)",
        "product_name": "தயாரிப்பு பெயர்",
        "price_kg": "கிலோகிராம் ஒன்றுக்கு விலை",
        "quantity": "அளவு (kg)",
        "contact_info": "தொடர்பு தகவல்",
        "post_listing": "பதிவேற்றுக",
        "product_success": "தயாரிப்பு வெற்றிகரமாக பதிவேற்றப்பட்டது!",
        "scheme_1": "PM-KISAN: ஆண்டுக்கு ₹6000 விவசாயிகளுக்கு ஆதரவு.",
        "scheme_2": "PMFBY: குறைந்த விலையில் பயிர் காப்பீடு.",
        "scheme_3": "eNAM: வாங்க & விற்க டிஜிட்டல் தளம்.",
        "scheme_4": "மண் சுகாதார அட்டை: இலவச சோதனை மற்றும் ஆலோசனை."
    },
    "हिन्दी": {
        "title": "किसान केंद्र - अपनी खेती की यात्रा को सशक्त बनाएं",
        "weather": "स्थानीय मौसम अपडेट",
        "crop_advisor": "सूझबूझ वाली फसल सिफारिशें",
        "market_prices": "वर्तमान बाजार मूल्य",
        "marketplace": "डिजिटल मार्केटप्लेस",
        "schemes": "सरकारी योजनाएं",
        "select_language": "भाषा चुनें",
        "select_state": "राज्य चुनें",
        "select_village": "गाँव / शहर चुनें",
        "showing_data": "जानकारी दिखा रहा है:",
        "temperature": "तापमान",
        "humidity": "नमी",
        "forecast": "पूर्वानुमान",
        "village_input": "गाँव / शहर",
        "soil_type": "मिट्टी का प्रकार",
        "ph_level": "pH स्तर",
        "nitrogen": "नाइट्रोजन (kg/ha)",
        "phosphorus": "फास्फोरस (kg/ha)",
        "potassium": "पोटैशियम (kg/ha)",
        "recommend": "फसल सिफारिश प्राप्त करें",
        "recommended_crops": "अनुशंसित फसलें",
        "crop": "फसल",
        "price": "कीमत (₹/kg)",
        "product_name": "उत्पाद का नाम",
        "price_kg": "प्रति किलोग्राम मूल्य",
        "quantity": "मात्रा (kg)",
        "contact_info": "संपर्क जानकारी",
        "post_listing": "सूची पोस्ट करें",
        "product_success": "उत्पाद सफलतापूर्वक जोड़ा गया!",
        "scheme_1": "PM-KISAN: सभी किसानों को ₹6000 वार्षिक सहायता.",
        "scheme_2": "PMFBY: कम प्रीमियम में फसल बीमा.",
        "scheme_3": "eNAM: खरीदने और बेचने के लिए डिजिटल प्लेटफॉर्म.",
        "scheme_4": "मिट्टी स्वास्थ्य कार्ड: मुफ्त परीक्षण और सलाह."
    }
    # Add other languages (Tamil, Hindi) here if needed
}

# ------------------ Top Bar ------------------
col1, col2 = st.columns([10, 1])
with col2:
    lang_choice = st.selectbox("🌐", list(languages.keys()), label_visibility="collapsed")
L = languages[lang_choice]

# ------------------ Header ------------------
st.markdown(f"<h1 style='text-align: center'>{L['title']}</h1>", unsafe_allow_html=True)

# ------------------ Static Data ------------------
df = pd.read_csv('states_and_districts.csv')
states_villages = {state: df[df['State'] == state]['District'].tolist() for state in df['State'].unique()}

# ------------------ Menu ------------------
selected_tab = option_menu(
    menu_title=None,
    options=[L["weather"], L["crop_advisor"], L["market_prices"], L["marketplace"], L["schemes"]],
    orientation="horizontal",
)

# ------------------ State/Village ------------------
state = st.selectbox(L["select_state"], list(states_villages.keys()))
village = st.selectbox(L["select_village"], states_villages[state])

# ------------------ WEATHER ------------------
def get_weather_from_api(village, state):
    # API Key for OpenWeatherMap (replace 'YOUR_API_KEY' with your actual API key)
    api_key = "e82ac14a7e3449f283b9622c41e505f6"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the full URL for the request
    complete_url = f"{base_url}q={village},{state}&appid={api_key}&units=metric"
    
    # Get the response
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_data = data["weather"][0]
        forecast = weather_data["description"]
        return temperature, humidity, forecast
    else:
        return None, None, None

if selected_tab == L["weather"]:
    st.subheader(f"☁️ {L['weather']}")
    st.success(f"{L['showing_data']} {village}, {state}")

    # Fetch weather data using the API
    temp, humidity, forecast = get_weather_from_api(village, state)
    
    if temp and humidity and forecast:
        st.metric(label=L["temperature"], value=f"{temp}°C")
        st.metric(label=L["humidity"], value=f"{humidity}%")
        st.metric(label=L["forecast"], value=forecast.capitalize())
    else:
        st.error("Unable to fetch weather data")

# ------------------ CROP ADVISOR ------------------
elif selected_tab == L["crop_advisor"]:
    st.subheader(f"🌱 {L['crop_advisor']}")
    with st.form("crop_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input(L["village_input"], value=village)
            st.selectbox(L["soil_type"], ["Alluvial", "Black", "Red"])
        with col2:
            ph_level = st.number_input(L["ph_level"], step=0.1)
            nitrogen = st.number_input(L["nitrogen"])
            phosphorus = st.number_input(L["phosphorus"])
            potassium = st.number_input(L["potassium"])

        if st.form_submit_button(L["recommend"]):
            # Crop recommendation logic
            if ph_level >= 5.5 and ph_level <= 7.5:
                recommended_crops = "Rice, Wheat, Maize"
            else:
                recommended_crops = "Sugarcane, Banana, Groundnut"
            st.success(f"{L['recommended_crops']}: {recommended_crops}")

# ------------------ MARKET PRICES ------------------
elif selected_tab == L["market_prices"]:
    st.subheader(f"💹 {L['market_prices']}")
    st.table({
        L["crop"]: ["Rice", "Wheat", "Onion", "Tomato"],
        L["price"]: ["₹30", "₹25", "₹20", "₹18"]
    })

# ------------------ MARKETPLACE ------------------
elif selected_tab == L["marketplace"]:
    st.subheader(f"🛒 {L['marketplace']}")
    with st.form("market_form"):
        product_name = st.text_input(L["product_name"])
        price_kg = st.text_input(L["price_kg"])
        quantity = st.text_input(L["quantity"])
        contact_info = st.text_input(L["contact_info"])

        if st.form_submit_button(L["post_listing"]):
            st.success(f"✅ {L['product_success']}")
            # Store product data temporarily (e.g., in an in-memory list or a database)
            # You can expand this part to save listings persistently in a database
            st.write(f"Product: {product_name}, Price: {price_kg} ₹/kg, Quantity: {quantity} kg, Contact: {contact_info}")

# ------------------ GOVERNMENT SCHEMES ------------------
elif selected_tab == L["schemes"]:
    st.subheader(f"📜 {L['schemes']}")
    st.info(f"🔹 {L['scheme_1']}")
    st.info(f"🔹 {L['scheme_2']}")
    st.info(f"🔹 {L['scheme_3']}")
    st.info(f"🔹 {L['scheme_4']}")
