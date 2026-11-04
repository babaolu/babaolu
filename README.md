# babaolu

Systems Engineer specializing in high-performance C++/Vulkan graphics, real-time spatial reconstruction, adaptive AI pipelines, and synchronized cross-platform applications.

I am a software engineer focused on building low-level graphics engines, distributed spatial compute platforms, and real-time synchronized applications. My recent work includes [MobileCAD](https://github.com/babaolu/MobileCAD), a native C++20/Vulkan 1.4 CAD engine engineered and compiled entirely on-device inside Termux, and [3ill](https://github.com/babaolu/3ill), a multi-phone 3D scene reconstruction platform created for the Meta Global AI Developer Hackathon. I also develop AI-driven learning systems like [learn-assist](https://github.com/babaolu/learn-assist) and real-time synchronized e-commerce services like [clirt](https://github.com/babaolu/clirt).

## Core Focus Areas

**High-Performance Graphics & Mobile Systems**
* Built [MobileCAD](https://github.com/babaolu/MobileCAD) in C++20 and Vulkan 1.4, interfacing directly with Android's `NativeActivity` and `ANativeWindow` to bypass display servers and build wrappers like Gradle.
* Implemented Cook-Torrance GGX PBR specular shading, S-Pen 2D sketch-on-plane tools, parametric CSG boolean operations, STL/OBJ mesh processing, and zero-lag undo/redo history stacks.
* Configured a self-hosting toolchain compiling, packaging, signing, and running ARM64 native binaries directly within Termux on mobile hardware.

**Real-Time 3D Reconstruction & Spatial Computing**
* Engineered [3ill](https://github.com/babaolu/3ill) to aggregate multi-device photo and camera pose streams into unified, navigable 3D spatial reconstructions.
* Architected a distributed split-compute pipeline offloading feature extraction, SAM masking, and dense CUDA-COLMAP reconstructions across compute-lender edge devices and cloud GPU nodes.
* Implemented live placement coverage guidance that dynamically calculates scene blind spots and re-plans positioning during camera drift.

**AI Systems, Local OCR & Adaptive Learning**
* Created [learn-assist](https://github.com/babaolu/learn-assist) to evaluate technical textbook mastery through an automated, multi-stage adaptive tutoring and retention evaluation system.
* Combined local OCR microservices with vision models to clean mangled mathematical notation, LaTeX symbols, and complex formulas from scanned textbook PDFs.
* Built isolated item-bank generators with non-author difficulty screening, concept topic mapping, and offline runner isolation.

**Real-Time Full-Stack & Cross-Platform Synchronization**
* Developed [clirt](https://github.com/babaolu/clirt) and [clirt-mobile](https://github.com/babaolu/clirt-mobile), establishing sub-second state and cart synchronization across Svelte web clients and Expo Android apps using Pusher Channels.
* Designed interactive SVG customization engines featuring drag-and-drop vector manipulation, font effects, matrix positioning, and localized pay-on-delivery checkout flows.

## Selected Projects

### [MobileCAD](https://github.com/babaolu/MobileCAD)
MobileCAD is a native Android 3D CAD application built from scratch in C++20 and Vulkan 1.1–1.4 featuring Cook-Torrance GGX PBR specular rendering and hardware-accelerated 3D primitives. The engine interfaces directly with Android's `NativeActivity` and `ANativeWindow`, bypassing display servers and Gradle wrappers to compile and execute entirely inside Termux on ARM64 hardware. Recent additions include interactive in-app tutorials, STL/OBJ mesh importers, S-Pen freehand and spline sketching, parametric CSG boolean operations, zero-lag undo history, 3D calipers, and automated 16 KB page-aligned APK releases via GitHub Actions.

Stack: C++, Vulkan, CMake, Shell, Slang, Android NDK, Termux

### [babaolu](https://github.com/babaolu/babaolu)
An automated profile generator and CI/CD workflow that dynamically maintains this GitHub profile README based on real-time commit telemetry and repository metadata. Driven by Python scripts running inside GitHub Actions, the system integrates Google's `gemini-3.5-flash` API with robust retry, fallback, and error-handling routines to synthesize low-level development activity and repository releases into structured technical profile documentation.

Stack: Python, GitHub Actions, Google Gemini API

### [3ill](https://github.com/babaolu/3ill)
Engineered for the Meta Global AI Developer Hackathon, 3ill links multiple mobile devices in a shared physical space to aggregate multi-angle photos and camera poses into navigable 3D scene reconstructions. The platform employs a split-compute architecture where camera-off devices and cloud GPU nodes handle pipeline workloads—including feature extraction, SAM masking, and dense CUDA-COLMAP reconstructions—while providing real-time visual placement guidance that re-plans device layouts when camera drift occurs.

Stack: Python, CUDA, COLMAP, SAM (Segment Anything Model), HTML, Shell

### [learn-assist](https://github.com/babaolu/learn-assist)
learn-assist is an adaptive tutoring system designed to evaluate whether learners can master complex technical topics—such as magnetic resonance imaging signal generation—strictly through automated instruction. It resolves corrupted OCR layers in scanned textbook PDFs using vision models and a local OCR microservice, then executes automated item-bank generation with dual-model verification, non-author difficulty screening, concept topic mapping, and offline runner isolation to verify long-term retention.

Stack: Python, Local OCR Microservices, Vision Models

### [clirt-mobile](https://github.com/babaolu/clirt-mobile)
The mobile client for the Clirt custom apparel engine built with TypeScript and Expo/React Native for Android. It integrates Google OAuth matching web sessions, interactive vector preview tools for shirt cuts, colors, and typography, real-time cart synchronization using Pusher Channels, and a localized checkout system supporting all 36 Nigerian states and the FCT with pay-on-delivery order tracking.

Stack: TypeScript, JavaScript, React Native, Expo, Pusher Channels

### [clirt](https://github.com/babaolu/clirt)
A full-stack e-commerce web application for custom apparel design in Nigeria built with TypeScript and Svelte. The platform features an in-browser live SVG customization canvas, sub-second cross-device cart synchronization powered by Pusher Channels, transactional notification pipelines via Mailgun, self-service account deletion, and a structured `/api/v1` REST backend shared directly with the native Android application.

Stack: TypeScript, Svelte, CSS, JavaScript, HTML, Pusher Channels, Mailgun

## Technical Skills

**Languages:** C++, TypeScript, Python, JavaScript, HTML, CSS, Shell, CMake, Slang, Svelte

**Graphics, Vision & Spatial Computing:** Vulkan 1.1–1.4, Cook-Torrance GGX PBR, CUDA, COLMAP, Segment Anything Model (SAM), Android NDK, Termux, Ray Picking, CSG Operations

**AI Systems & Data Engineering:** Vision Models, Local OCR, Google Gemini API, Multi-Agent Verification, Adaptive Learning Pipelines, GitHub Actions CI/CD

**Web & Mobile Frameworks:** Svelte, React Native, Expo, Node.js, REST APIs (`/api/v1`), Pusher Channels, Mailgun, Vercel

## Contact

[Email](mailto:babaolu98@gmail.com) | [LinkedIn](https://www.linkedin.com/in/babatunde-adeoti-1614b2b9/)
