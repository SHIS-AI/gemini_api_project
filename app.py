import streamlit as st
from utils.api_calling_app import note_generator,generate_audio,generator_quiz
from PIL import Image


#title
st.title("Note Summary and Voice generator and Quiz generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizes")
st.markdown("Creator by **SHIS**")
st.markdown("Contact me at : 01643376184")
st.markdown("Gmail : mdshisahammed@gmail.com")
st.divider()

# sidebar
with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload the photos of your note",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if images:
        pil_images = [Image.open(image) for image in images]
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            col = st.columns(len(images))

            st.subheader("Uploaded images")

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    #selectbox
    selected_option = st.selectbox(
        "Enter the difficulty of your quize",
        ("Easy", "Medium", "Hard"),
        index=None
    )


    pressed = st.button("Click the button to initiate AI",type="primary")


if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must selct difficulty")


    if images and selected_option:
        #note
        with st.container(border=True):
            st.subheader("Your note")
            with st.spinner("Ai is writing notes for you..."):
                generator_notes = note_generator(pil_images)
                st.markdown(generator_notes)
            

        #Audio transcipt
        with st.container(border=True):
            st.subheader("Audio treanscription of the note")


            generator_notes = generator_notes.replace("#","")
            generator_notes = generator_notes.replace("*","")
            generator_notes = generator_notes.replace("'","")
            generator_notes = generator_notes.replace(":","")
            generator_notes = generator_notes.replace(";","")


            with st.spinner("Ai is generating audio for you..."):
                audio_generate = generate_audio(generator_notes)
                st.audio(audio_generate)


        # quiz
        with st.container(border=True):
            st.subheader(f"Quiz {selected_option} Difficulty")
            
            quiz_generate = generator_quiz(pil_images,selected_option)
            st.markdown(quiz_generate)
