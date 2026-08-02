# babaolu

Software Engineer specializing in AI-driven systems, enterprise web applications, and decentralized infrastructure.

I focus on building robust software solutions, particularly in AI-driven systems, high-performance computing, and dynamic web applications. Recently, I've developed **TerAI**, a C++ rewrite for on-device AI with native ARM64 compilation, and **MyG**, a multi-agent AI system specifically for Vulkan graphics programming. I also create interactive web applications like **invitation** for event management and **Dedication** for rich user experiences, alongside contributing to decentralized infrastructure projects such as **Poot**.

## Core focus areas

**AI-Driven Systems & Agent Orchestration**
*   Developing high-performance, on-device AI tools like `TerAI` with native ARM64 compilation for zero-latency execution.
*   Orchestrating local multi-agent AI systems such as `MyG` to automate complex engineering tasks, including code generation, validation, and debugging.
*   Integrating on-device LLM inference capabilities using direct `libllama.so` linkage for efficient, local AI processing.

**Enterprise Web Applications**
*   Building dynamic web applications like `invitation` that offer live content updates, administrative dashboards, and on-demand PDF generation for event management.
*   Developing highly responsive, interactive web applications using modern frameworks such as Svelte 5 for engaging user experiences, as seen in `Dedication`.
*   Designing and implementing interactive frontends with modern JavaScript frameworks like Svelte and responsive CSS, ensuring dynamic content and rich user experiences.

**Decentralized Infrastructure**
*   Architecting and building secure decentralized physical infrastructure networks (DePINs) like `Poot`, which bridge mobile computing resources with cloud customers via demand-gated token economies.
*   Implementing decentralized zero-knowledge storage with erasure coding and AES-256-GCM encryption for data sharding across distributed nodes.
*   Designing orchestrator services for robust distributed node management, ensuring resilience and high-performance operations in DePIN architectures.

## Selected Projects

### [babaolu](https://github.com/babaolu/babaolu)
This repository serves as my dynamic GitHub profile README, automatically updated via GitHub Actions. Its purpose is to present a current overview of my technical expertise, focusing on AI-driven systems, enterprise web development, and decentralized infrastructure. The automation ensures my public profile accurately reflects my ongoing projects and evolving skill set without requiring manual updates, leveraging AI for content generation based on my latest work.
Stack: Python, GitHub Actions, AI

### [TerAI](https://github.com/babaolu/TerAI)
TerAI is a high-performance C++ rewrite of an AI system, engineered for zero-latency startup and minimal interpreter overhead through native ARM64 compilation within Termux. This project focuses on efficient on-device AI execution, integrating direct in-process `libllama.so` linkage for local LLM inference. Key technical features include advanced readline tab-completion, dynamic exposure of tool schemas, and robust daemon management, making it a powerful and portable solution for AI tasks without cloud dependencies.
Stack: C++, CMake, Shell, libcurl, nlohmann/json, readline, libllama.so, ARM64

### [MyG](https://github.com/babaolu/MyG)
MyG, also known as VulkanMind, is a local multi-agent AI system specifically crafted for modern Vulkan graphics programming and high-performance C++ systems engineering. It orchestrates specialized agents for critical tasks like platform detection, knowledge retrieval, Vulkan-Hpp/VMA code generation, validation, and debugging. The system utilizes a deterministic LangGraph state graph and integrates a self-improvement loop for continuous refinement, providing a robust and adaptable framework for complex graphics engineering challenges.
Stack: Python, FastAPI, LangGraph, Qdrant, SQLite, Pydantic, structlog, uv, Vulkan-Hpp/VMA, Makefile

### [invitation](https://github.com/babaolu/invitation)
This web application dynamically generates unique, permanent invitation pages and live PDF seating cards for event guests. A key technical feature is its ability to instantly update content—such as table numbers, QR codes, or event details—on a guest's existing link whenever changes occur, eliminating the need for re-sending invitations. It includes a login-protected admin dashboard for guest and table management, ensures full responsiveness, and integrates live PDF generation directly from the current database state using Supabase (PostgreSQL) and PLpgSQL.
Stack: JavaScript, PLpgSQL, HTML, Supabase (PostgreSQL), Vercel, Netlify

### [Poot](https://github.com/babaolu/Poot)
Poot is a decentralized physical infrastructure network (DePIN) designed to connect mobile device miners with cloud customers through a unique demand-gated token economy. Tokens are exclusively minted when real customer instances actively consume miner resources, ensuring the native token has genuine economic backing. Technically, it implements decentralized zero-knowledge storage, sharding customer data across multiple miners using erasure coding (Reed-Solomon) with AES-256-GCM encryption for K-redundancy and privacy. The system is engineered to utilize only residual phone resources, preventing performance degradation.
Stack: C++, Python, TypeScript, CMake, JavaScript, Reed-Solomon, AES-256-GCM, Docker, PostgreSQL

### [Dedication](https://github.com/babaolu/Dedication)
Dedication is a beautifully structured, highly responsive, and interactive web application built with Svelte 5 and Vite. It features a modular, performance-oriented architecture with capabilities such as randomized gallery layouts, scroll-aware components for enhanced user engagement, and dynamic content presentation. A notable technical aspect is its robust fallback mechanism: if specific photo assets are missing, the application gracefully displays handcrafted CSS gradients and emoji icons, maintaining an elegant user experience even before all media is fully loaded.
Stack: Svelte, CSS, JavaScript, HTML, Vite, Node.js

## Technical Skills

**Languages:** C++, CMake, CSS, HTML, JavaScript, Makefile, PLpgSQL, Python, Shell, Svelte, TypeScript

**Web Technologies:** FastAPI, GitHub Actions, Netlify, Node.js, Svelte, Supabase, Vercel, Vite

**Databases & Cloud Platforms:** Docker, Netlify, PostgreSQL, Qdrant, SQLite, Supabase, Vercel

**AI & Distributed Systems:** AI Orchestration, Decentralized Networks, Demand-Gated Token Economies, Distributed Zero-Knowledge Storage, Large Language Models (LLMs), Multi-Agent Systems, On-device AI

**Tools & Libraries:** AES-256-GCM, CMake, Docker, LangGraph, libcurl, libllama, nlohmann/json, Pydantic, readline, Reed-Solomon, structlog, uv, Vulkan-Hpp/VMA

## Contact

[Email](mailto:obabz.tech@gmail.com) | [LinkedIn](https://www.linkedin.com/in/oluwafemi-babajide-6b3a0b122/)
