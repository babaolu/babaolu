# babaolu

Software Engineer building AI-enhanced enterprise solutions, multi-agent AI systems, decentralized infrastructure, and high-performance simulations.

I focus on developing robust software across various domains, from AI-driven solutions to high-performance graphics and scientific simulations. Recently, I've been building **GP-Reporting**, an enterprise portal with AI-powered report analysis, and **MyG**, a multi-agent AI system for Vulkan development. My work also extends to **Poot**, a decentralized physical infrastructure network, and creating a multi-physics simulation framework for wearable devices in **MScProj**.

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
*   Architecting and implementing Decentralized Physical Infrastructure Networks (DePINs) like `Poot` that bridge physical resources with cloud services through demand-gated token economies.
*   Developing secure, distributed storage solutions utilizing erasure coding (Reed-Solomon) with AES-256-GCM encryption and k-redundancy for data integrity and privacy.
*   Building high-performance C++ orchestrator services to manage and optimize resource allocation within decentralized networks.

**Scientific Computing & Simulation**
*   Developing 2D multi-physics finite element simulation frameworks, such as `MScProj`, to model complex biomechanical interactions in wearable high-density electromyography (HD-EMG) devices.
*   Utilizing advanced numerical libraries like FEniCSx, GMSH, and PETSc for high-performance solving of partial differential equations and data visualization in R.
*   Implementing sophisticated physical models, including Nitsche-type contact penalties, to accurately simulate real-world phenomena and extract critical parameters like electrical potentials.

**High-Performance Graphics & Native Development**
*   Crafting native Android applications, like `MobileCAD`, with C++20 and Vulkan for direct hardware interaction and high-performance CAD functionalities.
*   Developing custom ARM64 toolchains and build processes (e.g., `arm-ndk`) to enable on-device compilation and efficient deployment of native mobile applications.
*   Implementing intricate graphics rendering pipelines, including physically based rendering techniques and custom shader languages like Slang, optimized for mobile GPUs.

## Selected Projects

**[GP-Reporting](https://github.com/babaolu/GP-Reporting)**
This project is an enterprise-grade, role-gated monorepo portal developed to streamline monthly report management across various church units. It features AI-driven capabilities for parsing and summarizing reports, automated reminders, a leaderboard, and consolidated PDF/DOCX export options. The application ensures secure access with role-based views, robust authentication, and Supabase Row Level Security, alongside full mobile responsiveness for accessibility.
Stack: TypeScript, React, Node.js, Express, Supabase (PostgreSQL), Tailwind CSS, Resend, Telegram Bot API, PDFKit, Anthropic Claude, Google Gemini, OpenRouter, Nvidia NIM.

**[MyG](https://github.com/babaolu/MyG)**
MyG, or VulkanMind, is a local multi-agent AI system specifically designed to assist with modern Vulkan graphics programming and high-performance C++ systems engineering. This sophisticated orchestrator uses LangGraph to manage specialized agents for tasks like platform intelligence, knowledge retrieval, Vulkan-Hpp/VMA code generation, and debugging. It even includes a self-improvement loop to continuously refine its capabilities, showcasing advanced AI for developer tooling.
Stack: Python, FastAPI, LangGraph, Claude API, Qdrant, SQLite, Pydantic, Vulkan-Hpp, VMA, C++.

**[Poot](https://github.com/babaolu/Poot)**
Poot is a Decentralized Physical Infrastructure Network (DePIN) that ingeniously connects mobile device owners ("miners") with cloud customers. It operates on a demand-gated token economy, ensuring that tokens are only minted when customer instances actively consume miner resources, providing genuine economic backing. Technically, it employs decentralized zero-knowledge storage using erasure coding (Reed-Solomon) with AES-256-GCM encryption and k-redundancy for robust data integrity and privacy, managed by a C++23 orchestrator.
Stack: C++, Python, TypeScript, CMake, PostgreSQL, Docker, Reed-Solomon, AES-256-GCM, DePIN.

**[babaolu](https://github.com/babaolu/babaolu)**
This repository hosts my dynamic GitHub profile README, acting as a living portfolio that automatically updates to reflect my latest projects and technical specializations. It leverages GitHub Actions for automated content management, ensuring that my profile stays current and accurately showcases my ongoing contributions in areas such as native mobile development, high-performance graphics, scientific simulations, and decentralized systems, including recent AI-driven profile refreshing.
Stack: Python, GitHub Actions.

**[Dedication](https://github.com/babaolu/Dedication)**
Dedication is an interactive and highly responsive web application, meticulously crafted with Svelte 5 and Vite, designed to celebrate a significant event or individual. Originally a single HTML file, it was refactored into a modular, performance-oriented architecture. Key technical features include scroll-aware UI elements like a docked countdown, randomized gallery layouts for images, and elegant fallback mechanisms using CSS gradients and emoji icons if photo assets are missing, ensuring a polished user experience.
Stack: Svelte, CSS, JavaScript, HTML, Vite.

**[MScProj](https://github.com/babaolu/MScProj)**
This repository presents a comprehensive 2D multi-physics finite element simulation framework focused on modeling and optimizing flexible, wearable high-density electromyography (HD-EMG) electrode array bands for human forearms. The framework utilizes FEniCSx and GMSH for meshing and solving, PETSc for high-performance linear algebra, and R for data visualization. It incorporates advanced physics like Nitsche-type contact penalties and extracts electrical potentials, addressing complex electromechanical contact challenges for biomedical devices.
Stack: Python, FEniCSx (DOLFINx), GMSH, PETSc, R.

## Technical Skills

**Languages:** C++, Python, TypeScript, JavaScript, HTML, CSS, Svelte, PLpgSQL, Shell, R, Slang, CMake, Makefile

**AI & Machine Learning:** Multi-Agent AI Systems, Anthropic Claude, Google Gemini, OpenRouter, Nvidia NIM, LangGraph, AI-driven Parsing & Summarization, Knowledge Retrieval, Code Generation, Self-Improvement Loops

**Web Development:** React, Svelte, Vite, Node.js, Express.js, FastAPI, Tailwind CSS, Netlify Serverless Functions, RESTful APIs, HTML/CSS/JavaScript

**Database & Backend:** PostgreSQL, Supabase, SQLite, Row Level Security (RLS), Data Storage, Cloud Functions

**High-Performance Computing & Graphics:** C++ Systems Engineering, Vulkan, Android NDK, NativeActivity, ARM64 Development, Mobile GPU Optimization, Physically Based Rendering, FEniCSx (DOLFINx), GMSH, PETSc, Finite Element Analysis (FEA), Multi-physics Modeling, Biomechanics

**Decentralized Systems:** DePIN (Decentralized Physical Infrastructure Networks), Distributed Systems, Token Economies, Erasure Coding (Reed-Solomon), K-Redundancy, Zero-Knowledge Storage, AES-256-GCM

**DevOps & Tooling:** Docker, GitHub Actions, Vercel, `uv`, CMake, Git, `aapt2`, `zipalign`, `apksigner`, Cross-compilation, CI/CD Principles

## Contact

Feel free to reach out to me:

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:babaolu98@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/babatunde-adeoti-1614b2b9/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BzaeWA8N4TR2tSvr8Dg7evg%3D%3D)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/Overwor56755051)
