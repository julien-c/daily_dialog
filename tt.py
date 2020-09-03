import streamlit as st
import nlp

st.sidebar.markdown(
    """<center>
<a href="https://github.com/huggingface/nlp">
    <img src="https://raw.githubusercontent.com/huggingface/nlp/master/docs/source/imgs/nlp_logo_name.png" width="200">
</a>
</center>""",
    unsafe_allow_html=True,
)
st.sidebar.subheader("DailyDialog dataset")

@st.cache
def get_dataset():
    return nlp.load_dataset("daily_dialog", split="train")

d = get_dataset()

keys = list(d[0].keys())

keys

step = 50
offset = st.sidebar.number_input(
    "Offset (Size: %d)"%len(d), min_value=0, max_value=int(len(d)) - step, value=0, step=step
)


for item in range(offset, offset + step):
    st.text("        ")
    st.text("                  ----  #" + str(item))
    st.text("        ")
    # Use st to write out.
    for k in keys:
        v = d[item][k]
        st.subheader(k)
        if isinstance(v, str):
            out = v
            st.text(textwrap.fill(out, width=120))
        elif isinstance(v, bool) or isinstance(v, int) or isinstance(v, float):
            st.text(v)
        else:
            st.write(v)
