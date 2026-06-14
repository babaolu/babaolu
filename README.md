# babaolu

Software Engineer crafting native mobile experiences, high-performance graphics, scientific simulations, and decentralized systems.

I build robust native applications for mobile platforms, as seen in my work on **MobileCAD**, a C++20 and Vulkan-based CAD application for Android. My recent efforts also extend to scientific computing with **MScProj**, where I developed a multi-physics finite element simulation framework for wearable HD-EMG devices, and architect decentralized systems like **Poot**, a DePIN bridging mobile resource providers with cloud customers. Additionally, I create practical API-driven solutions such as the **InterGen** web tool which leverages AI, and craft interactive web experiences like **Dedication** using Svelte.

## Core focus areas

**Native Mobile & High-Performance Graphics**
*   Developing native Android CAD applications using C++20, Vulkan, and Android NDK NativeActivity for direct hardware interaction, as demonstrated in `MobileCAD`.
*   Building custom ARM64 toolchains for compiling native mobile applications on-device without reliance on traditional build systems like Gradle (`arm-ndk`).
*   Implementing graphics rendering pipelines optimized for mobile GPUs with custom shader languages like Slang, handling manual APK packaging, and ensuring application stability.

**Scientific Computing & Simulation**
*   Developing 2D multi-physics finite element simulation frameworks to model electromechanical interactions in wearable devices (`MScProj`).
*   Utilizing high-performance computing libraries like FEniCSx, GMSH, and PETSc for solving complex partial differential equations in biomechanics simulations.
*   Implementing advanced features such as Nitsche-type contact penalties and extracting electrical potentials at electrode interfaces within detailed physical models.

**Decentralized Systems & Distributed Computing**
*   Designing and implementing Decentralized Physical Infrastructure Networks (DePIN) that bridge mobile resource providers with cloud customers, exemplified by `Poot`.
*   Developing demand-gated token economies to incentivize real-world resource consumption and prevent inflation in distributed systems.
*   Ensuring data integrity and high availability in decentralized environments using erasure coding (Reed-Solomon) and k-redundancy.

**Web Development & API Tooling**
*   Crafting interactive and responsive web applications using modern frameworks like Svelte 5 and Vite (`Dedication`).
*   Creating API-driven web tools, including serverless functions for interacting with AI models like Google Gemini (`InterGen`).
*   Developing backend orchestrator services in C++23, often integrating with databases like PostgreSQL, to support distributed applications (`Poot`).

## Selected Projects

**[Poot](https://github.com/babaolu/Poot)**
Poot is a pioneering Decentralized Physical Infrastructure Network (DePIN) that connects mobile resource providers (miners) with cloud customers through a demand-gated token economy. Its innovative design ensures tokens are only minted when real customer instances actively consume miner resources, preventing speculative inflation. The system ensures data integrity and high availability through secure data sharding with erasure coding (Reed-Solomon) and k-redundancy, ensuring customer data privacy and resilience against individual miner churn. The architecture includes a C++23 orchestrator service integrated with PostgreSQL to efficiently manage the distributed network.
Stack: Makefile, C++, CMake, Python, TypeScript, PostgreSQL, Reed-Solomon, DePIN

**[Dedication](https://github.com/babaolu/Dedication)**
This project is a beautifully structured, highly responsive, interactive web application, built with Svelte 5 and Vite, designed to celebrate an individual's dedication. It was migrated from a single-file HTML layout to a modular, performance-oriented architecture, showcasing modern web development practices. Technically, it features advanced scroll-aware UI elements like a docked countdown with map buttons, randomized gallery layouts for images, and elegant fallback mechanisms using CSS gradients and emoji icons if photo assets are unavailable. The site also incorporates natural scrolling transitions and entry animations.
Stack: Svelte, CSS, JavaScript, HTML, Vite

**[babaolu](https://github.com/babaolu/babaolu)**
This `babaolu` repository serves as my dynamic GitHub profile README, designed to automatically update and reflect my latest projects and specializations. It acts as a living portfolio, consolidating my work in areas like native mobile systems, high-performance graphics, and decentralized applications. The project itself demonstrates the implementation of GitHub Actions for automated content management, ensuring that my profile remains current and accurately showcases my ongoing technical contributions, including recent improvements to the update logic and AI-driven profile refreshing.
Stack: Python, GitHub Actions

**[MScProj](https://github.com/babaolu/MScProj)**
This repository contains a comprehensive 2D multi-physics finite element simulation framework designed to model, analyze, and optimize flexible, wearable high-density electromyography (HD-EMG) electrode array bands. It leverages FEniCSx and GMSH for meshing and solving, with PETSc for high-performance linear algebra and R for visualization. The project addresses the technical challenge of balancing electromechanical contact quality with bioelectric signal resolution, incorporating advanced physics like Nitsche-type contact penalties for linear elasticity and detailed electrical potential extraction at electrode interfaces.
Stack: Python, FEniCSx (DOLFINx), GMSH, PETSc, R

**[InterGen](https://github.com/babaolu/InterGen)**
InterGen is a lightweight web tool designed to generate three thoughtful, role-specific interview questions for any given job title, powered by the Google Gemini API. Developed as part of a technical screen, the project prioritizes simple, readable, and secure code. It features a plain HTML, CSS, and JavaScript frontend, communicating with a Netlify Serverless Function (Node.js) that securely proxies requests to the `gemini-2.5-flash` API, demonstrating a practical approach to integrating AI into web applications with a serverless architecture.
Stack: HTML, JavaScript, Node.js, Netlify Serverless Functions, Google Gemini API

**[MobileCAD](https://github.com/babaolu/MobileCAD)**
MobileCAD is a native Android CAD application built using C++20 and Vulkan, leveraging Android NDK NativeActivity for direct hardware interaction without reliance on high-level frameworks like X11 or GLFW. This project highlights deep expertise in low-level mobile graphics development, including the use of the Slang shader language, manual APK packaging with `aapt2`, `zipalign`, and `apksigner`, and strict C++ Core Guidelines compliance. Recent work has focused on robust error handling and fixing critical runtime crash bugs related to Vulkan swapchain management and the `ANativeActivity` lifecycle, ensuring high performance and stability on ARM64 devices.
Stack: C++, CMake, Shell, Slang, Vulkan, Android NDK, aapt2, zipalign, apksigner, ARM64

## Technical Skills

*   **Languages:** C++, Python, JavaScript, HTML, TypeScript, Shell, Svelte, CSS, Slang, CMake, Makefile, R
*   **Mobile & High-Performance Graphics:** Android NDK, Vulkan, NativeActivity, ARM64 Development, Mobile GPU Optimization, Slang, Cross-compilation, `aapt2`, `zipalign`, `apksigner`, Physically Based Rendering
*   **Scientific Computing & Simulation:** FEniCSx (DOLFINx), PETSc, Finite Element Analysis (FEA), Multi-physics Modeling, Biomechanics, Numerical Methods, R, GMSH
*   **Decentralized Systems:** DePIN (Decentralized Physical Infrastructure Networks), Distributed Systems, Token Economies, Erasure Coding (Reed-Solomon), K-Redundancy
*   **Web & API Development:** Svelte, Vite, HTML/CSS/JavaScript, Node.js, Serverless Functions (Netlify), API Integration, PostgreSQL, Google Gemini API, C++ Backend Development, Python Backend Development, CLI Development, RESTful APIs
*   **Tooling & DevOps:** CMake, Ninja, Git, GitHub Actions, `clang`, Makefile, `aapt2`, `zipalign`, `apksigner`, CI/CD Principles
*   **AI/ML:** Google Gemini API, AI Integration, Natural Language Processing

## Contact

Feel free to reach out to me:

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:babaolu98@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/babatunde-adeoti-1614b2b9/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BzaeWA8N4TR2tSvr8Dg7evg%3D%3D)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/Overwor56755051)
