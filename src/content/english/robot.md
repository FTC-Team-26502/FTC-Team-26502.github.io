---
title: "Our Robot"
description: "Meet our competition robots across FIRST Tech Challenge seasons."
layout: "robot"
draft: false

seasons:
- name: "DeCode"
  year: "2025-2026"
  current: true
  image: "images/robot/decode.jpg"
  overview: "Our DeCode season robot features a stable belt-driven mecanum drivetrain with low-centered motors, a ramp intake with powered wheels and servos, and a dual flywheel launcher driven by two 6000 RPM GoBilda motors. Built with custom 3D-printed and laser-cut parts, the design reflects lessons learned from three robot iterations during our rookie year."
  description: "Drivetrain:\nGoal was a stable and predictable mecanum drivetrain. Evolved from standard GoBilda geared drivetrain (V1) to center-mounted motors with belt drive (V3). Result: Lower center of gravity, smoother power transfer, and significantly improved stability.\n\nIntake:\nGoal was to collect balls from the field and reliably feed the shooter. Design choice: Ramp intake with powered wheels and servos. Iterated through three versions — from ramp with gecko wheels (V1), to adding 2 sets of GoBILDA intake wheels (V2), to extended ramp with a third set of wheels (V3). Result: Consistent intake, reliable ball transfer, and ability to load up to three balls.\n\nLauncher:\nGoal was to score consistently from multiple field locations. Early prototype was a tube shooter with manual feed, but it was inconsistent and location-limited. Transitioned to flywheel shooter for higher consistency. Fixed weak axle mount by adding heat-set inserts.\n\nCurrent Launcher Design:\n• Dual flywheels driven by two 6000 RPM GoBilda motors (1:1)\n• Mounted on 3D-printed base attached to rotating axle\n• Axle rotated by two 19.2:1 GoBilda motors\n\nLimitations: Motor vibration at high speed, limited max shooting angle at close range.\n\nPlanned Improvements: Stiffer 3D-printed mount, motor clamps and steel motor block."
  specs:
    - label: "Drivetrain"
      value: "Belt-driven mecanum with low-centered motors"
    - label: "Programming"
      value: "Java"
    - label: "Intake"
      value: "Ramp intake with powered wheels and servos (3 iterations)"
    - label: "Launcher"
      value: "Dual flywheel shooter — two 6000 RPM GoBilda motors, 3D-printed base, rotating axle"
    - label: "Manufacturing"
      value: "Custom 3D-printed and laser-cut parts"
  gallery:
    - image: "images/robot/decode-1.jpg"
      caption: "DeCode competition robot"
    - image: "images/robot/decode-2.jpg"
      caption: "Robot detail view"
  cad:
    enable: true
    label: "View CAD (Onshape)"
    link: "https://your-onshape-link-here.com"
  portfolio:
    enable: true
    label: "Download Portfolio"
    file: "/files/decode-portfolio.pdf"
    preview_image: "images/robot/decode-portfolio-preview.jpg"

- name: "Into The Deep"
  year: "2024-2025 — Rookie Year"
  current: false
  image: "images/robot/into-the-deep.jpg"
  overview: "Our rookie season saw rapid evolution across three major robot iterations — from a basic starter bot with no custom parts, to a fully original 3D-printed design, to an offseason bot that was fully CADed in OnShape with belt-driven mecanum."
  description: "First Competition:\n• Used no custom parts (no 3D prints or laser cuts)\n• Simple drivetrain design\n• Gear-driven mecanum drive\n• Experienced weight imbalance and stability issues\n\nSecond Competition:\n• Fully original, 3D-printed design\n• Gear-driven mecanum with lower-centered motors\n• Improved performance, minor weight imbalance\n• Design significantly different from the starter bot\n\nSummer Bot:\n• Offseason robot, fully CADed in OnShape\n• Custom 3D-printed and laser-cut parts\n• Belt-driven mecanum with low-centered motors\n• Stable and well-balanced, even with slides"
  specs:
    - label: "Comp 1 Drivetrain"
      value: "Gear-driven mecanum, no custom parts"
    - label: "Comp 2 Drivetrain"
      value: "Gear-driven mecanum with lower-centered motors, fully 3D-printed"
    - label: "Summer Bot Drivetrain"
      value: "Belt-driven mecanum with low-centered motors, fully CADed"
    - label: "Programming"
      value: "Java"
  gallery:
    - image: "images/robot/2024-2025/robot1.jpg"
      caption: "Competition 1 robot"
    - image: "images/robot/2024-2025/robot2.jpg"
      caption: "Competition 2 robot"
    - image: "images/robot/2024-2025/robot3.png"
      caption: "Summer bot"
  cad:
    enable: false
    label: "View CAD"
    link: ""
  portfolio:
    enable: false
    label: "Download Portfolio"
    file: ""
    preview_image: ""
---