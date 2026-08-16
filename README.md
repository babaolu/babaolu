# babaolu

Software Engineer developing AI-driven systems, high-performance C++ applications, decentralized networks, and interactive web experiences.

I build robust software solutions that blend AI innovation with high-performance computing and dynamic web experiences. My recent work includes developing **MyG**, a multi-agent AI system for Vulkan graphics programming, and **TerAI**, a C++ rewrite for efficient on-device AI with native ARM64 compilation. I also architect decentralized infrastructure projects like **Poot**, and craft interactive web applications such as **invitation** and **Dedication** for engaging user experiences.

## Core focus areas

**AI-Driven Systems & Agent Orchestration**
*   Developing high-performance, on-device AI tools like `TerAI` with native ARM64 compilation for zero-latency execution and direct `libllama.so` linkage for local LLM inference.
*   Orchestrating local multi-agent AI systems such as `MyG` to automate complex engineering tasks, including Vulkan code generation, validation, and debugging.

**High-Performance Graphics & C++ Systems**
*   Engineering high-performance C++ systems, including native ARM64 applications and orchestrators for distributed networks like `Poot`.
*   Building multi-agent AI solutions for modern Vulkan graphics programming, integrating Vulkan-Hpp/VMA code generation, validation, and debugging within `MyG`.

**Dynamic Web Applications**
*   Building dynamic web applications that offer features like live content updates, administrative dashboards, and on-demand PDF generation, as demonstrated in `invitation`.
*   Developing highly responsive and interactive web experiences using modern frameworks like Svelte 5 with modular, performance-oriented architectures, seen in `Dedication`.

**Decentralized Infrastructure**
*   Architecting and implementing decentralized physical infrastructure networks (DePINs) that connect mobile resources with cloud services via demand-gated token economies in `Poot`.
*   Developing secure, distributed storage solutions using erasure coding (Reed-Solomon) and AES-256-GCM encryption for zero-knowledge data sharding and K-redundancy.

## Selected Projects

### [babaolu](https://github.com/babaolu/babaolu)
This repository hosts my dynamic GitHub profile README, which is automatically updated through a GitHub Actions workflow. Its primary function is to provide a current and accurate overview of my technical expertise, highlighting my work in AI-driven systems, high-performance computing, and decentralized infrastructure. This automated process, which includes AI-powered content generation, ensures my profile remains up-to-date with my latest projects and evolving skill set without manual intervention.
Stack: Python, GitHub Actions, AI

### [MyG](https://github.com/babaolu/MyG)
**MyG** (also known as VulkanMind) is a local multi-agent AI system designed to streamline modern Vulkan graphics programming and high-performance C++ systems engineering. It orchestrates specialized agents for tasks like platform detection, knowledge retrieval, Vulkan-Hpp/VMA code generation, validation, and debugging. The project implements a deterministic LangGraph state graph, ensuring structured execution, and integrates a self-improvement loop. Recent commits show focus on enabling end-to-end functionality, enhancing C++ code generation, and adding an interactive shell client for easier interaction.
Stack: Python, FastAPI, LangGraph, Qdrant, SQLite, Pydantic, structlog, uv, Vulkan-Hpp/VMA, Makefile

### [TerAI](https://github.com/babaolu/TerAI)
**TerAI** is a native ARM64 rewrite of an AI system, specifically engineered for zero-latency startup and minimal interpreter overhead through direct compilation with `clang++` within Termux. This project enables efficient on-device AI execution by integrating direct in-process `libllama.so` linkage for local Large Language Model (LLM) inference. Technical highlights include sophisticated readline tab-completion, dynamic exposure of tool schemas, and a robust daemon designed to manage and prevent timeout issues, establishing it as a powerful, portable solution for local AI tasks.
Stack: C++, CMake, Shell, libcurl, nlohmann/json, readline, libllama.so, ARM64

### [invitation](https://github.com/babaolu/invitation)
**invitation** is a web application designed to streamline event guest management by generating unique, permanent invitation pages and live PDF seating cards for each guest. Its core innovation lies in instantly updating content—such as table numbers, QR codes, or event details—on an existing guest link whenever database changes occur, thus eliminating the need to resend invitations. The application features a login-protected admin dashboard for guest and table editing, offers full responsiveness, and directly generates PDFs from the live Supabase (PostgreSQL) database using PLpgSQL.
Stack: JavaScript, PLpgSQL, HTML, Supabase (PostgreSQL), Vercel, Netlify

### [Poot](https://github.com/babaolu/Poot)
**Poot** is a decentralized physical infrastructure network (DePIN) engineered to bridge mobile device miners with cloud customers via a unique demand-gated token economy. Its innovative economic model ensures tokens are only minted when actual customer instances actively consume miner resources, thereby providing tangible economic backing for the native token and preventing inflation. Technically, Poot features decentralized zero-knowledge storage, sharding customer data across multiple miners using erasure coding (Reed-Solomon) with AES-256-GCM encryption to ensure K-redundancy and privacy. The system is carefully designed to use only residual phone resources, preventing performance impact.
Stack: C++, Python, TypeScript, CMake, JavaScript, Reed-Solomon, AES-256-GCM, Docker, PostgreSQL

### [Dedication](https://github.com/babaolu/Dedication)
**Dedication** is a beautifully structured, highly responsive, and interactive web application crafted with Svelte 5 and Vite. It boasts a modular, performance-oriented architecture, featuring randomized gallery layouts, scroll-aware components for dynamic user engagement, and adaptable content presentation. A key technical highlight is its robust fallback mechanism: if specific photo assets are unavailable, the application gracefully displays handcrafted CSS gradients and emoji icons, ensuring the presentation remains elegant and visually cohesive even before all media is fully loaded.
Stack: Svelte, CSS, JavaScript, HTML, Vite, Node.js

## Technical Skills

**Languages:** C++, CMake, CSS, HTML, JavaScript, Makefile, PLpgSQL, Python, Shell, Svelte, TypeScript

**Web Technologies:** FastAPI, GitHub Actions, Netlify, Node.js, Svelte, Supabase, Vercel, Vite

**Databases & Cloud Platforms:** Docker, Netlify, PostgreSQL, Qdrant, SQLite, Supabase, Vercel

**AI & Distributed Systems:** AI Orchestration, Decentralized Networks, Demand-Gated Token Economies, Distributed Zero-Knowledge Storage, Large Language Models (LLMs), Multi-Agent Systems, On-device AI

**Tools & Libraries:** AES-256-GCM, CMake, Docker, LangGraph, libcurl, libllama, nlohmann/json, Pydantic, readline, Reed-Solomon, structlog, uv, Vulkan-Hpp/VMA

## Contact

[Email](mailto:obabz.tech@gmail.com) | [LinkedIn](https://www.linkedin.com/in/oluwafemi-babajide-6b3a0b122/)
