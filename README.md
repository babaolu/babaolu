# babaolu

Software Engineer specializing in AI-driven systems, real-time 3D reconstruction, high-performance C++ graphics, and scalable web applications, including decentralized infrastructure.

I'm a Software Engineer focused on designing and implementing robust systems across diverse domains. Recently, I've been building `3ill`, a novel system for real-time 3D scene reconstruction from networked phones, and `learn-assist`, an adaptive tutoring platform leveraging advanced OCR and vision models. My work also includes developing scalable web applications like `clirt` and `hng_todo` that feature real-time synchronization and intricate user interfaces, alongside engineering an automated GitHub profile (`babaolu`) to reflect my evolving technical landscape.

## Core focus areas

**AI-Driven Systems & Agent Orchestration**
*   Developed `learn-assist`, an adaptive tutoring system focused on high-fidelity text and mathematical formula extraction from textbook scans using vision models and local OCR for item-bank generation.
*   Engineered `MyG`, a multi-agent AI system that orchestrates specialized agents for Vulkan graphics code generation, validation, and debugging using LangGraph.
*   Implemented automated GitHub profile updates in `babaolu`, leveraging AI for content generation to ensure the profile reflects current project work and skills.

**Real-time 3D Reconstruction & Distributed Compute**
*   Created `3ill`, a system to fuse multiple phone camera perspectives into a navigable 3D scene in real time, employing distributed capture, compute, and viewer components.
*   Designed the `3ill` pipeline to handle photo/pose ingest, feature extraction, and tile rendering, with compute stages adaptable to compute-lender phones or cloud GPUs using CUDA-COLMAP.
*   Developed a placement guide for `3ill` that dynamically identifies optimal phone positions to maximize scene coverage and re-plans live as devices move.

**High-Performance Graphics & C++ Systems**
*   Implemented core Vulkan graphics rendering concepts in `VulkanTest`, including creating vertex buffers, managing swapchains, setting up graphics pipelines, and recording command buffers for scene rendering.
*   Designed and built the C++ orchestrator for `Poot`, a decentralized physical infrastructure network, enabling efficient resource allocation and management within a distributed environment.
*   Rewrote `TerAI` in C++ for native ARM64 compilation, achieving significant performance gains for on-device AI applications with zero-latency startup and direct `libllama.so` linkage.

**Scalable Web Applications & Real-time Synchronization**
*   Developed `clirt` and `clirt-mobile`, a web and Android application pair for custom T-shirt design, featuring live SVG previews, Google sign-in, and instant cart synchronization across devices using Pusher Channels.
*   Created `hng_todo`, a SvelteKit-based todo application with intelligent quick-add parsing for dates and lists, recurring task management, and drag-and-drop reordering.
*   Implemented a JSON API for `clirt` to support its mobile counterpart, alongside self-service account deletion and robust server-side validation for checkout and delivery.

## Selected Projects

### [babaolu](https://github.com/babaolu/babaolu)
This repository hosts my dynamic GitHub profile README, which is automatically generated and updated through a sophisticated GitHub Actions workflow. Its primary function is to provide a current and accurate overview of my technical expertise, highlighting my latest projects and evolving skill set without manual intervention. The automation process includes AI-powered content generation using the Gemini API, ensuring the profile remains up-to-date and reflects my ongoing work across various engineering domains.

Stack: Python, GitHub Actions, Gemini API

### [3ill](https://github.com/babaolu/3ill)
`3ill` is an innovative system designed to link multiple phones in a single location, fusing their camera perspectives into a navigable 3D scene that users can explore with a virtual camera, much like a video game. Built for the Meta Global AI Developer Hackathon, it features distributed processing where capture phones stream data to an aggregator, and compute-lender phones or cloud GPUs handle pipeline stages like decoding, feature extraction, and tile rendering. The project also includes a placement guide to optimize phone positioning for scene coverage.

Stack: Python, HTML, Shell, CUDA, COLMAP, GPU

### [learn-assist](https://github.com/babaolu/learn-assist)
`learn-assist` is an adaptive tutoring system designed to teach a textbook chapter to mastery and verify retention with delayed cold tests, exploring whether deep understanding is possible without reading the source material. The project focuses on high-fidelity text and mathematical formula extraction from scanned PDFs, using local OCR and vision models to overcome corruption in notation. Its multi-stage pipeline includes sophisticated item-bank generation with dual-model verification and difficulty screening, aiming to create transfer questions beyond mere recall.

Stack: Python, OCR, Vision Models

### [clirt-mobile](https://github.com/babaolu/clirt-mobile)
The Android application for Clirt, a custom T-shirt shop for Nigeria, `clirt-mobile` enables users to design custom tees, place orders, and track them with real-time cart synchronization with the web platform. Developed with Expo, it features seamless Google sign-in, a live design preview with various customization options (text, graphics, colors, sizes), and a straightforward checkout process with pay-on-delivery. The app ensures a consistent user experience by sharing cart and order data instantly across mobile and web platforms.

Stack: TypeScript, JavaScript, Expo, React Native

### [clirt](https://github.com/babaolu/clirt)
`clirt` is a web-based custom T-shirt shop for Nigeria, featuring a live SVG customizer where customers can design their shirts with text or graphics, drag elements into place, and see instant previews. The platform provides six styles with varying neck and sleeve options, supporting custom text effects and original graphics. Key technical features include instant cart synchronization across tabs and devices via Pusher Channels, Google sign-in, a robust JSON API for the accompanying mobile app, and server-side validation for order and delivery details, with pay-on-delivery.

Stack: TypeScript, Svelte, CSS, JavaScript, HTML, Vercel, Pusher Channels, Mailgun, PostgreSQL, Drizzle

### [hng_todo](https://github.com/babaolu/hng_todo)
`hng_todo` is a minimalist, single-account todo application built with SvelteKit on Vercel, utilizing PostgreSQL on Neon via Drizzle for data persistence. It features an intelligent quick-add input that understands natural language for dates and lists, a comprehensive view system (Today, Upcoming, Inbox, Lists, Logbook), and advanced recurring task management. Users benefit from drag-and-drop reordering, keyboard shortcuts, a detail panel for task management, and a powerful search function across titles and notes.

Stack: TypeScript, Svelte, SvelteKit, CSS, HTML, JavaScript, PostgreSQL, Drizzle, Neon, Vercel

## Technical Skills

**Languages:** C++, CMake, CSS, GLSL, HTML, JavaScript, PLpgSQL, Python, Shell, Svelte, SvelteKit, TypeScript

**Web Technologies:** Expo, FastAPI, Netlify, Pusher Channels, React Native, Svelte, SvelteKit, Supabase, Vercel

**Databases & Cloud Platforms:** Docker, Drizzle, GitHub Actions, Mailgun, Neon, PostgreSQL, Qdrant, SQLite, Supabase, Vercel

**AI & Distributed Systems:** AI Orchestration, COLMAP, Decentralized Networks, Demand-Gated Token Economies, Distributed Zero-Knowledge Storage, Large Language Models (LLMs), Multi-Agent Systems, OCR, On-device AI, Vision Models

**Tools & Libraries:** AES-256-GCM, ARM64, CMake, CUDA, Docker, Expo, FastAPI, Gemini API, GitHub Actions, GLSL, GPU, LangGraph, libcurl, libllama.so, Mailgun, nlohmann/json, Neon, Pydantic, Pusher Channels, readline, Reed-Solomon, structlog, uv, Vulkan-Hpp/VMA

## Contact

[Email](mailto:babaolu98@gmail.com) | [LinkedIn](https://www.linkedin.com/in/babatunde-adeoti-1614b2b9/)
