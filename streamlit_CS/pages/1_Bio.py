import os
import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Santos Adducci"
PROGRAM = "Your Program / Computer Science and General Mathematics / Student"
INTRO = (
    "Working on a lab for my data visualization class using Streamlit"
    "I love the idea of abstraction in computing. Everything is derived from basic logic" \
    "and clever physical systems. Everything that we do now could be constructed from some" \
    "basic axioms and truths. I like to think that data visualization is the interface between" \
    "logic and mankind"
)
FUN_FACTS = [
    "I love learn about everthing especially math and computers",
    "I’m learning about data visualization, algorithms, and real analysis right now",
    "I want to build a 3-D renderer",
]

PHOTO_PATH = os.path.join(os.path.dirname(__file__), "..", "BioDataVis.webp")
PHOTO_PATH = os.path.abspath(PHOTO_PATH)
#PHOTO_PATH = "BioDataVis.webp"  # Put a file in repo root or set a URL

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
