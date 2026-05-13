# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter


# def load_and_split_pdf(file_path):

#     loader = PyPDFLoader(file_path)

#     documents = loader.load()

#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200
#     )

#     chunks = text_splitter.split_documents(documents)

#     return chunks 

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter


# def load_and_split_pdf(file_path):

#     loader = PyPDFLoader(file_path)

#     documents = loader.load()

#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=700,
#         chunk_overlap=100,
#         separators=[
#             "\n\n",
#             "\n",
#             ". ",
#             " ",
#             ""
#         ]
#     )

#     chunks = text_splitter.split_documents(
#         documents
#     )

#     return chunks 

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_split_pdf(file_path):

    # Load PDF
    loader = PyPDFLoader(file_path)

    documents = loader.load()

    # Optimized splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=100,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    # Create chunks
    chunks = text_splitter.split_documents(
        documents
    )

    return chunks