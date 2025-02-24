from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from dotenv import load_dotenv
import os
load_dotenv()
# import litellm
# litellm._turn_on_debug()


# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class AiBookWriter():
	"""AiBookWriter crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you want to use a different LLM model, you can change it here
	open_router_llm = LLM(
    model="openrouter/google/gemini-2.0-flash-lite-preview-02-05:free",
    base_url="https://openrouter.ai/api/v1",
	api_key=os.getenv('OPENROUTER_API_KEY'),
	temperature=0.5,
	
	)

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def research_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['research_agent'],
			
			llm=self.open_router_llm,
			tools=[SerperDevTool()],
			allow_delegation=False,
			verbose=True,
		)

	@agent
	def extraction_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['extraction_agent'],
			tools=[ScrapeWebsiteTool()],
			llm=self.open_router_llm,
			allow_delegation=False,
			verbose=True,
		)
	
	@agent
	def writing_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['writing_agent'],
			# tools=[FileWriterTool()],
			tools=[],
			llm=self.open_router_llm,
			allow_delegation=False,
			verbose=True,
		)
	
	@agent
	def editing_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['editing_agent'],
			tools=[],
			llm=self.open_router_llm,
			allow_delegation=False,
			verbose=True,
		)

	@agent
	def publishing_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['publishing_agent'],
			tools=[FileWriterTool()],
			llm=self.open_router_llm,
			allow_delegation=False,
			verbose=True,
		)
	

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def research_book(self) -> Task:
		return Task(
			config=self.tasks_config['research_book'],
			verbose=True
		)
	
	@task
	def extract_information(self) -> Task:
		return Task(
			config=self.tasks_config['extract_information'],
			verbose=True
		)
	
	@task
	def write_book(self) -> Task:
		return Task(
			config=self.tasks_config['write_book'],
			verbose=True
		)
	
	@task
	def edit_book(self) -> Task:
		return Task(
			config=self.tasks_config['edit_book'],
			verbose=True
		)
	
	@task
	def publish_book(self) -> Task:
		return Task(
			config=self.tasks_config['publish_book'],
			verbose=True,
			output_file='book.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AiBookWriter crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
