import streamlit as st
from st_social_media_links import SocialMediaIcons


def social_media():
    # This function will help you to render socila media icons with link on the app
    social_media_links = [
    "https://github.com/LyzrCore/lyzr",
    "https://www.youtube.com/@LyzrAI",
    "https://www.instagram.com/lyzr.ai/",
    "https://www.linkedin.com/company/lyzr-platform/posts/?feedView=all",
                        ]   

    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render(sidebar=True, justify_content="space-evenly") # will render in the sidebar


def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 450px;
           max-width: 450px;
       }
    </style>
    """, unsafe_allow_html=True)

def page_config(layout = "centered"):
    st.set_page_config(
        page_title="AI Script Doctor",
        layout=layout,  # or "wide" 
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )

def template_end():
    with st.sidebar.expander("ℹ️ - About this App"):
        st.sidebar.markdown("This app uses Lyzr's Automata to finding plot holes, pacing issues and give some sugggested imporvements to make script more better")
        st.sidebar.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.sidebar.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.sidebar.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.sidebar.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)