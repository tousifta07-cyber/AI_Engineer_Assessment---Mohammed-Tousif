import streamlit as st
import requests


st.set_page_config(
    page_title="AI Support Ticket Analyst",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI Support Ticket Analyst")
st.write("Ask questions about the support tickets using natural language.")


question = st.text_input(
    "Ask a question",
    placeholder="Example: How many critical tickets are there?"
)


if st.button("Ask"):

    if question:

        response = requests.post(
            "http://127.0.0.1:8000/query",
            json={"question": question}
        )

        if response.status_code == 200:

            data = response.json()

            st.subheader("Answer")

            answer = data["answer"]

            if isinstance(answer, list):
                st.dataframe(
                    answer,
                    use_container_width=True
                )

            elif isinstance(answer, (int, float)):
                st.success(str(answer))

            else:
                st.success(str(answer))

        else:
            st.error("API request failed.")

    else:
        st.warning("Please enter a question.")


st.divider()

st.subheader("🚨 Anomaly Detection")


if st.button("Show Anomalies"):

    response = requests.get(
        "http://127.0.0.1:8000/anomalies"
    )

    if response.status_code == 200:

        data = response.json()

        st.write(
            f"Found **{data['count']}** anomalous tickets."
        )

        st.dataframe(
            data["anomalies"],
            use_container_width=True
        )

    else:
        st.error("Could not retrieve anomalies.")