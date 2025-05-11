import streamlit as st
import time
from datetime import timedelta

# --------------------
# OOP Classes
# --------------------

class Session:
    def __init__(self, subject: str, total_duration: int, pomodoro_length: int = 25,
                 break_length: int = 5, long_break_length: int = 15):
        self.subject = subject
        self.total_duration = total_duration  # in minutes
        self.pomodoro_length = pomodoro_length  # in minutes
        self.break_length = break_length  # in minutes
        self.long_break_length = long_break_length  # in minutes
        self.completed_pomodoros = 0

    def add_pomodoro(self):
        self.completed_pomodoros += 1

    def remaining_time(self) -> int:
        done = self.completed_pomodoros * self.pomodoro_length
        return max(self.total_duration - done, 0)

    def is_complete(self) -> bool:
        return self.remaining_time() == 0


class Schedule:
    def __init__(self):
        if 'sessions' not in st.session_state:
            st.session_state.sessions = []
        self.sessions = st.session_state.sessions
        if 'current_index' not in st.session_state:
            st.session_state.current_index = 0
        self.current_index = st.session_state.current_index

    def add_session(self, session: Session):
        self.sessions.append(session)
        st.session_state.sessions = self.sessions

    def next_session(self):
        if self.current_index + 1 < len(self.sessions):
            st.session_state.current_index += 1
            self.current_index = st.session_state.current_index
            return True
        return False

    def current_session(self) -> Session:
        if self.sessions:
            return self.sessions[self.current_index]
        return None

    def reset(self):
        st.session_state.current_index = 0
        for s in self.sessions:
            s.completed_pomodoros = 0

    def generate_report(self) -> dict:
        total = sum([s.completed_pomodoros * s.pomodoro_length for s in self.sessions])
        return {
            'total_minutes_studied': total,
            'total_pomodoros': sum([s.completed_pomodoros for s in self.sessions]),
            'sessions_completed': sum([1 for s in self.sessions if s.is_complete()])
        }

# --------------------
# Timer Logic
# --------------------

def run_timer(minutes: int, label: str):
    placeholder = st.empty()
    total_seconds = minutes * 60
    start = time.time()
    while time.time() - start < total_seconds:
        remaining = total_seconds - int(time.time() - start)
        delta = timedelta(seconds=remaining)
        placeholder.markdown(f"**{label}**: {str(delta)} remaining")
        time.sleep(1)
    placeholder.markdown(f"**{label}**: Done!")

# --------------------
# Streamlit UI
# --------------------
st.title("📚 Study Planner with Pomodoro Timer")

schedule = Schedule()

with st.sidebar:
    st.header("Add New Session")
    subj = st.text_input("Subject/topic")
    tot = st.number_input("Total duration (minutes)", min_value=1, value=60)
    pomo = st.number_input("Pomodoro length (min)", min_value=1, value=25)
    brk = st.number_input("Short break (min)", min_value=1, value=5)
    lb = st.number_input("Long break (min)", min_value=1, value=15)
    if st.button("Add Session"):
        session = Session(subj, tot, pomo, brk, lb)
        schedule.add_session(session)
        st.experimental_rerun()

st.subheader("Today's Sessions")
for idx, sess in enumerate(schedule.sessions):
    status = "✅" if sess.is_complete() else f"🔄 {sess.completed_pomodoros}/{sess.total_duration//sess.pomodoro_length}"
    st.write(f"{idx+1}. **{sess.subject}** - {sess.total_duration} min | Completed: {status}")

if st.button("Start Study Day") and schedule.sessions:
    st.session_state.running = True
    schedule.reset()
    st.experimental_rerun()

if 'running' in st.session_state and st.session_state.running:
    cur = schedule.current_session()
    st.markdown(f"### Current Session: **{cur.subject}**")
    # Loop through pomodoros
    while not cur.is_complete():
        run_timer(cur.pomodoro_length, f"Work on {cur.subject}")
        cur.add_pomodoro()
        # Decide break
        if cur.completed_pomodoros % 4 == 0:
            run_timer(cur.long_break_length, "Long Break")
        else:
            run_timer(cur.break_length, "Short Break")
        st.experimental_rerun()
    # Session complete
    if schedule.next_session():
        st.experimental_rerun()
    else:
        # Day finished
        report = schedule.generate_report()
        st.success("🎉 All sessions completed!")
        st.write(f"Total minutes studied: {report['total_minutes_studied']}")
        st.write(f"Total pomodoros: {report['total_pomodoros']}")
        st.write(f"Sessions fully completed: {report['sessions_completed']}/{len(schedule.sessions)}")
        st.session_state.running = False
