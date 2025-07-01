import streamlit as st

st.title("Government Scheme Info App")

st.sidebar.title("Input Options")
opt = st.sidebar.radio("Input method?", ["Type URLs", "Upload File"])

urls = []

# user types URL
if opt == "Type URLs":
    t = st.sidebar.text_area("Paste URLs (comma separated)")
    if t:
        urls = [x.strip() for x in t.split(",") if x.strip()]

# user uploads a file
if opt == "Upload File":
    f = st.sidebar.file_uploader("Upload .txt file with link")
    if f:
        data = f.read().decode("utf-8")
        urls = [x.strip() for x in data.splitlines() if x.strip()]

# Run Button
if st.sidebar.button("Run"):
    if len(urls) == 0:
        st.warning("No URL provided")
    else:
        st.info("Checking links and processing data... (mock)")
        st.success("Done! mock processed")

# Question box
st.subheader("Ask Question")

q = st.text_input("Your question:")

# Mock reply
if q:
    st.write("*Answer:* This is a mock reply based on your input question")
    st.caption(" Source: mock.gov.in")
