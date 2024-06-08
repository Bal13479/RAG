from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from phi.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=Ollama(model="openhermes"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    # debug_mode=True
)
assistant.print_response("Tell me about OpenAI Sora", markdown=True)
