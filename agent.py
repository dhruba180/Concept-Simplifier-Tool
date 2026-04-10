from strands import Agent
from strands.models.ollama import OllamaModel

# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.1"
)

# Define system prompt for simplification
system_prompt = """
You are a helpful assistant that simplifies complex concepts.
Explain everything in very simple terms, like teaching a beginner.
Use examples and avoid jargon.
"""

# Create agent with system prompt
agent = Agent(
    model=ollama_model,
    system_prompt=system_prompt
)

# Take user input
user_input = input("Enter a complex topic: ")

# Get response
response = agent(user_input)

# Print response
print("\nSimplified Explanation:\n")
print(response)
