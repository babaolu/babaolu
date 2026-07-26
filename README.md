# babaolu

Software Engineer specializing in AI-driven systems, enterprise web applications, and decentralized infrastructure.

I build robust software solutions, focusing on AI-driven systems, enterprise web applications, and decentralized infrastructure. Recently, I've developed **TerAI**, a high-performance C++ rewrite for on-device AI, and **MyG**, a multi-agent AI system designed for Vulkan graphics programming. I also create dynamic web applications like **invitation** for event management and contribute to decentralized physical infrastructure networks such as **Poot**.

## Core focus areas

**AI-Driven Systems & Agent Orchestration**
*   Developing high-performance, on-device AI tools like `TerAI` with native ARM64 compilation for zero-latency execution.
*   Orchestrating local multi-agent AI systems such as `MyG` to automate complex engineering tasks, including code generation, validation, and debugging.
*   Integrating on-device LLM inference capabilities using direct `libllama.so` linkage for efficient, local AI processing.

**Enterprise Web Applications**
*   Building dynamic web applications like `invitation` that offer live content updates, administrative dashboards, and on-demand PDF generation for event management.
*   Developing highly responsive, interactive web applications using modern frameworks such as Svelte 5 for engaging user experiences, as seen in `Dedication`.
*   Crafting enterprise-grade solutions for managing critical workflows, including automated reporting and role-based access control, as exemplified by `graceplace-reporting` in my broader work.

**Decentralized Infrastructure**
*   Architecting and building secure decentralized physical infrastructure networks (DePINs) like `Poot`, which bridge mobile computing resources with cloud customers via demand-gated token economies.
*   Implementing decentralized zero-knowledge storage with erasure coding and AES-256-GCM encryption for data sharding across distributed nodes.
*   Designing orchestrator services for robust distributed node management, ensuring resilience and high-performance operations in DePIN architectures.

## Selected Projects

### [babaolu](https://github.com/babaolu/babaolu)
This repository acts as my dynamic GitHub profile README, which is automatically updated using GitHub Actions. Its primary function is to provide a comprehensive and current overview of my technical specializations, highlighting my latest work in AI-driven systems, enterprise web development, and decentralized infrastructure. The automation ensures that my public profile accurately reflects my ongoing projects and evolving expertise without manual updates.
Stack: Python, GitHub Actions

### [TerAI](https://github.com/babaolu/TerAI)
`TerAI` is a high-performance, native ARM64 rewrite of an AI system, engineered for zero-latency startup and minimal overhead by compiling directly with `clang++` in Termux. This project focuses on efficient on-device AI execution, incorporating direct in-process `libllama.so` linkage for local LLM inference. Technical innovations include advanced tab-completion, exposing tool schemas, and robust daemon management, making it a powerful solution for portable AI tasks.
Stack: C++, CMake, Shell, libcurl, nlohmann/json, readline, libllama.so

### [MyG](https://github.com/babaolu/MyG)
Known as VulkanMind, `MyG` is a local multi-agent AI system specifically designed for modern Vulkan graphics programming and high-performance C++ systems engineering. It orchestrates specialized agents for tasks such as platform detection, knowledge retrieval, Vulkan-Hpp/VMA code generation, validation, and debugging. The system features a deterministic LangGraph state graph and integrates a self-improvement loop for continuous refinement, making it a robust and adaptable tool for complex engineering challenges.
Stack: Python, FastAPI, LangGraph, Qdrant, SQLite, Pydantic, structlog, uv, Vulkan-Hpp/VMA

### [invitation](https://github.com/babaolu/invitation)
This web application generates unique, permanent invitation pages and live PDFs for event guests. Its core technical innovation lies in the instant, dynamic updating of content (like table numbers or QR codes) on a guest's existing link whenever details change, eliminating the need to re-send invitations. The project includes a login-protected admin dashboard for guest and table management, features responsive design, and integrates live PDF generation directly from the current database state using Supabase and PLpgSQL.
Stack: JavaScript, PLpgSQL, HTML, Supabase (PostgreSQL), Vercel, Netlify

### [Poot](https://github.com/babaolu/Poot)
`Poot` is a decentralized physical infrastructure network (DePIN) that connects mobile miners with cloud customers through a demand-gated token economy. Tokens are only minted when real customer instances actively consume miner resources, giving the native token strong economic backing. Technically, it implements decentralized zero-knowledge storage, sharding customer data across multiple miners using erasure coding (Reed-Solomon) with AES-256-GCM encryption, ensuring K-redundancy and privacy. The system is designed to use only residual phone resources, avoiding lag or overheating.
Stack: C++, Python, TypeScript, CMake, JavaScript, Reed-Solomon, AES-256-GCM, Docker, Postgres

### [Dedication](https://github.com/babaolu/Dedication)
`Dedication` is a beautifully structured, highly responsive, and interactive web application built with Svelte 5 and Vite. It showcases a modular, performance-oriented architecture with features like randomized gallery layouts, scroll-aware components, and dynamic content presentation. A notable technical aspect is its robust fallback mechanism: if photo assets are missing, the application gracefully displays handcrafted CSS gradients and emoji icons, ensuring an elegant user experience even before media is fully loaded.
Stack: Svelte, CSS, JavaScript, HTML, Vite, Node.js

## Technical Skills

**Languages:** C++, CMake, CSS, HTML, JavaScript, Makefile, PLpgSQL, Python, Shell, Svelte, TypeScript

**Web Technologies:** Express, FastAPI, Netlify, Node.js, PDFKit, React, Svelte, Supabase SDK, Tailwind CSS, Vercel, Vite

**Databases & Cloud Platforms:** Netlify, PostgreSQL, Qdrant, SQLite, Supabase, Vercel

**AI & Distributed Systems:** AI Orchestration, Decentralized Networks, Demand-Gated Token Economies, Distributed Zero-Knowledge Storage, Large Language Models (LLMs), Multi-Agent Systems, On-device AI

**Tools & Libraries:** CMake, Docker, LangGraph, libcurl, libllama, nlohmann/json, Pydantic, readline, structlog, uv, Vulkan-Hpp/VMA

## Contact

[Email](mailto:obabz.tech@gmail.com) | [LinkedIn](https://www.linkedin.com/in/oluwafemi-babajide-6b3a0b122/)
