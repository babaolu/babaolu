# babaolu

Software Engineer focused on native mobile systems, high-performance graphics, scientific computing, and decentralized applications.

I build robust native applications for mobile platforms, as seen in my work on **MobileCAD**, a C++20 and Vulkan-based CAD application for Android, and the custom ARM64 toolchains developed in **arm-ndk**. My recent work also extends to scientific computing with **MScProj**, where I developed a multi-physics finite element simulation framework for wearable HD-EMG devices. Additionally, I architect decentralized systems like **Poot**, a DePIN bridging mobile resource providers with cloud customers, and create practical API-driven solutions such as the **InterGen** web tool which leverages AI.

## Core focus areas

**Native Mobile & High-Performance Graphics**
*   Developing native Android CAD applications using C++20, Vulkan, and Android NDK NativeActivity for direct hardware interaction, as demonstrated in `MobileCAD`.
*   Building custom ARM64 toolchains for compiling native mobile applications on-device without reliance on traditional build systems like Gradle (`arm-ndk`).
*   Implementing graphics rendering pipelines optimized for mobile GPUs with custom shader languages such as Slang, and handling manual APK packaging.

**Scientific Computing & Simulation**
*   Developing 2D multi-physics finite element simulation frameworks to model electromechanical interactions in wearable devices (`MScProj`).
*   Utilizing high-performance computing libraries like FEniCSx, GMSH, and PETSc for solving complex partial differential equations in biomechanics simulations (`MScProj`).
*   Implementing advanced features such as Nitsche-type contact penalties and extracting electrical potentials at electrode interfaces within detailed physical models (`MScProj`).

**Decentralized Systems & Distributed Computing**
*   Designing and implementing Decentralized Physical Infrastructure Networks (DePIN) that bridge mobile resource providers with cloud customers, exemplified by `Poot`.
*   Developing demand-gated token economies to incentivize real-world resource consumption and prevent inflation in distributed systems (`Poot`).
*   Ensuring data integrity and high availability in decentralized environments using erasure coding (Reed-Solomon) and k-redundancy (`Poot`).

**API Development & Web/CLI Tooling**
*   Creating API-driven web tools, including serverless functions for interacting with AI models like Google Gemini (`InterGen`).
*   Developing globally installable command-line interfaces (CLIs) for authenticating with and managing external APIs (`HNG_c14BE3-cli`).
*   Building backend orchestrator services in C++23, often integrating with databases like PostgreSQL, to support distributed applications (`Poot`).

## Selected Projects

**[MScProj](https://github.com/babaolu/MScProj)**
This repository contains a comprehensive 2D multi-physics finite element simulation framework designed to model, analyze, and optimize flexible, wearable high-density electromyography (HD-EMG) electrode array bands. It leverages FEniCSx and GMSH for meshing and solving, with PETSc for high-performance linear algebra and R for visualization. The project addresses the technical challenge of balancing electromechanical contact quality with bioelectric signal resolution, incorporating advanced physics like Nitsche-type contact penalties and detailed electrical potential extraction.
Stack: Python, FEniCSx (DOLFINx), GMSH, PETSc, R

**[babaolu](https://github.com/babaolu/babaolu)**
This `babaolu` repository serves as my dynamic GitHub profile README, designed to automatically update and reflect my latest projects and specializations. It acts as a living portfolio, consolidating my work in native mobile systems, high-performance graphics, and decentralized applications. The project itself demonstrates the implementation of GitHub Actions for automated content management, ensuring that my profile remains current and accurately showcases my ongoing technical contributions, including recent improvements to the update logic and AI-driven profile refreshing.
Stack: Python, GitHub Actions

**[InterGen](https://github.com/babaolu/InterGen)**
InterGen is a lightweight web tool designed to generate three thoughtful, role-specific interview questions for any given job title, powered by the Google Gemini API. Developed as part of a technical screen, the project prioritizes simple, readable, and secure code. It features a plain HTML, CSS, and JavaScript frontend, communicating with a Netlify Serverless Function (Node.js) that securely proxies requests to the `gemini-2.5-flash` API, demonstrating a practical approach to integrating AI into web applications with a serverless architecture.
Stack: HTML, JavaScript, Node.js, Netlify Serverless Functions, Google Gemini API

**[MobileCAD](https://github.com/babaolu/MobileCAD)**
MobileCAD is a native Android CAD application built using C++20 and Vulkan, leveraging Android NDK NativeActivity for direct hardware interaction without reliance on high-level frameworks like X11 or GLFW. This project highlights deep expertise in low-level mobile graphics development, including custom ARM64 toolchains, the Slang shader language, and manual APK packaging. Recent work has focused on robust error handling and fixing critical runtime crash bugs related to Vulkan swapchain management and the `ANativeActivity` lifecycle, ensuring high performance and stability.
Stack: C++, CMake, Shell, Slang, Vulkan, Android NDK, aapt2, zipalign, apksigner, ARM64

**[Poot](https://github.com/babaolu/Poot)**
Poot is a pioneering Decentralized Physical Infrastructure Network (DePIN) that connects mobile resource providers with cloud customers. It features a unique demand-gated token economy, where tokens are only minted when real customer instances actively consume miner resources, preventing speculative inflation. The system ensures data integrity and customer uptime through secure data sharding with erasure coding (Reed-Solomon) and k-redundancy. Its architecture includes a C++23 orchestrator service integrated with PostgreSQL to efficiently manage the distributed network.
Stack: Makefile, C++, CMake, Python, TypeScript, PostgreSQL, Reed-Solomon, DePIN

**[arm-ndk](https://github.com/babaolu/arm-ndk)**
This project provides reusable toolchain infrastructure for cross-compiling native C++/Vulkan Android applications directly on ARM64 devices within PRoot Ubuntu environments, bypassing the need for Gradle or x86_64 emulation. It employs the system's native `clang` compiler with the NDK's sysroot and libraries. The custom CMake toolchain file and accompanying Bash scripts handle direct APK construction using `aapt2`, `zipalign`, and `apksigner`, demonstrating a comprehensive understanding of low-level Android build processes and achieving independent native development workflows.
Stack: CMake, Shell, C++, Android NDK, Vulkan, ARM64, clang, PRoot Ubuntu, aapt2, zipalign, apksigner

## Technical Skills

*   **Languages:** C++, Python, JavaScript, HTML, TypeScript, Shell, Slang, CMake, Makefile
*   **Mobile & High-Performance Graphics:** Android NDK, Vulkan, NativeActivity, ARM64 Development, Mobile GPU Optimization, Slang, Cross-compilation, `aapt2`, `zipalign`, `apksigner`, PRoot Ubuntu, Physically Based Rendering, GMSH
*   **Scientific Computing & Simulation:** FEniCSx (DOLFINx), PETSc, Finite Element Analysis (FEA), Multi-physics Modeling, Biomechanics, Numerical Methods, R (for visualization/analysis)
*   **Decentralized Systems:** DePIN (Decentralized Physical Infrastructure Networks), Distributed Systems, Token Economies, Erasure Coding (Reed-Solomon), K-Redundancy
*   **Backend & APIs:** Node.js, Serverless Functions (Netlify), API Integration, PostgreSQL, GitHub OAuth, PKCE Authentication, CLI Development, RESTful APIs, Google Gemini API, C++ Backend Development, Python Backend Development
*   **Tooling & DevOps:** CMake, Ninja, Git, GitHub Actions, `clang`, Termux, Makefile, `aapt2`, `zipalign`, `apksigner`, PRoot Ubuntu, CI/CD Principles
*   **AI/ML:** Google Gemini API, AI Integration, Natural Language Processing

## Contact

Feel free to reach out to me:

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:obayomi.tijani@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/obayomi-tijani)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/obayomiti)
