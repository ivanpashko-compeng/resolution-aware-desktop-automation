# Resolution-Aware Desktop Automation

A configurable Python desktop automation tool for executing coordinate-based, multi-stage workflows. The project supports external configuration files, object-oriented execution, keyboard interruption, and coordinate scaling across 16:9 display resolutions.

This project was developed as an educational exercise in Python automation using a fixed-layout game interface as its initial test environment.

## Features

- Class-based Python architecture
- Configurable coordinates and deployment sequences
- Resolution-aware scaling
- Support for 2560×1440 and 1920×1080 displays
- Multi-stage workflow execution
- Repeated automation cycles
- Escape-key interruption
- PyAutoGUI fail-safe support
- External configuration files separated from program logic

## Project Structure

```text
resolution-aware-desktop-automation/
├── desktop_automation.py
├── run_automation.py
├── config/
│   ├── coordinateslist.csv
│   ├── troopdeployment.csv
│   ├── menubuttons.csv
│   └── eventdeployment.csv
├── requirements.txt
└── README.md
