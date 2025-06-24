import streamlit as st
import webbrowser
from PIL import Image
import os
import base64

# === Page Configuration ===
st.set_page_config(
    page_title="SCALE-UP 2025 Dashboard Hub",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === File Paths ===
BACKGROUND_IMAGE = "Background.png"
LOGO_PATH = "Logo.png"

# === Helper for background base64 ===
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# === Background Styling ===
if os.path.exists(BACKGROUND_IMAGE):
    bg_base64 = get_base64(BACKGROUND_IMAGE)
    st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
    </style>
    """, unsafe_allow_html=True)
else:
    st.warning("Background image not found.")

# === Custom CSS ===
st.markdown("""
<style>
    .main-header {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 700;
        color: #0014db;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.3rem;
        color: #0014db;
        font-weight: 600;
        margin-bottom: 2rem;
    }
    .main-container {
        background: rgba(255,255,255,0.95);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(0,20,219,0.15);
        margin: 1rem auto;
    }
    .stButton > button {
        width: 100%;
        height: 70px;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 15px;
        background-color: #0014db;
        color: white;
        border: none;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        background-color: #0014db;
        border: 2px solid #efab00;
    }
    .split-button-container {
        display: flex;
        gap: 4px;
        height: 70px;
    }
    .split-button {
        flex: 1;
        background-color: #0014db;
        color: white;
        border-radius: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        text-decoration: none;
    }
    .split-button:hover {
        transform: translateY(-3px);
        border: 2px solid #efab00;
    }
    .team-header {
        text-align: center;
        font-size: 1rem;
        font-weight: 600;
        color: #0014db;
        margin-bottom: 0.3rem;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        color: #0014db;
        font-size: 0.9rem;
        font-weight: 600;
        background: rgba(255,255,255,0.8);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">SCALE-UP 2025</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Dashboard Hub - Access all team solutions in one place</p>', unsafe_allow_html=True)

# === Groups Data ===
groups = [
    {"name": "313 Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/SW_MUDLOG/WEB_APP/uh3zxEd", "color": "#0014db"},
    {"name": "AWRP Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/TRY_STUCK_MULTIPLEWELL/DASHBOARD/KqCO5Hh?pageId=Mxuct54", "color": "#0014db"},
    {"name": "Cassanova Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/COPY2OFCASSANOVAOPTIMIZATION_CHOKE_SIZEFINAL/DASHBOARD/bdzDbDH?pageId=UIkTFBB", "color": "#0014db"},
    {"name": "HCML One Team", "url": None, "color": "#808080"},   # Disabled
    {"name": "Homonculus Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/HOMONCULUS/WEB_APP/KVzldJt", "color": "#0de1eb"},
    {"name": "Mavericks Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/SPARK/WEB_APP/pBLfP4t", "color": "#0de1eb"},
    {"name": "PetroData Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/PETRODATA_WEBAPP/WEB_APP/WUoy8g8", "color": "#0de1eb"},
    {"name": "PetroSolve Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/PETROFRAC/WEB_APP/Hb6yWXF", "color": "#0de1eb"},
    {"name": "PetroTechnicals Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/PETROTECHNICALS_PROJECT/WEB_APP/9qxhWZU", "color": "#efab00"},
    {"name": "Mr. Wiwir Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/SCALEUPWIWIR/WEB_APP/xURpsRL", "color": "#efab00"},
    {"name": "Young Blood Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/EORSCREENINGFIX/DASHBOARD/3g0FPEQ?pageId=LDhWFY0", "color": "#efab00"},
    {"name": "Young Engineer Team", "url": "https://ai-playground.app.weu-d1.delfi.slb-ds.com/workspaces/SCALE_UP_2025_WEBAPPS/YOUNGENGINEERTEAM/WEB_APP/1IkHKme", "color": "#efab00"}
]

# === Main Grid Layout ===
for row in range(3):
    cols = st.columns(4)
    for col_idx in range(4):
        group_idx = row * 4 + col_idx
        if group_idx < len(groups):
            group = groups[group_idx]
            with cols[col_idx]:

                # Disabled button for HCML
                if group["name"] == "HCML One Team":
                    st.markdown(f'''
                        <div style="
                            width: 100%;
                            height: 100px;
                            background-color: {group['color']};
                            color: white;
                            font-size: 1.3rem;
                            font-weight: 600;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            text-align: center;
                            border-radius: 15px;
                            opacity: 0.4;
                            cursor: not-allowed;
                            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        ">
                            🚫 {group['name']} (Unavailable)
                        </div>
                    ''', unsafe_allow_html=True)
                else:
                    st.markdown(f'''
                        <a href="{group['url']}" target="_blank" style="
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            width: 100%;
                            height: 100px;
                            background-color: {group['color']};
                            color: white;
                            font-size: 1.3rem;
                            font-weight: 600;
                            text-align: center;
                            border-radius: 15px;
                            text-decoration: none;
                            margin: 6px 0;
                            transition: all 0.3s ease;
                            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        " onmouseover="this.style.border='2px solid #efab00'" onmouseout="this.style.border='none'">
                            {group.get('icon', '')} {group['name']}
                        </a>
                    ''', unsafe_allow_html=True)


# === Footer ===
#st.markdown("""
#<div class="footer">
#    <p>🏆 SCALE-UP 2025 Dashboard Hub • Built with Streamlit • Empowering Innovation & Growth</p>
#</div>
#""", unsafe_allow_html=True)
