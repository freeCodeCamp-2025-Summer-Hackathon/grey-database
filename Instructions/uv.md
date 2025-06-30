# UV Package Manager Guide

UV is a fast Python package installer and dependency resolver, written in Rust. It's designed to be a drop-in replacement for pip and pip-tools with significantly better performance.

## Table of Contents
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Key Features](#key-features)
- [Common Commands](#common-commands)
- [Project Setup](#project-setup)
- [Virtual Environments](#virtual-environments)
- [Documentation Links](#documentation-links)
- [Tutorials](#tutorials)

## Installation

### Linux/macOS (Recommended)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Using pip
```bash
pip install uv
```

### Using Homebrew (macOS)
```bash
brew install uv
```

### Using Conda
```bash
conda install -c conda-forge uv
```

## Basic Usage

### Adding Dependencies
```bash
# Add a package to your project
uv add package-name

# Add with specific version
uv add "django>=4.0,<5.0"

# Add development dependency
uv add --dev pytest

# Add optional dependency group
uv add --optional docs sphinx
```

### Installing and Syncing
```bash
# Install all dependencies from lockfile
uv sync

# Install including development dependencies
uv sync --dev

# Install specific groups
uv sync --group docs
```

## Key Features

- **Speed**: 10-100x faster than pip
- **Drop-in replacement**: Works with existing pip workflows
- **Better dependency resolution**: Resolves conflicts more efficiently
- **Lockfile support**: Generates lock files for reproducible builds
- **Virtual environment management**: Built-in venv support

## Common Commands

### Project Management
```bash
# Initialize new project
uv init

# Add dependencies
uv add requests fastapi

# Add development dependencies
uv add --dev pytest black ruff

# Remove dependencies
uv remove package-name

# Update dependencies
uv lock --upgrade

# Install/sync all dependencies
uv sync
```

### Running Commands
```bash
# Run Python script
uv run main.py

# Run with specific arguments
uv run python -m pytest

# Run in project environment
uv run --python 3.11 script.py
```

## Project Setup

### Initialize a New Project
```bash
# Create a new project directory
mkdir my-project
cd my-project

# Initialize with pyproject.toml
uv init

# Add dependencies
uv add requests
uv add --dev pytest
```

### Working with pyproject.toml
```toml
[project]
name = "my-project"
version = "0.1.0"
dependencies = [
    "requests>=2.28.0",
    "fastapi>=0.68.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0",
    "black>=22.0",
    "flake8>=4.0",
]
```

## Virtual Environments

### Automatic Environment Management
```bash
# uv automatically creates and manages virtual environments
# No need to manually create or activate them!

# Run commands in project environment
uv run python script.py
uv run pytest
uv run black .

# Sync dependencies (auto-creates venv if needed)
uv sync
```

### Manual Environment Control (Optional)
```bash
# Create virtual environment manually
uv venv

# Create with specific Python version
uv venv --python 3.11

# Activate manually (if needed)
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate    # Windows
```

## Important Notes

### Why Use UV?
1. **Performance**: Significantly faster package installation and dependency resolution
2. **Reliability**: Better conflict resolution and error handling
3. **Compatibility**: Drop-in replacement for pip with improved features
4. **Modern tooling**: Built with modern Python packaging standards in mind

### Migration from pip
- Replace `pip install package` with `uv add package`
- Replace `pip install -r requirements.txt` with `uv sync`
- No need to manually manage virtual environments
- `pyproject.toml` replaces `requirements.txt`
- `uv.lock` ensures reproducible installs

### Best Practices
- Use `uv init` to start new projects
- Use `uv add` to add dependencies
- Use `uv sync` to install dependencies
- Use `uv run` to execute scripts
- Commit `uv.lock` for reproducible builds
- Use dependency groups for organization

## Documentation Links

- **Official Documentation**: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)
- **GitHub Repository**: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
- **Installation Guide**: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)
- **User Guide**: [https://docs.astral.sh/uv/concepts/](https://docs.astral.sh/uv/concepts/)
- **API Reference**: [https://docs.astral.sh/uv/reference/](https://docs.astral.sh/uv/reference/)

## Tutorials

### Video Tutorials
- **Tech With Tim - UV Tutorial**: [Python's New Package Manager is FAST](https://www.youtube.com/watch?v=8UuW8o4bHbw)
- **Tech With Tim - Advanced UV**: [Advanced UV Package Management](https://www.youtube.com/results?search_query=tech+with+tim+uv+python)

### Written Tutorials
- **Getting Started with UV**: [https://docs.astral.sh/uv/getting-started/](https://docs.astral.sh/uv/getting-started/)
- **Migrating from pip**: [https://docs.astral.sh/uv/pip/](https://docs.astral.sh/uv/pip/)
- **Project Management**: [https://docs.astral.sh/uv/concepts/projects/](https://docs.astral.sh/uv/concepts/projects/)

## Quick Start Example

```bash
# 1. Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Create a new project
mkdir my-app && cd my-app

# 3. Initialize project
uv init

# 4. Add dependencies
uv add requests fastapi

# 5. Add development dependencies
uv add --dev pytest black ruff

# 6. Install all dependencies
uv sync

# 7. Run your application
uv run python main.py

# 8. Run tests
uv run pytest
```

## Troubleshooting

### Common Issues
- **Permission errors**: Use `--user` flag or virtual environments
- **Network issues**: Configure proxy settings if behind corporate firewall
- **Version conflicts**: Use `uv pip compile` to resolve dependencies

### Getting Help
```bash
# Show help
uv --help
uv add --help
uv sync --help

# Check version
uv --version

# Verbose output for debugging
uv add package-name --verbose
```

---

**Note**: UV is actively developed and new features are regularly added. Check the official documentation for the latest updates and best practices.