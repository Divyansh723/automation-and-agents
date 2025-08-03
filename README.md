# 🤖 automation-and-agents

> A work-in-progress collection of small automation tools and intelligent agents built for various micro-tasks.

---

## 📦 What is This Repo?

`automation-and-agents` is a modular, evolving lab of lightweight automation tools and AI-powered agents — each one built to handle a specific micro-task or workflow shortcut.

Whether it's simplifying repetitive actions, generating content, extracting insights, or running smart utility operations, this repo brings together multiple small but powerful projects under one roof — all using Python, Flask, and free/open AI tools.

This is a space where automation meets creativity. Each sub-folder in the repo represents a standalone tool or intelligent flow — easy to plug in, remix, or extend.

---

## ⚙️ Core Philosophy

- ✅ **Modular** — each tool lives in its own directory, built to work independently
- 🧠 **Agentic-first** — built around the concept of autonomous micro-agents that handle tasks for you
- 🧰 **Automation-driven** — repetitive tasks get handled with logic, speed, and no manual work
- 🧪 **WIP-friendly** — imperfect, experimental, but functional (or fun)
- 💸 **Zero-budget mindset** — uses only free APIs, open-source tools, and local models whenever possible

---

## 🧩 Architecture

```
automation-and-agents/
│
├── agent_name_1/
│   ├── main.py
│   ├── utils/
│   ├── templates/
│   └── README.md
│
├── agent_name_2/
│   ├── main.py
│   ├── ...
│
├── shared/
│   └── utils.py
│
├── .env.example
├── requirements.txt
└── README.md  ← (you are here)
```

> Each folder = one self-contained automation tool or agent flow.

---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/Divyansh723/automation-and-agents.git
   cd automation-and-agents
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your environment variables**
   ```bash
   cp .env.example .env
   # Then edit .env with your keys (e.g., OpenAI, Hugging Face, Notion, etc.)
   ```

4. **Navigate into any tool folder**
   ```bash
   cd tool_folder_name/
   python main.py
   ```

---

## 🌱 Why This Repo Exists

Because sometimes you don’t need a full product — you just need a quick agent to:

- Summarize something
- Transcribe audio
- Analyze data
- Generate an image
- Auto-fill a form
- Or do *that one annoying thing* you always repeat

This repo is where those agents are born.

---

## 🛠️ Tech Stack (varies by tool)

- `Python 3.12`
- `Flask` (lightweight API/UI layer)
- `LangChain`, `LangGraph` (for orchestration and agent logic)
- `Hugging Face`, `Gemini`, `Whisper`, `Stable Diffusion`
- `dotenv`, `requests`, `notion-client`, `diffusers`, and more...

---

## 🧠 Built For

- Indie hackers who want quick tools
- Creatives who need AI-powered shortcuts
- Builders exploring agents without huge stacks
- Anyone automating workflows with *no budget and full ambition*

---

## 📜 License

MIT — free to use, remix, and build on top of. No gatekeeping here.

---

## 🧑‍💻 Maintained by

**Divyansh**  
_Creative Generalist | Agent Builder | Indie Vibe Dev_

> Always building, always dreaming. Follow the lab's journey 👇  
> [GitHub](https://github.com/Divyansh723) • [Twitter](https://x.com/tempest_4754) • [LinkedIn](https://www.linkedin.com/in/divyansh-agarwal-1b0641228/)