# babaolu

Software Engineer specializing in AI-driven systems, enterprise web applications, and decentralized infrastructure.

I focus on building robust software solutions, particularly within AI-driven systems and enterprise web applications. My recent work includes developing `TerAI`, a native C++ rewrite for on-device AI, and enhancing `graceplace-reporting`, an AI-powered portal for enterprise report management. I also architect multi-agent AI systems, exemplified by `MyG`, to automate complex engineering tasks, and build shared components like `graceplace-platform-kit` to streamline development across related projects.

## Core focus areas

**AI-Driven Systems & Agent Orchestration**
*   Developing high-performance, on-device AI tools like `TerAI` with native ARM64 compilation for zero-latency execution and minimal overhead.
*   Orchestrating local multi-agent AI systems such as `MyG` (VulkanMind) to automate complex engineering tasks, including code generation, validation, and debugging for C++ and Vulkan.
*   Integrating AI capabilities into enterprise applications, seen in `graceplace-reporting` for automated report parsing, summarization, and intelligent reminders.

**Enterprise Web Applications**
*   Crafting enterprise-grade, role-gated monorepo portals, like `graceplace-reporting`, to manage critical workflows and reporting across distributed organizational units.
*   Developing shared npm packages, as in `graceplace-platform-kit`, to standardize authentication utilities, design system tokens, and API contract types across a suite of platform applications.
*   Building dynamic web applications like `invitation` that feature live content updates, administrative dashboards, and responsive PDF generation for event management.

**Decentralized Infrastructure**
*   Architecting and building secure decentralized networks, exemplified by `Poot`, to bridge mobile computing resources with cloud customers through innovative token economies.
*   Designing orchestrator services for distributed node management, focusing on high-performance and resilient system operations.

## Selected Projects

### [babaolu](https://github.com/babaolu/babaolu)
This repository serves as my dynamic GitHub profile README, designed to be automatically updated via GitHub Actions. Its purpose is to provide a current and comprehensive overview of my technical expertise, showcasing my latest contributions across AI-driven systems, enterprise web development, and decentralized infrastructure projects. The automation ensures that my public profile remains a fresh reflection of my ongoing work and specializations.
Stack: Python

### [graceplace-reporting](https://github.com/babaolu/graceplace-reporting)
An enterprise-grade, role-gated monorepo portal meticulously designed to streamline monthly report management across distributed organizational units. This application features robust role-based views, automated reminders, and advanced AI for report parsing, summarization, and consolidated PDF/DOCX exports. Recent development includes migrating to a multi-permission RBAC system and implementing cross-subdomain SSO for enhanced security and a seamless user experience.
Stack: TypeScript, React, Node.js, Express, Supabase (PostgreSQL with RLS), Tailwind CSS, PDFKit, Anthropic Claude, Google Gemini, OpenRouter, Nvidia NIM

### [graceplace-platform-kit](https://github.com/babaolu/graceplace-platform-kit)
This repository hosts a collection of shared npm packages central to the GracePlace platform, designed to ensure consistency and reusability across multiple client applications. It includes `@graceplace/platform-kit` for shared authentication utilities, domain configurations, and a Supabase cookie adapter client, alongside CSS design system tokens. Additionally, `@graceplace/api-types` provides pure TypeScript backend contract types for public and CMS endpoints, streamlining API development and integration.
Stack: TypeScript, CSS

### [TerAI](https://github.com/babaolu/TerAI)
A native ARM64 rewrite of the TerAI system, specifically engineered for zero-latency startup and minimal interpreter overhead by compiling directly with `clang++` in Termux. This project prioritizes efficient on-device AI execution, incorporating a direct in-process `libllama.so` linkage for local LLM inference. Further enhancements include advanced tab-completion, exposing tool schemas, and robust daemon management to prevent timeouts and manage git operations safely.
Stack: C++, CMake, Shell, libcurl, nlohmann/json, readline, libllama.so

### [MyG](https://github.com/babaolu/MyG)
Known as VulkanMind, this local multi-agent AI system is meticulously tailored for modern Vulkan graphics programming and high-performance C++ systems engineering. It intelligently orchestrates specialized agents for tasks such as platform detection, knowledge retrieval, Vulkan-Hpp/VMA code generation, validation, and debugging. The system integrates a self-improvement loop for continuous refinement and adaptation to complex engineering challenges, ensuring robust and evolving performance.
Stack: Python, FastAPI, LangGraph, Qdrant, SQLite, Pydantic, structlog, uv, Vulkan-Hpp/VMA

### [invitation](https://github.com/babaolu/invitation)
A robust web application designed for dynamic event management, capable of generating unique, permanent invitation pages and live PDFs for each guest. Its innovative design ensures that if guest or table details change, the content on their personalized link and PDF updates instantly, eliminating the need for re-sending. It includes an administrative dashboard for guest and table management, along with responsive seating directory features for efficient event coordination, including options for guest creation and deletion.
Stack: JavaScript, HTML, PLpgSQL, Supabase (PostgreSQL), Vercel, Netlify

## Technical Skills

**Languages:** C++, Python, TypeScript, JavaScript, PLpgSQL, HTML, CSS, Shell, CMake, Makefile, Svelte

**Web Technologies:** React, Node.js, Express, FastAPI, Vite, Tailwind CSS, React Router, Supabase SDK, Resend SDK, PDFKit, Mammoth, Telegram Bot API

**Databases & Cloud Platforms:** Supabase, PostgreSQL, SQLite, Qdrant, Vercel, Netlify

**AI & Distributed Systems:** Multi-Agent Systems, Large Language Models (LLMs), On-device AI, AI Orchestration, Decentralized Networks

**Tools & Libraries:** Docker, LangGraph, Pydantic, libllama, Vulkan-Hpp/VMA, uv, structlog, nlohmann/json, libcurl, readline

## Contact

[Email](mailto:obabz.tech@gmail.com) | [LinkedIn](https://www.linkedin.com/in/oluwafemi-babajide-6b3a0b122/)
