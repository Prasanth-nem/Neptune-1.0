# data.py
"""
Neptune 1.0 - Data Module
Contains research data for 5 EPN species – exact match to the research document.
"""

SPECIES_DATA = {
    "Heterorhabditis indica": {
        "name": "Heterorhabditis indica",
        "common_name": "H. indica",
        "soil_moisture": {"min": 8, "max": 18, "unit": "%"},
        "soil_temperature": {"min": 25, "max": 30, "unit": "°C"},
        "atmospheric_temperature": {"min": 15, "max": 35, "unit": "°C"},
        "ph": {"min": 5.5, "max": 7.0, "up_to": 9.2},
        "relative_humidity": {"min": 90, "unit": "%"},
        "preferred_soils": ["Sandy Loam", "Sand", "Light Clay-Sand"],
        "porosity": {"min": 40, "max": 60, "unit": "%"},
        "bulk_density": {"min": 1.15, "max": 1.30, "unit": "g/cm³"},
        "ec": {"min": 0.0, "max": 2.0, "unit": "dS/m", "decline_at": 4.0, "blocked_at": 30.0},
        "saline_tolerance": {"max": 50.0, "unit": "dS/m"},
        "sodic_tolerance": {"max": 12, "unit": "ESP%", "reduced_at": 15},
        "penetration_depth": {
            "typical": {"min": 10, "max": 20, "unit": "cm"},
            "sandy_optimum": 30,
            "clay": 5,
        },
        "pests": [
            "White Grubs",
            "Fall Armyworm",
            "Tobacco Caterpillar",
            "Cutworm",
            "Cotton Bollworm",
            "Oriental Fruit Fly",
            "Banana Weevil Borer",
            "Diamondback Moth",
            "Ash weevil",
        ],
        "description": "Heterorhabditis indica is a highly effective EPN for controlling a wide range of soil‑dwelling pests. It has excellent host‑finding ability and tolerates varied soil conditions. Effective against White Grubs, Fall Armyworm, and many others.",
        "icon": "🐛",
        "color": "#2E7D32",
    },
    "Steinernema siamkayai": {
        "name": "Steinernema siamkayai",
        "common_name": "S. siamkayai",
        "soil_moisture": {"min": 15, "max": 20, "unit": "%"},
        "soil_temperature": {"min": 25, "max": 30, "unit": "°C"},
        "atmospheric_temperature": {"min": 20, "max": 35, "unit": "°C"},
        "ph": {"min": 3.0, "max": 7.0, "up_to": 8.5},
        "relative_humidity": {"min": 90, "unit": "%"},
        "preferred_soils": ["Sand", "Sandy Loam", "Sandy Clay Loam"],
        "porosity": {"min": 45, "max": 52, "unit": "%"},
        "bulk_density": {"min": 1.25, "max": 1.45, "unit": "g/cm³"},
        "ec": {"min": 0.5, "max": 1.5, "unit": "dS/m", "decline_at": 3.0},
        "saline_tolerance": {"min": 15.0, "max": 20.0, "unit": "dS/m"},
        "sodic_tolerance": {"max": 8, "unit": "ESP%"},
        "penetration_depth": {
            "typical": {"min": 5, "max": 15, "unit": "cm"},
            "clay": 10,
        },
        "pests": [
            "Guava Fruit Fly",
            "Solanum Fruit Fly",
            "Oriental Fruit Fly",
            "Fall Armyworm",
            "Tobacco Caterpillar",
            "Tomato Fruit Borer",
            "Diamondback Moth",
            "Ash weevil",
        ],
        "description": "Steinernema siamkayai is a versatile EPN effective against a broad spectrum of pests. It performs well across a wide pH range and tolerates temperatures up to 35°C. It is particularly effective in sandy soils.",
        "icon": "🪱",
        "color": "#1565C0",
    },
    "Steinernema glaseri": {
        "name": "Steinernema glaseri",
        "common_name": "S. glaseri",
        "soil_moisture": {"min": 19, "max": 25, "unit": "%"},
        "soil_temperature": {"min": 20, "max": 28, "unit": "°C"},
        "atmospheric_temperature": {"min": 15, "max": 25, "unit": "°C"},
        "ph": {"min": 5.5, "max": 7.5, "up_to": 7.5},
        "relative_humidity": {"min": 90, "unit": "%"},
        "preferred_soils": ["Sand", "Fine Sand", "Loamy Sand"],
        "porosity": {"min": 46, "max": 54, "unit": "%"},
        "bulk_density": {"min": 1.15, "max": 1.35, "unit": "g/cm³"},
        "ec": {"min": 0.0, "max": 2.0, "unit": "dS/m", "decline_at": 4.0},
        "saline_tolerance": {"min": 30.0, "max": 50.0, "unit": "dS/m"},
        "sodic_tolerance": {"max": 10, "unit": "ESP%"},
        "penetration_depth": {
            "typical": {"min": 15, "max": 30, "unit": "cm"},
        },
        "pests": [
            "Fall Armyworm",
            "Beet Armyworm",
        ],
        "description": "Steinernema glaseri is highly effective against cutworms, armyworms, and mole crickets. It penetrates deep into the soil (15‑30 cm) and thrives in coarse sandy soils. Tolerates high salinity.",
        "icon": "🐛",
        "color": "#E65100",
    },
    "Steinernema carpocapsae": {
        "name": "Steinernema carpocapsae",
        "common_name": "S. carpocapsae",
        "soil_moisture": {"min": 10, "max": 20, "unit": "%"},
        "soil_temperature": {"min": 22, "max": 28, "unit": "°C"},
        "atmospheric_temperature": {"min": 15, "max": 28, "unit": "°C"},
        "ph": {"min": 5.0, "max": 8.0, "up_to": 8.0},
        "relative_humidity": {"min": 90, "unit": "%"},
        "preferred_soils": ["Sandy Loam", "Loam", "Silt Loam"],
        "porosity": {"min": 40, "max": 50, "unit": "%"},
        "bulk_density": {"min": 1.20, "max": 1.50, "unit": "g/cm³"},
        "ec": {"min": 0.0, "max": 2.5, "unit": "dS/m", "decline_at": 4.0},
        "saline_tolerance": {"max": 25.0, "unit": "dS/m"},
        "sodic_tolerance": {"max": 8, "unit": "ESP%"},
        "penetration_depth": {
            "typical": {"min": 1, "max": 5, "unit": "cm"},
        },
        "pests": [
            "Ash weevil",
            "Fall Armyworm",
        ],
        "description": "Steinernema carpocapsae is an ambush forager, effective against surface‑dwelling pests. It penetrates only to 5 cm, making it ideal for targeting pests near the soil surface. Controls Ash weevil and Fall Armyworm.",
        "icon": "🪱",
        "color": "#7B1FA2",
    },
    "Heterorhabditis bacteriophora": {
        "name": "Heterorhabditis bacteriophora",
        "common_name": "H. bacteriophora",
        "soil_moisture": {"min": 15, "max": 25, "unit": "%"},
        "soil_temperature": {"min": 25, "max": 30, "unit": "°C"},
        "atmospheric_temperature": {"min": 18, "max": 32, "unit": "°C"},
        "ph": {"min": 6.0, "max": 7.5, "up_to": 7.5},
        "relative_humidity": {"min": 95, "unit": "%"},
        "preferred_soils": ["Sand", "Sandy Loam", "Loamy Sand"],
        "porosity": {"min": 43, "max": 55, "unit": "%"},
        "bulk_density": {"min": 1.15, "max": 1.35, "unit": "g/cm³"},
        "ec": {"min": 0.0, "max": 2.0, "unit": "dS/m", "decline_at": 4.0},
        "saline_tolerance": {"max": 35.0, "unit": "dS/m"},
        "sodic_tolerance": {"max": 12, "unit": "ESP%"},
        "penetration_depth": {
            "typical": {"min": 10, "max": 35, "unit": "cm"},
        },
        "pests": [
            "Banana Weevil Borer",
        ],
        "description": "Heterorhabditis bacteriophora is a powerful EPN with deep penetration (10‑35 cm). It is highly effective against white grubs and banana weevil borers. Requires high humidity (>95%).",
        "icon": "🐛",
        "color": "#00838F",
    },
}

# Build pest mapping
PEST_MAPPING = {}
for species, data in SPECIES_DATA.items():
    for pest in data["pests"]:
        if pest not in PEST_MAPPING:
            PEST_MAPPING[pest] = []
        PEST_MAPPING[pest].append(species)

ALL_PESTS = sorted(PEST_MAPPING.keys())
SPECIES_NAMES = list(SPECIES_DATA.keys())

SOIL_TYPES = sorted(
    set(
        soil
        for species in SPECIES_DATA.values()
        for soil in species["preferred_soils"]
    )
)

def get_species_for_pest(pest_name):
    return PEST_MAPPING.get(pest_name, [])

def get_pests_for_species(species_name):
    if species_name in SPECIES_DATA:
        return SPECIES_DATA[species_name]["pests"]
    return []

def get_species_data(species_name):
    return SPECIES_DATA.get(species_name, None)

def get_all_parameter_names():
    return ["Soil Type", "pH", "Soil Moisture", "Soil Temperature", "EC"]

def get_parameter_display_name(param):
    mapping = {
        "soil_type": "Soil Type",
        "ph": "pH",
        "soil_moisture": "Soil Moisture",
        "soil_temperature": "Soil Temperature",
        "ec": "EC",
    }
    return mapping.get(param, param)

def get_parameter_key(param):
    mapping = {
        "Soil Type": "soil_type",
        "pH": "ph",
        "Soil Moisture": "soil_moisture",
        "Soil Temperature": "soil_temperature",
        "EC": "ec",
    }
    return mapping.get(param, param.lower().replace(" ", "_"))

def validate_parameter(param_name, value):
    param_key = get_parameter_key(param_name)
    if param_key == "soil_type":
        return value in SOIL_TYPES, f"Must be one of: {', '.join(SOIL_TYPES)}"
    elif param_key == "ph":
        try:
            v = float(value)
            return 0 <= v <= 14, "pH must be between 0 and 14"
        except:
            return False, "Please enter a valid number"
    elif param_key == "soil_moisture":
        try:
            v = float(value)
            return 0 <= v <= 100, "Soil moisture must be between 0% and 100%"
        except:
            return False, "Please enter a valid number"
    elif param_key == "soil_temperature":
        try:
            v = float(value)
            return -10 <= v <= 60, "Temperature must be between -10°C and 60°C"
        except:
            return False, "Please enter a valid number"
    elif param_key == "ec":
        try:
            v = float(value)
            return 0 <= v <= 100, "EC must be between 0 and 100 dS/m"
        except:
            return False, "Please enter a valid number"
    return True, ""
