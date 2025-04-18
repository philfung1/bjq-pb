import streamlit as st
from logic_air import generate_positive_air_checklist, get_air_equipment_recommendations
from logic_water import generate_positive_water_checklist, get_water_equipment_recommendations
from logic_energy import generate_positive_energy_checklist, get_energy_equipment_recommendations
from logic_food import generate_positive_food_checklist, get_food_equipment_recommendations
from logic_wellbeing import generate_positive_wellbeing_checklist, get_wellbeing_equipment_recommendations

# --- Require user to confirm they've read the one-pager ---
if "confirmed_read" not in st.session_state:
    st.session_state.confirmed_read = False

if not st.session_state.confirmed_read:
    st.title("Welcome to BJQ-PB")
    st.markdown("Before using this prototype, please read the one-page overview of BJQ-PB.")
    st.markdown("📄 [Click here to read the PDF one-pager](https://your-link-to-BJQ-PB.pdf)")

    st.markdown("**BJQ-PB is a design support engine. All users must understand its purpose and limits before proceeding.**")

    if st.checkbox("I have read and understood the BJQ-PB one-pager."):
        st.session_state.confirmed_read = True
        st.experimental_rerun()
    else:
        st.stop()

# --- Initialize session state ---
if "design_recommendations" not in st.session_state:
    st.session_state.design_recommendations = []

if "equipment_recommendations" not in st.session_state:
    st.session_state.equipment_recommendations = []

st.set_page_config(page_title="BJQ-PB | Design Recommendations", layout="centered")
st.title("BJQ-PB: Positive Building Design Recommendations")

st.markdown("""
Select a Positive Building design category below and BJQ-PB will generate a customized set of design and equipment recommendations based on your project.
""")

# --- Module Selector ---
module = st.selectbox("Select Positive Building Module", [
    "Positive Air",
    "Positive Water",
    "Positive Energy",
    "Positive Food",
    "Positive Mental Well-being"
])

# --- Shared Inputs ---
project_name = st.text_input("Project Name")
project_type = st.selectbox("Project Type", ["Residential", "Commercial", "Institutional"])
location = st.text_input("Project Location")
floor_area = st.number_input("Total Conditioned Floor Area (ft²)", min_value=500)
orientation = st.selectbox("Primary Building Orientation", ["North", "South", "East", "West", "Mixed"])

# --- Locked Framework ---
frameworks = ["Positive Building"]
st.markdown("**Framework in use:** Positive Building")

# --- Generate Design Recommendations ---
if st.button("Generate Design Recommendations"):
    if not project_name:
        st.warning("Please enter a project name.")
    else:
        if module == "Positive Air":
            checklist = generate_positive_air_checklist(project_type, frameworks, location, floor_area, orientation)
        elif module == "Positive Water":
            checklist = generate_positive_water_checklist(project_type, frameworks, location, floor_area, orientation)
        elif module == "Positive Energy":
            checklist = generate_positive_energy_checklist(project_type, frameworks, location, floor_area, orientation)
        elif module == "Positive Food":
            checklist = generate_positive_food_checklist(project_type, frameworks, location, floor_area, orientation)
        elif module == "Positive Mental Well-being":
            checklist = generate_positive_wellbeing_checklist(project_type, frameworks, location, floor_area, orientation)
        else:
            checklist = []

        st.session_state.design_recommendations = checklist

# --- Generate Equipment Recommendations ---
if st.button("Generate Equipment Recommendations"):
    if module == "Positive Air":
        equipment = get_air_equipment_recommendations()
    elif module == "Positive Water":
        equipment = get_water_equipment_recommendations()
    elif module == "Positive Energy":
        equipment = get_energy_equipment_recommendations()
    elif module == "Positive Food":
        equipment = get_food_equipment_recommendations()
    elif module == "Positive Mental Well-being":
        equipment = get_wellbeing_equipment_recommendations()
    else:
        equipment = []

    st.session_state.equipment_recommendations = equipment

# --- Always display stored outputs ---
if st.session_state.design_recommendations:
    st.subheader(f"{module} Design Recommendations for: {project_name}")
    for item in st.session_state.design_recommendations:
        st.markdown(f"- {item}")

if st.session_state.equipment_recommendations:
    st.subheader(f"{module} Equipment Recommendations")
    for item in st.session_state.equipment_recommendations:
        st.markdown(f"- {item}")