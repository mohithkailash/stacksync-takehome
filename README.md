# StackSync Take-Home Project

## Description

This project provides a secure Python script execution service. The service allows users to submit Python scripts through an API endpoint and returns the result of the `main()` function as output. The scripts are executed in a secure sandbox environment using `nsjail`.

## Features

- **Secure Execution**: Uses `nsjail` to sandbox and safely execute user-provided Python scripts.
- **API Endpoint**: Provides a RESTful API for submitting and executing Python scripts.
- **Resource Limits**: Configured to enforce memory, CPU, and file size limits to prevent abuse.

### Example cURL Request



```bash
curl -X POST "https://python-script-executor-bsze2rjrca-uc.a.run.app/execute" \
     -H "Content-Type: application/json" \
     -d '{"script": "def main():\n    return {\"message\": \"Hello, World!\"}\n\nif __name__ == \"__main__\":\n    import json\n    print(json.dumps(main()))"}'
```

```bash
curl -X POST "https://python-script-executor-bsze2rjrca-uc.a.run.app/execute" \
     -H "Content-Type: application/json" \
     -d '{"script": "import json\n\nclass Calculator:\n    def __init__(self, a, b):\n        self.a = a\n        self.b = b\n\n    def add(self):\n        return self.a + self.b\n\n    def subtract(self):\n        return self.a - self.b\n\n    def multiply(self):\n        return self.a * self.b\n\n    def divide(self):\n        try:\n            return self.a / self.b\n        except ZeroDivisionError:\n            return \"Error: Division by zero\"\n\ndef main():\n    calc = Calculator(10, 5)\n    result = {\n        \"addition\": calc.add(),\n        \"subtraction\": calc.subtract(),\n        \"multiplication\": calc.multiply(),\n        \"division\": calc.divide()\n    }\n    return result\n\nif __name__ == \"__main__\":\n    print(json.dumps(main()))"}'

```

## Setup and Installation

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [Git](https://git-scm.com/)

### Clone the Repository

```bash
git clone git@github.com:mohithkailash/stacksync-takehome.git
cd stacksync-takehome
```
