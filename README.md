# Porygon Pipelines ADK

**AI Agent Development Kit with data exploration capabilities**

A Python-based AI agent framework built with Google Cloud's Agent Development Kit (ADK) that provides BigQuery data exploration capabilities through a conversational interface.

## Architecture

This project implements an AI agent with the following architecture:

- **Root Agent**: Core AI agent powered by Gemini 2.5 Flash model
- **BigQuery Integration**: Secure data exploration tools with read-only access
- **Cloud Deployment**: Vertex AI Agent Engine deployment capabilities
- **Session Management**: Multi-user session handling for conversations
- **Security**: Service account-based authentication with Google Cloud Secret Manager

## 🚀 Features

- **Conversational Data Exploration**: Chat with your BigQuery data using natural language
- **Read-Only Safety**: BigQuery toolset configured with blocked write mode to prevent accidental data modifications
- **Secure Authentication**: Service account credentials with proper OAuth2 scoping
- **Cloud Deployment**: Deploy agents to Google Cloud's Vertex AI platform
- **Session Management**: Create and manage user sessions for persistent conversations
- **Environment Configuration**: Flexible configuration through environment variables

## 📋 Prerequisites

- Python 3.9 or higher
- Google Cloud Project with the following APIs enabled:
  - Vertex AI API
  - BigQuery API
  - Secret Manager API
  - Cloud Storage API
- Service account with appropriate permissions
- Poetry for dependency management

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AnaPrec07/porygon-pipelines-adk.git
   cd porygon-pipelines-adk
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` with your configuration:
   ```bash
   GOOGLE_GENAI_USE_VERTEXAI=TRUE
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_CLOUD_STAGING_BUCKET=gs://your-bucket-name
   GOOGLE_CLOUD_LOCATION=us-east4
   ```

5. **Set up service account credentials**:
   - Place your service account JSON file at `config/credentials/service_account.json`
   - Or configure Google Cloud Secret Manager (see Configuration section)

## ⚙️ Configuration

### Service Account Permissions

Your service account needs the following roles:
- `roles/bigquery.user`
- `roles/bigquery.dataViewer`
- `roles/aiplatform.user`
- `roles/secretmanager.secretAccessor` (if using Secret Manager)

### BigQuery Tool Configuration

The BigQuery toolset is configured with:
- **Write Mode**: `BLOCKED` - Prevents any write operations
- **Authentication**: Service account credentials with proper OAuth2 scoping
- **Permissions**: Read-only access to BigQuery datasets

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_CLOUD_PROJECT` | Your GCP project ID | Yes |
| `GOOGLE_CLOUD_LOCATION` | GCP region (e.g., us-east4) | Yes |
| `GOOGLE_CLOUD_STAGING_BUCKET` | GCS bucket for staging | Yes |
| `GOOGLE_GENAI_USE_VERTEXAI` | Use Vertex AI backend | Yes |
| `AGENT_RESOURCE_ID` | Deployed agent resource ID | No |

## 🚀 Usage

### Local Development

To run the agent locally:

```python
from root_agent.agent import root_agent

# The agent is ready to use with BigQuery capabilities
# You can integrate it into your application
```

### Deployment to Vertex AI

Deploy your agent to Google Cloud:

```bash
# Deploy a new agent
poetry run deploy-remote --create \
  --project_id your-project-id \
  --location us-east4 \
  --bucket gs://your-bucket-name

# List existing deployments
poetry run deploy-remote --list

# Delete a deployment
poetry run deploy-remote --delete --resource_id your-resource-id
```

### Session Management

Create and manage user sessions:

```bash
# Create a new session
poetry run deploy-remote --create_session \
  --resource_id your-resource-id \
  --user_id test_user

# List sessions for a user
poetry run deploy-remote --list_sessions \
  --resource_id your-resource-id \
  --user_id test_user

# Send a message to the agent
poetry run deploy-remote --send \
  --resource_id your-resource-id \
  --user_id test_user \
  --session_id your-session-id \
  --message "Show me the top 10 rows from my dataset"
```

## 📁 Project Structure

```
porygon-pipelines-adk/
├── root_agent/                 # Core agent implementation
│   ├── agent.py               # Main agent definition
│   └── tools/                 # Agent tools
│       └── bigquery.py        # BigQuery integration
├── deployment/                # Deployment utilities
│   └── remote.py              # Vertex AI deployment script
├── utils/                     # Utility modules
│   └── secret_manager.py      # Google Cloud Secret Manager integration
├── config/                    # Configuration files
│   └── credentials/           # Service account credentials
├── docs/                      # Documentation
├── pyproject.toml             # Poetry configuration
├── .env.example               # Environment template
└── README.md                  # This file
```

## 🔐 Security

- **Read-Only Access**: BigQuery toolset configured with `WriteMode.BLOCKED`
- **Service Account Authentication**: Secure credential management
- **Scoped Permissions**: Minimal required OAuth2 scopes
- **Secret Management**: Optional integration with Google Cloud Secret Manager

## 🧪 Development

### Code Quality Tools

This project includes development tools configured in `pyproject.toml`:

- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Linting
- **mypy**: Type checking

Run code quality checks:

```bash
# Format code
poetry run black .

# Lint code
poetry run flake8 .

# Type checking
poetry run mypy .

# Run tests
poetry run pytest
```

## 📚 Dependencies

### Core Dependencies
- `google-adk`: Google Agent Development Kit
- `google-cloud-bigquery`: BigQuery client library
- `google-cloud-secret-manager`: Secret Manager integration
- `google-generativeai`: Generative AI capabilities
- `flask`: Web framework for API endpoints

### Development Dependencies
- `pytest`: Testing framework
- `black`: Code formatter
- `flake8`: Code linter
- `mypy`: Type checker

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in this repository
- Check the [Google Cloud ADK documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)
- Review the [BigQuery documentation](https://cloud.google.com/bigquery/docs)

## 🏷️ Version

Current version: 0.1.0

---

Built with ❤️ using Google Cloud's Agent Development Kit