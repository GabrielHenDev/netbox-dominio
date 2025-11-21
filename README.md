# NetBox Domino Plugin

NetBox Domino é um plugin simples para [NetBox](https://github.com/netbox-community/netbox) que adiciona um modelo de **Domínio**.  
Cada domínio armazena:

- Nome (`example.com.br`)
- Endereço IP (IPv4 ou IPv6)
- Descrição livre
- Tenant associado
- Tags nativas do NetBox

Assim você mantém o inventário de domínios próximo dos demais ativos, sem depender de planilhas ou automações externas.

## Compatibilidade

| Versão do plugin | NetBox |
| ---------------- | ------ |
| 0.1.x            | 4.4.x  |

## Instalação

1. Ative o virtualenv do NetBox (quando aplicável):

   ```bash
   source /opt/netbox/venv/bin/activate
   ```

2. Instale o pacote:

   ```bash
   pip install netbox-domino
   ```

3. Habilite o plugin em `netbox/netbox/configuration.py`:

   ```python
   PLUGINS = [
       "netbox_domino",
       # ... outros plugins
   ]
   ```

4. Reinicie o NetBox e acrescente `netbox-domino` no `local_requirements.txt`.

## Uso

Após habilitar o plugin, um novo menu **Domínios** aparece em *Plugins*.  
De lá é possível:

- Criar, visualizar, editar e remover domínios
- Filtrar por nome, IP, tenant ou tags
- Importar domínios em lote via CSV
- Aplicar ações em massa (edição ou exclusão)
- Consumir/gerar dados via API REST (`/api/plugins/domino/domains/`)

## Campos suportados

| Campo        | Tipo            | Descrição                                                |
| ------------ | --------------- | -------------------------------------------------------- |
| `name`       | Texto (único)   | Nome completo do domínio.                                |
| `ip_address` | IP              | IPv4/IPv6 vinculado.                                     |
| `tenant`     | FK opcional     | Referência a `tenancy.Tenant`.                           |
| `description`| Texto longo     | Observações diversas.                                    |
| `tags`       | Many-to-many    | Tags padrão do NetBox (em formulários e via API).        |

### Importação CSV

O formulário de importação aceita colunas `name`, `ip_address`, `tenant` (nome do tenant) e `description`.  
As tags podem ser enviadas usando o formato padrão do NetBox (`tag1,tag2`).

### API

O endpoint REST segue o mesmo padrão dos objetos nativos:

```
GET  /api/plugins/domino/domains/
POST /api/plugins/domino/domains/
```

Os filtros disponíveis incluem `name`, `ip_address`, `tenant_id`, `tenant`, `tag` e `q`.

## Desenvolvimento

- O diretório `develop/` contém uma stack Docker de laboratório com NetBox já configurado para carregar o plugin a partir do código local.
- `Makefile` expõe alvos para rodar lint, testes e build do pacote.

Pull requests são bem-vindos! Abra também um issue para sugerir novos campos ou integrações.
