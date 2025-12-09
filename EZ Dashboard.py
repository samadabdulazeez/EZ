import streamlit as st

st.set_page_config(layout="wide")

# --- MAIN CONTENT ---
st.title("EZ Job Portal")

# --- Recent Grant box ---
st.markdown("""
<div style="
    background-color:#1D75D2;
    padding:25px;
    border-radius:10px;
    color:white;
    font-size:22px;
    font-weight:700;
    display:flex;
    justify-content:space-between;
    align-items:center;
">
    <div style="flex:1;">
        Recent Grant:
        Technology Innovation Grant
        <p style="font-size:16px; font-weight:400;">
            This grant is from the federal government for companies that are located in Winnipeg and are in the technology sector.
        </p>
        <div style="display:flex; gap:10px; margin-top:10px;">
            <button style="
                padding:8px 16px;
                border:none;
                border-radius:5px;
                background:white;
                color:#1D75D2;
                font-weight:600;
                cursor:pointer;
            ">Learn More</button>
            <a href="https://forms.gle/Rnym4J3d8ivjfboa6" target="_blank" style="
                padding:8px 16px;
                border:none;
                border-radius:5px;
                background:white;
                color:#1D75D2;
                font-weight:600;
                cursor:pointer;
                text-decoration:none;
                display:inline-block;
            ">Apply Now</a>
        </div>
    </div>
    <div style="display:flex; gap:10px; align-items:center; margin-left:20px;">
        <button style="
            background:rgba(255,255,255,0.2);
            border:2px solid white;
            border-radius:50%;
            width:40px;
            height:40px;
            color:white;
            font-size:20px;
            cursor:pointer;
            display:flex;
            align-items:center;
            justify-content:center;
        ">◀</button>
        <button style="
            background:rgba(255,255,255,0.2);
            border:2px solid white;
            border-radius:50%;
            width:40px;
            height:40px;
            color:white;
            font-size:20px;
            cursor:pointer;
            display:flex;
            align-items:center;
            justify-content:center;
        ">▶</button>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
box1, box2, box3 = st.columns(3)
with box1:
    st.info("""
    **Featured Grant**
    
    _______
    
    • [Technology Innovation Grant](/)
    
    • [Small Business Development Fund](/)
    
    • [Research and Development Grant](/)
    
    • [Startup Accelerator Program](/)
    
    • [Green Energy Initiative Grant](/)
    """)
with box2:
    st.info("""
    **Deadline Approaching**
    
    _______
    
    • [Small Business Development Fund (Deadline: December 15, 2025)](/)
    """)
with box3:
    st.info("""
    **New This Week**
    
    _______
    
    • [Startup Accelerator Program](/)
    
    • [Green Energy Initiative Grant](/)
    """)

st.write("---")

# --- Recent Job box ---
st.markdown("""
<div style="
    background-color:#1D75D2;
    padding:25px;
    border-radius:10px;
    color:white;
    font-size:22px;
    font-weight:700;
    display:flex;
    justify-content:space-between;
    align-items:center;
">
    <div style="flex:1;">
        Student Opportunity:
        Exchange Met – Student Interest & Pathways Form
        <p style="font-size:16px; font-weight:400;">
            This was created in partnership with Exchange Met advisors and supported by the Family Ambassador program. This form helps students identify interests, strengths, and the types of experiences they are open to. Information may be shared with school staff to support planning and potential industry matching.
        </p>
        <div style="display:flex; gap:10px; margin-top:10px;">
            <button style="
                padding:8px 16px;
                border:none;
                border-radius:5px;
                background:white;
                color:#1D75D2;
                font-weight:600;
                cursor:pointer;
            ">Learn More</button>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSdbFDCIF6_iYh1f6nsqFdCJ0f9xmwaxPvh4uSmwS5PgHOBYOw/viewform?usp=sharing&ouid=111148685278668903790" target="_blank" style="
                padding:8px 16px;
                border:none;
                border-radius:5px;
                background:white;
                color:#1D75D2;
                font-weight:600;
                cursor:pointer;
                text-decoration:none;
                display:inline-block;
            ">Apply Now</a>
        </div>
    </div>
    <div style="display:flex; gap:10px; align-items:center; margin-left:20px;">
        <button style="
            background:rgba(255,255,255,0.2);
            border:2px solid white;
            border-radius:50%;
            width:40px;
            height:40px;
            color:white;
            font-size:20px;
            cursor:pointer;
            display:flex;
            align-items:center;
            justify-content:center;
        ">◀</button>
        <button style="
            background:rgba(255,255,255,0.2);
            border:2px solid white;
            border-radius:50%;
            width:40px;
            height:40px;
            color:white;
            font-size:20px;
            cursor:pointer;
            display:flex;
            align-items:center;
            justify-content:center;
        ">▶</button>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
box1, box2, box3 = st.columns(3)
with box1:
    st.info("""
    **Featured Job**
    
    _______
    
    • [Summer Intern - Software Development](/)
    
    • [Part-Time Customer Service Representative](/)
    
    • [Student Research Assistant](/)
    
    • [Retail Associate - Flexible Hours](/)
    
    • [Youth Camp Counselor](/)
    """)
with box2:
    st.info("""
    **Deadline Approaching**
    
    _______
    
    • [Summer Intern - Software Development (Deadline: May 1, 2025)](/)
    
    • [Student Research Assistant (Deadline: April 25, 2025)](/)
    """)
with box3:
    st.info("""
    **New This Week**
    
    _______
    
    • [Part-Time Barista](/)
    
    • [Tutor - High School Students](/)
    
    • [Event Staff - Weekend Work](/)
    """)

st.write("---")

# --- AI JOB MATCHING SECTION ---
left, right = st.columns([2, 1])
with left:
    st.header("AI Job/Grant Matching")
    st.write("**Coming Soon**")

with right:
    st.button("Get Started", use_container_width=True)
