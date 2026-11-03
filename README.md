# babaolu

Systems Engineer specializing in high-performance C++/Vulkan graphics, real-time 3D spatial reconstruction, adaptive AI pipelines, and synchronized full-stack applications.

I am a software engineer focused on building low-level graphics engines, distributed spatial compute platforms, and real-time synchronized applications. Recently, I developed [MobileCAD](https://github.com/babaolu/MobileCAD), a native Vulkan 1.4 3D CAD engine built on Android entirely inside Termux, and [3ill](https://github.com/babaolu/3ill), a multi-phone 3D scene reconstruction engine created for the Meta Global AI Developer Hackathon. My work spans low-level system graphics, AI-driven adaptive learning systems like [learn-assist](https://github.com/babaolu/learn-assist), and synchronized cross-platform e-commerce tools like [clirt](https://github.com/babaolu/clirt).

## Core Focus Areas

**High-Performance Graphics & Mobile Systems**
* Built [MobileCAD](https://github.com/babaolu/MobileCAD), a native C++20 and Vulkan 1.4 CAD application directly targeting Android's `NativeActivity` and `ANativeWindow`, bypassing display servers and build wrappers like Gradle.
* Developed custom 120Hz VSync double-buffered render loops, S-Pen 2D sketch-on-plane tools, parametric CSG boolean operations, ray-picked 3D scene graphs, and binary STL mesh exporters.
* Configured a self-hosting compilation and execution environment targeting ARM64 mobile hardware directly within native Termux.

**Real-Time 3D Reconstruction & Spatial Computing**
* Engineered [3ill](https://github.com/babaolu/3ill) to fuse raw multi-phone camera feeds and pose data into unified, navigable 3D scenes accessible via virtual camera viewports.
* Architected a distributed split-compute pipeline offloading dense feature extraction, SAM masking, and rendering across compute-lender phones and cloud CUDA-COLMAP nodes.
* Implemented live placement coverage guidance that dynamically calculates blind spots and re-plans device positioning during camera drift.

**AI Systems, OCR & Adaptive Learning**
* Created [learn-assist](https://github.com/babaolu/learn-assist) to test mastery-based learning from technical textbooks using an automated, multi-stage evaluation pipeline.
* Built local OCR microservices combined with vision models to resolve corrupted mathematical notation, LaTeX symbols, and complex formulas in scanned engineering texts.
* Implemented isolated item-bank generators with non-author difficulty screening and dual-model verification for multi-concept transfer problems.

**Real-Time Full-Stack & Cross-Platform Sync**
* Developed [clirt](https://github.com/babaolu/clirt) and [clirt-mobile](https://github.com/babaolu/clirt-mobile), establishing sub-second state and cart synchronization across web and Android clients using Pusher Channels.
* Built dynamic interactive canvas customization tools featuring real-time SVG rendering, font effects, matrix positioning, and localized checkout flows for Nigeria.

## Selected Projects

### [MobileCAD](https://github.com/babaolu/MobileCAD)
MobileCAD is a native Android 3D CAD application engineered from scratch in C++20 and Vulkan 1.4 (`VK_API_VERSION_1_4`). Designed for high-performance mobile modeling with touchscreen and S-Pen inputs, it interfaces directly with Android `NativeActivity` and `ANativeWindow` without intermediate display servers or Gradle wrappers. The project features 120Hz VSync rendering, ear-clipping polygon extrusion, CSG boolean solid primitives, ray-picked scene graphs, binary STL exports, and a self-hosting Termux toolchain.

Stack: C++, Vulkan 1.4, CMake, Shell, Slang, Android NDK, Termux

### [3ill](https://github.com/babaolu/3ill)
Built for the Meta Global AI Developer Hackathon, 3ill links networked mobile devices together to capture physical locations and fuse multi-angle photos and poses into navigable 3D scenes. Its split-compute architecture distributes pipeline stages—including feature extraction, SAM masking, and dense CUDA-COLMAP reconstructions—between edge phones and cloud GPU workers, complete with live coverage tracking to guide user placement and handle camera drift.

Stack: Python, CUDA, COLMAP, SAM, HTML, Shell

### [babaolu](https://github.com/babaolu/babaolu)
An automated GitHub profile generator driven by GitHub Actions that dynamically updates this profile README to reflect real-time engineering output. The system fetches repository data, commit logs, and topic metadata across all active projects, utilizing the Google Gemini API (`gemini-3.5-flash`) with structured error handling and automated fallbacks to rewrite technical summaries and preserve accurate engineering metrics.

Stack: Python, GitHub Actions, Gemini API

### [learn-assist](https://github.com/babaolu/learn-assist)
learn-assist is an adaptive tutoring platform engineered to evaluate whether students can achieve mastery over complex technical material (such as MRI physics) strictly through automated instruction. To bypass corrupted PDF notation, it uses vision models and a local OCR microservice to clean mathematical formulas before synthesizing multi-concept item banks, performing non-author difficulty screening, and executing offline mastery verification loops.

Stack: Python, Local OCR, Vision Models

### [clirt-mobile](https://github.com/babaolu/clirt-mobile)
The native Android client for the Clirt T-shirt customization service, built using React Native and Expo. It provides Google OAuth authentication, an interactive design canvas with live previews, 2D manipulation controls, and sub-second cart synchronization with web sessions powered by Pusher Channels. It includes full order management and localized checkout across all 36 Nigerian states and the FCT.

Stack: TypeScript, JavaScript, React Native, Expo, Pusher Channels

### [clirt](https://github.com/babaolu/clirt)
Clirt is a full-stack e-commerce platform and custom T-shirt design shop optimized for Nigerian users. Built with Svelte and hosted on Vercel, it features a live SVG customization engine with drag-and-drop vector manipulation, real-time multi-device cart synchronization via Pusher Channels, transactional notifications through Mailgun, and a shared `/api/v1` REST backend servicing both web browsers and native mobile clients.

Stack: TypeScript, Svelte, CSS, JavaScript, HTML, Vercel, Pusher Channels, Mailgun

## Technical Skills

**Languages:** C++, TypeScript, Python, JavaScript, HTML, CSS, Shell, CMake, Slang, Svelte

**Graphics, Vision & Spatial Computing:** Vulkan 1.4, CUDA, COLMAP, Segment Anything Model (SAM), Dear ImGui, Android NDK, 3D Parametric CAD, Ray Picking

**AI & Machine Learning:** LangGraph, Multi-Agent Systems, Vision Models, Local OCR, Gemini API, Adaptive Learning Systems

**Web & Mobile Frameworks:** SvelteKit, React Native, Expo, Node.js, REST APIs

**Databases & Cloud Infrastructure:** PostgreSQL, Drizzle, Neon, Vercel, Pusher Channels, GitHub Actions, Mailgun, Docker, Termux

## Contact

[Email](mailto:babaolu98@gmail.com) | [LinkedIn](https://www.linkedin.com/in/babatunde-adeoti-1614b2b9/)
