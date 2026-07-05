# babaolu

Software Engineer crafting AI-driven enterprise solutions, decentralized infrastructure, and high-performance systems.

I focus on developing robust and innovative software solutions, spanning AI-driven enterprise platforms and high-performance systems. My recent projects include `GP-Reporting`, an AI-enhanced portal for enterprise report management, and `MyG` (VulkanMind), a multi-agent AI system for Vulkan development. I also architect decentralized physical infrastructure networks like `Poot` and craft responsive web applications for event management, such as `invitation`.

## Core focus areas

**AI-Driven Systems & Agent Orchestration**
*   Developing local multi-agent AI systems, exemplified by `MyG` (VulkanMind), to automate complex engineering tasks like platform detection, code generation, and debugging for C++ and Vulkan.
*   Integrating AI capabilities into enterprise applications, such as `GP-Reporting`, for automated report parsing, summarization, and task reminders.
*   Building API-driven AI tools, like `InterGen`, using services such as Google Gemini for dynamic content generation.

**Enterprise Web Applications**
*   Designing and implementing role-gated monorepo portals, like `GP-Reporting`, for managing critical business workflows and reporting across distributed units.
*   Building full-stack web applications, such as `invitation`, for dynamic event management with features like live PDF generation and admin dashboards.
*   Developing secure and mobile-responsive solutions with modern frameworks (React, Svelte, Node.js, Supabase), including role-based access control and automated notifications.

**Decentralized Infrastructure & Web3**
*   Architecting and implementing Decentralized Physical Infrastructure Networks (DePINs) like `Poot` that bridge mobile resources with cloud services through demand-gated token economies.
*   Developing secure, distributed storage solutions utilizing erasure coding (Reed-Solomon) with AES-256-GCM encryption and k-redundancy for data integrity and privacy.
*   Building high-performance C++ orchestrator services to manage and optimize resource allocation within decentralized networks.

**Scientific Computing & Simulation**
*   Developing 2D multi-physics finite element simulation frameworks, such as `MScProj`, to model complex biomechanical interactions in wearable high-density electromyography (HD-EMG) devices.
*   Utilizing advanced numerical libraries like FEniCSx, GMSH, and PETSc for high-performance solving of partial differential equations and data visualization in R.
*   Implementing sophisticated physical models, including Nitsche-type contact penalties, to accurately simulate real-world phenomena and extract critical parameters like electrical potentials.

**High-Performance Graphics & Native Development**
*   Crafting native applications with C++ and Vulkan for direct hardware interaction and high-performance functionalities, as seen in `MyG` (VulkanMind), `pbr_V`, and `VulkanTest`.
*   Developing custom ARM64 toolchains and build processes (e.g., `arm-ndk`) to enable on-device compilation and efficient deployment of native mobile applications.
*   Implementing intricate graphics rendering pipelines, including physically based rendering techniques, optimized for high-performance visual computing.

## Selected Projects

**[invitation](https://github.com/babaolu/invitation)**
This web application is designed to streamline event management by generating unique, permanent invitation pages and live PDFs for each guest. Its core value lies in instantly updating invitation content—such as table numbers or QR codes—even if event details change, without requiring links to be re-sent. Technically, it supports pre-seeding 109 guests across 15 tables, offers 8 rotating design variants, features a login-protected admin dashboard for editing guest tables, and dynamically generates PDFs directly from the current database state, ensuring all information is always up-to-date. Recent enhancements include full responsiveness and API support for guest creation and deletion.
Stack: JavaScript, PLpgSQL, HTML, Supabase (PostgreSQL).

**[GP-Reporting](https://github.com/babaolu/GP-Reporting)**
GP-Reporting is an enterprise-grade, role-gated monorepo portal designed for managing monthly reports across various church units. It offers robust features like role-based views, automated reminders, and AI-driven capabilities for report parsing and summarization, alongside consolidated PDF/DOCX exports. Architected with React 19, Node.js, and Supabase, it leverages multiple AI providers (Claude, Gemini, OpenRouter, Nvidia NIM) for intelligent processing. Recent enhancements include support for late report submissions, email/Telegram notifications for unit heads, and an AI summarization retry button, all while ensuring a fully responsive mobile experience and robust security via Supabase Row Level Security.
Stack: TypeScript, React, Node.js, Express, Supabase (PostgreSQL), Tailwind CSS, Resend, Telegram Bot API, PDFKit, Anthropic Claude, Google Gemini, OpenRouter, Nvidia NIM.

**[MyG](https://github.com/babaolu/MyG)**
MyG, also known as VulkanMind, is an advanced local multi-agent AI system engineered to assist with modern Vulkan graphics programming and high-performance C++ systems development. It operates by orchestrating specialized agents through a deterministic LangGraph state graph, handling tasks such as platform detection, knowledge retrieval, Vulkan-Hpp/VMA code generation, validation, and debugging, with automatic routing for self-correction if code generation fails. Key features include a provider-agnostic LLM abstraction and an integrated self-improvement loop, alongside a new interactive shell client, making it a powerful tool for accelerating complex graphics engineering workflows.
Stack: Python, FastAPI, LangGraph, Claude API, Qdrant, SQLite, Pydantic, Vulkan-Hpp, VMA, C++.

**[babaolu](https://github.com/babaolu/babaolu)**
This repository hosts my dynamic GitHub profile README, designed to serve as a living portfolio that automatically updates to reflect my latest projects and technical specializations. Its purpose is to provide a current and accurate overview of my ongoing contributions, ensuring that my profile always showcases my most recent work in areas like AI-enhanced enterprise solutions, multi-agent AI systems, and decentralized infrastructure. The continuous integration process, primarily driven by automated bots, ensures that the content remains fresh and relevant, reflecting updates to project details and contact information.
Stack: Python, GitHub Actions.

**[Poot](https://github.com/babaolu/Poot)**
Poot is an innovative decentralized physical infrastructure network (DePIN) that connects mobile miners with cloud customers through a unique demand-gated token economy. This system ensures that tokens are only minted when active customer instances consume miner resources, thereby providing genuine economic backing and preventing inflation. Technically, it implements decentralized zero-knowledge storage where customer data is sharded across multiple miners using erasure coding (Reed-Solomon) with AES-256-GCM encryption, ensuring privacy and k-redundancy for data integrity. The core resource management is handled by a high-performance C++23 orchestrator service, with recent efforts focused on achieving testnet readiness and optimizing Docker builds.
Stack: C++, Python, TypeScript, CMake, PostgreSQL, Docker, Reed-Solomon, AES-256-GCM, DePIN.

**[Dedication](https://github.com/babaolu/Dedication)**
Dedication is a beautifully structured, highly responsive, and interactive web application, meticulously crafted with Svelte 5 and Vite, designed to celebrate a significant personal event. This project underwent a substantial refactor from a monolithic HTML file to a modular, performance-oriented architecture. Key technical features include scroll-aware UI elements such as a docked countdown with integrated maps buttons, dynamic randomized gallery layouts for images, and an elegant fallback mechanism that uses CSS gradients and emoji icons when photo assets are missing, ensuring a polished user experience even with incomplete media. It also incorporates scroll-based audio autoplay and a rethemed soft baby blue and sage green palette.
Stack: Svelte, CSS, JavaScript, HTML, Vite.

## Technical Skills

**Languages:** C++, Python, TypeScript, JavaScript, HTML, CSS, Svelte, PLpgSQL, R, CMake, Makefile

**AI & Machine Learning:** Multi-Agent AI Systems, Anthropic Claude, Google Gemini, OpenRouter, Nvidia NIM, LangGraph, AI-driven Parsing & Summarization, Knowledge Retrieval, Code Generation, Self-Improvement Loops

**Web Development:** React, Svelte, Vite, Node.js, Express.js, FastAPI, Tailwind CSS, RESTful APIs, HTML/CSS/JavaScript

**Database & Backend:** PostgreSQL, Supabase, SQLite, Row Level Security (RLS), Data Storage

**High-Performance Computing & Graphics:** C++ Systems Engineering, Vulkan, Android NDK, ARM64 Development, Mobile GPU Optimization, Physically Based Rendering, FEniCSx (DOLFINx), GMSH, PETSc, Finite Element Analysis (FEA), Multi-physics Modeling, Biomechanics

**Decentralized Systems:** DePIN (Decentralized Physical Infrastructure Networks), Distributed Systems, Token Economies, Erasure Coding (Reed-Solomon), K-Redundancy, Zero-Knowledge Storage, AES-256-GCM

**DevOps & Tooling:** Docker, GitHub Actions, Vercel, `uv`, CMake, Git, CI/CD Principles

## Contact

Feel free to reach out to me:

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:babaolu98@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/babatunde-adeoti-1614b2b9/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BzaeWA8N4TR2tSvr8Dg7evg%3D%3D)
[![Twitter](https://img.shields.io/badge/
