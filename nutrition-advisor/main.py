import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
#from crewai import LLM
from langchain_community.chat_models import ChatOpenAI


st.set_page_config(page_title="Personalized Nutrition Advisor by DrylanD", page_icon="🥗", layout="wide")

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = "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"       #Groq API key
#os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"
os.environ['GROQ_API_KEY'] = "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"

def get_llm_openai():
    return ChatOpenAI(model_name="groq/llama3-8b-8192")

def create_agents():
    """Create the specialized nutrition agents."""
    llm = get_llm_openai()
    
    # Nutrition Researcher
    nutritionist = Agent(
        role='Nutrition Specialist',
        goal='Research and develop personalized nutritional recommendations based on scientific evidence',
        backstory='''You are a highly qualified nutritionist with expertise in therapeutic diets, 
                    nutrient interactions, and dietary requirements across different health conditions. 
                    Your recommendations are always backed by peer-reviewed research.''',
        llm=llm,
        verbose=True
    )
    
    # Medical Nutrition Specialist
    medical_specialist = Agent(
        role='Medical Nutrition Therapist',
        goal='Analyze medical conditions and provide appropriate dietary modifications',
        backstory='''With dual training in medicine and nutrition, you specialize in managing 
                    nutrition-related aspects of various medical conditions. You understand 
                    medication-food interactions and how to optimize nutrition within medical constraints.''',
        llm=llm,
        verbose=True
    )
    
    # Diet Plan Creator
    diet_planner = Agent(
        role='Therapeutic Diet Planner',
        goal='Create detailed, practical and enjoyable meal plans tailored to individual needs',
        backstory='''You excel at transforming clinical nutrition requirements into delicious, 
                    practical eating plans. You have extensive knowledge of food preparation, 
                    nutrient preservation, and food combinations that optimize both health and enjoyment.''',
        llm=llm,
        verbose=True
    )
    
    return nutritionist, medical_specialist, diet_planner

def create_tasks(nutritionist, medical_specialist, diet_planner, user_info):
    """Create tasks for each agent based on user information."""
    
    # First task: Research nutrition needs based on demographics
    demographics_research = Task(
        description=f'''Research nutritional needs for an individual with the following demographics:
            - Age: {user_info['age']}
            - Gender: {user_info['gender']}
            - Height: {user_info['height']}
            - Weight: {user_info['weight']}
            - Activity Level: {user_info['activity_level']}
            - Goals: {user_info['goals']}
            
            Provide detailed nutritional requirements including:
            1. Caloric needs 
            2. Macronutrient distribution
            3. Meal timing and frequency recommendations''',
        agent=nutritionist,
        expected_output="A comprehensive nutritional profile with scientific rationale"
    )
    
    # Second task: Analyze medical conditions and adjust nutritional recommendations
    medical_analysis = Task(
        description=f'''Analyze the following medical conditions and medications, then provide dietary modifications:
            - Medical Conditions: {user_info['medical_conditions']}
            - Medications: {user_info['medications']}
            - Allergies/Intolerances: {user_info['allergies']}
            
            Consider the baseline nutritional profile and provide:
            1. Specific nutrients to increase or limit based on each condition
            2. Food-medication interactions to avoid
            3. Potential nutrient deficiencies associated with these conditions/medications
            ''',
        agent=medical_specialist,
        context=[demographics_research],
        expected_output="A detailed analysis of medical nutrition therapy adjustments"
    )
    
    # Third task: Create the comprehensive diet plan
    diet_plan = Task(
        description=f'''Create a detailed, practical, dry fruit, nuts & seeds centric diet plan incorporating all information:
            - User's Food Preferences: {user_info['food_preferences']}
            - Cooking Skills/Time: {user_info['cooking_ability']}
            - Budget Constraints: {user_info['budget']}
            - Cultural/Religious Factors: {user_info['cultural_factors']}
            
            Develop a comprehensive nutrition plan that includes:
            1. Specific foods to eat daily, weekly, and occasionally with portion sizes
            2. A 7-day meal plan with specific meals and recipes
            3. Meal preparation tips and simple recipes
            ''',
        agent=diet_planner,
        context=[demographics_research, medical_analysis],
        expected_output="A comprehensive, practical, and personalized nutrition plan"
    )
    
    return [demographics_research, medical_analysis, diet_plan]

def create_crew(agents, tasks):
    """Create the CrewAI crew with the specified agents and tasks."""
    return Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )

def run_nutrition_advisor(user_info):
    """Run the nutrition advisor with the user information."""
    try:
        # Create agents
        nutritionist, medical_specialist, diet_planner = create_agents()
        
        # Create tasks
        tasks = create_tasks(nutritionist, medical_specialist, diet_planner, user_info)
        
        # Create crew
        crew = create_crew([nutritionist, medical_specialist, diet_planner], tasks)
        
        # Execute the crew
        with st.spinner('Our nutrition team is creating your personalized plan. This may take a few minutes...'):
            result = crew.kickoff()
        
        return result
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

def app():
    """Main Streamlit application."""
    #st.set_page_config(page_title="Personalized Nutrition Advisor", layout="wide")
    
    st.title("🥗 Your Personalized Nutrition Advisor by DrylanD")
    st.markdown("""
    Get a detailed nutrition plan based on your demographics, health conditions, and preferences.
    Our AI team of nutrition specialists will create a personalized recommendation just for you.
    """)
    
    # Create tabs for organization
    tab1, tab2, tab3 = st.tabs(["Basic Information", "Health Details", "Preferences & Lifestyle"])
    
    with tab1:
        st.header("Personal Information")
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("Age", min_value=1, max_value=120, value=30)
            gender = st.selectbox("Gender", ["Male", "Female", "Non-binary/Other"])
            height = st.text_input("Height (e.g., 5'10\" or 178 cm)", "5'10\"")
            
        with col2:
            weight = st.text_input("Weight (e.g., 160 lbs or 73 kg)", "160 lbs")
            activity_level = st.select_slider(
                "Activity Level",
                options=["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"]
            )
            goals = st.multiselect(
                "Nutrition Goals",
                ["Weight Loss", "Weight Gain", "Maintenance", "Muscle Building", "Better Energy", 
                 "Improved Athletic Performance", "Disease Management", "General Health"]
            )
    
    with tab2:
        st.header("Health Information")
        
        medical_conditions = st.text_area(
            "Medical Conditions (separate with commas)",
            placeholder="E.g., Diabetes Type 2, Hypertension, Hypothyroidism..."
        )
        
        medications = st.text_area(
            "Current Medications (separate with commas)",
            placeholder="E.g., Metformin, Lisinopril, Levothyroxine..."
        )
        
        allergies = st.text_area(
            "Food Allergies/Intolerances (separate with commas)",
            placeholder="E.g., Lactose, Gluten, Shellfish, Peanuts..."
        )
    
    with tab3:
        st.header("Preferences & Lifestyle")
        
        col1, col2 = st.columns(2)
        
        with col1:
            food_preferences = st.text_area(
                "Food Preferences & Dislikes",
                placeholder="E.g., Prefer plant-based, dislike seafood..."
            )
            
            cooking_ability = st.select_slider(
                "Cooking Skills & Available Time",
                options=["Very Limited", "Basic/Quick Meals", "Average", "Advanced/Can Spend Time", "Professional Level"]
            )
        
        with col2:
            budget = st.select_slider(
                "Budget Considerations",
                options=["Very Limited", "Budget Conscious", "Moderate", "Flexible", "No Constraints"]
            )
            
            cultural_factors = st.text_area(
                "Cultural or Religious Dietary Factors",
                placeholder="E.g., Halal, Kosher, Mediterranean tradition..."
            )
    
    # Collect all user information
    user_info = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "activity_level": activity_level,
        "goals": ", ".join(goals) if goals else "General health improvement",
        "medical_conditions": medical_conditions or "None reported",
        "medications": medications or "None reported",
        "allergies": allergies or "None reported",
        "food_preferences": food_preferences or "No specific preferences",
        "cooking_ability": cooking_ability,
        "budget": budget,
        "cultural_factors": cultural_factors or "No specific factors"
    }
 
    # Check if API keys are present
    
    #if not os.getenv("SERPER_API_KEY") or not os.getenv("OPENAI_API_KEY"):
    #    st.warning("⚠️ API keys not detected. Please add your SERPER_API_KEY and OPENAI_API_KEY to your .env file.")
    
    # Create a submission button
    if st.button("Generate Nutrition Plan"):
        if not goals:
            st.error("Please select at least one nutrition goal.")
            return
        
        # Display user information summary
        with st.expander("Summary of Your Information"):
            st.json(user_info)
        
        # Run the nutrition advisor
        result = run_nutrition_advisor(user_info)
        
        if result:
            st.success("✅ Your personalized nutrition plan is ready!")
            st.markdown("## Your Personalized Nutrition Plan")
            st.markdown(result)
            
            # Add download capability
            st.download_button(
                label="Download Nutrition Plan",
                data=str(result),
                file_name="my_nutrition_plan.md",
                mime="text/markdown"
            )

if __name__ == "__main__":
    app()