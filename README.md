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

**[babaolu](https://github.com/babaolu/babaolu)**
This repository serves as my dynamic GitHub profile README, designed to automatically update and reflect my latest projects and skills. It consolidates my specializations in native mobile systems, high-performance graphics, and decentralized applications, providing a living overview of my technical interests. The project itself demonstrates an understanding of GitHub Actions for automating profile content management and ensures my README remains current with my ongoing development work.
Stack: Python, GitHub Actions

**[MobileCAD](https://github.com/babaolu/MobileCAD)**
MobileCAD is a native Android CAD application built entirely with C++20 and Vulkan, leveraging Android NDK NativeActivity for direct hardware rendering without reliance on frameworks like X11 or GLFW. This project showcases deep expertise in low-level mobile graphics, incorporating a custom shader language (Slang) and managing manual APK packaging processes. Recent work involved addressing critical crash bugs related to Vulkan swapchain management and `ANativeActivity` lifecycle events, ensuring application stability.
Stack: C++, CMake, Shell, Slang, Vulkan, Android NDK

**[Poot](https://github.com/babaolu/Poot)**
Poot is a Decentralized Physical Infrastructure Network (DePIN) that connects mobile miners offering residual device resources (CPU, RAM, storage) with cloud customers seeking affordable hosting. It features a unique demand-gated token economy where tokens are minted only when customer instances actively consume resources, preventing speculative inflation. Technical highlights include secure data sharding via erasure coding (Reed-Solomon), k-redundancy for fault tolerance, and a C++23 orchestrator service with PostgreSQL integration.
Stack: Makefile, C++, CMake, Python, TypeScript, PostgreSQL, Reed-Solomon

**[arm-ndk](https://github.com/babaolu/arm-ndk)**
This project provides a reusable toolchain infrastructure for cross-compiling native C++/Vulkan Android applications directly on ARM64 devices within PRoot Ubuntu environments. It streamlines development by using the system's native `clang` compiler with the NDK's sysroot and libraries, eliminating the need for Gradle or x86_64 emulation. The custom CMake toolchain and Bash script for manual APK construction via `aapt2`, `zipalign`, and `apksigner` demonstrate a thorough understanding of Android's low-level build and packaging mechanisms.
Stack: CMake, Shell, C++, Android NDK, Vulkan, ARM64

**[InterGen](https://github.com/babaolu/InterGen)**
InterGen is a lightweight web tool built with plain HTML, CSS, and JavaScript, designed to generate thoughtful, role-specific interview questions based on any job title. It achieves this by calling a Netlify serverless function that proxies requests to the Google Gemini API. This project highlights efficient API integration, serverless architecture, and straightforward frontend development, showcasing a practical and user-friendly application of artificial intelligence for interview preparation.
Stack: HTML, JavaScript, Node.js, Netlify Serverless Functions, Google Gemini API

**[HNG_c14BE3-cli](https://github.com/babaolu/HNG_c14BE3-cli)**
This project is a globally installable command-line interface (CLI) for the Insighta Labs+ API, offering a robust and secure method for interacting with user profiles, performing searches, and managing data. It incorporates GitHub OAuth with PKCE for secure authentication, stores credentials locally with strict permissions, and automatically refreshes access tokens to maintain session integrity. The CLI demonstrates strong backend integration, secure authentication practices, and effective terminal-based user interface design.
Stack: JavaScript, Node.js, GitHub OAuth, PKCE

## Technical Skills

*   **Languages:** C++, Python, JavaScript, HTML, TypeScript, Shell, Slang, CMake, Makefile
*   **Mobile & Graphics:** Android NDK, Vulkan, NativeActivity, ARM64 Development, Mobile GPU Optimization, Cross-compilation, Manual APK Packaging (`aapt2`, `zipalign`, `apksigner`)
*   **Decentralized Systems:** DePIN (Decentralized Physical Infrastructure Networks), Distributed Systems, Erasure Coding (Reed-Solomon), K-Redundancy, Token Economies
*   **Backend & APIs:** Node.js, Serverless Functions (Netlify), API Integration, PostgreSQL, GitHub OAuth, PKCE Authentication, CLI Development, RESTful APIs
*   **Tooling & Build Systems:** CMake, Ninja, Git, GitHub Actions, Termux, PRoot Ubuntu
*   **AI/ML:** Google Gemini API, Natural Language Processing (via API)

## Contact
