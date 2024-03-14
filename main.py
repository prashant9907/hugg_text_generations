# import requests

# API_URL = "https://api-inference.huggingface.co/models/Prashant-karwasra/GPT2_text_generation_model_arbaz"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()

# output = query({
# 	"inputs": "Can you please let us know more details about your ",
# })


# print(output)


import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/Prashant-karwasra/GPT2_text_generation_model_arbaz"
HEADERS = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()


def main():
    st.title('Text Generation with Hugging Face API')

    # Input text field
    input_text = st.text_area('Enter your text here:', '')

    if st.button('Generate Text'):
        if input_text:
            output = query({"inputs": input_text})
            st.write('Generated Text:')
            st.write(output)
        else:
            st.write('Please enter some text.')


if __name__ == '__main__':
    main()



