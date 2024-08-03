import streamlit as st

# Home page
def home():
    """ 
    Function that rendeers the main home page
    """

    st.title('Welcome to our first Stramlit APP!')

    st.write("""
            # Introduction:
            ### Stramlit is an open-source platform that allows us to create apps in seamless form.
            """)
    
if __name__ == '__main__':
    home()