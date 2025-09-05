import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	PDFSearchTool,
	DOCXSearchTool,
	CSVSearchTool
)



@CrewBase
class CorporateDocumentIntelligenceSystemCrew:
    """CorporateDocumentIntelligenceSystem crew"""

    
    @agent
    def document_indexing_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["document_indexing_specialist"],
            tools=[],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def multi_format_document_retrieval_expert(self) -> Agent:
        
        embedding_config_pdfsearchtool = dict(
            llm=dict(
                provider="openai",
                config=dict(
                    model="gpt-4o-mini",
                ),
            ),
            embedder=dict(
                provider="openai",
                config=dict(
                    model="text-embedding-3-small",
                ),
            ),
        )
        
        embedding_config_docxsearchtool = dict(
            llm=dict(
                provider="openai",
                config=dict(
                    model="gpt-4o-mini",
                ),
            ),
            embedder=dict(
                provider="openai",
                config=dict(
                    model="text-embedding-3-small",
                ),
            ),
        )
        
        embedding_config_csvsearchtool = dict(
            llm=dict(
                provider="openai",
                config=dict(
                    model="gpt-4o-mini",
                ),
            ),
            embedder=dict(
                provider="openai",
                config=dict(
                    model="text-embedding-3-small",
                ),
            ),
        )
        
        return Agent(
            config=self.agents_config["multi_format_document_retrieval_expert"],
            tools=[PDFSearchTool(config=embedding_config_pdfsearchtool), DOCXSearchTool(config=embedding_config_docxsearchtool), CSVSearchTool(config=embedding_config_csvsearchtool)],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def rag_response_generation_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["rag_response_generation_analyst"],
            tools=[],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def inventariar_corpus_documental(self) -> Task:
        return Task(
            config=self.tasks_config["inventariar_corpus_documental"],
        )
    
    @task
    def execute_multi_format_semantic_search(self) -> Task:
        return Task(
            config=self.tasks_config["execute_multi_format_semantic_search"],
        )
    
    @task
    def generate_rag_based_business_response(self) -> Task:
        return Task(
            config=self.tasks_config["generate_rag_based_business_response"],
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the CorporateDocumentIntelligenceSystem crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
