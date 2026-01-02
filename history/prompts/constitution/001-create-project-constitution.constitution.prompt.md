---
id: 001
title: Create Project Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: claude-code
command: /sp.constitution
labels: [constitution, specification, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
tests:
  - none
---

## Prompt

```text
Project Constitution: Multi-Phase Todo Application
1. Purpose & Vision

The purpose of this project is to design, build, and evolve a Todo application from a simple in-memory console program into a production-grade, AI-powered, cloud-native system.

The vision is to:

Demonstrate clean software engineering fundamentals first

Progressively introduce modern full-stack, AI, and cloud-native architectures

Maintain clarity, simplicity, and correctness at every phase

Treat each phase as a complete, reviewable milestone, not a prototype

2. Core Principles (Non-Negotiables)
2.1 Simplicity First

Prefer simple, readable solutions over clever or complex ones

Each feature must be understandable by a junior developer

2.2 Progressive Complexity

No advanced tooling before fundamentals are correct

Each phase builds strictly on the previous one

2.3 Single Responsibility

Each class, function, and module must have one clear purpose

2.4 Explicit Over Implicit

No hidden magic

All logic, state changes, and flows must be visible and traceable

2.5 Testable by Design

Code should be structured so it can be tested, even if tests are added later

2.6 Agentic Development Discipline

Development follows the workflow:

Write specification

Generate plan

Break into tasks

Implement via Claude Code

No manual coding during agent execution

3. Phase I Constitution – In-Memory Python Console App
3.1 Objective

Build a pure console-based Todo application that stores all data in memory and demonstrates core CRUD operations and state management.

3.2 Technology Constraints

Language: Python

Storage: In-memory only (no files, no database)

Interface: Command-line / terminal

Tools: Claude Code, Spec-Kit Plus

3.3 Functional Requirements

The application must support:

Add Task

Title (required)

Description (optional)

Auto-generated unique ID

Default status: Incomplete

List Tasks

Display all tasks

Show:

Task ID

Title

Description

Status (Complete / Incomplete)

Update Task

Update title and/or description

Task selected strictly by ID

Delete Task

Remove task by ID

Confirm task existence before deletion

Mark Task Status

Toggle between complete and incomplete

Explicit user action required

3.4 Structural Rules

Use Object-Oriented Programming (OOP)

Required entities:

Task (data + behavior)

TodoManager or equivalent (task orchestration)

No global state

Clear separation between:

Business logic

User interaction (input/output)

3.5 Out of Scope (Phase I)

File storage

Databases

Web interfaces

Authentication

AI features

4. Phase II Constitution – Full-Stack Web Application
4.1 Objective

Transform the console application into a full-stack web-based Todo system with persistent storage.

4.2 Technology Stack

Frontend: Next.js

Backend: FastAPI

ORM / Models: SQLModel

Database: Neon (PostgreSQL)

4.3 Principles

RESTful API design

Clear frontend–backend separation

Persistent data integrity

Schema-first development

5. Phase III Constitution – AI-Powered Todo Chatbot
5.1 Objective

Introduce an AI assistant that allows users to interact with their todos using natural language.

5.2 Technology Stack

OpenAI ChatKit

OpenAI Agents SDK

Official MCP SDK

5.3 AI Boundaries

AI assists, not replaces core logic

All AI actions must map to explicit backend operations

No uncontrolled autonomy

6. Phase IV Constitution – Local Kubernetes Deployment
6.1 Objective

Run the entire system locally in a production-like containerized environment.

6.2 Technology Stack

Docker

Minikube

Helm

kubectl-ai

kagent

6.3 Principles

Infrastructure as Code

Reproducible local environments

Clear service boundaries

7. Phase V Constitution – Advanced Cloud Deployment
7.1 Objective

Deploy a scalable, event-driven, cloud-native Todo platform.

7.2 Technology Stack

Kafka (event streaming)

Dapr (service invocation & state)

DigitalOcean DOKS (managed Kubernetes)

7.3 Principles

Scalability

Fault tolerance

Observability

Cloud-native best practices

8. Definition of Done (All Phases)

A phase is considered complete only when:

All
```

## Response snapshot

Created comprehensive project constitution for the Multi-Phase Todo Application, including all core principles and phase-specific requirements. Updated template files to align with the new constitution.

## Outcome

- ✅ Impact: Created complete project constitution with all phases defined
- 🧪 Tests: No tests required for constitution creation
- 📁 Files: Updated constitution.md and template files to align with constitution
- 🔁 Next prompts: Proceed with feature specification for Phase I
- 🧠 Reflection: Constitution provides clear guidance for all project phases and ensures consistency across implementations

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin Phase I specification