
from langchain_community.llms import Ollama
from langchain import PromptTemplate

import data_loader

class Runner:
    def __init__(self, model_names, option):
        self.model_names = model_names
        self.option = option

    def run(self):
        for model_name in self.model_names:
            model = self.build_model(model_name)

    def build_data(self, file_path, files):
        data_loader.DataLoader(file_path).run(files)

    def build_model(self, model_name):
        if 'llama' in model_name:
            llm = Ollama(model=model_name, stop=["<|eot_id|>"])

        elif 'gpt' in model_name:
            print('2')


    def build_template_llama(self):
        if self.option == 'basic':
            prompt_template = PromptTemplate.from_template(template)
            pdf_text = read_documents('./', ['docs.pdf'])
            target = ''

            question = prompt_template.format(doc_contents=pdf_text[:500], target=target)

            answer = llm(question)

            print(answer)
