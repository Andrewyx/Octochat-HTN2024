## Octochat
Hack the North 2024 Submission

When approaching a large repository, it is often difficult to parse through the whole codebase. The average time expected for a new developer (not intern) to become fully productive is about 7 months. That's why we made Octochat: a personal assistant that answers any question you have about any codebase, big or small, with the potential to onboard developers (including ourselves) faster and dive into what's important.

### What it does
Octochat is a Retrieval-Augmented Generatation (RAG) application which helps developers understand a new code file by allowing them to ask questions about how code snippets or functions work, search for where something has been implemented, how to debug an error, help generate better documentation if needed, and overall, more quickly understand the layers of code.

## Technology
The frontend consists of a wxt chrome extension built using React and Typescript while supported by a Python-Flask backend integrating the Voiceflow API to managing embedding processes, storage, and the underlying LLM. 

### Development .venv Setup
First `cd into server`
Windows Setup: `.venv\Scripts\activate` 
Mac/Linux Setup: `.venv/bin/activate`
