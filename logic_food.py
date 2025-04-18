def generate_positive_food_checklist(project_type, frameworks, location, floor_area, orientation):
    checklist = []

    # Core Positive Food Recommendations
    checklist.append("Design for access to healthy, minimally processed food options")
    checklist.append("Include space for indoor food growing (e.g., kitchen garden, tower garden, aquaponics)")
    checklist.append("Support composting or nutrient cycling to reduce food waste")
    checklist.append("Design kitchen layouts to promote cooking, sharing, and wellbeing")

    # Framework-specific logic
    if "WELL" in frameworks:
        checklist.append("Support mindful eating through access to fruits, vegetables, and hydration")
        checklist.append("Provide food education signage or resources")
        checklist.append("Ensure refrigeration and storage supports food safety and nutrition")

    if "LBC" in frameworks:
        checklist.append("Integrate edible landscape features where possible")
        checklist.append("Use on-site composting for food scraps or nutrient return to soil")

    if "Positive Building" in frameworks:
        checklist.append("Design biophilic food environments that inspire care and gratitude")
        checklist.append("Support resilience by including perennial, regenerative, or local food systems")
        checklist.append("Integrate food systems with Positive Water and Energy cycles")

    # Climate or location-based logic
    if location.lower() == "toronto":
        checklist.append("Plan for season extension strategies in northern climate (e.g., cold frames, LED grow lighting)")

    return checklist

def get_food_equipment_recommendations():
    return [
        "Indoor growing systems (e.g., vertical hydroponics, tower garden, LED grow lights)",
        "Composting unit (indoor electric or outdoor thermal system)",
        "Food-safe storage containers and modular pantry shelving",
        "Water-efficient irrigation timer for edible landscapes",
        "Induction cooktop and energy-efficient appliances to support healthy cooking",
        "Smart refrigerator with food freshness tracking (optional)"
    ]