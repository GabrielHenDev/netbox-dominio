from netbox.plugins import PluginMenuButton, PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_domino:domain_list",
        link_text="Domínios",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_domino:domain_add",
                link_text="Adicionar",
                icon_class="mdi mdi-plus-thick",
                color="success",
            ),
            PluginMenuButton(
                link="plugins:netbox_domino:domain_import",
                link_text="Importar",
                icon_class="mdi mdi-database-import",
            ),
        ),
    ),
)
