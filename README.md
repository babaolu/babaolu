# babaolu

Software Engineer building high-performance C++ systems, AI-driven applications, decentralized infrastructure, and engaging web experiences.

I am a Software Engineer focused on crafting robust solutions across high-performance computing, AI-driven systems, decentralized infrastructure, and interactive web applications. Recently, I've been developing **Poot**, a decentralized physical infrastructure network, and engineering **MyG**, a multi-agent AI system for Vulkan graphics. My work also includes optimizing on-device AI with **TerAI**'s native ARM64 rewrite, and creating engaging web platforms like **invitation** for dynamic content delivery.

## Core focus areas

**AI-Driven Systems & Agent Orchestration**
*   Developed `MyG`, a multi-agent AI system orchestrating specialized agents for Vulkan graphics code generation, validation, and debugging using LangGraph.
*   Engineered `TerAI`, a native ARM64 C++ rewrite for on-device AI, featuring zero-latency startup and direct `libllama.so` linkage for local LLM inference.
*   Implemented automated GitHub profile updates, leveraging AI for content generation and ensuring the profile reflects current project work and skills.

**High-Performance Graphics & C++ Systems**
*   Implemented core Vulkan graphics rendering concepts in `VulkanTest`, including creating vertex buffers, managing swapchains, setting up graphics pipelines, and recording command buffers for scene rendering.
*   Designed and built the C++ orchestrator for `Poot`, a decentralized physical infrastructure network, enabling efficient resource allocation and management within a distributed environment.
*   Rewrote `TerAI` in C++ for native ARM64 compilation, achieving significant performance gains for on-device AI applications.

**Dynamic Web Applications**
*   Developed `invitation`, a web application that generates unique, live invitation pages and PDFs that update instantly based on database changes, removing the need to resend event details.
*   Created administrative dashboards for `invitation` to manage guest lists and seating arrangements, alongside client-facing features such as QR code generation and live PDF downloads.
*   Focused on building responsive user interfaces and integrating with backend services like Supabase for dynamic content delivery and robust data persistence.

**Decentralized Infrastructure**
*   Architected `Poot`, a Decentralized Physical Infrastructure Network (DePIN) that connects mobile miners with cloud customers through a demand-gated token economy, ensuring token minting is proportional to real resource consumption.
*   Implemented decentralized zero-knowledge storage within `Poot`, sharding customer data using erasure coding (Reed-Solomon) and AES-256-GCM encryption to ensure privacy and K-redundancy.
*   Focused on optimizing resource usage on mobile devices, ensuring the `Poot` miner app utilizes only residual CPU, RAM, and storage to prevent performance impact.

## Selected Projects

### [Poot](https://github.com/babaolu/Poot)
Poot is a decentralized physical infrastructure network (DePIN) engineered to bridge mobile device miners with cloud customers via a unique demand-gated token economy. Its innovative economic model ensures tokens are only minted when actual customer instances actively consume miner resources, thereby providing tangible economic backing for the native token and preventing inflation. Technically, Poot features decentralized zero-knowledge storage, sharding customer data across multiple miners using erasure coding (Reed-Solomon) with AES-256-GCM encryption to ensure K-redundancy and privacy. The system is carefully designed to use only residual phone resources, preventing performance impact.
Stack: C++, Python, TypeScript, CMake, JavaScript, Reed-Solomon, AES-256-GCM, Docker, PostgreSQL

### [VulkanTest](https://github.com/babaolu/VulkanTest)
This project serves as a hands-on exploration and implementation of the Vulkan graphics API, aiming to render graphics to the screen. It systematically builds up a Vulkan rendering pipeline, starting with basic concepts like creating graphics pipelines and frame buffers. Progress includes defining vertex buffers, handling index buffers for drawing, managing swapchain recreation upon window resizing, and optimizing rendering with features like multiple frames in flight. The project demonstrates a foundational understanding of modern low-level graphics programming by successfully rendering a rotating square.
Stack: C++, CMake, GLSL

### [invitation](https://github.com/babaolu/invitation)
invitation is a web application that revolutionizes event guest management by generating unique, permanent invitation pages and live PDF seating cards for each guest. The key technical strength lies in its ability to instantly update content—such as table numbers, QR codes, or event details—on an existing guest link whenever database changes occur, eliminating the need to resend invitations. It includes a login-protected admin dashboard for guest and table editing, full responsiveness, and live PDF generation directly from a Supabase (PostgreSQL) database using PLpgSQL.
Stack: JavaScript, PLpgSQL, HTML, Supabase (PostgreSQL), Vercel

### [babaolu](https://github.com/babaolu/babaolu)
This repository hosts my dynamic GitHub profile README, which is automatically generated and updated through a sophisticated GitHub Actions workflow. Its primary function is to provide a current and accurate overview of my technical expertise, highlighting my latest projects and evolving skill set without manual intervention. The automation process includes AI-powered content generation, ensuring the profile remains up-to-date and reflects my ongoing work in AI-driven systems, high-performance computing, and decentralized infrastructure.
Stack: Python, GitHub Actions, AI

### [MyG](https://github.com/babaolu/MyG)
MyG, also known as VulkanMind, is a local multi-agent AI system designed to streamline modern Vulkan graphics programming and high-performance C++ systems engineering. It orchestrates specialized agents for tasks such as platform detection, knowledge retrieval, Vulkan-Hpp/VMA code generation, validation, and debugging. The project implements a deterministic LangGraph state graph for structured execution, integrates a self-improvement loop, and provides an interactive shell client. Recent developments have focused on enabling end-to-end functionality, enhancing C++ code generation for meaningful Vulkan code, and improving knowledge query responses.
Stack: Python, FastAPI, LangGraph, Qdrant, SQLite, Pydantic, structlog, uv, Vulkan-Hpp/VMA, Makefile

### [TerAI](https://github.com/babaolu/TerAI)
TerAI is a native ARM64 rewrite of an AI system, specifically engineered for zero-latency startup and minimal interpreter overhead through direct compilation with `clang++` within Termux. This project enables efficient on-device AI execution by integrating direct in-process `libllama.so` linkage for local Large Language Model (LLM) inference. Technical highlights include sophisticated readline tab-completion, dynamic exposure of tool schemas, and a robust daemon designed to manage and prevent timeout issues. The focus on native ARM64 makes it a powerful, portable solution for local AI tasks.
Stack: C++, CMake, Shell, libcurl, nlohmann/json, readline, libllama.so, ARM64

## Technical Skills

**Languages:** C++, CMake, GLSL, HTML, JavaScript, Makefile, PLpgSQL, Python, Shell, Svelte, TypeScript

**Web Technologies:** FastAPI, GitHub Actions, Netlify, Svelte, Supabase, Vercel

**Databases & Cloud Platforms:** Docker, GitHub Actions, Netlify, PostgreSQL, Qdrant, SQLite, Supabase, Vercel

**AI & Distributed Systems:** AI Orchestration, Decentralized Networks, Demand-Gated Token Economies, Distributed Zero-Knowledge Storage, Large Language Models (LLMs), Multi-Agent Systems, On-device AI

**Tools & Libraries:** AES-256-GCM, ARM64, CMake, Docker, FastAPI, LangGraph, libcurl, libllama.so, nlohmann/json, Pydantic, readline, Reed-Solomon, structlog, uv, Vulkan-Hpp/VMA

## Contact

[Email](mailto:obabz.tech@gmail.com) | [LinkedIn](https://www.linkedin.com/in/oluwafemi-babajide-6b3a0b122/)
