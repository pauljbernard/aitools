# LangChain Tool Repository

This repository contains the tool definitions used by the **Simple LangChain Factory** proof of concept. The FastAPI service reads the contents of this repository to build conversational agents on demand.

## How the Service Uses These Tools

1. **Tool Discovery**: Each tool lives in a versioned folder under `tools/` and includes a `tool_manifest.json` file describing the function. The service scans the repository for these manifests.
2. **Vector Store Indexing**: Tool descriptions are converted into LangChain documents and indexed using a FAISS vector store with OpenAI embeddings. This allows the service to select tools related to a user's request.
3. **Agent Construction**: Relevant tools are wrapped as `SerializableTool` objects and loaded into a LangChain agent. The agent code and metadata can be returned or executed depending on the user's query.
4. **Session Interaction**: Users start a session via the FastAPI endpoints and can send messages. Responses are streamed token by token while the session remains active.

This repository only contains the tool code; the FastAPI application is kept in a separate project but expects the same directory structure when mounting this repository.

## Adding or Updating Tools

1. Create a new folder inside `tools/` using the pattern `<tool-name>-<version>`. For example, `my-tool-1.0`.
2. Inside the folder, place the Python source file that implements the tool function.
3. Add a `tool_manifest.json` describing the tool. The manifest must include at least:
   - `name`: human‑friendly name of the tool.
   - `description`: short description used for semantic search.
   - `source_file`: relative path to the Python file.
   - `usage_instructions`, `tags`, and any input schema notes.
4. Keep each version of a tool in its own folder. Updating a tool means creating a new versioned directory.
5. Commit the folder and manifest to the repository. After deploying the FastAPI service, restart it so the new tool can be indexed.

The existing `simple-calculator-1.0` folder shows a minimal example.

## Repository Maintenance

- Keep the repository history clean by providing clear commit messages for each new tool or update.
- Avoid large binaries or data files; only lightweight Python code and manifest files are needed.
- If removing tools, delete both the versioned folder and any references in documentation.
- Run any unit tests associated with tool functions before committing.

This structure lets the LangChain Factory service dynamically load and combine tools without requiring code changes in the service itself.
