from distutils.command.upload import upload
from email.mime import image
from matplotlib.image import imread
from model import load_image,get_prediction
import streamlit as st
st.sidebar.header('Piranha Pool')
page = st.sidebar.selectbox("Page Navigation",['Hand Numbers','One Piece'])
st.sidebar.markdown("""---""")
st.sidebar.write("Created by [PiranhaGuy](https://github.com/thepiranhaguy)")
submit = None
if page=='Hand Numbers':
    st.title('Hand Numbers Interpreter')
    st.write('Model Trained to Recognize Number of fingers your hand is showing. Is Basic. Might go big.')
    st.markdown('---')   
    st.markdown('Upload a Image')
    upload_columns = st.columns([2,1])
    file_upload = upload_columns[0].expander(label='Upload Image')
    uploaded_file = file_upload.file_uploader("choose image file",type=['jpg','png','jpeg'])

    if uploaded_file:
        image_box = upload_columns[1].image(uploaded_file,use_column_width=True)
        submit = upload_columns[0].button('Guess How Many?')

    if submit:
        with st.spinner(text="Doing the *thing*..."):
            #here apply model
            x_instance = load_image(uploaded_file)
            pred = get_prediction(x_instance)

            outputs = st.columns([3,1])
            outputs[0].markdown(">I say its ")
            outputs[1].success(pred)
            

elif page=='P':
    st.markdown('#The One Piece is real')
    st.image('https://preview.redd.it/pyu6zmnb07p61.png?width=644&format=png&auto=webp&s=ac1b61e83501f4f71b26cfa9d9c314d21bbf13d7')

st.markdown("---")
