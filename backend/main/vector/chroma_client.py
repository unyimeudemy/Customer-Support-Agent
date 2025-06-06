import os
import chromadb
from main.vector.onnx_embedder import ONNXEmbeddingFunction
from main.lib.intent_map import INTENT_MAP
from main.lib import kb_collection_store

def setup_chroma_client():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CHROMA_STORE_PATH = os.path.join(BASE_DIR, "chroma_store")

    # Initialize embedder
    embedder = ONNXEmbeddingFunction()

    # Make sure store directory exists (but don't delete)
    os.makedirs(CHROMA_STORE_PATH, exist_ok=True)

    # Start Chroma client
    client = chromadb.PersistentClient(path=CHROMA_STORE_PATH)

    # Get or create collection safely
    kb_collection_store.knowledge_base_collection = client.get_or_create_collection(
        name="my_collection", embedding_function=embedder
    )
    kb_collection_store.intent_collection = client.get_or_create_collection(
        name="intent_collection", embedding_function=embedder
    )


    flat_phrases = []
    ids = []
    metadatas = []


    try:

        for intent, phrases in INTENT_MAP.items():
            for i, phrase in enumerate(phrases):
                flat_phrases.append(phrase)
                ids.append(f"{intent}_{i}")
                metadatas.append({"intent": intent})


        kb_collection_store.intent_collection.add(
            documents=flat_phrases, ids=ids, metadatas=metadatas
        )

        kb_docs = [
            {
                "id": "piraxx_overview",
                "text": "Piraxx Ltd. is a dynamic e-commerce and logistics company headquartered in Lagos, Nigeria. It was founded in 2017 by Maya Obasi and Daniel Ekong. Piraxx provides electronics, fashion, home appliances, and lifestyle products to customers across West Africa. The company is known for its fast last-mile delivery and commitment to customer service."
            },
            {
                "id": "piraxx_mission",
                "text": "Piraxx aims to simplify shopping in underserved regions by offering a trustworthy, fast, and customer-centric platform. It is committed to digital inclusion, sustainability, and creating meaningful jobs across the region. With over 500 employees and thousands of active sellers, Piraxx continues to redefine online retail in Africa."
            },
            {
                "id": "piraxx_services",
                "text": "Piraxx offers an online marketplace for electronics, clothing, groceries, appliances, and more. It provides fast nationwide delivery across Nigeria and Ghana, with same-day delivery in Lagos and Abuja for orders placed before 11 AM. Payment options include card, bank transfer, mobile money, and cash on delivery (in select locations)."
            },
            {
                "id": "piraxx_services_business_support",
                "text": "Piraxx supports bulk orders and corporate procurement through its Business Portal. Customers have access to 24/7 support via live chat, email, and toll-free phone lines."
            },
            {
                "id": "piraxx_return_policy",
                "text": "Piraxx operates a 14-day return policy on eligible items. Items must be unused and in original packaging. Refunds are processed within 5–7 business days of return approval. Non-returnable items include perishables, custom-made goods, and unsealed software, unless damaged on delivery. Complaints must be made within 48 hours of delivery."
            },
            {
                "id": "piraxx_support",
                "text": "Piraxx customer support is available 24/7. Contact options include email (support@piraxx.com), toll-free phone (0800-PIRAXX), and live chat on both the website and mobile app."
            },
            {
                "id": "piraxx_founders",
                "text": "Piraxx was founded by Maya Obasi and Daniel Ekong. Maya was formerly a Strategy Lead at Google Africa and holds an MBA from London Business School. Daniel is a software engineer with experience at Andela and Flutterwave, and he specializes in systems architecture and logistics infrastructure."
            },
            {
                "id": "piraxx_funding",
                "text": "In 2021, Piraxx raised $12 million in Series A funding. The round was led by FutureAfrica Capital, with participation from GreenTech Ventures and fintech angel investors. The funding was used to expand logistics and build new fulfillment centers across West Africa."
            },
            {
                "id": "piraxx_offices",
                "text": "Piraxx has office and fulfillment centers in several locations: Lagos HQ at 35 Admiralty Way, Lekki Phase 1; Abuja office at Plot 22, Aminu Kano Crescent, Wuse II; and Accra office at 18 Jungle Road, East Legon, Ghana."
            }
        ]

                # Add to Chroma collection
                
        kb_collection_store.knowledge_base_collection.add(
            documents=[doc["text"] for doc in kb_docs],
            ids=[doc["id"] for doc in kb_docs],
        )

    except Exception as e:
            print({"error": str(e)})

# ks