from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
You are an expert AI Research Assistant.

Research Paper:
{paper_input}

Explanation Style:
{style_input}

Explanation Length:
{length_input}

Instructions:
- Explain the paper according to the selected explanation style.
- Use simple language if the style is Beginner-Friendly.
- Use technical terminology if the style is Technical.
- Include code examples if the style is Code-Oriented.
- Include mathematical intuition and equations if the style is Mathematical.
- Explain the main problem the paper solves.
- Describe the proposed solution.
- Explain the model architecture.
- Discuss the key innovations.
- Mention the datasets used.
- Explain the evaluation metrics.
- Summarize the experimental results.
- Mention the strengths and limitations.
- End with a short conclusion and real-world applications.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save("template.json")