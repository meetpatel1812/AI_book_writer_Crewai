# AiBookWriter Crew

Welcome to the AiBookWriter Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses CrewAI for task automation and AI-driven workflows.

First, create a virtual environment:

```bash
python -m venv env
```

Activate the Virtual Environment

```bash
cd env/Scripts
activate
```

Install CrewAI and Required Tools

```bash
pip install crewai crewai-tools
```
Run the Project

```bash
python main.py
```


### Customizing

**Add your `GROQ_API_KEY` into the `.env` file**
**Add your `SERPER_API_KEY` into the `.env` file**
**Add your `OPENROUTER_API_KEY` into the `.env` file**

- Modify `src/ai_book_writer/config/agents.yaml` to define your agents
- Modify `src/ai_book_writer/config/tasks.yaml` to define your tasks
- Modify `src/ai_book_writer/crew.py` to add your own logic, tools and specific args
- Modify `src/ai_book_writer/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
python main.py
```

This command initializes the ai_book_writer Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `Book/book.md` file with the output of a book on `Topic` in the root folder.

## Understanding Your Crew

The ai_book_writer Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.


