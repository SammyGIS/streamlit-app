import streamlit as st

# set title
st.title("hello word")

# write on the page
st.write("A streamlit demo")
# instead of st write you can pass your text directt
"This is a test"

#"**bold**"
# "*italic*"
# markdown
st.markdown("streamlit is **very** *cool*")
st.header("This is a header") #header
st.subheader("This sis a subheader") # adding subheader
st.caption("This is caption") #adding caption

# to represent blcok of code

st.code("""
import streamlit as st

# set title
st.title("hello word")

# write on the page
st.write("A streamlit demo")
# instead of st write you can pass your text directt
"This is a test"

#"**bold**"
# "*italic*"
# markdown
st.markdown("streamlit is **very** *cool*")

#header
st.header("This is a header")
st.subheader("This sis a subheader")
        st.caption("This is caption") #adding caption

 """)

"___" # break line


