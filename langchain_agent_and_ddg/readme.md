# LangChain Custom Agents

![Image generated using Dalle 2](others/1.png)


LangChain Custom Agents are AI-powered decision-makers built with large language models (LLMs) to autonomously choose actions and interact with external tools for accomplishing various tasks.

One of the major problem with LLMs is that they are outdated so if we ask any iformation about the latest events they dont have a clue about it.

## What They Are

- **AI-powered Decision-Makers:** Custom agents are intelligent programs capable of autonomously making decisions and interacting with external tools to accomplish tasks.

- **Built with Language Models (LLMs):** Leveraging large language models, these agents can reason, make decisions, and generate text responses.

- **Adaptable and Versatile:** Custom agents can be created for a wide range of purposes, from simple automations to complex workflows.

## Key Features

- **Custom Tool Integration:** Agents can employ various tools, including external APIs, software services, databases, and other scripts, to execute tasks and gather information.

- **Conversational Capabilities:** They can engage in natural language conversations with users, guiding them through tasks and providing relevant information.

- **Memory and Context:** Agents can maintain a memory of past interactions, enabling them to adapt their responses based on context and create more personalized experiences.

## How They Work

1. **User Input:** A user provides a prompt or query to the custom agent.

2. **LLM Processing:** The agent sends the input to a large language model, which analyzes the text and suggests potential actions or responses.

3. **Tool Selection:** The agent chooses appropriate tools based on the LLM's suggestions and its understanding of the task.

4. **Tool Execution:** The agent interacts with the selected tools to retrieve data, perform actions, or generate content.

5. **Response Generation:** Combining the tool outputs and LLM's insights, the agent creates a comprehensive response tailored to the user's needs.

## Benefits of Using Custom Agents

- **Automation:** Automate repetitive tasks and workflows, saving time and effort.

- **Personalization:** Create highly customized experiences that align with user preferences and goals.

- **Intelligence:** Leverage the power of LLMs to make informed decisions and provide insightful responses.

- **Flexibility:** Adapt agents to evolving needs and scenarios without extensive coding.

- **Integration:** Seamlessly connect with diverse tools and services to expand functionality.



## Example

In this repository, i have made a simple agent which uses DuckDuckGo search, and response by searching and getting the results from the internet. 

## Usage

### Installation

Create a virtualenv and do the following.

```bash
pip install -r requirements.txt
```

#### Set OpenAI API Key
Create a .env file like .env_example and add OpenAI API Key.


#### Run the app
```bash
streamlit run app.py
```

# Demo
Here's the demo video for it!


# About me
I am Israr Ahmed, passionate about AI/DS/ML/DL. I work on tasks related to computer vision, nlp, gen ai, ml ops and also on resful apis like Flask or Fast Api.

* [LinkedIn](https://www.linkedin.com/in/ahmedisrar919/)
* [Medium](https://medium.com/@Ahmedisrar919)
