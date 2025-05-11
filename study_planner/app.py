import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import json
import os
from typing import List, Dict, Optional
import uuid

class Subject:
    def __init__(self, name: str, duration: int = 60, priority: str = "Medium", resources: List[str] = None):
        self.name = name
        self.duration = duration  # in minutes
        self.priority = priority  # Low, Medium, High
        self.resources = resources or []
        self.id = str(uuid.uuid4())  # Unique ID for each subject
    
    def to_dict(self):
        return {
            "name": self.name,
            "duration": self.duration,
            "priority": self.priority,
            "resources": self.resources,
            "id": self.id
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        subject = cls(
            name=data["name"],
            duration=data["duration"],
            priority=data["priority"],
            resources=data.get("resources", [])
        )
        subject.id = data.get("id", str(uuid.uuid4()))
        return subject

class StudyPlanner:
    def __init__(self):
        self.schedule = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": []
        }
        self.goals = []
        self.study_stats = {}
        self.file_path = "study_planner_data.json"
        self.load_data()
    
    def add_subject(self, day: str, subject: Subject) -> None:
        if day in self.schedule:
            # Check for duplicate subjects by name and day
            if any(s.name.lower() == subject.name.lower() for s in self.schedule[day]):
                raise ValueError(f"'{subject.name}' already exists on {day}")
            self.schedule[day].append(subject)
            self.save_data()
    
    def remove_subject(self, day: str, subject_id: str) -> None:
        if day in self.schedule:
            self.schedule[day] = [subj for subj in self.schedule[day] if subj.id != subject_id]
            self.save_data()
    
    def clear_day(self, day: str) -> None:
        if day in self.schedule:
            self.schedule[day] = []
            self.save_data()
    
    def get_schedule(self) -> Dict[str, List[Subject]]:
        return self.schedule
    
    def add_goal(self, goal: str, deadline: str) -> None:
        self.goals.append({
            "goal": goal, 
            "deadline": deadline, 
            "completed": False,
            "id": str(uuid.uuid4())
        })
        self.save_data()
    
    def mark_goal_complete(self, goal_id: str) -> None:
        for goal in self.goals:
            if goal["id"] == goal_id:
                goal["completed"] = True
                self.save_data()
                break
    
    def record_study_time(self, day: str, minutes: int) -> None:
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in self.study_stats:
            self.study_stats[today] = 0
        self.study_stats[today] += minutes
        self.save_data()
    
    def get_weekly_study_time(self) -> int:
        today = datetime.now()
        week_start = today - timedelta(days=today.weekday())
        weekly_total = 0
        
        for i in range(7):
            date = (week_start + timedelta(days=i)).strftime("%Y-%m-%d")
            weekly_total += self.study_stats.get(date, 0)
        
        return weekly_total
    
    def save_data(self) -> None:
        data = {
            "schedule": {day: [subj.to_dict() for subj in subjects] 
                        for day, subjects in self.schedule.items()},
            "goals": self.goals,
            "study_stats": self.study_stats
        }
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
    
    def load_data(self) -> None:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.schedule = {
                    day: [Subject.from_dict(subj) for subj in subjects]
                    for day, subjects in data.get("schedule", {}).items()
                }
                self.goals = data.get("goals", [])
                self.study_stats = data.get("study_stats", {})

# Initialize planner
if 'planner' not in st.session_state:
    st.session_state.planner = StudyPlanner()

# Custom CSS 
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stTextInput input, .stTextArea textarea {
        border-radius: 20px;
    }
    .stSelectbox select {
        border-radius: 20px;
    }
    .stButton button {
        border-radius: 20px;
        border: 1px solid #4CAF50;
        background-color: #4CAF50;
        color: white;
        padding: 8px 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .day-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .day-header {
        color: #4CAF50;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subject-item {
        padding: 8px;
        margin: 5px 0;
        background-color: #f0f8ff;
        border-radius: 5px;
        display: flex;
        justify-content: space-between;
    }
    .priority-high {
        border-left: 4px solid #ff4b4b;
    }
    .priority-medium {
        border-left: 4px solid #ffa500;
    }
    .priority-low {
        border-left: 4px solid #4CAF50;
    }
    .remove-btn {
        color: red;
        cursor: pointer;
    }
    .title {
        color: #4CAF50;
        text-align: center;
    }
    .goal-item {
        padding: 10px;
        margin: 5px 0;
        background-color: #fffacd;
        border-radius: 5px;
    }
    .completed-goal {
        text-decoration: line-through;
        opacity: 0.7;
    }
    .error-message {
        color: red;
        padding: 10px;
        border-radius: 5px;
        background-color: #ffebee;
    }
    </style>
""", unsafe_allow_html=True)

#  Title
st.markdown("<h1 class='title'>📚 Study Planner</h1>", unsafe_allow_html=True)

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", ["Schedule", "Goals", "Statistics", "Settings"])

# Current week display
current_week = datetime.now().isocalendar()[1]
st.sidebar.markdown(f"<p style='text-align:center;'>📅 Week {current_week}</p>", unsafe_allow_html=True)

# Progress tracker
total_subjects = sum(len(subjects) for subjects in st.session_state.planner.schedule.values())
st.sidebar.progress(min(total_subjects/30, 1))
st.sidebar.caption(f"Total subjects scheduled: {total_subjects}/30")

# Main content based on menu selection
if menu == "Schedule":
    st.header("📅 Weekly Study Schedule")
    
    with st.expander("➕ Add New Subject", expanded=False):
        with st.form("add_subject_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                day = st.selectbox("Day", list(st.session_state.planner.schedule.keys()))
                subject_name = st.text_input("Subject Name*", placeholder="Enter subject name")
            with col2:
                duration = st.number_input("Duration (minutes)*", min_value=15, step=15, value=60)
                priority = st.selectbox("Priority*", ["Low", "Medium", "High"])
            
            resources = st.text_area("Resources (comma separated)", placeholder="Textbooks, websites, etc.")
            
            submitted = st.form_submit_button("Add Subject")
            if submitted:
                if subject_name and duration:
                    try:
                        resources_list = [r.strip() for r in resources.split(",")] if resources else []
                        subject = Subject(
                            name=subject_name,
                            duration=duration,
                            priority=priority,
                            resources=resources_list
                        )
                        st.session_state.planner.add_subject(day, subject)
                        st.success(f"Added '{subject_name}' to {day}")
                    except ValueError as e:
                        st.error(str(e))
                else:
                    st.warning("Please fill all required fields (*)")

    # Display schedule
    tab1, tab2 = st.tabs(["📊 Table View", "🃏 Card View"])
    
    with tab1:
        # Create a DataFrame for display
        schedule_data = []
        for day, subjects in st.session_state.planner.schedule.items():
            for subject in subjects:
                schedule_data.append({
                    "Day": day,
                    "Subject": subject.name,
                    "Duration": f"{subject.duration} min",
                    "Priority": subject.priority,
                    "Resources": ", ".join(subject.resources)
                })
        
        if schedule_data:
            st.dataframe(pd.DataFrame(schedule_data), use_container_width=True)
        else:
            st.info("No subjects scheduled yet. Add some subjects to get started!")
    
    with tab2:
        for day, subjects in st.session_state.planner.schedule.items():
            with st.container():
                st.markdown(f"<div class='day-card'><div class='day-header'>{day}</div>", unsafe_allow_html=True)
                
                if subjects:
                    for subject in subjects:
                        priority_class = f"priority-{subject.priority.lower()}"
                        cols = st.columns([4, 1])
                        with cols[0]:
                            st.markdown(
                                f"""<div class='subject-item {priority_class}'>
                                    <strong>{subject.name}</strong><br>
                                    ⏱️ {subject.duration} min | {subject.priority} priority<br>
                                    📚 {', '.join(subject.resources) if subject.resources else 'No resources'}
                                </div>""", 
                                unsafe_allow_html=True
                            )
                        with cols[1]:
                            # Use subject.id instead of name for unique key
                            if st.button("❌", key=f"del_{subject.id}"):
                                st.session_state.planner.remove_subject(day, subject.id)
                                st.rerun()
                else:
                    st.info("No subjects scheduled for this day")
                
                st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Goals":
    st.header("🎯 Study Goals")
    
    with st.expander("➕ Add New Goal", expanded=False):
        with st.form("add_goal_form", clear_on_submit=True):
            goal = st.text_input("Goal Description*", placeholder="What do you want to achieve?")
            deadline = st.date_input("Deadline*", min_value=datetime.now().date())
            
            submitted = st.form_submit_button("Add Goal")
            if submitted:
                if goal:
                    st.session_state.planner.add_goal(goal, deadline.strftime("%Y-%m-%d"))
                    st.success("Goal added successfully!")
                else:
                    st.warning("Please enter a goal description")
    
    st.subheader("Your Goals")
    if not st.session_state.planner.goals:
        st.info("No goals set yet. Add some goals to track your progress!")
    else:
        for i, goal in enumerate(st.session_state.planner.goals):
            goal_class = "completed-goal" if goal["completed"] else "goal-item"
            cols = st.columns([8, 2])
            with cols[0]:
                st.markdown(
                    f"""<div class='{goal_class}'>
                        <strong>{goal["goal"]}</strong><br>
                        Deadline: {goal["deadline"]}
                    </div>""", 
                    unsafe_allow_html=True
                )
            with cols[1]:
                if not goal["completed"]:
                    if st.button("✓", key=f"complete_{i}"):
                        st.session_state.planner.mark_goal_complete(goal["id"])
                        st.rerun()
                else:
                    st.write("✓")  # Show checkmark for completed goals

elif menu == "Statistics":
    st.header("📊 Study Statistics")
    
    # Weekly study time
    weekly_time = st.session_state.planner.get_weekly_study_time()
    st.subheader(f"📅 Weekly Study Time: {weekly_time // 60}h {weekly_time % 60}m")
    
    # Daily study time chart
    if st.session_state.planner.study_stats:
        stats_df = pd.DataFrame.from_dict(
            st.session_state.planner.study_stats, 
            orient="index", 
            columns=["Minutes"]
        ).sort_index()
        stats_df["Date"] = pd.to_datetime(stats_df.index)
        stats_df["Day"] = stats_df["Date"].dt.day_name()
        stats_df["Hours"] = stats_df["Minutes"] / 60
        
        st.bar_chart(stats_df, x="Day", y="Hours")
    else:
        st.info("No study statistics recorded yet")
    
    # Manual time entry
    with st.expander("⏱️ Record Study Time", expanded=False):
        with st.form("study_time_form"):
            day = st.selectbox("Day", list(st.session_state.planner.schedule.keys()))
            minutes = st.number_input("Minutes studied*", min_value=1, step=5, value=30)
            
            submitted = st.form_submit_button("Record Time")
            if submitted:
                st.session_state.planner.record_study_time(day, minutes)
                st.success(f"Recorded {minutes} minutes of study time for {day}")

elif menu == "Settings":
    st.header("⚙️ Settings")
    
    st.subheader("Data Management")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("📤 Export Data", expanded=False):
            st.write("Export your planner data in different formats:")
            
            # PDF Export Button
            if st.button("Export as PDF"):
                try:
                    from fpdf import FPDF
                    
                    # Create PDF
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    
                    # Add title
                    pdf.cell(200, 10, txt="Study Planner Export", ln=1, align="C")
                    pdf.ln(10)
                    
                    # Add schedule
                    pdf.set_font("Arial", "B", 14)
                    pdf.cell(200, 10, txt="Weekly Schedule", ln=1)
                    pdf.set_font("Arial", size=10)
                    
                    for day, subjects in st.session_state.planner.schedule.items():
                        pdf.cell(200, 10, txt=f"{day}:", ln=1)
                        for subject in subjects:
                            pdf.cell(200, 10, 
                                    txt=f"- {subject.name} ({subject.duration} mins, {subject.priority} priority)", 
                                    ln=1)
                    pdf.ln(5)
                    
                    # Add goals
                    pdf.set_font("Arial", "B", 14)
                    pdf.cell(200, 10, txt="Study Goals", ln=1)
                    pdf.set_font("Arial", size=10)
                    
                    for goal in st.session_state.planner.goals:
                        status = "[X]" if goal["completed"] else "[ ]"
                        pdf.cell(200, 10, 
                                txt=f"{status} {goal['goal']} (Deadline: {goal['deadline']})", 
                                ln=1)
                    
                    # Save PDF to bytes
                    pdf_output = pdf.output(dest="S").encode("latin1", errors="replace")
                    
                    # Download button
                    st.download_button(
                        label="Download PDF",
                        data=pdf_output,
                        file_name="study_planner_export.pdf",
                        mime="application/pdf"
                    )
                except ImportError:
                    st.error("PDF export requires fpdf package. Install with: pip install fpdf")
                except Exception as e:
                    st.error(f"Error generating PDF: {str(e)}")
            
            # Original JSON Export
            st.download_button(
                label="Export as JSON",
                data=json.dumps({
                    "schedule": {day: [subj.to_dict() for subj in subjects] 
                                for day, subjects in st.session_state.planner.schedule.items()},
                    "goals": st.session_state.planner.goals,
                    "study_stats": st.session_state.planner.study_stats
                }, indent=4),
                file_name="study_planner_backup.json",
                mime="application/json"
            )
    
    with col2:
        with st.expander("🔄 Reset Data", expanded=False):
            # Use a form to properly handle the confirmation flow
            with st.form("reset_form"):
                if st.form_submit_button("Reset All Data"):
                    if st.session_state.get("reset_confirmed", False):
                        # Clear the planner data
                        st.session_state.planner = StudyPlanner()
                        # Delete the data file if exists
                        if os.path.exists(st.session_state.planner.file_path):
                            os.remove(st.session_state.planner.file_path)
                        st.success("All data has been reset successfully!")
                        st.session_state.reset_confirmed = False
                        st.rerun()
                    else:
                        st.session_state.reset_confirmed = True
                        st.warning("Are you sure you want to reset all data? This cannot be undone. Click the button again to confirm.")
                
                # Show checkbox only if confirmation is needed
                if st.session_state.get("reset_confirmed", False):
                    if st.checkbox("I understand this will delete all my data permanently"):
                        if st.form_submit_button("Confirm Reset"):
                            st.session_state.planner = StudyPlanner()
                            if os.path.exists(st.session_state.planner.file_path):
                                os.remove(st.session_state.planner.file_path)
                            st.success("All data has been reset successfully!")
                            st.session_state.reset_confirmed = False
                            st.rerun()
    
  