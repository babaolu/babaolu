# babaolu

Software Engineer specializing in AI-driven systems, enterprise web applications, and decentralized infrastructure.

I develop robust software solutions, particularly focusing on AI-driven systems, enterprise web applications, and decentralized physical infrastructure. My recent work includes `TerAI`, a native C++ rewrite for on-device AI, and `GP-Reporting`, an AI-enhanced portal for enterprise report management. I also architect multi-agent AI systems like `MyG` for complex engineering tasks and build secure decentralized networks such as `Poot`.

## Core focus areas

**AI-Driven Systems & Agent Orchestration**
*   Building zero-latency, native ARM64 AI tools like `TerAI` for efficient on-device execution with minimal overhead.
*   Integrating AI capabilities into enterprise applications, such as `GP-Reporting`, for automated report parsing, summarization, and intelligent task reminders.
*   Orchestrating local multi-agent AI systems, exemplified by `MyG`, to automate complex engineering tasks including code generation, validation, and debugging for C++ and Vulkan.

**Enterprise Web Applications**
*   Developing enterprise-grade, role-gated monorepo portals, like `GP-Reporting`, for managing critical workflows and reporting across distributed organizational units.
*   Crafting dynamic event management web applications, such as `invitation`, with features like live PDF generation, administrative dashboards, and responsive design.
*   Building full-stack solutions with modern frameworks (React, Node.js, Supabase) that include role-based access control and automated notifications.

**Decentralized Infrastructure & Web3**
*   Architecting and implementing Decentralized Physical Infrastructure Networks (DePINs) like `Poot` that bridge mobile resources with cloud services through a demand-gated token economy.
*   Developing secure, distributed storage solutions using erasure coding (Reed-Solomon) with AES-256-GCM encryption for data integrity, privacy, and k-redundancy.
*   Building high-performance C++ orchestrator services to manage and optimize resource allocation within decentralized networks, ensuring robust operation on testnet environments.

**High-Performance Computing & Native Development**
*   Rewriting AI tools natively in C++ for ARM64 platforms, as demonstrated in `TerAI`, to achieve zero-latency startup and a near-zero idle memory footprint.
*   Developing native C++ systems with Vulkan for graphics programming, integrating AI-driven code generation and debugging for complex rendering pipelines in projects like `MyG`.
*   Implementing complex cryptographic and distributed storage logic in high-performance C++ orchestrator services for decentralized physical infrastructure networks like `Poot`.

## Selected Projects

**[TerAI](https://github.com/babaolu/TerAI)**
TerAI is a native ARM64 rewrite of an AI system, designed for execution directly within Termux, offering significant performance advantages over interpreter-based solutions. This project focuses on achieving zero-latency startup and near-zero idle memory footprint by leveraging C++ and `clang++` for direct compilation. Technically, it incorporates robust error handling, daemon stability enhancements, readline integration with tab-completion, and exposes tool schemas, while actively resolving issues such as daemon timeouts, libc++ path iteration compile errors, and prompt corruption.
Stack: C++, CMake, Shell, libcurl, nlohmann/json, readline.

**[GP-Reporting](https://github.com/babaolu/GP-Reporting)**
GP-Reporting is an enterprise-grade, role-gated monorepo portal designed to manage monthly reports across various church units. It offers robust features including role-based views, automated reminders, AI-driven report parsing and summarization, and consolidated PDF/DOCX report exports. Architected with React 19, Node.js, and Supabase, the system integrates multiple AI providers (Anthropic Claude, Google Gemini, OpenRouter, Nvidia NIM) and communication APIs (Resend, Telegram Bot API). Recent enhancements include implementing document previews, supporting late report submissions, adding an AI summarization retry button, and resolving frontend production build compiler issues.
Stack: TypeScript, React, Node.js, Express, Supabase (PostgreSQL, RLS, Storage), Tailwind CSS, Resend SDK, Telegram Bot API, PDFKit, Mammoth, Anthropic Claude, Google Gemini, OpenRouter, Nvidia NIM.

**[babaolu](https://github.com/babaolu/babaolu)**
This repository hosts my dynamic GitHub profile README, designed to serve as a self-updating portfolio. Its purpose is to continuously reflect my latest projects and technical specializations, ensuring an accurate and current overview of my work in areas like AI-enhanced enterprise solutions, multi-agent AI systems, and decentralized infrastructure. The continuous integration process, primarily driven by automated bots, ensures that the content remains fresh and relevant, reflecting updates to project details and contact information in a timely manner.
Stack: Python, GitHub Actions.

**[invitation](https://github.com/babaolu/invitation)**
This web application simplifies event management by generating unique, permanent invitation pages and live PDFs for each guest. Its core value lies in instantly updating invitation content—such as table numbers or QR codes—even if event details change, without requiring links to be re-sent. Technically, it supports pre-seeding 109 guests across 15 tables, offers 8 rotating design variants, features a login-protected admin dashboard for editing guest tables, and dynamically generates PDFs directly from the current database state, ensuring all information is always up-to-date and fully responsive.
Stack: JavaScript, PLpgSQL, HTML, Supabase (PostgreSQL).

**[MyG](https://github.com/babaolu/MyG)**
MyG, also known as VulkanMind, is an advanced local multi-agent AI system engineered to assist with modern Vulkan graphics programming and high-performance C++ systems development. It operates by orchestrating specialized agents through a deterministic LangGraph state graph, handling tasks such as platform detection, knowledge retrieval, Vulkan-Hpp/VMA code generation, validation, and debugging, with automatic routing for self-correction if code generation fails. Key features include a provider-agnostic LLM abstraction, an integrated self-improvement loop, and a new interactive shell client, making it a powerful tool for accelerating complex graphics engineering workflows.
Stack: Python, FastAPI, LangGraph, Claude API, Qdrant, SQLite, Pydantic, structlog, Vulkan-Hpp, VMA, C++, Makefile.

**[Poot](https://github.com/babaolu/Poot)**
Poot is an innovative Decentralized Physical Infrastructure Network (DePIN) that connects mobile miners (lending residual CPU, RAM, storage) with cloud customers through a unique demand-gated token economy. This system ensures tokens are minted only when active customer instances consume miner resources, providing real economic backing and preventing inflation. Technically, it implements decentralized zero-knowledge storage where customer data is sharded via erasure coding (Reed-Solomon) with AES-256-GCM encryption for privacy and k-redundancy. The core orchestrator service is in C++23, with recent work focused on achieving testnet readiness and optimizing Docker builds.
Stack: C++, Python, TypeScript, CMake, JavaScript, PostgreSQL, Docker, Reed-Solomon, AES-256-GCM, DePIN.

## Technical Skills

**Languages:** C++, Python, TypeScript, JavaScript, HTML, CSS, Svelte, PLpgSQL, R, CMake, Shell, Makefile

**AI & Machine Learning:** Multi-Agent AI Systems, Anthropic Claude, Google Gemini, OpenRouter, Nvidia NIM, LangGraph, AI-driven Parsing & Summarization, Knowledge Retrieval, Code Generation, Self-Improvement Loops

**Web Development:** React, Svelte, Vite, Node.js, Express.js, FastAPI, Tailwind CSS, RESTful APIs, HTML/CSS/JavaScript

**Database & Backend:** PostgreSQL, Supabase, SQLite, Qdrant, Row Level Security (RLS), Storage Buckets, Triggers

**High-Performance Computing & Graphics:** C++ Systems Engineering, Vulkan, Android NDK, ARM64 Development, Mobile GPU Optimization, Physically Based Rendering

**Decentralized Systems:** DePIN (Decentralized Physical Infrastructure Networks), Distributed Systems, Token Economies, Erasure Coding (Reed-Solomon), K-Redundancy, Zero-Knowledge Storage, AES-256-GCM

**DevOps & Tooling:** Docker, GitHub Actions, Vercel, `uv`, CMake, Git, CI/CD Principles

## Contact

Feel free to reach out to me:

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:babaolu98@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/babatunde-adeoti-1614b2b9/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BzaeWA8N4TR2tSvr8Dg7evg%3D%3D)
[![Twitter](https://img.shields.io/badge/
