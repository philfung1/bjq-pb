def generate_positive_water_checklist(project_type, frameworks, location, floor_area, orientation):
    checklist = []

    # Core Positive Water Recommendations
    checklist.append("Implement whole-house water filtration to remove physical, chemical, and microbial contaminants")
    checklist.append("Install low-flow, WaterSense-certified fixtures to reduce potable water use")
    checklist.append("Use non-PVC piping for domestic water distribution")
    checklist.append("Design for water-efficient landscaping and native plantings")

    # Framework-specific logic
    if "WELL" in frameworks:
        checklist.append("Test for heavy metals, microbes, and VOCs in incoming water supply")
        checklist.append("Provide clear signage and education about water safety and quality")

    if "LEED" in frameworks:
        checklist.append("Calculate baseline indoor water use and demonstrate at least 20% reduction")
        checklist.append("Meter and monitor water use by major end-use category")

    if "LBC" in frameworks:
        checklist.append("Use rainwater harvesting or greywater systems for non-potable uses")
        checklist.append("Avoid all red list plumbing materials and additives")

    if "Positive Building" in frameworks:
        checklist.append("Incorporate visible, easily understood feedback about water use")
        checklist.append("Use biomimicry or regenerative wetland strategies for site-level water cycling")
        checklist.append("Design for rainwater or condensate reuse as part of circular water system")

    # Location-specific guidance
    if location.lower() == "toronto":
        checklist.append("Include freeze protection for greywater systems and pipes near exterior walls")

    return checklist

def get_water_equipment_recommendations():
    return [
        "Whole-house activated carbon or multi-stage water filtration system",
        "WaterSense-certified low-flow fixtures (toilets, faucets, showers)",
        "Greywater system for non-potable uses (e.g., irrigation, flushing)",
        "Rainwater harvesting system with first-flush diverter and storage tank",
        "Condensate recovery system from HVAC for reuse",
        "Non-PVC piping (e.g., PEX, stainless steel, copper)"
    ]