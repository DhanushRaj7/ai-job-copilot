# Security Policy

## Reporting a vulnerability

If you discover a security issue — especially anything involving **API keys, secret handling, or the code that constructs prompts/tool calls** — please report it privately rather than opening a public issue.

- **Email:** dhraj777@gmail.com
- Use the subject line `SECURITY: ai-job-copilot`
- Include: a description, steps to reproduce, and the potential impact.

Please give a reasonable window to respond before any public disclosure. I'll acknowledge within a few days and keep you updated on the fix.

## Scope & good practices for this project

Because this project integrates with LLM providers and external job APIs, keep these in mind:

- **Never commit secrets.** API keys live in `.env`, which is git-ignored. Use `.env.example` as the template.
- **Treat model output as untrusted.** Don't `eval`/execute LLM output; validate structured output before acting on it.
- **Be mindful of prompt injection.** Job listings are external, untrusted text — don't let listing content silently override system instructions.
- **Rate-limit and validate** external API responses.

## Supported versions

This is an early-stage project under active development; security fixes are applied to the `main` branch.
