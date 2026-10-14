import streamlit as st
import base64
st.set_page_config(
    page_title='Gabriela Naluyinda | Portfolio',
    layout='wide',
    initial_sidebar_state='collapsed'
)
def get_b64_file(bin_file):
    with open(bin_file, 'rb') as f:
        data=f.read()
    return base64.b64encode(data).decode()

try:
    bg_image_base64=get_b64_file('b2.jpeg')
    prof_pic=get_b64_file('profilepic.jpeg')
except FileNotFoundError:
    st.error('Error, pic files must be in same folder as python file.')

st.markdown(f"""
    <style>
    [data-testid='stAppViewContainer']{{
        background-color:transparent !important;
    }}
    .stApp{{
        background-image:url('data:image/jpeg;base64,{bg_image_base64}');
        background-size:cover;
        background-position:center-top;
        background-attachment:fixed;
        background-repeat:no-repeat;
        background-color:transparent !important;
    }}
    [data-testid='stMainBlockContainer']{{
    background:rgba(20,35,60,0.90) !important;
    padding:40px !important;
    border-radius:16px !important;
    border:1px solid rgba(100,255,218,0.3) !important;
    box-shadow:0 20px 40px rgba(0, 0, 0, 0.6) !important;
    backdrop-filter:blur(8px) !important;
    margin-bottom:30px !important;
    }}
    h1,h2,h3,h4 {{
        color:#ccd6f6 !important;
        font-family:'SF Mono','Fira Code','Roboto Mono',monospace;
    }}
    p,li{{
        color:#8892b0;
        font-size:1.1rem;
    }}
    a{{
        color:#64ffda!important;
        text-decoration:none;
    }}
    .profile-container{{
        width:200px;
        height:200px;
        margin-bottom:20px;
        position:relative;
        margin-left:auto;
        margin-right:auto;
        margin-top:20px;
    }}
    .profile-img{{
        width:100%;
        height:100%;
        object-fit:cover;
        border-radius:50%;
        border:2px solid #64ffda;
        filter:grayscale(80%) contrast(110%);
        transition:all 0.3s ease-in-out;
        }}
    
    .profile-container:hover .profile-img{{
        filter:grayscale(0%) contrast(100%);
        box-shadow: 0 0 15px rgba(100,255,218,0.5);
        transform: scale(1.03);
    }}
    </style>
""", unsafe_allow_html=True)
if prof_pic:
  st.markdown(
      f"""
        <div class='profile-container' style='margin: 0 auto 20px auto;'>
            <img src='data:image/jpg;base64,{prof_pic}' class='profile-img'>
        </div>
    """,
      unsafe_allow_html=True,
  )
else:
  st.info("Missing 'profilepic.jpeg'")

# Center your name and subheader right under the picture if you like, or go straight to columns
st.markdown("<h1 style='text-align: center;'>Gabriela Naluyinda</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #8892b0;'>Bachelor of Science in Computer Science Student at Uganda Christian University</h3>", unsafe_allow_html=True)
st.markdown('---')
st.markdown("""
-[Github Profile](https://github.com/Jlo21-peace)
-[Email me](mailto:gabrielanaluyinda@gmail.com)
""")
left_col, right_col =st.columns([1,1.3], gap='large')
with left_col:
     st.header('About me')
     st.write('Aspiring Dev with a passion for creating tech solutions and learning new technologies. Skilled in Python, C and web development frameworks. Eager to contribute to impactful projects and collaborate with diverse teams.'
    )
with right_col:
    st.header('')
    st.write(
        'I am a dedicated and enthusiastic software developer with a strong foundation in computer science principles and a keen interest in building user-friendly applications.Working on various projects, both independently and collaboratively, has honed my problem-solving skills and ability to adapt to new challenges. My goal is to leverage technical expertise and creativity to contribute to meaningful projects that positively impact and influence the world.')
st.markdown('---')
st.header('Current focus and skills')
col1,col2,col3=st.columns(3)
with col1:
    st.markdown('**Programming Languages:** ')
    st.write('. C (Low-level logic & Debugging)\n.Python (Data tools and Streamlit)')
with col2:
    st.markdown('**Core Domains:**')
    st.write('Website development, Robotics,Essential Hardware management')
with col3:
    st.markdown('**Skills:**')
    st.write('Data Enumeration, Scratch game development, TinkerCAD basic circuit proficiency')
st.markdown('---')
st.header('Projects and Learning milestones.')
col1,col2=st.columns(2)
with col1:
    with st.container(border=True):
        st.subheader('Dual control bluetooth rover')
        st.caption('C . Arduino. Hardware Integration')
        st.write('Practical robotics project with hybrid control system combining smartphone input and physical remote modules.')
        st.markdown('**Status: In Planning and development**')
with col2:
    with st. container(border=True):
        st.subheader('Junk App Website')
        st.caption('CSS . html . Javascript')
        st.write('Website for proposed waste-management app intended to digitalise booking of garbage collecting and recycling along with consumer behavioural adjustment goals towards clean living through awarding user points. ')
        st.markdown('**Status: In Development.**')
