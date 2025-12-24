from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20,separators=["\n\n", "\n", " "])
text = ["""In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the actual content is available.
The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book."""]

docs = text_splitter.create_documents(text)
print("type of docs:",type(docs))
print("number of docs:",len(docs))

docs = docs[0]
print("type of first doc:",type(docs))
print("content of first doc:",docs.page_content)
