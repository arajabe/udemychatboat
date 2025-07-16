from configparser import ConfigParser

class UIConfigFile:

    def __init__(self, config_file_path='src/langgraphagenticai/ui/uiconfigfile.ini'):
        self.config = ConfigParser()
        self.config.read(config_file_path)

    def get_page_title(self):
        return self.config.get('DEFAULT', 'PAGE_TITLE', fallback='LangGraph Agentic AI')

    def get_llm_options(self):
        return self.config.get('DEFAULT', 'LLM_OPTIONS', fallback='Groq').split(',')

    def get_use_case_options(self):
        return self.config.get('DEFAULT', 'USE_CASE_OPTIONS', fallback='Basic Chatbot, Chatbot with tool, AI News, Blog Generator').split(',')

    def get_groq_model(self):
        return self.config.get('DEFAULT', 'GROQ_MODEL', fallback='llama3-70b-8192, llama3-8b-8192').split(',')