from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini')

class Review(TypedDict):
    key_features: Annotated[list[str], "Write down all the key_features of the product"]
    summary: Annotated[str, "Explain the summary of the review"]
    sentiment: Annotated[str, "Say either the riview is postive, negitive or neutral"]
    pros: Annotated[list[str], "Pros of the thing"]
    cons: Annotated[list[str], "Cons of the thing"]

structured_model = model.with_structured_output(Review)

review = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
"""

result = structured_model.invoke(review)

print(result['cons'])