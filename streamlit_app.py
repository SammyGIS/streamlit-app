import streamlit as st
import pandas as pd

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

## Adding Display to our page
df = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-population.csv')
df.shape

# to write header you ca use st.write or st.dataframe or st,table
st.write(df.head())
st.dataframe(df.head())
st.table(df.head()) # table is not dynamic, cannot be sorted

# add metrics to the page (just like indidator or card)
st.metric("AR",df.groupby(['state/region'])['population'].sum()['AR'])

