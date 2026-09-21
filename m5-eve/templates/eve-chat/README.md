# Eve chat template deployment profile

This guide maps the upstream [Vercel Eve Chat Template](https://github.com/vercel/eve/tree/main/apps/templates/eve-chat-template) to the M5 Eve Member Workspace architecture. The upstream project is licensed under Apache License 2.0. This repository links to it and does not vendor its source code.

## One-click operator preview

The upstream [deploy flow](https://vercel.com/new/clone?clone-source=ai-gateway-empty-state&demo-description=A+persisted+Next.js+chat+template+for+eve%2C+built+with+shadcn%2Fui%2C+Tailwind+CSS%2C+Streamdown%2C+Better+Auth%2C+Drizzle%2C+and+Neon.&demo-title=eve+Chat+Template&demo-url=https%3A%2F%2Fchat.eve.dev&env=EVE_CHAT_PASSWORD&envDescription=Choose+a+strong+password+to+protect+your+agent+%2816%2B+characters+recommended%29.&envLink=https%3A%2F%2Fgithub.com%2Fvercel%2Feve%2Fblob%2Fmain%2Fapps%2Ftemplates%2Feve-chat-template%2Fdocs%2Fsetup-and-deploy.md&from=templates&project-name=eve+Chat+Template&repository-name=eve-chat-template&repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Feve%2Ftree%2Fmain%2Fapps%2Ftemplates%2Feve-chat-template) asks for one variable:

```text
EVE_CHAT_PASSWORD
```

Use a unique 16+ character value stored in a password manager. Do not reuse an AI provider/API key. Starter mode is one trusted operator: all password holders share the same Eve principal, browser-local history, and connection grants. It is not suitable for BOM member rollout.

## Production multi-user environment

The upstream template requires the complete production set before production mode takes precedence:

```text
DATABASE_URL
BETTER_AUTH_SECRET
NEXT_PUBLIC_VERCEL_APP_CLIENT_ID
VERCEL_APP_CLIENT_SECRET
UPSTASH_REDIS_REST_URL
UPSTASH_REDIS_REST_TOKEN
KV_REST_API_URL
KV_REST_API_TOKEN
```

Optional:

```text
EVE_MEMORY_BLOB_STORE_ID
EVE_MEMORY_BLOB_WEBHOOK_PUBLIC_KEY
BETTER_AUTH_URL
SLACK_CONNECTOR
LINEAR_CONNECTOR
NOTION_CONNECTOR
SENTRY_CONNECTOR
```

Use the upstream [`setup.sh`](https://github.com/vercel/eve/blob/main/apps/templates/eve-chat-template/scripts/setup.sh) after linking the application repository to Vercel. It can provision private Blob memory, Neon, Upstash, Better Auth, and Sign in with Vercel. Review all generated resources, scopes, callback URLs, environment targets, costs, and retention settings.

## M5 additions required before member access

The template's production mode supplies application users, not M5 standing. A member deployment additionally requires:

- verified principal binding;
- approved BOM/BOU/BOB/BOI/BOG context grants;
- explicit capability delegation;
- M5Canon or equivalent deterministic preflight;
- server-side tenant filtering;
- per-context consent, memory, and connector policy;
- human approval for consequential actions;
- evidence receipts, correction, revocation, and incident controls; and
- an accountable operator and data controller.

Do not copy secrets into this repository, chat messages, build logs, screenshots, issues, or pull requests. `.env.local` must remain ignored. Rotate any secret exposed in chat or terminal command history.

## Forking and attribution

If an implementation copies or modifies upstream code:

1. preserve the Apache-2.0 license and applicable notices;
2. mark modified files as changed;
3. use M5/TitleChain names only under the repository's trademark rules;
4. identify the deployment operator separately from Vercel and TitleChain Foundation; and
5. do not imply upstream or Foundation endorsement.

[Back to M5 Eve](../../README.md)
