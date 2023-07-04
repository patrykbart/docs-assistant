import time
import streamlit as st

from docs_assistant import DocsAssistant

if __name__ == "__main__":
    st.set_page_config(
        page_title="Docs Assistant",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Docs Assistant 📚")
    st.markdown(
        """
        AI assistant, allowing you to ask questions about the project based on documentation
        """
    )

    query = st.text_input("Ask a question", value="What is PyTorch?")

    if st.button("Ask"):
        try:
            assert query != "", "Please enter a query"
            assert "docs_assistant" in st.session_state, "Please upload documentation first"

            st.markdown("### Question")
            st.write(query)
            st.markdown("### Answer")
            st.write(st.session_state.docs_assistant.answer_question(query))
        except AssertionError as e:
            st.error(e)

    with st.sidebar:
        # st.markdown()
        model_name = st.selectbox("Select model", options=["hkunlp/instructor-xl"])

        if st.button("Upload documentation"):
            time_start = time.time()

            if "docs_assistant" not in st.session_state:
                st.session_state.docs_assistant = DocsAssistant()

            with st.spinner("Uploading and processing documentation..."):
                st.write(st.session_state.docs_assistant.embed_pdfs())
                st.success(f"Documentation uploaded and processed in {time.time() - time_start:.2f} seconds")