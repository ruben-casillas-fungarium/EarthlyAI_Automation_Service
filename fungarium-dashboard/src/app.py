import streamlit as st
from components.login import login_page
from auth.authentication import is_authenticated, logout
from components.sidebar import render_sidebar
from components.chat import render_chat
# from components.form import render_form

def main():
    if not is_authenticated():
        login_page()
    else:
        # Reconfigure page for wide layout after login
        st.set_page_config(
            page_title="Fungarium Dashboard",
            page_icon="🍄",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Custom CSS for main dashboard
        st.markdown("""
            <style>
            .block-container {
                max-width: 100% !important;
                padding: 2rem !important;
            }
            [data-testid="column"] {
                background-color: white;
                padding: 1.25rem;
                border-radius: 10px;
                border: 1px solid rgba(40, 49, 51, 0.1);
                box-shadow: 0 2px 4px rgba(40, 49, 51, 0.05);
                margin: 0.5rem;
                width: 100% !important;
            }
            </style>
        """, unsafe_allow_html=True)
        
        st.write(f"Welcome {st.session_state['user']['username']}!")
        
        st.title("Fungarium Dashboard")
        
        # Render sidebar
        render_sidebar()

        # Create single column for chat
        container = st.container()
        with container:
            render_chat()

if __name__ == "__main__":
    main()