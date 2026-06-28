# babaolu

Software Engineer specializing in AI-enhanced enterprise solutions, multi-agent AI systems, decentralized infrastructure, and scientific simulations.

I'm a software engineer focused on developing robust and innovative solutions across diverse technical domains. Recently, I've been building **GP-Reporting**, an AI-enhanced portal for enterprise report management, and **MyG**, a sophisticated multi-agent AI system for Vulkan development. My work also extends to **Poot**, a decentralized physical infrastructure network, and creating a multi-physics simulation framework for wearable devices in **MScProj**.

## Core focus areas

**AI-Driven Systems & Agent Orchestration**
*   Developing local multi-agent AI systems, exemplified by `MyG` (VulkanMind), to automate complex engineering tasks like platform detection, code generation, and debugging for C++ and Vulkan.
*   Integrating AI capabilities into enterprise applications, such as `GP-Reporting`, for automated report parsing, summarization, and task reminders.
*   Building API-driven AI tools, like `InterGen`, using services such as Google Gemini for dynamic content generation.

**Enterprise Web Applications**
*   Designing and implementing role-gated monorepo portals, like `GP-Reporting`, for managing critical business workflows and reporting across distributed units.
*   Developing full-stack solutions with modern frameworks (React, Node.js, Supabase) that include robust features such as role-based access control, automated notifications, and consolidated report exports.
*   Ensuring enterprise applications are mobile-responsive and maintain high standards of security, including database Row Level Security and secure session management.

**Decentralized Infrastructure & Web3**
*   Architecting and implementing Decentralized Physical Infrastructure Networks (DePINs) like `Poot` that bridge mobile resources with cloud services through demand-gated token economies.
*   Developing secure, distributed storage solutions utilizing erasure coding (Reed-Solomon) with AES-256-GCM encryption and k-redundancy for data integrity and privacy.
*   Building high-performance C++ orchestrator services to manage and optimize resource allocation within decentralized networks.

**Scientific Computing & Simulation**
*   Developing 2D multi-physics finite element simulation frameworks, such as `MScProj`, to model complex biomechanical interactions in wearable high-density electromyography (HD-EMG) devices.
*   Utilizing advanced numerical libraries like FEniCSx, GMSH, and PETSc for high-performance solving of partial differential equations and data visualization in R.
*   Implementing sophisticated physical models, including Nitsche-type contact penalties, to accurately simulate real-world phenomena and extract critical parameters like electrical potentials.

**High-Performance Graphics & Native Development**
*   Crafting native applications with C++ and Vulkan for direct hardware interaction and high-performance functionalities, as seen in `MobileCAD` and Vulkan-based projects.
*   Developing custom ARM64 toolchains and build processes (e.g., `arm-ndk`) to enable on-device compilation and efficient deployment of native mobile applications.
*   Implementing intricate graphics rendering pipelines, including physically based rendering techniques, optimized for high-performance visual computing.

## Selected Projects

**[GP-Reporting](https://github.com/babaolu/GP-Reporting)**
An enterprise-grade, role-gated monorepo portal designed to manage monthly reports across church units. This application includes role-based views, automated reminders, AI-driven report parsing & summaries, a leaderboard, and consolidated PDF/DOCX report exports. Recent work includes implementing late report submissions, adding department renaming, enhancing mobile layout, and notifying unit heads via email/Telegram for updates, alongside AI summarization retries for improved user experience and workflow. It offers robust security with Supabase Row Level Security and full mobile responsiveness.
Stack: TypeScript, React, Node.js, Express, Supabase (PostgreSQL), Tailwind CSS, Resend, Telegram Bot API, PDFKit, Anthropic Claude, Google Gemini, OpenRouter, Nvidia NIM.

**[MyG](https://github.com/babaolu/MyG)**
MyG, or VulkanMind, is a local multi-agent AI system specifically designed to assist with modern Vulkan graphics programming and high-performance C++ systems engineering. This sophisticated orchestrator uses LangGraph to manage specialized agents for tasks like platform detection, knowledge retrieval, Vulkan-Hpp/VMA code generation, validation, and debugging. Recent developments include an interactive shell client, refactoring for LangGraph 1.x and Pydantic v2, a provider-agnostic LLM abstraction, and the integration of a self-improvement loop to continuously enhance its capabilities.
Stack: Python, FastAPI, LangGraph, Claude API, Qdrant, SQLite, Pydantic, Vulkan-Hpp, VMA, C++.

**[babaolu](https://github.com/babaolu/babaolu)**
This repository hosts my dynamic GitHub profile README, acting as a living portfolio that automatically updates to reflect my latest projects and technical specializations. It leverages GitHub Actions for automated content management, ensuring that my profile stays current and accurately showcases my ongoing contributions in areas such as native mobile development, high-performance graphics, scientific simulations, and decentralized systems. Recent work includes refreshing the AI profile and updating contact information, keeping the content relevant and fresh.
Stack: Python, GitHub Actions.

**[Poot](https://github.com/babaolu/Poot)**
Poot is a decentralized physical infrastructure network (DePIN) that bridges mobile miners with cloud customers through a demand-gated token economy. Its unique model ensures tokens are only minted when real customer instances actively consume miner resources, providing genuine economic backing. Technically, it features decentralized zero-knowledge storage using erasure coding (Reed-Solomon) with AES-256-GCM encryption for privacy, and achieves k-redundancy for data integrity, managed by a C++23 orchestrator service. Recent commits focused on testnet readiness, Docker optimizations, and fixing Reed-Solomon bugs for robust deployment.
Stack: C++, Python, TypeScript, CMake, PostgreSQL, Docker, Reed-Solomon, AES-256-GCM, DePIN.

**[Dedication](https://github.com/babaolu/Dedication)**
Dedication is a beautifully structured, highly responsive, interactive web application, meticulously crafted with Svelte 5 and Vite, designed to celebrate a significant event or individual. Originally a single HTML file, it was refactored into a modular, performance-oriented architecture. Key technical features include scroll-aware UI elements like a docked countdown with maps buttons, dynamic randomized gallery layouts for images, and elegant fallback mechanisms using CSS gradients and emoji icons if photo assets are missing, ensuring a polished user experience even without complete media.
Stack: Svelte, CSS, JavaScript, HTML, Vite.

**[MScProj](https://github.com/babaolu/MScProj)**
This repository contains a 2D multi-physics finite element simulation framework designed to model, analyze, and optimize flexible, wearable high-density electromyography (HD-EMG) electrode array bands wrapped around a human forearm. Implemented using **FEniCSx (DOLFINx)** and **GMSH**, it utilizes high-performance parallel linear algebra solvers via **PETSc** and advanced data visualization in **R**. Recent work includes comprehensive documentation updates, parameter tuning, and detailed modeling of Gaussian dipoles, contact penalties, and voltage extraction at electrodes to accurately simulate complex electromechanical interactions for biomedical devices.
Stack: Python, FEniCSx (DOLFINx), GMSH, PETSc, R.

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
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/Overwor56755051)
