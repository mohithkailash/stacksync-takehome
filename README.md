# StackSync Take-Home Project

## Description

This project provides a secure Python script execution service. The service allows users to submit Python scripts through an API endpoint and returns the result of the `main()` function as output. The scripts are executed in a secure sandbox environment using `nsjail`.

## Features

- **Secure Execution**: Uses `nsjail` to sandbox and safely execute user-provided Python scripts.
- **API Endpoint**: Provides a RESTful API for submitting and executing Python scripts.
- **Resource Limits**: Configured to enforce memory, CPU, and file size limits to prevent abuse.

## Setup and Installation

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [Git](https://git-scm.com/)

### Clone the Repository

```bash
git clone git@github.com:mohithkailash/stacksync-takehome.git
cd stacksync-takehome
