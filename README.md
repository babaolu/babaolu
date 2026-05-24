# babaolu

Software Engineer specializing in native mobile systems, high-performance graphics, and decentralized applications.

I focus on developing robust native applications for mobile platforms and building complex decentralized systems. My recent work includes crafting a C++ and Vulkan-based CAD application for Android, MobileCAD, and developing a decentralized physical infrastructure network called Poot. I also create practical API-driven solutions, such as the `HNG_c14BE3-cli` for interacting with external services and `InterGen`, a web tool leveraging AI.

## Core focus areas

**Native Mobile & High-Performance Graphics**
*   Developing native Android applications using C++20, Vulkan, and Android NDK NativeActivity for direct hardware interaction.
*   Building custom ARM64 toolchains for compiling native mobile applications without reliance on traditional build systems like Gradle.
*   Implementing graphics rendering pipelines optimized for mobile GPUs with custom shader languages such as Slang.

**Decentralized Systems & Distributed Computing**
*   Designing and implementing Decentralized Physical Infrastructure Networks (DePIN) that bridge mobile resource providers with cloud customers.
*   Developing demand-gated token economies to incentivize real-world resource consumption in distributed systems.
*   Ensuring data integrity and uptime in decentralized environments using techniques like erasure coding and k-redundancy.

**API Development & CLI/Web Tooling**
*   Creating API-driven web tools, including serverless functions for interacting with AI models like Google Gemini.
*   Developing globally installable command-line interfaces (CLIs) for authenticating with and managing external APIs using secure credential storage and token refresh.
*   Building backend services in C++ and Python to support distributed applications and API endpoints, often integrating with databases like PostgreSQL.

## Selected Projects

**[InterGen](https://github.com/babaolu/InterGen)**
InterGen is a lightweight web tool that takes any job title and returns three thoughtful, role-specific interview questions, powered by the Google Gemini API. Built as part of a technical screen exercise, the project emphasizes simple, readable, and secure code. It utilizes a Netlify serverless function to proxy requests to the Google Gemini API, ensuring security and efficiency, with its frontend developed using plain HTML, CSS, and JavaScript, demonstrating a preference for framework-agnostic solutions.
Stack: HTML, JavaScript, Node.js, Netlify Serverless Functions, Google Gemini API

**[babaolu](https://github.com/babaolu/babaolu)**
This repository serves as my dynamic GitHub profile README, designed to automatically update and reflect my latest projects, skills, and specializations. It acts as a living portfolio, consolidating my work in native mobile systems, high-performance graphics, and decentralized applications. The project itself demonstrates the implementation of GitHub Actions for automated content management, ensuring that my profile remains current and accurately showcases my ongoing technical contributions and evolving areas of interest.
Stack: Python, GitHub Actions

**[MobileCAD](https://github.com/babaolu/MobileCAD)**
MobileCAD is a native Android CAD application developed with C++20 and Vulkan, utilizing Android NDK NativeActivity for direct hardware interaction without X11 or GLFW. This project showcases deep expertise in low-level mobile graphics, incorporating the Slang shader language and managing manual APK packaging. Recent development has focused on resolving critical runtime crash bugs related to Vulkan swapchain management and `ANativeActivity` lifecycle, ensuring robust application stability and performance through meticulous debugging and error handling.
Stack: C++, CMake, Shell, Slang, Vulkan, Android NDK, aapt2, zipalign, apksigner

**[Poot](https://github.com/babaolu/Poot)**
Poot is a Decentralized Physical Infrastructure Network (DePIN) designed to connect mobile resource providers with cloud customers. It features a unique demand-gated token economy, minting tokens only when real customer instances actively consume miner resources, thereby preventing speculative inflation. Technically, it employs secure data sharding using erasure coding (Reed-Solomon) and k-redundancy for fault tolerance, alongside a C++23 orchestrator service integrated with PostgreSQL to manage the distributed network efficiently.
Stack: Makefile, C++, CMake, Python, TypeScript, PostgreSQL, Reed-Solomon

**[arm-ndk](https://github.com/babaolu/arm-ndk)**
This project provides a reusable toolchain infrastructure for cross-compiling native C++/Vulkan Android applications directly on ARM64 devices within PRoot Ubuntu environments. It eliminates the need for Gradle or x86_64 emulation by leveraging the system's native `clang` compiler with NDK sysroot and libraries. The custom CMake toolchain and accompanying Bash scripts handle direct APK construction using `aapt2`, `zipalign`, and `apksigner`, demonstrating a comprehensive understanding of low-level Android build and packaging processes.
Stack: CMake, Shell, C++, Android NDK, Vulkan, ARM64, clang, PRoot Ubuntu, aapt2, zipalign, apksigner

**[HNG_c14BE3-cli](https://github.com/babaolu/HNG_c14BE3-cli)**
This globally installable command-line interface (CLI) for the Insighta Labs+ API provides a secure and robust method for interacting with user profiles and managing data. It integrates GitHub OAuth with PKCE for secure authentication, storing credentials locally with strict permissions, and automatically refreshes access tokens to maintain session integrity. The CLI demonstrates strong backend integration, effective terminal-based user interface design, and secure authentication best practices for API interactions.
Stack: JavaScript, Node.js, GitHub OAuth, PKCE

## Technical Skills

*   **Languages:** C++, Python, JavaScript, HTML, TypeScript, Shell, Slang, CMake, Makefile
*   **Mobile & Graphics:** Android NDK, Vulkan, NativeActivity, ARM64 Development, Mobile GPU Optimization, Cross-compilation, Manual APK Packaging (`aapt2`, `zipalign`, `apksigner`), Slang, PRoot Ubuntu
*   **Decentralized Systems:** DePIN (Decentralized Physical Infrastructure Networks), Distributed Systems, Token Economies, Erasure Coding (Reed-Solomon), K-Redundancy
*   **Backend & APIs:** Node.js, Serverless Functions (Netlify), API Integration, PostgreSQL, GitHub OAuth, PKCE Authentication, CLI Development, RESTful APIs, Google Gemini API
*   **Tooling & Build Systems:** CMake, Ninja, Git, GitHub Actions, clang, Termux
*   **AI/ML:** Google Gemini API, Natural Language Processing (via API)

## Contact

Feel free to reach out to me:

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:obayomi.tijani@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/obayomi-tijani)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/obayomiti)
