# Documentação rápida

Este diretório guarda notas curtas para operação e desenvolvimento do **NetBox Domino**.

## Modelagem

| Campo        | Tipo                      | Observações                                    |
| ------------ | ------------------------- | -----------------------------------------------|
| `name`       | `CharField(max_length=255)` único. | Nome do domínio (ex.: `dominio.com.br`). |
| `ip_address` | `net.fields.IPAddressField` opcional. | IPv4 ou IPv6.                        |
| `tenant`     | FK opcional para `tenancy.Tenant`. | Mantém o vínculo organizacional.     |
| `description`| `TextField` opcional.     | Espaço livre para observações.                 |
| `tags`       | `TaggableManager`.        | Tags padrão do NetBox.                          |

## Funcionalidades prontas

- Views CRUD com componentes genéricos do NetBox
- Importação CSV, bulk edit/delete
- Endpoint REST `/api/plugins/domino/domains/`
- Filtros: texto livre (`q`), `name`, `ip_address`, `tenant_id`, `tenant`, `tag`

## Como testar com Docker (diretório `develop/`)

1. Copie `dev.env.example` (caso exista) ou edite `dev.env`.
2. Suba o ambiente:

   ```bash
   docker compose up --build
   ```

3. Acesse `http://localhost:8080` (usuário padrão: `admin` / `admin`)*.

\* Ajuste conforme seu arquivo `.env`.

## Roadmap curto

- Campos adicionais (TTL, registrante, status de apontamento)
- Bulk export pré-formatado
- Privilégios/grupos dedicados
