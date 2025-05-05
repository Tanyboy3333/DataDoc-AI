import os

import gradio as gr
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.cohere import CohereEmbedding  # ✅ USE COHERE instead
from llama_index.llms.groq import Groq
from llama_parse import LlamaParse

from dotenv import load_dotenv
load_dotenv()


# API keys
llama_cloud_key = os.environ.get("LLAMA_CLOUD_API_KEY")
groq_key = os.environ.get("GROQ_API_KEY")
cohere_key = os.environ.get("COHERE_API_KEY")  # ✅ updated variable
if not (llama_cloud_key and groq_key and cohere_key):
    raise ValueError(
        "API Keys not found! Ensure they are passed to the Docker container."
    )

# models name
llm_model_name = "llama3-70b-8192"
embed_model_name = "embed-english-v3.0"  # ✅ Cohere's latest embedding model

# Initialize the parser
parser = LlamaParse(api_key=llama_cloud_key, result_type="markdown")

# Define file extractor with various common extensions
file_extractor = {
    ".pdf": parser,
    ".docx": parser,
    ".doc": parser,
    ".txt": parser,
    ".csv": parser,
    ".xlsx": parser,
    ".pptx": parser,
    ".html": parser,
    ".jpg": parser,
    ".jpeg": parser,
    ".png": parser,
    ".webp": parser,
    ".svg": parser,
}

# ✅ Initialize the embedding model using Cohere
embed_model = CohereEmbedding(api_key=cohere_key, model_name=embed_model_name)

# Initialize the LLM
llm = Groq(model=llm_model_name, api_key=groq_key)


# File processing function
def load_files(file_path: str):
    global vector_index
    if not file_path:
        return "No file path provided. Please upload a file."
   
    valid_extensions = ', '.join(file_extractor.keys())
    if not any(file_path.endswith(ext) for ext in file_extractor):
        return f"The parser can only parse the following file types: {valid_extensions}"

    document = SimpleDirectoryReader(input_files=[file_path], file_extractor=file_extractor).load_data()
    vector_index = VectorStoreIndex.from_documents(document, embed_model=embed_model)
    print(f"Parsing completed for: {file_path}")
    filename = os.path.basename(file_path)
    return f"Ready to provide responses based on: {filename}"


# Respond function
def respond(message, history):
    try:
        # Use the preloaded LLM
        query_engine = vector_index.as_query_engine(streaming=True, llm=llm)
        streaming_response = query_engine.query(message)
        partial_text = ""
        for new_text in streaming_response.response_gen:
            partial_text += new_text
            yield partial_text
    except (AttributeError, NameError):
        print("An error occurred while processing your request.")
        yield "Please upload the file to begin chat."


# Clear function
def clear_state():
    global vector_index
    vector_index = None
    return [None, None, None]


# UI Setup
with gr.Blocks(
    theme=gr.themes.Default(
        primary_hue="green",
        secondary_hue="blue",
        font=[gr.themes.GoogleFont("Poppins")],
    ),
    css="footer {visibility: hidden}",
) as demo:
    gr.Markdown("# DataDoc AI: Analyse files with Q&A 🤖📃")
    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(
                file_count="single", type="filepath", label="Upload Document"
            )
            with gr.Row():
                btn = gr.Button("Submit", variant="primary")
                clear = gr.Button("Clear")
            output = gr.Textbox(label="Status", lines=5, interactive=False)
        with gr.Column(scale=3):
            chatbot = gr.ChatInterface(
                fn=respond,
                chatbot=gr.Chatbot(height=500),
                theme="soft",
                show_progress="full",
                textbox=gr.Textbox(
                    placeholder="Ask questions about the uploaded document!",
                    container=False,
                ),
            )

    btn.click(fn=load_files, inputs=file_input, outputs=output)
    clear.click(fn=clear_state, outputs=[file_input, output])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
