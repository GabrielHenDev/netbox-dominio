from netbox.plugins import PluginConfig

from .version import __version__


class DominoConfig(PluginConfig):
    name = "netbox_domino"
    verbose_name = "Domínio"
    description = "Gerencie domínios, IPs e metadados básicos diretamente no NetBox."
    version = __version__
    author = "Gestão Domínio"
    base_url = "domino"
    author_email = "contato@gestaodomino.local"
    required_settings = []
    default_settings = {}
    min_version = "4.4.0"
    max_version = "4.4.99"


config = DominoConfig
