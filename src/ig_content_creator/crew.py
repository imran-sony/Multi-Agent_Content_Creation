# src/ig_content_creator/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Dict, Any
import os
from .image_client import SegmindClient

@CrewBase
class IGContentCreatorCrew:
    """Crew that produces an Instagram post pipeline."""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[]  # You can add web scraping/search tools like SerperDevTool
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True
        )

    @agent
    def reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['reviewer'],
            verbose=True
        )

    @agent
    def image_prompt_generator(self) -> Agent:
        # We will allow this agent to call an image client tool (wrapped as Python function)
        return Agent(
            config=self.agents_config['image_prompt_generator'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def write_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_task'],
        )

    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_task'],
            output_file='output/final_content.json'
        )

    @task
    def prompt_task(self) -> Task:
        return Task(
            config=self.tasks_config['prompt_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
