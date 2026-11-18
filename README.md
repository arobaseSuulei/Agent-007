# Agent-007

![alt text](https://github.com/arobaseSuulei/button-bouncing/blob/main/img/agent-007.png?raw=true)

## Overview

Agent-007 is a Python-based multi-agent system designed to support collaborative software development.

The system uses Groq's API through the OpenAI Python client to power multiple specialized AI agents.

## Architecture

The project uses a shared `Agent` class and a central `Orchestrator` to manage multiple specialized agents.

## Agents

| Agent | Role | Responsibility |
|---|---|---|
| 001 | Chief | Reads project memory and understands the codebase |
| 002 | Executor | Executes assigned development tasks |
| 003 | Executor | Executes assigned development tasks |
| 004 | Executor | Executes assigned development tasks |
| 005 | Reviewer | Reviews the executors' work |
| 006 | Tester | Tests the code before submission |
| 007 | Submitter | Handles the final submission |

## Core Components

- **Agent:** Represents an individual AI agent.
- **Orchestrator:** Creates and manages agents.
- **Memory:** Stores shared project context.
- **Groq API:** Provides LLM capabilities through the OpenAI Python client.

## Goal

Build a collaborative AI development workflow where specialized agents can execute tasks, review code, test implementations, and coordinate through a central orchestrator.

## Tech Stack

- Python
- Groq API
- OpenAI Python SDK
- python-dotenv